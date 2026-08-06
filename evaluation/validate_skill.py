#!/usr/bin/env python3
"""Validate the minimal-design package and its golden trigger set."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "minimal-design"
CASES = ROOT / "evaluation" / "trigger-cases.jsonl"

PRINCIPLES = [
    "KISS",
    "YAGNI",
    "DRY",
    "Rule of Three",
    "Occam's Razor",
    "Principle of Least Power",
    "Separation of Concerns",
    "Single Responsibility Principle",
    "Composition over Inheritance",
    "Convention over Configuration",
    "Unix Philosophy",
    "Functional Core, Imperative Shell",
    "Negative Code",
    "Dead Code Elimination",
    "Refactoring Toward Primitives",
    "Dependency Inversion Principle",
    "Data-Driven Design",
    "Make Illegal States Unrepresentable",
    "Parse, Don't Validate",
    "Tell, Don't Ask",
    "Law of Demeter",
    "Boy Scout Rule",
]
REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/workflow.md",
    "references/principles.md",
    "references/bundles.md",
    "references/boundaries.md",
    "assets/global-agents-activation.md",
]
EXPECTED_GROUPS = {
    "design": 12,
    "mechanical": 8,
    "software-adjacent": 8,
    "non-software": 8,
}


def fail(message: str) -> None:
    errors.append(message)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def headings(text: str) -> list[str]:
    return re.findall(r"^## (.+)$", text, flags=re.MULTILINE)


def check_local_links(path: Path, text: str) -> None:
    for target in re.findall(r"\[[^]]*\]\(([^)]+)\)", text):
        clean = target.split("#", 1)[0]
        if not clean or "://" in clean or clean.startswith("mailto:"):
            continue
        linked = (path.parent / clean).resolve()
        if not linked.exists():
            fail(f"broken local link in {path.relative_to(ROOT)}: {target}")


errors: list[str] = []

for relative in REQUIRED_FILES:
    read(SKILL / relative)

skill_text = read(SKILL / "SKILL.md")
if len(skill_text.splitlines()) >= 100:
    fail("SKILL.md must remain below 100 lines")
if "/Users/" in "\n".join(read(SKILL / relative) for relative in REQUIRED_FILES):
    fail("portable skill contains an absolute user path")

frontmatter_match = re.match(r"^---\n(.*?)\n---\n", skill_text, flags=re.DOTALL)
if not frontmatter_match:
    fail("SKILL.md frontmatter is missing")
else:
    keys = re.findall(r"^([a-zA-Z0-9_-]+):", frontmatter_match.group(1), flags=re.MULTILINE)
    if keys != ["name", "description"]:
        fail(f"SKILL.md frontmatter keys must be name, description; found {keys}")

principle_text = read(SKILL / "references" / "principles.md")
principle_headings = [item for item in headings(principle_text) if item != "Contents"]
if principle_headings != PRINCIPLES:
    fail("principle cards must represent the 22 principles exactly once and in canonical order")

bundle_text = read(SKILL / "references" / "bundles.md")
bundle_ids = re.findall(r"^## (B\d{2})\b", bundle_text, flags=re.MULTILINE)
if bundle_ids != [f"B0{number}" for number in range(1, 7)]:
    fail(f"bundle cards must represent B01-B06 exactly once; found {bundle_ids}")

openai_yaml = read(SKILL / "agents" / "openai.yaml")
if not re.search(r"^\s*allow_implicit_invocation:\s*true\s*$", openai_yaml, flags=re.MULTILINE):
    fail("agents/openai.yaml must enable implicit invocation")
if 'display_name: "Minimal Design"' not in openai_yaml:
    fail("agents/openai.yaml must use display name Minimal Design")

activation = read(SKILL / "assets" / "global-agents-activation.md")
if "$minimal-design" not in activation:
    fail("activation asset must explicitly name $minimal-design")

for relative in REQUIRED_FILES:
    path = SKILL / relative
    check_local_links(path, read(path))

cases: list[dict[str, object]] = []
for line_number, raw in enumerate(read(CASES).splitlines(), start=1):
    if not raw.strip():
        continue
    try:
        case = json.loads(raw)
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON on trigger-cases.jsonl line {line_number}: {exc}")
        continue
    cases.append(case)

ids = [str(case.get("id")) for case in cases]
if len(ids) != len(set(ids)):
    fail("trigger case IDs must be unique")
if len(cases) != 36:
    fail(f"golden set must contain 36 cases; found {len(cases)}")

group_counts = Counter(str(case.get("group")) for case in cases)
if dict(group_counts) != EXPECTED_GROUPS:
    fail(f"golden set group counts differ: {dict(group_counts)}")

required_case_keys = {
    "id",
    "group",
    "domain",
    "prompt",
    "expected_activation",
    "expected_classification",
    "expected_gate",
    "expected_references",
    "expected_persistence",
}
for case in cases:
    missing = required_case_keys - case.keys()
    if missing:
        fail(f"{case.get('id', '<unknown>')} lacks fields: {sorted(missing)}")
    group = case.get("group")
    activation = case.get("expected_activation")
    classification = case.get("expected_classification")
    refs = case.get("expected_references")
    if group in {"design", "mechanical"} and activation is not True:
        fail(f"{case.get('id')} must expect activation")
    if group in {"software-adjacent", "non-software"} and activation is not False:
        fail(f"{case.get('id')} must expect no activation")
    if group == "mechanical" and (classification != "mechanical" or refs != []):
        fail(f"{case.get('id')} must fast-exit as mechanical with no references")
    if group in {"software-adjacent", "non-software"} and classification != "none":
        fail(f"{case.get('id')} negative must use classification none")
    if "$minimal-design" in str(case.get("prompt", "")) or "minimal-design" in str(case.get("prompt", "")):
        fail(f"{case.get('id')} leaks the evaluated skill name")

pairs: dict[str, list[bool]] = defaultdict(list)
for case in cases:
    if "gate_pair" in case:
        pairs[str(case["gate_pair"])].append(bool(case.get("expected_gate")))
gate_cases = sum(bool(case.get("expected_gate")) for case in cases)
if gate_cases < 4:
    fail(f"golden set needs at least four Decision Gate cases; found {gate_cases}")
if len(pairs) < 4 or any(sorted(values) != [False, True] for values in pairs.values()):
    fail("each of four product-ambiguity pairs must contain one gate and one engineering control")

if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    raise SystemExit(1)

print(
    "Validated minimal-design: "
    f"{len(skill_text.splitlines())} SKILL.md lines, "
    f"{len(PRINCIPLES)} principles, 6 bundles, {len(cases)} trigger cases."
)
