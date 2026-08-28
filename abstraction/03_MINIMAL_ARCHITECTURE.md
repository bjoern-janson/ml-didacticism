# Minimal Architecture — Genesis 1–50

**Depends on:**
- `abstraction/00_ABSTRACTION_PROTOCOL.md`
- `abstraction/01_RELATION_INVENTORY.md`
- `abstraction/02_INVARIANT_STRIPPING_TESTS.md`

**Purpose:** minimize the vocabulary-independent Genesis architecture by removing candidate machinery unless source-level reconstruction fails  
**Status:** first dependency/ablation pass; provisional minimal sufficient architecture; no external-domain testing

The governing objective is not the fewest symbols.

```math
\boxed{
\min |B|
\quad\text{s.t.}\quad
\operatorname{Reconstruct}(B,\text{Genesis invariants})
=
\text{all surviving structural distinctions}
}
```

The minimization phase has one directional bias:

```math
\boxed{\textbf{remove machinery; add nothing unless an ablation failure forces it}}
```

For every candidate structure `S_i`, ask:

```math
\boxed{
S_i\stackrel{?}{\in}\operatorname{closure}(B\setminus\{S_i\})
}
```

Allowed results:

```text
DERIVABLE          — fully reconstructible by explicit composition of other retained structures
PARTIALLY DERIVABLE — the named higher-level object is eliminable, but one or more internal distinctions remain irreducible
PRIMITIVE           — removing it destroys a source distinction that cannot be reconstructed without hidden special cases
```

A similarity claim is not a derivation. Every reduction requires:

```math
\boxed{\text{inputs}\xrightarrow{\text{explicit composition}}S_i}
```

and every primitiveness claim requires an ablation witness:

```math
\boxed{\text{remove candidate}\rightarrow\text{specific source distinction becomes unreconstructible}}
```

---

# 1. Candidate basis before minimization

The stripping pass produced ten recurring structures:

```text
S1  world / access / representation separation
S2  provenance-sensitive evidence
S3  persistent object / changing function
S4  future representation / realization separation
S5  persistent obligation state machine
S6  typed authority routing
S7  asymmetric information topology
S8  relation-specific ordering / allocated priority
S9  environment + starting state → differentiated trajectory
S10 retrospective meaning without event erasure
```

The relation inventory additionally requires persistent identity, event/action completion structure, temporal ordering, and explicit uncertainty/provenance annotations.

The minimization question is therefore not whether these observations are valid. They are source-earned. The question is whether each needs its own architectural primitive.

---

# 2. Separate carrier structure from semantic irreducibles

A major source of false minimization is to hide semantics inside an unrestricted generic field such as `TYPE` and then claim that every other distinction has disappeared.

To avoid that, this pass distinguishes **carrier structure** from **semantic irreducibles**.

## 2.1 Carrier structure

These are the minimal graph objects needed to represent anything at all.

```text
ENTITY_ID
STATE
EVENT
TYPED_RELATION
TIME
```

### ENTITY_ID

Persistent identity across label, role, location, and state changes.

```math
\boxed{\text{NameString}\neq\text{EntityID}\neq\text{Role}}
```

### STATE

A time-indexed condition or relation configuration.

Examples after vocabulary stripping include:

```text
object-at-location
agent-in-role
resource-held-by
member-of-group
alive/dead
recognized/unrecognized
present/absent
```

### EVENT

An occurrence that may have actors, targets, inputs, outputs, completion status, and effects.

`ACTION` is represented as an actor-bearing event rather than as a separate primitive.

This is necessary because the corpus contains both agent actions and non-agent events, and because attempts/interruption can be events even when the intended terminal state is never reached.

### TYPED_RELATION

A relation edge whose dimension must remain explicit.

This is not permission to hide arbitrary semantics in a string. Relation families that survive ablation as irreducible are elevated below.

### TIME

At minimum:

```text
before / after
same interaction interval
future relative to representation time
persisting across intervals
```

Temporal structure is required for future-vs-realized, retrospective accounts, persistent objects, obligations, and event provenance.

---

## 2.2 Semantic candidates tested for irreducibility

The main semantic candidates are:

