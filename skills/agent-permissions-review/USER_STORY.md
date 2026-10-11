# User story: agent-permissions-review

## Story

**As** a person responsible for the safety of an AI agent,
**I want** a review of what the agent can access and change,
**so that** the agent has only the permissions it needs, and I know the worst case.

## Scenario

Our assistant reads incoming email and can also send messages and edit files.

## Acceptance criteria

- [ ] Every tool, credential and data source is inventoried.
- [ ] Untrusted input combined with powerful tools is flagged.
- [ ] Blast radius is estimated for each permission.
- [ ] Changes are ranked by risk reduction.
- [ ] No real secret is requested or shown.

## Try it

> Review the permissions of an assistant that reads email and can send messages and edit shared documents.

See [SKILL.md](SKILL.md) for the full instructions.
