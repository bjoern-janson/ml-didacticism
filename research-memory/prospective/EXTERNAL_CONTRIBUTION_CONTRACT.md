# External Contribution Contract — Independent Prospective Correction Test

**Status:** FROZEN EXTERNAL-CONTRIBUTION CONTRACT / NOT AN EXPERIMENT / NOT EVIDENCE / L2 REMAINS UNADMITTED / L3 REMAINS BLOCKED

This artifact freezes the minimum contract for the next authority-bearing stage of the `research-memory/` program.

The internal prospective scaffold has already established temporal separation:

```math
\boxed{
\text{accumulate}
\rightarrow
\text{freeze}
\rightarrow
\text{select defeater later}.
}
```

That is an engineering property of the scaffold.

The next scientific step requires a stronger causal separation between the people who proposed the hypothesis and the people who constitute the test.

The governing non-collapse is:

```math
\boxed{
\text{hypothesis design}
\neq
\text{world construction}
\neq
\text{defeater selection}
\neq
\text{gold derivation}.
}
```

This is not a claim of literal statistical independence. It is a requirement that the authority-bearing design decisions relevant to the test are not all inherited from the same internally authored hypothesis space.

---

## 1. Scientific question

The external contribution must be capable of testing, not assuming, the question:

```math
\boxed{
\textbf{Does preserving authority-producing lineage improve future selective correction?}
}
```

The compared memory representations remain:

```math
\boxed{
\begin{aligned}
A &: \text{claims + ordinary computational dependency}\\
B &: A + \text{source provenance}\\
C &: B + \text{transformation-instance / warrant lineage}.
\end{aligned}
}
```

No ordering is pre-authorized.

Legitimate scoped outcomes include:

```math
C>B>A,
\qquad
B\approx C>A,
\qquad
A\approx B\approx C,
```

or other orderings supported by the admitted result vector.

The external constructor must be free to produce worlds in which explicit transformation/warrant lineage provides no additional correction value.

---

## 2. Required causal order

An admissible external case must preserve:

```text
external construction
        ↓
prospective history
        ↓
FREEZE
        ↓
post-freeze defeater
        ↓
learner-facing observation
        ↓
prospective learner correction
        ↓
private gold comparison
        ↓
result interpretation
```

Formally:

```math
\boxed{
\text{construct}
\rightarrow
\text{freeze}
\rightarrow
\text{defeat}
\rightarrow
\text{observe}
\rightarrow
\text{predict}
\rightarrow
\text{compare}.
}
```

The history must exist before the particular later defeater is selected.

The learner output must be frozen before private gold is revealed or inspected for scoring adaptation.

---

## 3. Independence requirements

Do not collapse:

```math
\boxed{
\text{constructor independence}
\neq
\text{defeater independence}
\neq
\text{gold independence}.
}
```

### 3.1 Constructor independence

The prospective research history must be constituted by an external constructor or curator who is not required to preserve the current internal generator's topology, mechanism inventory, scenario grammar, or expected correction classes.

The constructor must be free to surprise the current research program.

### 3.2 Defeater independence

The later defeater should not be hand-selected by the hypothesis authors merely to expose a distinction already expected to favor one memory policy.

A test may use the same external party for history construction and defeater construction if that relationship is declared and audited, but it must not be represented as stronger independence than it actually has.

Preferred structure:

```text
independent history constructor
        ↓
frozen history
        ↓
independent or separately governed defeater selector
```

### 3.3 Gold independence

Private gold must be derived from the externally constituted world and declared warrant semantics, not from the learner's own correction graph, explanation, or bookkeeping.

```math
\boxed{
G^\star_{\rm warrant}\perp G_{\rm learner}
}
```

is therefore an informational and causal requirement, not merely a requirement to place gold in a different file.

---

## 4. External package

A contribution should provide an artifact bundle structurally equivalent to:

```text
external-case/
├── constructor_provenance.md
├── frozen_history.json
├── learner_view.json
├── defeaters/
│   ├── d1.json
│   ├── d2.json
│   └── ...
└── private/
    ├── warrant_gold.json
    └── scoring_manifest.json
```

Equivalent layouts are allowed if they preserve the same causal and informational separation.

### `constructor_provenance.md`

Must document enough information to audit constructor independence, author/curator roles, construction timing, known contact with the hypothesis authors, and any constraints inherited from this repository.

### `frozen_history.json`

Must contain the exact prospective history before the selected future defeater and be cryptographically or otherwise immutably bound before defeat.

### `learner_view.json`

Must contain sufficient but non-answer-shaped evidence for the learner to make the required correction commitment.

### `defeaters/`

Must contain post-freeze evidence events. Defeater provenance and selection procedure must be auditable.

### `private/warrant_gold.json`

Must remain unavailable to the learner before prediction freeze.

### `private/scoring_manifest.json`