```text
ACCESS
REPRESENTATION
AUTHORITY
COMMITMENT
PROVENANCE
EVIDENCE
OBLIGATION
FUTURE
ORDERING
PERSISTENCE
```

The rest of this file attempts to eliminate them.

---

# 3. Dependency matrix

| Candidate structure | Reconstruction inputs | Required reconstruction | Result |
|---|---|---|---|
| `S1` world/access/representation separation | `STATE + ACCESS + REPRESENTATION + ENTITY_ID` | world fact, agent access, agent-held model remain distinct | **PARTIALLY DERIVABLE** — the compound `S1` object is unnecessary, but `ACCESS` and `REPRESENTATION` survive as irreducibles |
| `S2` provenance-sensitive evidence | `ENTITY_ID + EVENT + TIME + STATE + ACCESS + REPRESENTATION` | authentic object, actual history, reported history, recipient inference | **DERIVABLE** — no primitive `EVIDENCE` or `PROVENANCE` object required |
| `S3` persistent object / changing function | `ENTITY_ID + STATE + TIME + TYPED_RELATION` | same object across changed holders/functions | **DERIVABLE** |
| `S4` future / realization separation | `REPRESENTATION + TIME + STATE + EVENT + TYPED_RELATION` | represented future distinct from later world event and correspondence | **DERIVABLE** — no primitive `FUTURE` object required |
| `S5` obligation state machine | `COMMITMENT + REPRESENTATION + TIME + STATE + EVENT + ENTITY_ID` | request/promise/oath distinction, trigger, completion/deferment | **PARTIALLY DERIVABLE** — eliminate `OBLIGATION` object; retain irreducible `COMMITMENT` relation family |
| `S6` authority routing | `AUTHORITY + ENTITY_ID + EVENT + TYPED_RELATION + TIME` | propose/authorize/delegate/execute scope distinctions | **PRIMITIVE** |
| `S7` asymmetric information topology | `ACCESS + REPRESENTATION + ENTITY_ID + TIME` | per-agent unequal information states | **DERIVABLE** |
| `S8` relation-specific ordering / priority | `TYPED_RELATION + STATE + TIME` | birth/age/seating/share/priority dimensions remain non-isomorphic | **DERIVABLE** — no primitive `ORDER` scalar |
| `S9` environment/start state → trajectory | `STATE + EVENT + TIME + TYPED_RELATION` | same environment, different starting relations, different transitions | **DERIVABLE** |
| `S10` retrospective meaning | `EVENT + TIME + REPRESENTATION + ENTITY_ID + TYPED_RELATION` | later explanation references prior event without overwriting event record | **DERIVABLE** |
| persistent identity | — | same entity across labels/roles/states | **PRIMITIVE CARRIER** |
| event/action occurrence | — | attempt/interruption/completion even when terminal state is unchanged | **PRIMITIVE CARRIER** |
| explicit uncertainty / `OPEN` | meta-level | absence of earned edge must remain representable | **NON-OPTIONAL META-CONSTRAINT** |
| source provenance | meta-level | every abstract record maps back to lexical structural source | **NON-OPTIONAL META-CONSTRAINT** |

This matrix produces a substantial reduction:

```math
\boxed{
\{S_1,\dots,S_{10}\}
\not\Rightarrow
10\text{ architecture primitives}
}
```

Most survivors are compositions.

---

# 4. Ablation tests

# A1 — Remove `EVIDENCE`

## Available

```text
ENTITY_ID
STATE
EVENT
TIME
ACCESS
REPRESENTATION
TYPED_RELATION
```

## Reconstruction witness

Represent an evidential episode as:

```text
persistent object/entity
+
current observable state
+
actual event ancestry
+
agent access to some subset of that ancestry/state
+
agent representation of ancestry/event
+
recipient representation update
```

Actual provenance is therefore not a special object. It is a path through the event graph over persistent identities:

```math
\boxed{
Prov_{actual}(x)
=
\operatorname{Path}_{EVENT,TIME}(x)
}
```

Reported provenance is a representation whose content is such a path:

```math
\boxed{
Prov_{reported,i}(x)
=
R_i(\operatorname{Path}(x))
}
```

## Discriminators

### Manipulated authentic object

The architecture can encode:

