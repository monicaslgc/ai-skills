---
name: operational-priority-ranker
description: Rank operational initiatives or issues using explicit impact, urgency, effort, risk, reversibility and evidence-confidence criteria.
---

# Operational Priority Ranker

## Purpose
Make trade-offs between competing operational actions transparent and reviewable.

## Procedure
1. List the candidate actions and the decision window; clarify any non-negotiable safety, legal, customer or policy constraints.
2. Agree criteria, definitions, weights and scoring scale with the user. If not supplied, propose a draft rubric and label it for approval.
3. Score each candidate only from supplied evidence; use unknown rather than inventing a score where evidence is missing.
4. Separate mandatory controls or urgent incidents from discretionary improvement work; do not let a weighted score downgrade a mandatory response.
5. Show the rationale, uncertainty, dependencies and opportunity cost for each ranking.
6. Run a sensitivity check where changing weights or uncertain assumptions could change the order.
7. Present a recommended sequence for human review, including what evidence would change the ranking.

## Guardrails
A score is a decision aid, not objective truth. Do not create false precision or hide value judgements in weights. Never rank a mandatory safety, legal, security or approved control obligation below optional work because of a low numerical score.

## Output contract
- Candidate list and constraints
- Scoring criteria, scales and weights
- Ranked table with evidence and confidence
- Sensitivity and dependency notes
- Human decision and review trigger

## Acceptance checks
- Criteria and weights are visible and approved or labelled provisional.
- Missing evidence is not converted into a confident score.
- Mandatory obligations are handled outside ordinary weighted ranking.
- Ranking changes under plausible assumptions are disclosed.

## Example prompt
"Help prioritise these operational actions. Propose transparent criteria, identify mandatory constraints, score only from evidence, test sensitivity and leave the final decision to the accountable owner."

## Evaluation
Pass if the output follows the contract, grounds material claims in supplied evidence, handles at least one edge case, labels uncertainty and proposes a concrete validation or follow-up step. Fail if it invents data or bypasses an approval boundary.
