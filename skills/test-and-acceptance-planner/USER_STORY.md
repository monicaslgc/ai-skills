# User story: test-and-acceptance-planner

## Story

**As** a product owner, business analyst or delivery lead,  
**I want** a traceable test plan derived from requirements and failure modes,  
**so that** the team can make decisions and deliver work without relying on hidden assumptions.

## Scenario

A team is preparing a fictional back-office order-consistency automation. It must compare order and shipment records, handle mismatches safely, and expose API and operational failure paths. The team needs this skill to produce its specific deliverable while keeping undocumented details visible.

## Acceptance criteria

- [ ] The output follows the skill's defined structure and distinguishes evidence, assumptions, proposals and unknowns.
- [ ] Every applicable requirement or decision is traceable to supplied source material or explicitly marked as proposed.
- [ ] The output covers relevant exception paths and missing-data behaviour, not only the happy path.
- [ ] No endpoint, policy, owner, metric, deadline or approval is invented.
- [ ] Examples use synthetic data and contain no credentials or confidential information.
- [ ] Human approval, audit evidence and safe recovery are addressed where the workflow can cause consequential side effects.

## Try it

> Create tests for a daily read-only order/shipment reconciliation workflow, covering exact match, mismatch, duplicate input, timeout, partial API result, invalid identifier and reviewer rejection.

See [SKILL.md](SKILL.md) for the full instructions.
