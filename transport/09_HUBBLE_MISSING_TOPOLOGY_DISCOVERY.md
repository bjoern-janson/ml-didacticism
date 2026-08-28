# AG/1 Transport Test 09 — Discovery of Previously Unrepresented Topology / Hubble Optical Failure

**Protocol:** `transport/00_TRANSPORT_PROTOCOL_AG1.md`  
**Frozen architecture:** `abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md` (`AG/1`)  
**Prior milestone:** `transport/MILESTONE_T1_T8.md`  
**Test status:** COMPLETED  
**External-domain class:** precision optical metrology / hidden apparatus dependency / anomalous observation / topology discovery / retrospective reconstruction

---

# 1. Selection rationale

Transport 08 established that a **known** shared dependency can be represented as ordinary relation topology:

```math
\boxed{
P\rightarrow X,
\qquad
C\rightarrow X,
\qquad
X\rightarrow F
}
```

Transport 09 attacks the next boundary:

```math
\boxed{\textbf{discovery of a dependency that was not previously represented}}
```

The target is not:

```text
known variable
→ new value
```

but:

```text
prior representation lacks relation X
→ unexpected observation
→ investigation
→ source-supported relation X is introduced
→ revised topology explains old and new evidence
```

Formally:

```math
\boxed{
X\notin content(\rho_t)
\qquad\text{and later}\qquad
X\in content(\rho_{t+1})
}
```

where `X` is a relation/dependency rather than merely a scalar parameter update.

The architecture must attempt to reconstruct this using only:

```math
\boxed{RELATION + REPRESENTATION + SOURCE\_PROVENANCE + OPEN}
```

without adding:

```text
STRUCTURAL_NOVELTY
INTERFACE_INVENTION
RELATION_DISCOVERY
ONTOLOGY_CHANGE
MODEL_EXPANSION
```

as architecture primitives.

---

# 2. Bounded external corpus

This run uses NASA's Hubble Space Telescope optical-failure investigation record and NASA historical summaries.

## S1 — Hubble Space Telescope Optical Systems Failure Report

```text
Hubble Space Telescope Optical Systems Board of Investigation
The Hubble Space Telescope Optical Systems Failure Report
NASA-TM-103443
November 1990
NASA Technical Reports Server
https://ntrs.nasa.gov/citations/19910003124
```

Source-level facts used:

```text
Hubble's primary mirror was manufactured to the wrong figure and produced spherical aberration on orbit.
The critical reflective null corrector (RNC) used as the template/test apparatus was preserved after fabrication.
Post-launch investigation measured the RNC and found its lens incorrectly spaced from its mirrors.
The measured spacing error was 1.3 mm.
Calculations showed that this spacing error accounted in detail for the magnitude and character of the observed image blurring.
No verification of the RNC dimensions had been carried out after original assembly.
Auxiliary tests had shown indications of the error during fabrication.
An inverse null corrector showed the RNC error.
A second/refractive null corrector showed error in the primary mirror.
Those discrepant indicators were discounted as flawed.
The fabrication plan relied on the RNC as the precision reference for both manufacture and verification.
```

## S2 — NASA Science: Hubble's Mirror Flaw

```text
NASA Science
Hubble's Mirror Flaw
https://science.nasa.gov/mission/hubble/observatory/design/optics/hubbles-mirror-flaw/
```

Source-level facts used:

```text
after launch, both imaging cameras showed the characteristic spherical-aberration distortion;
NASA formed an investigation board;
the contractors had improperly set up the null corrector;
the later investigation traced the wrong mirror shape to the 1.3 mm lens-spacing error in that device.
```

## S3 — NASA historical reconstruction of the null-corrector assembly

```text
NASA historical study of Hubble operations
Not Yet Imagined: A Study of Hubble Space Telescope Operations
NASA History
```

Source-level facts used:

```text
the null-corrector alignment process used a laser and metering rod/cap arrangement;
a reflective path associated with the cap contributed to the incorrect setup;
technicians introduced washer spacers and displaced the lens by about 1.3 mm;
the erroneous null corrector was then used to guide the polishing of the primary mirror;
later independent/auxiliary test results disagreed with the trusted RNC result and were dismissed.
```

Excluded from evidence for this run:

```text
modern optical-design textbooks
popular retellings not grounded in NASA records
later Hubble servicing history except where needed to distinguish diagnosis from correction
unbounded management commentary
```

This is an architecture transport test, not a complete organizational history of the Hubble programme.

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

No structural-novelty carrier may be added.

---

# 4. Reconstruction principle — topology novelty is a difference between scoped relation graphs

Let:

```text
rho_pre
```

be the pre-launch operative representation of the mirror/test system.

Let:

```text
rho_post
```

be the post-investigation causal representation.

A newly represented relation `x` is structurally novel relative to `rho_pre` when:

```math
\boxed{
x\notin content(\rho_{pre})
\quad\land\quad
x\in content(\rho_{post})
}
```

without requiring:

```text
x was explicitly represented false in rho_pre
```

The distinction is therefore:

```math
\boxed{
\text{absent from prior representation}
\neq
\text{negated in prior representation}
}
```

A derived novelty view may be:

```math
\boxed{
NewRelations(\rho_{pre},\rho_{post})
:=
content(\rho_{post})\setminus content(\rho_{pre})
}
```

subject to provenance and scope matching.

No primitive `NOVELTY` bit is required.

The kill test is whether the Hubble record requires some semantic residue beyond this graph difference plus the historical investigation relations that produced the later representation.

---

# 5. Witness N1 — pre-launch operative model lacks the later discovered RNC spacing relation

The operative manufacturing/test representation treated the reflective null corrector as the precision reference against which the primary mirror was shaped and verified.

A compact pre-launch scope is:

```text
rho_pre:
    RNC serves as precision reference for primary-mirror figure
    RNC output indicates mirror meets required surface specification
```

The later source-supported relation:

```text
LENS_SPACING_ERROR(RNC,1.3,MM)
```

is not part of that operative representation.

It would be incorrect to encode the pre-launch state as:

```text
NOT LENS_SPACING_ERROR(RNC,1.3,MM)
```

unless a source explicitly represented that negation.

The safe distinction is:

```math
\boxed{
LENS\_SPACING\_ERROR(RNC,1.3mm)
\notin content(\rho_{pre})
}
```

while later:

```math
\boxed{
LENS\_SPACING\_ERROR(RNC,1.3mm)
\in content(\rho_{post})
}
```

### Result

```text
PASS
```

AG/1 can encode the structural transition without an ontology-change primitive.

---

# 6. Witness N2 — anomalous world observation pressures the prior topology without itself naming the missing edge

After launch, Hubble's cameras produced blurred images with a characteristic spherical aberration.

Historical relations include:

```text
OBSERVES_ON_ORBIT(Hubble,rho_blurred_images)
CHARACTERISTIC_OF(rho_blurred_images,rho_spherical_aberration)
```

The anomalous observation does not itself contain:

```text
RNC lens was mis-spaced by 1.3 mm
```

Therefore:

```math
\boxed{
\text{prediction/expectation failure}
\neq
\text{identified missing mechanism}
}
```

The observation only forces pressure on the earlier representation:

```text
CONFLICTS_WITH(rho_blurred_images,rho_expected_optical_performance)
```

The causal edge is earned only later through investigation.

### Result

```text
PASS
```

This prevents the architecture from equating error detection with cause discovery.

---

# 7. Witness N3 — investigation introduces a new apparatus-internal relation

The investigation remeasured the preserved reflective null corrector and found that the lens was incorrectly spaced from the mirrors.

Represent historical investigation relations:

```text
INSPECTS(board,RNC)
MEASURES(board,RNC_lens_spacing,rho_spacing_measurement)
DERIVES(board,rho_spacing_measurement,rho_RNC_error)
```

with:

```text
rho_RNC_error:
    LENS_SPACING_ERROR(RNC,1.3,MM)
```

The new relation is now present in the post-investigation representation:

```math
\boxed{
LENS\_SPACING\_ERROR(RNC,1.3mm)
\in content(\rho_{post})
}
```

The architecture needs no primitive saying:

```text
DISCOVERED_NEW_RELATION = true
```

The discovery motif is reconstructible from:

```text
prior scope lacks x
investigation occurs
source-supported x enters later scope
```

### Result

```text
PASS
```

---

