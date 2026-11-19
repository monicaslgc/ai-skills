#!/usr/bin/env python3
"""Validate behavioural fixture coverage for every brand skill.

This checks fixture structure and coverage only. It does not execute an LLM or
claim that a skill has passed behavioural evaluation.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "evaluations" / "brand-strategy-identity" / "skill-fixtures.json"
SKILLS_DIR = ROOT / "skills"
REQUIRED_CATEGORIES = {"normal", "incomplete", "conflict_or_unsafe"}
errors = []

try:
    payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    print(f"FAILED: cannot read fixture file: {exc}")
    sys.exit(1)

fixtures = payload.get("fixtures")
declared = payload.get("skills")
if not isinstance(fixtures, list) or not isinstance(declared, list):
    errors.append("fixtures and skills must be arrays")
    fixtures = fixtures if isinstance(fixtures, list) else []
    declared = declared if isinstance(declared, list) else []

actual = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}
if not set(declared).issubset(actual):
    errors.append(
        "fixture pack references skills that do not exist; "
        f"unknown={sorted(set(declared) - actual)}"
    )
if len(declared) != len(set(declared)):
    errors.append("declared skills contains duplicates")

seen_ids = set()
coverage = {name: set() for name in declared}
for index, fixture in enumerate(fixtures):
    if not isinstance(fixture, dict):
        errors.append(f"fixture #{index + 1}: must be an object")
        continue
    fixture_id = fixture.get("id")
    skill = fixture.get("skill")
    category = fixture.get("category")
    if not fixture_id or fixture_id in seen_ids:
        errors.append(f"fixture #{index + 1}: missing or duplicate id {fixture_id!r}")
    seen_ids.add(fixture_id)
    if skill not in coverage:
        errors.append(f"{fixture_id}: unknown skill {skill!r}")
        continue
    if category not in REQUIRED_CATEGORIES:
        errors.append(f"{fixture_id}: invalid category {category!r}")
    else:
        coverage[skill].add(category)
    if not isinstance(fixture.get("prompt"), str) or len(fixture["prompt"].strip()) < 30:
        errors.append(f"{fixture_id}: prompt missing or too short")
    expected = fixture.get("expected_behaviours")
    if not isinstance(expected, list) or len(expected) < 2 or not all(
        isinstance(item, str) and item.strip() for item in expected
    ):
        errors.append(f"{fixture_id}: expected_behaviours must contain at least two non-empty items")

for skill, categories in coverage.items():
    missing = REQUIRED_CATEGORIES - categories
    if missing:
        errors.append(f"{skill}: missing fixture categories {sorted(missing)}")

if errors:
    print("FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print(
    f"OK: {len(declared)} skills have {len(fixtures)} behavioural fixtures "
    f"({len(REQUIRED_CATEGORIES)} categories each)"
)
print("NOTE: fixture validation is not an LLM behavioural test run.")
