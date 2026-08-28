# AG/1 Transport Test 08 — Challenge Independence / Ariane 501 Common-Mode Validation

**Protocol:** `transport/00_TRANSPORT_PROTOCOL_AG1.md`  
**Frozen architecture:** `abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md` (`AG/1`)  
**Prior milestone:** `transport/MILESTONE_T1_T7.md`  
**Test status:** COMPLETED  
**External-domain class:** launch-vehicle software / redundancy / common-mode failure / validation coverage / challenge independence

---

# 1. Selection rationale

Transport 07 established that AG/1 can reconstruct deliberate challenge selection from represented model-conditional consequences without adding a prospective-utility primitive.

Transport 08 attacks the next orthogonal distinction:

```math
\boxed{\textbf{challenge independence}}
```

The target is not merely whether a challenge is rationally selected.

It is whether the challenge/backup/validation path shares a dependency with the system it is intended to check or recover from.

The adversarial pattern is:

```math
\boxed{
DEPENDS(primary,X)
\qquad
DEPENDS(challenge,X)
}
```

while the challenge is represented or engineered as providing redundancy, validation, or discrimination.

The architecture must preserve:

```math
\boxed{
\text{nominal redundancy / validation}
\neq
\text{independence with respect to a particular failure-generating dependency}
}
```

without adding:

```text
INDEPENDENCE
COMMON_MODE
ASSUMPTION
CONFOUND
IDENTIFIABILITY
VALIDATION_STATE
EXOGENOUS_TEST
```

as new architecture primitives.

---

# 2. Bounded external corpus

This run uses the Ariane 5 Flight 501 inquiry record and ESA's official summary/action records.

## S1 — Ariane 501 Inquiry Board report

```text
Ariane 5 Flight 501 Failure
Report by the Inquiry Board
Paris, 19 July 1996

validated public mirrors of the official report:
https://ocw.mit.edu/courses/16-355j-software-engineering-concepts-fall-2005/resources/ari5fail_ful_rep/
https://www.cs.toronto.edu/~yijun/csc408h/reference/ariane5rep.pdf
```

Source-level facts used:

```text
two inertial reference systems (SRIs) operated in parallel;
one was active and one was hot standby;
the two SRIs had identical hardware and software;
the backup SRI failed first and the active SRI failed shortly afterward for the same software reason;
the software exception arose from an unprotected conversion of a 64-bit floating-point value to a 16-bit signed integer;
the failing alignment function had been retained from Ariane 4 and was not required after Ariane 5 liftoff;
software exception handling shut the SRI processor down;
the report explicitly warns that the same software running in both SRI units made software-function loss hazardous;
qualification/system tests did not include sufficiently representative SRI behavior with Ariane 5 trajectory data;
actual SRIs were replaced by simulated SRI output in important system simulations;
post-flight simulations using the actual SRI software with the Ariane 501 trajectory reproduced the failure chain.
```

## S2 — ESA presentation of Inquiry Board report

```text
European Space Agency
Ariane 501 — Presentation of Inquiry Board report
23 July 1996
https://www.esa.int/Newsroom/Press_Releases/Ariane_501_-_Presentation_of_Inquiry_Board_report
```

Source-level facts used:

```text
both inertial reference systems failed;
the loss of guidance came from specification/design errors in SRI software;
extensive reviews/tests did not adequately analyze/test the SRI or complete flight-control system;
the alignment function was not represented adequately in simulations;
testing environments were not sufficiently representative;
ESA/CNES accepted recommendations for more representative testing, real-equipment use, trajectory simulation, deliberate test overlap, and review of double-failure management.
```

## S3 — ESA qualification action plan

```text
European Space Agency
Qualification of Ariane-5 plan of action for a resumption of flights
11 September 1996
https://www.esa.int/Newsroom/Press_Releases/Qualification_of_Ariane-5_plan_of_action_for_a_resumption_of_flights
```

Source-level facts used:

```text
software correction in the SRI;
changes to simulation facilities to improve representativeness;
review of embedded software;
software-architecture responsibility strengthened.
```

Excluded from evidence for this run:

```text
popular summaries
later software-engineering textbooks except as pointers to the official report
unrelated Ariane failures
secondary organizational-culture interpretations not required by the bounded sources
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

No independence/common-mode carrier may be added.

---

# 4. Reconstruction principle — independence is relative dependency topology

Suppose a primary path `P` and a challenge/backup path `C` are both related to some dependency `X`:

```text
DEPENDS_ON(P,X)
DEPENDS_ON(C,X)
```

Then with respect to failure mode `F_X` generated through `X`, the paths are not independent in the relevant structural sense.

A derived query may inspect:

```math
\boxed{
SharedDeps(P,C)
:=
\{x\mid DEPENDS\_ON(P,x)\land DEPENDS\_ON(C,x)\}
}
```

and, where source relations earn it:

```math
\boxed{
SharedFailurePath(P,C,F)
}
```

may be reconstructed from the ordinary relation graph.

No scalar or primitive:

```text
independence(P,C)=0.2
```

is required.

The kill test is whether any source distinction about challenge dependence remains unreconstructible once these concrete dependency relations are retained.

---

# 5. Witness I1 — nominal hot-standby redundancy shares the same software dependency

The flight-control design used two SRIs in parallel.

Represent:

```text
ACTIVE_DURING(SRI_2,flight_segment)
HOT_STANDBY_FOR(SRI_1,SRI_2)

