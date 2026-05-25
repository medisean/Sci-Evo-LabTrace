#!/usr/bin/env python3
"""Build evaluation tasks from Sci-Evo trajectory cases."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "processed" / "scievo_gold.jsonl"
OUT = ROOT / "data" / "processed" / "scievo_eval_tasks.jsonl"


def load_cases(path: Path) -> list[dict]:
    cases = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                cases.append(json.loads(line))
    return cases


def compact_step(step: dict) -> dict:
    return {
        "step_index": step["step_index"],
        "phase": step["phase"],
        "action": step["action"],
        "tool": step["tool"]["name"],
        "observation": step["observation"],
    }


def build_next_step_tasks(case: dict) -> list[dict]:
    tasks = []
    steps = case["agent_trajectory"]
    for idx, step in enumerate(steps):
        previous_steps = [compact_step(s) for s in steps[:idx]]
        task = {
            "task_id": f"{case['case_id']}-NEXT-{step['step_index']:02d}",
            "case_id": case["case_id"],
            "task_type": "next_step_decision",
            "instruction": "Given the scientific objective and previous trajectory, predict the next research decision, action type, tool, and expected observation.",
            "input": {
                "initial_request": case["initial_request"],
                "previous_steps": previous_steps,
            },
            "answer": {
                "phase": step["phase"],
                "action": step["action"],
                "tool": step["tool"],
                "parameters": step["parameters"],
                "observation": step["observation"],
            },
            "evidence": step["evidence"],
        }
        tasks.append(task)
    return tasks


def build_failure_gap_tasks(case: dict) -> list[dict]:
    tasks = []
    for step in case["agent_trajectory"]:
        thought = step["thought"]
        if "[Gap]" not in thought:
            continue
        task = {
            "task_id": f"{case['case_id']}-GAP-{step['step_index']:02d}",
            "case_id": case["case_id"],
            "task_type": "gap_to_decision_reasoning",
            "instruction": "Extract the unresolved scientific gap and explain why the recorded decision addresses it.",
            "input": {
                "thought": thought,
                "observation": step["observation"],
            },
            "answer": {
                "decision": step["phase"],
                "action": step["action"],
                "tool": step["tool"]["name"],
            },
            "evidence": step["evidence"],
        }
        tasks.append(task)
    return tasks


def build_metric_task(case: dict) -> dict:
    return {
        "task_id": f"{case['case_id']}-METRICS",
        "case_id": case["case_id"],
        "task_type": "success_metric_extraction",
        "instruction": "Extract the final verification methods, success metrics, and final verdict for the scientific trajectory.",
        "input": {
            "initial_request": case["initial_request"],
            "trajectory_observations": [
                {
                    "step_index": step["step_index"],
                    "observation": step["observation"],
                }
                for step in case["agent_trajectory"]
            ],
        },
        "answer": case["success_verification"],
        "evidence": case["success_verification"].get("evidence", []),
    }


def main() -> None:
    cases = load_cases(DATASET)
    tasks = []
    for case in cases:
        tasks.extend(build_next_step_tasks(case))
        tasks.extend(build_failure_gap_tasks(case))
        tasks.append(build_metric_task(case))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as f:
        for task in tasks:
            f.write(json.dumps(task, ensure_ascii=False) + "\n")
    print(f"Wrote {len(tasks)} tasks to {OUT}")


if __name__ == "__main__":
    main()
