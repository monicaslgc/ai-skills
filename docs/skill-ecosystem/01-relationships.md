# 01 — Skill relationships

The machine-readable source is [relationships.json](relationships.json). Each edge is directional where sequence matters and carries a condition describing when the relationship is useful.

## Relationship types

| Type | Meaning | Example |
|---|---|---|
| `requires` | A capability is needed for a specific operation; this is not a general installation dependency | A creative session may need brief clarification when the challenge is materially ambiguous |
| `hands-off-to` | The first skill may produce an output suitable for the second | `concept-developer` → `concept-evaluator` |
| `complements` | Both skills may add value but neither automatically invokes the other | `creative-perspective-lenses` + `productive-tension-mapper` |
| `alternative-to` | Choose one according to the task boundary; do not run both by default | Early concept experiment versus operational improvement experiment |
| `governed-by` | A downstream or governance skill constrains how an action or output is accepted | Agent approval gates inform agent evaluation |

## Important routing boundaries

- **Creative exploration is not product discovery.** Use discovery skills for evidence about people and behaviour; use creative skills to explore frames and possibilities. They can inform each other.
- **Concept evaluation is not prioritisation.** Evaluate the uncertainties and value logic of a concept; use a scorecard only when comparing multiple opportunities against agreed criteria.
- **Concept experiments are not process-improvement experiments.** Test early assumptions about a proposed concept with `concept-experiment-designer`; test changes to an existing operation with `continuous-improvement-experiment-designer`.
- **Concept development is not requirements writing.** A concept brief preserves the proposition and experience; a PRD/specification defines approved product scope and testable requirements.
- **Generic workflow design is not platform implementation.** Define process states and controls before selecting n8n or another platform.
- **Brand specialists are not general creative replacements.** Use the brand workflow for brand decisions and creative-session when a stage needs open exploration.
- **Media planning is not media execution.** Plan the content pipeline separately from deterministic editing and grading.
- **Evaluation is stage-specific.** Brand quality, media quality, acceptance testing, release readiness and agent evaluation answer different questions.

## Availability

Nodes marked `available` exist on the Phase 4 branch. Nodes marked `pending-pr-1`, `pending-pr-2` or `pending-pr-3` are intentional references to skills in those open PRs. They must not be treated as installed or callable until their PRs are integrated.

## Maintenance rule

When a skill is added, renamed or moved:
1. update its kit and root README;
2. update the relationship registry only if a real relationship exists;
3. update workflow definitions only if it has a meaningful handoff role;
4. keep relationships sparse and explain the trigger;
5. run the registry validator.
