# Monthly client reporting

Produce a monthly service report with checked figures, a clear message and a meeting that ends in decisions.

**Use it when:** You report to a client or to management every month.

## Steps

| # | Skill | Input | Output | Gate (a person decides) |
|---|---|---|---|---|
| 1 | [`document-template-and-style-guide`](../skills/document-template-and-style-guide) | Past reports, client wishes | Report template and style rules (once, then reuse) | Report owner approves the template |
| 2 | [`kpi-insight-writer`](../skills/kpi-insight-writer) | Metrics export | What the numbers say, with caveats | Analyst checks the figures |
| 3 | [`support-kpi-dashboard-designer`](../skills/support-kpi-dashboard-designer) | Metric definitions | Dashboard layout with definitions and thresholds (once, then reuse) | Support lead approves |
| 4 | [`status-and-performance-report`](../skills/status-and-performance-report) | Figures, plan, issues | Report with headline, status, risks and decisions needed | Account owner approves before sending |
| 5 | [`meeting-minutes-and-action-log`](../skills/meeting-minutes-and-action-log) | Review meeting notes | Minutes, decisions and actions | Attendees correct the minutes |

## Rules for this workflow

- Every figure has a source and a definition.
- Bad news is stated plainly with a plan.
- Decisions needed carry an owner and a date.
- Carry the open items and assumptions from each step into the next.
- Keep the `INTERNAL` line out of anything that goes outside.

## Skills to install

`document-template-and-style-guide`, `kpi-insight-writer`, `support-kpi-dashboard-designer`, `status-and-performance-report`, `meeting-minutes-and-action-log`

## Start prompt

> Prepare this month's report. Start by checking the figures in this export and list what does not add up.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.
