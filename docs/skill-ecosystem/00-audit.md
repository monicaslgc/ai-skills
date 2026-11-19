# Skill ecosystem audit — Phase 5

**Status:** structural and relationship audit completed against the current main branch, Creative Thinking Phase 4, and the three other open kit PRs. This is an inventory and design audit, not a claim that every skill has passed behavioural evaluation.

## 1. Inventory snapshot

The branches are independent and must not be added together as if they were already merged.

| Snapshot | Skills | Kits | Status |
|---|---:|---:|---|
| `main` | 110 | 16 | Current default branch at audit time |
| Creative Thinking through Phase 4 | 123 | 17 | Stacked PRs #4–#7; Phase 4 is based on Phase 3 |
| PR #1 — Specifications & Delivery Workflows | 117 | 17 | Open; based on main |
| PR #2 — Photo & Video Color Grading | 117 | 17 | Open; based on main |
| PR #3 — Brand Strategy & Identity | 144 | 18 | Open; based on main |

If all four workstreams are accepted and integrated without overlap, the potential inventory is **171 skills and 21 kits**. This is a projected combined count, not the current main-branch count.

### Pending additions outside Creative Thinking

- **PR #1:** `delivery-readiness-reviewer`, `development-work-breakdown-planner`, `integration-contract-specifier`, `requirements-to-specification`, `requirements-to-user-stories`, `test-and-acceptance-planner`, `workflow-process-designer`.
- **PR #2:** `color-quality-reviewer`, `look-development`, `media-editing-pipeline`, `media-quality-analyzer`, `photo-color-corrector`, `shot-matching`, `video-color-grader`.
- **PR #3:** brand strategy, brand identity, audience research, naming, campaign and MCP operation skills; see the PR's own README for the full specialist inventory.

## 2. Kit capability map

