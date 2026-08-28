# Corpus Directory Contract

The canonical machine-readable corpus is deliberately simple:

```text
corpus/
  kjv.jsonl
  annotations/
    mechanical.jsonl
```

The exact source snapshot is pinned separately under [`../source/`](../source/).

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

## Deterministic generation

Materialize the pinned upstream snapshot, then run:

```bash
python scripts/ingest_kjv.py path/to/pinned/kjv-bible corpus/kjv.jsonl
```

The ingester refuses to emit records unless the 66 exact source book files reproduce the pinned whole-corpus SHA-512 fingerprint.

## `annotations/mechanical.jsonl`

Mechanical annotations remain sidecars keyed by verse `id` and stable offsets into `text_normalized`.

Annotations never overwrite source or normalized text.

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
