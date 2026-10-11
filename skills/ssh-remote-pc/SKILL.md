---
name: ssh-remote-pc
description: >
  This skill should be used when the user asks Claude to check on, control,
  or run something on "my PC", "my computer", "my desktop", or a specific
  home/personal machine over SSH -- for example "check my PC's CPU usage",
  "is my computer still on", "restart the Plex service on my PC", "run this
  command on my desktop", "what processes are eating memory on my machine",
  or "is my SSH server set up yet". Also use it when the user wants help
  setting up SSH access to a personal Windows PC for the first time.
metadata:
  version: "0.1.0"
---

# SSH Remote PC Control

Control a personal Windows PC over SSH using the `ssh-remote-pc` MCP server's
tools: `run_command`, `system_status`, `list_processes`, `list_services`, and
`manage_service`.

## Before first use: confirm setup is done

If this is the first time the user is using this skill, or a tool call fails
with a connection error, walk them through `references/windows-ssh-setup.md`
step by step rather than guessing at their configuration. Do not attempt to
SSH into their PC using Bash or any tool other than the `ssh-remote-pc` MCP
tools -- those tools are the only ones configured with the right key and
host details.

Required configuration (set as environment variables on the MCP server, not
things Claude collects during a chat): `SSH_HOST`, `SSH_USER`, `SSH_KEY_PATH`,
and optionally `SSH_PORT` and `SSH_KEY_PASSPHRASE`. If the user says a tool
call is failing with "SSH_HOST and SSH_USER are not configured", point them to
`references/windows-ssh-setup.md`.

## Choosing a tool

- Use `system_status` for CPU/memory/uptime/disk questions ("how's my PC
  doing", "is it running out of disk space").
- Use `list_processes` (with an optional `name_filter`) for "what's using my
  CPU/memory" or "is X running".
- Use `list_services` (with an optional `name_filter`) to check whether a
  specific Windows service exists and its state before starting/stopping it.
- Use `manage_service` to start, stop, or restart a named service. Look the
  exact service name up with `list_services` first if the user gave a
  friendly name (e.g. "Plex" vs the actual service name).
- Use `run_command` for anything else -- arbitrary PowerShell. Prefer the
  narrowest command that answers the question; avoid broad wildcards or
  recursive operations on `C:\` unless the user is explicit about the path
  and intent.

## Safety

The server blocks a fixed list of high-risk commands itself (drive formatting,
mass recursive delete of a whole drive, shutdown/restart, registry deletion,
disk partitioning). If a tool call comes back "Blocked: ...", do not try to
rephrase or work around it -- tell the user the action was blocked as a safety
measure and ask them to run it manually on the PC if they still want it done.

Beyond the hard block list, use judgment: confirm with the user in chat before
running anything destructive or hard to reverse (deleting files, killing
processes, changing configuration) even if the server would allow it. Read-only
checks (status, process/service listing) don't need confirmation.

## Interpreting output

Tool output is raw PowerShell console text. Summarize it for the user in plain
language rather than pasting the raw table unless they ask for the raw output.
