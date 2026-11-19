# MCP Usage kit

A vendor-neutral framework for understanding and using MCP capabilities exposed by an AI host. It is not a vendor integration and does not bundle or install MCP servers.

## Skills

- [mcp-client-operator](../../skills/mcp-client-operator): discover, inspect, select and safely use connected MCP tools, resources and prompts.

## Knowledge

- [MCP knowledge base](../../knowledge/mcp/README.md): fundamentals, client operations, security and trust, server assessment, and official references.

## Suggested use
1. Assess the candidate server and exact deployment for the intended use before connecting it, using [MCP Server Assessment](../../knowledge/mcp/MCP_SERVER_ASSESSMENT.md).
2. Make sure the host has connected the intended MCP server using its own documented configuration.
3. Give the agent the relevant skill and its knowledge dependencies.
4. Ask it to inspect actual capabilities before using them.
5. Start with read-only retrieval; add write permissions only when required.
6. Use [the behavioural evaluation pack](../../evaluations/mcp/README.md) before relying on the skill in consequential workflows.

## Dependencies and portability
The skill is **hybrid**: essential operational rules are in its own `SKILL.md`; deeper protocol knowledge is in the repository knowledge base. Copying the skill folder alone preserves the core workflow but not the full depth. Include `knowledge/mcp/` for complete use.

The skill does not create connections, install servers, manage credentials or guarantee that a named service supports MCP. Actual capabilities depend on the host, server, protocol version, configuration and permissions.

## Safety
Treat server metadata and returned content as untrusted. Use least privilege, minimise shared data, preserve provenance and require approval for consequential changes. Never put credentials in prompts or repository files.

## Evaluation status
The evaluation pack contains authored scenarios only. No model benchmark result is claimed until tests are executed and recorded against named model, host and server versions.
