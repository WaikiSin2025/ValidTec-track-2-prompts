from __future__ import annotations
from dataclasses import dataclass,asdict
from .evaluator import EvaluationResult
@dataclass
class PromotionDecision:
    decision:str; reasons:list[str]; token_reduction_pct:float
    def as_dict(self)->dict: return asdict(self)

def decide_promotion(baseline:EvaluationResult,candidate:EvaluationResult,minimum_pass_rate:float=.95,minimum_token_reduction:float=.15)->PromotionDecision:
    reasons=[]; reduction=(baseline.estimated_tokens-candidate.estimated_tokens)/baseline.estimated_tokens if baseline.estimated_tokens>0 else 0.0
    if candidate.pass_rate<baseline.pass_rate: reasons.append("candidate quality regressed below the approved baseline")
    if candidate.pass_rate<minimum_pass_rate: reasons.append(f"candidate pass rate is below {minimum_pass_rate:.0%}")
    if candidate.critical_failures: reasons.append("critical evaluation cases failed: "+", ".join(candidate.critical_failures))
    if candidate.estimated_tokens>baseline.estimated_tokens: reasons.append("candidate uses more estimated tokens than the baseline")
    if reduction<minimum_token_reduction: reasons.append(f"token reduction is below {minimum_token_reduction:.0%}")
    return PromotionDecision("ROLLBACK" if reasons else "PROMOTE",reasons or ["quality preserved, critical cases pass, and token target is met"],reduction*100)
