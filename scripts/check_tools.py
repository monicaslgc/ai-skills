#!/usr/bin/env python3
"""Check that skills, kits and the bundled MCP servers agree with each other.

Needs no third-party packages: server tools are read with the ast module.

Checks:
  1. Both bundled servers compile.
  2. Every tool a smart-home or SSH skill calls exists in the matching server.
  3. Every Basic Memory tool a memory skill calls is a known Basic Memory tool.
  4. Every skill named in backticks inside a SKILL.md exists in skills/.
  5. A skill does not rely on a skill that lives in a different kit
     (so installing one kit is always enough).
"""
import ast
import py_compile
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

SERVERS = {
    "home-assistant": ROOT / "tools" / "home-assistant-mcp" / "ha_server.py",
    "ssh": ROOT / "tools" / "ssh-remote-pc-mcp" / "ssh_server.py",
}
# Tool names of the open-source Basic Memory server that the memory skills may call.
BASIC_MEMORY = {"search_notes", "read_note", "list_directory", "recent_activity", "build_context",
                "list_memory_projects", "edit_note", "write_note"}
# Names that look like tools but are not (service names, attributes, fields).
HA_TOOL_LIKE = {"call_service", "get_state", "get_all_states", "get_history", "get_services", "list_automations",
                "trigger_automation", "enable_automation", "disable_automation", "send_notification",
                "list_services", "create_automation", "update_automation", "delete_automation"}
SSH_TOOL_LIKE = {"run_command", "system_status", "list_processes", "list_services", "manage_service"}
MEMORY_TOOL_LIKE = BASIC_MEMORY | {"memory_search", "memory_get_facts", "memory_get_conversation", "memory_get_conversations", "memory_stats"}


def server_tools(path: Path) -> set:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for dec in node.decorator_list:
                target = dec.func if isinstance(dec, ast.Call) else dec
                if isinstance(target, ast.Attribute) and target.attr == "tool":
                    names.add(node.name)
    return names


for label, path in SERVERS.items():
    try:
        py_compile.compile(str(path), doraise=True)
    except py_compile.PyCompileError as exc:
        errors.append(f"{label} server does not compile: {exc}")

ha_tools = server_tools(SERVERS["home-assistant"])
ssh_tools = server_tools(SERVERS["ssh"])

skills = {p.parent.name: p.read_text(encoding="utf-8") for p in sorted((ROOT / "skills").glob("*/SKILL.md"))}
kit_of = {}
for kit in sorted((ROOT / "kits").glob("*/README.md")):
    for ref in set(re.findall(r"\]\(\.\./\.\./skills/([a-z0-9-]+)\)", kit.read_text(encoding="utf-8"))):
        kit_of[ref] = kit.parent.name


def called(text: str) -> set:
    return set(re.findall(r"`([a-z]+(?:_[a-z]+)+)(?:\(|`)", text))


for name, text in skills.items():
    kit = kit_of.get(name)
    used = called(text)
    if kit == "smart-home":
        for tool in sorted((used & HA_TOOL_LIKE) - ha_tools):
            errors.append(f"{name}: calls `{tool}` which the Home Assistant server does not provide")
    if kit == "memory":
        for tool in sorted((used & MEMORY_TOOL_LIKE) - BASIC_MEMORY):
            errors.append(f"{name}: calls `{tool}` which is not a known Basic Memory tool")
    if name == "ssh-remote-pc":
        for tool in sorted((used & SSH_TOOL_LIKE) - ssh_tools):
            errors.append(f"{name}: calls `{tool}` which the SSH server does not provide")
    for ref in sorted(set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", text))):
        if ref == name or ref.endswith("-mcp"):
            continue
        if ref in skills and kit_of.get(ref) != kit:
            errors.append(f"{name}: relies on `{ref}` from a different kit ({kit_of.get(ref)}); install would be incomplete")

if errors:
    print("FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"OK: {len(ha_tools)} Home Assistant tools, {len(ssh_tools)} SSH tools, {len(skills)} skills consistent")
