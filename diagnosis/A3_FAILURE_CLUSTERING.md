# A3 Failure Clustering — Diagnostic Hypothesis Space

**Status:** DIAGNOSTIC ARTIFACT / NO REPAIR  
**Inputs:** frozen `D1`, frozen `P3`, frozen `A3`  
**Purpose:** explain the held-out error distribution before any decoder modification

The phase boundary is:

```math
\boxed{
D_1^F
\rightarrow
P_3^F
\rightarrow
A_3^F
\;\Big|\;
\text{DIAGNOSIS}
}
```

This artifact treats all three upstream objects as immutable.

It does not rewrite the held-out parse, rescore the audit, or specify a repair.

The governing question is:

```math
\boxed{
\textbf{What common latent decoder deficiency explains the largest coherent subset of the frozen failures?}
}
```

---

## 1. Frozen diagnostic target

The A3 held-out result is:

```text
FALSE PROMOTION:       1
MISSED STRUCTURE:      12
NEW FAILURE MODE:      0
explicit OPEN items:   49
correct OPEN items:    49
```

The error distribution is therefore strongly asymmetric:

```math
\boxed{
\text{unsupported promotion}
\ll
\text{missed recoverable structure}
}
```

The 12 frozen misses are:

```text
M1   GEN.3.1          maker relation omitted
M2   GEN.3.5          explicit “For” edge not preserved
M3   GEN.3.6          explicit “when” relation weakened to ordering
M4   GEN.3.5 ↔ 3.7    prospective/result correspondence omitted
M5   GEN.3.8          walking predicate omitted
M6   GEN.3.8          temporal setting omitted
M7   GEN.3.16         speaker/action attribution underrepresented
M8   GEN.3.19         second explicit “for” relation omitted
M9   GEN.3.5 ↔ 3.22   “knowing good and evil” correspondence omitted
M10  GEN.3.23         purpose relation weakened to assigned activity
M11  GEN.3.24         flaming-sword operation omitted
M12  GEN.3.24         explicit “So” discourse/result connective omitted
```

The single false promotion is:

```text
FP1  GEN.3.8          locative edge attached to the heard voice rather than
                       preserving the walking construction
```

---

## 2. Diagnostic criterion

Candidate hypotheses are compared on three dimensions:

```math
\boxed{
\text{failure coverage}
+
\text{mechanism coherence}
+
\text{complexity cost}
}
```

where:

```text
failure coverage
  = how many frozen findings are explained by the same generating property
    without changing their audit classification

mechanism coherence
  = whether the hypothesis explains why these particular errors cluster
    rather than merely redescribing them

complexity cost
  = how much new explanatory machinery must be assumed
```

The preferred diagnosis is the lowest-complexity hypothesis that explains a substantial coherent subset:

```math
\boxed{
H^*
=
\arg\min_H \operatorname{complexity}(H)
\quad
\text{s.t.}
\quad
H\text{ explains a substantial coherent subset of }A_3^F
}
```

No hypothesis is permitted to rewrite the frozen failures in order to improve its apparent fit.

---

## 3. Candidate hypotheses

### H1 — Explicit-relation retention incompleteness

```math
\boxed{
\text{D1 constrains admission strength better than it constrains extraction completeness.}
}
```

More specifically:

```math
\boxed{
\text{core semantic object recovered}
\not\Rightarrow
\text{all directly attached predicates/connectives/edges retained}
}
```

Under this hypothesis, the decoder is good at answering:

```text
“Is this stronger formal claim licensed?”
```

but less completely specified for:

```text
“Have all directly expressed relation-bearing structures attached to this
recognized object been preserved before compression stops?”
```

This predicts selective loss of:

```text
secondary predicates
explicit connectives
edge labels
speaker/action source edges
temporal modifiers
purpose edges
```

while leaving the main semantic object intact.

#### Direct coverage

H1 directly explains:

```text
M1   maker edge dropped while comparison object retained
M2   “For” token noticed but explanatory edge dropped
M3   “when” relation compressed into generic before/after ordering
M5   walking predicate dropped
M6   temporal modifier dropped
M7   addressee/content retained while speaker/action source edge dropped
M8   proposition retained while second “for” edge dropped
M10  activity retained while explicit purpose relation weakened
M11  sword object retained while its turning predicate dropped
M12  drive-out action retained while “So” discourse edge dropped
```

Therefore:

