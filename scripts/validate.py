#!/usr/bin/env python3
"""Check every skill: frontmatter, folder/name match, user story, README listing, no secrets or private IPs."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SECRETS = [
    (re.compile(r"eyJ[A-Za-z0-9_-]{20,}"), "JWT-like token"),
    (re.compile(r"\b(?:10\.\d{1,3}|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b"), "private IP address"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "email address"),
]
errors = []

dirs = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
if not dirs:
    errors.append("no skills found")

for d in dirs:
    manifest = d / "SKILL.md"
    if not manifest.is_file():
        errors.append(f"{d.name}: missing SKILL.md")
        continue
    text = manifest.read_text(encoding="utf-8")
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z", text, re.S)
    if not m:
        errors.append(f"{d.name}: missing frontmatter")
        continue
    front, body = m.groups()
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", front, re.M)
    if not name or name.group(1) != d.name:
        errors.append(f"{d.name}: frontmatter name missing or not equal to folder name")
    if not re.search(r"^description:", front, re.M):
        errors.append(f"{d.name}: missing description")
    if len(body.strip()) < 200:
        errors.append(f"{d.name}: body too short")
    if body.count("```") % 2:
        errors.append(f"{d.name}: unbalanced code fence")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
for d in dirs:
    if not (d / "USER_STORY.md").is_file():
        errors.append(f"{d.name}: missing USER_STORY.md")
    if f"(skills/{d.name})" not in readme:
        errors.append(f"{d.name}: not listed in README.md")

for f in ROOT.rglob("*"):
    if f.is_file() and ".git" not in f.parts and f.suffix in {".md", ".json", ".yml", ".yaml", ".py"} and f.name != "validate.py":
        content = f.read_text(encoding="utf-8", errors="ignore")
        for rx, label in SECRETS:
            for hit in rx.finditer(content):
                if "x.x" in hit.group(0) or "example" in hit.group(0):
                    continue
                errors.append(f"{f.relative_to(ROOT)}: {label}: {hit.group(0)[:40]}")

if errors:
    print("FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"OK: {len(dirs)} skills validated")
