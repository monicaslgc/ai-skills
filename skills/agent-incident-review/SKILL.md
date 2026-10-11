---
name: agent-incident-review
description: Review an incident where an AI agent behaved wrongly or unsafely: timeline, impact, root cause (prompt, tool, data, permission, model or human), containment, corrective actions and new tests. Use after an agent error, near miss or unexpected action.
---

# Agent incident review

Learn from agent failures the way teams learn from outages: blameless, evidence-based, ending in changes that prevent a repeat.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- What happened and when.
- Logs, prompts and inputs involved.
- Who or what was affected.
- What has already been done to contain it.

## Workflow

1. Contain first: pause the agent or the affected tool, preserve logs, and notify those affected. Do not delete evidence.
2. Build a timeline from logs: input, agent reasoning or outputs, tool calls, results, human actions.
3. State the impact in plain terms: data, money, people, time, trust.
4. Find the root cause category: instructions unclear, missing guardrail, too-broad permission, bad or malicious input, tool defect, model error, or human process gap. Look for more than one cause.
5. Ask why the failure was not caught earlier: tests, approvals, monitoring.
6. Agree corrective actions: narrow permissions, add an approval gate, fix the instruction or tool, add monitoring, add a regression test. Each has an owner and date.
7. Add the failing input as a permanent test case, and decide whether the agent can resume and under what limits.

## Output format

```
Summary / Impact
Timeline
Root causes (category, evidence)
Why it was not caught
Actions: action, owner, due, how we will know it worked
New test case(s)
Decision on resuming
```

## Safety

- Keep the review blameless; describe systems, not individuals.
- Do not paste real personal or secret data into the review; redact it.
- Do not restore the agent's access until containment and fixes are confirmed.
