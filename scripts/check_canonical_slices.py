#!/usr/bin/env python3
"""Strict integrity checks for tracked canonical substrate slices and bindings."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

CORPUS = Path("corpus/kjv.jsonl")
VERIFY_DIR = Path("verification/genesis")
HELDOUT_DIR = Path("heldout/genesis")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()




def canonical_file_bytes(path: Path) -> bytes:
    """Read repository text in the LF form used by committed Git blobs."""
    return path.read_bytes().replace(b"\r\n", b"\n")


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def load_jsonl(path: Path) -> list[dict]:
    records: list[dict] = []
    for line_number, line in enumerate(
        canonical_file_bytes(path).decode("utf-8").splitlines(), start=1
    ):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{line_number}: invalid JSON: {exc}") from exc
    return records


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    corpus_bytes = canonical_file_bytes(CORPUS)
    corpus_sha = sha256_bytes(corpus_bytes)
    corpus_records = load_jsonl(CORPUS)
    corpus_by_id: dict[str, dict] = {}
    for record in corpus_records:
        rid = record.get("id")
        require(isinstance(rid, str), "corpus record missing string id")
        require(rid not in corpus_by_id, f"duplicate corpus id: {rid}")
        corpus_by_id[rid] = record

    checked_manifests: dict[str, tuple[dict, Path, bytes]] = {}

    for manifest_path in sorted(VERIFY_DIR.glob("*_CANONICAL_MANIFEST.json")):
        manifest = json.loads(canonical_file_bytes(manifest_path).decode("utf-8"))
        artifact_path = Path(manifest["artifact"])
        artifact_bytes = canonical_file_bytes(artifact_path)
        artifact_sha = sha256_bytes(artifact_bytes)
        records = load_jsonl(artifact_path)

        require(
            manifest.get("source_corpus") == CORPUS.as_posix(),
            f"{manifest_path}: unexpected source_corpus",
        )
        require(
            manifest.get("source_corpus_sha256") == corpus_sha,
            f"{manifest_path}: source corpus SHA-256 mismatch",
        )
        require(
            manifest.get("artifact_sha256") == artifact_sha,
            f"{manifest_path}: artifact SHA-256 mismatch: "
            f"manifest={manifest.get('artifact_sha256')} actual={artifact_sha}",
        )
        require(
            manifest.get("verse_count") == len(records),
            f"{manifest_path}: verse_count mismatch",
        )
        require(bool(records), f"{manifest_path}: canonical slice is empty")
        require(
            manifest.get("first_id") == records[0].get("id")
            and manifest.get("last_id") == records[-1].get("id"),
            f"{manifest_path}: first/last id mismatch",
        )
        require(
            manifest.get("all_text_kjv_sha256_verified") is True,
            f"{manifest_path}: all_text_kjv_sha256_verified must be true",
        )

        seen: set[str] = set()
        for record in records:
            rid = record.get("id")
            require(isinstance(rid, str), f"{artifact_path}: record missing string id")
            require(rid not in seen, f"{artifact_path}: duplicate id {rid}")
            seen.add(rid)
            require(rid in corpus_by_id, f"{artifact_path}: {rid} absent from corpus")
            require(
                record == corpus_by_id[rid],
                f"{artifact_path}: {rid} differs from canonical corpus record",
            )
            text = record.get("text_kjv")
            source = record.get("source")
            require(isinstance(text, str), f"{artifact_path}: {rid} missing text_kjv")
            require(isinstance(source, dict), f"{artifact_path}: {rid} missing source")
            actual_text_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
            require(
                source.get("text_kjv_sha256") == actual_text_sha,
                f"{artifact_path}: {rid} embedded text SHA-256 mismatch",
            )

        checked_manifests[manifest_path.as_posix()] = (manifest, artifact_path, artifact_bytes)

    require(checked_manifests, "no canonical Genesis manifests found")

    # Validate held-out manifests that explicitly bind to canonical substrate artifacts.
    for heldout_path in sorted(HELDOUT_DIR.glob("*_MANIFEST.json")):
        heldout = json.loads(canonical_file_bytes(heldout_path).decode("utf-8"))
        substrate = heldout.get("substrate")
        if not isinstance(substrate, dict) or "canonical_manifest" not in substrate:
            continue

        artifact_path = Path(substrate["artifact"])
        artifact_bytes = canonical_file_bytes(artifact_path)
        canonical_manifest_path = Path(substrate["canonical_manifest"])
        canonical_manifest_bytes = canonical_file_bytes(canonical_manifest_path)
        canonical_manifest = json.loads(canonical_manifest_bytes.decode("utf-8"))

        require(
            substrate.get("sha256") == sha256_bytes(artifact_bytes),
            f"{heldout_path}: substrate SHA-256 mismatch",
        )
        require(
            substrate.get("blob_sha") == git_blob_sha1(artifact_bytes),
            f"{heldout_path}: substrate Git blob mismatch",
        )
        require(
            substrate.get("canonical_manifest_blob_sha") == git_blob_sha1(canonical_manifest_bytes),
            f"{heldout_path}: canonical manifest Git blob mismatch",
        )
        for key in ("first_id", "last_id", "verse_count", "source_corpus", "source_corpus_sha256"):
            require(
                substrate.get(key) == canonical_manifest.get(key),
                f"{heldout_path}: substrate field {key} disagrees with canonical manifest",
            )
        require(
            canonical_manifest.get("artifact") == artifact_path.as_posix(),
            f"{heldout_path}: canonical manifest points to a different artifact",
        )

    print(
        f"PASS: {len(checked_manifests)} canonical Genesis slices match corpus, "
        "embedded hashes, manifests, and held-out substrate bindings."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
