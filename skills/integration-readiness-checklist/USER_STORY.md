# User story: integration-readiness-checklist

## Story

**As** a customer operations or implementation manager,
**I want** to check an integration is ready before it is built,
**so that** the customer's IT team and our engineers do not find missing details during the test or after go-live.

## Scenario

A customer wants bookings sent from their system to ours and confirmations sent back. Nobody has yet agreed who monitors failures or what happens on a duplicate.

## Acceptance criteria

- [ ] Each data flow is described with trigger, source, destination, content and frequency.
- [ ] Authentication, environments and limits are covered without secrets.
- [ ] Errors, retries, duplicates and who sees failures are defined.
- [ ] Test cases include bad data and the other system being down.
- [ ] Responsibilities are assigned and each flow has a verdict.
- [ ] Questions for the other side are explicit.

## Try it

> Check the readiness of this integration between the customer's system and ours from these notes and their API documentation. List what is missing and give a verdict per flow.

See [SKILL.md](SKILL.md) for the full instructions.
