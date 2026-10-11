# People operations kit

Skills for managers and HR teams: shift scheduling, capacity planning, onboarding, structured interviews, CV screening and leave processes.

> Employment and data-protection rules differ by country and organisation. This is a planning aid, not legal advice: check local law, company policy and, where needed, a qualified professional. Treat people fairly and avoid discriminatory criteria.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`capacity-planning-forecast`](../../skills/capacity-planning-forecast) | Forecast workload and turn it into staffing needs with scenarios |
| [`shift-schedule-planner`](../../skills/shift-schedule-planner) | Build a fair shift schedule that meets coverage and respects rules |
| [`leave-attendance-process-designer`](../../skills/leave-attendance-process-designer) | Design a clear leave and attendance process with approvals and records |
| [`cv-screening-rubric`](../../skills/cv-screening-rubric) | Screen CVs against clear, job-related criteria |
| [`interview-kit-builder`](../../skills/interview-kit-builder) | Build a structured interview with questions and a scoring rubric |
| [`employee-onboarding-plan`](../../skills/employee-onboarding-plan) | Plan a new starter's first days, weeks and 90 days |

## Suggested order

1. Estimate how many people you need with `capacity-planning-forecast`, then build the rota with `shift-schedule-planner`.
2. Define how absences work with `leave-attendance-process-designer`.
3. Hire with `cv-screening-rubric` and `interview-kit-builder`, then welcome people with `employee-onboarding-plan`.

## Install the whole kit

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/capacity-planning-forecast ~/.claude/skills/
cp -r ai-skills/skills/shift-schedule-planner ~/.claude/skills/
cp -r ai-skills/skills/leave-attendance-process-designer ~/.claude/skills/
cp -r ai-skills/skills/cv-screening-rubric ~/.claude/skills/
cp -r ai-skills/skills/interview-kit-builder ~/.claude/skills/
cp -r ai-skills/skills/employee-onboarding-plan ~/.claude/skills/
```

These skills need no tools or servers. Each skill folder has a `USER_STORY.md` with a scenario and an example prompt.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.
