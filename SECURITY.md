# Security

## Reporting a problem

If you find a vulnerability, a leaked secret, or an unsafe behaviour in a skill or in the servers under `tools/`, please open a private report using GitHub's **Security > Report a vulnerability** option on this repository. If that is not available, open an issue that describes the problem **without** including the secret or exploit details.

## What to know before using the tools

- `tools/home-assistant-mcp` uses a long-lived Home Assistant token, and `tools/ssh-remote-pc-mcp` uses an SSH key. Keep both in environment variables or your client's secret store, never in a file in a repository.
- Both servers act with the full permissions of the account or token you give them. Create a dedicated, minimal-permission token or key, and revoke it if it is ever exposed.
- The SSH server blocks a list of high-risk commands, but that list is a safety net, not a security boundary.
- Skills are instructions for an AI agent. Review what an agent proposes before approving it, especially anything that changes devices, services or files.

## If you committed a secret

Revoke or rotate it first. Removing it from the latest commit is not enough, because it stays in the git history.