```math
\boxed{
\operatorname{coverage}(H_1)=10/12\ \text{misses directly}
}
```

H1 also gives a coherent account of the single false promotion.

In GEN.3.8, dropping the directly represented `walking` predicate leaves the locative phrase available to be absorbed into the surviving `voice` representation:

```text
walking predicate omitted
        ↓
locative attachment structure degraded
        ↓
“voice ... in garden”
```

Thus FP1 may be a downstream consequence of the same retention failure rather than an independent tendency toward aggressive inference.

#### Counterevidence / limitation

H1 does **not** directly explain the two chapter-level correspondence misses:

```text
M4   GEN.3.5 ↔ GEN.3.7
M9   GEN.3.5 ↔ GEN.3.22
```

unless “retention completeness” is broadened from local explicit edges to chapter-level recurrence/correspondence scanning.

That broadening is not assumed here merely to obtain 12/12 coverage.

---

### H2 — General lossy-compression / salience bias

```math
\boxed{
\text{P3 preferentially preserves salient semantic content and compresses lower-salience detail.}
}
```

This hypothesis can superficially account for many of the same cases as H1:

```text
main event retained
secondary relation omitted
```

Examples include the omitted walking predicate, temporal setting, second `for`, sword motion, and maker relation.

However H2 is less discriminating.

It does not explain why the omitted material clusters specifically around **relation-bearing predicates/connectives** rather than arbitrary low-salience lexical content.

It is therefore closer to a restatement of the observed compression than a mechanism for the particular error distribution.

---

### H3 — Locality-bounded structural comparison

```math
\boxed{
\text{the decoder is stronger at local extraction than at linking propositions across discourse distance.}
}
```

This predicts missed relations when the evidence requires preserving a correspondence between separated propositions rather than extracting a relation locally.

It directly fits:

```text
M4   GEN.3.5 ↔ GEN.3.7 prospective/result correspondence
M9   GEN.3.5 ↔ GEN.3.22 “knowing good and evil” correspondence
```

It also has partial relevance to discourse connectives whose semantic target lies in preceding discourse:

```text
M2   “For” in GEN.3.5 relates to the preceding assertion
M12  “So” in GEN.3.24 relates to the preceding sequence
```

But locality alone cannot explain clearly intra-verse losses such as:

```text
M1, M3, M5, M6, M7, M8, M10, M11
```

H3 is therefore a plausible **secondary** generating deficiency, not the best single explanation of the complete error pattern.

---

### H4 — Conservatism overshoot

```math
\boxed{
\text{the anti-promotion rule causes the decoder to suppress structure whenever relation strength is uncertain.}
}
```

This would explain missed structure as a side effect of excessive epistemic restraint.

The frozen evidence argues strongly against H4 as the dominant cause.

A3 found:

```math
\boxed{49/49\ \text{explicit OPENs correctly abstained}}
```

and P3 repeatedly preserved explicit reason, purpose, provenance, speaker/addressee, action, state, and prospective relations when they were directly supplied.

The misses therefore do not look like a general refusal to represent relations.

They look selective.

---

### H5 — Missing relation ontology

```math
\boxed{
\text{D1 lacks formal types for the relation families that P3 missed.}
}
```

If true, one would expect systematic absence of the same relation family throughout P3.

The frozen parse provides counterexamples.

P3 successfully preserves, among other things:

```text
explicit “because” relations
explicit “Therefore” relation
speaker → addressee edges
purpose relations
material-provenance relations
placement / transfer relations
performed predicates
```

Several missed cases therefore belong to relation families already representable under frozen D1 and already used successfully elsewhere in P3.

The failure is consequently better described as **inconsistent retention of available structure** than inability to type that structure at all.

---

## 4. Comparative score

Scale:

```text
mechanism coherence: 0–3, higher is better
complexity cost:      0–3, lower is better
```

`failure coverage` counts the 12 frozen missed-structure findings directly explained without broadening the hypothesis after inspection.

| Hypothesis | Failure coverage | Mechanism coherence | Complexity cost | Diagnostic status |
|---|---:|---:|---:|---|
| H1 — explicit-relation retention incompleteness | 10/12 | 3 | 1 | strongest primary hypothesis |
| H2 — general lossy-compression / salience bias | 10/12 | 2 | 1 | plausible but underspecified |
| H3 — locality-bounded structural comparison | 2/12 direct; 2 additional partial | 3 | 1 | strong secondary hypothesis |
| H4 — conservatism overshoot | low | 1 | 1 | disfavored by 49/49 correct OPENs |
| H5 — missing relation ontology | low after counterexamples | 1 | 3 | disfavored by successful same-family relations |

