# ML Didacticism

A structural reading project for the King James Bible (KJV) using machine-learning, causal, state-transition, representation, and information-processing language as an analytic lens.

The project is **not** a theological replacement, doctrinal paraphrase, or claim that ancient authors intended modern ML concepts.

The current experiment is a provenance-bound held-out decoder evaluation:

```math
\boxed{
\text{Genesis 1--2 calibration}
\rightarrow
D_1^F
\rightarrow
T_{\mathrm{GEN.3}}^F
\rightarrow
P_3^F
\rightarrow
A_3
}
```

where the audit may change confidence in the decoder but may not rewrite the frozen decoder or its held-out output.

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

The held-out invariant is:

```math
\boxed{
A_3\text{ may alter confidence in }D_1
\quad\neq\quad
A_3\text{ may alter }D_1\text{ or }P_3
}
```

## Experimental status

```text
source pinned                           ✓
deterministic extractor implemented   ✓
source fingerprint verified           ✓
corpus materialized                   ✓
ingestion verification                ✓
Genesis 1 canonical re-derivation     ✓
Genesis 2 canonical re-derivation     ✓
D1 frozen before Genesis 3             ✓
Genesis 3 held-out parse P3 frozen    ✓
P3 frozen before scoring               ✓
A3 scoring audit complete              ✓
D1 modified by A3                      ✗
P3 modified by A3                      ✗
D2 proposed inside A3                  ✗
```

The clean causal sequence is:

```text
Genesis 1–2
   ↓
canonical re-derivation audits
   ↓
D1
   ↓
FREEZE
   ↓
Genesis 3
   ↓
P3
   ↓
FREEZE
   ↓
A3 scoring audit
   ↓
belief update about D1
   ↓
only afterward: possible successor decoder
```

## Held-out Genesis 3 result

Frozen D1 was scored on frozen P3 against the predeclared error axes:

```text
unsupported structural promotion
missed recoverable structure
```

using claim/abstention-level classifications:

```text
SURVIVED
FALSE PROMOTION
MISSED STRUCTURE
CORRECT ABSTENTION
NEW FAILURE MODE
```

A3 found:

```text
FALSE PROMOTION:       1
MISSED STRUCTURE:      12
NEW FAILURE MODE:      0
explicit OPEN items:   49
correct OPEN items:    49
```

Therefore:

```math
\boxed{
49/49\ \text{explicit OPENs were correct abstentions}
}
```

and:

```math
\boxed{
\text{D1 generalized its epistemic boundary; its remaining failure is predominantly structural coverage.}
}
```

The observed misses cluster around:

```text
explicit discourse / connective edges
predicate detail
speaker / action attribution
temporal relations
cross-verse proposition correspondence
```

This clustering is a diagnostic result, not a decoder repair.

See:

- [`heldout/genesis/03_A3_SCORING_AUDIT.md`](heldout/genesis/03_A3_SCORING_AUDIT.md)
- [`heldout/genesis/03_A3_MANIFEST.json`](heldout/genesis/03_A3_MANIFEST.json)

The original [`heldout/genesis/03_P3_MANIFEST.json`](heldout/genesis/03_P3_MANIFEST.json) intentionally remains frozen at its pre-scoring state and therefore still records `scoring_status: NOT_RUN`. The later A3 artifacts record the audit without mutating that historical checkpoint.

## Source status

Pinned source:

```text
repository: renniemaharaj/kjv-bible
commit:     88723a44bb3e3f229a34f9cf11ce1b7acf971eee
tree:       df15756d8f2922f24c36ec86081d4d3244277619
```

Pinned 66-book source-corpus SHA-512:

```text
7c2eff0219d59c683b1d12739a64facb22807770e05daf20cf1a4d22ef1b739d5ec03268abb8c3201fd69eb1014cc45a37697cb8abaceccd316c2e473db0b264
```

“KJV” is not treated as a sufficient source identifier. The immutable git snapshot and fingerprints identify the source bytes; upstream historical/edition labels remain provenance claims rather than authority supplied by this repository.

## Materialized corpus

The canonical machine-readable artifact is [`corpus/kjv.jsonl`](corpus/kjv.jsonl):

```text
verse records: 31,102
first ID:      GEN.1.1
last ID:       REV.22.21
SHA-256:       b4a44c22899b0669f1d504c65a89bee2ac2dd4b08e01c2f012814f348a6ba2dc
```

The deterministic ingestion result is frozen in [`corpus/MANIFEST.json`](corpus/MANIFEST.json).

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

