---
name: bottleneck-and-flow-analyzer
description: Map work through an operational process and identify queues, rework and constraints using supplied evidence.
---

# Bottleneck and Flow Analyzer

## Purpose
Diagnose where work accumulates or loses flow, without assuming that the busiest step is automatically the root cause.

## Procedure
1. Define the start/end of the workflow, unit of work, scope, service promise and period being analysed.
2. Map stages, handoffs, entry/exit conditions, queues, rework loops and decision points from supplied evidence.
3. Calculate throughput, work-in-progress, queue age and stage time only when the necessary data and definitions exist.
4. Locate where queue size or age grows, where work waits for decisions, and where incomplete inputs cause rework.
5. Distinguish observed constraint, plausible contributing factor and unverified hypothesis.
6. Suggest low-risk experiments that target one constraint at a time; define baseline, measure, guardrail and stop condition.
7. Explain dependencies and what evidence would disprove the proposed bottleneck.

## Guardrails
Do not infer cycle time from incomplete timestamps or assume a resource is the bottleneck because it is busy. Avoid optimising one stage at the expense of total flow, quality or downstream workload. Do not alter production workflows.

## Output contract
- Scope and workflow map
- Available flow metrics and calculation notes
- Observed queues, waits, handoffs and rework
- Constraint candidates with confidence level
- Small experiments, metrics and guardrails
- Evidence gaps and next data to collect

## Acceptance checks
- Workflow boundaries and unit of work are clear.
- Observed facts are separated from hypotheses.
- Proposed experiment has a baseline and guardrail.
- Recommendations consider downstream effects.

## Example prompt
"Diagnose where work accumulates or loses flow, without assuming that the busiest step is automatically the root cause. Use only supplied or approved data, label assumptions and unknowns, and include a validation plan."

## Evaluation
Pass if the output follows the contract, labels assumptions, covers at least one exception or boundary case, avoids unsupported claims, and includes a concrete validation or follow-up measure.
