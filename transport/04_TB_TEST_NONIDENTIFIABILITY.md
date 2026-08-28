# AG/1 Transport Test 04 — Same Representation / Different Worlds

**Protocol:** `transport/00_TRANSPORT_PROTOCOL_AG1.md`  
**Frozen architecture:** `abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md` (`AG/1`)  
**Prior milestone:** `transport/MILESTONE_T1_T3.md`  
**Test status:** COMPLETED  
**External-domain class:** biomedical diagnostics / measurement non-identifiability / independent discrimination

---

# 1. Selection rationale

Transport 01 tested:

```text
historical system state
≠ operator representation
```

Transport 02 tested:

```text
experimental operation
≠ measurement result
≠ physical interpretation
```

Transport 03 tested:

```math
D_{shared}\rightarrow\rho_A,
\qquad
D_{shared}\rightarrow\rho_B,
\qquad
\rho_A\neq\rho_B
```

Transport 04 changes the failure mode.

The target is:

```math
\boxed{
\textbf{same local observation / representation}
\quad\text{compatible with}\quad
\textbf{different underlying world histories}
}
```

The intended discriminator is interface non-identifiability:

```math
\boxed{
O(H_1)=O(H_2)
\quad\text{while}\quad
H_1\neq H_2
}
```

The test asks whether frozen `AG/1` can preserve this without adding new primitives such as:

```text
POSSIBLE_WORLD
LATENT_STATE
DIAGNOSIS
HYPOTHESIS
CAUSAL_MODEL
TEST_RESULT
```

---

# 2. Bounded external corpus

This run uses a bounded set of CDC tuberculosis testing guidance.

## S1 — CDC Clinical Testing Guidance: Tuberculin Skin Test

```text
Centers for Disease Control and Prevention
Clinical Testing Guidance for Tuberculosis: Tuberculin Skin Test
https://www.cdc.gov/tb/hcp/testing-diagnosis/tuberculin-skin-test.html
```

Source-level facts used:

```text
TB skin testing is used to detect immune reactivity associated with TB infection.
Previous BCG vaccination can cause a false-positive skin-test result.
Nontuberculous mycobacterial infection can also cause false-positive results.
Some persons may have a positive skin-test result even though they are not infected with TB bacteria.
There is no reliable way, using the skin-test reaction itself, to distinguish a BCG-caused positive reaction from a reaction caused by true TB infection.
```

## S2 — CDC BCG Vaccine for Tuberculosis

```text
Centers for Disease Control and Prevention
Bacille Calmette-Guérin (BCG) Vaccine for Tuberculosis
https://www.cdc.gov/tb/hcp/vaccines/index.html
```

Source-level facts used:

```text
BCG vaccination may cause a false-positive TB skin-test reaction.
There is no reliable way to distinguish BCG-caused positive skin-test reaction from true TB infection using that reaction alone.
TB blood tests are not made positive by BCG vaccination and are preferred for people who have received BCG.
```

## S3 — CDC Diagnosing Tuberculosis / Testing for Tuberculosis

```text
Centers for Disease Control and Prevention
Diagnosing Tuberculosis
https://www.cdc.gov/tb/testing/diagnosing-tuberculosis.html

Testing for Tuberculosis
https://www.cdc.gov/tb/testing/index.html
```

Source-level facts used:

```text
A positive TB infection test requires further evaluation.
Additional tests are used to determine whether a person has inactive TB infection or active TB disease.
Examples include chest radiography and sputum testing.
```

Excluded from evidence for this run:

```text
individual patient case reports
non-CDC clinical guidance
treatment recommendations
popular summaries
unbounded epidemiological literature
```

This is an architecture transport test, not patient-specific medical guidance.

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

No new architecture primitive may be introduced.

Source-earned local predicates remain allowed.

---

# 4. Reconstruction discipline — test result is not hidden-world truth

A performed skin test and its classified result are historical relations.

A compact reconstruction can use:

```text
PERFORMS_TST(test_instance,subject)
REPORTS_RESULT(test_instance,rho_TST_positive)
```

where:

```text
rho_TST_positive:
    CLASSIFIED_AS_POSITIVE(TST_reaction)
```

The critical rule is:

```math
\boxed{
POSITIVE\_TST
\not\Rightarrow
TB\_INFECTION\in\mathcal H
}
```

unless independent evidence earns the infection relation for the actual historical subject.

The test result is therefore scoped measurement/classification content, not automatic hidden-world truth.

---

# 5. Witness N1 — identical positive skin-test representation, different underlying worlds

