# User story: n8n-automation-architect

## Story
**As** someone who wants to automate a business process,
**I want** an n8n blueprint with clear requirements, data mapping, failure handling and acceptance criteria,
**so that** I can review the design before building it.

## Scenario
A small team wants to capture website leads, validate their details, create a CRM record and notify sales. Some submissions may be incomplete or duplicated.

## Acceptance criteria
- [ ] The trigger, source of truth and destinations are explicit.
- [ ] Assumptions and unanswered questions are separated from known facts.
- [ ] The blueprint specifies required fields and invalid-data behaviour.
- [ ] Duplicate handling, retries and partial failures are addressed.
- [ ] High-impact side effects have approval or safe test controls.
- [ ] Acceptance criteria can be tested without real personal data.

## Try it
> Design an n8n workflow for website lead intake. Validate required fields, prevent duplicate CRM records, and notify sales only after a record is successfully created. Use synthetic examples and call out anything that depends on the CRM or n8n version.

See [SKILL.md](SKILL.md) for the full instructions.