# AG/1 Transport Test 06 — Deepwater Horizon Observability / Interface Modification

**Protocol:** `transport/00_TRANSPORT_PROTOCOL_AG1.md`  
**Frozen architecture:** `abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md` (`AG/1`)  
**Prior milestone:** `transport/MILESTONE_T1_T5.md`  
**Test status:** COMPLETED  
**External-domain class:** offshore drilling / active diagnostic testing / monitoring topology / alarm inhibition / observation-path degradation

---

# 1. Selection rationale

Transport 01–05 established that frozen AG/1 can reconstruct:

```text
world/history ≠ representation
measurement ≠ interpretation
same evidence → different models
same model/output → different worlds
representation → intervention → changed world → later representation
```

Transport 06 changes the failure mode.

The target is not merely:

```math
\rho_t\rightarrow a_t\rightarrow\mathcal H_{t+1}
```

but:

```math
\boxed{
\rho_t
\rightarrow
a_t
\rightarrow
\mathcal H_{t+1}+\mathcal I_{t+1}
\rightarrow
o_{t+1}
\rightarrow
\rho_{t+1}
}
```

where `\mathcal I` is **not** an architecture primitive. It is shorthand for the concrete relation topology that determines which physical process is connected to which measurement, alarm, display, recipient, or diagnostic procedure.

The test asks whether AG/1 can reconstruct interventions that alter future error detectability without adding:

```text
INTERFACE
OBSERVABILITY
CORRIGIBILITY
CHANNEL
SENSOR_STATE
MONITORING_STATE
ALARM_STATE
```

as new carriers.

The adversarial distinctions are:

```math
\boxed{
\text{world changed}
\neq
\text{observation path changed}
\neq
\text{information became available}
}
```

and:

```math
\boxed{
\text{capability}
\neq
\text{future error detectability}
}
```

---

# 2. Bounded external corpus

This run uses a bounded set of official/public investigative records concerning the April 20, 2010 Macondo / Deepwater Horizon disaster.

## S1 — National Commission / Chief Counsel record

```text
National Commission on the BP Deepwater Horizon Oil Spill and Offshore Drilling
Chief Counsel's Report / Macondo investigation
Official U.S. Government / Coast Guard-hosted and GovInfo copies
```

Source-level facts used:

```text
a negative pressure test repeatedly produced anomalous drill-pipe pressure;
well-site leaders and rig crew accepted a later test as successful without reconciling the persistent 1,400 psi drill-pipe pressure;
by about 9:10 p.m. the crew rerouted returns overboard;
that rerouting bypassed the pits, Sperry-Sun flow-out meter, and gas sensors;
those bypassed channels could no longer be used to monitor the well;
a separate Hitec flow-out meter remained available but did not alert the crew to the kick.
```

## S2 — U.S. Coast Guard / DOI Deepwater Horizon investigation

```text
Deepwater Horizon / Macondo investigation reports
U.S. Coast Guard / Department of the Interior / BSEE archival record
```

Source-level facts used:

```text
some fire/gas detectors were inoperable or set in inhibited mode;
in inhibited mode, detector information could still be reported to a control panel while an audible/general alarm would not automatically sound;
rig personnel described inhibition as standard practice in part to prevent false alarms from waking sleeping crew members;
when returns were pumped overboard, the Sperry-Sun flow meter could no longer adequately provide flow-out monitoring to personnel responsible for monitoring it.
```

## S3 — National Academies interim review

```text
National Research Council / National Academies
Interim Report on Causes of the Deepwater Horizon Oil Rig Blowout and Ways to Prevent Such Events
```

Source-level facts used:

```text
repeated negative-pressure tests supplied indications that well integrity had not been established;
diverting mud flow for the sheen test could remove flow from hydrocarbon-detection instrumentation;
several fire/gas detectors were inhibited because of frequent false alarms;
inhibited configuration left later response dependent on manual action.
```

Excluded from evidence for this run:

```text
popular retellings
later films/documentaries
unbounded secondary commentary
organizational-culture theories not explicitly required by the bounded records
```

