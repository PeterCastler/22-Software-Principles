#!/usr/bin/env python3
"""Forward-test implicit minimal-design invocation in disposable Codex sessions."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVALUATION = ROOT / "evaluation"
TMP = EVALUATION / ".tmp"
SKILL = ROOT / ".agents" / "skills" / "minimal-design"
CASES_PATH = EVALUATION / "trigger-cases.jsonl"
CODEX = shutil.which("codex") or "/Applications/ChatGPT.app/Contents/Resources/codex"

FIXTURE_FILES = {
    "README.md": """# Evaluation fixture

This synthetic repository supports isolated maintenance scenarios.

- Unauthorized document access must return the same not-found response as a missing document.
- Payment-provider idempotency keys and existing public behavior must be preserved.
- No compatibility, old-client, data-retention, or feature-deprecation policy is documented.
""",
    "package.json": '{"name":"evaluation-fixture","private":true,"scripts":{"test":"echo fixture-tests"}}\n',
    "Package.swift": "// swift-tools-version: 5.9\n// Supported platform: macOS 13\n",
    "src/client.ts": "export interface User { displayName: string }\n",
    "src/messages.ts": "export const success = 'Succesful';\n",
    "src/cli.ts": "export function parseDate(value: string): Date { return new Date(value); }\n",
    "src/legacy.ts": "export function exportV1(): string { return 'legacy'; }\n",
    "src/order-domain.ts": "export const canOrder = (credit: number) => credit > 0;\n",
    "src/order.tsx": "import { canOrder } from './order-domain';\nexport const OrderButton = ({ credit }: { credit: number }) => <button disabled={!canOrder(credit)}>Order</button>;\n",
    "src/invoice.py": "def charge(invoice, provider, ledger):\n    result = provider.charge(invoice.id, invoice.total)\n    if invoice.id in ledger:\n        return ledger[invoice.id]\n    ledger[invoice.id] = result\n    return result\n",
    "src/attempts.py": "def parse_attempts(value):\n    retrys = int(value)\n    return retrys\n",
    "src/auth.py": "def get_private_document(user, document):\n    loaded = document.load()\n    return loaded if user.project_id == document.project_id else None\n",
    "src/search.py": "def search(cache, key, loader):\n    return cache.get(key) or loader(key)\n",
    "src/retry.rs": "use std::collections::BTreeMap;\n\npub struct RetryScheduler { pending: BTreeMap<u64, Vec<u64>> }\nimpl RetryScheduler {\n    pub fn new() -> Self { Self { pending: BTreeMap::new() } }\n    pub fn schedule(&mut self, deadline_ms: u64, job_id: u64) { self.pending.entry(deadline_ms).or_default().push(job_id); }\n    pub fn cancel(&mut self, job_id: u64) { for jobs in self.pending.values_mut() { jobs.retain(|id| *id != job_id); } }\n    pub fn ready(&mut self, now_ms: u64) -> Vec<u64> {\n        let deadlines: Vec<u64> = self.pending.range(..=now_ms).map(|(deadline, _)| *deadline).collect();\n        deadlines.into_iter().flat_map(|deadline| self.pending.remove(&deadline).unwrap_or_default()).collect()\n    }\n}\n",
    "src/codec.rs": "pub fn encode(v:&str)->String{v.to_string()}\n",
    "src/lib.rs": "pub mod codec;\npub mod retry;\n",
    "App/SettingsView.swift": "import SwiftUI\nstruct SettingsView: View { var body: some View { Divider().foregroundStyle(Color.gray.opacity(0.19)) } }\n",
    "App/SettingsView.axaml.cs": "public partial class SettingsView { string Validate() => \"Unkown setting\"; }\n",
    "migrations/001_users.sql": "CREATE TABLE users (id INTEGER PRIMARY KEY, full_name TEXT NOT NULL);\n",
    "scripts/deploy.sh": "#!/bin/sh\nset -eu\n: \"${DEPLOY_TOKEN:?DEPLOY_TOKEN is required}\"\ndeploy_dev() { printf '%s\\n' dev; }\ndeploy_stage() { printf '%s\\n' stage; }\ndeploy_prod() { printf '%s\\n' prod; }\n",
    "scripts/healthcheck.sh": "#!/bin/sh\nHEALTHCHECK_TIMEOUT_SECONDS=4\n",
    "tests/fixtures/audit.sql": "INSERT INTO audit(created_at) VALUES ('2025-01-01T00:00:00Z');\n",
    "docs/setup.md": "# Setup\n",
    "DEVELOPER.md": "Read [setup](docs/setp.md).\n",
    "Cargo.toml": "[package]\nname = \"evaluation-fixture\"\nversion = \"0.1.0\"\nedition = \"2021\"\n\n[dependencies]\n",
    "operations/export-traffic.log": "last_observed_v1_export=2026-02-01\n",
}


def load_cases() -> list[dict[str, Any]]:
    return [json.loads(line) for line in CASES_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]


def package_hash() -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in SKILL.rglob("*") if item.is_file()):
        digest.update(path.relative_to(SKILL).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def codex_version() -> str:
    result = subprocess.run([CODEX, "--version"], capture_output=True, text=True, check=False)
    return (result.stdout or result.stderr).strip()


def safe_case_dir(mode: str, case_id: str) -> Path:
    target = (TMP / "fixtures" / mode / case_id).resolve()
    if TMP.resolve() not in target.parents:
        raise ValueError(f"unsafe fixture path: {target}")
    return target


def build_fixture(case: dict[str, Any], mode: str) -> Path:
    case_dir = safe_case_dir(mode, str(case["id"]))
    if case_dir.exists():
        shutil.rmtree(case_dir)
    case_dir.mkdir(parents=True)
    for relative, content in FIXTURE_FILES.items():
        path = case_dir / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    destination = case_dir / ".agents" / "skills" / "minimal-design"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SKILL, destination)
    if mode == "asset":
        source = SKILL / "assets" / "global-agents-activation.md"
        (case_dir / "AGENTS.md").write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    subprocess.run(["git", "init", "-q", str(case_dir)], check=True)
    subprocess.run(["git", "-C", str(case_dir), "add", "."], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(case_dir),
            "-c",
            "user.name=Codex Evaluation",
            "-c",
            "user.email=evaluation@example.invalid",
            "commit",
            "-qm",
            "fixture baseline",
        ],
        check=True,
    )
    if case["id"] == "D12":
        (case_dir / "src" / "order.tsx").write_text(
            "export const OrderButton = ({ credit }: { credit: number }) => "
            "<button disabled={!(credit > 0)}>Order</button>;\n",
            encoding="utf-8",
        )
    return case_dir


def artifact_files(case_dir: Path) -> list[str]:
    found = []
    for path in case_dir.rglob("*"):
        if not path.is_file() or ".git" in path.parts or ".agents" in path.parts:
            continue
        lowered = path.name.lower()
        if lowered in {"contract.md", "design-contract.md", "micro-brief.md", "brief.md"}:
            found.append(path.relative_to(case_dir).as_posix())
    return sorted(found)


def field_block_valid(text: str, heading: str, fields: list[str]) -> bool:
    if heading not in text:
        return False
    return all(re.search(rf"(?m)^{re.escape(field)}:\s*(?:\S|$)", text) for field in fields)


def event_evidence(stdout: str) -> tuple[str, str]:
    commands: list[str] = []
    messages: list[str] = []
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = event.get("item", {})
        if item.get("type") == "command_execution":
            commands.append(str(item.get("command", "")))
        elif item.get("type") == "agent_message":
            messages.append(str(item.get("text", "")))
    return "\n".join(commands), "\n".join(messages)


def reference_evidence(commands: str) -> dict[str, bool]:
    return {
        "workflow": "references/workflow.md" in commands,
        "principles": "references/principles.md" in commands,
        "bundles": "references/bundles.md" in commands,
        "boundaries": "references/boundaries.md" in commands,
    }


def expected_references_found(expected: list[str], raw: str, evidence: dict[str, bool]) -> bool:
    for item in expected:
        if item == "workflow" and not evidence["workflow"]:
            return False
        if item == "boundaries" and not evidence["boundaries"]:
            return False
        if re.fullmatch(r"B0[1-6]", item) and not (evidence["bundles"] and item in raw):
            return False
        if item not in {"workflow", "boundaries"} and not re.fullmatch(r"B0[1-6]", item):
            if not (evidence["principles"] and item in raw):
                return False
    return True


def infer_classification(raw: str, messages: str, activation: bool, gate_valid: bool) -> str:
    if gate_valid:
        return "consequential"
    if field_block_valid(
        messages,
        "Decision surface:",
        ["Requirement", "Decision surface", "Conservative option", "Proposed option", "Verification"],
    ):
        return "consequential"
    if "Micro-brief:" in messages or field_block_valid(
        messages, "Outcome:", ["Outcome", "Scope", "Preserve", "Evidence", "Verification"]
    ):
        return "normal"
    return "mechanical" if activation else "none"


def run_case(
    case: dict[str, Any], mode: str, model: str | None, timeout: int, version: str, skill_hash: str
) -> dict[str, Any]:
    case_dir = build_fixture(case, mode)
    evidence_dir = TMP / "evidence" / mode
    evidence_dir.mkdir(parents=True, exist_ok=True)
    case_id = str(case["id"])
    last_path = evidence_dir / f"{case_id}.last.md"
    command = [
        CODEX,
        "exec",
        "--ephemeral",
        "--json",
        "--color",
        "never",
        "--sandbox",
        "workspace-write",
        "--cd",
        str(case_dir),
    ]
    if model:
        command.extend(["--model", model])
    command.extend(["--output-last-message", str(last_path), str(case["prompt"])])
    started = datetime.now(timezone.utc).isoformat()
    try:
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
            env={**os.environ, "NO_COLOR": "1"},
        )
        stdout = process.stdout
        stderr = process.stderr
        return_code: int | None = process.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        return_code = None
        timed_out = True
    last = last_path.read_text(encoding="utf-8") if last_path.exists() else ""
    raw = "\n".join([stdout, stderr, last])
    (evidence_dir / f"{case_id}.jsonl").write_text(stdout, encoding="utf-8")
    (evidence_dir / f"{case_id}.stderr.txt").write_text(stderr, encoding="utf-8")

    commands, messages = event_evidence(stdout)
    activation = bool(re.search(r"minimal-design|Minimal Design|\.agents/skills/minimal-design", commands + "\n" + messages))
    gate_fields = ["Question", "Reason", "Evidence", "Impact", "Recommendation", "Owner", "Work paused before"]
    gate_valid = field_block_valid(raw, "Decision required", gate_fields) and bool(
        re.search(r"(?m)^Owner:\s*\n?User\s*$", raw)
    )
    refs = reference_evidence(commands)
    classification = infer_classification(raw, messages, activation, gate_valid)
    persisted = artifact_files(case_dir)
    expected_refs = list(case["expected_references"])
    references_correct = expected_references_found(expected_refs, raw, refs)
    if not expected_refs and any(refs.values()):
        references_correct = False

    expected_classification = str(case["expected_classification"])
    classification_correct = classification == expected_classification
    result = {
        "id": case_id,
        "group": case["group"],
        "mode": mode,
        "started_at": started,
        "skill_hash": skill_hash,
        "model": model or "host-default",
        "codex_version": version,
        "activation_asset_present": mode == "asset",
        "scoring_method": "raw skill-path/name evidence plus mandated response structures",
        "return_code": return_code,
        "timed_out": timed_out,
        "activation_observed": activation,
        "activation_correct": activation is bool(case["expected_activation"]),
        "classification_observed": classification,
        "classification_correct": classification_correct,
        "gate_observed": gate_valid,
        "gate_correct": gate_valid is bool(case["expected_gate"]),
        "reference_evidence": refs,
        "references_correct": references_correct,
        "unexpected_persistent_artifacts": persisted,
        "persistence_correct": not persisted,
    }
    result["overall_correct"] = all(
        [
            not timed_out,
            return_code == 0,
            result["activation_correct"],
            classification_correct,
            result["gate_correct"],
            references_correct,
            result["persistence_correct"],
        ]
    )
    return result


def select_cases(all_cases: list[dict[str, Any]], ids: list[str], groups: list[str]) -> list[dict[str, Any]]:
    selected = all_cases
    if ids:
        wanted = set(ids)
        selected = [case for case in selected if str(case["id"]) in wanted]
        missing = wanted - {str(case["id"]) for case in selected}
        if missing:
            raise SystemExit(f"unknown case IDs: {', '.join(sorted(missing))}")
    if groups:
        wanted_groups = set(groups)
        selected = [case for case in selected if str(case["group"]) in wanted_groups]
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["metadata", "asset"], default="metadata")
    parser.add_argument("--case", action="append", default=[], help="run one case ID; repeat as needed")
    parser.add_argument("--group", action="append", default=[], help="run one golden-set group")
    parser.add_argument("--jobs", type=int, default=3)
    parser.add_argument("--model")
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    selected = select_cases(load_cases(), args.case, args.group)
    output = args.output or TMP / f"results-{args.mode}.jsonl"
    metadata = {
        "mode": args.mode,
        "cases": [case["id"] for case in selected],
        "model": args.model or "host-default",
        "codex": CODEX,
        "output": str(output),
        "skill_hash": package_hash(),
    }
    if args.dry_run:
        print(json.dumps(metadata, indent=2))
        return 0

    TMP.mkdir(parents=True, exist_ok=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    version = codex_version()
    results: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as executor:
        futures = {
            executor.submit(run_case, case, args.mode, args.model, args.timeout, version, metadata["skill_hash"]): case
            for case in selected
        }
        for future in concurrent.futures.as_completed(futures):
            case = futures[future]
            try:
                result = future.result()
            except Exception as exc:  # preserve failure evidence for the remaining cases
                result = {"id": case["id"], "group": case["group"], "mode": args.mode, "harness_error": repr(exc)}
            results.append(result)
            print(json.dumps(result, sort_keys=True), flush=True)

    ordered = sorted(results, key=lambda item: str(item["id"]))
    output.write_text("".join(json.dumps(item, sort_keys=True) + "\n" for item in ordered), encoding="utf-8")
    failures = sum(not item.get("overall_correct", False) for item in ordered)
    print(f"Wrote {len(ordered)} results to {output}; {failures} cases failed full behavioral scoring.")
    return 1 if any("harness_error" in item for item in ordered) else 0


if __name__ == "__main__":
    sys.exit(main())
