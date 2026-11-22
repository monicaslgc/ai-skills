---
name: requirements-elicitation-plan
description: Plan how to discover requirements: map the stakeholders, choose techniques (interviews, workshops, observation, document and data analysis, surveys, prototype reviews), prepare questions and capture templates, and decide how to validate and reconcile what you hear. Use at the start of a project, a new feature or a redesign.
---

# Requirements elicitation plan

Find out what is really needed before deciding what to build.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The goal of the project or feature, the problem it addresses and any decisions already made.
- The people and groups affected, and how much time you can ask of them.
- Existing material: process documents, tickets, support data, reports, screenshots of current tools.
- Constraints: deadline, budget, regulations, systems that must stay.

## Workflow

1. Map the stakeholders: who uses the process, who owns it, who decides, who pays, who maintains, who is affected downstream, and who is rarely heard (night shift, field staff, new starters). Note their interest, influence and what they fear.
2. Choose techniques per group: interviews for individual detail, workshops for shared decisions and conflicts, observation for what people really do, document and ticket analysis for history, data analysis for volumes and exceptions, surveys for breadth, prototype reviews for reactions.
3. Prepare questions by theme: goals and outcomes, today's process step by step, pain points and workarounds, exceptions and rare cases, data and reports, rules and approvals, volumes and timing, security and compliance, success measures, constraints. Prefer "tell me about the last time…" to "what would you like?".
4. Plan the sessions: who, when, how long, what to bring, and a one-page guide per session. Ask for real recent examples and sample data in advance.
5. Prepare the capture: a template for notes, a log of needs with the speaker and the source, a glossary of terms, and a list of decisions and open questions.
6. Run the sessions: listen first, ask for examples, repeat back what you heard, separate needs from proposed solutions, and note disagreements instead of smoothing them over.
7. Triangulate: compare what people say with what the documents, tickets and data show, and with what you observe.
8. Validate and reconcile: send the findings back for correction, bring conflicting stakeholders together with the evidence, and record who decided what.
9. Turn the results into requirements (see [`requirements-quality-check`](../requirements-quality-check)) and decide what remains unknown and how to find out.

## Rules

- Observe real work when you can; people describe the ideal process more often than the real one.
- Do not lead the answer; avoid questions that contain the solution.
- Record who said what and the evidence; a need without a source cannot be defended or challenged.
- Respect confidentiality: use the minimum personal and commercial data needed.

## Output format

```
Goal and scope
Stakeholder map: group | role | interest | influence | how to reach | risk
Techniques per group and why
Question list by theme
Session plan: date | group | method | duration | guide | owner
Capture templates: needs log, glossary, decisions, open questions
Validation and conflict plan
Risks and unknowns
```

## Quality checks

- Every affected group, including the quiet ones, has a way to be heard.
- Questions ask for examples and facts, not only opinions.
- At least two sources support each important need.
- Conflicts and unknowns are listed with a plan to resolve them.
