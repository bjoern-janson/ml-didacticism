# Adversarial Ablation — STATE and ACCESS

**Depends on:**
- `abstraction/00_ABSTRACTION_PROTOCOL.md`
- `abstraction/01_RELATION_INVENTORY.md`
- `abstraction/02_INVARIANT_STRIPPING_TESTS.md`
- `abstraction/03_MINIMAL_ARCHITECTURE.md`
- `abstraction/04_ABLATION_COMMITMENT_AUTHORITY.md`

**Purpose:** test whether `STATE` and `ACCESS` are primitive architectural elements or derivable views over temporally indexed typed relations and events  
**Status:** adversarial carrier/semantic ablation pass; no external-domain testing; `EVENT` is explicitly out of scope for this pass

The references below to the `COMMITMENT` and `AUTHORITY` kernels mean the
provisional semantic residues established by `04`, not commitments that those
families must remain primitive carriers in the final architecture. The final
carrier question is settled only by the later joint ablation.

The governing criterion is:

```math
\boxed{\textbf{A carrier is primitive only if removing it prevents lossless reconstruction of a distinction the corpus requires.}}
```

The candidate architecture entering this pass is:

```math
\boxed{
\mathcal A^{(2)}=
\{ENTITY,STATE,EVENT,RELATION,TIME,ACCESS,REPRESENTATION,COMMITMENT,AUTHORITY\}
+
\{SOURCE\_PROVENANCE,OPEN\}
}
```

This pass attacks:

```math
\boxed{STATE\qquad ACCESS}
```

in three ablations:

```text
A. remove STATE
B. remove ACCESS
C. remove STATE + ACCESS jointly
```

No new abstraction may be introduced unless a reconstruction failure forces it.

---

# 0. Anti-cheat constraints

The hidden-parameter audit from `04` remains binding.

A reduction fails if the removed primitive reappears as an unconstrained parameter of a retained object.

Invalid examples:

```text
STATE removed
→ RELATION(type="state", value="imprisoned")

STATE removed
→ ENTITY(state="dead")

ACCESS removed
→ RELATION(type="access", modality="see", success=false)

ACCESS removed
→ EVENT(access=true)
```

These are renamings.

However, the existence of **source-earned local predicates** such as:

```text
is alive
is at place
possesses
recognizes
hears
understands
receives
remembers
```

is not itself a hidden reintroduction of `STATE` or `ACCESS`.

Why?

Because the architecture already requires typed relations to preserve source distinctions. The ablation question is whether those local relations require a further primitive umbrella called `STATE` or `ACCESS`.

Thus:

```math
\boxed{
\text{local predicate survives}
\not\Rightarrow
\text{higher-level family is primitive}
}
```

The parameter audit asks whether one free parameter recreates the removed semantic bit. It does **not** require erasing the source predicate inventory.

---

# 1. A necessary logical distinction: absent edge, explicit negation, and OPEN

Before attacking `STATE`, the graph language must preserve three distinct conditions:

```text
1. relation asserted
2. relation explicitly negated / contrary relation asserted
3. relation not established by source
```

These must not collapse.

For example:

```text
brothers do not recognize an agent
```

is not the same structural condition as:

```text
the source does not tell us whether they recognize the agent
```

Likewise:

```text
person is dead
```

is not represented merely by failing to store an `alive` edge.

Therefore the retained relation language must permit explicit source-supported negative assertions or contrary predicates.

This does **not** add a new semantic primitive. It is logical polarity on an asserted relation.

The governing rule is:

```math
\boxed{
\text{no edge}
\neq
\text{negative edge}
\neq
OPEN
}
```

`OPEN` remains the meta-level marker for an unearned relation.

---

# 2. Target A — kill `STATE`

## 2.1 Kill hypothesis

Attempt:

```math
\boxed{
STATE(t)
\stackrel{?}{=}
\Gamma(t)
=
\{r\in RELATION\mid r\text{ holds at }t\}
}
```

where relation assertions carry temporal support such as:

```text
start time
end time when known
or event-bounded validity
```

A `STATE` would then be a **query/view** over the graph, not a stored primitive.

A transition would be:

```math
\boxed{
\Delta\Gamma_{t\to t'}
=
\Gamma(t')-\Gamma(t)
}
```

