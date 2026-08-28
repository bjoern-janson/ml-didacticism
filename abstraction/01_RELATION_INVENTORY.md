# Cross-Chapter Relation Inventory — Genesis 1–50

**Depends on:** `abstraction/00_ABSTRACTION_PROTOCOL.md`  
**Source corpus:** `genesis/01_GENESIS_01.md` through `genesis/50_GENESIS_50.md`  
**Purpose:** inventory recurring relation types before vocabulary stripping  
**Status:** working inventory; not the final architecture

This file is deliberately conservative.

Its job is to identify repeated structural behavior while preserving local predicates until a merge is earned.

```math
\boxed{\textbf{preserve first; quotient later}}
```

The inventory uses four statuses:

```text
PRIMITIVE CANDIDATE  — appears structurally indispensable across unrelated cases
FAMILY CANDIDATE     — repeated behavior may support a higher-level relation family
KEEP DISTINCT        — corpus already shows downstream consequences from the distinction
OPEN MERGE           — relation similarity exists, but equivalence is not yet earned
```

---

# 1. Persistent entity identity

## Local predicates / relations

```text
is same person across time
is called
is renamed
is son/daughter of
is spouse of
is sibling of
is servant of
is prisoner under
is overseer over
is governor over
is member of household/group
is assigned new role
```

## Representative corpus behavior

- Jacob remains the same persistent person while `Jacob` and `Israel` labels alternate after renaming.
- Joseph remains one entity across son/brother, slave, overseer, prisoner, prison delegate, governor, husband, father, and Egyptian-name relations.
- Ephraim and Manasseh remain Joseph's sons while Genesis 48 adds a new Jacob-lineage/inheritance relation.
- Same surface names in Genesis 36 cannot safely be treated as identical entities without earned bridges.

## Candidate abstraction

```text
ENTITY_ID
LABEL_OF
ROLE_AT_TIME
KINSHIP_RELATION
MEMBERSHIP_RELATION
```

## Status

```text
PRIMITIVE CANDIDATE: persistent entity identity
KEEP DISTINCT: label identity vs entity identity
KEEP DISTINCT: role change vs entity replacement
KEEP DISTINCT: added relation vs erased prior relation
```

Core invariant:

```math
\boxed{\text{EntityID}\neq\text{NameString}\neq\text{Role}}
```

---

# 2. World state vs access state vs representation state

## Local predicates / relations

```text
exists
occurs
sees
hears
finds
inspects
recognizes
does not recognize
knows
does not know
is told
remembers
forgets
reports
believes / represents
fears
expects
infers
interprets
```

## Representative corpus behavior

- Genesis 12 / 20 repeatedly separate what is true from what one agent tells another and what the recipient knows.
- Genesis 27 separates multiple observations from correct discrimination.
- Genesis 31: hidden images exist, search occurs, search fails, Jacob remains unaware Rachel stole them.
- Genesis 37: Jacob correctly recognizes Joseph's coat but constructs a false event history.
- Genesis 39: Potiphar receives an accusation; the chapter narrates wrath and imprisonment but does not explicitly narrate his full belief proposition.
- Genesis 42–44: Joseph recognizes brothers while they do not recognize him; speakers mis-model who can understand their speech; object discovery fails to resolve provenance.
- Genesis 45: Jacob receives testimony, initially disbelieves, then updates after additional evidence.

## Candidate abstraction

```text
WORLD_STATE
ACCESS_STATE
REPRESENTATION_STATE
REPORT_EVENT
INFERENCE_EVENT
```

## Status

```text
PRIMITIVE CANDIDATE: W / P / R separation
KEEP DISTINCT: observation vs explanation
KEEP DISTINCT: report vs world state
KEEP DISTINCT: recognition vs disclosure
KEEP DISTINCT: testimony received vs testimony believed
KEEP DISTINCT: inspection result vs hidden world state
```

Core invariant:

```math
\boxed{
W_t
\neq
P_i(W_t)
\neq
R_i(W_t)
\neq
R_{i\to j}(W_t)
\neq
R_j(R_{i\to j})
}
```

---

# 3. Information transmission and audience topology

## Local predicates / relations

