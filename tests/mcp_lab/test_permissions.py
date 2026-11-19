"""Unit tests for least-privilege tool authorization policy."""

from tests.mcp_lab.permissions import authorize_tool


def test_read_scope_allows_read_only_tools():
    assert authorize_tool({"records:read"}, "get_demo_record") is True
    assert authorize_tool({"records:read"}, "list_demo_records_page") is True


def test_read_scope_does_not_allow_write_tool():
    assert authorize_tool({"records:read"}, "update_demo_record") is False


def test_write_scope_allows_read_and_write_tools():
    scopes = {"records:read", "records:write"}
    assert authorize_tool(scopes, "get_demo_record") is True
    assert authorize_tool(scopes, "update_demo_record") is True


def test_unknown_tool_is_denied_by_default():
    assert authorize_tool({"records:read", "records:write"}, "delete_everything") is False
