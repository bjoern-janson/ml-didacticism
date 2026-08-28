# ML Didacticism

A provenance-bound structural reading of Genesis 1–50 that was used to derive a compact representation architecture, freeze it, and test it across unrelated external domains.

The project began with a simple rule:

```math
\boxed{\textbf{Make it legible first. Understand what is there second. Interpret third.}}
```

It is **not** a theological replacement, doctrinal paraphrase, claim that biblical authors intended machine-learning concepts, or claim that Genesis by itself scientifically validates a general architecture.

The scientific question only becomes interesting after the Genesis-derived result is frozen and exposed to independent pressure.

## Current status

The Genesis 1–50 structural pass is complete. The abstraction/ablation sequence is complete. The resulting Genesis-derived architecture is frozen as `AG/1`:

```math
\boxed{
\mathcal A_G
=
\{RELATION,\ REPRESENTATION\}
+
\{SOURCE\_PROVENANCE,\ OPEN\}
}
```

Current external-test ledger:

```text
T1–T9      PASS           reconstruction / transport
T10.001    CONTAMINATED   family + constructor leakage
T10.002    UNSTARTED      no independently admitted Level-3 constructor/corpus
```

The strongest calibrated transport claim currently earned is:

```math
\boxed{
\textbf{AG/1 has survived nine heterogeneous external reconstruction tests without architectural enlargement.}
}
```

No claim is yet earned that AG/1 is universal, uniquely minimal, already useful as an engineering system, or sufficient for autonomous structural invention.

---

## Start here

New readers should begin with:

1. [`docs/PROJECT_ARC.md`](docs/PROJECT_ARC.md) — the whole Genesis → AG/1 → transport → Level-3 story in plain language.
2. [`docs/SCIENTIFIC_VALUE_AND_LIMITS.md`](docs/SCIENTIFIC_VALUE_AND_LIMITS.md) — where the scientific/engineering value may lie and where the current claims stop.
3. [`docs/README.md`](docs/README.md) — canonical reading map and explanation of current versus historical directories.
4. [`abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md`](abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md) — exact frozen architecture and claim ceiling.
5. [`transport/MILESTONE_T1_T9.md`](transport/MILESTONE_T1_T9.md) — exact nine-test transport frontier.
6. [`transport/t10/MILESTONE_T10_001_CONTAMINATION.md`](transport/t10/MILESTONE_T10_001_CONTAMINATION.md) — why the first blind invention pilot does not count.
7. [`transport/10B_LEVEL3_PROTOCOL_V2_HYPOTHESIS_SPACE_ISOLATION.md`](transport/10B_LEVEL3_PROTOCOL_V2_HYPOTHESIS_SPACE_ISOLATION.md) — current Level-3 protocol.

---

## The project in one page

Genesis 1–50 was first read as structured narrative data: who did what, who knew what, what was observed, what was said, what was promised, what actually happened, and what remained unresolved.

The text repeatedly forced distinctions such as:

```text
Joseph is alive
≠ Jacob represents Joseph as dead

Joseph recognizes his brothers
≠ his brothers recognize Joseph

a genuine object is present
≠ its provenance is correctly understood

a warning is received
≠ it is believed

a prediction is stated
≠ it is realized

a promise is made
≠ it is fulfilled

an instruction is issued
≠ it is executed

a search occurs
≠ the searched-for object is found

a later explanation is given
≠ the earlier event record is replaced
```

The recurring structural lesson became:

```math
\boxed{
\textbf{what happened}
\neq
\textbf{what was observed}
\neq
\textbf{what was represented}
\neq
\textbf{what was inferred}
}
```

Or, more compactly:

```math
\boxed{\textbf{The world is not the model of the world.}}
```

That distinction is why `REPRESENTATION` survived the later ablation sequence.

---

## Small architecture, large vocabulary

The chapter readings initially used a large descriptive vocabulary: entities, states, events, time, access, evidence, commitments, obligations, authority, predictions, actions, and more.

The abstraction phase then asked which of those categories were truly primitive.

Under the explicit Genesis ablations:

| Candidate | Frozen result |
|---|---|
| `ENTITY` | derived as referential-equivalence structure over provenance-bearing relation-argument occurrences |
| `STATE` | derived as a relational slice/view |
| `EVENT` | derived as an addressable relation motif / occurrence pattern |
| `TIME` | derived from explicit temporal relation families |
| `ACCESS` | derived from concrete information-bearing relations |
| `COMMITMENT` | derived from source-earned promise/oath/surety/request/fulfillment relations |
| `AUTHORITY` | derived from proposal/command/permission/appointment/refusal/allocation/execution topology |
| `RELATION` | surviving non-meta kernel |
| `REPRESENTATION` | surviving non-meta kernel |

This leads to the project compression:

```math
\boxed{\textbf{Small architecture. Large vocabulary.}}
```

New domain predicates are allowed. New architectural species require evidence.

---

## Why REPRESENTATION is separate from history

