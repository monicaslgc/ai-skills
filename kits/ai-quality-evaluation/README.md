# AI quality and evaluation kit

Skills for making AI behaviour testable through datasets, rubrics, regression checks, structured validation and failure analysis.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`ai-eval-dataset-builder`](../../skills/ai-eval-dataset-builder) | Build privacy-safe evaluation sets |
| [`ai-output-rubric-designer`](../../skills/ai-output-rubric-designer) | Create anchored scoring rubrics |
| [`prompt-regression-tester`](../../skills/prompt-regression-tester) | Compare prompt/model versions |
| [`structured-output-validator`](../../skills/structured-output-validator) | Check structured model outputs |
| [`ai-failure-analyzer`](../../skills/ai-failure-analyzer) | Diagnose failures and derive regression tests |

## Suggested order

1. Start with `ai-eval-dataset-builder` to define representative, privacy-safe cases.
2. Use `ai-output-rubric-designer` to define observable scoring criteria.
3. Apply `structured-output-validator` where outputs must follow a schema and business rules.
4. Use `prompt-regression-tester` to compare a candidate against a fixed baseline.
5. Finish with `ai-failure-analyzer` to turn failures into actionable regression cases.

## Install the whole kit

Clone the repository and copy the skill folders into the skills directory supported by your assistant. Example for Claude Code on macOS/Linux:

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/ai-eval-dataset-builder ~/.claude/skills/
cp -r ai-skills/skills/ai-output-rubric-designer ~/.claude/skills/
cp -r ai-skills/skills/prompt-regression-tester ~/.claude/skills/
cp -r ai-skills/skills/structured-output-validator ~/.claude/skills/
cp -r ai-skills/skills/ai-failure-analyzer ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\ai-eval-dataset-builder "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\ai-output-rubric-designer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\prompt-regression-tester "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\structured-output-validator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\ai-failure-analyzer "$env:USERPROFILE\.claude\skills\"
```

Other assistants use different locations; follow their skills-directory documentation. Each skill folder contains a `SKILL.md` and `USER_STORY.md`.

All examples use fictional or approved data. Do not paste credentials, personal data or confidential production records into a chat you do not control. The kit also includes an [example](examples.md), [reference checklist](references.md) and [evaluation pack](evaluation.md). The evaluation pack is a proposed test plan, not a claimed benchmark result.
