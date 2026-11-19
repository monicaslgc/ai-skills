#!/usr/bin/env python3
"""Validate cross-skill behavioural scenario fixtures without claiming to run them."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "docs/skill-ecosystem"
ERRORS = []


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: cannot load valid JSON: {exc}")
        return {}


registry = load(BASE / "relationships.json")
workflows = load(BASE / "workflows.json")
fixtures = load(ROOT / "evaluations/skill-ecosystem/workflow-scenarios.json")

known_skills = {node.get("id") for node in registry.get("nodes", [])}
known_workflows = {workflow.get("id") for workflow in workflows.get("workflows", [])}
if fixtures.get("schema_version") != "1.0":
    ERRORS.append("workflow-scenarios.json: unsupported or missing schema_version")
if fixtures.get("status") != "proposed-not-run":
    ERRORS.append("workflow-scenarios.json: status must not imply behavioural tests have run")

seen = set()
for case in fixtures.get("scenarios", []):
    case_id = case.get("id")
    if not case_id or case_id in seen:
        ERRORS.append(f"workflow-scenarios.json: missing or duplicate scenario id {case_id!r}")
    seen.add(case_id)
    if case.get("workflow_id") not in known_workflows:
        ERRORS.append(f"{case_id}: unknown workflow {case.get('workflow_id')!r}")
    if not case.get("prompt"):
        ERRORS.append(f"{case_id}: missing prompt")
    routes = case.get("expected_routes", [])
    if not routes:
        ERRORS.append(f"{case_id}: expected_routes must not be empty")
    for skill_id in routes:
        if skill_id not in known_skills:
            ERRORS.append(f"{case_id}: unknown expected skill {skill_id!r}")
    for field in ("must_preserve", "must_not", "human_gates"):
        if not isinstance(case.get(field), list):
            ERRORS.append(f"{case_id}: {field} must be a list")
    if not case.get("pass_condition"):
        ERRORS.append(f"{case_id}: missing pass_condition")

if len(seen) != 10:
    ERRORS.append(f"expected 10 scenarios, found {len(seen)}")

if ERRORS:
    print("FAILED")
    print("\n".join(f"- {error}" for error in ERRORS))
    sys.exit(1)

print(f"OK: {len(seen)} cross-skill scenarios reference known workflows and skills (not executed)")
