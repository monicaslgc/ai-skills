---
name: app-flow-mapper
description: Map the real flows of an existing app: screens, roles, entry points, steps, decisions, states, errors, data and integrations, from a live walkthrough, screenshots, recordings or notes. Produces a flow inventory and a simple diagram. Use before writing user documentation, a specification or a migration plan.
---

# App flow mapper

Record how an existing app really works, as evidence, before anyone writes about it or changes it.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The app, the version or environment, and the goal of the mapping (guide, specification, migration, training).
- The roles to cover (for example administrator, standard user, read-only user) and a test account for each.
- Where to explore: a test or demo environment. If the only option is a live system, agree what may and may not be touched.
- Existing material: old guides, screenshots, recordings, tickets, release notes.

## Workflow

1. Scope. List the flows to map as user goals ("create an order", "reset a password"), not as screens. Agree the order and what is out of scope.
2. Explore one flow at a time with a test account and demo data. If you have a browser or screen tool, walk the happy path yourself and capture a screenshot at every step; otherwise ask for screenshots, a screen recording or a person to narrate while sharing the screen.
3. For every step write: the screen or page name, where the user is (menu path or address), the action, what the app answers, and the screenshot reference.
4. Find the branches: decisions, optional steps, alternative ways to reach the same result, and what changes by role or permission.
5. Provoke the errors that are safe to provoke (empty required field, wrong format, no permission) and note the exact message and what the user can do next.
6. Record states and data: the statuses an item moves through, which fields are required, what is calculated, what is sent to other systems or people (emails, exports, integrations).
7. Label every statement as observed (seen in the app), reported (told by a user or found in old material) or inferred (guessed). Never present inferred as observed.
8. Draw the flow: a simple flowchart with the happy path in the middle, decisions as branches and errors off to the side. Keep one flow per diagram.
9. List open questions and anything that could not be reached with the available roles.

## Rules

- Use demo data and test accounts. Do not submit real customer data, change settings, send messages to real people or trigger payments. Stop and ask before any irreversible action.
- Capture what the app does, not what it should do. Differences from the old documentation are findings, not mistakes to hide.
- Mask personal data in screenshots before they are stored or shared.
- Do not paste credentials into notes or screenshots.

## Output format

```
Flow inventory: <app>, <version/environment>, <date>, <roles covered>
Flow 1: <user goal>
  Roles / prerequisites
  Steps: # | screen | action | app response | evidence (observed/reported/inferred) | screenshot
  Decisions and branches
  Errors: trigger | message | what the user can do
  States and data
  Integrations and notifications
Diagram (one per flow)
Gaps and open questions
Differences from existing documentation
```

## Quality checks

- Every step can be repeated by someone else and gives the same result.
- Evidence is labelled and nothing inferred is stated as fact.
- Each role that matters was either covered or listed as a gap.
- No real personal data or credentials appear in the notes or images.