Must define the result classes, required fields, comparison rules, and treatment of partial correctness before learner output is inspected.

---

## 5. Two disclosure times

Construction provenance must be auditable without leaking the hidden family to the learner.

Therefore distinguish:

```math
\boxed{
\text{pre-run audit metadata}
\neq
\text{post-run scientific disclosure}.
}
```

### Pre-run audit metadata

May establish:

```text
who constructed the history
who selected or generated defeaters
when each artifact was frozen
what independence relationships hold
what information is withheld from the learner
what scoring contract is frozen
```

It should not reveal generator logic, scenario-family labels, private warrant topology, or mechanism-specific clues that make the correction class answer-shaped.

### Post-run scientific disclosure

After learner predictions are frozen, the constructor may disclose the fuller construction procedure, hidden mechanisms, gold derivation, and audit trail needed for scientific inspection and replication.

The timing of disclosure is part of the experiment's provenance.

---

## 6. Learner-facing sufficiency

The learner must not inherit the answer space.

The benchmark must not erase the information required to discover the answer.

Therefore:

```math
\boxed{
\textbf{the learner must discover the authority consequence from evidence that is sufficient but not answer-shaped.}
}
```

The full learner-facing interface must satisfy an identifiability audit.

If:

```math
O(W_a)=O(W_b)
```

while:

```math
A_d^\star(W_a)\neq A_d^\star(W_b),
```

then:

```math
\boxed{
\text{BENCHMARK NON-IDENTIFIABILITY}.
}
```

Such a pair cannot be scored as learner failure.

---

## 7. Required L2 learner output

Do not require chain-of-thought.

Require a typed evidential commitment:

```math
\boxed{
\text{L2 output}
=
\langle
\text{localize},
\text{account},
\text{preserve}
\rangle.
}
```

### `localize`

What did the new evidence directly defeat?

At minimum:

```text
defeater locus
kind of defeat
referenced evidential object(s)
```

### `account`

What epistemic authority consequently disappeared, narrowed, or requires recomputation?

At minimum:

```text
affected authority instances / paths
removed or narrowed authority
claims requiring reopening or recomputation
```

### `preserve`

What remains warranted independently?

At minimum:

```text
retained claims
surviving warrant references
historical transformations that remain realized
```

The output should contain inspectable references to the learner-facing evidential objects or warrant-relevant relations the learner claims justify its correction.

---

## 8. Action accuracy is not rationale accuracy

Score separately:

```math
\boxed{
\text{action accuracy}
\neq
\text{warrant-reference accuracy}
\neq
\text{warrant-reference completeness}.
}
```

A learner may choose the correct action for the wrong reason.

Example:

```text
RETAIN(K3)
```

is not a successful warrant reconstruction merely because the action matches gold if the learner cites a nonexistent or defeated independent route.

Likewise, a learner may cite one genuine surviving route while omitting another.

Therefore allow states such as:

```math
\boxed{
ActionCorrect=1,
\qquad
RationaleFaithful=1,
\qquad
RationaleComplete<1.
}
```

The scoring manifest must preserve these distinctions instead of collapsing them into a single prose-grade or binary score.

---

## 9. Paired-world requirements

The admitted contribution must contain or support cases that attack superficial anomaly classification in both directions.

### Same-looking evidence, different corrections

```math
E_a\approx_{\rm surface}E_b
```

while:

```math
\boxed{
Correction(E_a)\neq Correction(E_b).
}
```

This defeats policies such as:

```text
same anomaly class → same correction
contradiction → reopen nearest claim
```

### Different-looking evidence, same correction

```math
E_c\not\approx_{\rm surface}E_d
```

while:

```math
\boxed{
Correction(E_c)=Correction(E_d).
}
```

This prevents superficial appearance differences from becoming a proxy for correction class.

The relevant capability is sensitivity to authority structure, not anomaly vocabulary.

---

## 10. Required nulls and hypothesis-losing worlds

An external contribution must be allowed to produce worlds where richer lineage does not help.

Examples of legitimate outcomes include:

```math
\boxed{A=B=C}
```

when all three representations preserve everything needed for correction.

Or:

```math
\boxed{B=C>A}
```

when source provenance is sufficient and explicit transformation lineage adds no measurable benefit.

The family should also include real anomalies or failures that carry no epistemic-authority consequence:

```math
\boxed{
\text{real anomaly}
+
\text{no warrant dependence}
\rightarrow
\text{retain epistemic authority}.
}
```

This protects:

```math
\boxed{
\text{feedback sensitivity}
\neq
\text{revision sensitivity}.
}
```

The benchmark output space must not secretly be `C wins`.

---

## 11. Result vector

Do not collapse the comparison into a single winner score before the first admitted result.

Retain at least the current vector:

```math
\boxed{
\mathcal M=
\langle
R_W,P_W,I_P,S_A,H_P,R_C,C_R,T_R
\rangle
}
```