```text
asks
answers
reports
tells
sends message
speaks through intermediary
speaks through interpreter
speaks privately
withholds identity
reveals identity
restricts audience
adds detail in later report
compresses earlier event
```

## Representative corpus behavior

- Genesis 24 separates principal objective, constraints, agent-generated selection criterion, event, and later report.
- Genesis 31 preserves multiple retrospective accounts of one household history.
- Genesis 37 distinguishes Reuben's public proposal from narrator-revealed private objective.
- Genesis 39 preserves two wife-to-audience accusation reports with overlapping but non-identical wording.
- Genesis 42: brothers speak under a false model of Joseph's comprehension.
- Genesis 43–44: later participant reports add, compress, or re-time details relative to earlier narrated encounters.
- Genesis 45: Joseph restricts the immediate disclosure audience, but the event is not informationally sealed.
- Genesis 50: Joseph routes a request to Pharaoh through Pharaoh's house.

## Candidate abstraction

```text
MESSAGE
SENDER
RECIPIENT
AUDIENCE_SET
INTERMEDIARY
CONTENT
CONTENT_PROVENANCE
DISCLOSURE_STATE
```

## Status

```text
PRIMITIVE CANDIDATE: information-routing topology
KEEP DISTINCT: event vs later report of event
KEEP DISTINCT: direct vs intermediated communication
KEEP DISTINCT: restricted audience vs globally private information
OPEN MERGE: paraphrase vs inference vs omitted-detail recovery
```

Core rule:

```math
\boxed{\text{later report is data, not transparent replay}}
```

---

# 4. Observation, inquiry, interpretation, explanation

## Local predicates / relations

```text
observe changed state
ask cause
receive explanation
observe dream / private experience
report dream
interpret report
attribute interpretation authority
explain prior event
```

## Representative corpus behavior

- Genesis 40: Joseph observes sad faces before learning the dream cause.
- Genesis 40–41: private dream, dream report, interpretation, and later event correspondence are explicitly separate.
- Genesis 30: procedure, narrated outcome, and general mechanism remain distinct.
- Genesis 45 / 50: Joseph adds later causal/purpose accounts to a prior event history without deleting the brothers' proximate actions.

## Candidate abstraction

```text
OBSERVATION
INQUIRY
EXPLANATION
INTERPRETATION
CAUSAL_ATTRIBUTION
PURPOSE_ATTRIBUTION
```

## Status

```text
KEEP DISTINCT: observed state vs explanation
KEEP DISTINCT: private experience vs report vs interpretation
KEEP DISTINCT: procedure vs outcome vs mechanism
KEEP DISTINCT: proximate action vs later causal/purpose attribution
```

---

# 5. Action and completion state

## Local predicates / relations

```text
proposes
prepares
attempts
begins
interrupts
completes
fails to complete
flees
returns
searches
finds / does not find
```

## Representative corpus behavior

- Genesis 22: instruction, preparation, proximal intended action, interruption, and alternative provision are separate.
- Genesis 29: agreement, performance, delivered outcome, mismatch discovery, and renegotiation are separate.
- Genesis 37: initial murder plan, Reuben intervention, Judah sale proposal, and final transfer path differ.
- Genesis 44: brothers propose one consequence; steward revises it before implementation.
- Genesis 48: Joseph attempts correction; Jacob refuses; crossed allocation remains.

## Candidate abstraction

```text
ACTION_SPECIFICATION
ACTION_PREPARATION
ACTION_ATTEMPT
ACTION_INTERRUPTION
ACTION_COMPLETION
ACTION_FAILURE
POLICY_REVISION
```

## Status

```text
PRIMITIVE CANDIDATE: action completion state
KEEP DISTINCT: intended action vs completed action
KEEP DISTINCT: proposal vs implementation
KEEP DISTINCT: correction attempt vs final state
```

Core invariant:

```math
\boxed{\text{specified}\neq\text{attempted}\neq\text{completed}}
```

---

# 6. Authority topology

## Local predicates / relations

```text
commands
requests
proposes
authorizes
appoints
delegates
allocates
overrides
judges
releases
restrains
executes
inspects
```

## Representative corpus behavior

