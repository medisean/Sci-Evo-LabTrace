#!/usr/bin/env python3
"""Submit PDFs to MinerU batch API and download parsing artifacts.

The script reads a token from MINERU_API_TOKEN or mineru-api-token.txt.
It never prints the token.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOKEN_FILE = ROOT / "mineru-api-token.txt"
BASE_URL = "https://mineru.net/api/v4"


def load_token() -> str:
    token = os.environ.get("MINERU_API_TOKEN", "").strip()
    if token:
        return token
    if TOKEN_FILE.exists():
        return TOKEN_FILE.read_text(encoding="utf-8").strip()
    raise SystemExit("Missing MinerU token. Set MINERU_API_TOKEN or create mineru-api-token.txt.")


def request_json(method: str, url: str, token: str, payload: dict | None = None) -> dict:
    data = None
    headers = {"Authorization": f"Bearer {token}"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from MinerU API: {body}") from exc


def put_file(upload_url: str, path: Path) -> None:
    result = subprocess.run(
        ["curl", "-sS", "-f", "-X", "PUT", "-T", str(path), upload_url],
        check=False,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"Upload failed for {path.name}: {detail}")


def download(url: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=300) as resp:
        out_path.write_bytes(resp.read())


def create_batch(token: str, pdfs: list[Path], output_dir: Path) -> str:
    payload = {
        "enable_formula": True,
        "enable_table": True,
        "language": "en",
        "model_version": "vlm",
        "files": [
            {
                "name": pdf.name,
                "is_ocr": False,
                "data_id": pdf.stem,
            }
            for pdf in pdfs
        ],
    }
    result = request_json("POST", f"{BASE_URL}/file-urls/batch", token, payload)
    (output_dir / "batch_create_response.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if result.get("code") != 0:
        raise RuntimeError(f"MinerU batch creation failed: {result}")
    data = result["data"]
    for pdf, file_info in zip(pdfs, data["file_urls"]):
        upload_url = file_info["url"] if isinstance(file_info, dict) else file_info
        put_file(upload_url, pdf)
    return data["batch_id"]


def poll_batch(token: str, batch_id: str, output_dir: Path, interval: int, max_wait: int) -> dict:
    deadline = time.time() + max_wait
    url = f"{BASE_URL}/extract-results/batch/{batch_id}"
    last = {}
    while time.time() < deadline:
        last = request_json("GET", url, token)
        (output_dir / "batch_status.json").write_text(
            json.dumps(last, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        if last.get("code") != 0:
            raise RuntimeError(f"MinerU batch status failed: {last}")
        extract_results = last.get("data", {}).get("extract_result", [])
        states = {item.get("state") for item in extract_results}
        print(f"Batch {batch_id} states: {sorted(states)}")
        if extract_results and states <= {"done", "failed"}:
            return last
        time.sleep(interval)
    raise TimeoutError(f"Timed out waiting for MinerU batch {batch_id}: {last}")


def download_results(status: dict, output_dir: Path) -> None:
    results = status.get("data", {}).get("extract_result", [])
    for item in results:
        data_id = item.get("data_id") or item.get("file_name", "unknown")
        if item.get("state") != "done":
            continue
        full_zip_url = item.get("full_zip_url")
        if full_zip_url:
            download(full_zip_url, output_dir / "downloads" / f"{data_id}.zip")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdfs", nargs="+", help="PDF files to parse")
    parser.add_argument("--output-dir", default="data/interim/mineru", help="Output directory")
    parser.add_argument("--interval", type=int, default=20, help="Polling interval in seconds")
    parser.add_argument("--max-wait", type=int, default=1800, help="Maximum wait time in seconds")
    args = parser.parse_args()

    token = load_token()
    pdfs = [Path(p).resolve() for p in args.pdfs]
    for pdf in pdfs:
        if not pdf.exists():
            raise SystemExit(f"Missing PDF: {pdf}")
    output_dir = (ROOT / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    batch_id = create_batch(token, pdfs, output_dir)
    print(f"Created MinerU batch {batch_id}")
    status = poll_batch(token, batch_id, output_dir, args.interval, args.max_wait)
    download_results(status, output_dir)
    print(f"Wrote MinerU artifacts to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
