# Sci-Evo-LabTrace

Sci-Evo-LabTrace is a scientific evolution dataset for AI4S agents. The first
release focuses on protein and enzyme design workflows, where papers often
contain clear loops of goal setting, computational design, wet-lab validation,
failure analysis, and iterative optimization.

This repository is prepared for Track 1: "AGI4S Frontier Corpus". The dataset
is designed as a Sci-Evo corpus rather than a static scientific QA set: each
case records a traceable research trajectory from initial scientific objective
to final verification.

## What Is Included

- `data/processed/scievo_gold.jsonl`: curated Sci-Evo cases.
- `schemas/scievo_case.schema.json`: field definitions for each case.
- `scripts/build_dataset.py`: converts curated source records into the
  submission JSONL format.
- `scripts/validate_dataset.py`: validates required fields and trajectory
  consistency.
- `docs/TECHNICAL_REPORT.md`: technical report draft for submission.
- `docs/VIDEO_SCRIPT.md`: short recording script.
- `docs/SUBMISSION_CHECKLIST.md`: final packaging checklist.

## Dataset Unit

Each case describes one scientific research chain:

1. Initial scientific request and measurable target.
2. Multi-step agent trajectory, including dry experiments, wet experiments,
   tool choices, parameters, observations, and iteration logic.
3. Success verification, including metrics and final verdict.
4. Evidence links back to source document pages, figures, tables, or text spans.

## Build

```bash
python3 scripts/build_dataset.py
python3 scripts/validate_dataset.py data/processed/scievo_gold.jsonl
python3 scripts/build_eval_tasks.py
python3 scripts/make_quality_report.py
```

## MinerU Usage

The seed PDF has been parsed with the MinerU API. Normalized artifacts are stored
under `data/interim/mineru/Sci-Evo-Sample/`, with the full image dump under
`data/interim/mineru/extracted/images/`. The processed dataset keeps evidence
fields that can point back to these MinerU artifacts.

## Expansion Pipeline

Use `scripts/collect_openalex_candidates.py` to collect open-access metadata for
future Sci-Evo cases:

```bash
python3 scripts/collect_openalex_candidates.py --limit 25
```

The script writes metadata only; it does not download PDFs. Candidate papers
still require license review before public release or full-text processing.

## License

Dataset records should only be released when the source material and derived
annotations are compliant with the original license and competition rules. The
recommended release license for original annotations is CC-BY-4.0, subject to
source-license compatibility.
