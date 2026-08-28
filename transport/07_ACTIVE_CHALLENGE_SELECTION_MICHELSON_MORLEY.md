# AG/1 Transport Test 07 — Active Challenge Selection / Michelson–Morley → Morley–Miller

**Protocol:** `transport/00_TRANSPORT_PROTOCOL_AG1.md`  
**Frozen architecture:** `abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md` (`AG/1`)  
**Prior milestone:** `transport/MILESTONE_T1_T6.md`  
**Test status:** COMPLETED  
**External-domain class:** experimental physics / deliberate discrimination / challenge selection / unresolved theory family

---

# 1. Selection rationale

Transport 06 established that actions can alter future observation topology without requiring `INTERFACE` or `OBSERVABILITY` as primitives.

Transport 07 attacks the next proposed distinction:

```math
\boxed{\textbf{expected discriminatory value}}
```

The target is not merely:

```text
perform experiment
→ observe result
```

but:

```math
\boxed{
\rho_t
\rightarrow
\{a_1,a_2,\ldots,a_n\}
\rightarrow
SELECT(a_k\mid\rho_t)
\rightarrow
EXECUTE(a_k)
\rightarrow
o_{t+1}
\rightarrow
\rho_{t+1}
}
```

where the source explicitly earns a prospective relation of the form:

```text
a_k was chosen because competing represented models predict discriminating outcomes under it
```

The test asks whether this can be reconstructed using only:

```math
\boxed{RELATION + REPRESENTATION + SOURCE\_PROVENANCE + OPEN}
```

without adding:

```text
QUERY
EXPERIMENT_DESIGN
ACTIVE_LEARNING
INFORMATION_GAIN
VALUE_OF_INFORMATION
EXPLORATION
CHALLENGE_SELECTION
```

as new architecture primitives.

---

# 2. Bounded external corpus

This run uses a bounded historical physics sequence.

## S1 — Michelson & Morley, 1887

```text
Albert A. Michelson and Edward W. Morley
On the Relative Motion of the Earth and the Luminiferous Ether
American Journal of Science 34 (1887), 333–345
validated transcription:
https://en.wikisource.org/wiki/The_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether
```

Source-level facts used:

```text
stationary-ether theory predicts direction-dependent light travel time;
rotating the interferometer should produce a calculable periodic fringe displacement;
the expected shift was on the order of one-tenth of a fringe spacing under the working assumptions;
the observed displacement was far smaller / effectively null;
the authors interpreted the result as contradicting the stationary-ether hypothesis.
```

## S2 — Morley & Miller, 1905

```text
Edward W. Morley and Dayton C. Miller
On the Theory of Experiments to detect Aberrations of the Second Degree
Philosophical Magazine 9 (1905), 669–680
validated transcription:
https://en.wikisource.org/wiki/On_the_Theory_of_Experiments_to_detect_Aberrations_of_the_Second_Degree
```

Source-level facts used:

```text
the 1887 result was at most about one-fortieth of the expected effect;
FitzGerald/Lorentz contraction was proposed to explain the null result;
one contraction interpretation is material-independent;
another may depend on physical material properties;
these alternatives imply potentially different behavior for sandstone and pine;
Morley and Miller built a new pine apparatus with larger optical effect;
they explicitly state that its object was to determine whether sandstone and pine behave differently;
the experiment again produced a null result.
```

## S3 — AIP / APS historical record

```text
American Institute of Physics historical Michelson exhibit
https://history.aip.org/exhibits/gap/Michelson/Michelson.html

American Physical Society historical account
https://www.aps.org/apsnews/2007/11/november-1887-michelson-uminiferous-ether
```

Source-level facts used only for the claim-ceiling / unresolved-family check:

```text
the null result did not immediately end ether-based theorizing;
FitzGerald and Lorentz proposed contraction explanations;
Michelson and Morley continued to believe in some form of ether despite the null result.
```

Excluded from evidence for this run:

```text
modern textbook reconstructions beyond the bounded historical summaries
later precision ether-drift experiments
special-relativity derivations not required to reconstruct the challenge-selection episode
popular retellings
```

---

# 3. Frozen machinery available

Only:

```math
\boxed{
RELATION
+
REPRESENTATION
+
SOURCE\_PROVENANCE
+
OPEN
}
```

Source-earned local predicates remain allowed.

No prospective-utility carrier may be added.

---

# 4. Reconstruction principle — expected discrimination is scoped relational content

Suppose two live represented alternatives are:

```text
rho_H1
rho_H2
```

and a candidate action `a` is represented as producing different expected observations under the two alternatives:

```text
content(rho_expect_a_H1):
    IF EXECUTE(a) AND H1
    → EXPECT(o1)

content(rho_expect_a_H2):
    IF EXECUTE(a) AND H2
    → EXPECT(o2)
```