```text
same object ID
→ altered observable state
→ presented to recipient
→ recipient recognizes object
→ recipient lacks actual production history
→ recipient constructs false event representation
```

### Authentic object + false transfer account

```text
actual transfer event path
≠
reported transfer-event path
```

### Deliberately planted object

```text
controller placement event
→ object located with unaware target
→ later search discovers location
→ target agency remains unsupported
```

Nothing requires an `EVIDENCE` primitive.

## Result

```text
DERIVABLE
```

### Reduction

```math
\boxed{
\textbf{EVIDENCE is not primitive.}
}
```

An object or observation becomes evidential only by participating in a representation/inference relation.

---

# A2 — Remove a primitive `PROVENANCE`

## Attempted reduction

```text
persistent identity
+
event ancestry
+
time
+
transfer/production relations
```

## Witness

Object provenance is reconstructible by following events that create, alter, transfer, hide, place, recover, or present the same persistent entity.

```math
\boxed{
Prov(x,t)
=
\langle e_1,e_2,\dots,e_n\rangle
\quad\text{such that each }e_k\text{ bears on persistent }x
}
```

A false provenance claim is not a second world-history object; it is:

```math
\boxed{R_i(Prov(x))}
```

whose content disagrees with the source event chain.

## Counterexample search

Genesis 37, 38, 39, and 44 remain distinguishable:

```text
actual event ancestry
reported ancestry
known ancestry
recipient-inferred ancestry
```

are separate because `EVENT`, `ACCESS`, and `REPRESENTATION` are separate.

## Result

```text
DERIVABLE
```

### Reduction

No dedicated `PROVENANCE` semantic primitive is required in Corpus B.

**Important:** source provenance remains a mandatory meta-constraint. This ablation removes a *domain semantic primitive*, not the source-audit trail.

---

# A3 — Remove persistent identity

## Attempt

Represent every state as a fresh anonymous node and connect adjacent states by similarity.

## Failure

This loses source distinctions where the architecture must know that one thing persists while its role changes.

Failure witnesses include:

```text
same personal tokens:
collateral → later identity evidence

same long-lived agent:
family member → servant → prisoner → administrator

same person under multiple labels:
rename does not create a new entity
```

Without persistent identity:

```math
\boxed{
Role(x,t_1)\neq Role(x,t_2)
}
```

cannot be distinguished from:

```math
\boxed{x_{t_1}\neq x_{t_2}}
```

## Result

```text
PRIMITIVE CARRIER
```

---

# A4 — Remove `ACCESS`

## Attempt 1

Treat access as whatever an agent represents.

## Failure witness — missed hidden object

```text
object exists
search occurs
search fails
agent has no observation of object
```

The world state and the agent representation may both be representable, but without `ACCESS` the architecture cannot distinguish:

```text
not observed
from
observed and misinterpreted
```

## Failure witness — hidden comprehension

One participant hears/understands speech while the speakers represent that participant as unable to understand it.

Without an access relation, the actual information channel disappears.

## Failure witness — recognition asymmetry

One party identifies another while remaining unidentified.

The distinction is not merely different beliefs; it is different access to identity-linked information.

## Result

```text
PRIMITIVE
```

### Irreducible content

```math
\boxed{Access(i,x,t)}
```

with typed channels such as perception, receipt, memory retrieval, recognition, comprehension, or inspection.

The channel type may remain a subtype rather than a new primitive.

---

# A5 — Remove `REPRESENTATION`

## Attempt 1

Treat every agent state as an access state.

## Failure witness — authentic object / false event model

An agent correctly accesses and identifies a genuine object, yet infers an event that did not happen.

```math
\boxed{
Access_i(x)=1
\quad\land\quad
R_i(history(x))\neq history(x)
}
```

Access alone cannot encode the false event model.

## Failure witness — feared future

An agent represents a possible attack and prepares for it, although the later target behavior does not instantiate the feared event.

The feared future is neither a world state nor an access relation.

## Failure witness — explanation without world rewrite

A later agent gives a causal/purpose account of an earlier event while the original event record remains unchanged.

Without `REPRESENTATION`, later meaning can only overwrite world history or disappear.

## Result

```text
PRIMITIVE
```

### Irreducible content

```math
\boxed{Representation(holder,content,time,provenance)}
```

