# AG/1 Transport Test 05 — Closed-Loop Representation / Mars Climate Orbiter

**Protocol:** `transport/00_TRANSPORT_PROTOCOL_AG1.md`  
**Frozen architecture:** `abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md` (`AG/1`)  
**Prior milestone:** `transport/MILESTONE_T1_T4.md`  
**Test status:** COMPLETED  
**External-domain class:** spacecraft navigation / closed-loop control / erroneous model / intervention / revised causal representation

---

# 1. Selection rationale

Transport 01–04 pressured world/model separation but did not yet require the complete loop:

```math
\boxed{
\rho_t
\rightarrow
a_t
\rightarrow
\mathcal H_{t+1}
\rightarrow
o_{t+1}
\rightarrow
\rho_{t+1}
}
```

Transport 05 is selected to test whether a representation can enter the causal history through action, alter the subsequently observed world, and then be revised from consequences without adding a new architecture primitive.

The adversarial target is:

```math
\boxed{
\text{materially incorrect/incomplete representation}
\rightarrow
\text{real intervention}
\rightarrow
\text{real changed trajectory}
\rightarrow
\text{new tracking evidence}
\rightarrow
\text{revised representation}
}
```

The architecture must preserve:

```text
represented trajectory
≠
computed corrective action
≠
executed maneuver
≠
actual resulting trajectory
≠
tracking measurement
≠
later causal account
```

without introducing:

```text
POLICY
DECISION
CONTROL
ACTION_MODEL
WORLD_STATE
BELIEF_STATE
FEEDBACK_STATE
```

as new carriers.

---

# 2. Bounded external corpus

This run uses NASA/JPL records concerning the 1999 Mars Climate Orbiter mishap.

## S1 — Mars Climate Orbiter Mishap Investigation Board, Phase II report

```text
Report on Project Management in NASA
Mars Climate Orbiter Mishap Investigation Board
March 13, 2000
https://discovery.larc.nasa.gov/discovery/PDF_FILES/mars_climate_orbiter_phaseII.pdf
```

The report includes the Phase I mishap material in its appendix and records:

```text
navigation-solution discrepancies during spring/summer 1999
expected versus observed Doppler residuals from AMD events
unresolved disagreement among orbit-determination methods
TCM-4 computed September 8
TCM-4 executed September 15
post-TCM-4 estimated periapse decreasing to 150–170 km
more accurate tracking about one hour before insertion indicating as low as 110 km
loss of signal during Mars orbit insertion
post-loss discovery that small-force ΔV data were low by factor 4.45
root cause: English-unit data supplied where Newton-seconds were specified/expected
```

The report also records that the navigation software underestimated the effects of thruster firings by factor 4.45 and therefore computed an erroneous trajectory.

## S2 — NASA Software Engineering Handbook / Lessons Learned

```text
Mars Climate Orbiter Mishap Investigation Board lesson summary
NASA Software Engineering Handbook
https://swehb.nasa.gov/spaces/7150/pages/16449723/SWE-017+-+Project+and+Software+Training
```

This source independently summarizes:

```text
root cause = failure to use metric units in ground Small Forces software
trajectory modelers assumed the AMD data met the metric interface requirement
undetected mismodeling of spacecraft velocity changes
TCM-5 not performed as contributing cause
```

## S3 — NASA/JPL mission and immediate-loss records

```text
Mars Climate Orbiter — NASA Science
https://science.nasa.gov/mission/mars-climate-orbiter/

NASA's Mars Climate Orbiter Believed to be Lost — JPL
https://www.jpl.nasa.gov/news/nasas-mars-climate-orbiter-believed-to-be-lost/

Mars Climate Orbiter Team Finds Likely Cause of Loss — JPL
https://www.jpl.nasa.gov/news/mars-climate-orbiter-team-finds-likely-cause-of-loss/
```

These sources preserve the mission-level loss and the later unit-conversion causal attribution.

Excluded from evidence for this run:

```text
popular retellings
non-NASA case studies
post-hoc management analogies
unbounded engineering literature
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

Source-earned local relation predicates are permitted.

No new carrier may be introduced.

---

# 4. Witness L1 — materially wrong navigation representation

The mission's ground navigation processing consumed AMD small-force data that were required/expected to be in Newton-seconds but were actually supplied in pound-force-seconds.

The report says subsequent processing underestimated the effect of thruster firings on the spacecraft trajectory by factor 4.45 and computed an erroneous trajectory.

Represent the source fact that the navigation system generated an estimate as history:

```text
COMPUTES_NAVIGATION_SOLUTION(ground_navigation,rho_nav_t)
```

with scoped content:

```text
rho_nav_t:
    ESTIMATED_DELTA_V(AMD_effect,underestimated)
    ESTIMATED_TRAJECTORY(MCO,trajectory_t)
