# Documentation Map

This repository contains both the **current canonical research path** and earlier scaffolding that records how the project got there.

Do not assume every file describes the current architecture.

The quickest rule is:

```math
\boxed{
\textbf{historical derivation artifacts are preserved; current claims are read from the frozen milestones.}
}
```

---

## If you read only seven files

Read these in order:

1. [`PROJECT_ARC.md`](PROJECT_ARC.md) — plain-language story from Genesis 1–50 through the Level-3 boundary.
2. [`SCIENTIFIC_VALUE_AND_LIMITS.md`](SCIENTIFIC_VALUE_AND_LIMITS.md) — what is scientifically interesting, what is not yet established, and where engineering value would have to come from.
3. [`AI_PARSABLE_CORPUS.md`](AI_PARSABLE_CORPUS.md) — how source bytes, verse records, normalization, annotations, structure, and interpretation are kept separate.
4. [`../abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md`](../abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md) — the frozen Genesis-derived architecture and exact claim ceiling.
5. [`../transport/MILESTONE_T1_T9.md`](../transport/MILESTONE_T1_T9.md) — the nine external transport passes and the reconstruction/invention boundary.
6. [`../transport/t10/MILESTONE_T10_001_CONTAMINATION.md`](../transport/t10/MILESTONE_T10_001_CONTAMINATION.md) — why the first blind Level-3 pilot does not count.
7. [`../transport/10B_LEVEL3_PROTOCOL_V2_HYPOTHESIS_SPACE_ISOLATION.md`](../transport/10B_LEVEL3_PROTOCOL_V2_HYPOTHESIS_SPACE_ISOLATION.md) — the current Level-3 protocol and `T10.002 = UNSTARTED` admission rule.

For the final `OPEN`/admission refinement, also read:

- [`../transport/t10/ADMISSION_GATE_CHALLENGE_INTERFACE_COMPOSITION.md`](../transport/t10/ADMISSION_GATE_CHALLENGE_INTERFACE_COMPOSITION.md)
- [`../transport/t10/FOSSIL_OPEN_EPISTEMIC_LICENSE.md`](../transport/t10/FOSSIL_OPEN_EPISTEMIC_LICENSE.md)

---

## Current canonical research path

The present project lineage is:

```text
source/
  immutable evidence pin
    ↓
corpus/
  deterministic machine-readable KJV
    ↓
genesis/01 ... genesis/50
  chapter-by-chapter legibility-first structural reading
    ↓
abstraction/00 ... abstraction/11
  relation inventory, stripping tests, adversarial ablations
    ↓
abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md
  AG/1 fossil
    ↓
transport/00_TRANSPORT_PROTOCOL_AG1.md
  frozen external-test rules
    ↓
transport/01 ... transport/09
  nine heterogeneous reconstruction tests
    ↓
transport/MILESTONE_T1_T9.md
  reconstruction frontier
    ↓
transport/t10/*
  Level-3 invention boundary, contamination audit, admission gates
```

The frozen architecture is:

```math
\boxed{
\mathcal A_G
=
\{RELATION,\ REPRESENTATION\}
+
\{SOURCE\_PROVENANCE,\ OPEN\}
}
```

Current experimental status:

```text
T1–T9      PASS           reconstruction / transport
T10.001    CONTAMINATED   family + constructor leakage
T10.002    UNSTARTED      no independently admitted constructor/corpus
```

---

## What the Genesis chapter files are

[`../genesis/`](../genesis/) contains the completed Genesis 1–50 first-pass structural reading.

These files use a large descriptive vocabulary because their job was **preservation before minimization**.

Terms such as:

```text
state
event
access
authority
commitment
obligation
time
entity
```

can appear throughout the chapter readings without implying that they survived as architecture primitives.

That distinction is essential:

```math
\boxed{
\text{derivation vocabulary}
\neq
\text{frozen primitive basis}.
}
```

The ablation sequence exists precisely because the project first preserved those distinctions generously and only later tested whether their umbrella categories were architecturally necessary.

---

## What the abstraction directory is

[`../abstraction/`](../abstraction/) is the minimization trail.

The useful reading order is numeric:

```text
00  abstraction protocol
01  cross-chapter relation inventory
02  invariant stripping tests
03  initial minimal-architecture candidate
04  early commitment/authority ablation
05  state/access ablation
06  event ablation
07  relation ablation
08  time ablation
09  representation ablation
10  final commitment/authority ablation
11  entity ablation
12  frozen Genesis architecture AG/1
```