- Genesis 2 gives permission/prohibition without implying unlimited authority.
- Genesis 39 distinguishes Potiphar's ownership from Joseph's delegated household authority.
- Genesis 39–41 show repeated delegation under changing formal status.
- Genesis 41 distinguishes response proposal, proposal evaluation, administrator selection, symbols of office, and actual authority.
- Genesis 42–44: Joseph conditions access and detention without revealing identity.
- Genesis 47: Pharaoh authorizes settlement; Joseph executes resource administration; priestly exception limits system-wide compression.
- Genesis 48: Joseph proposes correction; Jacob retains decision authority over final allocation.

## Candidate abstraction

```text
AUTHORITY_EDGE(actor, action_type, scope, target, time)
DELEGATION_EDGE
AUTHORIZATION_EDGE
OVERRIDE_EDGE
```

## Status

```text
PRIMITIVE CANDIDATE: typed authority topology
KEEP DISTINCT: authority vs ownership
KEEP DISTINCT: propose vs authorize vs execute
KEEP DISTINCT: formal status vs functional responsibility
KEEP DISTINCT: role title vs action-specific authority
```

Core invariant:

```math
\boxed{\text{who may propose}\neq\text{who may authorize}\neq\text{who may execute}}
```

---

# 7. Ownership, possession, access, allocation, and resource state

## Local predicates / relations

```text
owns
possesses
uses
occupies
buys
sells
gives
receives
stores
allocates
transfers
exchanges
has access to
is denied access to
```

## Representative corpus behavior

- Genesis 13 separates resource abundance from viable co-location.
- Genesis 14 separates capture, recovery, and ownership/allocation.
- Genesis 23 distinguishes need, negotiated price, witnessed transfer, bounded possession, and later burial use.
- Genesis 31 distinguishes physical object possession from hidden-object knowledge.
- Genesis 41 separates environmental abundance, collection, storage, and later crisis access.
- Genesis 42–44: resource access is conditional and can coexist with detention constraints.
- Genesis 47 stages money exhaustion, livestock exchange, land transfer, person-status relation, seed provision, and standing fifth-part rule.

## Candidate abstraction

```text
RESOURCE_STATE
OWNERSHIP
POSSESSION
ACCESS
USAGE
ALLOCATION
TRANSFER
EXCHANGE
STORAGE
```

## Status

```text
KEEP DISTINCT: ownership vs possession vs access vs use
KEEP DISTINCT: transfer vs recovery vs allocation
KEEP DISTINCT: resource exists vs resource accessible
KEEP DISTINCT: same numerical fraction vs same institutional mechanism
```

Core invariant:

```math
\boxed{\text{resource presence}\neq\text{resource access}\neq\text{resource ownership}}
```

---

# 8. Persistent objects and provenance

## Local predicates / relations

```text
object persists
object changes holder
object changes location
object changes state
object changes function
object is hidden
object is discovered
object is presented as evidence
object provenance is reported
object provenance is misrepresented
```

## Representative corpus behavior

- Genesis 28 / 31 / 35: stone/pillar/place relations persist across time while exact same-object identity may remain OPEN.
- Genesis 31: hidden images remain present despite failed search.
- Genesis 37: coat persists, is manipulated with blood, and supports a false event inference.
- Genesis 38: signet/bracelets/staff move from collateral to identity/provenance evidence.
- Genesis 39: garment transfer is real, but the wife supplies a false causal account of how it came to be in her possession.
- Genesis 42–43: returned money changes from hidden state to feared anomaly to later steward explanation.
- Genesis 44: cup is deliberately planted; search establishes location, not agency.

## Candidate abstraction

```text
PERSISTENT_OBJECT
OBJECT_STATE
HOLDER
LOCATION
PROVENANCE_CHAIN
EVIDENTIAL_ROLE
```

## Status

```text
PRIMITIVE CANDIDATE: persistent object with changing relational function
KEEP DISTINCT: object authenticity vs provenance accuracy
KEEP DISTINCT: object location vs agent responsibility
KEEP DISTINCT: inspection success vs causal explanation
```

Core invariant:

```math
\boxed{
\text{object authenticity}
\neq
\text{provenance authenticity}
\neq
\text{event reconstruction accuracy}
}
```

---

# 9. Future representations and realization

