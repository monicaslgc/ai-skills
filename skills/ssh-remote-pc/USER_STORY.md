# User story: ssh-remote-pc

## Story

**As** a person with a personal Windows PC at home,
**I want** to check on it and run safe commands from a chat,
**so that** I can see whether it is healthy or restart a service without sitting at it.

## Scenario

I am away and want to know whether the PC is still on, what is using its memory, and to restart one service.

## Acceptance criteria

- [ ] The assistant uses the dedicated SSH tools, not ad-hoc connections.
- [ ] Read-only checks run without extra confirmation.
- [ ] Anything destructive or hard to undo is confirmed in chat first.
- [ ] A blocked command is explained, not worked around.
- [ ] Output is summarised in plain language.

## Try it

> How much memory is my PC using, and which processes are the biggest?

See [SKILL.md](SKILL.md) for the full instructions.
