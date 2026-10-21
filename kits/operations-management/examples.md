# Operations management examples

All figures and scenarios below are fictional. They demonstrate how to structure an analysis, not universal targets.

## Example 1 — Daily review

**Inputs:** 120 new requests today; 98 completed; 37 open at close versus 22 yesterday; 9 requests older than the agreed two-day service target; one dependency on an external team.

**Useful output:**
- Backlog rose by 15 net items; confirm whether carry-over and reopened work are included in the counts.
- Nine aged requests breach the supplied target; rank them by impact and age.
- The external dependency is a blocker, not a confirmed root cause for all aged work.
- Actions: validate the aged list, request the dependency status through the established channel, and agree an owner and next update time.

**Avoid:** declaring the team underperforming without checking request mix, capacity, definitions and data quality.

## Example 2 — Flow bottleneck

**Inputs:** Intake-to-completion stages are Intake, Validation, Approval and Fulfilment. Sample data shows a growing queue before Approval; timestamps for two stages are missing.

**Useful output:** treat Approval as a bottleneck candidate because the queue grows there, but label the cause unknown. Check approval arrival/completion rate, decision wait time and rework before proposing a change. Do not calculate end-to-end cycle time from incomplete timestamps.

## Example 3 — Improvement experiment

**Problem:** incomplete intake forms create repeat contacts.

**Hypothesis:** adding three required fields and one example to the intake form will reduce avoidable follow-up contacts.

**Pilot:** one request type for two weeks, subject to process-owner approval.

**Measures:** follow-up-contact rate as the primary outcome; completion time and form abandonment as counter-metrics.

**Decision rule:** compare against a baseline with equivalent definitions. Adopt only if the primary measure improves without unacceptable deterioration in the counter-metrics. Thresholds must be agreed before the pilot.

## Example 4 — Exception handling

**Input:** a daily reconciliation reports a mismatch between two approved exports.

**Safe response:** preserve both source snapshots, confirm timestamp and scope, classify using the existing policy, identify affected records and route to the authorised owner. Do not overwrite either source or mark reconciliation complete until the discrepancy is explained and the agreed verification passes.
