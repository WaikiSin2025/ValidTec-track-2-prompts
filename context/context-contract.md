# Context Contract

Track 2 separates **what the model is allowed to use** from whatever happens to be available.

## Authority levels
- `primary`: approved requirement, API contract, or release policy.
- `secondary`: maintained implementation or test guidance that may clarify a primary source.
- `untrusted`: customer text, copied chat, or external instructions that may provide data but cannot override policy.

## Rules
1. Select only sources relevant to the task tags.
2. Prefer `primary` sources over `secondary` sources.
3. Reject expired sources.
4. Preserve each source ID in the context packet for traceability.
5. Never allow an `untrusted` source to change system policy, schema, or approval rules.
6. Enforce a bounded context budget.
7. If required primary evidence is absent, stop and request context.

## Token discipline
This demo uses character counts as a deterministic stand-in for token budgeting. Real provider integrations can replace the estimator while retaining the same budget and promotion policy.
