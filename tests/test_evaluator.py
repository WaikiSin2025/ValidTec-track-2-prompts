from pathlib import Path
import sys,unittest
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from validtec_track2.evaluator import evaluate_fixture
class EvaluatorTests(unittest.TestCase):
    def setUp(self): self.cases=ROOT/"eval/cases/evaluation-cases.json"
    def test_baseline_passes(self):
        r=evaluate_fixture(self.cases,ROOT/"eval/fixtures/approved-v1-results.json"); self.assertEqual(r.pass_rate,1.0); self.assertEqual(r.critical_failures,[])
    def test_candidate_passes(self):
        r=evaluate_fixture(self.cases,ROOT/"eval/fixtures/candidate-v2-results.json"); self.assertEqual(r.pass_rate,1.0); self.assertEqual(r.critical_failures,[])
    def test_regression_fails(self):
        r=evaluate_fixture(self.cases,ROOT/"eval/fixtures/candidate-regression-results.json"); self.assertLess(r.pass_rate,1.0); self.assertTrue(r.critical_failures)
if __name__=="__main__": unittest.main()