---

## 5. Discrimination by internal counterexamples

The most important discriminator is that P3 sometimes **does** preserve the exact kinds of structures that it misses elsewhere.

Examples from the frozen audit include:

```text
GEN.3.10  explicit “because” relation preserved
GEN.3.14  explicit “Because” relation preserved
GEN.3.17  explicit reason structure preserved
GEN.3.19  one “for” reason relation preserved
GEN.3.23  explicit “Therefore” relation preserved
GEN.3.24  explicit purpose relation preserved
```

Therefore the observed failure cannot be compressed to:

```math
\boxed{
\text{D1 does not know how to represent explicit relations}
}
```

A better fit is:

```math
\boxed{
\text{D1 permits these relations but does not enforce complete preservation of every directly recoverable instance.}
}
```

This distinction is central.

It separates **representation capacity** from **coverage discipline**.

---

## 6. Primary minimal diagnosis

The strongest current diagnosis is H1:

```math
\boxed{
\textbf{D1 has a strong admission invariant but a weak completeness invariant.}
}
```

Equivalently:

```math
\boxed{
\operatorname{constraint}_{\text{promotion}}
>
\operatorname{constraint}_{\text{retention completeness}}
}
```

The decoder reliably asks whether a candidate formal strengthening is earned, but it does not comparably require that all directly recoverable relation-bearing material survive structural compression.

This explains the characteristic pattern:

```text
semantic object survives
+
main event survives
+
strong unsupported inference is rejected
+
secondary explicit edge/predicate sometimes disappears
```

It also offers a parsimonious explanation of FP1: once the walking predicate was dropped, the locative material was attached to the surviving object rather than preserved on its original edge.

The primary diagnosis therefore accounts for:

```math
\boxed{
10/12\ \text{misses directly}
+
1/1\ \text{false promotion plausibly downstream}
}
```

without requiring a larger semantic ontology.

---

## 7. Residual uncertainty — the two cross-verse misses

M4 and M9 should not be forced into H1 simply to maximize numerical coverage.

They share a different property:

```text
both require recognizing correspondence between propositions separated in the chapter
```

Two live explanations remain:

```text
R1 — they are the chapter-scale form of the same completeness deficit:
     the decoder lacks a completeness check over previously represented propositions.

R2 — they arise from a distinct locality bias:
     local verse extraction is strong, but cross-verse correspondence is not routinely searched.
```

The present evidence does not discriminate these two explanations strongly enough to collapse them.

Therefore:

```math
\boxed{
H_1\text{ is the primary diagnosis}
\quad+
H_3\text{ remains a live secondary hypothesis for M4/M9.}
}
```

---

## 8. Falsifiers / discrimination criteria

This diagnosis remains reopenable.

Evidence against H1 would include a future frozen evaluation in which:

```text
all explicit local relation-bearing predicates/connectives are retained reliably,
but under-recovery remains concentrated in semantic categories unrelated to edge retention.
```

Evidence supporting H1 would be a recurring pattern in which:

```text
known relation types are represented correctly in some passages
but individual explicit instances are selectively omitted after the main semantic object has been captured.
```

Evidence distinguishing R1 from R2 would require comparing:

```text
local relation completeness
versus
cross-proposition / cross-verse correspondence completeness
```

under an independently frozen evaluation.

No such additional evidence is manufactured in this artifact.

---

## 9. Diagnostic conclusion

The frozen held-out result does **not** primarily support:

```text
D1 is too permissive
D1 is globally too conservative
D1 needs a much larger ontology
```

The minimal current explanation is:

```math
\boxed{
\textbf{D1 preserves semantic objects more reliably than it preserves the complete explicit relational structure connecting and qualifying those objects.}
}
```

or, more compactly:

```math
\boxed{
\textbf{admission discipline > retention completeness}
}
```

This diagnosis explains the largest coherent subset of the frozen A3 failures at low explanatory complexity while preserving a separate live hypothesis for the two cross-verse correspondence misses.

The artifact stops here.

```math
\boxed{
\textbf{explain the error distribution before repairing the decoder}
}
```
