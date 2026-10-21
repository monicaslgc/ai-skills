# Operations management kit

Practical skills for running day-to-day operations: reviewing performance, managing flow and capacity, coordinating exceptions, improving processes and strengthening operational controls.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`daily-operations-review`](../../skills/daily-operations-review) | Turn daily operational signals into decisions and owned actions |
| [`operational-performance-reviewer`](../../skills/operational-performance-reviewer) | Review KPIs and explain variances without inventing causes |
| [`bottleneck-and-flow-analyzer`](../../skills/bottleneck-and-flow-analyzer) | Find queues, handoffs, waiting time and rework |
| [`workload-and-capacity-balancer`](../../skills/workload-and-capacity-balancer) | Compare demand with usable capacity and assess options |
| [`operational-exception-coordinator`](../../skills/operational-exception-coordinator) | Triage exceptions, define escalation and verify recovery |
| [`continuous-improvement-experiment-designer`](../../skills/continuous-improvement-experiment-designer) | Test an improvement with measures and guardrails |
| [`operational-controls-checklist-builder`](../../skills/operational-controls-checklist-builder) | Create evidence-based checklists and exception paths |

## Suggested order

1. Start with `daily-operations-review` to create a shared view of the operation and immediate priorities.
2. Use `operational-performance-reviewer` to validate indicators and understand material variances.
3. Apply `bottleneck-and-flow-analyzer` to investigate queues, handoffs or rework behind the results.
4. Use `workload-and-capacity-balancer` to compare demand with available skills and time.
5. Apply `operational-exception-coordinator` when an exception requires containment, escalation or recovery tracking.
6. Use `continuous-improvement-experiment-designer` to test a focused improvement before wider adoption.
7. Finish with `operational-controls-checklist-builder` to make repeatable checks and exception handling explicit.

These skills can also be used independently. Use the order as a guide, not as a mandatory dependency chain.

## Install the whole kit

Clone the repository and copy the skill folders into the skills directory supported by your assistant. Example for Claude Code on macOS/Linux:

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/daily-operations-review ~/.claude/skills/
cp -r ai-skills/skills/operational-performance-reviewer ~/.claude/skills/
cp -r ai-skills/skills/bottleneck-and-flow-analyzer ~/.claude/skills/
cp -r ai-skills/skills/workload-and-capacity-balancer ~/.claude/skills/
cp -r ai-skills/skills/operational-exception-coordinator ~/.claude/skills/
cp -r ai-skills/skills/continuous-improvement-experiment-designer ~/.claude/skills/
cp -r ai-skills/skills/operational-controls-checklist-builder ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\daily-operations-review "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\operational-performance-reviewer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\bottleneck-and-flow-analyzer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\workload-and-capacity-balancer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\operational-exception-coordinator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\continuous-improvement-experiment-designer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\operational-controls-checklist-builder "$env:USERPROFILE\.claude\skills\"
```

Other assistants use different locations; follow their skills-directory documentation. Each skill folder contains a `SKILL.md` and `USER_STORY.md`.

All examples use fictional or approved data. Do not paste credentials, personal data or confidential production records into a chat you do not control. The kit also includes an [example](examples.md), [reference checklist](references.md) and [evaluation pack](evaluation.md). The evaluation pack is a proposed test plan, not a claimed benchmark result.
