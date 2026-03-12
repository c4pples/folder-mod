#!/usr/bin/env python3
"""Lightweight static checks for recurring AOTA HOI4 script regressions."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[3]

CHECKS = [
    (Path("common/decisions"), re.compile(r"^(decision_categories|decisions)\s*=|^category\s*=", re.M), "legacy decision root wrapper"),
    (Path("events"), re.compile(r"\badd_opinion\s*=\s*\{"), "deprecated add_opinion effect"),
    (Path("events"), re.compile(r"\bbecome_subject\s*=\s*\{"), "deprecated become_subject effect"),
    (Path("common/national_focus"), re.compile(r"\badd_autonomy_ratio\s*=\s*[-]?\d"), "legacy scalar add_autonomy_ratio syntax"),
    (Path("common/characters"), re.compile(r"\bportrait_path\s*="), "legacy character portrait_path syntax"),
    (Path("common/ideas"), re.compile(r"\b(improve_relation|coastal_bunker_cost|operative_mission_speed|army_experience_gain|navy_experience_gain|army_recovery_rate|army_attrition_factor)\s*="), "legacy idea modifier token"),
    (Path("common/ideas"), re.compile(r"\bideas\s*=\s*\{\s*country\s*=\s*\{\s*[A-Za-z0-9_]+\s*=\s*\{[^\n]{220,}\}\s*\}\s*\}", re.S), "compressed one-line ideas block"),
]

MAX_LINE_EXCLUDE = {
    Path("common/national_focus/AOTA_AWU.txt"),
    Path("common/national_focus/AOTA_CHI_warlords.txt"),
    Path("common/national_focus/AOTA_GER.txt"),
    Path("common/national_focus/AOTA_SOV.txt"),
    Path("common/national_focus/AOTA_USA.txt"),
}

MAX_LINE_CHECKS = [
    (Path("common/ideas"), 320, "overlong line in ideas script"),
    (Path("common/national_focus"), 520, "overlong line in focus script"),
    (Path("common/decisions"), 420, "overlong line in decisions script"),
    (Path("events"), 420, "overlong line in events script"),
]

issues = []
for folder, pattern, label in CHECKS:
    base = ROOT / folder
    for path in sorted(base.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for m in pattern.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            issues.append(f"{path.relative_to(ROOT)}:{line}: {label}")

for folder, threshold, label in MAX_LINE_CHECKS:
    base = ROOT / folder
    for path in sorted(base.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(ROOT)
        if rel in MAX_LINE_EXCLUDE:
            continue
        for idx, line_text in enumerate(text.splitlines(), start=1):
            if len(line_text) > threshold:
                issues.append(f"{rel}:{idx}: {label} ({len(line_text)}>{threshold})")

for path in sorted((ROOT / "common/ideas").glob("*.txt")):
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        issues.append(f"{path.relative_to(ROOT)}:1: UTF-8 BOM present in ideas file")

if issues:
    print("AOTA static lint found issues:")
    for item in issues:
        print(f" - {item}")
    sys.exit(1)

print("AOTA static lint passed: no tracked regression patterns found.")