```

The actual trajectory is **not** asserted by the internal content of `rho_nav_t`.

Thus:

```math
\boxed{
content(\rho_{nav_t})
\not\Rightarrow
\mathcal H_{trajectory}
}
```

### Result

```text
PASS
```

AG/1 preserves an operationally active but materially inaccurate world model without confusing it with the spacecraft's actual history.

---

# 5. Witness L2 — representation participates in intervention selection

On September 8, TCM-4 was computed as the final planned interplanetary trajectory-correction maneuver.

Its represented purpose/effect was to adjust the trajectory so that the first post-insertion periapse would be about 226 km. TCM-4 was executed on September 15.

Represent:

```text
rho_target:
    FIRST_PERIAPSE ≈ 226 km

COMPUTES_MANEUVER(
    navigation_team,
    rho_nav_pre_TCM4,
    rho_target,
    maneuver_TCM4
)

EXECUTES(MCO,maneuver_TCM4)
```

The exact internal algorithmic mapping from the navigation solution to the maneuver need not become an architecture primitive.

Where the report does not expose a finer causal edge, it remains provenance-bounded / OPEN rather than invented.

The key structure is source-earned:

```math
\boxed{
\text{represented trajectory/target}
\rightarrow
\text{computed correction}
\rightarrow
\text{executed physical maneuver}
}
```

### Result

```text
PASS
```

`POLICY`, `DECISION`, and `CONTROL` are not required as carriers. The action-selection relation is ordinary typed incidence over representation scopes and a maneuver occurrence.

---

# 6. Witness L3 — executed action changes history without validating the model

TCM-4 was physically executed.

Afterward, orbit-determination processing indicated that first periapse had decreased into the 150–170 km range; more accurate tracking during the final approach produced an estimate as low as 110 km.

The architecture must not infer:

```text
TCM-4 executed
→ prior model was correct
```

Represent:

```text
EXECUTES(MCO,maneuver_TCM4)
BEFORE(maneuver_TCM4,rho_nav_post_TCM4)

rho_nav_post_TCM4:
    ESTIMATED_FIRST_PERIAPSE = 150–170 km

rho_nav_final_pre_MOI:
    ESTIMATED_FIRST_PERIAPSE ≈ 110 km
```

The represented trajectory evolves after the intervention.

Thus:

```math
\boxed{
\rho_{nav,pre}
\neq
\rho_{nav,post}
}
```

while the historical spacecraft trajectory has also been altered by executed thruster/maneuver relations.

### Result

```text
PASS
```

Representation and history both change, but they remain distinct objects of assertion.

---

# 7. Witness L4 — new evidence does not automatically force correct revision

The report records that throughout spring and summer 1999 there were discrepancies among navigation solutions and residuals between expected and observed Doppler signatures of the more frequent AMD events.

Doppler-only solutions consistently indicated insertion closer to Mars.

These discrepancies were not resolved.

Represent:

```text
REPORTS_RESIDUAL(tracking,rho_doppler_residual)
INDICATES(rho_doppler_only,rho_closer_path)
CONFLICTS_WITH(rho_doppler_only,rho_prime_navigation)
UNRESOLVED(rho_navigation_discrepancy)
```

or preserve the unresolved relationship through source relations + `OPEN` where a stronger causal update is not earned.

The important result is:

```math
\boxed{
\text{new evidence available}
\not\Rightarrow
\text{correct representation immediately acquired}
}
```

No update-rule primitive is required.

### Result

```text
PASS
```

This prevents the closed loop from becoming an unrealistically perfect Bayesian controller merely because feedback exists.

---

# 8. Witness L5 — actual consequence outruns the operative representation

Mars orbit insertion began on September 23.

Signal loss occurred 49 seconds earlier than predicted and the signal was never reacquired.

The later investigation reconstructed that the actual trajectory passed far lower than intended/estimated and that the unit mismatch had driven the trajectory-estimation error.

Represent history:

```text
BEGINS(MCO,MOI_burn)
LOSES_SIGNAL(MCO)
NOT_REACQUIRED(MCO_signal)
```

and later scoped reconstruction:

```text
rho_mishap_account:
    AMD_INPUT_UNITS = lbf-s
    REQUIRED_UNITS = N-s
    UNDERMODELS_DELTA_V_BY = 4.45
    COMPUTES_ERRONEOUS_TRAJECTORY
    ACTUAL_CLOSE_APPROACH << intended_close_approach
