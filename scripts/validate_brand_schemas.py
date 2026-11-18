#!/usr/bin/env python3
"""Validate the syntax and basic shape of the Brand Strategy & Identity JSON schemas."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "tools" / "brand-strategy-identity" / "schemas"
errors = []
files = sorted(SCHEMA_DIR.glob("*.json"))

if not files:
    errors.append("no brand JSON schemas found")

for path in files:
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        continue
    if not isinstance(schema, dict):
        errors.append(f"{path.relative_to(ROOT)}: schema root must be an object")
        continue
    if not str(schema.get("$schema", "")).startswith("https://json-schema.org/"):
        errors.append(f"{path.relative_to(ROOT)}: missing supported JSON Schema dialect")
    if not schema.get("title"):
        errors.append(f"{path.relative_to(ROOT)}: missing title")
    if schema.get("type") != "object":
        errors.append(f"{path.relative_to(ROOT)}: root type must be object")
    properties = schema.get("properties")
    required = schema.get("required")
    if not isinstance(properties, dict) or not isinstance(required, list):
        errors.append(f"{path.relative_to(ROOT)}: properties and required must be declared")
        continue
    unknown = sorted(set(required) - set(properties))
    if unknown:
        errors.append(f"{path.relative_to(ROOT)}: required fields missing from properties: {', '.join(unknown)}")
    if schema.get("additionalProperties") is not False:
        errors.append(f"{path.relative_to(ROOT)}: additionalProperties must be false")

if errors:
    print("FAILED")
    print("\\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print(f"OK: {len(files)} Brand Strategy & Identity JSON schemas parsed and checked")
