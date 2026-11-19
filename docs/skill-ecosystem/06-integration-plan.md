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

At this revision, PRs #1–#9 have been integrated into `main`. PR #10 carries the final regression fixtures and integration updates. The original stack has been reconciled onto the updated default branch.

## Original merge sequence (now completed)

### First: reconcile the independent kit PRs

PRs #1, #2 and #3 are each based on `main`. They all update the root `README.md`; PR #3 also updates `.github/workflows/validate.yml`.

1. PR #1 (Specifications & Delivery Workflows) — merged.
2. PR #2 (Photo & Video Color Grading) — reconciled and merged.
3. PR #3 (Brand Strategy & Identity) — reconciled and merged, including workflow and protocol-test fixes.
4. Full validation passed after the three independent PRs were integrated.

### Then: integrate the creative and ecosystem stack

The dependency chain is:

`#4 → #5 → #6 → #7 → #8 → #9 → #10`

1. PR #4 — #9 were each rebased/reconciled onto the current `main` and merged in dependency order.
2. PR #10 is the remaining integration PR at this revision.
3. The combined workflow retains `actions/checkout@v5`, `actions/setup-python@v6`, brand validation, workflow validation and scenario validation.
4. Registry references for PRs #1–#3 have been changed from pending to available; the final validators run in CI.

Do not merge stacked PRs out of order. After each rebase, inspect the actual diff and CI status; do not force-push or overwrite branch history without an explicit decision.

## What is complete now

- Skills, kit docs and ecosystem integration architecture have been authored.
- The relationship registry contains 75 nodes and 44 typed relationships; all previously pending PR #1–#3 nodes are now marked available.
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