This is an architecture transport test, not a complete causal reconstruction of the Macondo disaster.

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

No `INTERFACE`, `CHANNEL`, `SENSOR`, `OBSERVABILITY`, `CORRIGIBILITY`, `ALARM`, or `DIAGNOSTIC` carrier may be added.

Those words may occur only as local source vocabulary represented through ordinary typed relations.

---

# 4. Reconstruction principle — an interface is a relation topology, not automatically a primitive

Suppose a physical process `p` can produce a measurable quantity `m`, which a device can report to a display or recipient.

AG/1 may encode source-earned relations such as:

```text
SENSES(sensor,p)
MEASURES(sensor,m)
REPORTS_TO(sensor,display)
TRIGGERS(sensor,alarm)
NOTIFIES(alarm,crew)
BYPASSES(flow_path,sensor)
INHIBITS_TRIGGER(configuration,sensor,alarm)
AVAILABLE_TO(display,operator)
```

These predicates do not create a new interface carrier.

A derived interface view is simply a query over such relations:

```math
\boxed{
InterfaceView(Q)
:=
\text{relation paths connecting physical process, measurement, signal, and recipient under }Q
}
```

The kill test is whether some source distinction about future detectability remains unreconstructible even after all such concrete relation paths are retained.

---

# 5. Witness I1 — active diagnostic action expands a discrimination opportunity

Before temporary abandonment, the crew performed a negative pressure test intended to probe whether the cement barrier would hold against hydrocarbon flow.

This is important because the test is not passive observation.

It is an intervention designed to create informative conditions:

```text
PERFORMS_NEGATIVE_PRESSURE_TEST(crew,well)
REDUCES_PRESSURE(test,configured_path)
OBSERVES(test,drill_pipe_pressure)
OBSERVES(test,kill_line_flow_or_pressure)
```

The first test repeatedly produced drill-pipe pressure that rose back to approximately 1,400 psi after being bled down.

The later official reconstruction treats that pressure as evidence that the well had failed the test.

So the test action created an observation opportunity that did not exist in the same form without the intervention:

```math
\boxed{
\text{diagnostic intervention}
\rightarrow
\text{new discriminating relation evidence}
}
```

No `INTERFACE` primitive is required.

The observation opportunity is reconstructed from ordinary relations among:

```text
test procedure
pressure path
measurement
observed value
barrier hypothesis/representation
```

### Result

```text
PASS
```

---

# 6. Witness I2 — increased evidence availability does not guarantee correction

The same negative-pressure test also preserves the T5 negative lesson.

The crew did not adequately reconcile the anomalous drill-pipe pressure with the zero-pressure/no-flow result on the kill line.

The anomaly was explained through a represented `bladder effect` and the later test was accepted as successful.

Represent:

```text
rho_pressure_anomaly:
    DRILL_PIPE_PRESSURE ≈ 1400 psi

rho_bladdereffect:
    anomaly explained without failed barrier

OBSERVES(crew,rho_pressure_anomaly)
CONSIDERS/ACCEPTS_EXPLANATION(crew,rho_bladdereffect)
PROCEEDS_TO_TEMPORARY_ABANDONMENT(crew)
```

Thus:

```math
\boxed{
\text{expanded diagnostic opportunity}
\not\Rightarrow
\text{correct representation revision}
}
```

This prevents `observability` from being silently equated with `corrigibility`.

### Result

```text
PASS
```

---

# 7. Witness I3 — operational action degrades the future observation path

At about 9:10 p.m., the crew rerouted well returns overboard.

The investigative record states that doing so bypassed:

```text
the pits
Sperry-Sun flow-out meter
gas sensors
```

and that those bypassed channels could no longer be used to monitor the well.

This is the direct T6 discriminator.

Before rerouting:

```text
FLOW_PATH(well_returns,pits)
MONITORED_BY(well_returns,Sperry_Sun_flow_meter)
SAMPLED_BY(well_returns,gas_sensors)
```

After rerouting:

