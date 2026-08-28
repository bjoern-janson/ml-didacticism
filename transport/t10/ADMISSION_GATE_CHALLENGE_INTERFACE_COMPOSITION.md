# T10 Admission Gate Addendum — Challenge Interface Must Not Be an Ontology Menu

**Status:** FROZEN ADMISSION-GATE ADDENDUM  
**Parent protocol:** `transport/10B_LEVEL3_PROTOCOL_V2_HYPOTHESIS_SPACE_ISOLATION.md`  
**Applies to:** all future T10 Level-3 runs beginning with T10.002  
**Current T10.002 status:** `UNSTARTED`

---

# 1. Motivation

A Level-3 test can remain contaminated even when:

```text
H_answer is hidden
H_family is not explicitly named
task constructor is externally separated
```

if the **challenge interface itself** exposes only a small curated set of operations whose structure effectively enumerates the intended hypothesis family.

Example:

```text
"Choose any experiment"
```

while the actual interface permits only:

```text
operation_1
operation_2
operation_3
operation_4
operation_5
```

where those five operations were hand-designed around the hidden structural alternatives.

Then:

```math
\boxed{
\text{nominally open challenge selection}
\neq
\text{genuinely open compositional challenge construction}
}
```

and:

```math
\boxed{
\text{novel candidate}
\text{ may collapse into }
\text{hidden multiple-choice search}
}
```

This addendum closes that leakage path.

---

# 2. Challenge-interface object of audit

For a challenge interface `J`, audit three layers:

```math
\boxed{
J=
\langle
A_{primitive},
\Theta,
Closure(A_{primitive},\Theta)
\rangle
}
```

where:

```text
A_primitive  = primitive operations available to learner
Theta        = operation parameterization space
Closure      = interventions constructible by composing primitives/parameters
```

The interface is not judged only by the number of API endpoints.

The relevant question is:

```math
\boxed{
\textbf{what class of distinct interventions can the learner construct without selecting from a curator-authored ontology menu?}
}
```

---

# 3. Invalid challenge interfaces

The following are inadmissible for `LEVEL3_CONFIRMED`.

## 3.1 Finite ontology menu

```text
choose one:
    test_interaction
    test_mediation
    test_feedback
    test_confounding
```

This directly leaks a candidate family.

## 3.2 Semantically disguised menu

```text
probe_1
probe_2
probe_3
probe_4
```

is still invalid if each probe was curated to correspond to one hidden structural hypothesis.

Renaming does not remove leakage.

## 3.3 Narrow parameterization that encodes the answer family

Example:

```text
challenge(pair_of_variables, interaction_strength)
```

when the hidden constructor guarantees that the missing distinction is a pairwise interaction.

The interface has already supplied the ontology even if it does not supply the exact pair.

## 3.4 Exhaustive intervention enumeration

If the learner can obtain Level-3 credit by mechanically trying every available challenge until one identifies the answer, the run is `SEARCH_ONLY` unless the candidate itself was independently generated before enumeration.

## 3.5 Constructor-shaped compositionality

An interface is not rescued merely because operations can technically be composed.

If the primitive set and composition grammar were selected specifically so that their closure closely matches the hidden answer family, this is constructor leakage.

---

# 4. Preferred challenge-interface form

A strong interface exposes low-level operations whose compositional closure is broad relative to the hidden distinction.

Examples may include domain-appropriate primitives such as:

```text
set or perturb a controllable quantity
hold another quantity fixed
repeat under changed context
route a signal through a selectable path
attach/remove a measurement operation
change timing/order of operations
construct a derived measurement from observable quantities
compare outputs under learner-chosen contrasts
```

The important property is not these exact verbs.

It is:

```math
\boxed{
\textbf{the learner composes a challenge from generic operations rather than selecting an experiment whose ontology was authored for the answer.}
}
```

---

# 5. Compositional-closure audit

Before T10.002 begins, the curator must document:

