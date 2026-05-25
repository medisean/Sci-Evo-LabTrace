#!/usr/bin/env python3
"""Generate a lightweight quality report for the processed dataset."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "processed" / "scievo_gold.jsonl"
EVAL_TASKS = ROOT / "data" / "processed" / "scievo_eval_tasks.jsonl"
CANDIDATES = ROOT / "data" / "raw" / "candidate_papers.jsonl"
VETTED = ROOT / "data" / "processed" / "vetted_open_access_sources.jsonl"
READINESS = ROOT / "reports" / "SUBMISSION_READINESS.md"
OUT = ROOT / "reports" / "QUALITY_REPORT.md"


def load_cases(path: Path) -> list[dict]:
    cases = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                cases.append(json.loads(line))
    return cases


def main() -> None:
    cases = load_cases(DATASET)
    eval_task_count = len(load_cases(EVAL_TASKS)) if EVAL_TASKS.exists() else 0
    candidate_count = len(load_cases(CANDIDATES)) if CANDIDATES.exists() else 0
    vetted = load_cases(VETTED) if VETTED.exists() else []
    curation = Counter(case["quality"]["curation_level"] for case in cases)
    actions = Counter()
    domains = Counter()
    license_statuses = Counter()
    vetting_statuses = Counter(item.get("vetting_status", "unknown") for item in vetted)
    evidence_count = 0
    step_count = 0
    for case in cases:
        domains.update(case.get("domain", []))
        license_statuses[case.get("source", {}).get("license_status", "missing")] += 1
        for step in case.get("agent_trajectory", []):
            actions[step.get("action", "unknown")] += 1
            step_count += 1
            evidence_count += len(step.get("evidence", []))
    avg_evidence = evidence_count / step_count if step_count else 0
    gold_cases = curation.get("gold", 0)
    local_mineru_cases = sum(1 for case in cases if case.get("source", {}).get("mineru_artifact"))
    risks: list[str] = []
    if any(case.get("quality", {}).get("requires_license_review") for case in cases):
        risks.append("- 公开发布前仍需逐条复核来源许可状态。")
    if gold_cases < 3:
        risks.append("- 当前版本少于 3 条完整 gold case，提交前仍需扩展。")
    if local_mineru_cases < len(cases):
        risks.append("- 仅部分 case 已绑定本地 MinerU 解析产物；最终包可继续补齐开放论文解析结果。")
    if len(vetted) > gold_cases:
        risks.append("- 仍有已筛选开放论文可继续扩展，用于增强最终提交规模。")
    if not risks:
        risks.append("- 未发现主要数据质量阻塞；剩余工作主要是打包和最终提交检查。")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as f:
        f.write("# Sci-Evo-LabTrace 质量报告\n\n")
        f.write("## 概要\n\n")
        f.write(f"- Case 数量：{len(cases)}\n")
        f.write(f"- 轨迹步骤数：{step_count}\n")
        f.write(f"- 评测任务数：{eval_task_count}\n")
        f.write(f"- 扩展候选论文数：{candidate_count}\n")
        f.write(f"- 已筛选开放来源数：{len(vetted)}\n")
        f.write(f"- 每步平均证据数：{avg_evidence:.2f}\n")
        f.write(f"- 提交就绪报告：{'已生成' if READINESS.exists() else '缺失'}\n")
        f.write("\n## 标注等级\n\n")
        for name, count in sorted(curation.items()):
            f.write(f"- {name}: {count}\n")
        f.write("\n## 动作类型分布\n\n")
        for name, count in sorted(actions.items()):
            f.write(f"- {name}: {count}\n")
        f.write("\n## 领域标签\n\n")
        for name, count in sorted(domains.items()):
            f.write(f"- {name}: {count}\n")
        f.write("\n## 来源许可状态\n\n")
        for name, count in sorted(license_statuses.items()):
            f.write(f"- {name}: {count}\n")
        f.write("\n## 开放来源筛选队列\n\n")
        for name, count in sorted(vetting_statuses.items()):
            f.write(f"- {name}: {count}\n")
        f.write("\n## 当前风险\n\n")
        for risk in risks:
            f.write(f"{risk}\n")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