```text
REROUTES(crew,well_returns,overboard_path)
BYPASSES(overboard_path,pits)
BYPASSES(overboard_path,Sperry_Sun_flow_meter)
BYPASSES(overboard_path,gas_sensors)
```

Therefore the same evolving physical process no longer had the same relation path to those monitoring devices.

Formally:

```math
\boxed{
\mathcal H_{process,t+1}
\text{ can continue evolving while }
InterfaceView_{t+1}(process\rightarrow observer)
\neq
InterfaceView_t(process\rightarrow observer)
}
```

No global `INTERFACE_STATE` object is required.

### Result

```text
PASS
```

---

# 8. Witness I4 — remaining capability does not imply equivalent detectability

The rerouting did not remove every possible information source.

The record notes that another Hitec flow-out meter remained available, but its data did not alert the crew to the accelerating kick.

The record also discusses possible secondary physical flow checks that were not performed.

So:

```math
\boxed{
\text{some monitoring capability remains}
\not\Rightarrow
\text{same error detectability remains}
}
```

Represent directly:

```text
AVAILABLE(Hitec_flow_meter)
NOT_BYPASSED_BY(overboard_path,Hitec_flow_meter)
DOES_NOT_ALERT(available_data,crew,kick)

AVAILABLE_PROCEDURE(secondary_physical_flow_check)
NOT_PERFORMED(secondary_physical_flow_check)
```

No scalar `OBSERVABILITY_LEVEL` is required.

The topology itself records which paths remain live and which fail to deliver discriminating information.

### Result

```text
PASS
```

---

# 9. Witness I5 — nuisance reduction can degrade alarm propagation

The investigation records that selected gas detectors were commonly configured in an inhibited mode, in part to prevent false alarms from waking sleeping crew members.

Crucially, inhibition did not necessarily mean that the sensing device ceased detecting gas.

Rather, the relation from detector output to wider alarm propagation was altered.

A source-faithful reconstruction is:

```text
DETECTS(gas_detector,gas)
REPORTS_TO(gas_detector,control_panel)

configuration_inhibited:
    INHIBITS_TRIGGER(gas_detector,general_alarm)
```

with a represented operational motivation such as:

```text
rho_nuisance_cost:
    false alarms disturb sleeping crew
```

and:

```text
CONFIGURES_TO_REDUCE(false_alarm_disturbance,inhibited_mode)
```

where the source earns that rationale.

This produces the adversarial pattern:

```math
\boxed{
\text{local operational convenience / nuisance reduction}
\rightarrow
\text{degraded automatic notification path}
}
```

without claiming that detector sensing itself vanished.

Thus:

```math
\boxed{
\text{sensing capability}
\neq
\text{automatic alarm propagation}
\neq
\text{crew-wide notification}
}
```

### Result

```text
PASS
```

---

# 10. Witness I6 — observation-channel change is not the same as world change

The well can continue to undergo hydrocarbon influx whether or not a particular flow meter, gas sensor, or alarm route is connected to that process.

Therefore AG/1 must preserve:

```text
HYDROCARBON_INFLUX(well)
```

separately from:

```text
MONITORS(sensor,well_returns)
```

and separately from:

```text
REPORTS_TO(sensor,operator)
```

and:

```text
ALERTS(operator,condition)
```

This yields:

```math
\boxed{
\text{world/process relation}
\neq
\text{measurement relation}
\neq
\text{signal-routing relation}
\neq
\text{recipient-information relation}
}
```

All are ordinary typed relations.

### Result

```text
PASS
```

---

# 11. Interface modification can alter future corrigibility without becoming a corrigibility primitive

The strongest T6 result is not that sensors matter.

It is that actions can change the relation topology through which later contradiction could reach an agent.

For example:

```text
rerouting returns overboard
→ bypasses primary monitoring paths
→ fewer/effectively weaker conventional kick-detection paths remain
```

and:

```text
inhibiting automatic alarm propagation
→ gas detection may still occur locally
→ crew-wide automatic notification no longer follows
```

This can be summarized analytically as:

```math
\boxed{
\Delta InterfaceView
\rightarrow
\Delta\{\text{available future error signals}\}
}
```

