# Workflows

Each workflow chains several skills into a complete job from start to finish. A workflow does not run by itself: you (or your agent) follow it step by step, one skill at a time, and a person reviews the output at every gate.

## How the chains work

- The output of one step is the input of the next. Carry forward the open items, assumptions and decisions.
- The `INTERNAL` line at the end of a skill's output never goes to the customer, the recipient or the next external document.
- Gates are decisions for a person: approve, correct or stop. No workflow sends anything on its own.
- If a step finds conflicting facts or missing information, resolve it before moving on; the later steps inherit the mistake otherwise.
- Install every skill a workflow uses (they may live in different kits). Each workflow file lists them.

## Workflows

| Workflow | Use it to |
|---|---|
| [Customer onboarding, from signature to handover](customer-onboarding-to-handover.md) | Take a new customer from signed contract to a running, documented solution that their own team can operate. |
| [Renewal season, from health check to signed renewal](renewal-season.md) | Reach the notice deadline with an honest picture of the customer's health, a prepared conversation and the paperwork ready. |
| [Incident, from first message to lasting fix](incident-to-learning.md) | Keep customers informed honestly during an incident, hand engineering what it needs, and turn the incident into a fix and updated guidance. |
| [Business request to buildable work](request-to-delivery.md) | Turn a non-technical request into checked requirements, a clear story and a plan engineering can start on. |
| [New client project, from scope to first status report](client-project-kickoff.md) | Start a client project with an agreed scope, a charter, a risk log and a rhythm of reporting. |
| [Monthly client reporting](monthly-client-reporting.md) | Produce a monthly service report with checked figures, a clear message and a meeting that ends in decisions. |
| [Document an existing app](document-an-existing-app.md) | Produce guides that match how the app really works, with diagrams, and keep them current. |
| [Job application, from posting to first 90 days](job-application.md) | Apply with truthful, tailored documents and prepare to start well. |
