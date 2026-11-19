# Skill ecosystem

This documentation explains how independent skills relate and how complete workflows can cross kit boundaries.

## Documents

- [00 — Ecosystem audit](00-audit.md): inventory snapshot, overlap boundaries, pending PR dependencies and workflow candidates.
- [01 — Relationship registry](01-relationships.md): typed relationships between skills and kits.
- [02 — Workflow catalogue](02-workflows.md): end-to-end workflows with entry conditions, handoffs and approval gates.
- [03 — Handoff contracts](03-handoff-contracts.md): reusable input/output contracts between skill stages.
- [04 — Orchestration rules](04-orchestration.md): routing, optionality, fallbacks and human control.
- [05 — Cross-skill evaluation](05-evaluation.md): proposed regression scenarios for complete workflows.
- [06 — Integration and completion plan](06-integration-plan.md): PR merge order, pending work and definition of done.

The documents describe intended routing, not an executing runtime. Skills remain independently usable. A workflow may recommend the next skill, but must not claim that it ran unless the host actually invoked it and returned a result.

## Design principles

1. **Independent by default:** no skill requires another skill merely to be useful.
2. **Explicit handoffs:** each transition states why it is useful and what information moves forward.
3. **Evidence-preserving:** retain source IDs, assumptions, unknowns and user decisions across stages.
4. **Human-owned decisions:** AI proposes; deterministic rules decide where rules exist; humans approve consequential actions.
5. **Conditional routing:** use only the specialist skills needed for the user's goal.
6. **Honest completion:** distinguish a proposed workflow, a skill invocation, a verified output and an approved action.
7. **Graceful fallback:** if a specialist skill or tool is unavailable, explain the limitation and continue only within safe scope.