but neither `InterfaceView` nor `available future error signals` is a new architecture primitive.

They are graph queries over the frozen relation substrate.

Thus AG/1 can represent a structural change in corrigibility opportunity without containing a primitive called `CORRIGIBILITY`.

---

# 12. Hidden-parameter audit

The reconstruction does not use:

```text
interface object
observability scalar
corrigibility scalar
channel object
sensor-state carrier
monitoring-state carrier
alarm-state carrier
feedback primitive
control primitive
```

The following appear only as source-earned typed relation vocabulary:

```text
SENSES
MEASURES
REPORTS_TO
TRIGGERS
NOTIFIES
BYPASSES
REROUTES
INHIBITS_TRIGGER
AVAILABLE
NOT_PERFORMED
PERFORMS_NEGATIVE_PRESSURE_TEST
OBSERVES
```

No unrestricted field such as:

```text
relation.interface_state = ...
representation.observability = ...
system.corrigibility = ...
```

is used.

The hidden-parameter audit passes.

---

# 13. Failure search

T6 deliberately searched for missing structure at these edges:

```text
active diagnostic action → new observation opportunity
new observation opportunity → incorrect interpretation still possible
operational rerouting → monitoring-path loss
remaining sensor capability → non-equivalent detectability
nuisance reduction → degraded automatic alarm propagation
physical process → measurement → signal routing → recipient information
```

None forces a new architecture primitive.

The strongest reconstruction is:

```math
\boxed{
\textbf{observation/interface structure is recoverable as typed relation topology over physical processes, measurement paths, signals, recipients, and representation scopes.}
}
```

and:

```math
\boxed{
\textbf{actions can modify that topology, changing future correction opportunities, without requiring INTERFACE or CORRIGIBILITY as primitive carriers.}
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
\textbf{Transport 06 does not force an architectural primitive beyond frozen AG/1.}
}
```

The decisive T6 structure is:

```math
\boxed{
\rho_t
\rightarrow
a_t
\rightarrow
\Delta InterfaceView
\rightarrow
\Delta o_{future}
\rightarrow
\rho_{future}
}
```

where every step is reconstructed through ordinary typed relations plus representation scopes.

---

# 15. What this result does not establish

This PASS does not establish:

```text
AG/1 is universal.
all interfaces are analytically equivalent.
more sensors always improve correction.
less alarm noise always reduces correction.
Macondo can be fully explained as an observability failure.
interface topology alone determines behavior.
corrigibility is reducible in every future domain.
```

It establishes only:

```math
\boxed{
\textbf{this bounded interface-modification corpus failed to force an addition to AG/1.}
}
```

---

# 16. Transport ledger after T6

```text
T1 — software incident / debugging
→ PASS

T2 — experimental science / measurement
→ PASS

T3 — shared evidence / competing analyses
→ PASS

T4 — same representation / different worlds
→ PASS

T5 — representation-driven intervention / changed world / revised representation
→ PASS

T6 — action changes future observation/correction topology
→ PASS
```

The calibrated claim ceiling advances only to:

```math
\boxed{
\textbf{AG/1 has survived six heterogeneous external reconstruction tests without architectural enlargement.}
}
```

No stronger universal claim is earned.

---

# 17. New boundary exposed by T6

T6 does not force `INTERFACE` as a primitive.

But it exposes the next sharper question.

AG/1 can represent:

```text
which paths from world → measurement → recipient exist
which paths are bypassed/inhibited
which actions alter those paths
which later observations are or are not delivered
```

The next unresolved pressure is not interface existence.

It is whether the architecture can reconstruct **selection over interface modifications based on expected future information value**, for example:

```math
\boxed{
\text{representation of uncertainty}
\rightarrow
\text{choose a measurement/challenge action}
\rightarrow
\text{new discriminating evidence}
\rightarrow
\text{update}
}
```

without adding `EXPERIMENT_DESIGN`, `INFORMATION_GAIN`, `QUERY`, or `ACTIVE_LEARNING` as new primitives.

That is a separate future transport test.

AG/1 remains frozen.