The CDC explicitly states that a positive TB skin-test result may occur even when a person is not infected with TB bacteria.

Two source-supported world configurations are therefore possible relative to the same local test representation.

## World class H1 — true infection

```text
rho_H1:
    INFECTED_WITH(subject,M_tuberculosis)
    PRODUCES(subject,positive_TST_reaction)
```

## World class H2 — no TB infection + BCG-confounded reaction

```text
rho_H2:
    NOT_INFECTED_WITH(subject,M_tuberculosis)
    PREVIOUSLY_RECEIVED(subject,BCG)
    BCG_CAN_PRODUCE(subject,positive_TST_reaction)
```

The locally observed/classified representation can be identical:

```text
rho_obs:
    TST_RESULT = POSITIVE
```

Thus:

```math
\boxed{
O_{TST}(H_1)=O_{TST}(H_2)=\rho_{obs}
}
```

while:

```math
\boxed{
H_1\neq H_2
}
```

This is exactly the desired converse pressure:

```math
\boxed{
\text{same representation}
\not\Rightarrow
\text{same world}
}
```

### AG/1 reconstruction

The two world classes are represented as distinct structured hypothetical/diagnostic content scopes:

```text
COMPATIBLE_WITH(rho_obs,rho_H1)
COMPATIBLE_WITH(rho_obs,rho_H2)
```

The shared observation remains one representation scope.

No `POSSIBLE_WORLD` primitive is required because `REPRESENTATION` already supports non-historical structured relational content.

### Result

```text
PASS
```

---

# 6. Witness N2 — observation-level non-identifiability is explicit, not inferred

The source says there is no reliable way to distinguish a BCG-caused positive skin-test reaction from a reaction caused by true TB infection using the skin-test reaction itself.

This can be preserved as an ordinary relation over scoped alternatives:

```text
NOT_RELIABLY_DISTINGUISHABLE_BY(
    TST_reaction,
    rho_H1,
    rho_H2
)
```

or equivalently by preserving the source statement/provenance and withholding any discriminating edge.

The architectural point is:

```math
\boxed{
\text{non-identifiability}
\neq
\text{identity of worlds}
}
```

and:

```math
\boxed{
\text{same interface output}
\neq
\text{same generating process}
}
```

No `LATENT_STATE` or `IDENTIFIABILITY` carrier is required.

### Result

```text
PASS
```

---

# 7. Witness N3 — independent challenge channel changes distinguishability

CDC states that BCG vaccination does not induce positive TB blood-test results and that blood tests are preferred for people who have received BCG.

This gives a different measurement relation whose confounding structure is not identical to the skin test.

Represent:

```text
PERFORMS_IGRA(test2,subject)
REPORTS_RESULT(test2,rho_IGRA)

NOT_AFFECTED_BY(IGRA_result,BCG_vaccination)
```

The important architecture pattern is:

```math
\boxed{
O_1(H_1)=O_1(H_2)
}

\boxed{
O_2(H_1)\text{ and }O_2(H_2)
\text{ need not collapse for the same BCG reason}
}
```

The second channel therefore has discriminating value relative to the first channel's BCG confound.

AG/1 does not require an `INDEPENDENT_CHALLENGE_CHANNEL` primitive.

It preserves the different measurement relations and their different causal sensitivities.

### Important restraint

This test does **not** encode:

```text
IGRA perfectly resolves every positive-TST ambiguity.
```

The source only earns the narrower relation:

```text
BCG vaccination does not induce positive IGRA results.
```

Any remaining diagnostic uncertainty stays source-relative or OPEN.

### Result

```text
PASS
```

---

# 8. Witness N4 — same positive infection-test representation, different disease worlds

The CDC also requires a second non-identifiability layer.

After a positive TB infection test, further evaluation is used to determine whether the person has:

```text
inactive TB infection
```

or:

```text
active TB disease
```

Therefore the same broad infection-test representation:

```text
rho_infection_test_positive
```

is compatible with at least two clinically different structured world models:

```text
rho_inactive:
    TB_INFECTION(subject)
    INACTIVE_FORM(subject)

rho_active:
    TB_INFECTION(subject)
    ACTIVE_DISEASE(subject)
```

with:

```math
\boxed{
O_{infection\ test}(H_{inactive})
=
O_{infection\ test}(H_{active})
}
```

at the level of the positive infection-test classification.

Further relations such as chest-radiograph and sputum-test results can discriminate the active/inactive distinction.

Again:

```math
\boxed{
\text{same test representation}
\neq
\text{same underlying condition}
}
```

