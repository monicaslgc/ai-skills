---
name: product-discovery-interviewer
description: Run discovery interviews that separate context, behaviour, pain, workaround and outcome.
---

# Product Discovery Interviewer

## Purpose
Run discovery interviews that separate context, behaviour, pain, workaround and outcome.

## Procedure
1. Confirm desired outcome, scope, systems, constraints and output format. Ask only high-impact missing questions.
2. Inventory supplied evidence and source-of-truth rules.
3. Separate facts, assumptions, hypotheses and unknowns.
4. Apply the task method; include normal, boundary, exception and failure paths.
5. Produce the artifact, rationale, risks, validation and next actions.
6. Review against the acceptance checks below.

## Task-specific guardrails
Avoid leading questions and feature pitching. Label observations, quotes and hypotheses separately.

## Output contract
- **Summary:** result and intended use.
- **Evidence:** source facts, assumptions and unknowns.
- **Artifact:** structured, actionable output with identifiers/rules.
- **Risks and exceptions:** likely failures and handling.
- **Validation:** checks performed and still required.
- **Next actions:** owner/action only when known.

## Acceptance checks
- Claims are traceable to evidence or labelled as assumptions.
- Edge cases and failure handling are explicit.
- No secrets or unnecessary confidential/personal data are requested or repeated.
- Validation is concrete and proportionate to the risk.
- Consequential changes are recommendations until explicitly approved.

## Example prompt
"Run discovery interviews that separate context, behaviour, pain, workaround and outcome. Use fictional sample data, flag unknowns, handle one edge case, and include validation checks."

## Evaluation
Pass only if the response produces the artifact, labels unknowns, handles a relevant boundary/failure case, invents no facts or APIs, and supplies a concrete validation check.

## Optional handoffs
- Use `customer-feedback-synthesizer` when there is an existing feedback corpus to analyse; interviews and supplied feedback synthesis are complementary evidence sources.
- Use `creative-session` when discovery has clarified the problem and the user wants to explore solution directions.
- Use `concept-evaluator` only after a concept exists and the user wants to examine its desirability, feasibility and viability.
Do not turn an interview plan or a small qualitative sample into a claim of market validation.
