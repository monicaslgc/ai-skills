---
name: workload-and-capacity-balancer
description: Compare operational demand with available capacity and propose transparent, constraint-aware workload options.
---

# Workload and Capacity Balancer

## Purpose
Help an operations lead balance incoming work, available capacity, priority and service commitments.

## Procedure
1. Confirm planning horizon, work types, priority rules, service commitments and what counts as available capacity.
2. Inventory demand by volume, effort, complexity, arrival pattern and known variability when data exists.
3. Calculate usable capacity from supplied working time, planned absence, meetings, non-queue work and skill constraints; show assumptions.
4. Compare demand and capacity by work type or skill, not only as one aggregate total.
5. Identify overload, underutilisation, single points of failure and work that should not be reassigned without training or authority.
6. Present options such as reprioritisation, cross-training, temporary intake controls, schedule changes or demand reduction.
7. Show each option's impact, trade-offs, prerequisites, risks and monitoring trigger.

## Guardrails
Do not invent staffing data or assume every person is interchangeable. Respect contractual, legal, accessibility, fairness and safety constraints supplied by the user. Recommendations do not authorise changes to shifts, staffing, customer commitments or employment decisions.

## Output contract
- Demand/capacity assumptions and sources
- Capacity calculation by work type or skill
- Gap and risk summary
- Options compared by impact and trade-off
- Dependencies, constraints and approvals required
- Monitoring triggers and review plan

## Acceptance checks
- Demand and capacity use compatible units and periods.
- Assumptions and exclusions are visible.
- Skills and non-queue work are considered.
- No staffing or schedule change is treated as approved.

## Example prompt
"Help an operations lead balance incoming work, available capacity, priority and service commitments. Use only supplied or approved data, label assumptions and unknowns, and include a validation plan."

## Evaluation
Pass if the output follows the contract, labels assumptions, covers at least one exception or boundary case, avoids unsupported claims, and includes a concrete validation or follow-up measure.
