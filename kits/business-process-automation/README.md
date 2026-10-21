# Business Process Automation kit

Skills for discovering, designing and validating business process automations: discovery, API integration, data mapping, ROI and acceptance testing.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`process-discovery-interviewer`](../../skills/process-discovery-interviewer) | Map a process before automation |
| [`api-integration-planner`](../../skills/api-integration-planner) | Plan verified API integrations |
| [`data-mapping-validator`](../../skills/data-mapping-validator) | Validate fields, identifiers and transformations |
| [`automation-roi-estimator`](../../skills/automation-roi-estimator) | Estimate costs, value and sensitivity |
| [`automation-acceptance-tester`](../../skills/automation-acceptance-tester) | Define acceptance and failure-path tests |

## Suggested order

1. Start with `process-discovery-interviewer` to map the current process, owners and exceptions.
2. Use `api-integration-planner` to verify the required integrations and document unknowns.
3. Apply `data-mapping-validator` to agree identifiers, field types and transformation rules.
4. Use `automation-roi-estimator` once a baseline and assumptions are available.
5. Finish with `automation-acceptance-tester` to define normal, boundary and failure-path tests.

## Install the whole kit

Clone the repository and copy the skill folders into the skills directory supported by your assistant. Example for Claude Code on macOS/Linux:

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/process-discovery-interviewer ~/.claude/skills/
cp -r ai-skills/skills/api-integration-planner ~/.claude/skills/
cp -r ai-skills/skills/data-mapping-validator ~/.claude/skills/
cp -r ai-skills/skills/automation-roi-estimator ~/.claude/skills/
cp -r ai-skills/skills/automation-acceptance-tester ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\process-discovery-interviewer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\api-integration-planner "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\data-mapping-validator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\automation-roi-estimator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\automation-acceptance-tester "$env:USERPROFILE\.claude\skills\"
```

Other assistants use different locations; follow their skills-directory documentation. Each skill folder contains a `SKILL.md` and `USER_STORY.md`.

All examples use fictional or approved data. Do not paste credentials, personal data or confidential production records into a chat you do not control. The kit also includes an [example](examples.md), [reference checklist](references.md) and [evaluation pack](evaluation.md). The evaluation pack is a proposed test plan, not a claimed benchmark result.