with events preserving what occurred between the two relational configurations.

The ablation must survive hard cases involving absence, persistence, negative relations, and transitions.

---

# 3. STATE witness S1 — alive → dead

The corpus repeatedly distinguishes living persons from narrated death events.

A stateful encoding might store:

```text
STATE(person,t0)=alive
STATE(person,t1)=dead
```

The proposed state-free encoding is:

```text
ALIVE(person) holds over interval before death event
DEATH_EVENT(person,t_d) occurs
DEAD(person) holds after t_d where the source establishes it
```

or equivalently, where only death-event provenance is needed:

```text
ALIVE relation has temporal support ending at death event
DEATH_EVENT remains in event history
```

The exact representation should preserve source wording and must not infer death merely from absence of `ALIVE`.

Required distinctions survive:

```math
\boxed{
\text{alive before death}
\neq
\text{death event}
\neq
\text{dead afterward}
}
```

without a `STATE` object.

### Hidden-parameter audit

No field of the form:

```text
state="dead"
```

is used.

The source predicate `dead` or the death event itself carries the content.

### Result

```text
STATE not required by alive/dead transition.
```

---

# 4. STATE witness S2 — present → absent / location change

Movement cases can be represented through temporally supported spatial relations:

```text
AT(entity,place_A) over interval T0
MOVE_EVENT(entity,place_A→place_B,t_m)
AT(entity,place_B) over interval T1
```

Therefore:

```math
\boxed{
\text{present at A}
\rightarrow
\text{movement event}
\rightarrow
\text{present at B}
}
```

requires no stored `STATE(entity)=present/absent` value.

A statement such as:

```text
entity is not present to observer / household
```

must remain typed to the relevant relation rather than becoming a generic absence state.

The following remain different:

```text
not at place P
not accessible to agent A
represented by agent A as dead
actually dead
```

They are different relational/event assertions.

### Result

```text
STATE not required by presence/location transition.
```

---

# 5. STATE witness S3 — possession transfer and changing object function

A stateful encoding might say:

```text
object state = possessed by A
object state = possessed by B
object state = evidence
```

The state-free encoding preserves the stronger structure:

```text
POSSESSES(A,O) over T0
TRANSFER_EVENT(A,B,O,t1)
POSSESSES(B,O) over T1
PRESENTS(B,O,recipient,t2)
REPRESENTATION(recipient,event-history-of-O,t3)
```

The object's later evidential role is not a physical `STATE` primitive. It is a changed relation between the persistent object, an interaction, and an agent representation.

Thus:

```math
\boxed{
ID(O)\text{ persists}
\land
Relations(O,t_0)\neq Relations(O,t_1)
}
```

is sufficient.

### Result

```text
STATE not required by persistent-object/function transitions.
```

---

# 6. STATE witness S4 — hidden → discovered

This is a dangerous case because `hidden` and `discovered` often look like state values.

The corpus gives stronger event/relational structure.

A hidden-object episode can be represented as:

```text
OBJECT_AT(O,location) holds
HIDE_EVENT(agent,O,location,t0) occurs where narrated
SEARCH_EVENT(searcher,domain,t1) occurs
no source-supported DISCOVER_EVENT(searcher,O,t1)
OBJECT_AT(O,location) continues
```

A later discovery is:

```text
DISCOVER_EVENT(agent,O,t2)
```

possibly followed by a new representation.

The important distinction is not:

```text
STATE(O)=hidden
STATE(O)=discovered
```

but:

```math
\boxed{
\text{object location/history}
+
\text{search history}
+
\text{discovery history}
}
```

The source can also explicitly describe concealment, which remains a local relation/action predicate.

### Critical caution

Failure to record a discovery event is not by itself proof that no discovery occurred unless the source establishes the search outcome.

This is where `OPEN` and source provenance remain essential.

### Result

```text
STATE not required by hidden/discovered transition.
```

---

# 7. STATE witness S5 — uncommitted → committed

`04` established an irreducible commitment kernel.

A stateful view might store:

```text
STATE(agent)=uncommitted
STATE(agent)=committed
```

That is weaker than the retained relation:

```math
COMMITMENT(agent,future\_content,t)
```

which begins after the source event that creates/strengthens it and persists according to event history.

The transition is therefore:

```text
speech/request event
→ promise/oath/surety event
→ COMMITMENT relation begins or changes
```

No general `STATE` primitive is required.

### Result

```text
STATE not required by commitment transition.
```

---

# 8. STATE witness S6 — unauthorized → authorized / authority change

`04` also established an irreducible authority kernel.

An appointment/delegation episode can be represented as:

```text
before appointment:
    no source-supported AUTHORITY edge for actor over scope

APPOINT/DELEGATE_EVENT occurs

after appointment:
    AUTHORITY(actor,action_class,scope,target,time-support) holds
```

Where the source explicitly revokes or limits authority, the relation's temporal support or scope changes.

Again:

```text
STATE(actor)=authorized
```

adds no information beyond the authority relation plus time and event history.

### Negative caution

Before appointment, absence of an authority edge means only that the source has not established that authority unless the source explicitly establishes lack/prohibition.

Do not convert absence into a negative fact.

### Result

```text
STATE not required by authority transitions.
```

---

# 9. STATE witness S7 — unrealized future → realized event

The prior minimization already killed primitive `FUTURE_STATE`.

A future representation is:

```math
REPRESENTATION_i(content=F,target\_time>t)
```

A later event may correspond:

```math
EVENT(e,t+n)
```

and the source may earn a correspondence relation:

```math
CORRESPONDS(e,F)
```

or leave it OPEN.

Thus:

```text
future represented
future later realized
```

is not a change in one primitive `STATE` variable. It is a temporal relation between a representation and later event/world relations.

### Result

```text
STATE not required by future/realization distinction.
```

---

# 10. STATE ablation result

Every tested state transition reconstructs through:

```text
ENTITY
EVENT
RELATION
TIME
```

plus whichever irreducible semantic relation is actually involved.

The correct formalization is therefore:

```math
\boxed{
StateView(t)
:=
\Gamma(t)
=
\{r(args)\mid Holds(r,args,t)\}
}
```

possibly together with events active at or immediately bounding the queried interval.

A state transition is a derived comparison between relational snapshots while the event graph preserves transitions that leave terminal relations unchanged.

Therefore:

```math
\boxed{STATE\ \text{is a derived view, not a primitive carrier.}}
```

## Verdict

```text
STATE: DERIVABLE
```

### What must survive after deletion

```text
typed relation identity
relation polarity where source explicit
temporal support
persistent entity identity
event history
OPEN vs explicit negative
```

No `state` parameter is permitted in the reduced basis.

---

# 11. Target B — kill `ACCESS`

## 11.1 Kill hypothesis

The previous architecture treated access as:

```math
ACCESS(agent,x,t)
```

with modalities such as perception, receipt, memory retrieval, recognition, comprehension, or inspection.

The new hypothesis is that no umbrella access primitive is required if the source-level information-bearing predicates remain typed ordinary relations/events:

```text
SEES
HEARS
RECEIVES
INSPECTS
SEARCHES
DISCOVERS
RECOGNIZES
UNDERSTANDS
REMEMBERS
RETRIEVES
IS_TOLD
```

The question is not whether these distinctions exist. They plainly do.

The question is whether they require an additional common semantic kernel called `ACCESS`.

---

# 12. ACCESS witness A1 — object exists, search occurs, object not discovered

Source discriminator: Genesis 31.

Required distinction:

```math
\boxed{
\text{object present}
\neq
\text{object discovered by searcher}
}
```

Without `ACCESS`, encode:

```text
OBJECT_AT(O,location,t)
SEARCH_EVENT(searcher,domain,t1)
source-supported search outcome: no DISCOVER_EVENT(searcher,O,t1)
OBJECT_AT(O,location,t1) still holds
```

where the narrative also supplies the concealment action/history.

This distinguishes:

```text
not discovered
```

from:

```text
discovered and misinterpreted
```

because the latter contains a perception/recognition/discovery event followed by a representation.

No generic `ACCESS(success=false)` flag is required.

### Hidden-parameter audit

Passes if the graph retains the concrete search/discovery predicates and does not add a generic access bit.

### Result

```text
ACCESS not required by failed-search case.
```

---

# 13. ACCESS witness A2 — authentic object observed, false event inferred

Source discriminator: Genesis 37.

Required distinction:

