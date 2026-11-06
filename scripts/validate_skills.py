#!/usr/bin/env python3
"""Structural validator for Agent Skills in this repository."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
errors = []
files = sorted(SKILLS.glob("*/SKILL.md")) if SKILLS.exists() else []
if not files:
    errors.append("No skills/*/SKILL.md files found.")

names = set()
for path in files:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing YAML frontmatter.")
        continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{path}: malformed frontmatter.")
        continue
    front = parts[1]
    name = re.search(r"^name:\s*([a-z0-9][a-z0-9-]*)\s*$", front, re.M)
    desc = re.search(r"^description:\s*(.+)$", front, re.M)
    if not name:
        errors.append(f"{path}: missing valid name.")
    else:
        value = name.group(1)
        if value in names:
            errors.append(f"{path}: duplicate skill name {value}.")
        names.add(value)
        if value != path.parent.name:
            errors.append(f"{path}: name '{value}' does not match directory '{path.parent.name}'.")
    if not desc or len(desc.group(1).strip()) < 20:
        errors.append(f"{path}: description missing or too short.")
    body = parts[2].lower()
    if "## workflow" not in body and "# workflow" not in body:
        errors.append(f"{path}: missing Workflow section.")
    if not any(marker in body for marker in ("acceptance criteria", "required outputs", "required deliverables")):
        errors.append(f"{path}: missing acceptance criteria or deliverables section.")

print(f"Validated {len(files)} skill files.")
if errors:
    print("\n".join(f"ERROR: {e}" for e in errors))
    sys.exit(1)
print("PASS: frontmatter, naming, workflow, and deliverable checks.")
