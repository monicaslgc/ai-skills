#!/usr/bin/env python3
"""Fail if any tracked file contains a term from a private blocklist.

The blocklist is a plain text file named `.private-terms` in the repository root
(one case-insensitive term per line, `#` for comments). It is listed in
.gitignore, so the terms themselves are never committed. Use it for employer and
client names, project codenames, people, phone numbers or anything else that must
not appear in this public repository.

Usage:  python scripts/check_private_terms.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
terms_file = ROOT / ".private-terms"

if not terms_file.is_file():
    print("No .private-terms file found; skipping private-term check.")
    sys.exit(0)

terms = [
    line.strip().lower()
    for line in terms_file.read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.lstrip().startswith("#")
]

tracked = subprocess.run(
    ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
).stdout.splitlines()

hits = []
for rel in tracked:
    path = ROOT / rel
    try:
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
    except OSError:
        continue
    for term in terms:
        if term in text or term in rel.lower():
            hits.append(f"{rel}: contains a blocked term")
            break

if hits:
    print("BLOCKED: private terms found (term not shown):")
    print("\n".join(f"- {h}" for h in hits))
    sys.exit(1)

print(f"OK: {len(tracked)} tracked files checked against {len(terms)} private terms")
