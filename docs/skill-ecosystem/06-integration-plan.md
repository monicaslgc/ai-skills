# 06 — Integration and completion plan

This document distinguishes implementation completion from merging and behavioural validation.

## Phase status

| Phase | Deliverable | Status |
|---|---|---|
| 1 — Creative foundation | Creative Partner/Room orchestration, framing, divergence and bouncing | Implemented in PR #4 |
| 2 — Creative methods | Lenses, rounds, tension mapping, analogy and constraint remix | Implemented in PR #5 |
| 3 — Synthesis and concepts | Convergence and concept development | Implemented in PR #6 |
| 4 — Evaluation and experimentation | Concept evaluation and early concept experiment design | Implemented in PR #7 |
| 5 — Ecosystem audit | Inventory, overlap boundaries, dependencies and workflow candidates | Implemented in PR #8 |
| 6 — Relationship/workflow architecture | Typed registry, six workflows, handoff contracts, orchestration rules and CI validation | Implemented in PR #9 |
| 7 — Integration and regression framework | Optional handoffs, 10 end-to-end scenarios and fixture validators | Implemented in PR #10 |

All PRs are still open; no merge has been performed. The phase chain is deliberately stacked.

## Recommended merge sequence

### First: reconcile the independent kit PRs

PRs #1, #2 and #3 are each based on `main`. They all update the root `README.md`; PR #3 also updates `.github/workflows/validate.yml`.

1. Review and integrate PR #1 (Specifications & Delivery Workflows).
2. Rebase/reconcile PR #2 (Photo & Video Color Grading) on the updated main and preserve both README kit indexes.
3. Rebase/reconcile PR #3 (Brand Strategy & Identity) on the updated main. Preserve the README entries and review its workflow changes, knowledge architecture, MCP docs and additional evaluation tooling.
4. Run the full validation suite after the three independent PRs are integrated.

### Then: integrate the creative and ecosystem stack

The dependency chain is:

`#4 → #5 → #6 → #7 → #8 → #9 → #10`

1. Rebase PR #4 onto the updated main and preserve all existing kit indexes.
2. Merge #4, then rebase and merge #5, #6 and #7 in order.
3. Rebase and merge #8, #9 and #10 in order.
4. Reconcile `.github/workflows/validate.yml`: retain the Node.js 24-compatible actions and run `validate.py`, `check_tools.py`, `validate_skill_workflows.py` and `validate_workflow_scenarios.py`. Preserve any additional validation introduced by PR #3.
5. Update `relationships.json` and `workflows.json` from pending PR references to available skills after PRs #1–#3 are merged. Re-run both registry validators.

Do not merge stacked PRs out of order. After each rebase, inspect the actual diff and CI status; do not force-push or overwrite branch history without an explicit decision.

## What is complete now

- Skills, kit docs and ecosystem integration architecture have been authored.
- The relationship registry contains 75 nodes and 44 typed relationships.
- Six cross-kit workflow definitions and handoff contracts are documented.
- CI checks validate skill structure, kit independence, workflow references and scenario fixtures.
- The final Phase 7 PR has a passing GitHub Actions run.

## What is not yet empirically complete

The ten E2E scenarios are **fixtures only**. The validators prove that the test cases are structurally valid and reference known workflows/skills; they do not run the skills against a model.

Before claiming behavioural quality:
1. Run the ten scenarios in the intended assistant/runtime with the relevant skills installed.
2. Capture exact model/version, skill commit, prompts, outputs and any tool evidence.
3. Score against the rubric in [05 — Cross-skill evaluation](05-evaluation.md).
4. Fix failures and rerun affected scenarios.
5. Only then publish aggregate scores or claim the cross-skill workflows have passed behavioural evaluation.

## Definition of done

The repository integration is complete when all ten PRs are merged in a reconciled sequence, all pending registry references are updated, and the complete CI suite passes on `main`.

The behavioural quality gate is complete only when the ten E2E scenarios have actually been run and reviewed. These are separate completion conditions.
