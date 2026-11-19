# Knowledge Architecture

## Purpose
This repository should produce AI skills grounded in reusable domain knowledge, not merely collections of prompts or procedural checklists. A skill is only as capable as the knowledge it can reliably access and apply.

## Core principles
1. Knowledge before instructions: skills must be grounded in concepts, principles, models, methods, evidence and limitations.
2. Separation of concerns: keep domain knowledge, task execution, project context, tools and evaluation distinct.
3. Reusable without fragmentation: share genuinely common knowledge; keep specialist knowledge close to its domain.
4. Traceability: material claims and methods need identifiable sources, dates and confidence.
5. Operational usefulness: knowledge must help an agent reason, choose, explain, execute and evaluate.
6. Honest uncertainty: distinguish established knowledge, professional convention, contested interpretation, local policy and project assumptions.
7. Portable by design: declare dependencies and define fallback behaviour.
8. Human accountability: knowledge informs recommendations; it does not grant authority to approve high-impact decisions.

## Repository layers

| Layer | Responsibility | Typical contents |
|---|---|---|
| Knowledge | Explain the domain and why methods work | Concepts, frameworks, evidence, methodologies, decision criteria, limitations, references |
| Skills | Apply knowledge to a defined task | Trigger, inputs, reasoning workflow, tool use, outputs, checks, handoffs |
| Kits | Package a coherent domain or workflow | Skill catalogue, shared context, sequence, common policies, examples |
| Project context | Preserve facts and decisions for one engagement | Brief, approved decisions, constraints, terminology, evidence register |
| Tools | Perform deterministic or external operations | Scripts, API contracts, schemas, connectors |
| Evaluations | Test whether the agent can apply knowledge | Behavioural fixtures, expected behaviours, rubrics, regression records |

Do not put project-specific facts in general knowledge. Do not turn SKILL.md into a textbook. Tool schemas are not domain knowledge and do not prove an integration exists.

## Suggested structure

Use this as a pattern, not a mandatory template:

- knowledge/README.md
- knowledge/KNOWLEDGE_STANDARD.md
- knowledge/<domain>/README.md
- knowledge/<domain>/fundamentals.md
- knowledge/<domain>/frameworks.md
- knowledge/<domain>/methods-and-practice.md
- knowledge/<domain>/decision-criteria.md
- knowledge/<domain>/risks-and-limitations.md
- knowledge/<domain>/references.md

Small domains may combine documents; large domains may split by subdiscipline. Avoid files created only to satisfy a template.

## Dependency and portability model

Every skill must declare one mode:
- Standalone: contains the minimum knowledge needed to perform its task safely and competently; deeper references are optional.
- Kit-dependent: relies on named knowledge documents or shared kit policies; exact paths and fallback behaviour are declared.
- Hybrid: includes essential knowledge in the skill and links to shared knowledge for depth, examples or specialist cases.

A skill must never silently assume that a linked file, tool, connector, network or external service is available. If a dependency cannot be accessed, disclose the limitation and continue only within safe capability.

Copying a skill folder alone is not a valid installation method for a kit-dependent skill. Installation instructions must preserve its dependencies.

## Knowledge lifecycle
1. Identify decisions and tasks the knowledge must support.
2. Research authoritative sources and relevant professional literature.
3. Synthesize original explanations; compare models and identify disagreements.
4. Operationalise concepts through decisions, examples, failure modes and skill workflows.
5. Review domain accuracy, provenance, safety and evaluation design.
6. Release knowledge with dependent skills.
7. Maintain through review triggers and updates when standards, products, laws or evidence change.

## Governance
- Assign an owner or maintainer role to each knowledge area.
- Record source provenance and review dates.
- Prefer primary sources, official standards, peer-reviewed research and recognised professional bodies where applicable.
- Use books and paid material for original synthesis; do not reproduce copyrighted chapters, proprietary worksheets or substantial passages.
- Identify the origin and assumptions of frameworks; do not present one school of thought as universal consensus.
- Record material changes and downstream skill/evaluation impact.
- Apply more frequent review to high-risk and fast-changing domains.

## Definition of done
A knowledge area is ready for production use when it has clear scope, sufficient fundamentals and relevant frameworks, bounded methods, decision criteria, examples, risks and limitations, traceable references, at least one consuming skill, and behavioural evaluations that test application.

See knowledge/KNOWLEDGE_STANDARD.md and KNOWLEDGE_ROADMAP.md.
