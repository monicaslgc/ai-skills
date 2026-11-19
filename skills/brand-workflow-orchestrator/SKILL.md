---
name: brand-workflow-orchestrator
description: Coordinate brand strategy and identity work by routing each stage to the smallest useful specialist skill and preserving approvals and handoffs.
---

# Brand Workflow Orchestrator

## Purpose

Coordinate a brand project without turning every specialist skill into a separate autonomous agent. Keep the sequence coherent, track dependencies and stop at human decision gates.

## Required inputs

- Project objective, scope and desired deliverable.
- Organisation, product/service, audience, market and language context.
- Available research, existing brand assets and approved decisions.
- Decision-makers, reviewers, deadlines and constraints.
- Skills and tools actually available in the host runtime.

## Routing workflow

1. **Intake and discovery:** use `brand-discovery`; add `brand-workshop-facilitator`, `brand-stakeholder-interviews`, `audience-research` or `brand-audit` only when relevant.
2. **Market context:** use `market-category-analysis` and `competitive-brand-research` when external category evidence is needed.
3. **Strategy:** use `brand-strategy`, then `brand-positioning`, `brand-personality-archetypes`, `brand-identity-prism` or `brand-architecture` as required. Stop for explicit strategy approval.
4. **Naming:** read `kits/brand-strategy-identity/NAMING_METHOD_PLAYBOOK.md` as the shared method reference. Use `naming-studio` to generate a raw batch across distinct naming territories, not just keyword blends. Evaluate spoken and remembered qualities using the playbook's tests and scorecard. Immediately route the batch to `brand-name-availability` to check mandatory domains (default .pt and .com for Portugal/international briefs), company registers and preliminary trademark conflicts. Eliminate blocked candidates before developing concepts; mark unverifiable checks as unknown, never available. Only develop concepts for candidates that pass or are explicitly accepted for review. Then use `brand-naming-validation` for deeper linguistic, cultural and confusion-risk screening. Never treat any screen as legal clearance. Stop for owner and legal review.
5. **Visual direction:** use `visual-inspiration-research`, `moodboard-art-direction` and `logo-design-brief`. Stop for direction approval before final identity production.
6. **Expression:** use `brand-messaging-framework`, `brand-voice-copywriter`, `brand-application-designer` and `brand-guidelines-generator`. Use `brand-claim-validator` for factual or comparative claims.
7. **Activation:** use campaign, content, launch and localization skills only when the approved scope includes them. Stop before external publication.
8. **Governance:** use `brand-asset-governance`, `brand-consistency-auditor` and `brand-performance-analyst` after the system is in use.

## Handoff contract

For each stage, return:

- Status: `draft`, `needs-input`, `ready-for-review`, `approved` or `blocked`.
- Summary and deliverable/version.
- Evidence with sources and dates; assumptions separately.
- Decisions, open questions, risks and dependencies.
- Next recommended skill and whether human approval is required.

Only mark a stage `approved` when an authorised human has explicitly approved the exact version. A complete document, positive comment or lack of response is not approval.

## Safety

- Invoke only the skills needed for the current stage; avoid redundant or circular handoffs.
- Never invent research, decisions, tool availability or approval records.
- Preserve provenance and unresolved disagreement across handoffs.
- If a required skill or integration is unavailable, state the limitation and continue manually where safe.

## Additional orchestration rules
- Maintain a project state with current stage, deliverable versions, owners, blockers, decisions and next action.
- Treat user corrections, rejected options, repeated friction, tool failures and test outcomes as learning signals. Use them to improve the current workflow continuously; keep project-specific decisions separate from general process improvements.
- Read the shared Brand Context and Decision Log at the start of each stage; write back only through a traceable update.
- Parallelise independent research tasks only when they do not depend on an unapproved decision.
- Do not invoke all skills by default. Explain why each specialist is needed and what output it must return.
- Use explicit stage exit criteria; incomplete outputs remain in draft/needs-input and do not unlock dependent stages.
- When an upstream decision changes, identify downstream artefacts that may be invalidated and request review.
- Stop before publishing, external outreach, legal commitment, asset deletion or irreversible changes until explicit approval.