## Local predicates / relations

```text
promises
predicts
fears
expects
threatens
blesses with future language
represents route
represents future population
requests future action
```

## Representative corpus behavior

- Genesis 2: prospective consequence is represented before later events.
- Genesis 15 / 17: future land/population statements remain distinct from present state.
- Genesis 27: future murder plan is not action.
- Genesis 32: Jacob's feared attack model is not Esau's later observed behavior.
- Genesis 33: communicated future route to Seir differs from narrated route to Succoth/Shechem.
- Genesis 40: interpreted futures later correspond to differentiated events, while a remembrance request does not become action.
- Genesis 41: future information becomes present infrastructure before the forecasted famine arrives.
- Genesis 48–49: future lineage statements remain future-typed within the chapter.
- Genesis 50: Jacob burial obligation closes; Joseph bone-transfer obligation remains deferred.

## Candidate abstraction

```text
FUTURE_REPRESENTATION
REALIZATION_EDGE
NONREALIZATION
DEFERRED_STATE
```

## Status

```text
PRIMITIVE CANDIDATE: future representation vs realized state
KEEP DISTINCT: forecast vs request vs promise vs fear vs threat
KEEP DISTINCT: future statement vs later event
OPEN MERGE: different future-speech subclasses under one higher family
```

Core invariant:

```math
\boxed{R_t(FutureState)\neq W_{t+n}}
```

until correspondence is narrated.

---

# 10. Obligations, commitments, guarantees, and terminal state

## Local predicates / relations

```text
requests
promises
vows
swears
guarantees
becomes surety
accepts obligation
triggers obligation
fulfills
defers
fails to fulfill
```

## Representative corpus behavior

- Genesis 24: principal instruction, family authorization, Rebekah query/consent, and departure are separate.
- Genesis 28 / 31: vow and later remembered vow remain provenance-bearing future relations.
- Genesis 38: represented future obligation concerning Shelah reaches trigger condition but is not fulfilled.
- Genesis 40: Joseph requests remembrance; no butler promise is narrated; request is not executed.
- Genesis 43–44: Judah's surety later becomes behaviorally active and produces a self-substitution proposal.
- Genesis 47 / 49 / 50: burial request, promise, oath, renewed specification, death, authorization, and execution remain distinct.
- Genesis 50: Joseph creates a new bone-transfer oath that remains unexecuted at book end.

## Candidate abstraction

```text
OBLIGATION
COMMITMENT_TYPE
TRIGGER_CONDITION
OBLIGATION_STATE
```

Possible states:

```text
PROPOSED
ACCEPTED
PROMISED
SWORN
TRIGGERED
FULFILLED
DEFERRED
UNFULFILLED
SUPERSEDED
```

## Status

```text
PRIMITIVE CANDIDATE: persistent obligation object
KEEP DISTINCT: request vs promise vs oath vs execution
KEEP DISTINCT: trigger condition reached vs obligation fulfilled
KEEP DISTINCT: obligation closed vs obligation still open
```

---

# 11. Ordering, priority, rank, and allocation

## Local predicates / relations

```text
is firstborn
is younger
is older
is placed before
is given larger portion
is seated in order
is assigned authority
is assigned future priority
```

## Representative corpus behavior

- Genesis 25: birth order and birthright transaction are separate.
- Genesis 27: identity substitution affects blessing interaction without changing actual biological identity.
- Genesis 43: brothers are seated according to birthright/youth while Benjamin receives fivefold portion.
- Genesis 48: Manasseh remains firstborn while Jacob deliberately sets Ephraim before him in blessing/priority.
- Genesis 49: Reuben remains firstborn yet is told he shall not excel; Judah receives a different authority future.

## Candidate abstraction

```text
STRUCTURAL_ORDER
ALLOCATED_PRIORITY
RESOURCE_ALLOCATION_ORDER
AUTHORITY_PRIORITY
```

## Status

```text
PRIMITIVE CANDIDATE: order is relation-typed, not scalar
KEEP DISTINCT: inherited order vs allocated priority
KEEP DISTINCT: seating order vs portion size
KEEP DISTINCT: biological order vs authority future
```

Core invariant:

