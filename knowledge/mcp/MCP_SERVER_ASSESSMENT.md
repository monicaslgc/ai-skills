# MCP Server Assessment

A vendor-neutral method for deciding whether an MCP server is suitable to connect to an AI host, and under what constraints. This is an operational risk assessment, not a security certification, penetration test, legal opinion or guarantee of safety.

## 1. Purpose and decision

Assess a specific server deployment, not merely a product name or repository. The same server software can have materially different risk depending on version, transport, configuration, credentials, network exposure, enabled capabilities and the data it can reach.

The assessment must produce one of four decisions:

- **Accept** — suitable for the stated use and scope, with documented controls.
- **Accept with restrictions** — suitable only with reduced permissions, isolated data, disabled capabilities or additional monitoring.
- **Defer** — evidence is insufficient; do not connect until named gaps are resolved.
- **Reject** — unacceptable risk, untrusted provenance, unsafe behaviour or no viable mitigation for the intended use.

A decision applies only to the assessed version and configuration. It is not a blanket endorsement of every deployment or future update.

## 2. Define the intended use first

Do not assess a server in the abstract. Record:

- Intended task and users.
- Data sources and sensitivity (public, internal, confidential, personal, regulated).
- Required operations: discovery, read, draft, write, publish, delete or administration.
- Expected volume, frequency and retention.
- Required availability and recovery expectations.
- Host/client, deployment environment and network boundary.
- Required MCP primitives and protocol features.
- Consequences of incorrect, unauthorised or unavailable operation.

Use the narrowest use case that provides value. A server that is acceptable for public catalogue search may not be acceptable for private document access or account modification.

## 3. Establish identity and provenance

Collect evidence for the exact server:

- Canonical project name and repository or publisher.
- Maintainer identity and organisational ownership, where verifiable.
- Official documentation and installation source.
- Release/version, commit or immutable artifact digest where available.
- Package publisher and distribution channel.
- Licence and dependency notices.
- Release history, security advisories and vulnerability reporting process.
- Whether the deployment is official, community-maintained, forked or internally modified.

Prefer evidence from the project's canonical repository, signed releases, package registry metadata and maintainer documentation. A popular listing, search result, README badge or download count is not proof of safety.

**Stop or defer** when the artifact's origin cannot be established sufficiently for the data and permissions involved. Do not execute an unknown package merely to discover what it does.

## 4. Review maintenance and supply-chain posture

Inspect:

- Recent meaningful releases and maintenance activity.
- Compatibility with the intended MCP protocol version and host.
- Open and resolved security issues, advisories and incident disclosures.
- Dependency age, known vulnerabilities and dependency provenance.
- Build/release process and availability of reproducible or signed artifacts.
- Whether versions can be pinned and updates reviewed before deployment.
- Whether the project documents support boundaries and deprecation policy.

Do not use commit frequency as a standalone quality metric. A stable project may change infrequently; an active project may still be unsafe. Record evidence and uncertainty rather than assigning trust based on popularity.

## 5. Map data flows and access boundaries

Create a simple data-flow map before connection:

1. What user or agent input enters the server?
2. What data can the server read?
3. What external services receive data?
4. What data is stored, cached, logged or retained?
5. What outputs return to the host?
6. Which identities and credentials authorise each step?
7. Can data cross tenant, project, library or user boundaries?

Check the actual deployment configuration, not only the documentation. Look for broad filesystem mounts, environment variables, network egress, database permissions, shared service accounts, telemetry, logging and backup locations.

Apply data minimisation:
- grant only the folders, collections, records and operations required;
- use read-only credentials for research where possible;
- avoid administrator or owner tokens;
- separate identities for distinct agents or environments;
- do not expose unrelated personal or confidential data;
- document retention and deletion behaviour.

If data flows cannot be understood, restrict the server to non-sensitive test data or defer/reject it.

## 6. Inventory MCP capabilities and side effects

Discover capabilities through the intended host/client or a controlled test environment. Record the actual advertised surface:

| Item | What to capture |
|---|---|
| Protocol | Negotiated version and supported capabilities |
| Tools | Exact name, description, input/output schema, annotations and side effects |
| Resources | URI schemes/templates, access scope, sensitivity and update behaviour |
| Prompts | Arguments, returned content and instruction risks |
| Client features | Roots, elicitation and other negotiated features, if supported |
| Transport | stdio or HTTP transport, endpoint/process boundary and security controls |
| Authentication | Identity, scopes, token audience, renewal and revocation path |
| Limits | Pagination, rate limits, timeouts, payload limits and concurrency |

For every tool, classify its impact:
- **Read:** retrieves or searches data.
- **Draft:** creates a non-final artefact.
- **Write:** changes records or configuration.
- **External action:** sends, publishes, shares or triggers another system.
- **Destructive/high impact:** deletes, overwrites, purchases, changes access or exposes sensitive information.

Descriptions and annotations are untrusted metadata, not guarantees. Inspect schemas and test behaviour safely. A tool labelled read-only may still have unexpected side effects; verify implementation or behaviour where the risk warrants it.

## 7. Evaluate security controls

Review the following proportionately to the deployment risk:

### Identity and authentication
- Is authentication required where appropriate?
- Are credentials scoped to the intended resource and audience?
- Are secrets stored and rotated through a secure mechanism?
- Can access be revoked promptly?
- Are unauthorised and expired credentials handled safely?

