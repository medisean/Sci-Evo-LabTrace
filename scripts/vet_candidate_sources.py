#!/usr/bin/env python3
"""Filter OA candidate metadata into a license-aware sourcing queue."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "raw" / "candidate_papers.jsonl"
OUT_JSONL = ROOT / "data" / "processed" / "vetted_open_access_sources.jsonl"
OUT_MD = ROOT / "reports" / "VETTED_SOURCE_QUEUE.md"

ALLOWED_LICENSES = {
    "cc-by",
    "cc-by-4.0",
    "cc-by-sa",
    "cc0",
}

RESTRICTED_LICENSES = {
    "cc-by-nc",
    "cc-by-nc-nd",
    "cc-by-nc-sa",
    "cc-by-nd",
}


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


def classify_license(value: str) -> tuple[str, str]:
    normalized = (value or "").strip().lower()
    if normalized in ALLOWED_LICENSES:
        return "permitted_for_local_processing", "explicit_open_license"
    if normalized in RESTRICTED_LICENSES:
        return "needs_manual_rules_review", "noncommercial_or_noderivs"
    if normalized:
        return "needs_manual_rules_review", "unknown_open_license_string"
    return "blocked_until_license_verified", "missing_license_metadata"


def rank_priority(item: dict, status: str) -> int:
    score = int(item.get("candidate_score") or 0)
    has_pdf = bool(item.get("pdf_url"))
    if status == "permitted_for_local_processing":
        return score + (2 if has_pdf else 0)
    if status == "needs_manual_rules_review":
        return score
    return max(score - 2, 0)


def build_queue(rows: list[dict]) -> list[dict]:
    queue = []
    for item in rows:
        status, reason = classify_license(item.get("license", ""))
        queue.append(
            {
                **item,
                "vetting_status": status,
                "vetting_reason": reason,
                "has_pdf_url": bool(item.get("pdf_url")),
                "next_step": (
                    "download_pdf_then_parse_with_mineru"
                    if status == "permitted_for_local_processing" and item.get("pdf_url")
                    else "review_license_and_competition_rules"
                ),
                "priority_score": rank_priority(item, status),
            }
        )
    queue.sort(
        key=lambda item: (
            item["vetting_status"] != "permitted_for_local_processing",
            -item["priority_score"],
            -(item.get("publication_year") or 0),
            item.get("title", ""),
        )
    )
    return queue


def write_outputs(queue: list[dict]) -> None:
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSONL.open("w", encoding="utf-8") as f:
        for item in queue:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    counts: dict[str, int] = {}
    for item in queue:
        counts[item["vetting_status"]] = counts.get(item["vetting_status"], 0) + 1

    with OUT_MD.open("w", encoding="utf-8") as f:
        f.write("# Vetted Source Queue\n\n")
        f.write("This queue is built from OpenAlex metadata only. It does not imply that the paper has already been downloaded, parsed, or curated into a gold Sci-Evo case.\n\n")
        f.write("## Summary\n\n")
        for status in [
            "permitted_for_local_processing",
            "needs_manual_rules_review",
            "blocked_until_license_verified",
        ]:
            f.write(f"- {status}: {counts.get(status, 0)}\n")
        f.write("\n## Highest-Priority Papers\n\n")
        for item in queue[:10]:
            f.write(
                f"- {item['title']} ({item.get('publication_year', 'n/a')}, {item.get('venue', 'n/a')}): "
                f"{item['vetting_status']}; license={item.get('license') or 'missing'}; "
                f"next={item['next_step']}\n"
            )


def main() -> int:
    queue = build_queue(load_jsonl(INPUT))
    write_outputs(queue)
    print(f"Wrote {len(queue)} vetted source rows to {OUT_JSONL} and {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
