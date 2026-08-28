# Corpus Directory Contract

The corpus is intentionally layered.

```text
corpus/
  raw/
    kjv.jsonl
  normalized/
    kjv.jsonl
  annotations/
    mechanical.jsonl
```

These data files should be added only after the exact KJV source / edition and checksum are pinned.

## `raw/kjv.jsonl`

One verse per line with:

```text
id
book
chapter
verse
text_kjv
```

`text_kjv` must preserve the ingested source wording exactly.

## `normalized/kjv.jsonl`

Generated deterministically from the raw corpus with:

```text
id
book
chapter
verse
text_kjv
text_normalized
```

Normalization must not modernize lexical content.

## `annotations/mechanical.jsonl`

Sidecar span annotations keyed by verse `id`.

Annotations must point back to `text_normalized` by stable character offsets and must not overwrite or paraphrase source text.

## Boundary

```math
\boxed{
\text{raw text}
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
