# Operations management kit

Practical skills for day-to-day execution and multi-unit management: reviewing performance, diagnosing unit health, prioritising interventions, managing flow and capacity, coordinating recovery and keeping actions accountable.

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
| [`business-unit-health-diagnostic`](../../skills/business-unit-health-diagnostic) | Assess business-unit health across evidenced performance, financial, customer and people indicators |
| [`performance-variance-investigator`](../../skills/performance-variance-investigator) | Investigate differences from targets or baselines and test possible explanations |
| [`operational-priority-ranker`](../../skills/operational-priority-ranker) | Rank competing actions using explicit criteria, evidence and sensitivity checks |
| [`operational-recovery-planner`](../../skills/operational-recovery-planner) | Build phased recovery plans with metrics, milestones and review gates |
| [`management-review-pack-builder`](../../skills/management-review-pack-builder) | Turn validated data into decision-oriented management reviews |
| [`action-plan-follow-through-tracker`](../../skills/action-plan-follow-through-tracker) | Track commitments, blockers, evidence and follow-up actions |
| [`multi-unit-performance-comparator`](../../skills/multi-unit-performance-comparator) | Compare units fairly, accounting for scale, maturity and data comparability |
| [`operational-maturity-assessor`](../../skills/operational-maturity-assessor) | Assess operational maturity using explicit criteria and observable evidence |
| [`leadership-development-planner`](../../skills/leadership-development-planner) | Turn agreed leadership goals into practical development plans |
| [`operational-onboarding-designer`](../../skills/operational-onboarding-designer) | Design onboarding journeys with competency checks and sign-off gates |
| [`peer-learning-program-designer`](../../skills/peer-learning-program-designer) | Structure peer learning and test whether practices transfer |
| [`network-expansion-readiness-assessor`](../../skills/network-expansion-readiness-assessor) | Assess readiness and prerequisites before expanding a network |
| [`profitability-improvement-planner`](../../skills/profitability-improvement-planner) | Identify testable profitability opportunities with transparent assumptions |

## Suggested order

1. Start with `daily-operations-review` to create a shared view of the operation and immediate priorities.
2. Use `operational-performance-reviewer` to validate indicators and understand material variances.
3. Apply `bottleneck-and-flow-analyzer` to investigate queues, handoffs or rework behind the results.
4. Use `workload-and-capacity-balancer` to compare demand with available skills and time.
5. Apply `operational-exception-coordinator` when an exception requires containment, escalation or recovery tracking.
6. Use `continuous-improvement-experiment-designer` to test a focused improvement before wider adoption.
7. Use `business-unit-health-diagnostic` to assess unit health and identify evidence gaps.
8. Apply `performance-variance-investigator` to investigate material deviations.
9. Use `operational-priority-ranker` to make trade-offs explicit.
10. Use `operational-recovery-planner` for a phased recovery plan.
11. Use `management-review-pack-builder` to present decisions and validated results.
12. Use `action-plan-follow-through-tracker` to verify commitments and outcomes.
13. Use `multi-unit-performance-comparator` to compare units only where measures are comparable.
14. Apply `operational-maturity-assessor` to identify evidence-backed practice gaps.
15. Use `profitability-improvement-planner` to develop and validate potential unit-economics improvements.
16. Use `leadership-development-planner` and `operational-onboarding-designer` to build capability.
17. Use `peer-learning-program-designer` to share practices and test transferability.
18. Use `network-expansion-readiness-assessor` before proposing network growth.
19. Finish with `operational-controls-checklist-builder` to make repeatable checks explicit.

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
cp -r ai-skills/skills/business-unit-health-diagnostic ~/.claude/skills/
cp -r ai-skills/skills/performance-variance-investigator ~/.claude/skills/
cp -r ai-skills/skills/operational-priority-ranker ~/.claude/skills/
cp -r ai-skills/skills/operational-recovery-planner ~/.claude/skills/
cp -r ai-skills/skills/management-review-pack-builder ~/.claude/skills/
cp -r ai-skills/skills/action-plan-follow-through-tracker ~/.claude/skills/
cp -r ai-skills/skills/multi-unit-performance-comparator ~/.claude/skills/
cp -r ai-skills/skills/operational-maturity-assessor ~/.claude/skills/
cp -r ai-skills/skills/leadership-development-planner ~/.claude/skills/
cp -r ai-skills/skills/operational-onboarding-designer ~/.claude/skills/
cp -r ai-skills/skills/peer-learning-program-designer ~/.claude/skills/
cp -r ai-skills/skills/network-expansion-readiness-assessor ~/.claude/skills/
cp -r ai-skills/skills/profitability-improvement-planner ~/.claude/skills/
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
Copy-Item -Recurse ai-skills\skills\business-unit-health-diagnostic "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\performance-variance-investigator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\operational-priority-ranker "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\operational-recovery-planner "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\management-review-pack-builder "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\action-plan-follow-through-tracker "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\multi-unit-performance-comparator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\operational-maturity-assessor "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\leadership-development-planner "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\operational-onboarding-designer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\peer-learning-program-designer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\network-expansion-readiness-assessor "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\profitability-improvement-planner "$env:USERPROFILE\.claude\skills\"
```

Other assistants use different locations; follow their skills-directory documentation. Each skill folder contains a `SKILL.md` and `USER_STORY.md`.

All examples use fictional or approved data. Do not paste credentials, personal data or confidential production records into a chat you do not control. The kit also includes an [example](examples.md), [reference checklist](references.md) and [evaluation pack](evaluation.md). The evaluation pack is a proposed test plan, not a claimed benchmark result.
