#!/usr/bin/env python3
"""Build the Sci-Evo-LabTrace JSONL dataset from curated case sources."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_JSON = ROOT / "Sci-Evo_tool_case.json"
CURATED_CASES_DIR = ROOT / "data" / "curated" / "cases"
OUT_JSONL = ROOT / "data" / "processed" / "scievo_gold.jsonl"
OUT_PRETTY = ROOT / "data" / "processed" / "scievo_gold.pretty.json"
OUT_MANIFEST = ROOT / "data" / "processed" / "dataset_manifest.json"
README_FILE = ROOT / "README.md"
TECH_REPORT = ROOT / "docs" / "TECHNICAL_REPORT.md"
CHECKLIST = ROOT / "docs" / "SUBMISSION_CHECKLIST.md"
VIDEO_SCRIPT = ROOT / "docs" / "VIDEO_SCRIPT.md"


STEP_PHASES = {
    1: "scaffold_generation",
    2: "active_site_installation",
    3: "sequence_design_and_filtering",
    4: "experimental_screening",
    5: "substrate_specific_extension",
    6: "activity_optimization",
    7: "cellular_validation",
}


TOOL_CATEGORIES = {
    "trRosetta": "structure_prediction_and_design",
    "RifGen and RifDock": "docking_and_rotamer_field_design",
    "RosettaDesign": "sequence_design",
    "E. coli expression and colony-based screening": "wet_lab_screening",
    "AlphaFold2 and ProteinMPNN": "structure_prediction_and_sequence_design",
    "Site-saturation mutagenesis (SSM)": "wet_lab_optimization",
    "Mammalian cell culture and luminescence imaging": "cell_assay_validation",
}


EVIDENCE_BY_STEP = {
    1: [
        {
            "source_doc": "Sci-Evo-Sample.pdf",
            "page": 2,
            "locator": "Family-wide hallucination section and Fig. 1a",
            "support": "The paper describes Monte Carlo sequence search with trRosetta on naturally occurring NTF2s.",
        },
        {
            "source_doc": "Sci-Evo-Sample.pdf",
            "page": 3,
            "locator": "Family-wide hallucination continuation",
            "support": "The paper reports 1,615 family-wide hallucinated NTF2 scaffolds.",
        },
    ],
    2: [
        {
            "source_doc": "Sci-Evo-Sample.pdf",
            "page": 3,
            "locator": "De novo design of luciferases for DTZ",
            "support": "The paper describes DTZ conformer generation, RifGen RIF enumeration, and RifDock placement.",
        }
    ],
    3: [
        {
            "source_doc": "Sci-Evo-Sample.pdf",
            "page": 3,
            "locator": "RosettaDesign paragraph",
            "support": "The paper reports sequence optimization and selection of 7,648 designs for screening.",
        }
    ],
    4: [
        {
            "source_doc": "Sci-Evo-Sample.pdf",
            "page": 3,
            "locator": "Identification of active luciferases",
            "support": "The paper describes E. coli expression, colony imaging, and 96-well confirmation.",
        }
    ],
    5: [
        {
            "source_doc": "Sci-Evo-Sample.pdf",
            "page": 3,
            "locator": "De novo design of luciferases for h-CTZ",
            "support": "The paper describes using prior design knowledge to create h-CTZ-specific luciferases.",
        }
    ],
    6: [
        {
            "source_doc": "Sci-Evo-Sample.pdf",
            "page": 3,
            "locator": "Site-saturation mutagenesis paragraph",
            "support": "The paper describes SSM over substrate-binding pocket residues.",
        },
        {
            "source_doc": "Sci-Evo-Sample.pdf",
            "page": 4,
            "locator": "Optimization results",
            "support": "The paper reports LuxSit-i with more than 100-fold higher photon flux.",
        },
    ],
    7: [
        {
            "source_doc": "Sci-Evo-Sample.pdf",
            "page": 5,
            "locator": "Mammalian-cell validation paragraph",
            "support": "The paper describes live HEK293T-cell expression and DTZ-specific luminescence.",
        },
        {
            "source_doc": "Sci-Evo-Sample.pdf",
            "page": 6,
            "locator": "Multiplex luciferase assay schematic",
            "support": "The paper describes multiplex reporter assays with HEK293T cells.",
        },
    ],
}


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


def load_source_case() -> dict:
    with SOURCE_JSON.open("r", encoding="utf-8") as f:
        return json.load(f)


def normalize_tool(tool: dict) -> dict:
    name = tool.get("name", "").strip()
    return {
        "name": name,
        "version": tool.get("version", ""),
        "category": TOOL_CATEGORIES.get(name, "unspecified"),
    }


def normalize_step(step: dict) -> dict:
    idx = int(step["step_index"])
    out = {
        "step_index": idx,
        "phase": STEP_PHASES.get(idx, "unspecified"),
        "thought": step["thought"],
        "action": step["action"],
        "tool": normalize_tool(step.get("tool", {})),
        "parameters": step.get("parameters", {}),
        "observation": step["observation"],
        "outcome_type": "success" if step.get("valid") else "partial",
        "valid": bool(step.get("valid", False)),
        "references": step.get("references", []),
        "evidence": EVIDENCE_BY_STEP.get(idx, []),
    }
    return out


def build_seed_case(source: dict) -> dict:
    return {
        "case_id": "SELT-PROT-0001",
        "dataset_version": "0.1.0",
        "sci_evo_type": "scientific_evolution_trace",
        "domain": [
            "protein_design",
            "enzyme_engineering",
            "synthetic_biology",
            "bioluminescence",
        ],
        "source": {
            "title": "De novo design of luciferases using deep learning",
            "authors": [
                "Andy Hsien-Wei Yeh",
                "Christoffer Norn",
                "Yakov Kipnis",
                "Doug Tischer",
                "Samuel J. Pellock",
                "Declan Evans",
                "Pengchen Ma",
                "Gyu Rie Lee",
                "Jason Z. Zhang",
                "Ivan Anishchenko",
                "Brian Coventry",
                "Longxing Cao",
                "Justas Dauparas",
                "Samer Halabiya",
                "Michelle DeWitt",
                "Lauren Carter",
                "K. N. Houk",
                "David Baker",
            ],
            "venue": "Nature",
            "year": 2023,
            "doi": "10.1038/s41586-023-05696-3",
            "url": "",
            "document_path": "Sci-Evo-Sample.pdf",
            "license_status": "sample_from_competition_package_requires_review_before_public_release",
            "mineru_artifact": {
                "markdown_path": "data/interim/mineru/Sci-Evo-Sample/full.md",
                "content_json_path": "data/interim/mineru/Sci-Evo-Sample/content_list.json",
                "images_dir": "data/interim/mineru/extracted/images",
                "tables_dir": "",
            },
        },
        "initial_request": {
            **source["01_initial_request"],
            "evidence": [
                {
                    "source_doc": "Sci-Evo-Sample.pdf",
                    "page": 1,
                    "locator": "Abstract",
                    "support": "The abstract states the goal of designing artificial luciferases for synthetic luciferin substrates.",
                }
            ],
        },
        "agent_trajectory": [
            normalize_step(step) for step in source["02_agent_trajectory"]
        ],
        "success_verification": {
            **source["03_success_verification"],
            "evidence": [
                {
                    "source_doc": "Sci-Evo-Sample.pdf",
                    "page": 5,
                    "locator": "Biochemical characterization paragraph",
                    "support": "The paper reports catalytic efficiency, selectivity, and live-cell validation outcomes.",
                },
                {
                    "source_doc": "Sci-Evo-Sample.pdf",
                    "page": 8,
                    "locator": "Data availability section",
                    "support": "The paper identifies public source data and model/plasmid availability.",
                },
            ],
        },
        "quality": {
            "schema_version": "0.1.0",
            "curation_level": "gold",
            "evidence_coverage": 1.0,
            "requires_license_review": True,
            "notes": "Seed case derived from competition-provided sample files and enriched with page-level evidence pointers.",
        },
    }


def load_curated_cases() -> list[dict]:
    if not CURATED_CASES_DIR.exists():
        return []
    cases = []
    for path in sorted(CURATED_CASES_DIR.glob("*.json")):
        with path.open("r", encoding="utf-8") as f:
            case = json.load(f)
        case.setdefault("quality", {})
        notes = case["quality"].get("notes", "")
        provenance = f"Curated source file: {path.relative_to(ROOT)}"
        case["quality"]["notes"] = f"{notes} {provenance}".strip()
        cases.append(case)
    return cases


def build_cases() -> list[dict]:
    cases = [build_seed_case(load_source_case())]
    cases.extend(load_curated_cases())
    cases.sort(key=lambda item: item["case_id"])
    return cases


def validate_case(case: dict, line_no: int) -> list[str]:
    errors: list[str] = []
    prefix = f"line {line_no} case {case.get('case_id', '<missing>')}"

    for field in REQUIRED_TOP_LEVEL:
        if field not in case:
            errors.append(f"{prefix}: missing top-level field {field}")
    if errors:
        return errors

    if case["sci_evo_type"] != "scientific_evolution_trace":
        errors.append(f"{prefix}: unexpected sci_evo_type")
    if not isinstance(case["domain"], list) or not case["domain"]:
        errors.append(f"{prefix}: domain must be non-empty list")

    source = case["source"]
    for field in ["title", "document_path", "license_status"]:
        if not source.get(field):
            errors.append(f"{prefix}: source.{field} is required")

    initial = case["initial_request"]
    for field in REQUIRED_INITIAL:
        if not initial.get(field):
            errors.append(f"{prefix}: initial_request.{field} is required")

    steps = case["agent_trajectory"]
    if not isinstance(steps, list) or not steps:
        errors.append(f"{prefix}: agent_trajectory must be non-empty")
    else:
        expected_index = 1
        for step in steps:
            for field in REQUIRED_STEP:
                if field not in step:
                    errors.append(f"{prefix}: step missing {field}")
            if step.get("step_index") != expected_index:
                errors.append(f"{prefix}: step_index should be {expected_index}")
            expected_index += 1
            if not isinstance(step.get("parameters"), dict):
                errors.append(f"{prefix}: step parameters must be object")
            tool = step.get("tool", {})
            if not isinstance(tool, dict) or not tool.get("name"):
                errors.append(f"{prefix}: step tool.name is required")
            evidence = step.get("evidence")
            if not isinstance(evidence, list) or not evidence:
                errors.append(f"{prefix}: step evidence is required")

    verification = case["success_verification"]
    for field in REQUIRED_VERIFICATION:
        if not verification.get(field):
            errors.append(f"{prefix}: success_verification.{field} is required")

    quality = case["quality"]
    coverage = quality.get("evidence_coverage")
    if not isinstance(coverage, (int, float)) or not 0 <= coverage <= 1:
        errors.append(f"{prefix}: quality.evidence_coverage must be 0..1")
    if quality.get("curation_level") not in {"gold", "silver"}:
        errors.append(f"{prefix}: quality.curation_level invalid")

    return errors


def dataset_is_valid(cases: list[dict]) -> bool:
    errors: list[str] = []
    for idx, case in enumerate(cases, 1):
        errors.extend(validate_case(case, idx))
    return not errors


def build_manifest(cases: list[dict]) -> dict:
    gold = sum(1 for case in cases if case["quality"]["curation_level"] == "gold")
    silver = sum(1 for case in cases if case["quality"]["curation_level"] == "silver")
    license_review_needed = sum(1 for case in cases if case["quality"].get("requires_license_review"))
    mineru_cases = sum(1 for case in cases if case.get("source", {}).get("mineru_artifact"))
    dataset_validated = dataset_is_valid(cases)
    readiness = {
        "dataset_jsonl_validated": dataset_validated,
        "minimum_complete_gold_cases": gold >= 3,
        "mineru_usage_documented": True,
        "docs_complete": all(path.exists() and path.stat().st_size > 0 for path in [README_FILE, TECH_REPORT, CHECKLIST, VIDEO_SCRIPT]),
        "quality_report_expected": True,
        "source_license_risks_explicit": True,
        "git_clean_required_before_submission": True,
    }
    return {
        "dataset_name": "Sci-Evo-LabTrace",
        "version": "0.1.0",
        "case_count": len(cases),
        "gold_case_count": gold,
        "silver_case_count": silver,
        "license_review_required_count": license_review_needed,
        "cases_with_mineru_artifacts": mineru_cases,
        "processed_file": str(OUT_JSONL.relative_to(ROOT)),
        "eval_tasks_file": "data/processed/scievo_eval_tasks.jsonl",
        "candidate_sources_file": "data/raw/candidate_papers.jsonl",
        "vetted_sources_file": "data/processed/vetted_open_access_sources.jsonl",
        "schema_file": "schemas/scievo_case.schema.json",
        "created_from": ["Sci-Evo_tool_case.json", "data/curated/cases/*.json"],
        "readiness": readiness,
    }


def main() -> None:
    cases = build_cases()
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSONL.open("w", encoding="utf-8") as f:
        for case in cases:
            f.write(json.dumps(case, ensure_ascii=False) + "\n")
    with OUT_PRETTY.open("w", encoding="utf-8") as f:
        json.dump(cases, f, ensure_ascii=False, indent=2)
        f.write("\n")
    manifest = build_manifest(cases)
    with OUT_MANIFEST.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {OUT_JSONL}")


if __name__ == "__main__":
    main()
