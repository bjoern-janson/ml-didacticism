#!/usr/bin/env python3
"""Repair and verify the canonical Genesis 5 substrate custody metadata.

This is a custody-only operation. It re-extracts Genesis 5 from the committed
canonical corpus, verifies every embedded text hash against the verse text,
rewrites the canonical slice deterministically, and updates the dependent P5
manifest's Git-blob binding. The held-out raw parse is never modified.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

CORPUS = Path("corpus/kjv.jsonl")
OUT_RECORDS = Path("verification/genesis/05_CANONICAL_RECORDS.jsonl")
OUT_MANIFEST = Path("verification/genesis/05_CANONICAL_MANIFEST.json")
P5_MANIFEST = Path("heldout/genesis/05_P5_MANIFEST.json")
EXPECTED_IDS = [f"GEN.5.{verse}" for verse in range(1, 33)]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()




def canonical_file_bytes(path: Path) -> bytes:
    """Read repository text in the LF form used by committed Git blobs."""
    return path.read_bytes().replace(b"\r\n", b"\n")


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def canonical_json_bytes(obj: object) -> bytes:
    return (json.dumps(obj, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> int:
    selected: list[dict] = []
    with CORPUS.open("r", encoding="utf-8") as source:
        for line in source:
            if not line.strip():
                continue
            record = json.loads(line)
            if record.get("book") == "Genesis" and record.get("chapter") == 5:
                selected.append(record)

    ids = [record.get("id") for record in selected]
    if ids != EXPECTED_IDS:
        raise SystemExit(f"Genesis 5 IDs mismatch: {ids!r}")

    for verse, record in enumerate(selected, start=1):
        if record.get("chapter") != 5 or record.get("verse") != verse:
            raise SystemExit(f"coordinate mismatch at expected verse {verse}")
        text = record.get("text_kjv")
        if not isinstance(text, str) or not text:
            raise SystemExit(f"missing text_kjv at GEN.5.{verse}")
        source_obj = record.get("source")
        if not isinstance(source_obj, dict):
            raise SystemExit(f"missing source object at GEN.5.{verse}")
        actual = hashlib.sha256(text.encode("utf-8")).hexdigest()
        expected = source_obj.get("text_kjv_sha256")
        if actual != expected:
            raise SystemExit(
                f"corpus verse hash mismatch at GEN.5.{verse}: "
                f"expected {expected}, actual {actual}"
            )

    payload = "".join(
        json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
        for record in selected
    ).encode("utf-8")
    artifact_sha256 = sha256_bytes(payload)
    corpus_sha256 = sha256_bytes(canonical_file_bytes(CORPUS))

    manifest = {
        "schema_version": 1,
        "purpose": "canonical Genesis 5 substrate slice; no structural interpretation",
        "source_corpus": "corpus/kjv.jsonl",
        "source_corpus_sha256": corpus_sha256,
        "first_id": EXPECTED_IDS[0],
        "last_id": EXPECTED_IDS[-1],
        "verse_count": len(selected),
        "artifact": OUT_RECORDS.as_posix(),
        "artifact_sha256": artifact_sha256,
        "all_text_kjv_sha256_verified": True,
    }
    manifest_bytes = canonical_json_bytes(manifest)

    # Historical invariant discovered by the second-pass audit: the frozen
    # manifest already names the deterministic corpus-derived artifact hash.
    existing_manifest = json.loads(OUT_MANIFEST.read_text(encoding="utf-8"))
    existing_target = existing_manifest.get("artifact_sha256")
    if existing_target != artifact_sha256:
        raise SystemExit(
            "Genesis 5 frozen manifest target differs from deterministic corpus "
            f"derivation: manifest={existing_target}, derived={artifact_sha256}"
        )

    old_records = canonical_file_bytes(OUT_RECORDS)
    old_blob_sha = git_blob_sha1(old_records)

    OUT_RECORDS.write_bytes(payload)
    OUT_MANIFEST.write_bytes(manifest_bytes)

    p5 = json.loads(P5_MANIFEST.read_text(encoding="utf-8"))
    substrate = p5["substrate"]
    repair = p5.setdefault("custody_repair", {})
    repair.setdefault("prior_substrate_blob_sha", old_blob_sha)
    repair["kind"] = "EMBEDDED_HASH_METADATA_REPAIR"
    repair["verse_text_changed"] = False
    repair["canonical_artifact_sha256_changed"] = False
    repair["embedded_hashes_rederived_from_corpus"] = True
    repair["raw_parse_modified"] = False

    substrate["sha256"] = artifact_sha256
    substrate["blob_sha"] = git_blob_sha1(payload)
    substrate["canonical_manifest_blob_sha"] = git_blob_sha1(manifest_bytes)

    P5_MANIFEST.write_bytes(canonical_json_bytes(p5))

    print(
        "Genesis 5 custody repaired: "
        f"artifact_sha256={artifact_sha256} "
        f"records_blob={git_blob_sha1(payload)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