| Capability family | Kit(s) | Primary purpose |
|---|---|---|
| Creative exploration | Creative Thinking & Ideation | Frame, diverge, bounce, explore perspectives, converge, develop, evaluate and test concepts |
| Product decisions | Product Discovery & Delivery | Gather discovery evidence, synthesise feedback, compare opportunities, define requirements and prepare releases |
| Project execution | Project Management; Specifications & Delivery Workflows (PR #1) | Turn approved scope into plans, work breakdowns, specifications, stories, tests and readiness checks |
| Brand and communication | Brand Strategy & Identity (PR #3); Content Creation | Research and define identity, positioning, messaging, campaigns and content |
| Visual production | Photo & Video Color Grading (PR #2); Content Creation | Develop looks, correct and grade media, inspect quality and prepare publishable assets |
| Operational improvement | Operations Management; Operations & Productivity; Support Operations; E-commerce Operations | Diagnose performance, bottlenecks and exceptions; improve and govern operational work |
| Automation and systems | Business Process Automation; n8n Automation; Self-hosted AI | Discover processes, design integrations and workflows, implement and operate automation |
| AI agent lifecycle | Agent Management; AI Quality & Evaluation | Define agent scope, permissions, approvals, evaluations, release and incident controls |
| People and organisational capability | People Operations | Plan staffing, onboarding, interviews and people processes |
| Personal and home systems | Career; Memory; Smart Home | Support individual workflows, knowledge retrieval and home automation |

## 3. Relationship and overlap findings

The following pairs are related but should remain separate. Their boundaries need to be explicit in handoff guidance.

| Skills / capabilities | Relationship | Boundary to preserve |
|---|---|---|
| `concept-developer` ↔ `campaign-concept-developer` (PR #3) | Complements / specialised variant | Generic concept development versus campaign territories grounded in an approved brand strategy |
| `concept-evaluator` ↔ `brand-quality-evaluator` (PR #3) | Complements | Early concept desirability/feasibility/viability versus quality of a brand deliverable against a rubric |
| `concept-evaluator` ↔ `prioritization-scorecard` | Sequential handoff | Evaluate one concept's uncertainties first; compare competing opportunities only when criteria and weights are agreed |
| `concept-experiment-designer` ↔ `continuous-improvement-experiment-designer` | Complements; not duplicates | Early concept learning versus measured improvement of an existing operational process |
| `concept-experiment-designer` ↔ `test-and-acceptance-planner` (PR #1) | Sequential handoff | Learn whether a concept assumption holds versus verify a defined system/process against requirements |
| `creative-session` ↔ `brand-workflow-orchestrator` (PR #3) | Different orchestration scope | General creative-thinking session versus staged brand strategy/identity workflow |
| `creative-perspective-lenses` ↔ `brand-personality-archetypes` (PR #3) | Similar language; different domain | Thinking perspectives used to explore a problem versus traits describing a brand's behaviour |
| `customer-feedback-synthesizer` ↔ `audience-research` (PR #3) | Sequential / complementary | Synthesis of supplied feedback versus design of audience segments and research questions |
| `requirements-to-specification` (PR #1) ↔ `prd-and-spec-writer` | Potential overlap; clarify trigger | General transformation of ambiguous requirements versus product-specific PRD and product specification |
| `development-work-breakdown-planner` (PR #1) ↔ `project-plan-builder` | Sequential handoff | Engineering work items and dependencies versus project-level phases, milestones and governance |
| `delivery-readiness-reviewer` (PR #1) ↔ `release-readiness-reviewer` | Sequential handoff | Readiness of a specification or development increment versus production release readiness |
| `workflow-process-designer` (PR #1) ↔ `n8n-automation-architect` / `self-hosted-ai-workflow-designer` | Sequential handoff | Technology-agnostic process design versus platform-specific automation architecture |
| `automation-acceptance-tester` ↔ `test-and-acceptance-planner` (PR #1) | Related scope; clarify trigger | Acceptance of a business automation versus a broader traceable system test plan |
| `content-pipeline-planner` ↔ `media-editing-pipeline` (PR #2) | Sequential handoff | End-to-end content production plan versus safe execution of media correction/rendering |
| `media-quality-analyzer` ↔ `color-quality-reviewer` (PR #2) | Sequential handoff | Diagnose source media before editing versus review before/after results and delivery integrity |
| `brand-name-availability` ↔ `brand-naming-validation` (PR #3) | Sequential handoff | Early screening of candidate names versus validation of a selected shortlist |
| `mcp-client-operator` (PR #3) ↔ `brand-tool-calling` (PR #3) | General capability plus domain policy | General discovery and safe use of host MCP capabilities versus brand-workflow-specific tool selection and approval |

### Audit conclusions

1. No broad consolidation is recommended. The specialist skills are useful when each has a clear trigger, scope and output.
2. Several generic skills use similar scaffolding. Their task-specific methods and output contracts—not their generic headings—must define the difference.
3. Orchestrators should route only when a handoff condition is met. They should not invoke every related skill by default.
4. A skill may recommend a handoff, but it must not claim that another skill or external tool was actually run unless the host confirms execution.
5. Keep domain specialists reusable: a generic skill should not absorb a brand, media, product or operations method merely to reduce the skill count.

## 4. Cross-kit workflow candidates

These are the highest-value end-to-end paths to formalise in Phase 6.

1. **Idea to product delivery:** discovery evidence → creative exploration → concept brief → concept evaluation → concept experiment → opportunity prioritisation → PRD/specification → stories/work breakdown → test and readiness → release.
2. **Brand from discovery to launch:** audience and stakeholder research → brand discovery and category research → strategy/positioning → identity and messaging → campaign/content concepts → quality and claim review → launch and performance review.
3. **Content to publishable media:** content brief and plan → concept and art direction → pipeline plan → media edit/grade → quality review → captions, thumbnails and publishing approval.
4. **Operational improvement to automation:** process discovery → performance/bottleneck diagnosis → improvement experiment → automation suitability → process/workflow design → integration/data mapping → platform implementation → acceptance and controls.
5. **Agent from idea to governed release:** agent charter → permissions review → workflow and approval gates → evaluation dataset/rubric → regression and failure analysis → release checklist → incident review.
6. **Project from approval to delivery:** charter → plan and work breakdown → requirements/specification → RAID and change control → acceptance/readiness → status and retrospective.

## 5. Integration risks and dependencies

- PRs #1, #2 and #3 are all based on `main` and each changes `README.md`. They need a deliberate rebase/merge order and a final README reconciliation; do not assume they can all merge cleanly.
- PR #3 also changes `.github/workflows/validate.yml` and introduces knowledge, evaluations and MCP documentation. Its workflow changes need review alongside the skill inventory.
- Creative PRs #4–#7 are stacked: #5 depends on #4, #6 depends on #5, and #7 depends on #6. They should be integrated in order.
- The ecosystem audit includes the open PRs as planned capabilities, but references to their skills are conditional until those PRs are merged.
- Do not change branch protection, merge PRs, publish content, contact participants or execute live workflows as part of this documentation work.

## 6. Standards for the next phases

Every cross-skill workflow must declare:
- entry condition and intended decision;
- required inputs and provenance;
- output contract and receiving skill;
- pass/hold/rework conditions;
- human approval points;
- what to do when a required skill or tool is unavailable;
- stop conditions and evidence required to claim completion.

Skills remain independently invocable. Cross-skill relationships are metadata and optional routing guidance, not hard runtime dependencies.

## 7. Evaluation status

This audit is based on repository manifests, README indexes, kit documentation and the open PR file inventories. It is not a model benchmark. Cross-skill scenarios will be specified in Phase 7 and must be run against actual model outputs before any quality claims are made.
