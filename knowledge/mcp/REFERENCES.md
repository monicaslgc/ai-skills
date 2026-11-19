# MCP References

Accessed: 2026-11-19. The MCP specification is actively maintained; always check the version supported by the client and server before implementing protocol-level details.

## Primary sources

1. **Model Context Protocol maintainers — Specification, version 2026-07-28.** Authoritative protocol requirements and schemas.  
   https://modelcontextprotocol.io/specification/2026-07-28  
   Supports: protocol overview, normative requirements, primitives, versioning and security baseline.

2. **Model Context Protocol maintainers — Architecture, version 2026-07-28.**  
   https://modelcontextprotocol.io/specification/2026-07-28/architecture  
   Supports: host/client/server roles, data and transport layers, trust boundaries and capability negotiation.

3. **Model Context Protocol maintainers — Tools, version 2026-07-28.**  
   https://modelcontextprotocol.io/specification/2026-07-28/server/tools  
   Supports: tool discovery, schemas, invocation and human oversight considerations.

4. **Model Context Protocol maintainers — Resources, version 2026-07-28.**  
   https://modelcontextprotocol.io/specification/2026-07-28/server/resources  
   Supports: resource discovery, retrieval, URI-based context and optional subscriptions.

5. **Model Context Protocol maintainers — Prompts, version 2026-07-28.**  
   https://modelcontextprotocol.io/specification/2026-07-28/server/prompts  
   Supports: prompt discovery, arguments and retrieval.

6. **Model Context Protocol maintainers — Transports, version 2026-07-28.**  
   https://modelcontextprotocol.io/specification/2026-07-28/basic/transports  
   Supports: transport-level distinctions and connection behaviour.

7. **Model Context Protocol maintainers — Authorization, version 2026-07-28.**  
   https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization  
   Supports: HTTP authorisation flows and security requirements. Use the current specification rather than copying older OAuth tutorials.

8. **Model Context Protocol maintainers — Security Best Practices.**  
   https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices  
   Supports: implementation security guidance and threat mitigation.

9. **Model Context Protocol maintainers — Elicitation, version 2026-07-28.**  
   https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation  
   Supports: user-input requests, consent, sensitive information restrictions and external authorisation patterns.

10. **Model Context Protocol maintainers — 2026-07-28 specification release notes.**  
    https://modelcontextprotocol.io/blog/2026-07-28-spec-ga  
    Supports: release context and changes in the 2026-07-28 specification.

## Interpretation and currency notes

- The official specification is the normative source. Tutorials, SDK examples and third-party server READMEs are implementation guidance and may lag.
- The protocol evolves. Older material may describe stateful sessions, transports, sampling or authorisation behaviour that differs from the current specification.
- The 2026-07-28 specification marks the former sampling feature deprecated. Verify current client/server support and deprecation status before relying on it.
- MCP does not certify server trustworthiness. Security recommendations in this knowledge base are operational guidance synthesised from the protocol's security and consent requirements.
- This repository does not endorse a specific MCP server registry, vendor, client or book platform.
