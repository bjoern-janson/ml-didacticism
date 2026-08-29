# Research Memory — Warrant-Aware Selective Correction Prototype

**Status:** ENGINEERING PROTOTYPE / INSTRUMENTATION / NON-EVIDENTIAL / NOT L2 / NOT L3

This directory turns one lesson from `ml-didacticism` into a deliberately boring systems object:

```math
\boxed{
\textbf{Does preserving authority-producing lineage improve future selective correction?}
}
```

It does **not** assume the answer is yes.

The three memory policies are hypotheses under comparison:

```math
\boxed{
\begin{aligned}
A &: \text{claims + ordinary computational dependency}\\
B &: A + \text{source provenance}\\
C &: B + \text{transformation-instance / warrant lineage}.
\end{aligned}}
```

Possible outcomes include:

```math
C>B>A,\qquad B\approx C>A,\qquad A\approx B\approx C,
```

or any other ordering supported by a future admitted experiment.

The present code is an engineering scaffold that proves the representations, evaluator, paired cases, and typed correction delta can be executed. Its deterministic outcomes are **not** scientific evidence that real learners benefit from policy `C`.

---

## 1. Portable discipline

The implementation carries four reusable rules:

```math
\boxed{
\textbf{preserve distinctions}
\rightarrow
\textbf{track authority-producing transformations}
\rightarrow
\textbf{retain defeater pathways}
\rightarrow
\textbf{test selective correction}.
}
```

The central non-collapse is:

```math
\boxed{
\text{recompute}
\neq
\text{reconsider}
\neq
\text{retract}
\neq
\text{erase history}.
}
```

A defeater therefore produces a typed authority delta rather than a rewritten worldview.

---

## 2. Minimal memory object

Conceptually:

```math
\boxed{
\mathcal M=
\langle
K,\tau,\mathcal W,\mathcal P,\mathcal D,\mathcal R
\rangle
}
```

where:

```text
K            claims/results
tau          realized transformation instances
W            current warrant paths
P            provenance
D            defeaters
R            reopening/reconstruction handles
```

This prototype does not attempt to model a complete mind.

---

## 3. Core operation

The only correction operation under test is:

```text
REASSESS(defeater)
```

Its output is a typed delta:

```text
defeater_locus
affected_authority_instances
removed_warrant_paths
reopened_claims
retained_claims
narrowed_scopes
required_recomputations
preserved_history
repair_cost
```

The operation is intentionally **non-generative**. It accounts for authority change; it does not invent a replacement theory.

The audit question is:

```math
\boxed{
\textbf{Which authority disappeared because of this specific defeated reason, and what remains warranted independently?}
}
```

---

## 4. Present-task matching

Every policy receives the same research history.

Before a defeater, the runner checks:

```math
\boxed{
V_{\rm now}(A)
\approx
V_{\rm now}(B)
\approx
V_{\rm now}(C)
}
```

at the resolution represented here: the same currently warranted derived outputs are available to all three policies.

This is an engineering precondition, not a proof of full behavioral equivalence.

The intended future experiment is interesting only if correction differences appear **after contradiction**, not because one system simply solved the present task better.

---

## 5. Adversarial scenario matrix

`scenarios.py` contains small paired cases whose local anomaly language is intentionally similar while the correct authority consequences differ.

| Scenario | Correct epistemic behavior |
|---|---|
| `alternate_support` | withdraw one route; retain claim through independent support |
| `sole_support` | reopen claim after its sole route is defeated |
| `scope_only` | narrow authority scope rather than retract |
| `operational_null` | retain epistemic authority; failed event carried no warrant |
| `instance_not_operator` | defeat one instance; preserve another use of same operator |
| `operator_invalid` | reassess all affected instances of invalid operator |
| `route_locked` | propagate authority loss through a provenance-locked route while preserving independent support |

The key anti-shortcut property is:

```math
\boxed{
E_a\approx_{\rm surface}E_b
\quad\text{while}\quad
Correction(E_a)\neq Correction(E_b).
}
```

This is meant to break generic policies such as:

```text
contradiction → reopen nearest claim
defeated instance → blacklist operator
dependency descendant → inherited warrant
defeater → always change something
```

---

## 6. Policies

### A — dependency only