with:

```math
\boxed{o_1\neq o_2}
```

Then the prospective discriminatory structure can be represented through ordinary relations:

```text
PREDICTS_UNDER(rho_H1,a,rho_o1)
PREDICTS_UNDER(rho_H2,a,rho_o2)
DIFFERS_FROM(rho_o1,rho_o2)
SELECTS_FOR_TEST(actor,a,rho_H1,rho_H2)
```

No scalar:

```text
information_gain(a)=x
```

is required.

The kill test is whether the source requires some extra semantic residue beyond these relations and scoped predictions.

---

# 5. Witness C1 — 1887: choose rotation because the stationary-ether model predicts a directional fringe shift

The 1887 paper starts from a represented physical model:

```text
rho_stationary_ether:
    ether approximately stationary
    Earth moves through ether
    light travel time depends on direction relative to Earth motion
```

The experimental action is not arbitrary.

The authors derive a prospective observational consequence:

```text
IF stationary ether
AND interferometer arms rotate relative to Earth motion
→ interference fringes should shift periodically
```

They estimate the displacement to be sought at roughly one-tenth of a fringe spacing under the working assumptions.

So the relation structure is:

```text
PREDICTS_UNDER(rho_stationary_ether,ROTATE_INTERFEROMETER,rho_expected_shift)

rho_expected_shift:
    PERIODIC_FRINGE_DISPLACEMENT ≈ 0.1 fringe

SELECTS_FOR_TEST(Michelson_Morley,ROTATE_INTERFEROMETER,rho_stationary_ether)
```

The experiment is therefore selected because its represented consequences would expose a distinction relevant to the live model.

No `INFORMATION_GAIN` primitive is needed.

### Result

```text
PASS
```

---

# 6. Witness C2 — prospective discrimination remains separate from realized result

The selected action is executed:

```text
ROTATES(interferometer)
OBSERVES(fringe_positions)
```

The observed displacement is far smaller than the predicted stationary-ether shift and is treated as experimental error / effectively null.

Keep separate:

```text
rho_expected_shift
rho_observed_result
```

with:

```math
\boxed{
rho_{expected}\neq rho_{observed}
}
```

and historical relations:

```text
EXECUTES(Michelson_Morley,ROTATE_INTERFEROMETER)
REPORTS_RESULT(experiment,rho_observed_result)
CONTRADICTS_OR_FAILS_TO_MATCH(rho_observed_result,rho_expected_shift)
```

Thus:

```math
\boxed{
\text{represented discriminatory value}
\neq
\text{actual information obtained}
}
```

No assumption is made that a well-motivated challenge must return the expected discriminating signal.

### Result

```text
PASS
```

---

# 7. Witness C3 — null evidence modifies the live model set without requiring global resolution

Michelson and Morley interpreted the result as contradicting the stationary-ether hypothesis used to derive the expected fringe shift.

Represent:

```text
INTERPRETS_AS_CONTRADICTING(
    Michelson_Morley,
    rho_observed_null,
    rho_stationary_ether
)
```

But this does not require:

```text
ETHER = false
```

as an unconditional historical assertion.

The bounded later record preserves alternative ether-related explanations.

So:

```math
\boxed{
\text{challenge eliminates/pressures one represented mechanism}
\neq
\text{all neighboring models resolved}
}
```

This is important because the challenge was deliberately discriminating but did not collapse the broader theoretical family.

### Result

```text
PASS
```

---

# 8. Witness C4 — 1905: the selected action is explicitly chosen to distinguish two contraction models

The 1905 paper gives a stronger prospective-selection witness.

After the 1887 null result, FitzGerald/Lorentz contraction provides a possible explanation.

Morley and Miller then distinguish two represented variants.

## H1 — material-independent contraction

```text
rho_geometric_contraction:
    contraction independent of physical material
    sandstone and pine of same form should contract in same ratio
```

## H2 — material-dependent contraction

```text
rho_material_contraction:
    contraction depends on physical properties
    pine may compress more than sandstone
```

The paper explicitly notes that if compression cancels the expected effect in one apparatus, a different apparatus might show a nonzero or even opposite-sign effect.

This gives different prospective consequences under a changed material intervention:

```text
PREDICTS_UNDER(rho_geometric_contraction,PINE_APPARATUS,rho_same_behavior)
PREDICTS_UNDER(rho_material_contraction,PINE_APPARATUS,rho_different_behavior)
```

with:

```math
\boxed{
rho_{same\_behavior}\neq rho_{different\_behavior}
}
```

The authors then state explicitly that they completed an experiment using two pine structures, with enlarged optical sensitivity, and that:

```text
its object was to determine whether there is any difference between the behaviour of sandstone and pine
```

Therefore:

