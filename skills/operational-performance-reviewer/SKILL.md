---
name: operational-performance-reviewer
description: Review operational KPIs, distinguish signal from noise and produce evidence-led variance analysis and actions.
---

# Operational Performance Reviewer

## Purpose
Review operational metrics and turn changes into testable questions and proportionate actions.

## Procedure
1. Confirm the operational objective, KPI definitions, reporting period, comparison period and decision to be supported.
2. Validate units, denominators, time windows, filters, missing values, duplicates and whether metrics are comparable.
3. Separate leading indicators, lagging outcomes, quality, cost, volume and service measures where relevant.
4. Compare results with supplied targets and prior periods; quantify absolute and relative change only when inputs support it.
5. Identify plausible explanations as hypotheses, not causes, and specify the evidence needed to test each one.
6. Check for trade-offs, such as speed versus quality, throughput versus rework, or lower backlog versus unresolved ageing.
7. Recommend actions proportionate to confidence and impact, with a measurement plan and review date only if agreed.

## Guardrails
Never fabricate a target, benchmark, denominator, causal explanation or statistical significance. Flag small samples and changed definitions. Do not rank individuals from aggregate metrics or recommend punitive action from unvalidated data.

## Output contract
- KPI definition and data-quality notes
- Performance summary against supplied baseline
- Material variances and calculations
- Hypotheses with evidence needed
- Trade-offs and unintended-consequence checks
- Recommended actions and follow-up measures

## Acceptance checks
- Metric definitions and comparison windows are explicit.
- Calculations can be reproduced from supplied values.
- Correlation is not presented as causation.
- At least one data-quality limitation is stated when applicable.

## Example prompt
"Review operational metrics and turn changes into testable questions and proportionate actions. Use only supplied or approved data, label assumptions and unknowns, and include a validation plan."

## Evaluation
Pass if the output follows the contract, labels assumptions, covers at least one exception or boundary case, avoids unsupported claims, and includes a concrete validation or follow-up measure.
