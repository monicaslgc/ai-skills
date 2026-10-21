# User story: n8n-workflow-builder-debugger

## Story
**As** an n8n user implementing or fixing a workflow,
**I want** candidate workflow JSON, explicit validation status and a reproducible test plan,
**so that** I can import and verify the workflow without relying on invented configuration.

## Scenario
A workflow fails because an expression expects a field that is absent from some incoming items. The user has a sanitized export and a sample execution.

## Acceptance criteria
- [ ] The diagnosis cites observed evidence and separates it from hypotheses.
- [ ] The fix is minimal and its behaviour change is explained.
- [ ] No credentials or sensitive payloads are reproduced.
- [ ] Candidate JSON is clearly distinguished from imported/executed workflow.
- [ ] Tests include the missing-field case and at least one normal case.
- [ ] Validation claims identify exactly which checks ran.

## Try it
> Here is a sanitized n8n workflow export and error message. Find the likely root cause, propose the smallest safe fix, and give me tests. Do not claim the JSON was imported or executed unless you actually verify that.

See [SKILL.md](SKILL.md) for the full instructions.