```text
SELECTS_FOR_TEST(Morley_Miller,PINE_APPARATUS,rho_geometric_contraction,rho_material_contraction)
```

is source-earned.

This is the direct T7 discriminator:

```math
\boxed{
\textbf{action chosen because its represented outcomes differ across live models}
}
```

### Result

```text
PASS
```

---

# 9. Witness C5 — challenge selection is not the same thing as action selection for ordinary utility

The corpus does not require a generic concept of why all actions are chosen.

It only requires the local source relation that this particular experimental configuration was chosen to test a represented difference.

So AG/1 need not contain:

```text
UTILITY
VALUE
POLICY
EXPLORATION
```

A source-earned relation is enough:

```text
PURPOSE_OF(experiment,rho_distinguish_material_behavior)
SELECTS_FOR_TEST(actor,apparatus,rho_H1,rho_H2)
```

The architectural distinction is:

```math
\boxed{
\text{selection relation}
+
\text{prospective scoped predictions}
\neq
\text{new selection primitive}
}
```

### Result

```text
PASS
```

---

# 10. Witness C6 — selected challenge can still fail to settle the broader uncertainty

The 1905 paper describes the experiment as null.

The broader historical record also shows that ether-related explanations persisted after the 1887 result, and that Michelson and Morley themselves did not simply abandon all ether concepts.

Therefore T7 preserves the negative case:

```math
\boxed{
\text{deliberately selected discriminating challenge}
\rightarrow
\text{new evidence}
\not\Rightarrow
\text{complete theoretical resolution}
}
```

This prevents hidden assumptions such as:

```text
selected_for_discrimination = guaranteed_information_gain
```

or:

```text
null_result = unique model selection
```

The realized update remains source-dependent.

### Result

```text
PASS
```

---

# 11. Hidden-parameter audit

The reconstruction does not use:

```text
query object
experiment-design carrier
active-learning primitive
information-gain scalar
value-of-information scalar
exploration state
challenge-selection state
policy object
```

The following appear only as source-earned typed relation vocabulary or representation content:

```text
PREDICTS_UNDER
SELECTS_FOR_TEST
PURPOSE_OF
EXPECTS
EXECUTES
REPORTS_RESULT
DIFFERS_FROM
INTERPRETS_AS_CONTRADICTING
```

No unrestricted field such as:

```text
action.expected_information_gain = ...
representation.discriminatory_value = ...
system.active_learning_mode = ...
```

is used.

The hidden-parameter audit passes.

---

# 12. Failure search

T7 deliberately searched for missing structure at these edges:

```text
live alternative models
→ candidate experimental manipulation
→ represented model-conditional outcomes
→ represented outcome difference
→ selection because of that difference
→ execution
→ realized observation
→ partial/failed model discrimination
```

None forces a new architecture primitive.

The strongest reconstruction is:

```math
\boxed{
\textbf{expected discriminatory value is representable as relational structure among candidate actions, scoped model-conditional predictions, and a source-earned selection relation.}
}
```

and:

```math
\boxed{
\textbf{active challenge selection is a derived relational motif over representation, not a primitive carrier, for this bounded corpus.}
}
```

---

# 13. Verdict

```text
PASS
```

More precisely:

```math
\boxed{
\textbf{Transport 07 does not force an architectural primitive beyond frozen AG/1.}
}
```

The decisive T7 structure is:

```math
\boxed{
\rho_{H_1},\rho_{H_2}
\rightarrow
\{a_i\}
\rightarrow
\rho_{expected\ consequences}
\rightarrow
SELECT(a_k)
\rightarrow
EXECUTE(a_k)
\rightarrow
o
\rightarrow
\rho'
}
```

where every prospective and realized step remains representable through ordinary typed relations plus scoped content.

---

# 14. What this result does not establish

This PASS does not establish:

```text
AG/1 is universal.
all experiment design is reducible in every domain.
all action selection can be reconstructed from prospective discrimination.
expected information value is never a useful derived quantity.
every selected experiment is informative.
null results uniquely resolve competing models.
Michelson–Morley alone logically entailed special relativity.
```

It establishes only:

```math
\boxed{
\textbf{this bounded active-challenge-selection corpus failed to force an addition to AG/1.}
}
```

---

# 15. Transport ledger after T7

```text
T1  software incident                                  PASS
T2  experimental science                               PASS
T3  shared evidence / competing analyses               PASS
T4  same observation / different worlds                PASS
T5  representation-driven causal loop                  PASS
T6  observation-topology modification                  PASS
T7  deliberate challenge selection                     PASS
```

The calibrated claim after this run is:

```math
\boxed{
\textbf{AG/1 has survived seven heterogeneous external reconstruction tests without architectural enlargement.}
}
```

This remains a bounded empirical transport claim, not a universality theorem.