Representation subtypes may include report, fear, forecast, explanation, proposal, memory, inference, and interpretation, but these should not be merged when source consequences still depend on the subtype.

---

# A6 — Remove `EVENT`

## Attempt

Represent only state snapshots and differences between them.

## Failure witness — attempted but interrupted action

A specified action can be prepared and proximally initiated yet never complete.

If only pre/post world states are retained, the attempted action vanishes whenever its intended terminal state does not occur.

## Failure witness — correction attempt rejected

A subordinate attempts to alter a current allocation; the senior agent refuses and the world allocation remains unchanged.

The attempted correction is still part of the source structure.

## Failure witness — search failure

A search procedure can occur even if it produces no object-location change.

## Result

```text
PRIMITIVE CARRIER
```

An event record therefore needs at least:

```text
participants
optional actor
input state references
output/effect references
completion state
source provenance
```

---

# A7 — Remove a primitive `FUTURE`

## Attempted reduction

Represent future statements as ordinary representations whose content bears a temporal target later than the representation time.

```math
\boxed{
FutureRep_i(F,t)
:=
Representation_i(content=F,\ target\_time>t)
}
```

Realization is a later correspondence relation between the prior representation and a narrated world state/event.

```math
\boxed{
Realization(R_t(F),W_{t+n})
}
```

is added only when the source earns it.

## Counterexample test

This preserves:

```text
fear vs later behavior
forecast vs later realization
route statement vs actual route
future lineage statement still unrealized
bone-transfer instruction still deferred
```

provided representation subtype and temporal target remain available.

## Result

```text
DERIVABLE
```

### Reduction

No separate `FUTURE_STATE` primitive is necessary.

Future-ness is a relation between representation time and represented target time.

---

# A8 — Remove `OBLIGATION`

## Attempted reduction

Represent an obligation lifecycle as the composition:

```math
\boxed{
Representation(FutureAction)
+
Commitment(obligated\_party,target,scope)
+
TriggerCondition
+
EventHistory
+
CompletionState
}
```

## Witness — completed terminal transfer

```text
request future action
→ obligated party explicitly promises
→ commitment strengthened by oath
→ triggering death occurs
→ authorization obtained
→ transfer event performed
→ requested terminal state established
```

## Witness — deferred terminal transfer

```text
future transfer specified
→ collective party swears
→ triggering death occurs
→ body remains in current location at corpus end
```

The two cases differ because their event histories differ after trigger, not because they require different obligation primitives.

## Failure after removing `COMMITMENT` as well

If both `OBLIGATION` and `COMMITMENT` are removed, the architecture can no longer distinguish:

```text
request for future action
from
promise to perform that action
from
oath strengthening that commitment
```

This failure is source-visible.

A request for future remembrance occurs without a narrated promise; elsewhere a promise and oath are explicitly narrated for a future burial action.

Therefore the reduction stops at `COMMITMENT`.

## Result

```text
PARTIALLY DERIVABLE
```

### Reduction

```math
\boxed{\textbf{OBLIGATION is derived; COMMITMENT survives.}}
```

---

# A9 — Remove `COMMITMENT`

## Attempt 1

Treat commitment as merely a representation of future action.

## Failure witness

Two agents can represent the same future action with different speech-act force:

```text
one party requests future action
another party promises it
later an oath explicitly strengthens the relation
```

The represented future content may be nearly identical while the relational state changes.

## Attempt 2

Derive commitment from authority.

## Failure

An agent may bind itself to a future action without acquiring authority over another agent or over the target domain.

Surety likewise creates a responsibility relation that is not reducible to permission or command.

## Result

```text
PRIMITIVE
```

### Minimal form

```math
\boxed{
Commitment(actor,target\_future,beneficiary,scope,time,strength)
}
```

`promise`, `oath`, `surety`, and `vow` remain typed variants when needed for reverse reconstruction.

---

# A10 — Remove `AUTHORITY`

## Attempt 1

Infer authority from who actually performs an action.

## Failure witness — proposal / authorization / execution

A policy can be proposed by one actor, evaluated/authorized by another, and executed by the first after authority transfer.

Actual execution does not reconstruct who could authorize it.

## Failure witness — attempted correction

A subordinate can attempt to correct a senior allocator while lacking final decision authority.

