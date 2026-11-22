---
name: requirements-quality-check
description: Check a set of requirements for clarity, testability, necessity, consistency and completeness: classify each one, rewrite vague ones, find duplicates, conflicts and gaps, check coverage of the goals, and propose priorities with reasons. Use before a specification is approved, a build starts or a vendor is asked to quote.
---

# Requirements quality check

Find the weak requirements while they are still cheap to fix.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The requirements as written (list, document, tickets or notes) and where each came from.
- The goals and success measures they are supposed to serve.
- The roles, systems and rules that exist today, and known constraints.
- How requirements will be used: a build, a vendor quote, a test plan, a contract annex.

## Workflow

1. Classify each requirement: business need, functional behaviour, data, business rule, non-functional (performance, security, privacy, audit, availability, accessibility, language), constraint or assumption.
2. Test each one against the checklist: one idea only; clear and unambiguous; testable with a pass or fail; necessary for a goal; feasible; consistent with the others; written as a need, not as a hidden solution; traceable to a source.
3. Flag vague words and rewrite them with something measurable: "fast", "easy", "user-friendly", "as needed", "etc.", "flexible", "all". Ask for the number, the example or the rule that fills each gap.
4. Add acceptance criteria where they are missing, as given, when and then statements or measurable thresholds.
5. Find duplicates and conflicts, and decide which stays or who must decide.
6. Look for gaps: roles and permissions, error and empty states, data volumes, migration of existing data, reporting, audit and retention, notifications, integrations, languages, support and training, and what happens when a dependency fails.
7. Check coverage: every goal should be served by at least one requirement, and every requirement should serve a goal. Remove or question those that serve none.
8. Propose priorities (must, should, could, won't now) with the reason for each, and mark risks and open questions.
9. Give a verdict per requirement (ready, needs rewrite, needs a decision, remove) and a short summary of the biggest problems.

## Rules

- Do not change the meaning of a requirement while rewriting it; when unsure, ask the source.
- Keep every change traceable to the original wording.
- A requirement that cannot be tested is not finished; say so.
- Do not copy confidential details from one stakeholder's material into another's.

## Output format

```
Summary: counts by verdict | biggest problems
Table: id | type | original | problem | rewrite | acceptance criterion | priority + reason | verdict
Duplicates and conflicts
Gaps found
Goal coverage: goal | requirements | gap
Open questions and decisions needed (owner, date)
```

## Quality checks

- Each requirement has a type, a verdict and, if not ready, a concrete fix.
- Vague words are replaced by measurable statements or by questions.
- Gaps and conflicts are listed with owners.
- Every goal is covered, and no requirement is without a goal.
