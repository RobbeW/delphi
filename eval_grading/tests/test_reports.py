import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from eval_grading.app import reports

def sample():
    return {'id':'synthetic','name':'Voorbeeld Leerling','class_name':'3NW','revision':0,'approved_revision':None,'attested':False,'exercises':[{'id':('mobit' if i==5 else str(i)),'title':'Oefening '+str(i),'criteria':{k:{'max':(.5 if i==5 else m),'points':None,'rationale':'Nog te beoordelen op basis van de oplossing.','checked':False} for k,m in [('functioneel',1),('leesbaarheid',1),('programmeerconcepten',2),('wiskundeconcepten',1)]},'feedback':{'strength':'Een aanzet is aanwezig.','improve':'Controleer de berekening.'}} for i in range(6)]}
class ReportsTest(unittest.TestCase):
    def test_pdf_pending_and_final_guard(self):
        from pypdf import PdfReader
        s=sample()
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'feedback.pdf'; reports.build_pdf(s,path)
            text=' '.join(page.extract_text() for page in PdfReader(path).pages)
            self.assertIn('Voorlopige beoordeling',text); self.assertIn('Open',text); self.assertIn('0 - 27 / 27',text); self.assertIn('Oefening 5',text)
            self.assertNotIn('Oefenen',text)
            with self.assertRaises(ValueError): reports.build_pdf(s,path,True)
    def test_exports_exclude_unapproved(self):
        s=sample()
        with patch.object(reports.core,'load',return_value={'students':[s]}):
            self.assertNotIn(b'Voorbeeld',reports.teacher_csv('/tmp'))
    def test_long_teacher_feedback_remains_complete(self):
        from pypdf import PdfReader
        s=sample();s['exercises'][0]['criteria']['leesbaarheid']['rationale']=('Controleer de structuur van je oplossing. '*100)+'UNIEK_EINDE'
        s['exercises'][0]['feedback']['improve']='Werk één onderdeel per keer uit. '*80
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'long.pdf';reports.build_pdf(s,path)
            text=' '.join(page.extract_text() for page in PdfReader(path).pages)
            self.assertIn('UNIEK_EINDE',text);self.assertIn('Oefening 5',text)
if __name__=='__main__': unittest.main()
