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
        "# 提交就绪报告",
        "",
        "## 总体状态",
        "",
        f"- 是否可提交：{'是' if ready else '否'}",
        f"- Gold case 数量：{gold_cases}",
        f"- Case 总数：{len(cases)}",
        f"- 评测任务数：{len(tasks)}",
        f"- 已筛选 OA 候选数：{len(vetted)}",
        f"- Manifest 版本：{manifest.get('version', 'missing')}",
        "",
        "## 检查项",
        "",
    ]
    for name, value in checks:
        lines.append(f"- {name}: {'通过' if value else '未通过'}")

    lines.extend(
        [
            "",
            "## 阻塞项",
            "",
        ]
    )
    if gold_cases < 3:
        lines.append("- 完整 gold case 少于 3 条；若要冲击高排名，还需要更多带证据链的论文案例。")
    if not bool(vetted):
        lines.append("- 尚未生成开放获取候选论文筛选队列。")
    if not git_is_clean():
        lines.append("- Git 工作区尚未清理。")
    if ready:
        lines.append("- 未发现阻塞项。")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote readiness report to {OUT}")
    return 0 if ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
