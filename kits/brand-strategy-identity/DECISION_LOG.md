# Brand Decision Log

Use this log to preserve the rationale and authority behind brand decisions across skills and handoffs.

## Decision record template

### DEC-[NNN]: [Short decision title]
- **Status:** Draft | In Review | Approved | Locked | Superseded
- **Decision owner:**
- **Approver(s):**
- **Created / reviewed:** YYYY-MM-DD
- **Related stage / deliverable:**
- **Question to resolve:**
- **Options considered:**
- **Evidence:**
- **Decision and rationale:**
- **Trade-offs / risks:**
- **Impact on existing work:**
- **Review trigger / date:**
- **Supersedes / superseded by:**

## Status semantics

| Status | Meaning | May downstream skills treat it as a rule? |
|---|---|---|
| Draft | Working proposal, not yet reviewed | No |
| In Review | Submitted for human review | No |
| Approved | Explicitly accepted by the named decision owner | Yes, within stated scope |
| Locked | Approved and frozen for the current release / phase | Yes; changes require a change request |
| Superseded | Replaced by a later recorded decision | No; retain for history |

## Governance rules

- Only a named human decision owner can approve or lock a material brand decision.
- An agent may prepare options, compare evidence, flag contradictions and draft a recommendation; it cannot approve on behalf of a person.
- Never infer approval from silence, a completed workshop, a polished deliverable or a tool response.
- A change to an Approved or Locked decision requires a new record that references the previous decision and explains downstream impact.
- If two approved decisions conflict, stop the affected work and request resolution; do not choose silently.
- Preserve dissent and minority views where they materially affect implementation.
- Record approval evidence (for example, a dated written confirmation), not merely "approved".
