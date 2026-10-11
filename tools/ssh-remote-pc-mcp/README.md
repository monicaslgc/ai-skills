# SSH Remote PC MCP server

The tool server used by the `ssh-remote-pc` skill. It connects to your own Windows PC over SSH and exposes five tools: `run_command`, `system_status`, `list_processes`, `list_services`, `manage_service`.

## Safety

The server refuses a fixed list of high-risk commands (drive formatting, recursive delete of a whole drive, shutdown or restart, registry key deletion, disk partitioning). This is a safety net, not a sandbox. Anyone with your private key and this server has the same access as the account it logs in as, so use a dedicated key and keep it private.

## Setup

1. Requires Python 3.10 or newer. Install: `pip install -r requirements.txt`
2. Set up OpenSSH on the PC: follow [the setup guide](../../skills/ssh-remote-pc/references/windows-ssh-setup.md). SSH in manually once so the host key is stored in `known_hosts`.
3. Set environment variables where your MCP client runs the server:

| Variable | Required | Description |
|---|---|---|
| `SSH_HOST` | yes | The PC's IP address or hostname |
| `SSH_USER` | yes | The Windows user to log in as |
| `SSH_KEY_PATH` | no | Private key path (default `~/.ssh/id_ed25519`) |
| `SSH_PORT` | no | Port (default `22`) |
| `SSH_KEY_PASSPHRASE` | no | Passphrase for the key, if it has one |

4. Add the server to your MCP client. Example:

```json
{
  "mcpServers": {
    "ssh-remote-pc": {
      "command": "python",
      "args": ["/path/to/ai-skills/tools/ssh-remote-pc-mcp/ssh_server.py"],
      "env": {
        "SSH_HOST": "<pc-address>",
        "SSH_USER": "<windows-user>",
        "SSH_KEY_PATH": "<path-to-private-key>"
      }
    }
  }
}
```

The host key is verified against `~/.ssh/known_hosts`; connections to unknown hosts are rejected on purpose. The PC must be reachable directly (same network or VPN).
