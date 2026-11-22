---
name: integration-readiness-checklist
description: Check whether a customer integration with a product or a third-party system is ready to build, test and go live: systems and owners, data flows, authentication, environments, error handling, test cases and responsibilities. Use when a customer, supplier or partner connection is part of an onboarding.
---

# Integration readiness checklist

Find what is missing before the integration is built, not after it fails in production.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The business purpose: what should happen in system A when something happens in system B, and who benefits.
- The systems on both sides: names, versions, owners, how each exposes or receives data (API, file, webhook, queue) and links to their documentation.
- Volumes and timing: how much data, how often, real time or scheduled, peak periods.
- Environments and access: test and production endpoints, credentials process, network rules.
- Contacts: the technical owner on each side and who decides on changes.

## Workflow

1. Describe each data flow in one line: trigger, source, destination, content, direction and frequency.
2. For each flow list the fields that matter, their format, which are required, who owns the master data and how conflicts are resolved.
3. Check authentication and authorisation: method, who issues and rotates the credentials, scopes needed, where secrets are stored. Never ask for secrets in a chat or document.
4. Check environments: a test environment on both sides, realistic test data, how to reset it and who can.
5. Define error handling: what counts as a failure, retries, duplicates and idempotency, timeouts, how failures are reported, who fixes them and in what time.
6. Define limits and constraints: rate limits, maintenance windows, versioning and deprecation policy, data protection and where data may be processed.
7. Write test cases: the normal flow, boundary values, wrong or missing data, the other system being down, and a duplicate message.
8. Assign responsibilities with a table (who builds, tests, monitors and supports each part) and agree the support path for incidents.
9. Give a verdict per flow: ready, ready with conditions, or blocked, and list what is needed to unblock.

## Rules

- Read the other system's documentation and note any ambiguity as a question, not an assumption.
- Do not go live without a failure path that a person will see.
- Treat personal data as a requirement, not an afterthought: what is sent, why and where it is stored.
- Keep credentials and real customer data out of the checklist.

## Output format

```
Integration: <purpose> | systems | owners
Flows: # | trigger | from -> to | content | frequency | master data owner
Authentication and environments
Errors and recovery: failure | detection | retry/handling | owner | time
Limits and constraints
Test cases: case | input | expected result | status
Responsibilities: build | test | monitor | support
Verdict per flow and what unblocks it
Questions for the other side
```

## Quality checks

- Each flow has an owner and a failure path.
- Test cases include the bad cases and the other system being down.
- Questions to the other side are explicit, with a person to answer them.
- No secrets or real personal data are in the document.
