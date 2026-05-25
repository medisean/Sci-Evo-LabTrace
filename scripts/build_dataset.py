#!/usr/bin/env python3
"""Build the initial Sci-Evo-LabTrace JSONL dataset."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_JSON = ROOT / "Sci-Evo_tool_case.json"
OUT_JSONL = ROOT / "data" / "processed" / "scievo_gold.jsonl"
OUT_PRETTY = ROOT / "data" / "processed" / "scievo_gold.pretty.json"
OUT_MANIFEST = ROOT / "data" / "processed" / "dataset_manifest.json"


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


def build_case(source: dict) -> dict:
    case = {
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
    return case


def main() -> None:
    source = load_source_case()
    case = build_case(source)
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSONL.open("w", encoding="utf-8") as f:
        f.write(json.dumps(case, ensure_ascii=False) + "\n")
    with OUT_PRETTY.open("w", encoding="utf-8") as f:
        json.dump([case], f, ensure_ascii=False, indent=2)
        f.write("\n")
    manifest = {
        "dataset_name": "Sci-Evo-LabTrace",
        "version": "0.1.0",
        "case_count": 1,
        "gold_case_count": 1,
        "silver_case_count": 0,
        "processed_file": str(OUT_JSONL.relative_to(ROOT)),
        "schema_file": "schemas/scievo_case.schema.json",
        "created_from": ["Sci-Evo_tool_case.json", "Sci-Evo-Sample.pdf"],
    }
    with OUT_MANIFEST.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {OUT_JSONL}")


if __name__ == "__main__":
    main()