Let `\mathcal H` denote the historical assertion graph and `\rho` a representation scope.

The architecture must allow:

```math
\boxed{
r\in content(\rho)
\not\Rightarrow
r\in\mathcal H
}
```

so that a false, future, hypothetical, reported, feared, dreamed, accused, or retrospectively inferred relation can be structurally represented without becoming world truth.

For example:

```text
HISTORY:
    Joseph alive

REPRESENTATION:
    Jacob → Joseph dead
```

The historical fact that Jacob carries that representation may itself affect later history.

So representation is not merely passive description:

```math
\boxed{
\text{world}
\rightarrow
\text{representation}
\rightarrow
\text{action}
\rightarrow
\text{changed world}
\rightarrow
\text{new evidence}
\rightarrow
\text{revised representation}
}
```

A representation can be wrong and still causally matter.

---

## SOURCE_PROVENANCE and OPEN

Two constraints remain outside the ordinary semantic basis.

### `SOURCE_PROVENANCE`

Every important assertion, representation, identity bridge, abstraction decision, and unresolved edge must remain traceable to its source basis.

```math
\boxed{
\textbf{abstraction may reduce ontology; it may not erase evidential lineage.}
}
```

### `OPEN`

`OPEN` preserves a deliberately unforced edge when the available evidence has not earned a stronger commitment.

```math
\boxed{
\text{unknown}
\neq
\text{unasserted}
\neq
\text{unlicensed}
\neq
\text{false}
}
```

The current fossilized formulation is:

```math
\boxed{
\textbf{OPEN = a reachable structural edge whose evidential path has not yet earned activation.}
}
```

See [`transport/t10/FOSSIL_OPEN_EPISTEMIC_LICENSE.md`](transport/t10/FOSSIL_OPEN_EPISTEMIC_LICENSE.md).

---

## Why the freeze matters

The Genesis result was frozen **before** external transport testing.

From that point onward:

```math
\boxed{\mathcal A_G\ \textbf{cannot learn new primitives from the external corpus being used to test it.}}
```

An external case may fit the architecture or expose a missing distinction. It may not redesign the target during the run.

This is the core causal cut:

```text
Genesis derivation
→ AG/1 freeze
→ external transport
```

The exact protocol is [`transport/00_TRANSPORT_PROTOCOL_AG1.md`](transport/00_TRANSPORT_PROTOCOL_AG1.md).

---

## External transport ledger

| Test | External pressure | Verdict |
|---|---|---|
| [`T1`](transport/01_GITLAB_2017_DATABASE_INCIDENT.md) | GitLab database incident — actual system history versus operator representation | `PASS` |
| [`T2`](transport/02_OPERA_NEUTRINO_VELOCITY.md) | OPERA/ICARUS — measurement result versus physical interpretation | `PASS` |
| [`T3`](transport/03_CHALLENGER_SHARED_EVIDENCE_ANALYSES.md) | Challenger — same presented evidence, competing analyses | `PASS` |
| [`T4`](transport/04_TB_TEST_NONIDENTIFIABILITY.md) | TB testing — same local observation, different underlying worlds | `PASS` |
| [`T5`](transport/05_MARS_CLIMATE_ORBITER_CLOSED_LOOP.md) | Mars Climate Orbiter — wrong representation drives real intervention and later evidence | `PASS` |
| [`T6`](transport/06_DEEPWATER_HORIZON_OBSERVABILITY_INTERFACE.md) | Deepwater Horizon — action changes future observation/monitoring topology | `PASS` |
| [`T7`](transport/07_ACTIVE_CHALLENGE_SELECTION_MICHELSON_MORLEY.md) | Michelson–Morley / Morley–Miller — deliberate challenge selection | `PASS` |
| [`T8`](transport/08_ARIANE501_CHALLENGE_INDEPENDENCE.md) | Ariane 501 — nominal redundancy versus failure-path independence | `PASS` |
| [`T9`](transport/09_HUBBLE_MISSING_TOPOLOGY_DISCOVERY.md) | Hubble — discovery of previously unrepresented dependency/topology | `PASS` |

Nine passes are evidence of bounded transportability under the tested conditions. They are not a universality theorem.

---

## Where the scientific value is

The Genesis pass by itself is **not** scientific validation. Its role is derivation and adversarial distinction pressure.

The potentially serious value comes from three things:

1. **Architecture:** many useful concepts may be representable as patterns over a smaller relation/representation substrate rather than requiring separate primitive machinery.
2. **Transport:** the frozen basis survived nine unrelated reconstruction tests without enlargement.
3. **Evaluation methodology:** the project found a sharper boundary between representing/recovering a distinction and genuinely inventing one.

A calibrated research statement is:

> **We used Genesis as an adversarial corpus to derive a compact representation architecture, demonstrated bounded transport across nine unrelated domains, and constructed a stricter experimental boundary for distinguishing reconstruction from genuinely novel structural invention.**

The following must remain distinct:

```math
\boxed{
\text{interesting architecture}
\neq
\text{useful system}
\neq
\text{scientifically validated theory}.
}
```

See [`docs/SCIENTIFIC_VALUE_AND_LIMITS.md`](docs/SCIENTIFIC_VALUE_AND_LIMITS.md).

---

## The Level-3 boundary

The project now distinguishes:

```math
\boxed{
\begin{aligned}
L_1 &: \text{represent a supplied distinction}\\
L_2 &: \text{recover/select a hidden distinction inside a supplied hypothesis space}\\
L_3 &: \text{invent an unsupplied distinction, risk it against reality, and retract/revise it if wrong}
\end{aligned}
}
```

T1–T9 primarily test `L1` reconstruction/transport.

### T10.001 — `CONTAMINATED`

The first blind invention pilot looked like a success: the learner generated the exact hidden structural relation and made the correct prospective prediction.

It was rejected because the same learner context had authored the narrow hidden relation family.

The key methodological result was:

```math
\boxed{
\textbf{hidden answer}
\neq
\textbf{hidden hypothesis space}
}
```

So `CONTAMINATED` is not a negative architecture result. It means the experiment failed to isolate the capability being claimed.

### T10.002 — `UNSTARTED`

The successor experiment may not begin until an independent curator/corpus clears answer-family, constructor, and challenge-interface admission gates.

The challenge interface itself must not be a disguised ontology menu.

The allowed transition is:

```text
UNSTARTED → ADMITTED → RUNNING
```

not:

```text
UNSTARTED → RUNNING
```

because:

```math
\boxed{
\text{absence of admissible evidence}
\neq
\text{evidence of capability}.
}
```

See:

- [`transport/10B_LEVEL3_PROTOCOL_V2_HYPOTHESIS_SPACE_ISOLATION.md`](transport/10B_LEVEL3_PROTOCOL_V2_HYPOTHESIS_SPACE_ISOLATION.md)
- [`transport/t10/ADMISSION_GATE_CHALLENGE_INTERFACE_COMPOSITION.md`](transport/t10/ADMISSION_GATE_CHALLENGE_INTERFACE_COMPOSITION.md)

---

## Source and corpus provenance

The source substrate is pinned to:

```text
repository: renniemaharaj/kjv-bible
commit:     88723a44bb3e3f229a34f9cf11ce1b7acf971eee
tree:       df15756d8f2922f24c36ec86081d4d3244277619
```

Pinned 66-book source-corpus SHA-512:

```text
7c2eff0219d59c683b1d12739a64facb22807770e05daf20cf1a4d22ef1b739d5ec03268abb8c3201fd69eb1014cc45a37697cb8abaceccd316c2e473db0b264
```

The canonical materialized corpus is [`corpus/kjv.jsonl`](corpus/kjv.jsonl):

```text
verse records: 31,102
first ID:      GEN.1.1
last ID:       REV.22.21
SHA-256:       b4a44c22899b0669f1d504c65a89bee2ac2dd4b08e01c2f012814f348a6ba2dc
```

See [`source/PINNED_SOURCE.json`](source/PINNED_SOURCE.json), [`source/README.md`](source/README.md), and [`corpus/MANIFEST.json`](corpus/MANIFEST.json).

---

## Repository map

```text
source/       pinned evidence substrate
corpus/       deterministic machine-readable KJV
schema/       source/annotation schemas
scripts/      source/corpus utilities

docs/         reader orientation + derivation methods
genesis/      completed Genesis 1–50 structural reading
abstraction/  relation inventory, minimization, ablations, AG/1 freeze
transport/    frozen external tests + Level-3 boundary

decoder/      earlier research scaffolding
heldout/      earlier heldout workflow artifacts
diagnosis/    earlier diagnosis/discrimination artifacts
verification/ earlier re-derivation/verification artifacts
```

The last four historical directories are preserved as provenance. They are not the current canonical research path.

Likewise, [`docs/STRUCTURAL_DECODING_METHOD.md`](docs/STRUCTURAL_DECODING_METHOD.md) is derivation-era working notation: it uses categories such as `STATE` that were later tested and removed as primitive architecture candidates. Working vocabulary is not the frozen primitive basis.

---

## Claim ceiling

This repository currently supports the bounded statement:

```math
\boxed{
\textbf{Genesis supplied a compact candidate architecture, and that frozen architecture reconstructed nine heterogeneous external cases without enlargement.}
}
```

It does **not** currently establish:

```text
RELATION + REPRESENTATION is universally sufficient.
AG/1 is mathematically unique or irreducible under every formalism.
Nine passes estimate the probability of success on arbitrary future domains.
AG/1 improves a production AI system.
AG/1 is a general scientific theory of intelligence or reality.
Level-3 structural invention has been demonstrated.
T10.002 is authorized to run.
```

The strongest project discipline is therefore:

```math
\boxed{
\textbf{Never give a distinction more authority than its provenance has earned.}
}
```

**Decode the book.**