# Transport 10 — Blind Level-3 Structural Invention Protocol

**Status:** FROZEN TEST PROTOCOL  
**Architecture:** `AG/1 = {RELATION, REPRESENTATION} + {SOURCE_PROVENANCE, OPEN}`  
**Prior milestone:** `transport/MILESTONE_T1_T9.md`  
**Task-class change:** reconstruction → candidate structural invention

---

# 1. Governing question

T10 asks:

```math
\boxed{
\textbf{Can a learner generate, test, and retract/retain a useful relation that was absent from its prior representation and was not supplied as an explicit candidate?}
}
```

The target sequence is:

```math
\boxed{
\rho_t
+
o_t\not\approx P_{\rho_t}
\rightarrow
Generate(\rho_t,o_t)
\rightarrow
\{x_1,\ldots,x_n\}
\rightarrow
Challenge(x_k)
\rightarrow
o_{t+1}
\rightarrow
\rho_{t+1}
}
```

with at least one generated candidate satisfying:

```math
\boxed{x_k\notin content(\rho_t)}
```

---

# 2. What counts as structural novelty

A candidate is structurally novel for this run only if it adds at least one relation pattern not asserted in the initial representation.

Examples include:

```text
new edge between already represented participants
new n-ary interaction relation
new intermediate participant + relations
new dependency between measurement process and measured process
new temporal/history dependence relation
```

A mere parameter change does not qualify:

```text
coefficient 1.0 → 1.2
threshold 5 → 6
noise variance revised
```

unless the parameter change is accompanied by a genuinely new source-supported relation topology.

---

# 3. Anti-cheat rules

A T10 success is invalid if the candidate relation is obtained through any of the following:

```text
human-supplied missing relation
external oracle
answer-key leakage
explicit finite menu containing the missing relation
exhaustive enumeration of all allowable graph edges/topologies
post-hoc fitting after seeing the challenge result
retrieval of the hidden answer from source metadata
```

The learner may compose new candidates from the existing generic capacities of `RELATION` and `REPRESENTATION`.

The learner may generate a small number of competing hypotheses from the contradiction.

The learner may not claim success merely because one candidate can retrospectively explain the evidence.

---

# 4. Blind-instance construction

A valid blind instance must separate:

```text
INITIAL EVIDENCE PACKET
HIDDEN GENERATING TOPOLOGY
CHALLENGE INTERFACE
HOLDOUT / REVEAL
```

The hidden topology is generated or curated before candidate generation.

Before any candidate is produced, publish a cryptographic commitment:

```text
SHA256(hidden_topology_serialization)
```

The hidden topology itself remains unavailable to the learner until the reveal phase.

This prevents the evaluator from altering the answer after seeing the learner's candidate.

---

# 5. Candidate-generation phase

Given only:

```text
initial representation rho_t
observed contradiction/anomaly packet
allowed intervention/challenge operations
```

the learner must commit:

```text
candidate relation/topology x_k
why it is structurally new relative to rho_t
at least one competing shallow explanation where useful
one prospective challenge chosen to discriminate x_k
predicted result if x_k is present
predicted result if x_k is absent / competing explanation holds
retraction condition
```

The candidate artifact must be committed before the challenge result is obtained.

---

# 6. Prospective discrimination requirement

A candidate cannot pass on explanatory fit alone.

It must entail a prospective difference:

```math
\boxed{
x_k\rightarrow P(o_{future}\mid a_k)
}
```

that differs from at least one live alternative:

```math
\boxed{
P_{x_k}(o_{future}\mid a_k)
\neq
P_{alt}(o_{future}\mid a_k)
}
```

Exact probabilities are not required unless the instance supplies a probabilistic model.

A directional, categorical, relational, or quantitative prediction is sufficient if it is genuinely discriminating.

---

# 7. Challenge phase

After the candidate artifact is frozen, the chosen challenge is executed against the hidden system.

The challenge result is committed before the hidden topology is revealed.

The learner must then update:

```text
RETAIN
RETRACT
REVISE
OPEN
```

with explicit provenance from the challenge result.

A correct retraction is a success of corrigibility even when the candidate itself was wrong.

---

# 8. Reveal and scoring

Only after candidate + prospective prediction + challenge observation + learner update are frozen may the hidden topology be revealed.

Score the run along separate axes.

## G — Generation novelty

```text
G0: no candidate generated
G1: parameter/value revision only
G2: recombination/search over explicit supplied candidates
G3: genuinely new relation topology relative to initial representation
```

## P — Prospective discrimination

```text
P0: no prospective difference
P1: vague/non-falsifiable difference
P2: concrete challenge-linked prediction
```

## E — Empirical contact

```text
E0: no challenge executed
E1: challenge executed but does not bear on candidate
E2: challenge discriminates candidate from at least one alternative
```

## C — Corrigibility

```text
C0: candidate retained regardless of contrary evidence
C1: uncertainty acknowledged but candidate not properly revised
C2: candidate retained/retracted/revised in the direction earned by evidence
```

## H — Hidden-topology agreement

```text
H0: candidate misses hidden structural relation
H1: candidate captures a useful partial structural dependency
H2: candidate recovers the hidden relation/topology at the tested resolution
```

---

# 9. Outcome classes

## LEVEL3_CONFIRMED

Require at minimum:

```text
G3
P2
E2
C2
H1 or H2
```

with no contamination violation.

This supports the bounded claim:

```math
\boxed{
\textbf{in this instance, contradiction led to a novel structural candidate that earned predictive contact with hidden structure while remaining retractable.}
}
```

## INVENTION_RETRACTED_CORRECTLY

A generated G3 candidate is empirically rejected and the learner retracts it correctly.

This is evidence for:

```math
\boxed{
\textbf{invention without epistemic foreclosure}
}
```

but not recovery of the hidden topology.

## SEARCH_ONLY

The successful candidate was already supplied explicitly or found only by exhaustive enumeration.

Do not count as Level 3.

## REPRESENTATION_ONLY

The learner can encode the hidden relation after reveal but did not generate it before reveal.

This reproduces the T9 capability only.

## GENERATION_FAILURE

Contradiction is detected but no useful G3 structural candidate is generated.

## OPEN_TEST

The evidence/challenge interface is insufficient to discriminate the candidate.

## CONTAMINATED

Any answer-key leakage, post-hoc candidate generation, or invalid oracle access occurred.

---

# 10. Architecture versus learner capability

A T10 generation failure does not by itself imply AG/1 needs another primitive.

AG/1 may remain representationally sufficient while the learner lacks a search/generation operator capable of proposing useful graph expansions.

Therefore always distinguish:

```math
\boxed{
\text{carrier architecture}
\neq
\text{candidate-generation algorithm}
\neq
\text{challenge-selection algorithm}
}
```

T10 tests the latter capabilities operating over the frozen architecture.

---

# 11. Current claim ceiling

Before a valid blind T10 run:

```math
\boxed{
\textbf{AG/1 has survived nine heterogeneous external reconstruction tests without architectural enlargement.}
}
```

No claim is yet earned that AG/1-equipped learners can invent missing interfaces or relations.

---

# 12. Binding maxim

```math
\boxed{
\textbf{Do not reward a story for fitting the past. Reward a new distinction only when it risks a future prediction and remains deletable.}
}
```
