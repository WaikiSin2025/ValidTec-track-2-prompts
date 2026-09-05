# Sample Track 2 Evaluation Report

Baseline `approved-v1` and candidate `candidate-v2` both pass 5/5 evaluation cases. Candidate estimated token usage falls from 2100 to 1450 (31.0% reduction), so the sample promotion gate returns **PROMOTE**.

A separate `candidate-regression` fixture intentionally fails critical authorization/adversarial cases and is blocked with **ROLLBACK**.
