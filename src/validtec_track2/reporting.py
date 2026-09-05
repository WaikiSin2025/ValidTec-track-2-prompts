from __future__ import annotations
from datetime import datetime,timezone
from .evaluator import EvaluationResult
from .promotion_gate import PromotionDecision

def markdown_report(baseline:EvaluationResult,candidate:EvaluationResult,decision:PromotionDecision)->str:
    rows=f"""# Track 2 Evaluation Report\n\nGenerated: {datetime.now(timezone.utc).isoformat()}\n\n## Comparison\n\n| Metric | Baseline | Candidate |\n| --- | ---: | ---: |\n| Prompt version | {baseline.prompt_version} | {candidate.prompt_version} |\n| Passed cases | {baseline.passed_cases}/{baseline.total_cases} | {candidate.passed_cases}/{candidate.total_cases} |\n| Pass rate | {baseline.pass_rate:.1%} | {candidate.pass_rate:.1%} |\n| Critical failures | {len(baseline.critical_failures)} | {len(candidate.critical_failures)} |\n| Estimated tokens | {baseline.estimated_tokens} | {candidate.estimated_tokens} |\n\n## Promotion gate\n\n**Decision: {decision.decision}**\n\nToken reduction: **{decision.token_reduction_pct:.1f}%**\n\nReasons:\n"""
    return rows+"\n".join(f"- {r}" for r in decision.reasons)+"\n"
