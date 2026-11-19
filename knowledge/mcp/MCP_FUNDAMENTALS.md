# MCP Fundamentals

## 1. What MCP is — and is not

The Model Context Protocol (MCP) is an open protocol for communication between an AI application and external servers that provide context or capabilities. It standardises how a host application can connect to multiple specialised servers without each integration inventing a completely different interface.

MCP is an interoperability protocol, not:
- a guarantee that a service has an MCP server;
- a directory or certification scheme for trustworthy servers;
- a guarantee that a connected server is safe, accurate or authorised;
- a replacement for the host application's permission model;
- an agent, model, workflow engine or database;
- proof that every MCP client supports every protocol feature.

A connection proves only that a particular client can communicate with a particular server under a particular configuration and permission set.

## 2. Architecture and trust boundaries

The conceptual roles are:

| Role | Responsibility |
|---|---|
| Host | The AI application. Manages user interaction, model context, client lifecycle, permissions and consent. |
| Client | A protocol component managed by the host. Maintains a connection to one server and speaks MCP. |
| Server | Exposes a bounded set of context or capabilities to a client. May wrap local data, a local application or a remote service. |

A host can manage multiple clients, generally one client connection per server. Servers should not be assumed to see the full conversation or the capabilities of other servers. The host mediates what context and operations are exposed.

**Operational implication:** an agent skill runs inside the host's boundaries. It can inspect and use only the servers, tools, resources and prompts made available to it by that host. It cannot independently install, configure, authenticate or connect to a server unless the host explicitly provides a mechanism for those actions.

## 3. Protocol layers

MCP has two useful conceptual layers:

- **Data layer:** JSON-RPC-based messages, protocol versioning, capability negotiation, requests, responses, notifications and the protocol's primitives.
- **Transport layer:** how messages move between client and server, including connection establishment, framing and transport-specific security.

Do not confuse a transport with a capability. A server reachable over HTTP is not necessarily authorised to access a user's account; a server launched locally is not automatically trustworthy.

## 4. Core server primitives

### Tools

Tools are executable operations that a model-controlled application may invoke. Examples include searching a catalogue, reading a record, querying a database or creating a draft.

A tool definition commonly includes:
- a unique name;
- a human-readable description;
- an input schema, commonly JSON Schema;
- optional annotations or output schema, depending on server and protocol version.

Tool descriptions and annotations help selection but are not security guarantees. Validate arguments against the actual schema and understand side effects before invocation.

### Resources

Resources expose addressable context, often identified by a URI. They are generally intended to provide data for an application or model to inspect, such as a document, catalogue record, file or database schema.

Resources are not automatically harmless: reading them can expose sensitive information, and their contents can contain malicious or misleading instructions. Resource availability, URI schemes, templates and subscription support depend on server capabilities and host support.

### Prompts

Prompts are reusable templates exposed by a server. They may include arguments and return structured prompt messages intended to guide a task.

A prompt is not a trusted policy override. Treat it as server-supplied content and reconcile it with the user's request, host policy and higher-priority instructions.

### Comparison

| Primitive | Main question | Typical use | Risk to consider |
|---|---|---|---|
| Tool | What operation can be invoked? | Search, update, export, calculate | Side effects, data disclosure, destructive operations |
| Resource | What context can be read? | Document, record, schema, catalogue entry | Sensitive data, stale data, prompt injection |
| Prompt | What reusable task template is available? | Search workflow, report structure | Instruction conflict, unsafe assumptions, hidden scope |

A server may expose any subset of these. Never infer that the absence of one primitive means the server is broken.

## 5. Client-side features and extensions

Depending on the protocol revision and host implementation, clients may support features such as roots, elicitation or sampling. These are not equivalent to server tools/resources/prompts.

- **Roots** can communicate filesystem boundaries or context about directories a client makes available. They do not grant a server unrestricted filesystem access.
- **Elicitation** lets a server request additional user input through the client. It is not permission to ask for passwords or secrets through an ordinary form. Sensitive authorisation should use a secure external authorisation flow.
- **Sampling** historically allowed a server to request model generation through the client. Its status is version-dependent; the 2026-07-28 specification marks the former sampling feature deprecated. Do not design new workflows around it without checking the selected protocol version and host support.
- **Extensions** add optional capabilities. They require explicit support and negotiation; do not assume they exist because they appear in a specification or another client.

The protocol evolves. Always use the specification version supported by the actual client/server pair rather than copying examples from an older tutorial.

## 6. Capability and version negotiation

MCP participants advertise supported protocol versions and capabilities. A capability indicates support for a feature; it does not prove that the feature is enabled for a particular user, account or resource.

An operator should distinguish:
1. protocol-level support;
2. server-advertised capability;
3. host/client implementation support;
4. user/account authorisation;
5. actual availability of a particular item or operation.

A failure at one layer should not be misreported as a failure at another.

## 7. Transports

Common transports in the current specification include:

- **stdio:** the host launches or manages a local process and communicates over standard input/output. Appropriate for local integrations; process execution and environment configuration become part of the trust boundary.
- **Streamable HTTP:** a client communicates with a remote server over HTTP, with streaming support as defined by the transport. Authentication and network exposure must be configured correctly.

Transport support and authentication details are version-sensitive. Use official transport and authorisation documentation for exact wire behaviour. Never invent command lines, endpoints, headers or OAuth scopes.

## 8. A useful mental model

Think of MCP as a typed capability interface:
- the host decides what is connected and exposed;
- the server declares what it offers;
- the client discovers and exchanges protocol messages;
- the agent selects among the capabilities the host exposes;
- the user and host remain responsible for consent and permission boundaries.

The protocol standardises the interface. It does not make the underlying operation safe, truthful, authorised or appropriate.
