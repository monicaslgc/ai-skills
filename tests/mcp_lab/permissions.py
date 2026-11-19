"""Small deterministic authorization policy used to test least privilege.

This is an application policy unit under test, not an OAuth implementation and
not a replacement for the MCP host's or server's authenticated identity layer.
"""

READ_TOOLS = {"list_demo_records", "list_demo_records_page", "get_demo_record"}
WRITE_TOOLS = {"update_demo_record"}


def authorize_tool(scopes: set[str], tool_name: str) -> bool:
    """Return whether the supplied authenticated scopes permit a known tool."""
    if tool_name in READ_TOOLS:
        return "records:read" in scopes or "records:write" in scopes
    if tool_name in WRITE_TOOLS:
        return "records:write" in scopes
    return False