If authority is inferred from action alone, the subordinate's physical intervention is incorrectly promoted into allocation authority.

## Failure witness — owner / delegate

Ownership and delegated operational authority can belong to different actors and can have explicit exclusions.

## Attempt 2

Infer authority from role labels.

## Failure

The same role can carry different scopes at different times, and formal status can diverge from local functional authority.

## Result

```text
PRIMITIVE
```

### Minimal form

```math
\boxed{
Authority(actor,action\_class,scope,target,time)
}
```

with delegation/authorization/override represented as changes or relations in this topology rather than one scalar `power` value.

---

# A11 — Remove asymmetric information topology

## Attempted reduction

Use per-agent `ACCESS` and `REPRESENTATION` states.

```math
\boxed{
InfoState_i(x,t)
:=
\langle Access_i(x,t),Representation_i(x,t)\rangle
}
```

Asymmetry exists whenever:

```math
\boxed{InfoState_i(x,t)\neq InfoState_j(x,t)}
```

## Counterexample test

This reconstructs:

```text
recognized / unrecognized identity
hidden comprehension
private objective / public proposal
controller knows planted provenance / inspected party does not
```

No additional topology primitive is required; topology is the graph induced by per-agent access and representation edges.

## Result

```text
DERIVABLE
```

---

# A12 — Remove persistent-object/function primitive

## Attempted reduction

```math
\boxed{
PersistentObject(x)
:=
EntityID(x)
+
\{State(x,t_k),Relation(x,t_k)\}_{k=1}^{n}
}
```

Changing function is represented as changing relation type over the same persistent entity.

## Counterexample test

This reconstructs:

```text
ordinary possession → collateral → identity evidence
clothing → manipulated evidence
transaction medium → hidden anomaly → explanation target
```

while preserving cases where physical same-object identity remains OPEN.

## Result

```text
DERIVABLE
```

---

# A13 — Remove ordering/priority primitive

## Attempted reduction

Represent each ordering as a typed relation dimension:

```math
\boxed{Order_{d}(a,b,t)}
```

where `d` may be stripped but remains structurally distinct, e.g.:

```text
inherited chronology
physical seating
resource allocation
assigned priority
authority succession
```

## Counterexample test

The architecture can hold simultaneously:

```math
Order_{d_1}(a,b)
\quad\land\quad
Order_{d_2}(b,a)
```

without contradiction.

This reconstructs known firstborn order together with deliberately reversed blessing priority, and age-aligned seating together with unequal resource share.

## Result

```text
DERIVABLE
```

### Reduction

No scalar `RANK` or generic `PRIORITY` primitive is admissible.

---

# A14 — Remove environment/trajectory primitive

## Attempted reduction

An environment is part of world state. A trajectory is an ordered sequence of state/event transitions.

```math
\boxed{
Trajectory_i
=
\langle State_i(t_0),Event_i(t_1),State_i(t_1),\dots\rangle
}
```

Different populations may share some environmental state while differing in resource, authority, location, or protection relations.

## Counterexample test

One famine can coexist with:

```text
protected settlement + nourishment + growth
```

and:

```text
money exhaustion + asset exchange + land transfer + standing levy
```

No special `ENVIRONMENT_CAUSES_TRAJECTORY` primitive is required.

## Result

```text
DERIVABLE
```

---

# A15 — Remove retrospective-meaning primitive

## Attempted reduction

A later explanation is a representation at `t_2` whose content references an event at `t_1<t_2`.

```math
\boxed{
RetrospectiveMeaning_i(e_{t_1},t_2)
:=
Representation_i(content=Cause/Purpose(e_{t_1}),t_2)
}
```

The earlier event record remains in the world/event graph.

## Counterexample test

This preserves simultaneously:

```text
proximate human action
later causal attribution
later purpose attribution
present observed downstream outcome
```

without rewriting the earlier event or earlier agents' information states.

## Result

```text
DERIVABLE
```

---

# 5. The representation ablation is the deepest discriminator

The most tempting aggressive reduction is:

```math
\boxed{Representation_i(x)\stackrel{?}{=}AccessibleState_i(x)}
```

The source corpus rejects it.

Three independent cases are sufficient:

