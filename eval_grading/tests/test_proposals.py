import unittest
from pathlib import Path
from eval_grading.app import core
from eval_grading.app.rubric import EXERCISES, NORMAL, MOBIT

CONTENT=Path(__file__).resolve().parents[2]/'content'/'02-Hoofdstuk 2 - Selectie'/'7-Evaluatie'

class ProposalCalibration(unittest.TestCase):
    def proposal(self,slug,code,status='wrong'):
        _,title,folder,topic=next(e for e in EXERCISES if e[0]==slug)
        tests,_=core.tests_for(CONTENT,folder)
        return core.proposal(code,status,title,topic,MOBIT if slug=='mobit' else NORMAL,tests,slug=='taille-heup')

    def test_all_reference_solutions(self):
        for slug,_,folder,_ in EXERCISES:
            with self.subTest(exercise=slug):
                code=(CONTENT/folder/'solution'/'solution.nl.py').read_text()
                diag,criteria,_=self.proposal(slug,code,'correct')
                self.assertEqual(sum(c['points'] or 0 for c in criteria.values()),2 if slug=='mobit' else 5)
                self.assertEqual(diag['math_probes']['passed'],diag['math_probes']['tested'])

    def test_conditional_else_is_partial_and_keeps_other_marks_unknown(self):
        for slug, maximum in [('leeftijd-hond', 1), ('mobit', .25)]:
            for condition in ['age > 2', '(age > 2)']:
                code = f'age=int(input())\nif age == 1:\n    print(1)\nelse {condition}:\n    print(2)\n'
                diag, criteria, feedback = self.proposal(slug, code, 'compilation error')
                self.assertTrue(diag['conditional_else'])
                self.assertEqual(diag['conditional_else_lines'], [4])
                self.assertEqual(criteria['programmeerconcepten']['points'], maximum)
                self.assertIn('Achter else komt geen voorwaarde.', criteria['programmeerconcepten']['rationale'])
                self.assertEqual(criteria['functioneel']['points'], 0)
                self.assertIsNone(criteria['leesbaarheid']['points'])
                self.assertIsNone(criteria['wiskundeconcepten']['points'])
                self.assertEqual(set(feedback), {'strength', 'improve'})

    def test_else_detection_ignores_comments_and_strings(self):
        from eval_grading.app.proposals import conditional_else
        for code in ['# else age > 2:\nif True:\n    pass\nelse: # age > 2\n    pass',
                     'text = "else age > 2:"\nif True:\n    pass\nelif False:\n    pass']:
            self.assertEqual(conditional_else(code)[0], [])
        diag, criteria, feedback = self.proposal('colruyt', 'if True print(1)', 'compilation error')
        self.assertFalse(diag['conditional_else'])
        self.assertIsNone(criteria['programmeerconcepten']['points'])
        self.assertNotIn('geen aangetroffen', str(criteria))
        self.assertEqual(set(feedback), {'strength', 'improve'})

    def test_requested_positive_language(self):
        _, _, folder, _ = next(e for e in EXERCISES if e[0] == 'leeftijd-hond')
        code = (CONTENT/folder/'solution'/'solution.nl.py').read_text()
        _, criteria, feedback = self.proposal('leeftijd-hond', code, 'correct')
        self.assertEqual(criteria['leesbaarheid']['rationale'], 'De gebruikte namen zijn passend en duidelijk.')
        self.assertIn('Je gebruikt een correct datatype voor je invoer.', criteria['programmeerconcepten']['rationale'])
        self.assertEqual(set(feedback), {'strength', 'improve'})

    def test_valid_ternary_is_not_mistaken_for_conditional_else(self):
        from eval_grading.app.proposals import conditional_else
        for code in ['answer = 1 if True else 2\nif False print(0)',
                     'answer = (1 if True\n          else 2)\nif False print(0)',
                     'if True:\n    pass\nelse\n    print(2)']:
            self.assertEqual(conditional_else(code)[0],[])

    def test_wrong_output_does_not_erase_concepts(self):
        code='leeftijd=int(input())\nif leeftijd==1:\n    mensen=15\nelif leeftijd==2:\n    mensen=24\nelse:\n    mensen=24+(leeftijd-2)*5\nprint("Antwoord:",mensen)\n'
        _,criteria,_=self.proposal('leeftijd-hond',code)
        self.assertEqual(criteria['functioneel']['points'],0)
        self.assertEqual(criteria['programmeerconcepten']['points'],2)
        self.assertEqual(criteria['wiskundeconcepten']['points'],1)

    def test_wrong_formula_receives_only_partial_math(self):
        code='leeftijd=int(input())\nif leeftijd==1:\n    mensen=15\nelif leeftijd==2:\n    mensen=24\nelse:\n    mensen=24+leeftijd*5\nprint(mensen)\n'
        _,criteria,_=self.proposal('leeftijd-hond',code)
        self.assertEqual(criteria['programmeerconcepten']['points'],2)
        self.assertEqual(criteria['wiskundeconcepten']['points'],.5)

    def test_unrelated_values_and_runtime_failures_are_not_math_proof(self):
        for code in ['bedrag=3.29*1\nprint(1/0)', 'bedrag=3.29*1\nprint(0)', 'bedrag=1+2\nprint(3.29,0)']:
            with self.subTest(code=code):
                _,criteria,_=self.proposal('colruyt',code)
                self.assertIn(criteria['wiskundeconcepten']['points'],(0,None))

    def test_unsupported_stays_pending(self):
        _,criteria,_=self.proposal('colruyt','import statistics\naantal=int(input())\nprint(statistics.mean([aantal]))')
        self.assertIsNone(criteria['wiskundeconcepten']['points'])

    def test_dead_and_overwritten_calculations_do_not_count(self):
        for code in ['if False:\n    print(1+1)\nprint(3.29)',
                     'bedrag=1*3.29\nbedrag=3.29\nprint(bedrag)']:
            _,criteria,_=self.proposal('colruyt',code)
            self.assertEqual(criteria['wiskundeconcepten']['points'],0)

if __name__=='__main__': unittest.main()
