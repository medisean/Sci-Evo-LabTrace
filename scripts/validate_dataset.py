#!/usr/bin/env python3
"""Validate Sci-Evo-LabTrace JSONL files without third-party dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = [
    "case_id",
    "dataset_version",
    "sci_evo_type",
    "domain",
    "source",
    "initial_request",
    "agent_trajectory",
    "success_verification",
    "quality",
]

REQUIRED_INITIAL = [
    "target_name",
    "input_data",
    "user_intent",
    "quantifiable_goal",
]

REQUIRED_STEP = [
    "step_index",
    "phase",
    "thought",
    "action",
    "tool",
    "parameters",
    "observation",
    "outcome_type",
    "valid",
    "evidence",
]

REQUIRED_VERIFICATION = [
    "validation_technique",
    "metrics",
    "final_verdict",
]


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_case(case: dict, line_no: int) -> list[str]:
    errors: list[str] = []
    prefix = f"line {line_no} case {case.get('case_id', '<missing>')}"

    for field in REQUIRED_TOP_LEVEL:
        require(field in case, f"{prefix}: missing top-level field {field}", errors)
    if errors:
        return errors

    require(
        case["sci_evo_type"] == "scientific_evolution_trace",
        f"{prefix}: unexpected sci_evo_type",
        errors,
    )
    require(isinstance(case["domain"], list) and case["domain"], f"{prefix}: domain must be non-empty list", errors)

    source = case["source"]
    for field in ["title", "document_path", "license_status"]:
        require(field in source and source[field], f"{prefix}: source.{field} is required", errors)

    initial = case["initial_request"]
    for field in REQUIRED_INITIAL:
        require(field in initial and initial[field], f"{prefix}: initial_request.{field} is required", errors)

    steps = case["agent_trajectory"]
    require(isinstance(steps, list) and steps, f"{prefix}: agent_trajectory must be non-empty", errors)
    expected_index = 1
    for step in steps:
        for field in REQUIRED_STEP:
            require(field in step, f"{prefix}: step missing {field}", errors)
        require(step.get("step_index") == expected_index, f"{prefix}: step_index should be {expected_index}", errors)
        expected_index += 1
        require(isinstance(step.get("parameters"), dict), f"{prefix}: step parameters must be object", errors)
        tool = step.get("tool", {})
        require(isinstance(tool, dict) and bool(tool.get("name")), f"{prefix}: step tool.name is required", errors)
        require(isinstance(step.get("evidence"), list) and step.get("evidence"), f"{prefix}: step evidence is required", errors)

    verification = case["success_verification"]
    for field in REQUIRED_VERIFICATION:
        require(field in verification and verification[field], f"{prefix}: success_verification.{field} is required", errors)

    quality = case["quality"]
    coverage = quality.get("evidence_coverage")
    require(isinstance(coverage, (int, float)) and 0 <= coverage <= 1, f"{prefix}: quality.evidence_coverage must be 0..1", errors)
    require(quality.get("curation_level") in {"gold", "silver"}, f"{prefix}: quality.curation_level invalid", errors)

    return errors


def load_jsonl(path: Path) -> tuple[list[dict], list[str]]:
    cases: list[dict] = []
    errors: list[str] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                cases.append(json.loads(line))
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_no}: invalid JSON: {exc}")
    return cases, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_dataset.py <dataset.jsonl>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    cases, errors = load_jsonl(path)
    for idx, case in enumerate(cases, 1):
        errors.extend(validate_case(case, idx))
    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1
    print(f"Validation passed: {len(cases)} case(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
