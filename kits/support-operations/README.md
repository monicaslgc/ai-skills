# Support operations kit

Skills for running a support team: SLAs and escalation, KPIs, quality audits, coaching and access management.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`sla-and-escalation-designer`](../../skills/sla-and-escalation-designer) | Define priorities, response and resolution targets and escalation paths |
| [`support-kpi-dashboard-designer`](../../skills/support-kpi-dashboard-designer) | Choose support metrics, define them precisely and design a dashboard |
| [`ticket-quality-audit`](../../skills/ticket-quality-audit) | Audit support tickets or calls with a scorecard and calibration |
| [`agent-coaching-plan`](../../skills/agent-coaching-plan) | Prepare a coaching conversation and development plan for a team member |
| [`access-request-workflow`](../../skills/access-request-workflow) | Design joiner, mover, leaver and access request workflows with approvals and audit |

## Suggested order

1. Set expectations with `sla-and-escalation-designer`, measure with `support-kpi-dashboard-designer`, improve quality with `ticket-quality-audit` and `agent-coaching-plan`, and manage who can do what with `access-request-workflow`.

## Install the whole kit

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/sla-and-escalation-designer ~/.claude/skills/
cp -r ai-skills/skills/support-kpi-dashboard-designer ~/.claude/skills/
cp -r ai-skills/skills/ticket-quality-audit ~/.claude/skills/
cp -r ai-skills/skills/agent-coaching-plan ~/.claude/skills/
cp -r ai-skills/skills/access-request-workflow ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\sla-and-escalation-designer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\support-kpi-dashboard-designer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\ticket-quality-audit "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\agent-coaching-plan "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\access-request-workflow "$env:USERPROFILE\.claude\skills\"
```

These skills need no tools or servers. Each skill folder has a `USER_STORY.md` with a scenario and an example prompt.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.