```

with:

```text
ATTRIBUTES(MIB,rho_loss,rho_mishap_account)
```

The later representation targets the earlier history without replacing the earlier operational model.

Thus:

```math
\boxed{
\rho_{nav,t}
\neq
\mathcal H_{t+1}
\neq
\rho_{MIB,later}
}
```

### Result

```text
PASS
```

---

# 9. Witness L6 — the causal loop closes without a FEEDBACK primitive

The bounded corpus supports the following abstract reconstruction:

```math
\boxed{
\rho_{nav,t}
\rightarrow
\text{COMPUTES}(TCM4)
\rightarrow
\text{EXECUTES}(TCM4)
\rightarrow
\mathcal H_{trajectory,t+1}
\rightarrow
\rho_{tracking,t+1}
\rightarrow
\rho_{nav,t+1}
}
```

and ultimately:

```math
\boxed{
\rho_{loss/investigation}
\rightarrow
\rho_{revised\ causal\ account}
}
```

No primitive `FEEDBACK` object is necessary.

The loop is a motif over relations connecting historical actions, measurements, and representation scopes.

### Result

```text
PASS
```

---

# 10. Strong adversarial discriminator — wrong representation can have real causal consequences

The most important T5 result is:

```math
\boxed{
\textbf{a false or materially inaccurate representation can participate in a real action-selection chain and thereby alter later history.}
}
```

This does **not** mean the representation itself physically moves the spacecraft.

The source-supported chain is mediated:

```text
navigation representation
→ maneuver computation / operational decision relation
→ spacecraft command/execution
→ changed trajectory
```

Therefore:

```math
\boxed{
\text{representation is causally relevant through historical relations}
\neq
\text{representation is identical to physical cause}
}
```

AG/1 preserves this without a new causal-operator carrier.

---

# 11. Non-retroactivity test

The later mishap account does not rewrite the earlier navigation representation as though the navigation team had already known the unit mismatch.

Keep:

```text
AT t:
    rho_nav_t = operational estimate under assumed metric interface

LATER:
    rho_MIB = unit mismatch + under-modeled ΔV + erroneous trajectory account
```

Therefore:

```math
\boxed{
\rho_t
\neq
\rho_{later}
}
```

and:

```math
\boxed{
\text{later correctness}
\neq
\text{earlier possession of that representation}
}
```

### Result

```text
PASS
```

This is the causal analogue of preserving retrospective meaning without event erasure.

---

# 12. Hidden-parameter audit

The reconstruction does **not** introduce:

```text
POLICY object
DECISION object
CONTROL_STATE
FEEDBACK_STATE
WORLD_STATE
ACTION_MODEL
BELIEF_STATE
EVENT carrier
TIME carrier
AGENT carrier
CAUSAL_MODEL carrier
```

The following are source-earned typed relation vocabulary:

```text
COMPUTES_NAVIGATION_SOLUTION
COMPUTES_MANEUVER
EXECUTES
ESTIMATES
REPORTS_RESIDUAL
INDICATES
CONFLICTS_WITH
LOSES_SIGNAL
ATTRIBUTES
BEFORE
```

The architecture does not contain a free field such as:

```text
representation.policy = ...
relation.control_state = ...
representation.feedback_update = ...
```

The hidden-parameter audit passes.

---

# 13. Failure search

T5 deliberately searched for failure at:

```text
representation influencing action selection
action changing the represented world
same representation not being validated by successful execution
new evidence arriving after intervention
feedback failing to produce immediate correct revision
later causal reconstruction
non-retroactive preservation of the earlier wrong model
```

None forces a new primitive.

The strongest recovered loop is:

```math
\boxed{
\textbf{scoped representation}
\rightarrow
\textbf{typed historical action relations}
\rightarrow
\textbf{changed relational history}
\rightarrow
\textbf{new scoped representation}
}
```

---

# 14. Verdict

```text
PASS
```

More precisely:

```math
\boxed{
\textbf{Transport 05 does not force an architectural primitive beyond frozen AG/1.}
}
```

AG/1 can reconstruct an epistemic/control loop in which:

```text
model is materially wrong
→ model participates in intervention computation
→ intervention is physically executed
→ world trajectory changes
→ new evidence arrives
→ representation changes
→ later investigation supplies a revised causal account
```

without adding a policy, decision, control, feedback, or action-model primitive.

---

# 15. What this result does not establish

This PASS does not establish:

```text
AG/1 is universal.
all control systems reduce to this case.
representations are sufficient physical causes.
feedback guarantees correction.
NASA's operational decision mechanism is fully reconstructed.
TCM-4 alone caused the loss.
all navigation-team beliefs are known from the report.
```

The source itself identifies multiple contributing causes and unresolved/process failures.

The safe transport claim is only:

```math
\boxed{
\textbf{this bounded closed-loop spacecraft-navigation corpus failed to force an addition to AG/1.}
}
```

---

# 16. Transport ledger

```text
AG/1 frozen
    ↓
T1 — software incident
    PASS
    ↓
T2 — experimental science
    PASS
    ↓
T3 — shared evidence / competing analyses
    PASS
    ↓
T4 — same representation / different worlds
    PASS
    ↓
T5 — representation → intervention → changed world → revised representation
    PASS
```

The current evidence supports:

```math
\boxed{
\textbf{AG/1 has survived five heterogeneous external reconstruction tests without architectural enlargement.}
}
```

This remains a bounded transport result, not a universal-minimum claim.
