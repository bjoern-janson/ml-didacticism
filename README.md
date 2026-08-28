# ML Didacticism

A structural reading project for the King James Bible (KJV) using machine-learning, causal, state-transition, representation, and information-processing language as an analytic lens.

The project is **not** a theological replacement, doctrinal paraphrase, or claim that ancient authors intended modern ML concepts.

## Canonical order

```math
\boxed{
\text{SOURCE}
\rightarrow
\text{PARSABLE CORPUS}
\rightarrow
\text{STRUCTURAL DECODING}
\rightarrow
\text{INTERPRETATION}
}
```

The governing evidence invariant is:

```math
\boxed{\textbf{downstream revisions never mutate upstream evidence}}
```

The current exact source snapshot is pinned under [`source/`](source/).

## Source status

Pinned source:

```text
repository: renniemaharaj/kjv-bible
commit:     88723a44bb3e3f229a34f9cf11ce1b7acf971eee
tree:       df15756d8f2922f24c36ec86081d4d3244277619
```

Pinned 66-book corpus SHA-512:

```text
7c2eff0219d59c683b1d12739a64facb22807770e05daf20cf1a4d22ef1b739d5ec03268abb8c3201fd69eb1014cc45a37697cb8abaceccd316c2e473db0b264
```

“KJV” is not treated as a sufficient source identifier. The immutable git snapshot and fingerprints identify the source bytes; upstream historical/edition labels remain provenance claims rather than authority supplied by this repository.

## Verse identity

```math
\boxed{\text{verse ID} \neq \text{evidence}}
```

A verse ID such as `GEN.1.1` is an address.

A canonical verse record is bound to evidence by:

```text
pinned repository + commit + tree
source book file
JSON pointer
source-file SHA-512
verse-text SHA-256
```

The intended relation is:

```math
\boxed{
\text{canonical verse}
\leftrightarrow
\text{exact source bytes}
\leftrightarrow
\text{deterministic extraction}
}
```

## Machine-readable layer

The corpus pipeline is:

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

with:

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

The canonical verse format is documented in [`docs/AI_PARSABLE_CORPUS.md`](docs/AI_PARSABLE_CORPUS.md) and [`corpus/README.md`](corpus/README.md).

The deterministic ingester is [`scripts/ingest_kjv.py`](scripts/ingest_kjv.py). It verifies the pinned source-byte fingerprint before emitting any verse.

## Structural-decoding discipline

The structural layer still obeys:

```math
\boxed{\text{TEXT} \neq \text{STRUCTURAL PARSE} \neq \text{INTERPRETATION}}
```

and:

```math
\boxed{\textbf{Every formal symbol must correspond to something actually recoverable from the text.}}
```

If a needed causal, intentional, predictive, normative, or other bridge is absent, mark it **OPEN** rather than completing it by assumption.

Typed structural objects may include:

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

These types must not be silently collapsed.

## Project structure

- [`source/PINNED_SOURCE.json`](source/PINNED_SOURCE.json) — immutable upstream source pin and byte fingerprint.
- [`source/README.md`](source/README.md) — source/evidence boundary.
- [`docs/AI_PARSABLE_CORPUS.md`](docs/AI_PARSABLE_CORPUS.md) — machine-readable corpus specification.
- [`schema/verse.schema.json`](schema/verse.schema.json) — provenance-bound canonical verse schema.
- [`schema/annotation.schema.json`](schema/annotation.schema.json) — mechanical sidecar annotation schema.
- [`scripts/ingest_kjv.py`](scripts/ingest_kjv.py) — deterministic source verifier/extractor.
- [`scripts/normalize_kjv.py`](scripts/normalize_kjv.py) — loss-minimizing normalizer that preserves provenance.
- [`docs/STRUCTURAL_DECODING_METHOD.md`](docs/STRUCTURAL_DECODING_METHOD.md) — downstream structural-decoding rules.
- [`genesis/01_GENESIS_01.md`](genesis/01_GENESIS_01.md) — derivative Genesis 1 analysis.
- [`genesis/02_GENESIS_02.md`](genesis/02_GENESIS_02.md) — derivative Genesis 2 analysis.

Genesis 1–2 are analyses, not canonical evidence. Once `corpus/kjv.jsonl` is materialized from the pinned source, they should be rechecked against those canonical verse records before further chapter decoding.