```math
\boxed{\text{structural order}\neq\text{allocated priority}}
```

---

# 12. Spatial state, movement, route, dwelling, and boundary

## Local predicates / relations

```text
is at
moves to
leaves
returns
dwells
sojourns
owns land
uses land
crosses boundary
is forbidden crossing
is routed through
is buried at
```

## Representative corpus behavior

- Genesis 12–13: movement, dwelling, land use, and separation are distinct.
- Genesis 23: physical need, purchased field/cave, and burial use are distinct.
- Genesis 31: future boundary agreement constrains hostile crossing while retrospective conflict remains unresolved.
- Genesis 33: communicated route to Seir differs from narrated Succoth/Shechem movement.
- Genesis 36: birthplace, dwelling, inhabitation, reign-territory, and possession/habitation must remain distinct.
- Genesis 46: physical arrival in Egypt differs from later institutional settlement.
- Genesis 49–50: burial destination persists as a separate relation from current dwelling location.

## Candidate abstraction

```text
LOCATION_STATE
MOVEMENT_EDGE
ROUTE_REPRESENTATION
DWELLING_RELATION
BOUNDARY_RULE
TERMINAL_LOCATION
```

## Status

```text
KEEP DISTINCT: current location vs intended destination
KEEP DISTINCT: physical use vs ownership
KEEP DISTINCT: dwelling vs possession vs political territory
KEEP DISTINCT: temporary stop vs terminal destination
```

---

# 13. Population, group, and member-specific state

## Local predicates / relations

```text
member of group
population count
subgroup
household
tribe
city
collective action
individual exception
```

## Representative corpus behavior

- Genesis 10 / 36 require typed graphs rather than one undifferentiated family tree.
- Genesis 37 shows a brother group with non-identical information states; Reuben is not reducible to a single collective state.
- Genesis 42–44 repeatedly produce group-level action plus member-specific detention/accusation/consequence.
- Genesis 46 gives scope-qualified population totals and distinguishes household membership from participation in the migration leg.
- Genesis 47 shows a broad Egyptian institutional rule with an explicit priestly exception.
- Genesis 49 gives one twelve-tribe summary over heterogeneous local records.

## Candidate abstraction

```text
GROUP
MEMBER_OF
GROUP_STATE
MEMBER_STATE
SUBGROUP_EXCEPTION
POPULATION_COUNT(scope)
```

## Status

```text
PRIMITIVE CANDIDATE: group state and member state must coexist
KEEP DISTINCT: group label vs shared information state
KEEP DISTINCT: group-wide rule vs explicit exception
KEEP DISTINCT: population total vs counting scope
```

Core invariant:

```math
\boxed{\text{group membership}\not\Rightarrow\text{identical member state}}
```

---

# 14. Evaluation and state-dependent interpretation

## Local predicates / relations

```text
sees as good
sees as evil
is pleased / displeased
fears
judges outcome favorable
calls state good / bad
represents event as threat
```

## Representative corpus behavior

- Genesis 1 repeatedly separates state transformation from evaluation.
- Genesis 4 gives differentiated evaluation before later action.
- Genesis 32: approaching Esau + 400 men becomes Jacob's threat representation, but later observed encounter is peaceful.
- Genesis 40: baker sees butler interpretation as good and chooses to report his own dream; favorable first case does not determine second outcome.
- Genesis 43: brothers interpret Joseph's house invitation as threat despite reader-known hospitality instruction.
- Genesis 47: Egyptians represent Joseph's famine policy outcome as life-saving; participant evaluation remains provenance-bound.

## Candidate abstraction

```text
EVALUATION_STATE(agent, target, value, basis, time)
THREAT_MODEL
```

## Status

```text
KEEP DISTINCT: world state vs agent evaluation
KEEP DISTINCT: preparation generated by threat model vs target intent
OPEN MERGE: moral evaluation / utility evaluation / threat evaluation
```

---

# 15. Causal attribution and mechanism claims

## Local predicates / relations

```text
because
therefore
for this reason
caused by
sent by
meant for
made possible by
```

## Representative corpus behavior