Mechanical annotations are sidecars that reference canonical verse records by ID and exact character offsets; they do not copy matched text into the annotation record.

## Structural-decoding discipline

The structural layer obeys:

```math
\boxed{\text{TEXT} \neq \text{STRUCTURAL PARSE} \neq \text{INTERPRETATION}}
```

and:

```math
\boxed{\textbf{Every formal symbol must correspond to something actually recoverable from the text.}}
```

Frozen D1 adds the governing admission rule:

```math
\boxed{
\text{weaker textual relation}
\not\Rightarrow
\text{stronger formal type}
}
```

A stronger formal type is admissible only when the text supplies the bridge required for that strengthening.

At the same time:

```math
\boxed{
\text{everything}=\mathrm{OPEN}
}
```

is not an acceptable decoder because it destroys recoverable structure. The objective is to preserve maximal textually licensed structure while minimizing unsupported formal commitment.

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

## Calibration and held-out artifacts

Genesis 1–2 were re-derived from verified canonical slices before D1 was frozen:

- [`verification/genesis/01_REDERIVATION_AUDIT.md`](verification/genesis/01_REDERIVATION_AUDIT.md)
- [`verification/genesis/02_REDERIVATION_AUDIT.md`](verification/genesis/02_REDERIVATION_AUDIT.md)

The original derivative analyses remain historical downstream artifacts rather than canonical evidence:

- [`genesis/01_GENESIS_01.md`](genesis/01_GENESIS_01.md)
- [`genesis/02_GENESIS_02.md`](genesis/02_GENESIS_02.md)

Frozen decoder:

- [`decoder/D1.md`](decoder/D1.md)
- [`decoder/D1_MANIFEST.json`](decoder/D1_MANIFEST.json)

Frozen held-out Genesis 3 output:

- [`heldout/genesis/03_P3_RAW_PARSE.md`](heldout/genesis/03_P3_RAW_PARSE.md)
- [`heldout/genesis/03_P3_MANIFEST.json`](heldout/genesis/03_P3_MANIFEST.json)

Post-freeze audit:

- [`heldout/genesis/03_A3_SCORING_AUDIT.md`](heldout/genesis/03_A3_SCORING_AUDIT.md)
- [`heldout/genesis/03_A3_MANIFEST.json`](heldout/genesis/03_A3_MANIFEST.json)

## Project structure

- [`source/PINNED_SOURCE.json`](source/PINNED_SOURCE.json) — immutable upstream source pin and byte fingerprint.
- [`source/README.md`](source/README.md) — source/evidence boundary.
- [`corpus/kjv.jsonl`](corpus/kjv.jsonl) — materialized 31,102-verse evidence substrate.
- [`corpus/MANIFEST.json`](corpus/MANIFEST.json) — deterministic ingestion fingerprint and boundaries.
- [`.github/workflows/materialize-corpus.yml`](.github/workflows/materialize-corpus.yml) — reproducible GitHub-side materialization and verification.
- [`docs/AI_PARSABLE_CORPUS.md`](docs/AI_PARSABLE_CORPUS.md) — machine-readable corpus specification.
- [`schema/verse.schema.json`](schema/verse.schema.json) — provenance-bound canonical verse schema.
- [`schema/annotation.schema.json`](schema/annotation.schema.json) — offset-only mechanical sidecar annotation schema.
- [`scripts/ingest_kjv.py`](scripts/ingest_kjv.py) — deterministic source verifier/extractor.
- [`scripts/normalize_kjv.py`](scripts/normalize_kjv.py) — loss-minimizing normalizer that preserves provenance.
- [`docs/STRUCTURAL_DECODING_METHOD.md`](docs/STRUCTURAL_DECODING_METHOD.md) — downstream structural-decoding rules.
- [`verification/genesis/`](verification/genesis/) — canonical Genesis 1–2 substrate slices and re-derivation audits.
- [`decoder/`](decoder/) — frozen decoder artifacts.
- [`heldout/genesis/`](heldout/genesis/) — frozen Genesis 3 parse and post-freeze audit artifacts.

## Current boundary

The Genesis 3 held-out evaluation is complete through `A3`.

The repository therefore currently supports the empirical statement:

```math
\boxed{
\textbf{D1 generalized its epistemic boundary; remaining error was predominantly structural coverage.}
}
```

The next legitimate operation, if taken, is a **separate post-audit analysis** asking what minimal decoder deficiency accounts for the held-out failures and whether those failures earn a successor decoder.

That operation must not rewrite the historical `D1`, `P3`, or `A3` artifacts.
