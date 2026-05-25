#!/usr/bin/env python3
"""Collect open-access paper candidates for future Sci-Evo expansion.

This script only stores bibliographic metadata and OA links. It does not
download full text or PDFs.
"""

from __future__ import annotations

import argparse
import csv
import json
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_CSV = ROOT / "data" / "raw" / "candidate_papers.csv"
OUT_JSONL = ROOT / "data" / "raw" / "candidate_papers.jsonl"


DEFAULT_QUERIES = [
    "de novo protein design enzyme engineering",
    "directed evolution enzyme design",
    "protein language model functional protein sequences",
    "artificial intelligence protein engineering antibodies",
]

DOMAIN_TERMS = {
    "protein",
    "enzyme",
    "antibody",
    "luciferase",
    "peptide",
    "biocatalyst",
    "sequence",
}

PROCESS_TERMS = {
    "design",
    "engineering",
    "evolution",
    "mutagenesis",
    "optimization",
    "optimize",
    "functional",
    "screening",
}


def candidate_score(title: str) -> int:
    lowered = title.lower()
    domain_hits = sum(1 for term in DOMAIN_TERMS if term in lowered)
    process_hits = sum(1 for term in PROCESS_TERMS if term in lowered)
    if not domain_hits or not process_hits:
        return 0
    return domain_hits + process_hits


def fetch_query(query: str, per_page: int) -> list[dict]:
    params = {
        "search": query,
        "filter": "from_publication_date:2020-01-01,is_oa:true,type:article",
        "per-page": str(per_page),
        "sort": "relevance_score:desc",
    }
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    candidates = []
    for item in payload.get("results", []):
        oa = item.get("open_access") or {}
        primary = item.get("primary_location") or {}
        source = primary.get("source") or {}
        best_oa = item.get("best_oa_location") or {}
        title = item.get("title", "") or ""
        score = candidate_score(title)
        if score <= 0:
            continue
        candidates.append(
            {
                "openalex_id": item.get("id", ""),
                "doi": item.get("doi", ""),
                "title": title,
                "publication_year": item.get("publication_year", ""),
                "venue": source.get("display_name", ""),
                "is_oa": oa.get("is_oa", False),
                "oa_status": oa.get("oa_status", ""),
                "license": best_oa.get("license", "") or primary.get("license", ""),
                "landing_page_url": primary.get("landing_page_url", ""),
                "pdf_url": best_oa.get("pdf_url", ""),
                "candidate_score": score,
                "query": query,
                "relevance_note": "若论文包含明确的设计、实验或优化闭环，可作为 Sci-Evo 抽取候选。",
            }
        )
    return candidates


def fetch_candidates(queries: list[str], limit: int) -> list[dict]:
    seen = set()
    merged = []
    per_query = max(limit, 25)
    for query in queries:
        for item in fetch_query(query, per_query):
            key = item["doi"] or item["openalex_id"]
            if key in seen:
                continue
            seen.add(key)
            merged.append(item)
    merged.sort(key=lambda item: (item.get("candidate_score", 0), item.get("publication_year", 0)), reverse=True)
    return merged[:limit]


def write_outputs(candidates: list[dict]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "openalex_id",
        "doi",
        "title",
        "publication_year",
        "venue",
        "is_oa",
        "oa_status",
        "license",
        "landing_page_url",
        "pdf_url",
        "candidate_score",
        "query",
        "relevance_note",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(candidates)
    with OUT_JSONL.open("w", encoding="utf-8") as f:
        for item in candidates:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--query",
        action="append",
        help="Override default query. Can be provided multiple times.",
    )
    parser.add_argument("--limit", type=int, default=25)
    args = parser.parse_args()
    queries = args.query or DEFAULT_QUERIES
    candidates = fetch_candidates(queries, args.limit)
    write_outputs(candidates)
    print(f"Wrote {len(candidates)} candidates to {OUT_CSV} and {OUT_JSONL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