- Genesis 15 / 30 repeatedly force separation of event correlation from full mechanism.
- Genesis 31 preserves multiple explanations for accumulated wealth/history.
- Genesis 37: manipulated evidence causes a recipient inference, but object authenticity does not establish event provenance.
- Genesis 41: forecast motivates present policy, which creates stored capacity later activated under famine.
- Genesis 45 / 50: Joseph gives retrospective divine-causal/purpose accounts while preserving human proximate action.

## Candidate abstraction

```text
CAUSAL_CLAIM
MECHANISM_CLAIM
PURPOSE_CLAIM
CAUSAL_CHAIN
```

## Status

```text
KEEP DISTINCT: observed correlation vs stated mechanism
KEEP DISTINCT: proximate action vs higher-level causal attribution
KEEP DISTINCT: causal attribution vs purpose attribution
KEEP DISTINCT: participant causal claim vs narrator-certified mechanism
```

Core rule:

```math
\boxed{\text{procedure is data; outcome is data; mechanism requires an additional edge}}
```

---

# 16. Memory, retrieval, and persistence of information

## Local predicates / relations

```text
remembers
forgets
recalls prior event
retrieves prior promise
quotes / reconstructs past speech
carries belief forward
revises belief
```

## Representative corpus behavior

- Genesis 31 recalls Genesis 28 pillar/vow relations.
- Genesis 37 creates a false household model that persists and shapes later behavior.
- Genesis 40 ends with explicit forgetting.
- Genesis 41 begins with memory recovery that reopens Joseph as an available interpreter.
- Genesis 45–46: Jacob moves from false death model to testimony-based revision to direct confirmation.
- Genesis 48–50 repeatedly retrieve prior promises, purchases, obligations, and histories.

## Candidate abstraction

```text
MEMORY_STATE
RETRIEVAL_EVENT
BELIEF_PERSISTENCE
BELIEF_REVISION
```

## Status

```text
PRIMITIVE CANDIDATE: information persistence over time
KEEP DISTINCT: information once received vs information currently active
KEEP DISTINCT: remembered representation vs original event
KEEP DISTINCT: belief accuracy vs causal efficacy of belief
```

---

# 17. Environmental state and preserved capability

## Local predicates / relations

```text
resource abundance
resource scarcity
famine
land capacity
stored resource
migration pressure
population growth
preserved option
```

## Representative corpus behavior

- Genesis 13: resource abundance plus land capacity produces separation pressure.
- Genesis 26: repeated well conflict produces changing local resource-access states.
- Genesis 41: future information becomes storage infrastructure before famine.
- Genesis 42–45: famine creates cross-region dependence on the Egyptian resource system.
- Genesis 47: one environmental shock coexists with sharply different household/population trajectories under different institutional/resource positions.

## Candidate abstraction

```text
ENVIRONMENT_STATE
CAPACITY_STATE
RESOURCE_PRESSURE
PRESERVED_CAPABILITY
```

## Status

```text
FAMILY CANDIDATE: environment × resource × institutional position
KEEP DISTINCT: environment condition vs population trajectory
KEEP DISTINCT: resource abundance vs access vs storage
```

Strong recurring pattern:

```math
\boxed{
\text{future information}
\rightarrow
\text{present preparation}
\rightarrow
\text{preserved capability under later adverse state}
}
```

This is a structural pattern, not yet a general theory of intelligence or adaptation.

---

# 18. Candidate top-level type set

The inventory currently supports at least the following high-level types without requiring Genesis-specific vocabulary:

```text
ENTITY
GROUP
POPULATION
OBJECT
PLACE
RESOURCE
ROLE
STATE
WORLD_STATE
ACCESS_STATE
REPRESENTATION_STATE
MESSAGE
OBSERVATION
INFERENCE
ACTION
AUTHORITY_EDGE
OBLIGATION
FUTURE_REPRESENTATION
EVALUATION
CAUSAL_CLAIM
PURPOSE_CLAIM
MOVEMENT_EDGE
OWNERSHIP
POSSESSION
ACCESS
ALLOCATION
PERSISTENT_OBJECT
MEMORY_STATE
ENVIRONMENT_STATE
UNCERTAINTY / OPEN_EDGE
```

This set is intentionally redundant at this stage.

No attempt should yet be made to minimize it.

---

# 19. Distinctions already strong enough to prohibit early merging

