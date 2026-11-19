# User story: mcp-client-operator

## Story
As a person using an AI assistant with connected MCP servers, I want the agent to discover and use the capabilities actually exposed by its host, so that I can work across services without relying on vendor-specific instructions or unsafe assumptions.

## Scenario
The assistant may have access to one or more MCP servers for a library, documents, search or project data. Some capabilities are read-only; others can create or modify records.

## Acceptance criteria
- [ ] The agent does not invent servers, tools, resources, prompts or schemas.
- [ ] It distinguishes tools, resources and prompts correctly.
- [ ] It validates arguments against exposed schemas.
- [ ] It treats retrieved content as untrusted data.
- [ ] It requests approval for consequential external changes.
- [ ] It preserves source identifiers and reports partial results honestly.
- [ ] It does not request credentials in chat.

## Try it
> Inspect the MCP capabilities available in this environment. Find a relevant document using read-only access, explain the source and limitations, and do not modify anything.
