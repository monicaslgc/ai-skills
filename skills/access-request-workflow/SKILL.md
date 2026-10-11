---
name: access-request-workflow
description: Design an access management workflow: requests, approvals, least privilege, joiners, movers and leavers, periodic reviews and audit records. Use when setting up how people get and lose access to systems, or when access is inconsistent or untracked.
---

# Access request workflow

Give people the access they need quickly, and remove it reliably when they no longer need it.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- Systems and the roles that use them.
- Current way access is requested and granted.
- Policies for sensitive systems.
- Teams involved: managers, IT, security, HR.

## Workflow

1. Inventory systems and classify them by sensitivity. List standard access bundles per role.
2. Define the request flow: who can request, what information is required, who approves (manager, system owner, security for sensitive access) and time limits.
3. Define joiner steps: access provisioned from the role bundle on the start date, with a record.
4. Define mover steps: remove access no longer needed when a role changes, add what is new.
5. Define leaver steps: revoke all access on the last day, including shared accounts and tokens, and transfer ownership of resources.
6. Define periodic access reviews: who reviews what, how often, and what happens to unconfirmed access.
7. Define the audit trail: who requested, who approved, when, and what was granted or removed.
8. Define emergency and temporary access with an expiry date.

## Output format

| Event | Trigger | Steps | Owner | Time limit | Record |
|---|---|---|---|---|---|

Role access bundles, approval matrix, review schedule, audit fields.

## Safety

- Default to least privilege and time-limited access for sensitive systems.
- Never record passwords or tokens in requests or logs.
- Separate the person who requests access from the person who approves it.
