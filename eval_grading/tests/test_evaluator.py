import unittest
from eval_grading.app.evaluator import run
class EvaluatorTests(unittest.TestCase):
    def test_subset(self):
        code='from math import ceil\nx = float(input("Geef: "))\ny: int = ceil(x / 20)\nif y > 2:\n    y += 1\nprint(f"Blokken: {y}")\n'
        self.assertEqual(run(code,'41')['output'],'Blokken: 4\n')
    def test_denial_and_bounds(self):
        for code in ['import os', '__import__("os")', 'while True: pass', 'print((1).__class__)', 'if False:\n open("x")', 'print(10 ** 1000)', 'print("a" * 1000000000)']:
            self.assertNotEqual(run(code)['state'],'ok',code)
        for code in ['print((1,) * 1000000000000)', 'print("%1000000000000s" % "a")']:
            self.assertEqual(run(code)['state'],'unsupported')
        self.assertEqual(run('print = 1\nprint("ok")')['state'],'unsupported')
if __name__=='__main__': unittest.main()
