# AG/1 Transport Test 02 — OPERA Neutrino-Velocity Anomaly

**Protocol:** `transport/00_TRANSPORT_PROTOCOL_AG1.md`  
**Frozen architecture:** `abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md` (`AG/1`)  
**Test status:** COMPLETED  
**External-domain class:** experimental particle physics / metrology / scientific disagreement / revised measurement

---

# 1. Selection rationale

Transport 01 exercised software-incident history, operator error, diagnosis, and recovery.

Transport 02 is selected to attack `AG/1` from a different direction:

```text
measurement
→ numerical result + uncertainty
→ physical interpretation
→ explicit caution
→ independent contradictory measurement
→ candidate systematic effects
→ new discriminating measurements
→ revised interpretation / revised measurement
```

The intended pressure point is `REPRESENTATION`.

The corpus must preserve all of the following without adding a new primitive:

```math
\boxed{
\text{physical world relation}
\neq
\text{measurement result}
\neq
\text{interpretation of result}
\neq
\text{later competing measurement}
\neq
\text{later causal account of measurement error}
}
```

It must also represent scientific disagreement without introducing a `DISAGREEMENT` primitive.

This test is selected to make `AG/1` fail if measurement/interpretation structure requires a semantic carrier beyond `RELATION + REPRESENTATION`.

---

# 2. Bounded external corpus

This run uses four bounded scientific/public records.

## S1 — OPERA initial result, version 1

```text
The OPERA Collaboration
Measurement of the neutrino velocity with the OPERA detector in the CNGS beam
arXiv:1109.4897v1
submitted 22 September 2011
https://arxiv.org/abs/1109.4897v1
```

Source-level result:

```text
baseline ≈ 730 km
measured early arrival relative to light-speed expectation
δt = 60.7 ± 6.9(stat.) ± 7.4(sys.) ns
(v-c)/c = (2.48 ± 0.28(stat.) ± 0.30(sys.)) × 10^-5
```

## S2 — CERN chronology / public scientific update record

```text
OPERA experiment reports anomaly in flight time of neutrinos from CERN to Gran Sasso
CERN
original publication 23 September 2011
updates through 8 June 2012
https://home.cern/opera-experiment-reports-anomaly-in-flight-time-of-neutrinos-from-cern-to-gran-sasso/
```

This source preserves:

```text
initial anomaly announcement
explicit demand for independent measurement
November 2011 short-pulse cross-check
February 2012 candidate timing-system effects
March 2012 ICARUS disagreement
June 2012 four-experiment convergence
CERN retrospective attribution to faulty fibre-optic timing element
```

## S3 — independent ICARUS measurement

```text
ICARUS Collaboration
Measurement of the neutrino velocity with the ICARUS detector at the CNGS beam
arXiv:1203.3433
submitted 15 March 2012
https://arxiv.org/abs/1203.3433
```

Source-level result:

```text
7 beam-associated events
measured time of flight compatible with propagation at light speed
explicitly described as strikingly different from the OPERA report
```

## S4 — OPERA 2012 dedicated measurement

```text
The OPERA Collaboration
Measurement of the neutrino velocity with the OPERA detector in the CNGS beam using the 2012 dedicated data
arXiv:1212.1276
submitted 6 December 2012
https://arxiv.org/abs/1212.1276
```

Source-level result:

```text
upgraded timing setup
independent RPC-based timing system
δt_ν = 0.6 ± 0.4(stat.) ± 3.0(sys.) ns
δt_antiν = 1.7 ± 1.4(stat.) ± 3.1(sys.) ns
result compatible with light-speed propagation
confirms revised OPERA result with higher accuracy
```

Excluded from evidence for this run:

```text
popular-media commentary
retrospective textbook summaries
unbounded later literature
social-media reactions
outside theoretical critiques
```

The bounded corpus therefore contains experimental disagreement and revision without depending on later popular interpretation.

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

No new primitive may be introduced.

