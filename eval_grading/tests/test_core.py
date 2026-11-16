import copy
import csv
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
from eval_grading.app.core import intake, load, save_review, totals, is_approved
from eval_grading.app.rubric import EXERCISES

class CoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name); self.content=self.root/'content'; self.ws=self.root/'private'
        for _,_,folder,_ in EXERCISES:
            p=self.content/folder/'evaluation'; p.mkdir(parents=True); (p/'tests.yaml').write_text('- stdin: "1"\n  stdout: "1\\n"\n')
        self.account={'id':'123','username':'synthetic','first_name':'Test','last_name':'Leerling','email':'test@example.test','labels':'3nw1'}
        for _,title,_,_ in EXERCISES:
            self.account[title]='0'; self.account['Status '+title]='unstarted'
        self.account['Colruyt']='0'; self.account['Status Colruyt']='wrong'
        self.record=dict(self.account,filename='source.py',name_nl='Colruyt',exercise_id='1',submission_id='10',created_at='2026-01-01',status='wrong')
        self.score=self.root/'scores.csv'; self.archive=self.root/'input.zip'; self.write_inputs()
    def tearDown(self): self.tmp.cleanup()
    def write_inputs(self, records=None, filename='source.py'):
        def csvbytes(rows):
            f=io.StringIO(newline=''); w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows); return f.getvalue().encode()
        self.score.write_bytes(csvbytes([self.account]))
        with zipfile.ZipFile(self.archive,'w') as z:
            z.writestr('manifest.csv',csvbytes(records or [self.record])); z.writestr(filename,'x = 1\nif x > 0:\n    print(x)\n')
    def intake(self): return intake(self.archive,self.score,self.ws,self.content)
    def test_intake_and_review(self):
        state=self.intake(); student=state['students'][0]
        self.assertEqual(totals(student)['maximum'],27); self.assertEqual(student['exercises'][-1]['criteria']['programmeerconcepten']['max'],.5)
        self.assertEqual(student['exercises'][0]['criteria']['functioneel']['points'],0)
        self.assertEqual(student['exercises'][0]['criteria']['wiskundeconcepten']['points'],0)
        self.assertGreater(student['exercises'][0]['criteria']['programmeerconcepten']['points'],0)
        self.assertEqual(self.intake(),state)
        es=copy.deepcopy(student['exercises'])
        with self.assertRaises(ValueError): save_review(self.ws,student['id'],0,'Docent',es,True,True)
        for e in es:
            for c in e['criteria'].values(): c.update(points=0,checked=True,rationale='Nagezien aan de hand van de bron.')
        result=save_review(self.ws,student['id'],0,'Docent',es,True,True)
        self.assertTrue(is_approved(result))
        with self.assertRaises(ValueError): save_review(self.ws,student['id'],0,'Docent',es)
        es[0]['source']['code']='changed'
        with self.assertRaises(ValueError): save_review(self.ws,student['id'],1,'Docent',es)
        self.assertTrue(is_approved(load(self.ws)['students'][0]))
        self.account['username']='changed'; self.write_inputs()
        with self.assertRaises(ValueError): self.intake()
    def test_duplicate_and_mismatch(self):
        self.write_inputs([self.record,self.record])
        with self.assertRaises(ValueError): self.intake()
        self.record['email']='wrong@example.test'; self.write_inputs()
        with self.assertRaises(ValueError): self.intake()
    def test_traversal(self):
        self.record['filename']='../source.py'; self.write_inputs(filename='../source.py')
        with self.assertRaises(ValueError): self.intake()
    def test_tampered_state(self):
        self.intake(); p=self.ws/'state.json'; state=json.loads(p.read_text()); state['students'][0]['exercises'][0]['diagnostics']['syntax_error_line']=999; p.write_text(json.dumps(state))
        with self.assertRaises(ValueError): load(self.ws)

if __name__=='__main__': unittest.main()
