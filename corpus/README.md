# Corpus Directory Contract

The canonical machine-readable corpus is deliberately simple:

```text
corpus/
  kjv.jsonl
  MANIFEST.json
  annotations/
    mechanical.jsonl
```

The exact source snapshot is pinned separately under [`../source/`](../source/).

## Materialization status

`kjv.jsonl` is materialized from the pinned source and contains exactly **31,102** verse records from `GEN.1.1` through `REV.22.21`.

`MANIFEST.json` records the deterministic artifact SHA-256 and the pinned upstream repository, commit, tree, and source-corpus SHA-512.

The current `kjv.jsonl` SHA-256 is:

```text
b4a44c22899b0669f1d504c65a89bee2ac2dd4b08e01c2f012814f348a6ba2dc
```

## `kjv.jsonl`

One verse per line.

Each record contains:

```text
id
book
chapter
verse
text_kjv
text_normalized
source.repository
source.commit
source.tree
source.file
source.json_pointer
source.source_file_sha512
source.text_kjv_sha256
```

`text_kjv` is the exact verse string deterministically extracted from the pinned source JSON value.

`text_normalized` is a deterministic, loss-minimizing derivative. It does not modernize spelling, pronouns, morphology, punctuation, capitalization, or word order.

The source object is mandatory because:

```math
\boxed{\text{verse ID} \neq \text{evidence}}
```

The ID is an address. The pinned source locator plus hashes bind the record to evidence.

## Deterministic regeneration

Materialize the pinned upstream snapshot, then run:

```bash
python scripts/ingest_kjv.py path/to/pinned/kjv-bible corpus/kjv.jsonl
```

The ingester refuses to emit records unless the 66 exact source book files reproduce the pinned whole-corpus SHA-512 fingerprint.

The tracked workflow [`.github/workflows/materialize-corpus.yml`](../.github/workflows/materialize-corpus.yml) performs the same operation on GitHub, verifies 31,102 unique verse records and every embedded verse-text hash, writes `MANIFEST.json`, and commits only if the deterministic outputs changed.

## `annotations/mechanical.jsonl`

Mechanical annotations are sidecars keyed by canonical verse `id` and exact character offsets into that verse record's `text_normalized`.

They do **not** copy the matched text. The evidence span is recovered from the referenced canonical verse record.

## Boundary

```math
\boxed{
\text{pinned source bytes}
\neq
\text{verse extraction}
\neq
\text{normalized text}
\neq
\text{mechanical annotation}
\neq
\text{structural parse}
\neq
\text{interpretation}
}
```

See [`../docs/AI_PARSABLE_CORPUS.md`](../docs/AI_PARSABLE_CORPUS.md) for the corpus specification.
