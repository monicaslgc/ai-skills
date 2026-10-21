# Specifications & Delivery Workflows kit

A practical delivery toolkit for turning business requests into testable specifications, explicit workflows, developer-ready work and evidence-based acceptance decisions. The examples use a fictional back-office order-consistency automation.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`requirements-to-specification`](../../skills/requirements-to-specification) | Create a specification that a business owner, analyst, tester and developer can review without guessing what the request means. |
| [`workflow-process-designer`](../../skills/workflow-process-designer) | Describe exactly how a workflow behaves on normal, delayed, duplicated, invalid and failed inputs. |
| [`requirements-to-user-stories`](../../skills/requirements-to-user-stories) | Create backlog items that explain user value and can be accepted or rejected with observable evidence. |
| [`integration-contract-specifier`](../../skills/integration-contract-specifier) | Make interfaces explicit enough to implement and test without guessing undocumented API behaviour. |
| [`development-work-breakdown-planner`](../../skills/development-work-breakdown-planner) | Give the team a delivery plan that exposes uncertainty and dependencies rather than hiding them behind precise-looking dates. |
| [`test-and-acceptance-planner`](../../skills/test-and-acceptance-planner) | Make it possible to determine whether a workflow meets its requirements, including when dependencies fail or data is malformed. |
| [`delivery-readiness-reviewer`](../../skills/delivery-readiness-reviewer) | Provide a defensible readiness decision with clear evidence, conditions and next actions. |

## Suggested order

1. Start with `requirements-to-specification` to separate facts, decisions, assumptions, scope and open questions.
2. Use `workflow-process-designer` to map states, branches, exceptions, retries and approval gates.
3. Use `integration-contract-specifier` to define data contracts and mark undocumented API details as unverified.
4. Apply `requirements-to-user-stories` to create traceable, testable backlog items.
5. Use `development-work-breakdown-planner` to sequence implementation and validation work.
6. Use `test-and-acceptance-planner` to cover normal, boundary, failure and recovery behaviour.
7. Apply `delivery-readiness-reviewer` before moving into the next stage.

Use the sequence as a guide, not a mandatory chain. Revisit earlier artifacts when tests or new evidence expose a gap.

## Templates

- [Functional specification](templates/functional-specification-template.md)
- [Workflow design](templates/workflow-design-template.md)
- [Integration contract](templates/integration-contract-template.md)
- [Development plan](templates/development-plan-template.md)
- [Test matrix](templates/test-matrix-template.md)

## Install the whole kit

Clone the repository and copy the skill folders into the skills directory supported by your assistant. Example for Claude Code on macOS/Linux:

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/requirements-to-specification ~/.claude/skills/
cp -r ai-skills/skills/workflow-process-designer ~/.claude/skills/
cp -r ai-skills/skills/requirements-to-user-stories ~/.claude/skills/
cp -r ai-skills/skills/integration-contract-specifier ~/.claude/skills/
cp -r ai-skills/skills/development-work-breakdown-planner ~/.claude/skills/
cp -r ai-skills/skills/test-and-acceptance-planner ~/.claude/skills/
cp -r ai-skills/skills/delivery-readiness-reviewer ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\\skills\\requirements-to-specification "$env:USERPROFILE\\.claude\\skills\\"
Copy-Item -Recurse ai-skills\\skills\\workflow-process-designer "$env:USERPROFILE\\.claude\\skills\\"
Copy-Item -Recurse ai-skills\\skills\\requirements-to-user-stories "$env:USERPROFILE\\.claude\\skills\\"
Copy-Item -Recurse ai-skills\\skills\\integration-contract-specifier "$env:USERPROFILE\\.claude\\skills\\"
Copy-Item -Recurse ai-skills\\skills\\development-work-breakdown-planner "$env:USERPROFILE\\.claude\\skills\\"
Copy-Item -Recurse ai-skills\\skills\\test-and-acceptance-planner "$env:USERPROFILE\\.claude\\skills\\"
Copy-Item -Recurse ai-skills\\skills\\delivery-readiness-reviewer "$env:USERPROFILE\\.claude\\skills\\"
```

The skills require no specific tools. If you ask a skill to verify an API or inspect a live system, the relevant documentation, tools and permissions must be available separately.

See [examples](examples.md), [references](references.md) and the [evaluation pack](evaluation.md). Evaluation cases are proposed tests, not a claim that a model passed them.

All examples are fictional. Use synthetic or approved masked data, never credentials or confidential production records.
