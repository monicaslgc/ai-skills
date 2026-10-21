---
name: catalogue-change-reviewer
description: Review catalogue imports and bulk edits for impact, reversibility, SKU uniqueness and deletion risk.
---

# Catalogue Change Reviewer

## Procedure
1. Identify source and destination snapshots, scope and publication window.
2. Compare additions, updates, deletions, identifiers, variants and required fields.
3. Check duplicate SKUs, unexpected blanks, invalid values and suspicious volume changes.
4. Summarise high-risk records and sample records for human review.
5. Recommend staged import, validation, audit capture and rollback.
6. Do not publish or modify records; request explicit approval for any consequential action.

## Guardrails
Treat uncertain mapping as quarantine, not a best guess. Never silently merge or delete. Preserve a before-snapshot and rollback evidence.

## Output
Counts and exceptions, affected IDs, risk tiers, validation results, approval gates and rollback plan.

## Evaluation
Pass if additions/updates/deletions are distinguished, duplicate IDs are flagged, destructive changes require approval and rollback is addressed.