`DependencyOnlyMemory` retains claims and ordinary computational dependency.

Its reassessment baseline treats a named failed dependency as a reason to reopen the computational descendant cone.

This intentionally exposes the failure mode:

```math
\boxed{
\text{computational dependence}
\neq
\text{warrant dependence}.
}
```

### B — source provenance

`SourceProvenanceMemory` adds source identity to dependency structure.

It can preserve support coming from a different source and can propagate ordinary support loss through the dependency graph, but it does not retain explicit transformation-instance warrant paths, authority scope, provenance-locked routes, or operational-versus-epistemic typing.

This tests whether cheaper source provenance captures most of the useful correction value.

### C — warrant lineage

`WarrantLineageMemory` retains explicit transformation-instance and warrant-path semantics.

In this prototype it has evaluator-equivalent stored semantics and therefore acts as an engineering upper bound.

That is **not** learner evidence. A real experiment must require a system to build/use such memory prospectively rather than receive private gold semantics for free.

---

## 7. Metrics

The evaluator keeps correction quality vector-valued:

```math
\boxed{
\mathcal M=
\langle
R_W,P_W,I_P,S_A,H_P,R_C,C_R,T_R
\rangle.
}
```

Current operational readings:

```text
R_W   affected-authority recall
P_W   affected-authority precision
I_P   independent-support preservation
S_A   authority-scope accuracy
H_P   historical-preservation recall
R_C   recomputation correctness
C_R   authority-change count (repair-cost component)
T_R   deterministic records-inspected proxy (latency/work component)
```

The evaluator also reports:

```text
removed warrant-path precision/recall
reopened-claim precision/recall
exact typed-delta match
```

`C_R` and `T_R` are instrumentation proxies, not final scientific cost/latency definitions.

---

## 8. Run

Standard library only:

```bash
python research-memory/self_test.py
```

Then inspect the full matrix:

```bash
python research-memory/run_experiment.py
```

The runner prints private gold, policy outputs, and metric vectors because this is an inspectable engineering prototype.

A future admitted evaluation must not expose gold this way.

---

## 9. What could falsify or narrow the hypothesis

The scientific hypothesis must be allowed to lose.

A future independently admitted comparison should narrow or reject the transformation-lineage claim if:

```math
A\approx B\approx C
```

on selective correction.

If:

```math
B\approx C>A,
```

then explicit transformation lineage may add little beyond source provenance in that environment.

If `C` helps only on handcrafted toy cases, the claim remains toy-scoped.

If `C` improves correction but damages present capability or costs too much to maintain, the engineering question becomes a compression tradeoff rather than a correctness victory.

No ordering is pre-authorized.

---

## 10. Compression stage — deliberately not implemented

Do not scale graph depth yet.

If transformation-aware lineage earns value first, the next comparison is:

```math
\begin{aligned}
C_0 &: \text{full active lineage}\\
C_1 &: \text{compressed + reconstruction handle}\\
C_2 &: \text{compressed + handle + live trigger}\\
C_3 &: \text{recoverable but trigger-blind}\\
C_4 &: \text{irrecoverable}.
\end{aligned}
```

That future stage tests:

```math
\boxed{
\text{storage}
\neq
\text{recoverability}
\neq
\text{triggerability}
\neq
\text{correction quality}.
}
```

It is not implemented here.

---

## 11. L2/L3 boundary remains unchanged

This directory does not admit the existing `frontier/benchmark_nucleus/l2_constructor/`.

It does not create an independent constructor.

It does not move:

```text
L2 = UNADMITTED
L3 = BLOCKED
```

The existing admission contract remains binding.

The present prototype asks a simpler engineering question under known semantics:

```math
\boxed{
\textbf{Can different retained memory structures support different correction behavior after the same accumulated history?}
}
```

A scientific learner claim still requires independently constructed hidden worlds, sufficient-but-not-answer-shaped learner evidence, prospective freeze, and private gold.

---

## 12. Terminal engineering principle

```math
\boxed{
\textbf{Don't just preserve what the system learned. Preserve what made the learning authoritative.}
}
```

But treat that as a design hypothesis, not a result.

The result-bearing question is:

```math
\boxed{
\textbf{Does remembering what made a conclusion authoritative actually make a system better at surviving a later upstream defeater?}
}
```
