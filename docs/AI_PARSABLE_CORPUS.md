# AI-Parsable KJV Corpus

**Status:** corpus-preparation specification / pre-interpretive

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

- `T_raw` is the exact source KJV verse text;
- `T_normalized` is a deterministic, loss-minimizing surface normalization;
- `A_mechanical` is recoverable span-level annotation;
- `S_structural` is the later typed structural decoding;
- `I_interpretive` is any stronger interpretive claim.

The governing boundary is:

```math
\boxed{\text{annotation} \neq \text{interpretation}}
```

and the corpus must preserve:

```math
\boxed{T_{\rm raw} \neq T_{\rm normalized} \neq T_{\rm annotated}}
```

No layer overwrites the layer below it.

---

## 1. One verse = one record

The canonical interchange format is **JSONL**.

Each line contains one verse record with a stable identifier:

```text
GEN.1.1
GEN.1.2
GEN.1.3
...
```

The minimal verse record is:

```json
{
  "id": "GEN.1.3",
  "book": "Genesis",
  "chapter": 1,
  "verse": 3,
  "text_kjv": "And God said, Let there be light: and there was light.",
  "text_normalized": "And God said, Let there be light: and there was light."
}
```

Book, chapter, and verse hierarchy are therefore explicit rather than inferred from surrounding prose.

---

## 2. Normalization must be loss-minimizing

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

must not be collapsed into modern `you` in the normalized layer. Those forms can encode distinctions that would otherwise be destroyed.

If a modern-English rendering is useful later, it must be stored as a separate explicitly lossy derivative.

---

## 3. Mechanical annotations are sidecars

Annotations should live in a separate JSONL file keyed by verse `id`.

Example:

```json
{
  "id": "GEN.1.3",
  "annotations": [
    {
      "kind": "command",
      "start": 14,
      "end": 32,
      "text": "Let there be light"
    }
  ]
}
```

Offsets are zero-based character offsets into `text_normalized`; `end` is exclusive.

Initial annotation kinds should remain close to recoverable surface structure:

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

## 4. What does not belong in the mechanical layer

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

Likewise, do not infer `speaker`, `addressee`, intent, causal role, normativity, or coreference merely because an LLM finds the inference plausible.

Those belong in later structural layers and should carry textual evidence and `OPEN` where uncertain.

---

## 5. Corpus hierarchy

The logical hierarchy is:

```text
CORPUS
 └── BOOK
      └── CHAPTER
           └── VERSE
                └── SPAN / TOKEN
```

Cross-verse and cross-book relations are stored separately rather than embedded into raw verse records.

This keeps the source representation stable while allowing later graph construction:

```text
verse → verse
entity → entity
entity → location
entity → action
action → consequence
statement → statement
passage → cited passage
```

---

## 6. Provenance rule

The full corpus should not be populated from an unspecified KJV source.

Before ingestion, pin:

- source / edition;
- retrieval location or source file;
- retrieval date if applicable;
- source file checksum;
- transformation script version.

Then every derived corpus can be reproduced from the exact raw source.

The desired lineage is:

```math
\boxed{
\text{source bytes}
\rightarrow
\text{verse records}
\rightarrow
\text{normalized records}
\rightarrow
\text{annotations}
}
```

with no irreversible overwrite.

---

## 7. Minimal success criterion

The AI-parsable layer succeeds if a model can reliably retrieve and inspect:

- exact book/chapter/verse identity;
- exact KJV wording;
- deterministic normalized wording;
- stable character spans;
- simple surface annotations;

without being handed theological or structural conclusions as if they were source facts.

The project rule is therefore:

```math
\boxed{\textbf{Make the text machine-legible before asking the machine what it means.}}
```
