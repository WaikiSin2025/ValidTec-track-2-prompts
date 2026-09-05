from __future__ import annotations
import json
from dataclasses import dataclass,asdict
from pathlib import Path
REQUIRED_FIELDS={"case_id","summary","risks","test_scenarios","evidence_ids","unknowns","decision"}
@dataclass
class CaseResult:
    case_id:str; passed:bool; critical:bool; failures:list[str]
@dataclass
class EvaluationResult:
    prompt_version:str; estimated_tokens:int; passed_cases:int; total_cases:int; pass_rate:float; critical_failures:list[str]; cases:list[CaseResult]
    def as_dict(self)->dict:
        d=asdict(self); d["cases"]=[asdict(c) for c in self.cases]; return d

def load_json(path:str|Path)->dict: return json.loads(Path(path).read_text(encoding="utf-8"))

def evaluate_fixture(cases_path:str|Path, fixture_path:str|Path)->EvaluationResult:
    defs={c["id"]:c for c in load_json(cases_path)["cases"]}; fixture=load_json(fixture_path); outputs={o.get("case_id"):o for o in fixture["outputs"]}; results=[]
    for cid,case in defs.items():
        f=[]; out=outputs.get(cid)
        if out is None: f.append("missing output")
        else:
            missing=REQUIRED_FIELDS-set(out)
            if missing: f.append("missing required fields: "+", ".join(sorted(missing)))
            if out.get("decision")!=case.get("expected_decision"): f.append(f'decision {out.get("decision")!r} != {case.get("expected_decision")!r}')
            missing_risks=set(case.get("required_risks",[]))-set(out.get("risks",[]))
            if missing_risks: f.append("missing risks: "+", ".join(sorted(missing_risks)))
            supplied=set(out.get("evidence_ids",[])); allowed=set(case.get("allowed_evidence",[])); disallowed=supplied-allowed
            if disallowed: f.append("disallowed evidence: "+", ".join(sorted(disallowed)))
            forbidden=supplied & set(case.get("forbidden_evidence",[]))
            if forbidden: f.append("forbidden evidence used: "+", ".join(sorted(forbidden)))
            if out.get("decision")=="needs_context" and not out.get("unknowns"): f.append("needs_context output must explain unknowns")
            for sc in out.get("test_scenarios",[]):
                for fld in ("id","risk","expected"):
                    if not sc.get(fld): f.append(f"scenario missing {fld}")
        results.append(CaseResult(cid,not f,bool(case.get("critical")),f))
    passed=sum(r.passed for r in results); total=len(results); critical=[r.case_id for r in results if r.critical and not r.passed]
    return EvaluationResult(fixture["prompt_version"],int(fixture["estimated_tokens"]),passed,total,passed/total if total else 0.0,critical,results)