In particular, the following are forbidden as architecture additions:

```text
MEASUREMENT
OBSERVATION
HYPOTHESIS
UNCERTAINTY
DISAGREEMENT
EVIDENCE
EVENT
STATE
TIME
AGENT
CAUSE
```

as *new carriers*.

Source-earned predicates with those local meanings are allowed as ordinary typed `RELATION` instances.

---

# 4. Reconstruction principle for scientific measurement

A scientific measurement result must not be silently promoted to physical-world truth.

For example, the historical graph may contain:

```text
REPORTS_MEASUREMENT(OPERA_2011, rho_m1)
```

where the representation scope contains:

```text
BASELINE(CERN,LNGS,≈730,KM)
DELTA_T(neutrino_vs_light,60.7,NS)
STAT_UNCERTAINTY(delta_t,6.9,NS)
SYS_UNCERTAINTY(delta_t,7.4,NS)
RELATIVE_VELOCITY_DIFFERENCE(2.48e-5)
```

but:

```math
\boxed{
r\in content(\rho_{m1})
\not\Rightarrow
r\in\mathcal H_{physical}}
```

The historical fact earned by the corpus is that OPERA obtained/reported that result under a specified experimental system.

This is a direct use of the frozen assertion-scope distinction.

---

# 5. Witness S1 — result versus interpretation

The initial OPERA record reports a numerical early-arrival result.

CERN's September 2011 record says the result *appears* to indicate neutrino propagation roughly 20 parts per million above light speed, while simultaneously emphasizing the need for independent confirmation and refusing immediate strong physics conclusions.

Represent:

```text
rho_measurement_2011:
    DELTA_T = 60.7 ns early
    uncertainties = 6.9 stat / 7.4 sys ns

rho_interpretation_superluminal:
    NEUTRINO_SPEED > c

REPORTS_MEASUREMENT(OPERA,rho_measurement_2011)
APPEARS_TO_SUPPORT(rho_measurement_2011,rho_interpretation_superluminal)
REQUESTS_INDEPENDENT_TEST(OPERA/CERN,rho_measurement_2011)
```

The reconstruction preserves:

```math
\boxed{
\text{measured quantity}
\neq
\text{physical interpretation}
\neq
\text{confidence that interpretation is established}
}
```

No `HYPOTHESIS` or `MEASUREMENT` primitive is required.

### Result

```text
PASS
```

---

# 6. Witness S2 — successful cross-check does not certify the whole model

In November 2011 OPERA repeated the measurement with short beam pulses.

CERN records that this test confirmed the accuracy of one part of the timing measurement and ruled out one potential source of systematic error, while the anomaly still required further scrutiny and independent measurement.

Represent:

```text
TESTS(short_pulse_run,rho_systematic_candidate_1)
RESULT(short_pulse_run,rho_supports_timing_component)
RULES_OUT(short_pulse_run,rho_systematic_candidate_1)
```

while keeping:

```text
rho_anomaly
```

open to other explanations.

Thus:

```math
\boxed{
\text{one diagnostic test passes}
\neq
\text{entire interpretation certified}
}
```

This reconstructs without a special `EVIDENCE` or `VALIDATION` primitive.

### Result

```text
PASS
```

---

# 7. Witness S3 — candidate systematic effects with opposite directional consequences

In February 2012 OPERA reported two possible timing effects:

```text
oscillator effect
→ could overestimate neutrino time of flight

optical-fibre connector effect
→ could underestimate neutrino time of flight
```

Both required further testing.

Represent each as a distinct scoped causal possibility:

```text
rho_oscillator_effect:
    IF oscillator_effect
    → TOF estimate shifts in direction A

rho_fibre_effect:
    IF fibre_connector_effect
    → TOF estimate shifts in direction B
```

and:

```text
CONSIDERS(OPERA,rho_oscillator_effect)
CONSIDERS(OPERA,rho_fibre_effect)
REQUIRES_TEST(rho_oscillator_effect)
REQUIRES_TEST(rho_fibre_effect)
```