```text
1. primitive challenge operations
2. parameter domains for each operation
3. allowed operation composition
4. ordering/conditional composition rules
5. resource/query limits
6. forbidden operations and why
7. whether the hidden answer family can be inferred from the interface grammar
8. whether exhaustive traversal of the interface effectively enumerates the hidden ontology
```

Then classify:

```text
INTERFACE_CLEAR
INTERFACE_POSSIBLE_LEAK
INTERFACE_LEAK
```

A material `INTERFACE_LEAK` forces:

```text
T10 instance = UNSTARTED
```

if discovered before learner exposure.

If discovered only after exposure:

```text
CONTAMINATED_CONSTRUCTOR
```

or:

```text
CONTAMINATED_FAMILY
```

as appropriate.

---

# 6. Counterfactual interface criterion

A useful anti-menu test is:

```math
\boxed{
\textbf{Would the same challenge interface remain natural and useful if the curator had instantiated a materially different hidden structural family?}
}
```

If **no**, the interface likely encodes the intended ontology.

If **yes**, that is evidence—though not proof—that the interface is generic enough for Level-3 use.

Examples of materially different structural families may include, where domain-appropriate:

```text
new direct relation
new mediator
new n-ary interaction
history/lag dependence
measurement-process dependency
context-conditional path
unrepresented participant
relation reversal
nonlocal coupling
```

These examples are for curator-side audit only.

They must not be supplied to the learner as a candidate menu.

---

# 7. Candidate generation must precede challenge search

The learner must commit a structural candidate before performing broad challenge exploration.

Required order:

```math
\boxed{
contradiction
\rightarrow
candidate\ X
\rightarrow
prospective\ discriminator\ a_X
\rightarrow
execute\ challenge
}
```

Not:

```math
\boxed{
run\ all\ available\ probes
\rightarrow
notice\ which\ probe\ behaves\ strangely
\rightarrow
invent\ candidate\ afterward
}
```

The latter is post-hoc search, not the Level-3 capability under test.

---

# 8. Wrong invention remains positive evidence when corrigible

Challenge-interface openness must not bias the scoring toward hidden-answer recovery only.

A valid run may produce:

```math
\boxed{
X_{novel}
\rightarrow
prediction
\rightarrow
challenge
\rightarrow
\neg prediction
\rightarrow
RETRACT
}
```

and receive:

```text
INVENTION_RETRACTED_CORRECTLY
```

provided:

```text
N_data=1
N_learner=1
N_constructor=1
interface audit passes
candidate was prospectively committed
retraction follows evidence
```

Thus being wrong can be positive Level-3 evidence about **generation + corrigibility**, even though it is not hidden-topology recovery.

---

# 9. Admission gate extension for T10.002

The frozen v2 admission gate is extended with:

```text
[ ] primitive challenge operations documented
[ ] parameterization documented
[ ] compositional closure documented
[ ] interface not a finite/disguised ontology menu
[ ] interface remains natural under counterfactual hidden families
[ ] exhaustive interface traversal does not trivially enumerate hidden ontology
[ ] candidate must be committed before broad challenge exploration
```

All existing v2 admission requirements remain binding.

If any required gate is not established:

```text
T10.002 = UNSTARTED
```

---

# 10. Current state

```text
T1–T9      PASS           reconstruction / transport
T10.001    CONTAMINATED   family + constructor leakage
T10.002    UNSTARTED      no independent admitted curator/corpus yet
```

The current Level-3 claim remains:

```math
\boxed{OPEN}
```

No experiment is to be run merely to advance the sequence number.

The next legitimate state transition is:

```math
\boxed{
UNSTARTED
\rightarrow
ADMITTED
}
```

only after an independent curator/corpus passes the complete v2 + challenge-interface gate.

---

# 11. Binding compression

```math
\boxed{
\textbf{Do not let the challenge language smuggle in the hypothesis language.}
}
```

and:

```math
\boxed{
\textbf{Level 3 begins only when the learner must supply the distinction, not merely choose how to ask for it.}
}
```
