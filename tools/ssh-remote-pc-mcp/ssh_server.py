#!/usr/bin/env python3
"""SSH Remote PC MCP server.

A small, safety-limited set of tools for controlling a personal Windows PC over
SSH: run PowerShell, check system status, list processes and services, and
start/stop/restart services. Used by the `ssh-remote-pc` skill.

Install:  pip install -r requirements.txt
Configure with environment variables:
  SSH_HOST, SSH_USER                (required)
  SSH_PORT (22), SSH_KEY_PATH (~/.ssh/id_ed25519), SSH_KEY_PASSPHRASE (optional)
"""

import os
import re
from typing import Optional

import paramiko
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ssh-remote-pc")

SSH_HOST = os.environ.get("SSH_HOST", "").strip()
SSH_PORT = int(os.environ.get("SSH_PORT", "22") or "22")
SSH_USER = os.environ.get("SSH_USER", "").strip()
SSH_KEY_PATH = os.path.expanduser(os.environ.get("SSH_KEY_PATH", "~/.ssh/id_ed25519"))
SSH_KEY_PASSPHRASE = os.environ.get("SSH_KEY_PASSPHRASE") or None

# Commands matching these patterns are refused outright: drive wipes,
# shutdown/restart, registry and partition destruction. This is a safety net
# against accidents, not a security boundary: the account and key you connect
# with still define what is possible.
BLOCKED_PATTERNS = [
    r"format-volume",
    r"\bformat\s+[a-z]:",
    r"remove-item\b.*-recurse.*-force.*[a-z]:\\?\s*[\"']?\s*$",
    r"\bdel\s+/s\s+/q\s+[a-z]:\\?\s*$",
    r"\brd\s+/s\s+/q\s+[a-z]:\\?\s*$",
    r"stop-computer",
    r"restart-computer",
    r"\bshutdown\b",
    r"\bdiskpart\b",
    r"vssadmin\s+delete\s+shadows",
    r"reg(\.exe)?\s+delete",
    r"cipher\s+/w",
    r"\bbcdedit\b",
    r"remove-partition",
    r"clear-disk",
]


def _is_blocked(command: str) -> Optional[str]:
    lowered = command.lower()
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, lowered):
            return pattern
    return None


def _safe_fragment(value: str) -> str:
    """Keep only characters that are safe inside a quoted PowerShell wildcard."""
    return re.sub(r"[^A-Za-z0-9 ._*-]", "", value)


def _get_client() -> paramiko.SSHClient:
    if not SSH_HOST or not SSH_USER:
        raise RuntimeError(
            "SSH_HOST and SSH_USER are not configured. Set them in the MCP server environment."
        )
    client = paramiko.SSHClient()
    known_hosts = os.path.expanduser("~/.ssh/known_hosts")
    if os.path.exists(known_hosts):
        client.load_host_keys(known_hosts)
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    client.connect(
        hostname=SSH_HOST,
        port=SSH_PORT,
        username=SSH_USER,
        key_filename=SSH_KEY_PATH if os.path.exists(SSH_KEY_PATH) else None,
        passphrase=SSH_KEY_PASSPHRASE,
        timeout=10,
        allow_agent=True,
        look_for_keys=not os.path.exists(SSH_KEY_PATH),
    )
    return client


def _run_powershell(command: str, timeout: int = 30) -> str:
    try:
        client = _get_client()
    except paramiko.SSHException as exc:
        if "not found in known_hosts" in str(exc) or "Server " in str(exc):
            return (
                "Could not verify this PC's SSH host key. SSH into it manually once "
                "from a terminal (for example `ssh user@host`) to accept and store the "
                "host key, then try again."
            )
        raise
    try:
        escaped = command.replace('"', '\\"')
        full_command = f'powershell -NoProfile -NonInteractive -Command "{escaped}"'
        _stdin, stdout, stderr = client.exec_command(full_command, timeout=timeout)
        out = stdout.read().decode("utf-8", errors="replace")
        err = stderr.read().decode("utf-8", errors="replace")
        exit_status = stdout.channel.recv_exit_status()
        result = out
        if err.strip():
            result += f"\n[stderr]\n{err}"
        if exit_status != 0:
            result += f"\n[exit code: {exit_status}]"
        return result.strip() or "(no output)"
    finally:
        client.close()