```text
1. An agent accesses a genuine object and still constructs a false event history.
2. An agent represents a feared future that is not currently accessible because it has not happened.
3. An agent later attributes cause/purpose to a past event without changing that event.
```

Therefore:

```math
\boxed{
ACCESS\neq REPRESENTATION
}
```

This is not merely a naming preference. Their closures differ:

```text
ACCESS can be true while REPRESENTATION is false.
REPRESENTATION can concern an inaccessible or nonexistent future.
REPRESENTATION can contradict world state.
REPRESENTATION can be transmitted to create another agent's access event.
```

This ablation strongly earns `REPRESENTATION` as a primitive semantic state class.

---

# 6. The authority ablation also resists reduction

A generic role/action model cannot reconstruct all of:

```text
can propose but not decide
can authorize but not execute
can execute under delegated scope
can own while another controls operations
can attempt correction while lacking final allocation authority
```

Therefore authority is not a synonym for:

```text
role
capacity
ownership
actual action
status
```

The minimal retained object is action- and scope-relative:

```math
\boxed{
AUTHORITY = relation(actor,action\_class,scope,target,time)
}
```

No broader scalar is admitted.

---

# 7. Provisional minimal sufficient architecture

After the first ablation pass, the architecture separates into three layers.

## 7.1 Carrier basis

```math
\boxed{
B_{carrier}
=
\{
ENTITY\_ID,
STATE,
EVENT,
TYPED\_RELATION,
TIME
\}
}
```

These are required to preserve persistence, occurrence, relational state, and sequence.

## 7.2 Semantic irreducibles

```math
\boxed{
B_{semantic}
=
\{
ACCESS,
REPRESENTATION,
AUTHORITY,
COMMITMENT
\}
}
```

### ACCESS

Who can obtain which state/information through which channel.

### REPRESENTATION

What content an agent holds, reports, fears, predicts, explains, proposes, remembers, or infers, independently of whether the content matches world state.

### AUTHORITY

Who may determine, authorize, delegate, override, or execute an action under a specific scope.

### COMMITMENT

A future-directed binding relation whose force cannot be reconstructed from future content alone.

## 7.3 Mandatory meta-constraints

```math
\boxed{
M
=
\{
SOURCE\_PROVENANCE,
OPEN/UNCERTAINTY
\}
}
```

These are not domain primitives. They are conditions on acceptable reconstruction.

`SOURCE_PROVENANCE` ensures every abstract record remains traceable to the lexical structural corpus.

`OPEN` ensures the architecture can preserve an absent or unearned edge instead of silently completing it.

---

# 8. Derived structures under the minimal basis

The major stripped invariants now reconstruct as follows.

## Evidence / provenance-sensitive inference

```math
\boxed{
ENTITY\_ID
+ EVENT\ HISTORY
+ ACCESS
+ REPRESENTATION
\Rightarrow
\text{provenance-sensitive evidential behavior}
}
```

## Persistent object / changing function

```math
\boxed{
ENTITY\_ID
+ STATE_t
+ TYPED\_RELATION_t
+ TIME
\Rightarrow
\text{persistent object with changing role}
}
```

## Future / realization

```math
\boxed{
REPRESENTATION_t(target\ time>t)
+ EVENT/STATE_{t+n}
+ correspondence\ relation
\Rightarrow
\text{future-vs-realization structure}
}
```

## Obligation lifecycle

```math
\boxed{
COMMITMENT
+ REPRESENTATION(FutureAction)
+ TriggerState
+ EVENT\ HISTORY
\Rightarrow
\text{requested/promised/sworn/triggered/fulfilled/deferred lifecycle}
}
```

## Asymmetric information topology

```math
\boxed{
\{ACCESS_i,REPRESENTATION_i\}_{i=1}^{n}
\Rightarrow
\text{information topology}
}
```

## Typed order / priority

```math
\boxed{
TYPED\_RELATION(d_1)
\neq
TYPED\_RELATION(d_2)
\Rightarrow
\text{non-isomorphic orderings without contradiction}
}
```

## Environment / trajectory

```math
\boxed{
STATE_{environment}
+ STATE_{agent/group}
+ EVENT\ HISTORY
\Rightarrow
\text{trajectory}
}
```