DEPENDS_ON(SRI_1,SRI_software_X)
DEPENDS_ON(SRI_2,SRI_software_X)

IDENTICAL_HARDWARE_CLASS(SRI_1,SRI_2)
IDENTICAL_SOFTWARE(SRI_1,SRI_2,SRI_software_X)
```

The backup path was intended to preserve guidance if the active SRI failed, subject to the backup remaining functional:

```text
BACKS_UP(SRI_1,SRI_2)
SWITCHES_TO_IF_AVAILABLE(OBC,SRI_1,FAILURE_OF(SRI_2))
```

But the Inquiry Board established:

```text
FAILS_BY(SRI_1,software_exception_X)
FAILS_BY(SRI_2,software_exception_X)
SAME_FAILURE_REASON(software_exception_X,SRI_1,SRI_2)
```

The backup was therefore redundant at equipment level while sharing the systematic software dependency that generated the failure.

The decisive structure is:

```math
\boxed{
\text{BACKS_UP}(C,P)
\not\Rightarrow
\text{no shared failure-generating dependency}
}
```

No primitive `COMMON_MODE_FAILURE` is required.

### Result

```text
PASS
```

---

# 6. Witness I2 — a challenge channel can be suitable for random failure yet non-independent for systematic software failure

The report explains that the backup philosophy was shaped around random hardware failure.

That distinction can be represented locally:

```text
DESIGNED_TO_COVER(backup_policy,rho_random_hardware_failure)

rho_random_hardware_failure:
    one unit fails independently
    alternate unit remains functional
```

But the realized failure was:

```text
rho_systematic_software_failure:
    shared software computation overflows
    same exception-handling rule shuts each processor down
```

with:

```text
NOT_COVERED_BY(backup_policy,rho_systematic_software_failure)
```

where the source earns that relation.

Thus:

```math
\boxed{
\text{independence relative to one failure family}
\neq
\text{independence relative to another failure family}
}
```

This is important because challenge independence is not a global boolean property.

It is relative to which generating dependency is under pressure.

No `INDEPENDENCE` primitive is required to preserve that scope.

### Result

```text
PASS
```

---

# 7. Witness I3 — preflight system validation omitted the hidden failure mechanism

The inquiry record says that system-level simulations did not exercise the two actual SRIs in a sufficiently representative way.

Instead, SRI output was simulated for important qualification tests.

Represent:

```text
SYSTEM_TESTS(Ariane5,flight_control_system)
REPLACES_WITH_SIMULATED_OUTPUT(system_test,SRI_behavior)

DOES_NOT_EXERCISE(
    system_test,
    actual_SRI_alignment_software_under_Ariane5_trajectory
)
```

The hidden failure mechanism required the actual relation chain:

```text
Ariane5_trajectory
→ high_horizontal_velocity_related_value
→ unprotected_numeric_conversion
→ operand_error
→ processor_shutdown
```

If the validation harness supplies expected SRI outputs instead of executing the internal SRI path, that chain is absent from the challenge topology.

So:

```math
\boxed{
\text{system test includes SRI interface output}
\neq
\text{system test independently exercises SRI internal failure mechanism}
}
```

No primitive `VALIDATION_COVERAGE` is required.

Coverage is a derived relation question:

```math
\boxed{
\text{does challenge }C\text{ contain a path through the failure-generating relations under test?}
}
```

### Result

```text
PASS
```

---

# 8. Witness I4 — apparent validation strength can be inflated by shared/omitted assumptions

The Ariane programme had undergone extensive reviews and tests, yet the Inquiry Board concluded that those tests did not adequately analyze or exercise the SRI or complete flight-control behavior that produced the failure.

AG/1 must not encode:

```text
MANY_TESTS
→ SYSTEM_CORRECT
```

Instead:

```text
PERFORMS(program,qualification_tests)
PASSES_OR_COMPLETES(program,qualification_sequence)

