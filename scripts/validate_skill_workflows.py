#!/usr/bin/env python3
"""Validate the machine-readable skill relationship and workflow registries."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/skill-ecosystem/relationships.json"
WORKFLOWS = ROOT / "docs/skill-ecosystem/workflows.json"
ERRORS = []
ALLOWED_TYPES = {"requires", "hands-off-to", "complements", "alternative-to", "governed-by"}
PENDING = re.compile(r"^pending-pr-(\d+)$")


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: cannot load valid JSON: {exc}")
        return {}


registry = load(REGISTRY)
workflows = load(WORKFLOWS)
if registry.get("schema_version") != "1.0":
    ERRORS.append("relationships.json: unsupported or missing schema_version")
if workflows.get("schema_version") != "1.0":
    ERRORS.append("workflows.json: unsupported or missing schema_version")

nodes = registry.get("nodes", [])
node_map = {}
for node in nodes:
    skill_id = node.get("id")
    if not skill_id or skill_id in node_map:
        ERRORS.append(f"relationships.json: missing or duplicate node id {skill_id!r}")
        continue
    node_map[skill_id] = node
    availability = node.get("availability")
    if availability == "available":
        if not (ROOT / "skills" / skill_id / "SKILL.md").is_file():
            ERRORS.append(f"{skill_id}: marked available but SKILL.md is missing")
    else:
        match = PENDING.match(availability or "")
        if not match:
            ERRORS.append(f"{skill_id}: invalid availability {availability!r}")
        elif node.get("source_pr") != int(match.group(1)):
            ERRORS.append(f"{skill_id}: source_pr does not match {availability}")

seen_edges = set()
for edge in registry.get("relationships", []):
    source, target, relation = edge.get("from"), edge.get("to"), edge.get("type")
    if source not in node_map:
        ERRORS.append(f"relationship: unknown source {source!r}")
    if target not in node_map:
        ERRORS.append(f"relationship: unknown target {target!r}")
    if relation not in ALLOWED_TYPES:
        ERRORS.append(f"relationship: invalid type {relation!r}")
    key = (source, relation, target)
    if key in seen_edges:
        ERRORS.append(f"relationship: duplicate edge {key}")
    seen_edges.add(key)
    if not edge.get("when"):
        ERRORS.append(f"relationship {key}: missing routing condition")

workflow_ids = set()
for workflow in workflows.get("workflows", []):
    workflow_id = workflow.get("id")
    if not workflow_id or workflow_id in workflow_ids:
        ERRORS.append(f"workflows.json: missing or duplicate workflow id {workflow_id!r}")
    workflow_ids.add(workflow_id)
    stages = workflow.get("stages", [])
    stage_ids = [stage.get("id") for stage in stages]
    if len(stage_ids) != len(set(stage_ids)):
        ERRORS.append(f"{workflow_id}: duplicate stage id")
    for stage in stages:
        skill_id = stage.get("skill")
        node = node_map.get(skill_id)
        if not node:
            ERRORS.append(f"{workflow_id}: unknown skill {skill_id!r}")
            continue
        if stage.get("availability") != node.get("availability"):
            ERRORS.append(f"{workflow_id}/{stage.get('id')}: availability mismatch for {skill_id}")
        if node.get("availability", "").startswith("pending") and stage.get("source_pr") != node.get("source_pr"):
            ERRORS.append(f"{workflow_id}/{stage.get('id')}: missing or incorrect source_pr for {skill_id}")
        if not stage.get("when") or not stage.get("output"):
            ERRORS.append(f"{workflow_id}/{stage.get('id')}: missing trigger or output contract")
        handoff = stage.get("handoff_to")
        if handoff and handoff not in stage_ids:
            ERRORS.append(f"{workflow_id}/{stage.get('id')}: unknown handoff_to stage {handoff!r}")

if not registry.get("relationships"):
    ERRORS.append("relationships.json: no relationships defined")
if not workflows.get("workflows"):
    ERRORS.append("workflows.json: no workflows defined")

if ERRORS:
    print("FAILED")
    print("\n".join(f"- {error}" for error in ERRORS))
    sys.exit(1)

pending = sum(1 for node in nodes if node["availability"] != "available")
print(f"OK: {len(nodes)} nodes, {len(seen_edges)} relationships, {len(workflow_ids)} workflows ({pending} pending-PR references)")
