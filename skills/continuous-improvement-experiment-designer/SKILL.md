---
name: continuous-improvement-experiment-designer
description: Turn an operational pain point into a small, measurable improvement experiment with guardrails and a review decision.
---

# Continuous Improvement Experiment Designer

## Purpose
Design a practical improvement experiment that tests a specific operational hypothesis before wider rollout.

## Procedure
1. Define the problem in observable terms, who is affected, the process boundary and why it matters.
2. Establish a baseline using supplied evidence and identify data-quality limitations.
3. Write one testable hypothesis linking a proposed change to an expected outcome.
4. Choose a primary outcome measure, counter-metric, sample or time window, and success threshold; label proposed thresholds for stakeholder approval.
5. Specify the smallest safe intervention, affected users/processes, prerequisites, rollback/stop condition and approver.
6. Define how results will be compared, including seasonality, mix changes, small samples and other plausible confounders.
7. Set decision rules: adopt, adapt, repeat, or stop, with follow-up ownership agreed by the user.

## Guardrails
Do not claim savings or improvements before measurement. Avoid experiments that weaken safety, compliance, privacy, accessibility or financial controls. Require approval before changing live processes, customer communications, permissions or production data.

## Output contract
- Problem statement and baseline
- Hypothesis and proposed intervention
- Measures, thresholds and counter-metrics
- Pilot scope, risks and approval gate
- Data collection and comparison plan
- Rollback/stop condition
- Decision rules and next steps

## Acceptance checks
- Hypothesis is falsifiable.
- Outcome and counter-metric are both defined.
- Success thresholds are labelled as supplied or proposed.
- Pilot has an approval gate and stop condition.

## Example prompt
"Design a practical improvement experiment that tests a specific operational hypothesis before wider rollout. Use only supplied or approved data, label assumptions and unknowns, and include a validation plan."

## Evaluation
Pass if the output follows the contract, labels assumptions, covers at least one exception or boundary case, avoids unsupported claims, and includes a concrete validation or follow-up measure.
