#!/usr/bin/env python3
"""Deterministically ingest the pinned KJV source snapshot into verse JSONL.

The ingester does no NLP and no interpretation.

Order of operations:
    exact source book bytes
        -> verify pinned corpus SHA-512
        -> deterministic chapter/verse extraction
        -> verse text SHA-256
        -> deterministic surface normalization
        -> JSONL

A verse ID is only an address. Each emitted record also carries a source file,
JSON pointer, exact source-file SHA-512, pinned upstream commit/tree, and the
SHA-256 of the extracted KJV verse text.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

from normalize_kjv import normalize_surface


PINNED_REPOSITORY = "renniemaharaj/kjv-bible"
PINNED_COMMIT = "88723a44bb3e3f229a34f9cf11ce1b7acf971eee"
PINNED_TREE = "df15756d8f2922f24c36ec86081d4d3244277619"
EXPECTED_CORPUS_SHA512 = (
    "7c2eff0219d59c683b1d12739a64facb22807770e05daf20cf1a4d22ef1b739"
    "d5ec03268abb8c3201fd69eb1014cc45a37697cb8abaceccd316c2e473db0b264"
)
FINGERPRINT_DOMAIN = b"KJV-JSON-CORPUS\0v1\0"
EXPECTED_VERSE_COUNT = 31_102

# Canonical Protestant 66-book order used by the pinned source snapshot.
BOOKS: tuple[tuple[str, str], ...] = (
    ("Genesis", "GEN"),
    ("Exodus", "EXO"),
    ("Leviticus", "LEV"),
    ("Numbers", "NUM"),
    ("Deuteronomy", "DEU"),
    ("Joshua", "JOS"),
    ("Judges", "JDG"),
    ("Ruth", "RUT"),
    ("1 Samuel", "1SA"),
    ("2 Samuel", "2SA"),
    ("1 Kings", "1KI"),
    ("2 Kings", "2KI"),
    ("1 Chronicles", "1CH"),
    ("2 Chronicles", "2CH"),
    ("Ezra", "EZR"),
    ("Nehemiah", "NEH"),
    ("Esther", "EST"),
    ("Job", "JOB"),
    ("Psalms", "PSA"),
    ("Proverbs", "PRO"),
    ("Ecclesiastes", "ECC"),
    ("Song of Solomon", "SNG"),
    ("Isaiah", "ISA"),
    ("Jeremiah", "JER"),
    ("Lamentations", "LAM"),
    ("Ezekiel", "EZK"),
    ("Daniel", "DAN"),
    ("Hosea", "HOS"),
    ("Joel", "JOL"),
    ("Amos", "AMO"),
    ("Obadiah", "OBA"),
    ("Jonah", "JON"),
    ("Micah", "MIC"),
    ("Nahum", "NAM"),
    ("Habakkuk", "HAB"),
    ("Zephaniah", "ZEP"),
    ("Haggai", "HAG"),
    ("Zechariah", "ZEC"),
    ("Malachi", "MAL"),
    ("Matthew", "MAT"),
    ("Mark", "MRK"),
    ("Luke", "LUK"),
    ("John", "JHN"),
    ("Acts", "ACT"),
    ("Romans", "ROM"),
    ("1 Corinthians", "1CO"),
    ("2 Corinthians", "2CO"),
    ("Galatians", "GAL"),
    ("Ephesians", "EPH"),
    ("Philippians", "PHP"),
    ("Colossians", "COL"),
    ("1 Thessalonians", "1TH"),
    ("2 Thessalonians", "2TH"),
    ("1 Timothy", "1TI"),
    ("2 Timothy", "2TI"),
    ("Titus", "TIT"),
    ("Philemon", "PHM"),
    ("Hebrews", "HEB"),
    ("James", "JAS"),
    ("1 Peter", "1PE"),
    ("2 Peter", "2PE"),
    ("1 John", "1JN"),
    ("2 John", "2JN"),
    ("3 John", "3JN"),
    ("Jude", "JUD"),
    ("Revelation", "REV"),
)


def sha512_bytes(data: bytes) -> str:
    return hashlib.sha512(data).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def source_files(source_dir: Path) -> list[tuple[str, str, Path]]:
    return [
        (book, abbr, source_dir / f"{book}.json")
        for book, abbr in BOOKS
    ]


def corpus_fingerprint(source_dir: Path) -> str:
    digest = hashlib.sha512()
    digest.update(FINGERPRINT_DOMAIN)

    for book, _abbr, path in source_files(source_dir):
        if not path.is_file():
            raise ValueError(f"missing pinned source file: {path.name}")
        raw = path.read_bytes()
        filename = f"{book}.json".encode("utf-8")
        digest.update(len(filename).to_bytes(4, "big"))
        digest.update(filename)
        digest.update(len(raw).to_bytes(8, "big"))
        digest.update(raw)

    return digest.hexdigest()


def verify_source_bytes(source_dir: Path) -> None:
    actual = corpus_fingerprint(source_dir)
    if actual != EXPECTED_CORPUS_SHA512:
        raise ValueError(
            "source corpus fingerprint mismatch:\n"
            f"  expected {EXPECTED_CORPUS_SHA512}\n"
            f"  actual   {actual}"
        )


def optional_verify_git_pin(source_dir: Path) -> None:
    """If source_dir is a Git checkout, require the pinned commit and tree."""
    git_dir = source_dir / ".git"
    if not git_dir.exists():
        return

    def git(*args: str) -> str:
        return subprocess.check_output(
            ["git", "-C", str(source_dir), *args],
            text=True,
            stderr=subprocess.STDOUT,
        ).strip()

    head = git("rev-parse", "HEAD")
    tree = git("rev-parse", "HEAD^{tree}")
    if head != PINNED_COMMIT:
        raise ValueError(f"source Git HEAD is {head}, expected {PINNED_COMMIT}")
    if tree != PINNED_TREE:
        raise ValueError(f"source Git tree is {tree}, expected {PINNED_TREE}")


def load_book(path: Path) -> dict[str, dict[str, str]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot parse {path.name}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path.name}: top level must be an object")
    return data


def numeric_keys(obj: dict, context: str) -> list[str]:
    try:
        numbers = sorted(int(key) for key in obj)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{context}: non-numeric chapter/verse key") from exc
    if numbers != list(range(1, len(numbers) + 1)):
        raise ValueError(f"{context}: keys must be consecutive from 1")
    return [str(number) for number in numbers]


def iter_records(source_dir: Path):
    count = 0
    for book, abbr, path in source_files(source_dir):
        raw_file = path.read_bytes()
        source_file_sha512 = sha512_bytes(raw_file)
        data = load_book(path)

        for chapter_key in numeric_keys(data, path.name):
            chapter_obj = data[chapter_key]
            if not isinstance(chapter_obj, dict):
                raise ValueError(f"{path.name}/{chapter_key}: chapter must be object")

            for verse_key in numeric_keys(
                chapter_obj, f"{path.name}/{chapter_key}"
            ):
                text = chapter_obj[verse_key]
                if not isinstance(text, str) or not text:
                    raise ValueError(
                        f"{path.name}/{chapter_key}/{verse_key}: verse must be non-empty string"
                    )

                chapter = int(chapter_key)
                verse = int(verse_key)
                count += 1
                yield {
                    "id": f"{abbr}.{chapter}.{verse}",
                    "book": book,
                    "chapter": chapter,
                    "verse": verse,
                    "text_kjv": text,
                    "text_normalized": normalize_surface(text),
                    "source": {
                        "repository": PINNED_REPOSITORY,
                        "commit": PINNED_COMMIT,
                        "tree": PINNED_TREE,
                        "file": path.name,
                        "json_pointer": f"/{chapter_key}/{verse_key}",
                        "source_file_sha512": source_file_sha512,
                        "text_kjv_sha256": sha256_text(text),
                    },
                }

    if count != EXPECTED_VERSE_COUNT:
        raise ValueError(
            f"extracted {count} verses, expected {EXPECTED_VERSE_COUNT}"
        )


def ingest(source_dir: Path, destination: Path) -> None:
    verify_source_bytes(source_dir)
    optional_verify_git_pin(source_dir)

    destination.parent.mkdir(parents=True, exist_ok=True)
    temp = destination.with_suffix(destination.suffix + ".tmp")

    try:
        with temp.open("w", encoding="utf-8", newline="\n") as out:
            for record in iter_records(source_dir):
                out.write(
                    json.dumps(record, ensure_ascii=False, separators=(",", ":"))
                )
                out.write("\n")
        temp.replace(destination)
    finally:
        if temp.exists():
            temp.unlink()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "source_dir",
        type=Path,
        help="checkout/copy of the exact pinned renniemaharaj/kjv-bible source snapshot",
    )
    parser.add_argument(
        "destination",
        type=Path,
        nargs="?",
        default=Path("corpus/kjv.jsonl"),
        help="output JSONL (default: corpus/kjv.jsonl)",
    )
    args = parser.parse_args()

    try:
        ingest(args.source_dir, args.destination)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