# 8. Witness N4 — the newly represented relation explains both apparatus behavior and mirror error

The Board calculated that the measured 1.3 mm RNC spacing error accounts for the magnitude and character of Hubble's observed spherical aberration.

Represent:

```text
CAUSES_OR_PRODUCES(
    rho_RNC_spacing_error,
    rho_wrong_polishing_reference
)

GUIDES(
    RNC_output,
    primary_mirror_polishing
)

RESULTS_IN(
    rho_wrong_polishing_reference,
    rho_wrong_primary_mirror_figure
)

EXPLAINS(
    rho_wrong_primary_mirror_figure,
    rho_on_orbit_spherical_aberration
)
```

where each causal-strength relation is only asserted to the degree earned by the Board's findings.

Thus the later graph does more than add a disconnected fact.

It introduces a relation that reconnects:

```text
test apparatus
→ measurement/reference output
→ manufacturing action
→ mirror figure
→ on-orbit observation
```

This is genuine topology expansion in the representation.

### Result

```text
PASS
```

---

# 9. Witness N5 — deeper investigation can add relations beneath the first discovered relation

NASA's historical reconstruction goes deeper than the abstract spacing error.

It reconstructs an assembly/alignment sequence involving the metering-rod/cap optical path and subsequent spacer/washer adjustment that displaced the null-corrector lens.

A later, more detailed scope may therefore add relations such as:

```text
LASER_REFLECTS_FROM(alignment_beam,protective_cap_surface)
MISIDENTIFIES_REFERENCE_PATH(setup_process,cap_vs_metering_rod)
ADDS_SPACERS(technicians,RNC_assembly)
DISPLACES(spacers,RNC_lens,1.3,MM)
```

only where the bounded source earns them.

This yields nested structural revision:

```math
\boxed{
\rho_{pre}
\subsetneq
\rho_{post1}
\subsetneq
\rho_{post2}
}
```

in relation content, without claiming every later representation is globally truer in every dimension.

The architecture can therefore represent successive discovery of deeper topology using the same two primitives.

### Result

```text
PASS
```

---

# 10. Witness N6 — earlier discrepant evidence existed without the missing relation being integrated

The Inquiry Board found that auxiliary optical tests had already indicated the problem during fabrication.

An inverse null corrector showed the error in the reflective null corrector.

A second/refractive null corrector also showed an error in the finished primary mirror.

Those indicators were discounted as flaws in the auxiliary tests.

Represent:

```text
REPORTS_RESULT(inverse_null_test,rho_discrepancy_A)
REPORTS_RESULT(refractive_null_test,rho_discrepancy_B)

CONFLICTS_WITH(rho_discrepancy_A,rho_RNC_trusted_result)
CONFLICTS_WITH(rho_discrepancy_B,rho_RNC_trusted_result)

DISCOUNTS(actor_group,rho_discrepancy_A,rho_auxiliary_test_flawed)
DISCOUNTS(actor_group,rho_discrepancy_B,rho_auxiliary_test_flawed)
```

The important negative result is:

```math
\boxed{
\text{contradictory evidence available}
\not\Rightarrow
\text{missing topology discovered}
}
```

This is a stronger version of the T5/T6 lesson.

The evidence existed, but the operative representation did not acquire the correct RNC-dependency relation.

### Result

```text
PASS
```

---

# 11. Witness N7 — structural discovery is not merely a parameter update

A simple parameter update would look like:

```text
known relation:
    LENS_SPACING(RNC,d)

update:
    d = d_new
```

But the historically relevant pre-launch representation need not contain the failure relation:

```text
RNC internal spacing error
→ biased optical reference
→ wrong mirror polishing
```

The later investigation adds the dependency chain itself.

Therefore T9 preserves:

```math
\boxed{
\text{new value on known edge}
\neq
\text{newly represented edge/dependency chain}
}
```

AG/1 handles both because representation content is a relation graph whose membership can change across scopes.

No architecture species is required to distinguish value revision from graph expansion.

### Result

```text
PASS
```

---

# 12. Witness N8 — the architecture does not guarantee discovery

The Hubble record itself proves that discrepancy can persist without successful structural revision.

Before launch:

```text
auxiliary tests disagree
→ discrepancy discounted
→ operative topology remains unchanged
```

