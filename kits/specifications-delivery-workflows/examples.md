# Specifications & Delivery Workflows examples

All systems, identifiers and records below are fictional. These examples demonstrate method, not vendor-specific API behaviour or production readiness.

## Example 1 — Back-office order consistency

**Request:** Each weekday, compare order records from a fictional OrderHub with shipment records from a fictional ShipTrack. Surface mismatches for review. Do not change orders or message customers automatically.

**Specification decisions:**
- Trigger: scheduled daily run; exact timezone and schedule need owner confirmation.
- Read mode: source systems are read-only for the first release.
- Match key: proposed stable order ID, pending confirmation that both systems use the same identifier.
- Result states: `MATCHED`, `MISMATCH`, `SOURCE_MISSING`, `INVALID_RECORD`, `REVIEW_REQUIRED`.
- Unknowns: API endpoints, pagination, authentication, rate limits, source-of-truth rules and retention are not supplied and must be verified.
- Approval: any future write-back is a separate scope and requires explicit review.

## Example 2 — Workflow and exception table

| Condition | Workflow response | Retry? | Human action |
|---|---|---|---|
| Valid records match | Record match and audit reference | No | None unless sampling policy requires it |
| Valid records disagree | Create review item with source evidence | No automatic write | Reviewer classifies mismatch |
| Duplicate input file | Detect using approved file/run fingerprint | No duplicate processing | Review if fingerprint is ambiguous |
| API timeout | Record failed attempt and preserve run state | Bounded retry only if safe | Escalate after retry budget |
| Partial API result | Mark run incomplete; do not call reconciliation complete | Depends on documented error and cursor behaviour | Resume or re-run after verification |
| Missing identifier | Quarantine record with reason | No | Correct source data or approve exception |
| Reviewer rejects proposed resolution | Keep mismatch open and record reason | No | Route according to supplied policy |

## Example 3 — Synthetic field mapping

| Source field | Destination concept | Rule | Unknown to verify |
|---|---|---|---|
| `order_ref` | Order identifier | Required, non-empty string; preserve leading zeros | Is it globally unique? |
| `shipment_state` | Shipment state | Map only documented enum values | Full enum and version |
| `updated_at` | Source update timestamp | Parse documented format; preserve source timezone/offset | Is timestamp monotonic? |
| `tracking_ref` | Tracking reference | Optional; redact from broad logs if sensitive | Retention and access policy |

The names above are invented examples, not actual vendor schema fields.

## Example 4 — Backlog slice

- **Epic:** Daily consistency review.
- **Story:** As an operations reviewer, I want mismatches grouped with source evidence so I can investigate without altering either source record.
- **Acceptance:** matching identifiers and states are marked consistent; disagreements create a review item; malformed identifiers are quarantined; a source timeout leaves the run incomplete; no write-back or external message occurs.
- **Dependencies:** verified read APIs, agreed identifier mapping, secure credential configuration and an approved retention rule.
- **Validation:** schema/contract tests, duplicate-run test, timeout test, partial-result test and reviewer acceptance.

## Example 5 — Readiness review

**Evidence supplied:** specification exists, workflow includes timeout and duplicate handling, API authentication and pagination remain undocumented, and no contract tests have been executed.

**Decision:** NOT READY for implementation against real APIs until the interface questions are resolved; design work using abstract contracts may continue. Execution status is “not run”, not “failed”.

## Anti-patterns

- Treating a plausible endpoint or field name as verified.
- Retrying a write operation without idempotency protection.
- Marking a partial extraction as a complete reconciliation.
- Hiding unknown decisions in implementation tasks.
- Claiming tests pass because test cases have been written.
- Treating AI-generated recommendations as authority to mutate production records.