## Retrospective meaning

```math
\boxed{
EVENT_{past}
+ REPRESENTATION_{later}(EVENT_{past})
\Rightarrow
\text{later causal/purpose account without event erasure}
}
```

---

# 9. What was actually eliminated

The minimization pass currently removes the need for standalone primitives named:

```text
EVIDENCE
PROVENANCE
PERSISTENT_OBJECT
FUTURE_STATE
OBLIGATION
INFORMATION_TOPOLOGY
ORDERING
ENVIRONMENT_TRAJECTORY
RETROSPECTIVE_MEANING
```

This does **not** mean those structures disappear.

It means they become explicit compositions whose ingredients remain inspectable.

```math
\boxed{
\text{remove named primitive}
\neq
\text{remove represented distinction}
}
```

That is the desired kind of compression.

---

# 10. What resisted minimization

The first pass could not eliminate:

```text
persistent identity
world/state representation substrate
event occurrence
access
representation
authority
commitment
temporal structure
```

without losing source distinctions.

The most important semantic failures were:

```math
\boxed{ACCESS\neq REPRESENTATION}
```

```math
\boxed{AUTHORITY\neq ACTION\neq ROLE\neq OWNERSHIP}
```

```math
\boxed{COMMITMENT\neq FUTURE\ CONTENT}
```

and the most important carrier failure was:

```math
\boxed{ROLE\ CHANGE\neq ENTITY\ REPLACEMENT}
```

---

# 11. Anti-cheating constraint

The architecture may not claim minimization by introducing a universal relation such as:

```text
RELATION(type="whatever-we-need")
```

and hiding every source distinction inside `type`.

A typed relation family counts as architecturally irreducible when removing its semantics causes a source-visible reconstruction failure.

This is why `AUTHORITY`, `ACCESS`, `REPRESENTATION`, and `COMMITMENT` remain named despite all being representable as graph edges/states at an implementation level.

The minimization target is semantic architecture, not serialization syntax.

---

# 12. Reconstruction criterion for the provisional basis

For any source structural record `g` in Genesis 1–50, an admissible abstraction must produce `a(g)` using only:

```math
B_{carrier}\cup B_{semantic}\cup M
```

such that:

```math
\boxed{
Reconstruct(a(g),provenance(g))
}
```

recovers every source distinction known to affect later structure, including explicit `OPEN` edges.

The provisional architecture is sufficient only if this remains true across all chapter records.

No external-domain example may be used to repair a failure during this phase.

---

# 13. Current minimal architecture

The first dependency/minimization pass therefore yields:

```math
\boxed{
\begin{aligned}
\mathcal A_{min}^{(1)}
=
&\underbrace{\{ENTITY\_ID,STATE,EVENT,TYPED\_RELATION,TIME\}}_{carrier}\\
&\cup\underbrace{\{ACCESS,REPRESENTATION,AUTHORITY,COMMITMENT\}}_{semantic\ irreducibles}\\
&\cup\underbrace{\{SOURCE\_PROVENANCE,OPEN\}}_{mandatory\ meta}
\end{aligned}
}
```

This is **provisional**, not frozen.

The next admissible operation is not to add applications or new concepts. It is to run **full-corpus reconstruction pressure** against this basis and attempt further ablations.

The two highest-value remaining reduction questions are:

```math
\boxed{
\textbf{Can COMMITMENT be reduced further without collapsing request / promise / oath / surety?}
}
```

and:

```math
\boxed{
\textbf{Can AUTHORITY be reduced into a more general scoped normative relation without losing propose / authorize / execute / override distinctions?}
}
```

No reduction is accepted until a reconstruction witness exists.

---

# 14. Governing result

The Genesis source corpus currently supports a much smaller architecture than the raw invariant inventory suggested.

The reduction is not:

```text
many words → few words
```

It is:

```math
\boxed{
\text{many recurring source structures}
\rightarrow
\text{few compositional primitives}
\rightarrow
\text{lossless reconstruction}
}
```

The operating maxim for the next pass is:

```math
\boxed{\textbf{kill every primitive the corpus does not force us to keep}}
```

while preserving the harder boundary:

```math
\boxed{\textbf{compression is valid only when source distinctions survive reconstruction}}
```
