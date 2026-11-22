---
name: guide-freshness-check
description: Check whether user guides still match the current app: compare each guide with the app, release notes and support questions, and list what is outdated, missing or unclear, with a priority and an owner. Use after a release or when support keeps getting the same question.
---

# Guide freshness check

Find the guides that have drifted from the app, before users find them.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The list of guides, with their location and last-verified date if known.
- The current app version and what changed since the guides were written (release notes, change log, screenshots of new screens).
- Support data: the most frequent questions, tickets that quote a guide, search terms with no result.
- Who owns each guide and how users reach it.

## Workflow

1. Inventory the guides: title, task, audience, location, version verified, date, owner. Note guides that nobody owns.
2. List what changed in the app: new or removed screens, renamed labels, moved menus, changed permissions, new steps, removed features.
3. For each guide, compare every step with the app (or with the evidence of the change): screen, label, order, permission, result. Use a test account with the reader's role.
4. Classify each guide: current, outdated (a step is wrong), incomplete (a new step or option is missing), unclear (users still ask), or obsolete (the feature is gone).
5. Find the gaps in the other direction: tasks that users do or ask about for which no guide exists.
6. Prioritise by impact: how many users, how many tickets, how costly a mistake is, how visible the guide is.
7. Write the update list: guide, what is wrong, the exact line to change, the evidence, owner, due date.
8. Record the check: date, app version, who checked, result per guide. Propose a review cadence (after each release for high-impact guides, otherwise every few months) and a rule that a release is not closed until affected guides are updated or listed.

## Rules

- Verify against the app, not against memory or another guide.
- A guide is only "current" if every step was checked. Mark partly checked guides as such.
- Do not rewrite guides in this skill; list the changes and hand them to [`user-guide-writer`](../user-guide-writer).
- Keep personal data and credentials out of the log and the screenshots.

## Output format

```
Freshness check: <app version>, <date>, <by>
Guide | Task | Status | What is wrong | Evidence | Priority | Owner | Due
Missing guides: task | evidence of demand
Process changes: cadence, ownership, release rule
```

## Quality checks

- Every guide has a status, and every "current" was fully checked.
- Each problem names the exact step and the evidence.
- Priorities reflect users and tickets, not only the order of the list.
- Owners and dates are assigned.