```text
recipient correctly recognizes authentic object
recipient constructs false event history
```

Without `ACCESS`, encode:

```text
PRESENT_EVENT / object presentation
RECOGNIZES(recipient,O,t)
REPRESENTATION(recipient,history_claim,t2)
```

with:

```math
history\_claim\neq actual\ event\ ancestry(O)
```

This cleanly differs from Genesis 31:

```text
G31: search without object discovery
G37: object recognition followed by false inference
```

The distinction is carried by specific event/relation history plus `REPRESENTATION`, not by an access umbrella.

### Result

```text
ACCESS not required by observation-vs-misinterpretation distinction.
```

---

# 14. ACCESS witness A3 — asymmetric recognition

Source discriminator: Genesis 42.

The source explicitly gives:

```text
party A recognizes party B
party B does not recognize party A
```

A state/access encoding might write:

```math
ACCESS_A(identity_B)=1
\qquad
ACCESS_B(identity_A)=0
```

But the source-level structure is more precise:

```text
RECOGNIZES(A,B,t)
NOT RECOGNIZES(B,A,t)
```

plus the later disclosure/non-disclosure events.

The umbrella `ACCESS` adds no reconstruction power.

### Result

```text
ACCESS not required by identity asymmetry.
```

---

# 15. ACCESS witness A4 — hidden comprehension under false speaker model

Source discriminator: Genesis 42.

Structural record:

```text
speakers converse
interpreter relation is present in public interaction
speakers represent target as not understanding them
target actually understands their speech
```

Without `ACCESS`, encode:

```text
SPEECH_EVENT(group,message,t)
UNDERSTANDS(target,message,t)
REPRESENTATION(group,NOT UNDERSTANDS(target,message,t),t)
```

This preserves the essential mismatch:

```math
\boxed{
\text{actual comprehension relation}
\neq
\text{speakers' representation of comprehension relation}
}
```

A generic `ACCESS(target,message)=true` field is unnecessary.

### Result

```text
ACCESS not required by hidden-comprehension case.
```

---

# 16. ACCESS witness A5 — testimony received but not believed

Source discriminator: Genesis 45.

Required distinction:

```text
recipient receives report
recipient initially does not accept represented proposition
additional evidence later accompanies representation revision
```

Without `ACCESS`, encode:

```text
REPORT_EVENT(senders→recipient,content,t0)
RECEIVES(recipient,report,t0)
REPRESENTATION(recipient,content-status,t0)
OBSERVATION_EVENT(recipient,wagons,t1)
REPRESENTATION(recipient,revised-content-status,t2)
```

The source-level distinction:

```math
\boxed{
\text{message received}
\neq
\text{message believed}
}
```

remains because `RECEIVES` and `REPRESENTATION` are different typed relations/events.

No common access variable is required.

### Result

```text
ACCESS not required by testimony/belief separation.
```

---

# 17. ACCESS witness A6 — impaired perception with intentional action

Source discriminator: Genesis 48.

The chapter gives both:

```text
age-related visual impairment
```

and:

```text
deliberate crossed-hand allocation
```

Without `ACCESS`, encode the sensory limitation with the source-level perceptual/capability predicate and preserve the intentional action event separately.

For example:

```text
VISUAL_CAPABILITY(agent,target-domain,t)=limited
IDENTIFICATION_REPORT(other→agent,candidates,t1)
ALLOCATION_EVENT(agent,candidates,t2)
intentionality supported by narrator wording
```

The exact predicate name should remain close to source structure; no general `ACCESS` field is needed.

The architectural lesson remains:

```math
\boxed{
\text{limited perception}
\neq
\text{accidental action}
}
```

### Hidden-parameter audit

Using a modality-specific relation such as `SEES`, `RECOGNIZES`, `UNDERSTANDS`, or a source-supported perceptual limitation is **not** equivalent to restoring one generic `ACCESS` primitive.

The modalities remain distinct because the corpus gives them distinct consequences.

### Result

```text
ACCESS not required by sensory-limitation case.
```

---

# 18. ACCESS as a derived analytic family

After ablation, one may still define a convenience projection:

```math
\boxed{
AccessView_i(t)
:=
\Pi_{info}(Relations_i(t),Events_i(t))
}
```

