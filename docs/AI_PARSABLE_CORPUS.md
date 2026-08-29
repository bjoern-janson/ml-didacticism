# AI-Parsable KJV Corpus

**Status:** corpus materialized / pre-interpretive

The first machine-facing layer of this project should be deliberately boring.

The order is:

```math
\boxed{
T_{\rm raw}
\rightarrow
T_{\rm normalized}
\rightarrow
A_{\rm mechanical}
\rightarrow
S_{\rm structural}
\rightarrow
I_{\rm interpretive}
}
```

where:

- `T_raw` is the exact verse string deterministically extracted from the pinned source;
- `T_normalized` is a deterministic, loss-minimizing surface normalization;
- `A_mechanical` is recoverable span-level annotation;
- `S_structural` is the later typed structural decoding;
- `I_interpretive` is any stronger interpretive claim.

The governing boundaries are:

```math
\boxed{\text{annotation} \neq \text{interpretation}}
```

and:

```math
\boxed{T_{\rm raw} \neq T_{\rm normalized} \neq T_{\rm annotated}}
```

No downstream layer overwrites the layer below it.

---

## 1. Pinned source

“KJV” is not a sufficient source identifier.

The current byte source is the immutable Git snapshot:

```text
repository: renniemaharaj/kjv-bible
commit:     88723a44bb3e3f229a34f9cf11ce1b7acf971eee
tree:       df15756d8f2922f24c36ec86081d4d3244277619
```

The pinned 66-book corpus fingerprint is SHA-512:

```text
7c2eff0219d59c683b1d12739a64facb22807770e05daf20cf1a4d22ef1b739d5ec03268abb8c3201fd69eb1014cc45a37697cb8abaceccd316c2e473db0b264
```

The source snapshot contains 66 books, 1,189 chapters, and 31,102 verses. Its upstream metadata describes a KJV editorial basis of 1611 / 1769 and records a 2026-07-30 verse-by-verse verification against Bible SuperSearch KJV module 6.2.0.

Those are provenance facts about the selected source. `ml-didacticism` does not treat them as independent bibliographical certification.

The source pin is recorded in [`../source/PINNED_SOURCE.json`](../source/PINNED_SOURCE.json).

---

## 2. Verse ID is not evidence

```math
\boxed{\text{verse ID} \neq \text{evidence}}
```

`GEN.1.1` is an address.

Each canonical verse is also bound to:

- pinned source repository;
- commit;
- tree;
- source book file;
- deterministic JSON pointer;
- exact source-file SHA-512;
- SHA-256 of the extracted `text_kjv` value.

This prevents an unchanged address from silently pointing at changed evidence.

---

## 3. One verse = one record

The canonical interchange format is **JSONL**.

The materialized corpus is [`../corpus/kjv.jsonl`](../corpus/kjv.jsonl). Its deterministic ingestion manifest is [`../corpus/MANIFEST.json`](../corpus/MANIFEST.json).

The current artifact contains 31,102 verse records from `GEN.1.1` through `REV.22.21`.

Example shape:

```json
{
  "id": "GEN.1.3",
  "book": "Genesis",
  "chapter": 1,
  "verse": 3,
  "text_kjv": "And God said, Let there be light: and there was light.",
  "text_normalized": "And God said, Let there be light: and there was light.",
  "source": {
    "repository": "renniemaharaj/kjv-bible",
    "commit": "88723a44bb3e3f229a34f9cf11ce1b7acf971eee",
    "tree": "df15756d8f2922f24c36ec86081d4d3244277619",
    "file": "Genesis.json",
    "json_pointer": "/1/3",
    "source_file_sha512": "<128 hex chars>",
    "text_kjv_sha256": "<64 hex chars>"
  }
}
```

Book, chapter, verse, and source locator are explicit rather than inferred from surrounding prose.

---

## 4. Extraction and normalization are distinct

Source extraction answers:

> Which exact value in the pinned source corresponds to this verse address?

Normalization answers:

> Given that extracted verse string, what deterministic surface cleanup do we apply?

