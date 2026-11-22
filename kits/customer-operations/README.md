# Customer operations kit

Skills for running a portfolio of customers from signature to steady state: onboarding projects, workshops, integrations, go-live and hypercare, health and adoption, feedback to product, escalations and business reviews.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`customer-onboarding-project-plan`](../../skills/customer-onboarding-project-plan) | Plan an onboarding with goals, scope, milestones, owners, risks and go-live criteria |
| [`configuration-workshop-planner`](../../skills/configuration-workshop-planner) | Plan and run a workshop that ends with decisions and a configuration sheet |
| [`integration-readiness-checklist`](../../skills/integration-readiness-checklist) | Check an integration is ready to build, test and go live |
| [`go-live-and-hypercare-plan`](../../skills/go-live-and-hypercare-plan) | Plan a safe go-live with a rollback and a watched hypercare period |
| [`customer-health-scorecard`](../../skills/customer-health-scorecard) | Score customer health from transparent signals, with reasons and next actions |
| [`adoption-review`](../../skills/adoption-review) | Compare usage with expected value and plan targeted interventions |
| [`customer-feedback-to-product-brief`](../../skills/customer-feedback-to-product-brief) | Turn scattered feedback into an evidenced brief for Product and Engineering |
| [`engineering-escalation-brief`](../../skills/engineering-escalation-brief) | Escalate a customer issue to Engineering with everything they need |
| [`business-review-pack`](../../skills/business-review-pack) | Prepare an honest customer business review |
| [`rollout-coordination-plan`](../../skills/rollout-coordination-plan) | Coordinate a rollout across product, engineering, partners and the customer's IT |
| [`customer-playbook-builder`](../../skills/customer-playbook-builder) | Turn a recurring customer situation into a playbook and mark what can be automated |
| [`renewal-and-expansion-plan`](../../skills/renewal-and-expansion-plan) | Plan a renewal from the notice deadline and the growth conversation from evidence |
| [`customer-incident-communication`](../../skills/customer-incident-communication) | Write honest customer messages during and after an incident |
| [`international-customer-communication`](../../skills/international-customer-communication) | Communicate clearly across languages, cultures and time zones |
| [`ai-in-customer-operations-guardrails`](../../skills/ai-in-customer-operations-guardrails) | Decide where AI helps in customer work, and set limits, approvals and data rules |

## Suggested order

1. Plan the onboarding with `customer-onboarding-project-plan`.
2. Set up with the customer using `configuration-workshop-planner` and `integration-readiness-checklist`.
3. Go live with `go-live-and-hypercare-plan`.
4. In steady state, follow `customer-health-scorecard` and `adoption-review`.
5. Pass problems on with `engineering-escalation-brief` and `customer-feedback-to-product-brief`.
6. Review with the customer using `business-review-pack`, and plan the renewal with `renewal-and-expansion-plan`.

Along the way: `rollout-coordination-plan` for launches that involve several organisations, `customer-playbook-builder` to capture what works, `customer-incident-communication` when something breaks, `international-customer-communication` for mixed audiences and `ai-in-customer-operations-guardrails` for using AI safely.

## Install the whole kit

```bash
git clone https://github.com/monicaslgc/ai-skills.git
for s in customer-onboarding-project-plan configuration-workshop-planner integration-readiness-checklist go-live-and-hypercare-plan customer-health-scorecard adoption-review customer-feedback-to-product-brief engineering-escalation-brief business-review-pack rollout-coordination-plan customer-playbook-builder renewal-and-expansion-plan customer-incident-communication international-customer-communication ai-in-customer-operations-guardrails; do cp -r ai-skills/skills/$s ~/.claude/skills/; done
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
foreach ($s in 'customer-onboarding-project-plan','configuration-workshop-planner','integration-readiness-checklist','go-live-and-hypercare-plan','customer-health-scorecard','adoption-review','customer-feedback-to-product-brief','engineering-escalation-brief','business-review-pack','rollout-coordination-plan','customer-playbook-builder','renewal-and-expansion-plan','customer-incident-communication','international-customer-communication','ai-in-customer-operations-guardrails') {
  Copy-Item -Recurse "ai-skills\skills\$s" "$env:USERPROFILE\.claude\skills\"
}
```

These skills need no tools or servers. Each skill folder has a `USER_STORY.md` with a scenario and an example prompt.

All examples are invented. Do not paste real customer data, credentials or confidential contract text into a chat you do not control.
