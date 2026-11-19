# 03 — Handoff contracts

A handoff is a compact, portable record. Use only fields that matter to the next stage; do not force every skill to produce every field. Preserve source identifiers and user decisions so later skills do not turn assumptions into facts.

## Shared envelope

| Field | Meaning |
|---|---|
| `id` | Stable identifier for this brief or record, if one exists |
| `purpose` | Decision or outcome this work supports |
| `source_context` | User-provided brief, session, document or evidence references |
| `facts` | Claims directly supported by supplied sources |
| `assumptions` | Provisional beliefs that have not been established |
| `unknowns` | Missing information that could change the next decision |
| `constraints` | Fixed requirements and negotiable preferences, clearly distinguished |
| `user_decisions` | Decisions explicitly made by the user |
| `approval_status` | Proposed, awaiting approval, approved, rejected or not applicable |
| `next_action` | Suggested next step; owner only if known |

## Domain contracts

### DiscoveryEvidence
- Research question and audience/context.
- Observation or feedback records with source IDs.
- Direct quotes only when supplied and permitted.
- Behaviour, pain, workaround and outcome.
- Counts only when traceable to the supplied sample.
- Sample limitations, bias and unanswered questions.

### IdeaLandscape
- Original idea ID and wording.
- Source: user-provided or assistant-generated where relevant.
- Underlying need, mechanism, value or experience.
- Patterns, combinations and meaningful differences.
- Outliers and tensions retained.
- No implied ranking unless explicitly requested.

### ConceptBrief
- Core spark and concept proposition.
- Intended audience/context, only when known.
- Desired change and high-level experience/mechanism.
- Design principles and key elements.
- Fixed constraints, assumptions, risks and unknowns.
- First question worth testing and open decisions.

### ConceptEvaluation
- Decision being supported.
- Desirability, feasibility and viability considered separately.
- Evidence source and strength for each material claim.
- Confidence rationale, critical assumptions and risks.
- Learning priorities and possible next moves.
- No automatic go/no-go unless explicitly requested with criteria.

### ConceptExperiment
- Critical assumption and falsifiable learning question.
- Method and why it is proportionate.
- Participant profile and recruitment assumptions.
- Stimulus, neutral protocol and observation plan.
- Positive, negative and ambiguous signals.
- Consent, privacy, accessibility, safety and approval gates.
- Stop conditions and limits on inference.

### ProductSpecification
- Approved scope and intended outcome.
- User/problem context and traceability to evidence.
- Functional and non-functional requirements.
- Business rules, acceptance criteria and exception paths.
- Dependencies, constraints, assumptions and open questions.
- Explicit decisions and approvals.

### WorkflowSpecification
- Trigger, actors, states and transitions.
- Branches, validation, retries and exception handling.
- Data sources, integrations and permissions.
- Human approval gates and audit evidence.
- Monitoring, recovery, rollback and ownership.

### AgentCharterAndRelease
- Agent purpose, boundaries and prohibited actions.
- Tools, data access and permission rationale.
- Autonomy level and approval policy.
- Evaluation scenarios, dataset provenance and rubric.
- Release evidence, monitoring, rollback and incident owner.

## Handoff rules

1. Never silently discard an outlier, constraint, risk or user decision.
2. Keep evidence provenance; do not replace source records with a model's summary alone when traceability matters.
3. Label assistant-generated ideas separately when source attribution matters.
4. Receiving skills may ask for missing critical information, but should not make the sender's assumptions look approved.
5. If a required field is missing, either ask one focused question or state the limitation and continue provisionally.
6. Do not transfer personal, confidential or sensitive data unless it is necessary and authorised.
