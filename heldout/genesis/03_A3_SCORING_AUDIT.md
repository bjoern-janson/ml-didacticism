# Genesis 3 — A3 Held-Out Scoring Audit

**Status:** FROZEN SCORING AUDIT  
**Audit target:** frozen `P3` produced by frozen `D1` on frozen Genesis 3 evidence  
**Decoder revision:** NOT PERMITTED IN THIS ARTIFACT  
**Parse revision:** NOT PERMITTED IN THIS ARTIFACT

The audited causal chain is:

```math
\boxed{
D_1^F + T_{\mathrm{GEN.3}}^F
\rightarrow
P_3^F
\rightarrow
A_3
}
```

This document classifies the held-out output. It does **not** rewrite `P3`, revise `D1`, or propose `D2`.

## 1. Frozen inputs

Decoder:

```text
artifact:   decoder/D1.md
git blob:   4c1a36da5f5e8b59606a1d2fdbdda010c4dbe62f
SHA-256:    b5b50e58b43602de61ca4c35fe38fbc45518ea46ddcaaed1f36cb6e31f8ff12a
freeze:     c66414fb33366fcf213410b3a0789c032be264c2
```

Held-out parse:

```text
artifact:   heldout/genesis/03_P3_RAW_PARSE.md
git blob:   73ac3c8b5e2474a6fb1ee16b6ffedd8e6a942b60
SHA-256:    e9c2c0fadc0dc47bb6e2f2ff61dfde645b632f14f81e96be4ef46c1ea56c232a
creation:   f1a5c93f8013173bf519cbe2395b057374caf836
```

Evidence:

```text
source corpus:             corpus/kjv.jsonl
source corpus SHA-256:     b4a44c22899b0669f1d504c65a89bee2ac2dd4b08e01c2f012814f348a6ba2dc
held-out passage:          GEN.3.1 → GEN.3.24
canonical slice SHA-256:   e9fa5eb2a0ef5713104559a2dbadcbdf93bd3f288fc0f7f8d9a5eaac614a64c1
verse count:               24
```

## 2. Scoring rubric

The audit classifies claim/abstention units rather than assigning one grade per verse.

Audit unit:

```math
\boxed{
\text{claim/abstention}
\times
\text{canonical evidence}
\times
\text{applicable frozen D1 rule}
}
```

Classes:

```text
SURVIVED
FALSE PROMOTION
MISSED STRUCTURE
CORRECT ABSTENTION
NEW FAILURE MODE
```

Definitions:

```text
SURVIVED
  P3 recovered textually supported structure at an appropriate strength.

FALSE PROMOTION
  P3 committed to a relation stronger than the canonical evidence licenses.

MISSED STRUCTURE
  Canonical evidence supplied structure that frozen D1 should have admitted but P3 did not preserve.

CORRECT ABSTENTION
  P3 left a stronger classification OPEN because the required textual bridge was absent.

NEW FAILURE MODE
  A defect observed under the fixed audit criteria that cannot be expressed by the existing D1 failure taxonomy.
```

`OPEN` is not automatically a success. An `OPEN` is positive only where stronger structure is not already recoverable under D1.

The rubric was fixed in the experimental session before scoring. No separate pre-scoring rubric artifact was committed to this repository, so this audit does not claim a repository-level precommit hash for the rubric.

