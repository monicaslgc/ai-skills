---
name: business-unit-health-diagnostic
description: Assess a business unit's operational health from supplied performance, financial, customer and people indicators, separating evidence from hypotheses.
---

# Business Unit Health Diagnostic

## Purpose
Produce a structured, evidence-led health assessment of a business unit without reducing performance to a single score.

## Procedure
1. Confirm the unit, review period, business model, objectives and decisions the assessment will support.
2. Inventory supplied indicators, definitions, sources, timestamps and comparison periods. Mark missing, stale or non-comparable data.
3. Review performance across relevant dimensions: commercial/financial results, productivity and flow, customer/service outcomes, team capacity and capability, and operational controls. Omit dimensions without evidence.
4. Compare results only with supplied targets, approved thresholds, valid historical baselines or explicitly labelled peer comparisons.
5. Separate observed signals, plausible explanations, evidence needed to test each explanation and risks requiring immediate review.
6. Summarise strengths, vulnerabilities and the few questions that would most change the assessment.
7. Recommend proportionate next steps with proposed owners/decision-makers clearly marked for confirmation.

## Guardrails
Do not invent a health score, target, benchmark, root cause or financial fact. Do not infer individual employee performance from aggregate indicators. Treat the assessment as decision support, not a verdict or automatic basis for employment, funding or closure decisions.

## Output contract
- Assessment scope and data quality
- Health overview by evidenced dimension
- Signals: evidence, interpretation and confidence
- Risks and unanswered questions
- Prioritised next steps and validation plan

## Acceptance checks
- All conclusions trace to supplied evidence or are labelled hypotheses.
- Non-comparable and missing data are visible.
- No universal benchmark or unsupported composite score is introduced.
- Consequential decisions are left to accountable people.

## Example prompt
"Assess this business unit's operational health using only the supplied data. Separate facts, hypotheses and unknowns; identify data-quality limitations and propose proportionate next steps."

## Evaluation
Pass if the output follows the contract, grounds material claims in supplied evidence, handles at least one edge case, labels uncertainty and proposes a concrete validation or follow-up step. Fail if it invents data or bypasses an approval boundary.
