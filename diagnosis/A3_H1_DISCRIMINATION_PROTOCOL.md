# H1 Discrimination Protocol — Frozen Before New Diagnostic Evidence

**Status:** FROZEN DIAGNOSTIC PROTOCOL  
**Purpose:** discriminate the A3 primary diagnosis from its unresolved cross-verse alternatives without modifying `D1`, `P3`, or `A3`  
**Decoder:** frozen `D1`  
**Next diagnostic passage:** Genesis 5  
**Why not Genesis 4:** Genesis 4 source text was already surfaced during the earlier Genesis source inspection, so it is not treated as clean unseen diagnostic evidence.

The current diagnostic state is:

```math
\boxed{
D_1^F\rightarrow P_3^F\rightarrow A_3^F\rightarrow H_1+(R_1,R_2)
}
```

No decoder repair is permitted in this protocol.

The next operation is a discrimination test, not a `D2` construction.

---

## 1. Frozen hypotheses

### H1 — local explicit-relation retention incompleteness

```math
\boxed{
\text{D1 has a strong admission invariant but a weak completeness invariant.}
}
```

Operational prediction:

```text
D1 will sometimes recover the main semantic object/event while omitting a directly expressed local predicate, connective, modifier, source edge, temporal edge, or purpose edge that D1 is already capable of representing.
```

### R1 — chapter-scale form of the same completeness deficit

```math
\boxed{
\text{cross-verse misses are the nonlocal extension of the same retention-completeness weakness.}
}
```

Operational prediction:

```text
local relation retention and cross-verse correspondence retention will fail together rather than separating sharply by discourse distance.
```

### R2 — distinct locality-bounded comparison deficit

```math
\boxed{
\text{local extraction can be substantially complete while cross-verse correspondence remains selectively under-recovered.}
}
```

Operational prediction:

```text
cross-verse correspondence misses will remain materially higher than local explicit-relation misses.
```

---

## 2. Frozen diagnostic passage

Genesis 5 is selected before its text is fetched or parsed in this diagnostic phase.

It is used only as new evidence about the frozen decoder and the frozen diagnostic hypotheses.

```math
\boxed{
D_1^F + T_{\mathrm{GEN.5}}^F\rightarrow P_5^F\rightarrow A_5^{\mathrm{diag}}
}
```

Genesis 5 may change confidence in `H1`, `R1`, or `R2`.

It may not change `D1` during this test.

---

## 3. Two separately scored opportunity classes

The diagnostic audit must keep local and nonlocal coverage separate.

### L — local explicit-relation opportunities

A local opportunity is a directly expressed relation-bearing unit recoverable without leaving the verse or immediate syntactic construction, including where present:

```text
predicate attached to an already represented entity/event
explicit discourse/reason/result connective
speaker/addressee or source/action attribution
temporal/subordinate relation
purpose/function edge
material/provenance edge
explicit modifier that changes the represented relation
```

The scorer asks:

```math
\boxed{
\text{Was the directly expressed local relation preserved at the weakest sufficient type?}
}
```

Each opportunity is scored:

```text
L-RETAINED
L-MISSED
L-FALSE-PROMOTION
```

### X — cross-verse correspondence opportunities

A cross-verse opportunity exists only when two or more separated verses directly instantiate the same recoverable proposition, relation template, named-role relation, or repeated textual operation with enough lexical/structural identity that correspondence can be recorded without causal, psychological, symbolic, or theological inference.

Examples of admissible correspondence form:

```text
same proposition/content recurs
same explicit relation template recurs
same named role/predicate recurs
same textual operation repeats across separated verses
```

A merely thematic resemblance is not an X opportunity.

The scorer asks:

```math
\boxed{
\text{Did P5 preserve the recurrence/correspondence as chapter-level recoverable structure?}
}
```

Each opportunity is scored:

```text
X-RETAINED
X-MISSED
X-FALSE-PROMOTION
```

---