### Result

```text
PASS
```

---

# 9. Witness N5 — same representation can remain causally/operationally relevant before world resolution

A positive skin-test or blood-test result triggers further evaluation even though the result alone does not uniquely identify the downstream world classification.

Represent:

```text
REPORTS_RESULT(test,rho_positive)
LEADS_TO(rho_positive,rho_further_evaluation_plan)
```

while preserving:

```text
rho_H1
rho_H2
```

as unresolved/competing structured possibilities where the source leaves them unresolved.

Thus a representation can guide later action without uniquely identifying the world that generated it.

This survives with ordinary relations over representation scopes.

No `DIAGNOSIS`, `POLICY`, or `DECISION` primitive is needed in this bounded test.

### Result

```text
PASS
```

---

# 10. Hidden-parameter audit

The reconstruction does not use:

```text
possible_world_id
latent_state
hidden_state_vector
diagnosis object
hypothesis object
causal_model object
sensor_state object
test_result carrier
```

Allowed source-earned relation vocabulary includes:

```text
PERFORMS_TST
REPORTS_RESULT
INFECTED_WITH
PREVIOUSLY_RECEIVED
COMPATIBLE_WITH
NOT_RELIABLY_DISTINGUISHABLE_BY
PERFORMS_IGRA
NOT_AFFECTED_BY
LEADS_TO
```

The alternative world configurations are structured `REPRESENTATION` scopes, not new world-carrier objects.

The audit passes.

---

# 11. Failure search

Transport 04 deliberately searched for a missing distinction at the converse boundary:

```text
same positive representation + true infection
same positive representation + no infection / BCG confound
explicit inability of one interface to discriminate the generating worlds
second measurement channel with different confounding structure
same positive infection test + inactive infection
same positive infection test + active disease
representation guiding action before hidden-world resolution
```

None forces a new primitive.

The strongest result is:

```math
\boxed{
\textbf{AG/1 can preserve observational equivalence without collapsing causal/world identity.}
}
```

Formally:

```math
\boxed{
O(H_1)=O(H_2)
\quad\not\Rightarrow\quad
H_1=H_2
}
```

because the shared observation is one scoped relational representation while the incompatible generating histories remain distinct scoped relational structures.

---

# 12. Verdict

```text
PASS
```

More precisely:

```math
\boxed{
\textbf{Transport 04 does not force an architectural primitive beyond frozen AG/1.}
}
```

The decisive surviving reconstruction is:

```math
\boxed{
\textbf{same local representation}
\rightarrow
\textbf{multiple compatible world models}
\rightarrow
\textbf{independent discriminating relation/channel}
}
```

without introducing `POSSIBLE_WORLD`, `LATENT_STATE`, `DIAGNOSIS`, or `CAUSAL_MODEL` as architecture species.

---

# 13. Important limitation

This corpus supplies source-certified **world classes / diagnostic possibilities**, not two fully narrated individual patient histories with every relation instantiated.

Therefore T4 establishes the architecture's ability to reconstruct a documented non-identifiability relation:

```math
O(H_1)=O(H_2),\ H_1\neq H_2
```

at the class/model level.

A later transport test may strengthen this by using paired fully observed cases that produce the same model/sensor output under different realized histories.

This limitation does not change the PASS verdict for the bounded reconstruction attempted here.

---

# 14. Updated transport ledger

```text
AG/1 frozen
    ↓
T1 — GitLab software incident
    PASS
    ↓
T2 — OPERA / ICARUS experimental science
    PASS
    ↓
T3 — Challenger same evidence / competing analyses
    PASS
    ↓
T4 — TB testing non-identifiability
    PASS
```

The calibrated cumulative claim is now:

```math
\boxed{
\textbf{AG/1 has survived four heterogeneous external reconstruction tests without architectural enlargement, including both directions of world/model non-equivalence tested so far.}
}
```

Those directions are:

```math
\boxed{
\text{same evidence}\rightarrow\text{different representations}
}

and:

```math
\boxed{
\text{same representation}\rightarrow\text{different compatible worlds}
}
```

This still does not establish universality or a complete transportability envelope.

---

# 15. Next unopened pressure

The next orthogonal boundary remains:

```math
\boxed{
\rho
\rightarrow
\text{action/intervention}
\rightarrow
\mathcal H'
\rightarrow
\text{new observation}
\rightarrow
\rho'
}
```

where a representation is not only about history but causally participates in changing the world later observed.

That pressure is intentionally left for a separate frozen transport run.