with:

```text
R_W   affected-warrant recall
P_W   affected-warrant precision
I_P   independent-support preservation
S_A   authority-scope accuracy
H_P   historical-preservation accuracy
R_C   recomputation correctness
C_R   repair-cost measure
T_R   repair-latency/work measure
```

The admitted scoring manifest may refine the operational definitions, but any refinements must be frozen before learner outcomes are inspected.

Action, rationale fidelity, and rationale completeness must remain separately inspectable.

---

## 12. Admission states

Preserve:

```math
\boxed{
\text{ADMISSION}
\neq
\text{RUN}
\neq
\text{RESULT}
\neq
\text{INTERPRETATION}.
}
```

The relevant states are:

```text
UNADMITTED
ADMITTED / NOT RUN
ADMITTED + FAIL
ADMITTED + PASS
BENCHMARK NON-IDENTIFIABLE
INVALIDATED / CONTAMINATED
```

Passing this external-contribution contract means only that the contribution may proceed to the existing L2 admission audit.

It does **not** itself mean L2 is admitted.

The existing `frontier/benchmark_nucleus/l2_constructor/ADMISSION_GATE.md` remains the binding L2 admission contract.

---

## 13. Claim ceiling

A positive admitted comparison may support only a scoped statement such as:

> Under this admitted external prospective history and defeater family, the specified memory representation supported better selective correction on the reported metric dimensions than the compared cheaper representation(s).

It does **not** automatically establish:

```text
general superiority of policy C
universal necessity of transformation lineage
safe epistemic compounding
corrigibility debt
Level-3 invention
general corrigibility
AG/1 enlargement
L3 correction locality under scale
```

A result such as:

```math
A=B=C
```

is a legitimate negative result against the incremental value of richer lineage under that scope.

A result such as:

```math
B\approx C>A
```

is evidence that source provenance may be sufficient under that scope.

A result in which `C` improves correction but imposes unacceptable operational cost is a tradeoff result, not an unqualified win.

---

## 14. External-contribution admission checklist

Before an external case may be treated as a candidate scientific test, verify all of the following:

1. **External constructor provenance is documented.**
2. **The prospective history was frozen before the selected future defeater.**
3. **Constructor independence and defeater independence are separately described rather than collapsed.**
4. **Private gold is independent of the learner's own bookkeeping.**
5. **Pre-run audit metadata does not expose hidden family logic or answer-shaped mechanism labels.**
6. **Post-run disclosure is sufficient for scientific audit.**
7. **Learner-facing evidence is sufficient for every gold-relevant distinction.**
8. **Any benchmark-non-identifiable pair is rejected before learner scoring.**
9. **The learner produces a prospectively frozen typed `localize/account/preserve` commitment.**
10. **Warrant references are inspectable without requiring chain-of-thought.**
11. **Action accuracy, rationale fidelity, and rationale completeness are separately scored.**
12. **The family contains or supports surface-similar / consequence-different cases.**
13. **The family contains or supports surface-different / consequence-equivalent cases.**
14. **Real nulls exist where no epistemic authority should change.**
15. **Worlds where `A=B=C` or `B=C>A` are not excluded by design.**
16. **The metric vector and scoring rules are frozen before learner outcome inspection.**
17. **The contribution does not silently authorize L3 scaling.**
18. **The existing L2 admission gate is still applied after this contract is cleared.**

If these conditions are not satisfied, the contribution may still be useful engineering pressure, but it does not carry the authority of an external admitted learner test.

---

## 15. Current program state

This contract changes no current evidential status.

```text
L0/L1 = instrument established
L2     = prospective scaffolded, UNADMITTED
L3     = BLOCKED
```

The internal prospective generator remains an engineering instrument.

No internally authored refinement can satisfy external-constructor independence by itself.

The next authority-bearing transition requires a genuinely external contribution that clears this contract and then clears the existing L2 admission gate.

---

## 16. Freeze rule

This contract is a methodological fossil.

It may be challenged by:

```text
an external constructor showing that a requirement is insufficient;
an external constructor showing that a requirement is impossible or self-defeating;
a benchmark-identifiability failure;
a leakage path not covered here;
an independently observed result that forces revision of the scoring distinctions.
```

It should not be expanded merely because additional ontology, mechanism labels, or toy cases are easy to invent.

```math
\boxed{
\textbf{Protect the causal cuts; do not inflate the benchmark.}
}
```

The stable experimental bookends remain:

```math
\boxed{
\textbf{Don't let the learner steal the answer.}
}
```

```math
\boxed{
\textbf{Don't make the answer undiscoverable.}
}
```

And the external-contribution principle is:

```math
\boxed{
\textbf{Let someone outside the hypothesis-bearing loop construct the world that earns or defeats the next increment of authority.}
}
```