where `\Pi_{info}` selects source-earned information-bearing relation/event families such as seeing, hearing, receiving, recognizing, understanding, remembering, inspecting, and discovering.

This is useful for analyzing information topology, but it is not part of the primitive basis.

Critically, `\Pi_{info}` does not reduce all modalities to one scalar bit.

The source distinctions remain:

```text
heard but did not understand
received but did not believe
searched but did not discover
recognized object but inferred wrong event
recognized person but did not disclose identity
remembered but did not act
```

Thus:

```math
\boxed{
\text{access-family membership}
\neq
\text{one universal access variable}
}
```

## Verdict

```text
ACCESS: DERIVABLE AS A FAMILY / NOT A PRIMITIVE
```

The corpus requires the modality-specific relations.
It does not require an additional umbrella `ACCESS` kernel.

---

# 19. Joint ablation — remove STATE + ACCESS simultaneously

The joint test matters because the previous formulation sometimes described access as a relation to a state.

With both removed, the remaining architecture must represent information-bearing interaction directly over entities, events, relations, messages, and representations.

The reduced candidate is:

```math
\boxed{
\mathcal A^{-STATE,-ACCESS}
=
\{ENTITY,EVENT,RELATION,TIME,REPRESENTATION,COMMITMENT,AUTHORITY\}
+
\{SOURCE\_PROVENANCE,OPEN\}
}
```

---

# 20. Joint witness J1 — hidden object and failed search

Required structure:

```text
object exists at location
agent hides object
searcher searches domain
object not discovered
object remains at location
```

Reconstruction:

```text
ENTITY: object, hider, searcher, location
EVENT: hiding, search
RELATION: object-at-location, search-domain relation, explicit search outcome
TIME: event/order support
REPRESENTATION: optional searcher claims/inferences where narrated
```

No `STATE` or `ACCESS` primitive required.

---

# 21. Joint witness J2 — one-sided identity recognition

Required structure:

```text
A recognizes B
B does not recognize A
A preserves concealment
```

Reconstruction:

```text
ENTITY: A,B
RELATION: recognizes(A,B), not-recognizes(B,A)
EVENT: concealment/interaction/speech
TIME: relation support
REPRESENTATION: later accusations/family reports/etc.
```

No state object is required to hold `recognized/unrecognized` and no access bit is required to summarize the relations.

---

# 22. Joint witness J3 — received evidence and false inference

Required structure:

```text
persistent authentic object
presentation event
recipient recognizes object
recipient constructs false past-event representation
```

Reconstruction:

```text
ENTITY: object, recipient, earlier actors
EVENT: object history + presentation
RELATION: recognizes(recipient,object)
TIME: ancestry/order
REPRESENTATION: false inferred event graph
```

Again:

```math
\boxed{
\text{recognition event/relation}
\neq
\text{resulting representation}
}
```

survives without either candidate.

---

# 23. Joint witness J4 — future promise, trigger, fulfillment/deferment

Required structure:

```text
future content represented
binding relation created
trigger event occurs
later action either occurs or remains absent at corpus boundary
```

Reconstruction:

```text
REPRESENTATION
COMMITMENT
EVENT
RELATION
TIME
```

A `STATE=fulfilled/deferred` field is unnecessary.

Fulfillment is a relation between the commitment content and later event history.

Deferment is represented by:

```text
commitment persists
trigger condition may have occurred
terminal event required by commitment not yet narrated by corpus boundary
```

with `OPEN` preventing unsupported future completion.

---

# 24. Joint witness J5 — authority change and action under limited information

Required structure:

```text
agent has partial information
agent proposes action
higher actor authorizes/appoints
agent later executes
```

Reconstruction:

```text
modality-specific information relations/events
REPRESENTATION: proposal
AUTHORITY: decision-right after authorization
EVENT: appointment + execution
TIME: order
```

Neither a global state snapshot nor an access umbrella adds reconstruction power.

---

# 25. Joint-ablation result

The joint removal does not expose a missing source distinction.

Every tested case remains reconstructible through:

```math
\boxed{
ENTITY
+
EVENT
+
RELATION
+
TIME
+
REPRESENTATION
+
COMMITMENT
+
AUTHORITY
}
```

with:

```math
\boxed{SOURCE\_PROVENANCE+OPEN}
```

as mandatory meta-constraints.

