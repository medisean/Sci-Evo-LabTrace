# Dataset Card: Sci-Evo-LabTrace

## Dataset Type

Sci-Evo scientific evolution data.

## Domain

Protein design, enzyme engineering, synthetic biology, and bioluminescence.

## Intended Use

- Training AI4S agents to understand scientific research trajectories.
- Evaluating next-step scientific decision making.
- Studying tool-use reasoning in computational and wet-lab workflows.
- Building traceable scientific process knowledge bases.

## Data Format

JSON Lines. Each line is one scientific evolution case.

## Annotation Level

Current seed release: gold curated sample.

Planned release: gold curated cases plus silver automatically extracted cases.

## Provenance

The seed case is derived from the competition-provided Sci-Evo sample PDF and JSON. Public release should be gated by source-license review.

## Quality Signals

- Required schema validation.
- Page-level evidence pointers.
- Explicit curation level.
- License review flag.

## Limitations

The current seed release contains one case and is intended as a submission scaffold. A competitive release should expand the number of gold cases and include MinerU parsing artifacts for each source document.
