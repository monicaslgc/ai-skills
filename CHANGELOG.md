# Changelog

All notable changes to this repository are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.1.0] - 2026-10-11

First public release.

### Added
- 26 skills in five groups: smart home, memory, self-hosted AI and homelab, careers and planning, and content creation.
- A `USER_STORY.md` for every skill (story, scenario, acceptance criteria, example prompt).
- `tools/home-assistant-mcp` and `tools/ssh-remote-pc-mcp`, the MCP servers used by the smart-home and SSH skills. Credentials are read from environment variables only.
- `scripts/validate.py` and a GitHub Actions workflow: checks frontmatter, folder and name match, user story and README listing, and scans for tokens, private IP addresses and emails.
- Contribution files: `CONTRIBUTING.md`, `SECURITY.md`, issue templates (request a skill, report a bad output) and a pull request template.

### Notes
- Status: prototypes. Structure is validated; no formal model evaluations have been run.
- The memory skills use the open-source Basic Memory server.
