# ML Didacticism

A machine-legible and structurally disciplined reading project for the King James Bible (KJV).

The project is **not** a theological replacement, doctrinal paraphrase, or claim that ancient authors intended modern ML concepts.

The first goal is simpler:

> **Make the text easy for an AI to inspect before asking the AI what the text means.**

The pipeline is:

```math
\boxed{
\text{RAW KJV}
\rightarrow
\text{normalized verse corpus}
\rightarrow
\text{mechanical annotations}
\rightarrow
\text{structural decoding}
\rightarrow
\text{bounded interpretation}
}
```

The layers must remain distinct:

```math
\boxed{
\text{RAW TEXT}
\neq
\text{NORMALIZED TEXT}
\neq
\text{ANNOTATION}
\neq
\text{STRUCTURAL PARSE}
\neq
\text{INTERPRETATION}
}
```

No later layer overwrites the layer below it.

## AI-parsable corpus layer

The canonical corpus format is **JSONL with one verse per record**.

The raw and normalized records preserve:

```text
id
book
chapter
verse
text_kjv
text_normalized
```

Mechanical annotations live in sidecar JSONL files keyed by verse `id` and use stable character spans.

Normalization is deliberately loss-minimizing. It may normalize Unicode and whitespace, but it does **not** modernize spelling, archaic pronouns, morphology, capitalization, punctuation, lexical choice, or word order.

See [`docs/AI_PARSABLE_CORPUS.md`](docs/AI_PARSABLE_CORPUS.md).

## Structural decoding layer

Only after the source is machine-legible do we ask:

> **What information structure is this text preserving?**

The structural invariant is:

```math
\boxed{\text{TEXT} \neq \text{STRUCTURAL PARSE} \neq \text{INTERPRETATION}}
```

The strongest symbol rule is:

```math
\boxed{\textbf{Every formal symbol must correspond to something actually recoverable from the text.}}
```

If a needed causal, intentional, predictive, normative, or other bridge is absent, mark it **OPEN** rather than completing it by assumption.

The structural layer may use typed objects such as:

```math
S_t = \text{state}
```

```math
R_t = \text{representation / represented distinction}
```

```math
\hat P_t = \text{prediction or prospective claim}
```

```math
A_t = \text{action / transformation}
```

```math
C_{t+1} = \text{observed consequence}
```

```math
\Pi_{t+1} = \text{provenance / causal attribution}
```

```math
\mathcal A(S_t) = \text{available / represented action structure}
```

```math
\mathcal P(S_t) = \text{explicitly permitted action structure}
```

```math
\mathcal F_H(S_t) = \text{reachable future structure over horizon }H
```

These types must not be silently collapsed:

```math
\boxed{
R \neq S,
\qquad
\hat P \neq C,
\qquad
C \neq \Pi,
\qquad
S \neq \mathcal A,
\qquad
\mathcal A \neq \mathcal P,
\qquad
\mathcal P \neq \hat P,
\qquad
\mathcal A \neq \mathcal F
}
```

Each bridge must be earned by the text.

## Project structure

### Corpus preparation

- [`docs/AI_PARSABLE_CORPUS.md`](docs/AI_PARSABLE_CORPUS.md) — minimal machine-legibility specification.
- [`corpus/README.md`](corpus/README.md) — corpus directory contract.
- [`schema/verse.schema.json`](schema/verse.schema.json) — minimal verse-record schema.
- [`schema/annotation.schema.json`](schema/annotation.schema.json) — mechanical span-annotation schema.
- [`scripts/normalize_kjv.py`](scripts/normalize_kjv.py) — deterministic Unicode/whitespace normalizer.

### Structural decoding

- [`docs/STRUCTURAL_DECODING_METHOD.md`](docs/STRUCTURAL_DECODING_METHOD.md) — decoding rules and claim discipline.
- [`genesis/01_GENESIS_01.md`](genesis/01_GENESIS_01.md) — Genesis 1: world-level differentiation, relation, recurrence, and evaluation.
- [`genesis/02_GENESIS_02.md`](genesis/02_GENESIS_02.md) — Genesis 2: agent-environment structure, role, permission, constraint, prospective consequence, and relational reconfiguration.

## Source provenance

The full KJV corpus should **not** be populated from an unspecified source.

Before ingestion, pin the source / edition, source file or retrieval location, checksum, and transformation version. Then derive every later layer reproducibly from those source bytes.

## Reading rule

Do not infer a state transition from a representation transition, or a causal explanation from an observed consequence, unless the text supplies the bridge.

A useful recurring structural question remains:

```math
\boxed{\textbf{Which futures became possible or impossible because this changed?}}
```
