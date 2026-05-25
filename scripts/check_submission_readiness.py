#!/usr/bin/env python3
"""Evaluate Sci-Evo submission readiness from local artifacts."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "processed" / "scievo_gold.jsonl"
EVAL_TASKS = ROOT / "data" / "processed" / "scievo_eval_tasks.jsonl"
MANIFEST = ROOT / "data" / "processed" / "dataset_manifest.json"
QUALITY = ROOT / "reports" / "QUALITY_REPORT.md"
MINERU = ROOT / "reports" / "MINERU_RUN_REPORT.md"
README = ROOT / "README.md"
TECH_REPORT = ROOT / "docs" / "TECHNICAL_REPORT.md"
CHECKLIST = ROOT / "docs" / "SUBMISSION_CHECKLIST.md"
VIDEO = ROOT / "docs" / "VIDEO_SCRIPT.md"
VETTED = ROOT / "data" / "processed" / "vetted_open_access_sources.jsonl"
OUT = ROOT / "reports" / "SUBMISSION_READINESS.md"


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def git_is_clean() -> bool:
    result = subprocess.run(
        [
            "git",
            "status",
            "--short",
            "--",
            ".",
            ":(exclude)reports/SUBMISSION_READINESS.md",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.returncode == 0 and not result.stdout.strip()


def check_docs() -> bool:
    return all(path.exists() and path.stat().st_size > 0 for path in [README, TECH_REPORT, CHECKLIST, VIDEO])


def main() -> int:
    cases = load_jsonl(DATASET)
    tasks = load_jsonl(EVAL_TASKS)
    vetted = load_jsonl(VETTED)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    gold_cases = sum(1 for case in cases if case.get("quality", {}).get("curation_level") == "gold")
    has_license_flags = all("license_status" in case.get("source", {}) for case in cases)

    checks = [
        ("dataset_jsonl_exists", DATASET.exists()),
        ("dataset_has_cases", bool(cases)),
        ("minimum_complete_gold_cases_met", gold_cases >= 3),
        ("manifest_present", MANIFEST.exists()),
        ("mineru_usage_documented", MINERU.exists()),
        ("quality_report_present", QUALITY.exists()),
        ("evaluation_tasks_generated", bool(tasks)),
        ("docs_complete", check_docs()),
        ("source_license_risks_explicit", has_license_flags and bool(vetted)),
        ("git_clean", git_is_clean()),
    ]
    ready = all(value for _, value in checks)

    lines = [
        "# Submission Readiness",
        "",
        "## Overall",
        "",
        f"- Ready to submit: {'yes' if ready else 'no'}",
        f"- Gold cases: {gold_cases}",
        f"- Total cases: {len(cases)}",
        f"- Evaluation tasks: {len(tasks)}",
        f"- Vetted OA candidates: {len(vetted)}",
        f"- Manifest version: {manifest.get('version', 'missing')}",
        "",
        "## Checks",
        "",
    ]
    for name, value in checks:
        lines.append(f"- {name}: {'pass' if value else 'fail'}")

    lines.extend(
        [
            "",
            "## Blocking Gaps",
            "",
        ]
    )
    if gold_cases < 3:
        lines.append("- Fewer than 3 complete gold cases are present; first-place-quality expansion still needs more evidence-backed papers.")
    if not bool(vetted):
        lines.append("- No vetted open-access candidate queue is available yet.")
    if not git_is_clean():
        lines.append("- Worktree is not clean.")
    if ready:
        lines.append("- No blocking gaps detected.")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote readiness report to {OUT}")
    return 0 if ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
