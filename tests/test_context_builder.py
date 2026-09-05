from pathlib import Path
import sys,unittest
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from validtec_track2.context_builder import build_context_packet,load_registry
class ContextBuilderTests(unittest.TestCase):
    def test_filters_expired_and_untrusted(self):
        p=build_context_packet(load_registry(ROOT/"context/source-registry.json"),{"onboarding","authorization"},2000)
        self.assertNotIn("OLD-999",p["source_ids"]); self.assertNotIn("USR-777",p["source_ids"]); self.assertIn("REQ-101",p["source_ids"]); self.assertIn("REQ-102",p["source_ids"])
    def test_respects_budget(self):
        p=build_context_packet(load_registry(ROOT/"context/source-registry.json"),{"onboarding","authorization","release"},500)
        self.assertLessEqual(p["characters_used"],500)
if __name__=="__main__": unittest.main()