Artifacts `00`–`11` are historical derivation evidence. `12` freezes the result and claim ceiling.

Do not edit `12` to accommodate later domains.

---

## What the transport directory is

[`../transport/`](../transport/) tests the frozen architecture against external domains.

The governing rule is:

```math
\boxed{
\mathcal A_G\text{ cannot learn new primitives from the corpus it is being tested on.}
}
```

New domain vocabulary is allowed. New architecture species are not.

The test sequence is:

```text
01  GitLab database incident
02  OPERA / ICARUS neutrino anomaly
03  Challenger shared evidence / competing analyses
04  TB testing non-identifiability
05  Mars Climate Orbiter closed epistemic loop
06  Deepwater Horizon observation-topology modification
07  Michelson–Morley / Morley–Miller challenge selection
08  Ariane 501 challenge independence / common-mode validation
09  Hubble missing-topology discovery
```

All nine return `PASS` under their bounded reconstruction questions.

`PASS` means only that the tested corpus did not force a new primitive under the frozen protocol.

---

## What T10 is

T10 changes the task class.

T1–T9 are fundamentally reconstruction tests:

```text
source eventually contains distinction
→ can AG/1 represent it?
```

T10 asks whether a learner can produce a distinction **before the evaluator supplies it**:

```text
contradiction
→ unsupplied structural candidate
→ prospective prediction
→ empirical challenge
→ retain / retract / revise / OPEN
```

The first blind pilot is preserved under [`../transport/t10/`](../transport/t10/) but is permanently classified `CONTAMINATED` because the learner context knew the narrow hidden relation family.

The successor protocol requires independent answer-family and constructor isolation.

`T10.002` is intentionally `UNSTARTED` until an external curator/corpus passes the admission gate.

---

## Earlier / historical scaffolding

Several directories predate the current Genesis 1–50 → AG/1 → transport program boundary.

They are preserved for provenance and research history, but they are **not the current canonical workflow**.

### `decoder/`

Earlier decoder artifacts and manifests.

### `diagnosis/`

Earlier failure-clustering and discrimination work.

### `heldout/`

Earlier heldout Genesis parses/manifests and scoring artifacts.

### `verification/`

Earlier chapter re-derivation/canonical-record audits.

These artifacts should not be deleted merely because the later program changed direction. Their existence documents the development history.

But new readers should not infer from them that the current project still uses the old heldout/decoder benchmark framing.

---

## Derivation-era method document

[`STRUCTURAL_DECODING_METHOD.md`](STRUCTURAL_DECODING_METHOD.md) is explicitly a **working/revisable structural method** from the derivation phase.

It uses convenient typed objects such as `STATE`, action, prediction, and future-space notation because those were useful while reading the text.

Later ablations tested those categories as architectural candidates and removed several of them from the primitive basis.

Therefore:

```math
\boxed{
\text{working parse notation}
\neq
\text{final frozen architecture}.
}
```

Read it for method lineage, not as the final ontology specification.

---

## Operational support directories

These remain current support infrastructure rather than architecture claims:

### `source/`

Pinned source identity and byte/provenance boundary.

### `corpus/`

Materialized `kjv.jsonl`, manifest, and mechanical annotation contract.

### `schema/`

JSON schemas for source/annotation records.

### `scripts/`

Source fetching, normalization, ingestion, and early verification utilities.

### `.github/workflows/`

Tracked automation for materialization and verification.

---

## Freeze discipline

When a file says `FROZEN`, `FOSSILIZED`, or `FROZEN TEST PROTOCOL`, treat that status literally.

Later summaries may explain those artifacts but should not silently rewrite their historical claims.

The project uses versioned transitions instead:

```math
\boxed{
A_{old}
\neq
A_{new}
}
```

with the evidence causing any transition preserved explicitly.

---

## New-reader claim ceiling

The repository currently supports:

```math
\boxed{
\textbf{a compact Genesis-derived architecture survived nine heterogeneous bounded reconstruction tests without enlargement.}
}
```

It does not currently support:

```text
AG/1 is universal.
AG/1 is uniquely minimal.
AG/1 is already proven useful as an engineering system.
Level-3 structural invention has been demonstrated.
T10.002 is merely waiting to be run.
```

The Level-3 boundary remains `OPEN`, and `T10.002` remains `UNSTARTED` until an independent admission is actually earned.

**Decode the book.**