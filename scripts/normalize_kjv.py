#!/usr/bin/env python3
"""Normalize KJV verse JSONL without changing lexical content.

Input JSONL records must contain:
    id, book, chapter, verse, text_kjv

Output records add:
    text_normalized

The normalizer performs only Unicode/whitespace cleanup. It does not modernize
spelling, pronouns, morphology, punctuation, capitalization, or word order.
"""

from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from pathlib import Path


def normalize_surface(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\u00a0", " ")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return " ".join(text.split())


def normalize_record(record: dict) -> dict:
    required = ("id", "book", "chapter", "verse", "text_kjv")
    missing = [key for key in required if key not in record]
    if missing:
        raise ValueError(f"missing required fields: {', '.join(missing)}")

    output = {
        "id": record["id"],
        "book": record["book"],
        "chapter": record["chapter"],
        "verse": record["verse"],
        "text_kjv": record["text_kjv"],
        "text_normalized": normalize_surface(record["text_kjv"]),
    }
    return output


def normalize_jsonl(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)

    with source.open("r", encoding="utf-8") as src, destination.open(
        "w", encoding="utf-8", newline="\n"
    ) as dst:
        for line_number, line in enumerate(src, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
                normalized = normalize_record(record)
            except (json.JSONDecodeError, ValueError, TypeError) as exc:
                raise ValueError(f"line {line_number}: {exc}") from exc

            dst.write(json.dumps(normalized, ensure_ascii=False, separators=(",", ":")))
            dst.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="raw verse JSONL")
    parser.add_argument("destination", type=Path, help="normalized verse JSONL")
    args = parser.parse_args()

    try:
        normalize_jsonl(args.source, args.destination)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