### Transport and deployment
- Is remote traffic protected with correctly configured TLS?
- Are endpoints restricted to intended networks?
- Are local processes isolated and run with minimal operating-system privileges?
- Are environment variables, temporary files and logs protected?
- Are inbound and outbound network paths understood?

### Input and output handling
- Are arguments validated against schemas and server-side constraints?
- Are paths, URIs, IDs and filters constrained to authorised scope?
- Are outputs bounded, encoded and handled without unsafe execution?
- Are errors free of secrets and unnecessary personal data?
- Can untrusted content influence downstream tool calls?

### Prompt injection and confused-deputy risk
- Can resources, prompts, tool descriptions or external content contain instructions?
- Does the host preserve the distinction between untrusted data and governing instructions?
- Can the server induce the agent to access unrelated data or invoke other tools?
- Are user intent and approval checked at the point of consequential action?

### Observability and incident response
- Are security-relevant actions auditable?
- Can logs be accessed by unauthorised users?
- Are secrets and sensitive content redacted?
- Is there an owner and a process for reporting, containing and recovering from incidents?

## 8. Test in a controlled environment

Do not begin with production data or broad credentials. Use synthetic data and a dedicated test identity.

Test at least:

1. **Capability accuracy:** advertised tools/resources/prompts match observed behaviour.
2. **Schema enforcement:** missing, malformed, oversized and unexpected arguments are rejected safely.
3. **Permission boundaries:** attempts to access out-of-scope records, folders or tenants fail.
4. **Read/write separation:** read-only credentials cannot modify data.
5. **Side effects:** write, publish and delete operations behave as documented and require the expected approval.
6. **Prompt injection:** malicious instructions in resource content do not trigger unrelated actions or data disclosure.
7. **Error handling:** authentication failures, timeouts, rate limits and unavailable dependencies fail safely.
8. **Pagination and limits:** results are complete or clearly marked partial; limits are respected.
9. **Data leakage:** logs, errors and outbound requests do not expose credentials or unrelated sensitive data.
10. **Verification:** consequential operations can be confirmed through an independent read or authoritative state.

Do not conduct intrusive security testing against a third-party service without explicit authorisation. Use the project's supported test environment and documented safe test procedures.

## 9. Risk rating and decision gates

Rate each dimension from 0 to 3:

- **0 — No material concern evidenced:** controls and evidence are adequate for this use.
- **1 — Low:** limited concern; routine controls are sufficient.
- **2 — Significant:** material gap; restrictions or remediation are required.
- **3 — Critical:** unacceptable for the proposed use; stop until resolved.

Dimensions:
- Provenance and publisher confidence.
- Maintenance and supply-chain posture.
- Data sensitivity and data-flow clarity.
- Permission scope and blast radius.
- Tool side effects and schema clarity.
- Transport, authentication and deployment security.
- Prompt-injection and output-handling resilience.
- Logging, incident response and recoverability.

Do not average away a critical finding. Any dimension scored 3 blocks acceptance for the intended use until mitigated and reassessed. A score of 2 requires a documented mitigation and an **Accept with restrictions** or **Defer** decision. Missing evidence is not a zero-risk score; mark it **unknown** and defer when it affects a material risk.

This rating is a prioritisation aid, not a validated quantitative security model. Record the rationale and evidence behind each rating.

## 10. Apply controls after acceptance

An accepted server should still be deployed with controls:

- Pin the assessed release or artifact where possible.
- Keep permissions at the minimum required.
- Start with read-only access and expand only when justified.
- Separate production from test identities and data.
- Require explicit approval for consequential operations.
- Monitor server, dependency and protocol security updates.
- Reassess after changes to version, configuration, transport, credentials, data scope or enabled tools.
- Maintain a rollback or disconnect procedure.
- Remove access when the use case ends.

Acceptance is not permanent. A material change invalidates the assessment until reviewed.

## 11. Assessment record

Keep a record with these fields:

| Field | Record |
|---|---|
| Server / deployment name | Exact identity |
| Canonical source | Repository, publisher and documentation |
| Version / artifact | Version, commit or digest |
| Assessment date | UTC date |
| Assessor / owner | Accountable person or team |
| Intended use | Specific task and users |
| Host / client | Product and version |
| Transport / endpoint | Actual configured transport; redact secrets |
| Protocol version | Negotiated version |
| Capabilities | Tools, resources, prompts and client features |
| Data classification | Data in scope and data flows |
| Permissions | Identity, scopes and accessible boundaries |
| Test evidence | Environment, fixtures and observed outcomes |
| Findings | Risks, unknowns and mitigations |
| Decision | Accept / Accept with restrictions / Defer / Reject |
| Restrictions | Exact controls and prohibited operations |
| Review trigger | Date or material-change event |

Do not store credentials, access tokens or sensitive payloads in the assessment record.

## 12. Relationship to MCP client operation

Server assessment answers: **Should this deployment be trusted for this use, and under what controls?**

MCP client operation answers: **Given the capabilities exposed by the host, how should the agent discover and use them for this task?**

Both are required for consequential workflows. A server that passed assessment does not remove the need to inspect its current capabilities, validate arguments, minimise data, obtain approvals and verify outcomes at runtime.

## Sources and limitations

Use the official MCP specification and security guidance in [REFERENCES.md](REFERENCES.md) for protocol requirements. Supplement these with the exact server's canonical documentation, release history, advisories and deployment configuration.

This assessment framework is general operational guidance. It does not replace a formal security review, penetration test, privacy impact assessment, vendor due diligence or legal review where those are required.
