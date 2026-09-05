from pathlib import Path
import sys,unittest
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from validtec_track2.evaluator import evaluate_fixture
from validtec_track2.promotion_gate import decide_promotion
class PromotionGateTests(unittest.TestCase):
    def setUp(self):
        c=ROOT/"eval/cases/evaluation-cases.json"; self.b=evaluate_fixture(c,ROOT/"eval/fixtures/approved-v1-results.json"); self.good=evaluate_fixture(c,ROOT/"eval/fixtures/candidate-v2-results.json"); self.bad=evaluate_fixture(c,ROOT/"eval/fixtures/candidate-regression-results.json")
    def test_good_promotes(self):
        d=decide_promotion(self.b,self.good); self.assertEqual(d.decision,"PROMOTE"); self.assertGreaterEqual(d.token_reduction_pct,15)
    def test_bad_rolls_back(self):
        d=decide_promotion(self.b,self.bad); self.assertEqual(d.decision,"ROLLBACK"); self.assertTrue(any("critical" in r for r in d.reasons))
if __name__=="__main__": unittest.main()