DOES_NOT_COVER(test_sequence,rho_failure_path_X)
```

where `rho_failure_path_X` is the scoped later reconstruction of the failure mechanism.

Thus:

```math
\boxed{
\text{challenge volume}
\neq
\text{challenge independence / coverage of the target failure path}
}
```

and:

```math
\boxed{
\text{validation result}
\not\Rightarrow
\text{independent discrimination of unexercised mechanisms}
}
```

### Result

```text
PASS
```

---

# 9. Witness I5 — later challenge changes the dependency topology and reproduces the failure

After the accident, simulations were performed using the SRI software with an environment containing the actual Ariane 501 trajectory data.

The inquiry record says these simulations reproduced the chain of events leading to failure.

Represent:

```text
POSTFLIGHT_SIMULATION(sim_post)
USES(sim_post,actual_SRI_software)
USES(sim_post,Ariane501_trajectory_data)
EXERCISES(sim_post,alignment_function)
REPRODUCES(sim_post,rho_failure_chain)
```

Compare with the earlier system test:

```text
REPLACES_WITH_SIMULATED_OUTPUT(sim_pre,SRI_behavior)
DOES_NOT_EXERCISE(sim_pre,actual_failure_chain)
```

The later challenge does not become magically independent in every sense.

It is more diagnostic **with respect to this failure path** because its relation topology now traverses the mechanism that the earlier tests omitted.

Thus:

```math
\boxed{
\text{challenge quality changes when dependency/coverage relations change}
}
```

without a primitive challenge-quality variable.

### Result

```text
PASS
```

---

# 10. Witness I6 — challenge independence is not the same as challenge disagreement

Two channels can agree because they share a cause.

Two channels can fail together because they share a cause.

Two channels can disagree while still sharing many assumptions.

Therefore AG/1 must not define independence as:

```text
outputs_differ(C1,C2)
```

or:

```text
outputs_agree(C1,C2)
```

The relevant source structure is dependency topology:

```text
DEPENDS_ON(C1,X)
DEPENDS_ON(C2,X)
```

plus the causal/failure relations earned by the record.

For Ariane 501:

```text
same software
+ same unprotected conversion
+ same exception-handling behavior
→ both SRI paths fail
```

This supports:

```math
\boxed{
\text{output agreement/disagreement}
\neq
\text{independence of generating paths}
}
```

### Result

```text
PASS
```

---

# 11. Hidden-parameter audit

The reconstruction does not use:

```text
independence bit
common-mode carrier
assumption object as a new architecture species
validation-state carrier
identifiability scalar
confounding scalar
challenge-quality scalar
coverage object
```

The following appear only as source-earned typed relations or representation content:

```text
DEPENDS_ON
BACKS_UP
HOT_STANDBY_FOR
IDENTICAL_SOFTWARE
DESIGNED_TO_COVER
NOT_COVERED_BY
REPLACES_WITH_SIMULATED_OUTPUT
DOES_NOT_EXERCISE
USES
EXERCISES
REPRODUCES
SAME_FAILURE_REASON
```

No unrestricted field such as:

```text
challenge.independence = false
validation.coverage = 0.6
system.common_mode = true
```

is used.

The hidden-parameter audit passes.

---

# 12. Failure search

T8 deliberately searched for missing structure at these edges:

```text
primary path + backup path
→ shared systematic dependency
→ simultaneous/common failure

random-failure coverage
→ systematic-failure noncoverage

system validation
→ simulated interface output
→ omitted internal failure mechanism

later diagnostic reproduction
→ changed challenge topology
→ failure mechanism exercised
```

None forces a new architecture primitive.

The strongest reconstruction is:

```math
\boxed{
\textbf{challenge independence is recoverable as a relative property of dependency topology, not as a primitive carrier, for this bounded corpus.}
}
```

More specifically:

```math
\boxed{
\textbf{a challenge is non-independent with respect to failure family }F
\textbf{ when the target and challenge retain a shared generating dependency relevant to }F.
}
```

This is a derived query over ordinary relations.

---

# 13. Verdict

```text
PASS
```

More precisely:

```math
\boxed{
\textbf{Transport 08 does not force an architectural primitive beyond frozen AG/1.}
}
```

The decisive T8 motif is:

```math
\boxed{
P\rightarrow X
\qquad
C\rightarrow X
\qquad
X\rightarrow F
\quad\Rightarrow\quad
\text{nominal challenge }C\text{ does not independently break failure path }F
}
```

where the implication is an analytic reconstruction over the relation graph rather than a new primitive assertion.

---

# 14. What this result does not establish

This PASS does not establish:

```text
AG/1 is universal.
all notions of statistical or causal independence reduce trivially to graph overlap.
all redundant systems fail when they share software.
all simulated validation is weak.
all common-mode failures are obvious from dependency graphs before failure.
Ariane 501 was caused only by redundancy design.
```

It establishes only:

```math
\boxed{
\textbf{this bounded common-mode challenge/validation corpus failed to force an addition to AG/1.}
}
```

---

# 15. Transport ledger after T8

```text
T1  software incident                                  PASS
T2  experimental science                               PASS
T3  shared evidence / competing analyses               PASS
T4  same observation / different worlds                PASS
T5  representation-driven causal loop                  PASS
T6  observation-topology modification                  PASS
T7  deliberate challenge selection                     PASS
T8  challenge independence / common-mode validation    PASS
```

The calibrated claim after this run is:

```math
\boxed{
\textbf{AG/1 has survived eight heterogeneous external reconstruction tests without architectural enlargement.}
}
```

This remains a bounded empirical transport claim, not a universality theorem.