@mcp.tool()
def run_command(command: str) -> str:
    """Run a PowerShell command on the remote Windows PC over SSH.

    Use for anything not covered by the more specific tools. Commands that could
    wipe a drive, shut down or restart the machine, or delete registry keys are
    blocked; ask the user to run those manually if they are really needed.
    """
    blocked = _is_blocked(command)
    if blocked:
        return (
            f"Blocked: this command matches a restricted, high-risk pattern ({blocked}). "
            "Ask the user to run it manually on their PC instead."
        )
    return _run_powershell(command)


@mcp.tool()
def system_status() -> str:
    """CPU load, memory use, uptime and disk space of the remote PC."""
    script = (
        "$cpu = (Get-CimInstance Win32_Processor | Measure-Object -Property LoadPercentage -Average).Average; "
        "$os = Get-CimInstance Win32_OperatingSystem; "
        "$mem = [math]::Round((($os.TotalVisibleMemorySize - $os.FreePhysicalMemory) / $os.TotalVisibleMemorySize) * 100, 1); "
        "$uptime = (Get-Date) - $os.LastBootUpTime; "
        "Write-Output \\\"CPU load: $cpu%\\\"; "
        "Write-Output \\\"Memory used: $mem%\\\"; "
        "Write-Output \\\"Uptime: $($uptime.Days)d $($uptime.Hours)h $($uptime.Minutes)m\\\"; "
        "Write-Output '--- Disks ---'; "
        "Get-PSDrive -PSProvider FileSystem | Select-Object Name, "
        "@{N='UsedGB';E={[math]::Round($_.Used/1GB,1)}}, "
        "@{N='FreeGB';E={[math]::Round($_.Free/1GB,1)}} | Format-Table -AutoSize | Out-String"
    )
    return _run_powershell(script)


@mcp.tool()
def list_processes(name_filter: str = "") -> str:
    """Top 30 processes by CPU, optionally filtered by a name substring."""
    name_filter = _safe_fragment(name_filter)
    where_clause = (
        f"Where-Object {{ $_.ProcessName -like '*{name_filter}*' }} | " if name_filter else ""
    )
    script = (
        f"Get-Process | {where_clause}Sort-Object CPU -Descending | "
        "Select-Object -First 30 ProcessName, Id, CPU, WorkingSet | Format-Table -AutoSize | Out-String"
    )
    return _run_powershell(script)


@mcp.tool()
def list_services(name_filter: str = "") -> str:
    """Windows services and their Running/Stopped status, optionally filtered by name."""
    name_filter = _safe_fragment(name_filter)
    where_clause = (
        f"Where-Object {{ $_.Name -like '*{name_filter}*' -or $_.DisplayName -like '*{name_filter}*' }} | "
        if name_filter
        else ""
    )
    script = f"Get-Service | {where_clause}Select-Object Name, DisplayName, Status | Format-Table -AutoSize | Out-String"
    return _run_powershell(script)


@mcp.tool()
def manage_service(service_name: str, action: str) -> str:
    """Start, stop or restart a Windows service by name. action: start, stop or restart."""
    action = action.lower().strip()
    if action not in ("start", "stop", "restart"):
        return "action must be one of: start, stop, restart"
    verb = {"start": "Start-Service", "stop": "Stop-Service", "restart": "Restart-Service"}[action]
    safe_name = _safe_fragment(service_name).replace("*", "")
    if not safe_name:
        return "service_name is empty or contains only unsupported characters"
    script = (
        f"{verb} -Name '{safe_name}' -ErrorAction Stop; "
        f"Get-Service -Name '{safe_name}' | Select-Object Name, Status | Format-Table -AutoSize | Out-String"
    )
    return _run_powershell(script)


if __name__ == "__main__":
    mcp.run()
