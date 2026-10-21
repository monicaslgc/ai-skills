---
name: performance-variance-investigator
description: Investigate differences between actual operational results and an agreed target, budget or comparable period, checking definitions before explaining variances.
---

# Performance Variance Investigator

## Purpose
Explain what changed, how material the change is, and what evidence is needed before attributing causes.

## Procedure
1. Confirm the metric, period, unit, denominator, target/baseline and decision at stake.
2. Validate whether periods use comparable definitions, populations, cut-off dates and data sources.
3. Calculate absolute and relative variance only where the inputs support it; show formulas and flag zero or unsuitable denominators.
4. Break down the variance by available dimensions such as channel, location, product, work type or stage without assuming a segment explains causality.
5. Distinguish arithmetic contributors, observed correlations, plausible hypotheses and confirmed causes.
6. List targeted checks that could confirm or disprove the leading hypotheses.
7. Recommend immediate containment only if supported by an approved process; otherwise propose a review owner and follow-up.

## Guardrails
Never fabricate data, decompose a variance without a valid basis, or claim causality from correlation. State when seasonality, mix, policy changes or data quality could affect comparison. Do not imply a target exists if none was supplied.

## Output contract
- Metric and comparability check
- Actual, baseline and variance with formula
- Largest evidenced contributors
- Hypotheses ranked by evidence, not certainty
- Validation questions and next actions

## Acceptance checks
- Metric definitions and periods are checked first.
- Calculations are reproducible.
- Causes are labelled confirmed only when evidence supports them.
- Unknowns and counter-explanations remain visible.

## Example prompt
"Investigate the variance in these operational results. Validate comparability, show reproducible calculations, separate contributors from hypotheses, and propose checks before claiming root cause."

## Evaluation
Pass if the output follows the contract, grounds material claims in supplied evidence, handles at least one edge case, labels uncertainty and proposes a concrete validation or follow-up step. Fail if it invents data or bypasses an approval boundary.