## 3. Aggregate held-out result

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
49/49\ \text{explicit OPENs}
=\text{CORRECT ABSTENTION}
}
```

and the held-out error distribution is strongly asymmetric:

```math
\boxed{
\text{unsupported promotion}
\ll
\text{missed recoverable structure}
}
```

The main result is:

```math
\boxed{
\text{D1 generalized its epistemic boundary; its remaining failure is predominantly structural coverage.}
}
```

## 4. False promotion

### FP1 — GEN.3.8 — locative edge attached too strongly

Canonical evidence reports:

```text
heard the voice of the LORD God walking in the garden in the cool of the day
```

P3 records:

```text
Adam + wife → heard → voice of LORD God in garden
```

while omitting the `walking` predicate.

Applicable frozen rules:

```text
D2 weakest sufficient type
D3 no unsupported edge strengthening
D6 preserve relational edge type
```

The locative relation is attached by P3 to the heard voice rather than preserving the directly represented walking construction.

Classification:

```text
FALSE PROMOTION
```

This is a local edge-attachment error, not a broad collapse of D1's conservatism.

## 5. Missed recoverable structure

### M1 — GEN.3.1 — maker relation omitted

The verse supplies the comparison class together with the relation that the LORD God had made the beasts of the field.

P3 preserves the comparison but not:

```text
LORD God → made → comparison class
```

Classification: **MISSED STRUCTURE**.

### M2 — GEN.3.5 — explicit `For` edge not preserved

P3 detects the `For` connective but does not preserve the explanatory/reason relation joining the serpent's preceding assertion to the following clause.

Classification: **MISSED STRUCTURE**.

### M3 — GEN.3.6 — explicit `when` relation weakened to generic ordering

The canonical text directly supplies a `when` relation joining the woman's seeing/evaluation to the following action sequence.

P3 records only that the evaluation report occurs before the actions.

Classification: **MISSED STRUCTURE**.

### M4 — GEN.3.5 ↔ GEN.3.7 — prospective/result correspondence omitted

GEN.3.5 contains the prospective content:

```text
your eyes shall be opened
```

GEN.3.7 later reports:

```text
the eyes of them both were opened
```

A neutral textual correspondence can be recorded without promoting it to causal mechanism, verified belief, or theological interpretation.

P3 explicitly declines the comparison.

Classification: **MISSED STRUCTURE**.

### M5 — GEN.3.8 — walking predicate omitted

The verse directly supplies the walking construction associated with the LORD God in the garden.

P3 does not preserve the walking operation.

Classification: **MISSED STRUCTURE**.

### M6 — GEN.3.8 — temporal setting omitted

The verse directly supplies:

```text
in the cool of the day
```

P3 does not preserve this temporal relation.

Classification: **MISSED STRUCTURE**.

### M7 — GEN.3.16 — speaker/action attribution underrepresented

The verse continues the LORD God speech and contains:

```text
Unto the woman he said, I will greatly multiply ...
```

P3 records the woman as addressee and the prospective statements but drops the speaker/actor edge behind the first-person future action.

Classification: **MISSED STRUCTURE**.

### M8 — GEN.3.19 — second explicit `for` relation omitted

The verse contains two distinct `for` clauses:

```text
for out of it wast thou taken
for dust thou art
```

P3 preserves the first reason relation and separately records `dust thou art`, but does not preserve the second `for` as its own explanatory/reason edge.

Classification: **MISSED STRUCTURE**.

### M9 — GEN.3.5 ↔ GEN.3.22 — `knowing good and evil` correspondence omitted

GEN.3.5 contains:

```text
knowing good and evil
```

GEN.3.22 later contains:

```text
to know good and evil
```

The identity or semantics of `gods/us` can remain OPEN while the recurring proposition is still textually recoverable.

Classification: **MISSED STRUCTURE**.

### M10 — GEN.3.23 — purpose relation weakened to assigned activity

The text says the LORD God sent the man forth from Eden:

```text
to till the ground
```

P3 records an `assigned activity after transfer`, but D1 already admits explicit purpose relations. The `to` relation itself is recoverable.

Classification: **MISSED STRUCTURE**.

### M11 — GEN.3.24 — flaming-sword operation omitted

The verse directly reports a flaming sword:

```text
which turned every way
```

P3 records placement but omits this predicate.

Classification: **MISSED STRUCTURE**.

### M12 — GEN.3.24 — explicit `So` discourse/result connective omitted

The verse begins:

```text
So he drove out the man
```

P3 captures the drive-out action but does not preserve the explicit discourse/result connective.

Classification: **MISSED STRUCTURE**.

## 6. Correct abstentions

P3 contains 49 explicit `OPEN` items.

The audit found no case in which one of those explicit abstentions required promotion under frozen D1.

They correctly preserve evidence boundaries for classes including:

```text
speaker intent
speaker belief
truth status
physical executability
complete action spaces
complete reachable-future spaces
unspecified mechanisms
causal inference from narrative sequence
responsibility / exoneration judgments
symbolic or theological extensions
unresolved referents
normative versus descriptive status where the wording does not settle it
```

Classification:

```math
\boxed{
49/49=\text{CORRECT ABSTENTION}
}
```

This is the strongest held-out evidence that D1's learned restraint generalized rather than collapsing into either unsupported promotion or indiscriminate refusal to parse.

## 7. New failure modes

No new failure mode is required to describe the held-out defects.

The observed problems already fit the frozen axes:

```text
unsupported edge strengthening → FALSE PROMOTION
omitted directly recoverable relations → MISSED STRUCTURE
```

Therefore:

```math
\boxed{
\text{NEW FAILURE MODE}=0
}
```

## 8. Failure clustering

Without proposing a repair, the missed structures cluster descriptively around:

```text
explicit discourse / connective edges
predicate detail
speaker / action attribution
temporal relations
cross-verse proposition correspondence
```

This clustering is an observation about held-out performance only. It is not a decoder revision.

## 9. Held-out conclusion

The held-out question was:

```math
\boxed{
\text{Did D1's precommitted rules generalize to unseen text without either overclaiming or collapsing into abstention?}
}
```

The audit result is:

```math
\boxed{
\text{D1 generalized strongly on epistemic precision.}
}
```

```math
\boxed{
\text{D1 retained substantial structural coverage, but did not maximize it.}
}
```

```math
\boxed{
\text{remaining error is predominantly under-recovery rather than overclaiming.}
}
```

No decoder repair is made here.

No replacement parse is supplied here.

No `D2` rule is proposed here.

The causal boundary remains:

```math
\boxed{
D_1^F
\rightarrow
P_3^F
\rightarrow
A_3
\rightarrow
\text{belief update about }D_1
}
```

and only a later, separate operation may ask whether the audit earns a successor decoder.