The following pairs have repeatedly shown source-level consequences and should remain separate during the next pass:

```math
\boxed{\text{world state}\neq\text{agent representation}}
```

```math
\boxed{\text{observation}\neq\text{interpretation}}
```

```math
\boxed{\text{event}\neq\text{report of event}}
```

```math
\boxed{\text{recognition}\neq\text{disclosure}\neq\text{mutual recognition}}
```

```math
\boxed{\text{object location}\neq\text{object provenance}\neq\text{agent responsibility}}
```

```math
\boxed{\text{proposal}\neq\text{authorization}\neq\text{execution}}
```

```math
\boxed{\text{ownership}\neq\text{possession}\neq\text{access}\neq\text{use}}
```

```math
\boxed{\text{request}\neq\text{promise}\neq\text{oath}\neq\text{fulfillment}}
```

```math
\boxed{\text{future statement}\neq\text{realized state}}
```

```math
\boxed{\text{structural order}\neq\text{allocated priority}}
```

```math
\boxed{\text{group label}\neq\text{identical member state}}
```

```math
\boxed{\text{same quantity}\neq\text{same mechanism}}
```

```math
\boxed{\text{same label}\neq\text{same entity}}
```

```math
\boxed{\text{formal status}\neq\text{functional responsibility}}
```

```math
\boxed{\text{correlation}\neq\text{mechanism}}
```

```math
\boxed{\text{causal attribution}\neq\text{purpose attribution}}
```

---

# 20. First recurring invariant structures

These are not yet the final architecture. They are cross-chapter patterns that now have enough independent support to deserve dedicated comparison in the next pass.

## I1 — Representation-mediated action

```math
\boxed{W\rightarrow P\rightarrow R\rightarrow A\rightarrow W'}
```

with missing edges allowed.

## I2 — Provenance-sensitive evidence

```math
\boxed{
\text{object state}
+
\text{provenance representation}
\rightarrow
\text{recipient event model}
}
```

## I3 — Persistent object / changing function

```math
\boxed{O_t=O_{t+n}\quad\land\quad role_t(O)\neq role_{t+n}(O)}
```

## I4 — Future representation / later correspondence

```math
\boxed{R_t(F)\quad\text{separate from}\quad W_{t+n}}
```

with optional later realization edge.

## I5 — Persistent obligation

```math
\boxed{C_t\rightarrow C_{t+1}\rightarrow\dots\rightarrow\{fulfilled,deferred,unfulfilled\}}
```

## I6 — Authority routing

```math
\boxed{
\text{proposal}
\rightarrow
\text{evaluation}
\rightarrow
\text{authorization}
\rightarrow
\text{delegation}
\rightarrow
\text{execution}
}
```

where steps may be absent or performed by different entities.

## I7 — Asymmetric information topology

```math
\boxed{I_i(x)\neq I_j(x)}
```

within one shared interaction.

## I8 — Structural order / allocated priority split

```math
\boxed{O_{inherited}\neq O_{allocated}}
```

without changing the underlying identity relation.

## I9 — Environment × position → trajectory

```math
\boxed{
\text{same broad environment}
+
\text{different resource/institutional states}
\rightarrow
\text{different trajectories}
}
```

## I10 — Retrospective meaning without event erasure

```math
\boxed{
E_{past}
+
R_{later}(E_{past})
}
```

where the later explanation can add causal or purposive structure without rewriting the earlier event or earlier agent knowledge.

---

# 21. Immediate next operation

The next artifact should compare the invariant candidates above across deliberately unrelated chapters.

For each invariant candidate:

1. select multiple source cases from different narrative contexts,
2. rewrite each case in typed vocabulary,
3. strip Genesis-specific labels,
4. identify the minimal common graph,
5. record what distinctions must be retained for reverse reconstruction,
6. reject any abstraction that needs Genesis vocabulary to remain intelligible,
7. reject any abstraction that cannot reconstruct the source-level structural differences.

The next question is therefore not:

> What is the architecture?

It is:

```math
\boxed{\textbf{Which candidate invariants remain identical after independent vocabulary stripping?}}
```

Only those survivors should enter the first actual vocabulary-free architecture draft.
