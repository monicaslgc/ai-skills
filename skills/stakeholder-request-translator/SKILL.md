---
name: stakeholder-request-translator
description: Turn a non-technical stakeholder request into a clear technical request: the real goal, the questions to clarify, the affected processes, data, roles and integrations, behaviour with edge cases, acceptance criteria, assumptions and open questions, then read it back to the stakeholder in plain words. Use when a business request must become a ticket, a specification or a brief for engineers.
---

# Stakeholder request translator

Keep what the stakeholder meant and give engineers what they need to build it.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The request in the stakeholder's own words, who made it, when and why now.
- The process, team and systems involved, and a recent real example of the situation.
- Constraints they already know: deadlines, rules, budgets, people, systems that cannot change.
- Existing tickets, documents or earlier decisions about the same topic.

## Workflow

1. Copy the request word for word. Everything you write later must stay traceable to it.
2. Find the goal behind it: who is affected, what they cannot do today, what outcome they want, why it matters now and how they would know it worked. Separate the need from the solution they proposed ("add a button" may hide "approve orders faster").
3. List the ambiguous words and the missing facts ("quickly", "all customers", "reports", "like before"). Turn each into a question and ask for a concrete example or number.
4. Map the request to technical terms: the process steps, the screens or channels, the data and fields (new, changed, read-only), the roles and permissions, the notifications, the reports, the integrations with other systems, and the volumes and timing.
5. Describe the expected behaviour as concrete scenarios: given a situation, when something happens, then what the system does. Add the edge cases: empty data, wrong data, duplicates, no permission, another system down, a large volume.
6. Add non-functional needs only where they matter: performance, security and privacy, audit trail, retention, availability, accessibility, languages.
7. Write acceptance criteria that a person can check as pass or fail, using the stakeholder's own examples.
8. State assumptions, risks, dependencies and what is explicitly out of scope. Mark every technical detail you inferred as an assumption to confirm.
9. Read it back to the stakeholder in plain words, including what will not change, and ask them to confirm or correct. Record the decision and who made it.

## Rules

- Never invent technical facts; mark assumptions and ask the people who know.
- Describe the problem before the solution. A solution may stay as an option, labelled as such.
- Use the stakeholder's vocabulary in the plain version and the system's vocabulary in the technical version, with a short glossary linking them.
- Do not put personal data, credentials or confidential figures in the request.

## Output format

```
Original request (verbatim) | who | date
Goal and success measure
Clarifying questions (with the person who can answer)
Plain version (what you will get)  |  Technical version (what will be built)
Process / data / roles / integrations / reports
Scenarios: given / when / then, including edge cases
Non-functional needs
Acceptance criteria
Assumptions | risks | dependencies | out of scope
Glossary
Confirmation: who confirmed what, and when
```

## Quality checks

- The goal and the success measure are written, separate from any proposed solution.
- Every ambiguous word became a question or a concrete example.
- Edge cases and acceptance criteria are checkable.
- The stakeholder confirmed the plain version, and assumptions are labelled.