Therefore:

```text
STATE  → DERIVABLE VIEW
ACCESS → DERIVABLE FAMILY
```

and the joint ablation succeeds.

---

# 26. Revised minimal candidate

The new provisional architecture is:

```math
\boxed{
\mathcal A^{(3)}
=
\underbrace{\{ENTITY,EVENT,RELATION,TIME\}}_{carrier}
\cup
\underbrace{\{REPRESENTATION,COMMITMENT,AUTHORITY\}}_{semantic\ kernels}
\cup
\underbrace{\{SOURCE\_PROVENANCE,OPEN\}}_{meta}
}
```

This is a two-element reduction from `\mathcal A^{(2)}`.

The deleted terms remain available as derived notation:

```math
\boxed{
STATE(t):=\Gamma(t)
}
```

and:

```math
\boxed{
ACCESS_i(t):=\Pi_{info}(Relations_i(t),Events_i(t))
}
```

but neither belongs to the basis.

---

# 27. What the reduction means

The architecture no longer assumes that the world is fundamentally stored as a sequence of state objects.

Instead:

```math
\boxed{
\text{world history}
=
\text{persistent entities}
+
\text{typed relations with temporal support}
+
\text{events}
}
```

A state is a slice through that history.

Likewise, the architecture no longer assumes one generic information-access variable.

Instead:

```math
\boxed{
\text{information topology}
=
\text{who sees/hears/receives/recognizes/understands/remembers/etc. what, when}
}
```

The umbrella `ACCESS` is a useful analysis view over those relations, not a primitive.

This preserves a critical asymmetry:

```math
\boxed{
\text{modality-specific information relation}
\neq
\text{agent representation}
}
```

`REPRESENTATION` survives because correct perception/recognition can still produce a false model, future representations can exist without a corresponding world event, and later explanations can refer to unchanged past events.

---

# 28. Hidden-parameter audit after reduction

## STATE audit

Forbidden:

```text
state=...
status=...   # if used as a free replacement for all temporal relation configurations
```

Allowed:

```text
explicit typed relations with temporal support
explicit events
relation/query snapshots derived from them
```

The semantics are in the source-earned predicates, not in a generic state field.

## ACCESS audit

Forbidden:

```text
access=true/false
access_type=...
information_available=true
```

as a universal replacement primitive.

Allowed:

```text
sees
hears
receives
recognizes
understands
remembers
searches
discovers
```

when these are actual source-supported relation/event types.

No single retained parameter answers the question `has access?` for all cases.
The answer is a derived query over heterogeneous modality relations.

Therefore the parameter audit passes.

---

# 29. Non-results / limits

This pass does **not** show that:

```text
all relation types are equivalent
all information modalities can be merged
representation can be reduced to relation
commitment can be reduced to relation
authority can be reduced to relation
events are reducible to relation changes
```

Those are separate ablations.

In particular, `EVENT` is intentionally untouched here.

The next tempting question is:

```math
\boxed{
EVENT
\stackrel{?}{=}
\text{relation change over time}
}
```

but this file makes no verdict on it.

Attempted/interrupted actions, searches with no terminal world change, speech events, and actions whose intended effect fails are likely to be strong discriminators if that ablation is attempted later.

---

# 30. Provisional compression

The Genesis-derived architecture has now been reduced from the earlier five-layer intuition:

```text
WORLD
ACCESS
REPRESENTATION
ACTION
STATE TRANSITION
```

into a smaller event-relational form:

```math
\boxed{
\textbf{persistent entities}
+
\textbf{temporally supported relations}
+
\textbf{events}
+
\textbf{agent representations}
+
\textbf{commitment kernel}
+
\textbf{authority kernel}
}
```

with source provenance and explicit OPEN edges mandatory.

The central result of this pass is:

```math
\boxed{
\textbf{STATE is a view over temporal relations, and ACCESS is a view over modality-specific information relations/events.}
}
```

Neither currently survives as a primitive.

The resulting candidate is:

```math
\boxed{
\mathcal A^{(3)}
=
\{ENTITY,EVENT,RELATION,TIME,REPRESENTATION,COMMITMENT,AUTHORITY\}
+
\{SOURCE\_PROVENANCE,OPEN\}
}
```

The architecture is smaller, but the source distinctions remain.
