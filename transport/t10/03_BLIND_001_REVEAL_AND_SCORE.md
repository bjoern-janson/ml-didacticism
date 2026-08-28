# T10 Blind Instance 001 — Hidden Topology Reveal and Score

**Protocol:** `transport/10_LEVEL3_BLIND_STRUCTURAL_INVENTION_PROTOCOL.md`  
**Evidence:** `transport/t10/00_BLIND_001_EVIDENCE.md`  
**Candidate:** `transport/t10/01_BLIND_001_CANDIDATE.md`  
**Challenge result:** `transport/t10/02_BLIND_001_CHALLENGE_RESULT.md`  
**Status:** REVEALED / SCORED  
**Final outcome:** `CONTAMINATED` — does **not** count as Level-3 confirmation

---

# 1. Commitment verification

Published before candidate generation:

```text
33e69350718d1022dad2b991972e08c486eeb3ea50014147d635953fef2d9737
```

Recomputed after reveal from the sealed hidden-topology serialization:

```text
33e69350718d1022dad2b991972e08c486eeb3ea50014147d635953fef2d9737
```

Therefore:

```text
COMMITMENT MATCH: YES
```

The evaluator did not alter the hidden instance after seeing the learner's candidate.

---

# 2. Hidden topology reveal

The sealed generator instance contained:

```text
type: joint_interaction
sources: B, C
target: Y1
relation: JOINT_EFFECT(B,C) -> Y1
coefficient: -2.25
```

Hidden quantitative relation:

```math
\boxed{
\Delta Y_1=-2.25BC
}
```

The learner candidate committed before challenge was:

```math
\boxed{
JOINT\_EFFECT(B,C,Y_1)
}
```

with:

```math
\boxed{
\Delta Y_1\approx-2.25BC.
}
```

So at the exposed structural/quantitative resolution:

```text
CANDIDATE ↔ HIDDEN TOPOLOGY MATCH: EXACT
```

---

# 3. Prospective test performance

The candidate prospectively predicted residuals:

```text
Q1: -9
Q2: +9
Q3:  0
Q4:  0
```

The simulator returned exactly:

```text
Q1: -9
Q2: +9
Q3:  0
Q4:  0
```

The learner retained the candidate before reveal, consistent with its precommitted retention/retraction rule.

Ignoring contamination, the raw behavioral scores would be:

```text
P2 — concrete challenge-linked prediction
E2 — challenge discriminated the candidate from shallow alternatives
C2 — learner update followed the evidence
H2 — candidate recovered the hidden relation at tested resolution
```

The only disputed axis is generation novelty `G`.

---

# 4. Contamination audit — decisive failure

The hidden simulator for Blind Instance 001 was authored in the same learner context that later generated the candidate.

More importantly, the generator's hidden structural family was restricted in advance to:

```text
joint interaction among controls affecting one output
```

with randomized:

```text
source pair
target output
coefficient
```

Therefore, although the exact hidden instance was cryptographically sealed and not revealed, the learner had implicitly preloaded knowledge of the missing relation **family** through authorship of the generator.

That violates the T10 anti-cheat rule against:

```text
candidate relation supplied through a hidden predefined library / evaluator prior
```

The evidence still selected the correct members and coefficient, but the run cannot establish that contradiction caused generation of an unconstrained structural distinction.

Thus:

```text
FINAL OUTCOME: CONTAMINATED
```

not:

```text
LEVEL3_CONFIRMED
```

---

# 5. Correct interpretation

Blind Instance 001 validates several pieces of the protocol machinery:

```text
cryptographic precommitment works
candidate can be frozen before challenge
prospective prediction can be frozen before challenge
challenge can be executed before reveal
candidate can remain retractable
reveal/scoring can occur after all learner commitments
```

It also demonstrates that AG/1 can encode the generated candidate and the complete candidate → challenge → evidence → update sequence.

But T9 had already established representational sufficiency for newly added topology.

Blind 001 does **not** advance the Level-3 claim.

---

# 6. What a valid next instance must change

A valid T10 Level-3 instance needs independence between:

```text
task/hidden-topology construction
```

and:

```text
learner candidate generation
```

At minimum, the learner must not know a narrow hidden relation family selected by the evaluator.

Acceptable stronger constructions include:

```text
independent curator supplies sealed task + answer
external time-split corpus where learner sees only pre-discovery evidence before committing candidate
procedural generator authored outside learner context with a broad compositional relation language rather than an answer-family menu
```

The missing relation must remain unavailable as an explicit option.

---

# 7. Claim ceiling after this pilot

The calibrated external-transport claim remains:

```math
\boxed{
\textbf{AG/1 has survived nine heterogeneous external reconstruction tests without architectural enlargement.}
}
```

No valid claim is yet earned that an AG/1-equipped learner has demonstrated autonomous Level-3 structural invention.

The T10 boundary remains open.

---

# 8. Methodological result

The pilot exposes a useful new distinction:

```math
\boxed{
\textbf{hidden instance}
\neq
\textbf{hidden hypothesis class}
}
```

Cryptographically hiding the exact answer is insufficient if the learner already knows the narrow family from which the answer must come.

Therefore future T10 runs must protect not only answer secrecy but also candidate-family independence strongly enough that a successful candidate can count as genuine structural generation rather than constrained search.
