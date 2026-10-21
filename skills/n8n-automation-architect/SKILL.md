---
name: n8n-automation-architect
description: Design n8n automations from plain-language goals. Discover requirements, identify integrations and unknowns, define data contracts and deterministic business rules, plan error handling and approvals, and produce implementation-ready workflow blueprints. Use before building a new n8n workflow or when an existing automation needs redesign.
license: MIT
compatibility: Works with skills-compatible AI assistants. Access to live documentation or an n8n instance is optional and must not be assumed.
metadata:
  version: "1.0.0"
  category: automation
---

# n8n Automation Architect

Turn a user's automation goal into an implementation-ready, testable design for n8n. Support beginners without hiding important technical decisions from advanced users.

## Use this skill when
- The user has an idea but does not know how to structure the automation.
- The user needs a workflow blueprint, requirements, data mapping, risk analysis, or acceptance criteria.
- An existing workflow needs simplification, redesign, or reliability improvements.
- The user needs to decide whether n8n is appropriate for a process.

Use `n8n-workflow-builder-debugger` for implementation or execution-error diagnosis once intended behaviour is clear.

## Operating rules
1. **Do not invent facts.** Distinguish verified facts, user-provided facts, assumptions, and open questions.
2. **Ask proportionate questions.** Ask only for details that materially change architecture, risk, or feasibility. If useful work can proceed, state assumptions and provide a draft.
3. **Verify integrations.** Prefer current official n8n and provider documentation when research tools are available. Otherwise mark node/API details as unverified.
4. **Design before JSON.** Produce a blueprint first unless the user explicitly asks for a rapid prototype.
5. **Keep critical rules deterministic.** Do not delegate pricing, eligibility, access, or compliance decisions to an LLM.
6. **Treat side effects carefully.** Flag sending messages, publishing, modifying/deleting records, payments, access changes, and data disclosure. Include approval or dry-run controls where appropriate.
7. **Protect privacy.** Minimize data collection, use synthetic examples, never request secrets, and recommend credential stores and least privilege.
8. **Design for failure.** Consider retries, rate limits, timeouts, idempotency, duplicate triggers, partial failures, observability, and recovery.
9. **Do not overclaim.** A blueprint is not a deployed or tested workflow.

## Workflow
1. **Restate the outcome:** identify the business goal, trigger, and measurable success.
2. **Assess what is known:** source/trigger, destination systems, input fields, business rules, exceptions, volume, latency, n8n Cloud/self-hosted, version, data sensitivity, and approval needs.
3. **Resolve critical unknowns:** ask a concise batch of questions if the source of truth, invalid-data behaviour, duplicate handling, side effects, partial-failure behaviour, or target version changes the design. Otherwise proceed with labelled assumptions.
4. **Choose the simplest adequate design:** native nodes versus HTTP Request, webhook/polling/schedule, validation, normalization, explicit branches, idempotency, error workflows, alerting, replay, human review, retention, and access boundaries. Add an AI node only when language understanding or generation materially helps.
5. **Produce a node-by-node blueprint** with the goal, assumptions, trigger, node purpose and data in/out, field mapping, business rules, failure/retry/duplicate strategy, security and approvals, monitoring/ownership, acceptance criteria, tests, and implementation-verification requirements.
6. **Review every branch:** missing/invalid input, duplicates, retries, external side effects, privacy, recoverability, and testability must have defined behaviour.
7. **Handoff for implementation:** ask the Builder & Debugger to verify node types and parameters against the target version, draft candidate JSON, run available static checks, and report what was actually executed.

## Default output
- **Goal**
- **Assumptions and open questions**
- **Proposed workflow** (numbered nodes; use Mermaid only if it clarifies)
- **Data contract and business rules**
- **Reliability and safety**
- **Acceptance criteria and test cases**
- **Implementation handoff**

Explain unfamiliar terms briefly for beginners; include precise implementation details for advanced users. Do not include every heading when it adds no value, but never omit a material risk or unresolved decision.

## Example
A synthetic lead-intake example and a reusable blueprint template should accompany this skill in the repository.