Therefore:

```math
\boxed{
\text{source extraction}
\neq
\text{text normalization}
}
```

The deterministic ingester verifies the full source-byte fingerprint before extracting any verse.

---

## 5. Normalization must be loss-minimizing

`text_normalized` is **not** a modern-English paraphrase.

Allowed deterministic normalization is intentionally narrow:

- Unicode normalization to NFC;
- convert non-breaking spaces to ordinary spaces;
- normalize line endings;
- collapse repeated whitespace;
- trim leading/trailing whitespace.

Do **not** alter:

- word order;
- spelling;
- archaic pronouns;
- verb forms;
- capitalization;
- punctuation;
- lexical choice.

In particular:

```text
thou / thee / thy / thine / ye
```

must not be collapsed into modern `you` in the normalized layer.

If a modern-English rendering is useful later, it must be stored as a separate explicitly lossy derivative.

---

## 6. Mechanical annotations are sidecars

Annotations live in a separate JSONL file keyed by canonical verse `id`.

In the current repository state this is a downstream contract rather than a
present tracked artifact: `corpus/annotations/mechanical.jsonl` is not included
in the canonical corpus tree. Its absence must not be interpreted as an empty
annotation result. A future materialized sidecar requires its own deterministic
manifest and may be regenerated without changing the source corpus.

Example:

```json
{
  "id": "GEN.1.3",
  "annotations": [
    {
      "kind": "command",
      "start": 14,
      "end": 32
    }
  ]
}
```

Offsets are zero-based character offsets into the referenced verse record's `text_normalized`; `end` is exclusive.

The annotation does **not** copy the matched text. The span is recovered from the canonical verse record itself:

```math
\boxed{
\text{annotation}
\rightarrow
\text{verse record}
\rightarrow
\text{exact offsets}
}
```

Initial annotation kinds remain close to recoverable surface structure:

```text
entity_mention
location_mention
temporal_marker
action
negation
question
command
conditional
causal_connective
contrast_connective
enumeration
quotation
```

A later parser may add richer relation records, but only with explicit evidence spans and without rewriting the verse text.

---

## 7. What does not belong in the mechanical layer

Do not insert labels such as:

```text
temptation
sin
faith
moral lesson
symbol of X
author intended Y
caused by Z
```

unless the literal text itself supplies that label or relation and the annotation records the supporting span.

Likewise, do not infer speaker, addressee, intent, causal role, normativity, or coreference merely because an LLM finds the inference plausible.

Those belong in later structural layers and should carry textual evidence and `OPEN` where uncertain.

---

## 8. Corpus hierarchy

The logical hierarchy is:

```text
CORPUS
 └── BOOK
      └── CHAPTER
           └── VERSE
                └── SPAN / TOKEN
```

Cross-verse and cross-book relations are stored separately rather than embedded into source text.

This keeps the evidence representation stable while allowing later graph construction.

---

## 9. Reproducible lineage

The realized lineage is:

```math
\boxed{
\text{pinned source bytes}
\rightarrow
\text{verified deterministic extraction}
\rightarrow
T_{\rm raw}+h_v
\rightarrow
T_{\rm normalized}
}
```

where:

```math
h_v=\operatorname{SHA256}(T_{\rm raw}^{(v)}).
```

The materialized JSONL has its own SHA-256 recorded in `corpus/MANIFEST.json`. Mechanical annotations remain downstream and may be deleted and regenerated independently.

Any downstream artifact may be deleted and regenerated without granting it authority over the source.

---

## 10. Minimal success criterion

The AI-parsable layer succeeds if a model can reliably retrieve and inspect:

- exact book/chapter/verse identity;
- exact source-bound KJV wording;
- deterministic normalized wording;
- stable source locator and fingerprints;
- stable annotation offsets;
- simple surface annotations;

without being handed theological or structural conclusions as if they were source facts.

The project rule is therefore:

```math
\boxed{\textbf{Make the text machine-legible before asking the machine what it means.}}
```
