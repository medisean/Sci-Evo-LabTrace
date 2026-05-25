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
- `scripts/check_submission_readiness.py`: evaluates whether the repo is
  actually ready to submit.
- `scripts/vet_candidate_sources.py`: filters OA metadata into a
  license-aware expansion queue.
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
python3 scripts/vet_candidate_sources.py
python3 scripts/make_quality_report.py
python3 scripts/check_submission_readiness.py
```

The readiness script returns non-zero until the submission gates are met. The
current hard blocker is dataset scale: the seed release has only one complete
gold case, and this repo now treats `>=3` complete gold cases as the minimum
credible submission threshold.

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
Run `scripts/vet_candidate_sources.py` after collection to prioritize only the
papers whose license metadata is explicit enough for local MinerU parsing.

## Current Status

- Dataset build/validation pipeline is in place and currently produces 3 gold
  cases and 37 evaluation tasks.
- MinerU usage is documented with local run artifacts for the seed paper, and
  two additional gold cases are curated from explicit CC-BY open-access PDFs.
- Submission docs, checklist, quality report, and readiness report are present.
- The main remaining submission gate is repository hygiene: the final handoff
  should be committed and packaged from a clean git status.

## License

Dataset records should only be released when the source material and derived
annotations are compliant with the original license and competition rules. The
recommended release license for original annotations is CC-BY-4.0, subject to
source-license compatibility.