Only after the on-orbit anomaly and dedicated investigation was the RNC spacing relation integrated into the accepted causal account.

Therefore AG/1 must preserve:

```math
\boxed{
\text{missing relation}
+\text{contradictory evidence}
\not\Rightarrow
\text{automatic topology invention}
}
```

There is no built-in rule:

```text
prediction failure → discover correct hidden edge
```

The actual discovery requires source-earned investigation, measurement, derivation, and later representation relations.

### Result

```text
PASS
```

---

# 13. Hidden-parameter audit

The reconstruction does not use:

```text
novelty bit
interface-invention carrier
ontology-change state
relation-discovery primitive
model-expansion mode
latent-topology object
```

The following appear only as source-earned typed relations or derived graph comparisons:

```text
INSPECTS
MEASURES
DERIVES
CONFLICTS_WITH
DISCOUNTS
EXPLAINS
GUIDES
RESULTS_IN
LENS_SPACING_ERROR
LASER_REFLECTS_FROM
ADDS_SPACERS
DISPLACES
NewRelations(rho_pre,rho_post)
```

No unrestricted field such as:

```text
representation.has_structural_novelty = true
model.ontology_version += 1
relation.discovery_status = novel
```

is used.

The hidden-parameter audit passes.

---

# 14. Failure search

T9 deliberately searched for missing structure at these edges:

```text
trusted measurement model
→ anomalous world observation
→ contradiction without identified cause

pre-existing discrepant auxiliary evidence
→ failure to integrate missing relation

post-anomaly investigation
→ newly measured apparatus relation
→ causal reconnection of test apparatus, manufacturing action, and observed failure

first discovered relation
→ deeper later causal relations

prior relation graph
→ later relation graph with new membership
```

None forces a new architecture primitive.

The strongest reconstruction is:

```math
\boxed{
\textbf{structural novelty is representable as provenance-bearing relation content that is absent from an earlier representation scope and present in a later one, together with historical relations describing the investigation that earned the addition.}
}
```

and:

```math
\boxed{
\textbf{discovery of a missing graph edge is a transition between representation graphs, not a primitive carrier, for this bounded corpus.}
}
```

---

# 15. Verdict

```text
PASS
```

More precisely:

```math
\boxed{
\textbf{Transport 09 does not force an architectural primitive beyond frozen AG/1.}
}
```

The decisive T9 motif is:

```math
\boxed{
X\notin content(\rho_t)
\rightarrow
unexpected\ evidence
\rightarrow
investigation
\rightarrow
X\in content(\rho_{t+1})
}
```

with `X` a newly represented relation/dependency rather than merely a changed scalar value.

---

# 16. What this result does not establish

This PASS does not establish:

```text
AG/1 is universal.
all structural novelty is discoverable.
all interface invention reduces trivially to adding graph edges.
all anomalous evidence tells investigators what relation is missing.
all later causal reconstructions are uniquely correct.
Hubble's failure was caused only by one technical relation.
any autonomous learner can generate the missing relation without external/source support.
```

The last restriction is critical.

This transport test shows that AG/1 can **represent the historical transition in which a previously absent relation becomes represented**.

It does **not** yet show that a learner operating only over its current representation can autonomously invent the correct new relation without the source/investigation supplying it.

That stronger generative problem remains open.

---

# 17. Transport ledger after T9

```text
T1  software incident                                  PASS
T2  experimental science                               PASS
T3  shared evidence / competing analyses               PASS
T4  same observation / different worlds                PASS
T5  representation-driven causal loop                  PASS
T6  observation-topology modification                  PASS
T7  deliberate challenge selection                     PASS
T8  challenge independence / common-mode validation    PASS
T9  discovery of previously unrepresented topology     PASS
```

The calibrated claim after this run is:

```math
\boxed{
\textbf{AG/1 has survived nine heterogeneous external reconstruction tests without architectural enlargement.}
}
```

This remains a bounded empirical transport claim, not a universality theorem.

The open frontier is now narrower than T9:

```math
\boxed{
\textbf{Can a system generate a missing distinction from contradiction without the correct new relation being supplied by an external source or later investigator?}
}
```

That is no longer merely representation of structural discovery.

It is autonomous structural invention.
