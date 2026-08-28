#!/usr/bin/env python3
"""Extract and verify Genesis 1 from the frozen canonical corpus.

This is a substrate audit only. It performs no structural interpretation.

Input:
    corpus/kjv.jsonl

Outputs:
    verification/genesis/01_CANONICAL_RECORDS.jsonl
    verification/genesis/01_CANONICAL_MANIFEST.json

The script:
- selects exactly GEN.1.1 through GEN.1.31 from the committed corpus;
- verifies record ordering and coordinates;
- recomputes each text_kjv SHA-256 and compares it to source.text_kjv_sha256;
- preserves the complete canonical records without modification;
- hashes the extracted 31-line artifact.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

CORPUS = Path("corpus/kjv.jsonl")
OUT_DIR = Path("verification/genesis")
OUT_RECORDS = OUT_DIR / "01_CANONICAL_RECORDS.jsonl"
OUT_MANIFEST = OUT_DIR / "01_CANONICAL_MANIFEST.json"

EXPECTED_IDS = [f"GEN.1.{verse}" for verse in range(1, 32)]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    selected: list[dict] = []

    with CORPUS.open("r", encoding="utf-8") as source:
        for line_number, line in enumerate(source, start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            if record.get("book") == "Genesis" and record.get("chapter") == 1:
                selected.append(record)

    ids = [record.get("id") for record in selected]
    if ids != EXPECTED_IDS:
        raise SystemExit(f"Genesis 1 IDs mismatch: {ids!r}")

    for verse, record in enumerate(selected, start=1):
        if record.get("chapter") != 1 or record.get("verse") != verse:
            raise SystemExit(f"coordinate mismatch at expected verse {verse}")
        text = record.get("text_kjv")
        if not isinstance(text, str) or not text:
            raise SystemExit(f"missing text_kjv at GEN.1.{verse}")
        source_obj = record.get("source")
        if not isinstance(source_obj, dict):
            raise SystemExit(f"missing source object at GEN.1.{verse}")
        actual = hashlib.sha256(text.encode("utf-8")).hexdigest()
        expected = source_obj.get("text_kjv_sha256")
        if actual != expected:
            raise SystemExit(
                f"verse hash mismatch at GEN.1.{verse}: expected {expected}, actual {actual}"
            )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = "".join(
        json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
        for record in selected
    ).encode("utf-8")
    OUT_RECORDS.write_bytes(payload)

    corpus_sha256 = sha256_bytes(CORPUS.read_bytes())
    manifest = {
        "schema_version": 1,
        "purpose": "canonical Genesis 1 substrate slice; no structural interpretation",
        "source_corpus": "corpus/kjv.jsonl",
        "source_corpus_sha256": corpus_sha256,
        "first_id": EXPECTED_IDS[0],
        "last_id": EXPECTED_IDS[-1],
        "verse_count": len(selected),
        "artifact": str(OUT_RECORDS),
        "artifact_sha256": sha256_bytes(payload),
        "all_text_kjv_sha256_verified": True,
    }
    OUT_MANIFEST.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
