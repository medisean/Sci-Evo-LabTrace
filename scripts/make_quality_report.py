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
    curation = Counter(case["quality"]["curation_level"] for case in cases)
    actions = Counter()
    domains = Counter()
    evidence_count = 0
    step_count = 0
    for case in cases:
        domains.update(case.get("domain", []))
        for step in case.get("agent_trajectory", []):
            actions[step.get("action", "unknown")] += 1
            step_count += 1
            evidence_count += len(step.get("evidence", []))
    avg_evidence = evidence_count / step_count if step_count else 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as f:
        f.write("# Sci-Evo-LabTrace Quality Report\n\n")
        f.write("## Summary\n\n")
        f.write(f"- Cases: {len(cases)}\n")
        f.write(f"- Trajectory steps: {step_count}\n")
        f.write(f"- Evaluation tasks: {eval_task_count}\n")
        f.write(f"- Expansion paper candidates: {candidate_count}\n")
        f.write(f"- Average evidence items per step: {avg_evidence:.2f}\n")
        f.write("\n## Curation Levels\n\n")
        for name, count in sorted(curation.items()):
            f.write(f"- {name}: {count}\n")
        f.write("\n## Action Distribution\n\n")
        for name, count in sorted(actions.items()):
            f.write(f"- {name}: {count}\n")
        f.write("\n## Domain Tags\n\n")
        for name, count in sorted(domains.items()):
            f.write(f"- {name}: {count}\n")
        f.write("\n## Current Risks\n\n")
        f.write("- Source license status must be reviewed before public release.\n")
        f.write("- Current seed release should be expanded with more gold cases.\n")
        f.write("- MinerU parsing artifacts should be attached for the formal submission.\n")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
