# Changelog

All notable changes to this repository are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.3.0] - 2026-10-11

### Added
- Product and requirements kit: functional specs, traceability, UAT, RBAC matrix, process flows, survey analysis, OCR extraction mapping, integration catalogue.
- Support and knowledge kit: knowledge base builder, support evidence pack, onboarding and enablement kit.
- AI and automation kit: confidence-gated triage designer, code change risk summary, data quality audit, personal data flow mapper.
- Career kit: CV tailoring from a master CV, cover letters, achievement stories, confidentiality-safe wording.
- Vendor governance: delivery audit, phase acceptance gate, scope compliance check, supplier invoice review.
- Project management: steering committee pack.

## [0.2.0] - 2026-10-11

### Added
- Project management kit: charter, plan, RAID log, status report, minutes to actions, change request, retrospective.
- Agent management kit: charter, permissions review, approval gates, evaluation planner, release checklist, incident review.
- People operations kit: capacity planning, shift scheduling, leave and attendance process, CV screening rubric, structured interview kit, onboarding plan.
- Support operations kit: SLA and escalation design, KPI dashboard design, ticket quality audit, coaching plan, access request workflow.
- Operations and productivity kit: SOP writer, process automation finder, KPI insight writer.
- Career kit: CV tailoring from a master CV, cover letters, achievement stories, confidentiality-safe wording.
- Memory, Self-hosted AI and homelab, and Content creation kits, so every skill belongs to exactly one kit; README groups now mirror the kits.
- Validator rule: each skill must belong to exactly one kit.
- `scripts/check_tools.py`, run in CI: checks that skills only call tools their server provides and do not rely on skills from another kit.
- Requirements section and Windows install commands in the README.
- Smart home kit: 11 new Home Assistant skills that use only the tools of the included Home Assistant server.
- Content creation skills, user stories for every skill, `CITATION.cff`, an authorship and license section and a disclaimer.
- A validator check that kits reference real skills, and a private-term check for pre-push use.

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
