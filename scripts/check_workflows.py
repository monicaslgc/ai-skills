#!/usr/bin/env python3
"""Check the workflow files in workflows/.

Checks:
  1. Every workflow file is listed in workflows/README.md, and every listed file exists.
  2. Every skill named in a step table exists in skills/.
  3. Every skill used in a step table appears in the 'Skills to install' list, and the reverse.
  4. Each workflow has the required sections.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / "workflows"
skills = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
errors = []

readme = (W / "README.md").read_text(encoding="utf-8")
files = sorted(p for p in W.glob("*.md") if p.name != "README.md")
for p in files:
    if f"({p.name})" not in readme:
        errors.append(f"{p.name} is not listed in workflows/README.md")
for name in re.findall(r"\]\(([\w-]+\.md)\)", readme):
    if not (W / name).exists():
        errors.append(f"workflows/README.md lists {name}, which does not exist")

for p in files:
    text = p.read_text(encoding="utf-8")
    for section in ("## Steps", "## Rules for this workflow", "## Skills to install", "## Start prompt"):
        if section not in text:
            errors.append(f"{p.name}: missing section {section}")
    steps = text.split("## Steps", 1)[-1].split("\n## ", 1)[0]
    used = set(re.findall(r"\[`([\w-]+)`\]\(\.\./skills/([\w-]+)\)", steps))
    for shown, target in used:
        if shown != target:
            errors.append(f"{p.name}: link text {shown} does not match target {target}")
        if target not in skills:
            errors.append(f"{p.name}: unknown skill {target}")
    used_names = {t for _, t in used}
    install = text.split("## Skills to install", 1)[-1].split("\n## ", 1)[0]
    listed = set(re.findall(r"`([\w-]+)`", install))
    for s in used_names - listed:
        errors.append(f"{p.name}: {s} is used in a step but not in 'Skills to install'")
    for s in listed - used_names:
        errors.append(f"{p.name}: {s} is in 'Skills to install' but not used in a step")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(files)} workflows consistent with {len(skills)} skills")
