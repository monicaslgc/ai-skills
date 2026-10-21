# Workflow JSON checklist

## Before drafting
- Confirm the goal, target n8n version, deployment type, and approved side effects.
- Verify node types, node versions, operations, and parameters from official docs or a known-good export.
- Identify credentials as external configuration; never invent credential IDs.

## JSON integrity
- Parse with a JSON parser when available.
- Check required top-level fields and expected data types.
- Ensure node names are unique and connections reference existing nodes.
- Check expressions, node references, branch outputs, and expected item shape.
- Confirm every path has an intended outcome and error handling.

## Operational safety
- Use placeholders for URLs/IDs that the user must configure; never embed secrets.
- Review retries and duplicate side effects.
- Check pagination, binary data, rate limits, timeouts, and credential scopes.
- Include a disabled/manual test path where appropriate.
- Confirm error paths do not accidentally send success notifications or repeat writes.

## Report honestly
State separately whether JSON was drafted, parsed, structurally reviewed, imported into a specific n8n version, or executed with observed results. A successful parse does not prove import compatibility.