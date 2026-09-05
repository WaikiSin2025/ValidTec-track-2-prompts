from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/"src"))
from validtec_track2.context_builder import build_context_packet,load_registry
from validtec_track2.evaluator import evaluate_fixture
from validtec_track2.promotion_gate import decide_promotion
from validtec_track2.reporting import markdown_report

def main()->int:
    cases=ROOT/"eval/cases/evaluation-cases.json"
    baseline=evaluate_fixture(cases,ROOT/"eval/fixtures/approved-v1-results.json")
    candidate=evaluate_fixture(cases,ROOT/"eval/fixtures/candidate-v2-results.json")
    decision=decide_promotion(baseline,candidate)
    packet=build_context_packet(load_registry(ROOT/"context/source-registry.json"),{"onboarding","authorization","release"},1200)
    print(f"Baseline: {baseline.prompt_version}")
    print(f"Candidate: {candidate.prompt_version}")
    print(f"Quality pass rate: {baseline.pass_rate:.1%} -> {candidate.pass_rate:.1%}")
    print(f"Estimated tokens: {baseline.estimated_tokens} -> {candidate.estimated_tokens}")
    print(f"Token reduction: {decision.token_reduction_pct:.1f}%")
    print(f"Decision: {decision.decision}")
    print(f"Context packet: {len(packet['source_ids'])} sources, {packet['characters_used']}/{packet['character_budget']} characters")
    art=ROOT/"artifacts"; art.mkdir(exist_ok=True)
    (art/"evaluation-report.md").write_text(markdown_report(baseline,candidate,decision),encoding="utf-8")
    record={"baseline":baseline.as_dict(),"candidate":candidate.as_dict(),"promotion_gate":decision.as_dict(),"context_packet":packet,"human_review":{"required":True,"status":"pending-demo-review"}}
    (art/"run-record.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
    return 0 if decision.decision=="PROMOTE" else 1
if __name__=="__main__": raise SystemExit(main())
