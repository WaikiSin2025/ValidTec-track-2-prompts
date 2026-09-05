# ValidTec Track 2 — Prompt, Context & Token Discipline

A runnable QA portfolio project for **versioned prompts, authoritative context, token discipline, project memory, evaluation regression, human review, promotion gates, and rollback evidence**.

Repository: `ValidTec-track-2-prompts`

## Where Track 2 fits

ValidTec's three repository story is:

```text
Track 1 — Decide what to test
requirements → risk analysis → human approval → automation specification

                    ↓ approved QA intent

Track 2 — Control AI-assisted testing inputs
prompt policy → context packet → token budget → project memory → evaluation gate

                    ↓ reviewed automation task packet

Track 5 — Execute and prove
API regression → Postman/Newman → GitHub Actions → reports/cleanup
```

Track 2 is the control layer between AI-assisted QA design and deterministic automation. It treats prompts and supporting context as testable engineering assets rather than one-off chat instructions.

## What this repository demonstrates

- Stable system policy separated from task-specific instructions.
- Versioned approved and candidate prompts.
- Source authority, freshness, context selection, and token-budget rules.
- A concise `CLAUDE.md` and a reusable risk-based testing skill.
- Structured output contracts for QA artifacts.
- Normal, boundary, negative, missing-context, and adversarial evaluation cases.
- Deterministic fixture outputs so the project runs without a paid model API.
- Quality and token-efficiency comparison between prompt versions.
- Promotion and rollback rules.
- A run record and evaluation report suitable for portfolio discussion.
- GitHub Actions validation.

## Quick start

Requirements: **Python 3.11+**. The demonstration uses only the Python standard library.

```bash
python3 run_demo.py
python3 -m unittest discover -s tests -v
```

Expected demonstration result:

```text
Baseline: approved-v1
Candidate: candidate-v2
Quality pass rate: 100.0% → 100.0%
Estimated tokens: 2100 → 1450
Token reduction: 31.0%
Decision: PROMOTE
```

The repository also contains a deliberate regression fixture used by the automated tests to prove that a bad candidate is blocked.

## Repository map

```text
ValidTec-track-2-prompts/
├── README.md
├── CLAUDE.md
├── LICENSE
├── requirements.txt
├── run_demo.py
├── prompts/
│   ├── approved-v1.md
│   └── candidate-v2.md
├── templates/
│   └── task-brief.md
├── context/
│   ├── context-contract.md
│   └── source-registry.json
├── skills/
│   └── risk-based-test-design.md
├── schemas/
│   └── qa-output.schema.json
├── eval/
│   ├── cases/evaluation-cases.json
│   └── fixtures/
│       ├── approved-v1-results.json
│       ├── candidate-v2-results.json
│       └── candidate-regression-results.json
├── src/validtec_track2/
│   ├── __init__.py
│   ├── context_builder.py
│   ├── evaluator.py
│   ├── promotion_gate.py
│   └── reporting.py
├── tests/
│   ├── test_context_builder.py
│   ├── test_evaluator.py
│   └── test_promotion_gate.py
├── artifacts/
│   ├── sample-evaluation-report.md
│   └── sample-run-record.json
└── .github/workflows/quality-gate.yml
```

## Evaluation contract

Every output must contain:

- `case_id`
- `summary`
- `risks`
- `test_scenarios`
- `evidence_ids`
- `unknowns`
- `decision`

The evaluator checks structure, evidence authority, required risk coverage, missing-context behavior, and adversarial-instruction handling. A candidate cannot be promoted if quality regresses or a critical case fails.

## Promotion policy

The sample policy promotes a candidate only when all of these are true:

1. Candidate pass rate is at least the approved baseline pass rate.
2. Candidate pass rate is at least 95%.
3. No critical case fails.
4. Candidate token usage is no greater than the baseline.
5. Candidate reduces estimated token usage by at least 15%.

This demonstrates a key Track 2 rule: **token reduction is useful only when approved quality is preserved**.

## What the demo does — and does not do

This repository **does not call an LLM by default**. Instead, it uses stored fixture outputs representing runs from two prompt versions. That makes the quality gate deterministic, inexpensive, and suitable for CI.

A real provider adapter can later replace the fixture source while retaining the same prompt registry, context contract, evaluation cases, metrics, and promotion rules.

## Suggested portfolio explanation

> Track 1 defines approved QA intent. Track 2 controls the prompt, context, memory, and evaluation evidence used by AI-assisted testing. Track 5 then executes deterministic regression in CI. In Track 2 I version prompt assets, evaluate them against known QA cases, compare quality and token usage, and prevent promotion when critical behavior regresses.

## ValidTec resources

- Track 2: https://www.validtec.net/tracks/track2.html
- Track 2 Implementation Playbook: https://www.validtec.net/books/track2/ValidTec_Track2_Prompt_Context_Token_Discipline_Implementation_Playbook.pdf
- ValidTec projects: https://www.validtec.net/project-repo.html

## License

MIT. See `LICENSE`.