The architecture preserves competing causal models without asserting either as settled history.

### Result

```text
PASS
```

---

# 8. Witness S4 — inter-experiment disagreement

ICARUS measured seven neutrino events and reported a result compatible with propagation at the speed of light.

ICARUS explicitly characterized this as in striking difference with the OPERA report.

Represent:

```text
REPORTS_MEASUREMENT(OPERA,rho_opera_2011)
REPORTS_MEASUREMENT(ICARUS,rho_icarus_2012)

content(rho_opera_2011):
    DELTA_T ≈ +60 ns early

content(rho_icarus_2012):
    DELTA_T compatible with 0
```

The disagreement is reconstructible from incompatible content targeting the same physical quantity/baseline class.

A source-earned relation may also record:

```text
AT_ODDS_WITH(rho_icarus_2012,rho_opera_2011)
```

because CERN/ICARUS explicitly state that relationship.

No architecture primitive `DISAGREEMENT` is required.

### Decisive point

```math
\boxed{
R_{OPERA}(q)
\neq
R_{ICARUS}(q)
}
```

can coexist without contradiction because both are scoped scientific results/representations rather than unconditional physical-world assertions.

### Result

```text
PASS
```

---

# 9. Witness S5 — later evidence distinguishes competing representations

CERN's June 2012 update reports that Borexino, ICARUS, LVD, and OPERA all obtained neutrino time-of-flight results consistent with light speed.

The same update states that the original OPERA result can be attributed to a faulty element in the experiment's fibre-optic timing system.

Represent:

```text
REPORTS_MEASUREMENT(Borexino,rho_B)
REPORTS_MEASUREMENT(ICARUS,rho_I)
REPORTS_MEASUREMENT(LVD,rho_L)
REPORTS_MEASUREMENT(OPERA_2012,rho_O2)

CONSISTENT_WITH(rho_B,rho_c)
CONSISTENT_WITH(rho_I,rho_c)
CONSISTENT_WITH(rho_L,rho_c)
CONSISTENT_WITH(rho_O2,rho_c)

rho_later_causal_account:
    FAULTY_FIBRE_TIMING_ELEMENT
    → ORIGINAL_OPERA_ANOMALY

ATTRIBUTES(CERN_2012,rho_original_anomaly,rho_later_causal_account)
```

The later explanation targets the earlier measurement history without deleting it.

Thus:

```math
\boxed{
\text{earlier result occurred as a result/report}
\neq
\text{later account of why that result occurred}
}
```

This is exactly the retrospective-representation structure already reconstructible under `AG/1`.

### Result

```text
PASS
```

---

# 10. Witness S6 — same collaboration, revised measurement

The 2012 OPERA dedicated run used an upgraded setup and an independent timing system.

It found:

```text
δt_ν = 0.6 ± 0.4(stat.) ± 3.0(sys.) ns
δt_antiν = 1.7 ± 1.4(stat.) ± 3.1(sys.) ns
```

and reports compatibility with light-speed propagation.

Represent:

```text
REPORTS_MEASUREMENT(OPERA_2011,rho_O1)
REPORTS_MEASUREMENT(OPERA_2012,rho_O2)
BEFORE(rho_O1,rho_O2)
USES_SETUP(OPERA_2012,rho_upgraded_setup)
USES_INDEPENDENT_TIMING(OPERA_2012,rho_rpc_timing)
```

with incompatible/changed measured-content values kept in separate scopes.

No identity contradiction occurs:

```math
\boxed{
\text{same collaboration}
+
\text{different experimental configuration/history}
\rightarrow
\text{different reported result}
}
```

No primitive `REVISION` is required.

### Result

```text
PASS
```

---

# 11. Measurement versus world truth — strongest scientific-domain pressure

The most important transport result is not the disagreement itself.

It is that the scientific corpus forces three layers that must not collapse:

```text
1. historically performed experimental operation
2. scoped numerical measurement result
3. scoped physical interpretation of that result
```

A safe AG/1 reconstruction is:

```math
\boxed{
\text{experiment/history relation}
\rightarrow
\rho_{measurement}
\rightarrow
\rho_{interpretation}
}
```

where neither scoped content graph is automatically promoted to physical truth.

This preserves:

```math
\boxed{
\text{measurement}
\neq
\text{measured reality}
}
```

without requiring a third architecture primitive.

The distinction is represented through source provenance + assertion scope.

---

# 12. Hidden-parameter audit

The reconstruction does not use:

```text
state object
event carrier
time object
measurement carrier
hypothesis carrier
observation carrier
evidence object
disagreement bit
confidence object
scientific-truth flag
```

Scientific-specific vocabulary appears only as source-earned typed relations and scoped content, for example:

```text
REPORTS_MEASUREMENT
STAT_UNCERTAINTY
SYS_UNCERTAINTY
CONSISTENT_WITH
TESTS
RULES_OUT
ATTRIBUTES
USES_SETUP
AT_ODDS_WITH
```

These do not share an unrestricted hidden parameter that recreates a deleted primitive.

The audit therefore passes.

---

# 13. Failure search

The test deliberately searched for the following possible missing distinctions:

```text
measurement result versus world truth
uncertainty versus OPEN
competing investigator results
same target quantity under incompatible results
systematic-error hypothesis versus established cause
successful local cross-check versus global validation
revised interpretation without erasing prior result
same collaboration across changed apparatus/configuration
```

None forces a new primitive.

## Important distinction: explicit measurement uncertainty ≠ OPEN

Statistical/systematic uncertainty is source-provided quantitative relation content:

```text
STAT_UNCERTAINTY(...)
SYS_UNCERTAINTY(...)
```

`OPEN` remains reserved for an unforced architectural/source edge.

Therefore:

```math
\boxed{
\text{measurement uncertainty}
\neq
OPEN
}
```

No new uncertainty carrier is required.

---

# 14. Verdict

```text
PASS
```

More precisely:

```math
\boxed{
\textbf{Transport 02 does not force an architectural primitive beyond frozen AG/1.}
}
```

The strongest surviving scientific-domain reconstruction is:

```math
\boxed{
\textbf{historical experimental relations}
+
\textbf{scoped measurement/interpretation relations}
}
```

with independent provenance.

`RELATION + REPRESENTATION` is sufficient for this bounded corpus under the frozen protocol.

---

# 15. What this result does not establish

This PASS does not establish:

```text
AG/1 is universal.
AG/1 is mathematically minimal.
all scientific inference is reducible to OPERA-like structure.
measurement and interpretation are psychologically identical kinds of representation.
all scientific disagreement can be resolved by later experiments.
```

It establishes only:

```math
\boxed{
\textbf{this second, deliberately different external corpus failed to force an addition to AG/1.}
}
```

---

# 16. Transport ledger

```text
AG/1 frozen
    ↓
Transport 01 — GitLab 2017 database incident
    → PASS
    ↓
Transport 02 — OPERA neutrino-velocity experimental record
    → PASS
```

The two passes exercise substantially different domains:

```text
Transport 01:
operator model / destructive action / diagnosis / recovery

Transport 02:
measurement / uncertainty / physical interpretation / inter-experiment disagreement / systematic error / revised measurement
```

A transportability envelope is **not yet claimed**.

The next valid experiment should increase adversarial distance again rather than selecting another incident or another simple measurement-revision story.

---

# 17. Reopenability

If a later corpus requires a distinction that cannot be reconstructed from:

```text
provenance-bearing typed relation assertions
structured non-history assertion scopes
cross-scope reference
OPEN for genuinely unforced edges
```

without hidden-parameter tax evasion, record the smallest failure witness under the frozen protocol.

Do not modify `AG/1`.

Only accumulated external failure may motivate a separately versioned architecture proposal.