## 4. Parse-before-score sequence

The required causal order is:

```text
1. Freeze this protocol.
2. Constitute and fingerprint the canonical GEN.5 slice.
3. Parse Genesis 5 using frozen D1 only.
4. Freeze P5.
5. Only after P5 is frozen, enumerate L and X opportunities from the canonical slice under the definitions above.
6. Score P5 against those opportunities.
7. Freeze the diagnostic audit.
8. Update confidence in H1/R1/R2 only after scoring.
```

Forbidden sequence:

```text
read Genesis 5
→ notice a useful discriminator
→ alter the opportunity definitions
→ score
```

---

## 5. Minimum evidence gate

A discrimination result is considered informative only if Genesis 5 supplies at least:

```text
n_L >= 6 local opportunities
n_X >= 6 cross-verse opportunities
```

If either class has fewer than six opportunities:

```math
\boxed{\text{result}=\mathrm{INSUFFICIENT\ DISCRIMINATING\ EVIDENCE}}
```

No hypothesis is rejected merely because the selected chapter lacks the required opportunity structure.

---

## 6. Frozen outcome map

Let:

```math
m_L=\text{number of L-MISSED items}
```

```math
m_X=\text{number of X-MISSED items}
```

provided the minimum evidence gate is satisfied.

The diagnostic outcome is classified before seeing Genesis 5 as follows:

### O1 — supports R1 / shared completeness deficit

```text
m_L >= 2
and
m_X >= 2
```

with no sharp separation in which one class is nearly complete and the other repeatedly fails.

Interpretation:

```math
\boxed{\text{local and nonlocal retention weaknesses co-occur}}
```

### O2 — supports R2 / distinct locality deficit

```text
m_L <= 1
and
m_X >= 2
```

Interpretation:

```math
\boxed{\text{local retention is substantially intact while cross-verse comparison selectively fails}}
```

### O3 — supports H1 as predominantly local; weakens both R1 and R2 as stable explanations of M4/M9

```text
m_L >= 2
and
m_X <= 1
```

Interpretation:

```math
\boxed{\text{local retention weakness replicates without a corresponding nonlocal deficit}}
```

### O4 — H1 fails to replicate on this passage

```text
m_L <= 1
and
m_X <= 1
```

Interpretation:

```math
\boxed{\text{the A3 failure pattern does not reproduce under this diagnostic sample}}
```

This does not erase A3. It lowers confidence that H1 describes a stable decoder property rather than a passage/run-specific pattern.

### Mixed/ambiguous outcome

If counts satisfy O1 numerically but one class is nearly exhaustive while the other only barely crosses the threshold, the result must be reported as `MIXED` rather than forced into R1.

No post-hoc numerical threshold may be introduced to turn a mixed result into a preferred hypothesis.

---

## 7. Precision remains separately monitored

Although this is a coverage-discrimination experiment, unsupported promotion remains independently scored.

```math
\boxed{\text{coverage evidence must not be purchased by weakening admission discipline}}
```

Any `L-FALSE-PROMOTION` or `X-FALSE-PROMOTION` is recorded separately and cannot be counted as retained structure.

Because `D1` is unchanged, this is a replication check on the original precision boundary, not a repair tradeoff experiment.

---

## 8. What this protocol cannot establish

This test does not ask:

```text
how D2 should work
which implementation would increase completeness
whether a repair would preserve precision
```

It asks only:

```math
\boxed{
\textbf{Is the A3 under-recovery best explained as a general completeness deficit, a local retention deficit, or a distinct locality-bounded comparison deficit?}
}
```

---

## 9. Freeze statement

This protocol is frozen before Genesis 5 is fetched or parsed in the diagnostic phase.

No opportunity definition, minimum-evidence gate, or outcome class may be revised after Genesis 5 exposure for the purpose of improving hypothesis fit.

The governing boundary remains:

```math
\boxed{
\textbf{diagnose before repair}
}
```
