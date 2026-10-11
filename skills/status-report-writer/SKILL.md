---
name: status-report-writer
description: Write a concise project status report: overall RAG status with reasons, progress against plan, milestones, decisions needed, top risks and next steps. Use when asked for a status update, weekly report, steering committee update or progress summary.
---

# Status report writer

Give readers the truth in one page: where the project is, what is at risk, and what you need from them.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The plan and milestones.
- Progress since the last report.
- Current risks and issues.
- Decisions or help needed.

## Workflow

1. Decide the overall status using explicit criteria: Green is on track; Amber is at risk and recoverable with action; Red is off track and needs a decision or help.
2. Write one sentence that explains the status. Lead with the conclusion.
3. Summarise progress against the plan using facts: what was done, what was planned, and the gap.
4. List milestones with date, forecast and status.
5. Give the top three risks or issues, each with the response and owner.
6. List decisions needed, from whom, and by when.
7. State what happens next period.
8. Check tone: remove spin. If good news depends on an unconfirmed assumption, say so.

## Output format

```
Status: Green | Amber | Red - <one sentence why>
Progress this period / Planned vs actual
Milestones (date, forecast, status)
Top risks and issues (response, owner)
Decisions needed (who, by when)
Next period
```
Maximum one page.

## Safety

- Do not report Green when the evidence says otherwise.
- Do not invent progress figures. Mark unknowns as 'not yet confirmed'.
- Keep names out of blame statements.
