# Knowledge Architecture Rollout Roadmap

## Goal
Evolve the repository from a collection of task skills into a maintainable library of domain-grounded AI capabilities. Skills should explain, reason, apply, evaluate and recognise the limits of their speciality.

## Current-state findings
The repository already has useful foundations: multi-skill kits, shared Brand Context and Decision Log, a substantive Naming Method Playbook, quality gates, tool schemas, security notes, evaluation fixtures and CI checks.

The main gaps are:
- Domain knowledge is uneven and often compressed into brief method summaries in individual skills.
- Shared knowledge is not yet a first-class repository layer.
- Portability claims can conflict with cross-folder knowledge dependencies.
- Source provenance and review metadata are not standardised across domains.
- CI validates schemas and fixture structure, but does not prove model behaviour or domain competence.
- Skills vary in how clearly they distinguish framework knowledge from task instructions.

## Phase 0 — Establish the standard
Deliverables: repository architecture, authoring standard, knowledge directory guide and this roadmap.
Exit: standards documented; no mass migration before the pilot is reviewed.

## Phase 1 — Brand Strategy & Identity pilot
Consolidate the kit's reusable knowledge into knowledge/brand-strategy/ (or a better-scoped name after inventory).

Initial knowledge map:
- Brand fundamentals: identity, image, reputation, equity, purpose, positioning, value proposition and brand systems.
- Strategy and positioning: category, audience, differentiation, competitive frame, proof and strategic trade-offs.
- Research: qualitative and quantitative evidence, sampling, interviews, segmentation, competitor/category research and limitations.
- Naming: preserve and deepen NAMING_METHOD_PLAYBOOK.md, including naming theory, linguistic evaluation and legal/digital screening boundaries.
- Identity and expression: verbal/visual identity, semiotics, design systems, brand architecture and touchpoint coherence.
- Governance and measurement: consistency, asset governance, claims substantiation, brand metrics and causal limitations.

Do not move or delete existing documents until dependencies and links are mapped. Keep project context, kit quality gates and decisions in the kit.

Exit criteria:
- Every Brand Strategy skill declares knowledge dependencies.
- Shared knowledge covers material methods used by the kit.
- Duplication is reduced without breaking standalone/hybrid use.
- Every skill has normal, incomplete and conflict/unsafe behavioural fixtures.
- A representative sample is executed with named model/version and human reviewer.

## Phase 2 — Skill inventory and risk-based triage
Inventory all skills by domain/kit, task and decision, risk, knowledge depth, dependencies, portability mode, tools, evaluation maturity and maintainer.

Prioritise high-judgement, high-impact, fast-changing or legally/financially/health/safety-sensitive skills. Do not impose identical documentation overhead on every skill.

## Phase 3 — Migrate remaining kits
Proposed sequence, subject to user demand and risk:
1. Product Discovery & Delivery.
2. Project Management and Operations Management.
3. People Operations and Support Operations.
4. AI Quality & Evaluation and Agent Management.
5. Business Process Automation and n8n Automation.
6. Self-hosted AI, Smart Home and E-commerce Operations.
7. Career, Content Creation and Memory.

For each kit: map concepts and skills; identify authoritative sources; build knowledge; update skills; add examples and failure modes; add behavioural evaluations; review portability and installation.

## Phase 4 — Evaluation maturity
Keep separate checks for static quality, knowledge quality, behavioural quality, tool quality and regression. Record model/version, provider, skill and knowledge commit, tool configuration, fixture, reviewer, scores and critical failures. Never label unexecuted fixtures as passed evaluations.

## Phase 5 — Release and governance
Before release: confirm dependencies and portability modes; validate links and installation; review sources and stale-content warnings; run static checks and deterministic tests; run representative behavioural evaluations; review security, privacy and copyright; publish a changelog.

## Suggested inventory fields
| Field | Purpose |
|---|---|
| Skill ID | Stable identifier |
| Kit/domain | Knowledge ownership |
| Task and decision | What it helps the agent do |
| Risk tier | Consequence of failure |
| Knowledge dependencies | Required domain documents |
| Portability mode | Standalone, kit-dependent or hybrid |
| Tool dependencies | External capabilities |
| Evidence freshness | Last review / trigger |
| Evaluation status | Static, behavioural, regression |
| Maintainer | Accountable role |

## Non-goals
- Do not turn every skill into a textbook.
- Do not create one knowledge file per skill by default.
- Do not copy copyrighted books or paid training.
- Do not treat a source list as proof of understanding.
- Do not claim behavioural quality from static CI.
- Do not burden simple deterministic skills with unnecessary theory.

## Immediate next work
Start Phase 1 with a knowledge map and dependency inventory for Brand Strategy & Identity. Use the existing naming playbook as a source asset, not a template to copy mechanically. Then migrate one high-value skill end-to-end (brand strategy or positioning) and evaluate it before scaling to all 32 skills.
