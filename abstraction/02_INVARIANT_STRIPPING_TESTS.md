# Invariant Stripping Tests — Genesis 1–50

**Depends on:**
- `abstraction/00_ABSTRACTION_PROTOCOL.md`
- `abstraction/01_RELATION_INVENTORY.md`

**Purpose:** test whether candidate cross-chapter invariants remain intelligible and structurally identical after Genesis-specific vocabulary is removed  
**Status:** first stripping pass; not yet the final architecture

The test is deliberately adversarial.

For each candidate invariant:

```text
1. choose structurally separated source cases,
2. restate each case without proper names or domain-specific nouns,
3. identify the minimal common graph,
4. record source distinctions needed for reverse reconstruction,
5. mark SURVIVES / WEAKENS / REJECT.
```

A candidate survives only if:

```math
\boxed{
\text{domain nouns removed}
\land
\text{common structure remains intelligible}
\land
\text{source distinctions remain reconstructible}
}
```

---

# S1 — World / access / representation separation

## Source spread

- Genesis 3 — competing claims about a prohibited action and prospective consequence.
- Genesis 27 — multiple observations fail to produce correct identity discrimination.
- Genesis 31 — hidden objects survive an unsuccessful search.
- Genesis 42 — one participant recognizes the others while remaining unrecognized.

## Vocabulary-stripped cases

### Case A

```text
A rule and prospective consequence exist.
One agent receives a competing representation of the consequence.
The agent evaluates an observable object/state and acts.
The later world state differs from the earlier represented options.
```

### Case B

```text
A decision-maker receives several observations about a target identity.
The observations conflict or have limited discriminative power.
The decision-maker commits to an identity-dependent action.
Later information reveals that the inferred identity was wrong.
```

### Case C

```text
An object exists in a searched environment.
The search procedure does not locate it.
A searching agent therefore lacks evidence of its presence.
The object's world-state presence remains unchanged.
```

### Case D

```text
Two parties occupy one interaction.
Party A correctly identifies Party B.
Party B does not identify Party A.
Party A can therefore interpret incoming information under a richer identity model than Party B possesses.
```

## Minimal common graph

```math
\boxed{
W
\rightarrow
P_i(W)
\rightarrow
R_i(W)
}
```

with:

```math
\boxed{P_i(W)\neq W}
```

and often:

```math
\boxed{R_i(W)\neq R_j(W)}
```

## Reverse-reconstruction requirements

Must retain:

```text
agent identity
access channel
observation/search event
representation holder
certainty/OPEN state
later corrective evidence where present
```

## Result

```text
SURVIVES
```

### Survivor statement

```math
\boxed{\textbf{World state, accessible evidence, and agent representation are independent state variables.}}
```

---

# S2 — Provenance-sensitive evidence

## Source spread

- Genesis 31 — object present but search misses it.
- Genesis 37 — authentic garment altered/presented under false or missing provenance.
- Genesis 38 — exchanged tokens later recover correct actor/event provenance.
- Genesis 39 — authentic garment possession paired with false transfer narrative.
- Genesis 44 — genuine object deliberately planted before inspection.

## Vocabulary-stripped cases

### Case A — hidden object

```text
An object is present in a location.
Inspection fails to discover it.
The inspection result does not alter the object's actual presence.
```

### Case B — manipulated evidence

```text
An authentic object persists.
Its observable state is altered.
It is presented without correct production history.
A recipient correctly recognizes the object but infers a false event history.
```

### Case C — provenance restoration

```text
Authentic objects previously transferred between agents persist.
A later recipient presents the same objects with a correct claim about the earlier holder/action relation.
Recognition of the objects revises the accused agent's event model.
```

### Case D — false provenance narrative

```text
An object genuinely changes hands during an escape action.
The later holder accurately possesses the object but falsely reports why the transfer occurred.
The object supports an accusation whose event history conflicts with the primary event record.
```

### Case E — planted object

```text
A controller deliberately places an authentic object in another agent's container without that agent's knowledge.
A later search correctly locates the object.
The discovery resolves location but not agency or causal provenance.
```

## Minimal common graph

```math
\boxed{
O_{identity}
+
O_{state}
+
P_{object}
+
R_{provenance}
\rightarrow
R_{recipient}(event)
}
```

where:

```math
\boxed{
O_{identity}\text{ authentic}
\not\Rightarrow
R_{provenance}\text{ authentic}
}
```

## Reverse-reconstruction requirements

Must retain separately:

```text
object identity
object observable state
holder/location
production/transfer history
who knows provenance
reported provenance
recipient inference
```

## Result

```text
SURVIVES — STRONG
```

### Survivor statement

```math
\boxed{\textbf{Evidence value depends on provenance, not merely object authenticity or presence.}}
```

---

# S3 — Persistent object with changing relational function

## Source spread

- Genesis 28 / 31 / 35 — a material marker participates in place, memorial, vow-recall, and later marking relations.
- Genesis 37 — garment moves from clothing to manipulated evidence.
- Genesis 38 — personal tokens move from collateral to identity/provenance evidence.
- Genesis 42–43 — returned transaction objects move from hidden state to anomaly to explanation target.

## Vocabulary-stripped cases

### Case A

```text
One physical object is used in an immediate practical context.
It persists across time.
Later interactions attach memorial, identity, or historical-reference functions to it.
```

### Case B

```text
A personal object begins as ordinary possession.
It is exchanged as collateral.
It later becomes evidence linking a present claim to a prior interaction.
```

### Case C

```text
A transferred resource is hidden from its recipient.
Later discovery changes its informational role from transaction medium to unexplained anomaly.
A still-later account attempts to explain the anomaly.
```

## Minimal common graph

```math
\boxed{
ID(O_t)=ID(O_{t+n})
\quad\land\quad
Role(O_t)\neq Role(O_{t+n})
}
```

## Reverse-reconstruction requirements

Must retain:

```text
persistent object ID
state history
holder/location history
role-at-time relation
uncertainty about physical identity where source leaves it OPEN
```

## Result

```text
SURVIVES
```

### Survivor statement

```math
\boxed{\textbf{Object identity can persist while evidential, memorial, transactional, or relational function changes.}}
```

---

# S4 — Future representation is not future realization

## Source spread

- Genesis 15 / 17 — future land/population statements before realization.
- Genesis 32–33 — feared attack model and communicated route differ from later observed events.
- Genesis 40 — interpreted futures later correspond to two different realized outcomes; remembrance request does not.
- Genesis 41 — forecast drives intervention before forecast realization.
- Genesis 50 — one transfer obligation closes while another remains deferred.

## Vocabulary-stripped cases

### Case A

```text
An agent represents a possible future threat.
The agent prepares for that future.
A later encounter does not match the feared event model.
```

### Case B

```text
An interpreted future state is specified with a time horizon.
A later event corresponds to that specification.
A separate requested future action remains unrealized.
```

### Case C

```text
A future adverse environment is represented before arrival.
Present resource policy is changed in response.
The adverse environment later occurs.
Previously stored capacity is then available.
```

### Case D

```text
A future transfer action is requested and sworn.
One such obligation is later executed.
A second structurally similar obligation remains open at the terminal state.
```

## Minimal common graph

```math
\boxed{
R_t(F)
\neq
W_{t+n}
}
```

with optional:

```math
\boxed{R_t(F)\rightarrow A_t\rightarrow W_{t+n}}
```

and later:

```math
\boxed{Realizes(W_{t+n},R_t(F))}
```

only when supported.

## Reverse-reconstruction requirements

Must retain future-speech subtype:

```text
forecast
fear
promise
request
threat
route representation
blessing/future statement
```

## Result

```text
SURVIVES — FAMILY WITH REQUIRED SUBTYPES
```

### Survivor statement

```math
\boxed{\textbf{Representing a future state, acting because of it, and later realizing it are distinct relations.}}
```

---

# S5 — Persistent obligation state machine

## Source spread

- Genesis 28 / 31 — future-directed vow later recalled.
- Genesis 38 — future obligation reaches trigger condition without fulfillment.
- Genesis 40 — request for future remembrance lacks promise and is not executed.
- Genesis 43–44 — accepted surety becomes behaviorally active under adverse state.
- Genesis 47 / 49 / 50 — burial request → promise → oath → specification → execution.
- Genesis 50 — new body-transfer oath remains deferred.

## Vocabulary-stripped cases

### Case A

```text
An agent states a future commitment.
Later narration retrieves that commitment as relevant to present action.
```

### Case B

```text
A future transfer is represented as due after a condition is met.
The condition becomes true.
The promised relation is not established.
```

### Case C

```text
An agent guarantees another agent's return.
A later event threatens non-return.
The guarantor proposes bearing the adverse consequence instead.
```

### Case D

```text
A terminal-location request is accepted, then sworn.
Later speech refines destination provenance.
After the requesting agent dies, the obligated agent obtains authorization, performs transport, and completes the terminal action.
```

## Minimal common graph

```math
\boxed{
C_t
\rightarrow
C_{state,t+1}
\rightarrow
\dots
\rightarrow
\{FULFILLED,DEFERRED,UNFULFILLED,SUPERSEDED\}
}
```

## Reverse-reconstruction requirements

Must retain:

```text
creator
obligated party
beneficiary/target
commitment type
trigger
scope
oath/guarantee strengthening
terminal action
completion status
```

## Result

```text
SURVIVES — STRONG
```

### Survivor statement

```math
\boxed{\textbf{Future obligations are persistent stateful relations whose trigger and completion status must be represented separately.}}
```

---

# S6 — Authority routing is typed and staged

## Source spread

- Genesis 24 — principal objective and constraints, agent-generated criterion, family authorization, individual consent, departure.
- Genesis 39 — owner delegates broad household control but retains an explicit excluded relation.
- Genesis 41 — proposal → evaluation → administrator selection → material/public authority → implementation.
- Genesis 47 — ruler authorizes settlement while administrator executes placement/resource operations.
- Genesis 48 — subordinate attempts correction; senior decision-maker refuses and final allocation remains.

## Vocabulary-stripped cases

### Case A

```text
A principal delegates a task under constraints.
The delegated agent creates an operational selection procedure not explicitly supplied by the principal.
Other parties later authorize and an affected individual separately consents before movement occurs.
```

### Case B

```text
An owner delegates broad operational control to an agent.
One explicitly excluded relation remains outside the delegation.
```

### Case C

```text
An analyst interprets future risk and proposes policy.
A ruler evaluates the policy, selects the analyst as administrator, publicly grants authority, and the administrator executes the system-wide program.
```

### Case D

```text
A subordinate identifies what it considers an allocation error and attempts physical/verbal correction.
The senior allocator rejects correction.
The senior allocator's chosen state persists.
```

## Minimal common graph

```math
\boxed{
Authority(actor,action,scope,target,time)
}
```

with common staged path:

```math
\boxed{
PROPOSE
\rightarrow
EVALUATE
\rightarrow
AUTHORIZE
\rightarrow
DELEGATE
\rightarrow
EXECUTE
}
```

where stages may be absent or assigned to different actors.

## Reverse-reconstruction requirements

Must retain action-specific scope. A scalar `power` field is insufficient.

## Result

```text
SURVIVES — STRONG
```

### Survivor statement

```math
\boxed{\textbf{Authority is a typed topology over actions and scopes, not a single property of an agent.}}
```

---

# S7 — Asymmetric information topology

## Source spread

- Genesis 20 — different agents possess different facts about a marriage relation and its communication history.
- Genesis 27 — one actor knows an identity substitution that another does not.
- Genesis 37 — Reuben's private objective differs from the proposal heard by the group.
- Genesis 42–44 — one party recognizes identity, hears private speech, and controls hidden object states while the other party lacks those facts.

## Vocabulary-stripped cases

### Case A

```text
Two agents interact under different identity models of the same person.
The better-informed agent can predict the informational effect of statements the other agent treats as ordinary disclosure.
```

### Case B

```text
An agent communicates a proposal that is compatible with a hidden private objective.
Recipients can condition only on the public proposal; the reader has access to both.
```

### Case C

```text
A controller knows that an object was deliberately planted.
The inspected party does not know this.
The searcher knows only the object's discovered location.
Different participants therefore update from the same physical discovery under different provenance states.
```

## Minimal common graph

```math
\boxed{I_i(x)\neq I_j(x)}
```

with access graph:

```math
\boxed{Access(i,x,t)}
```

## Reverse-reconstruction requirements

Must retain per-agent information state rather than only a global fact store.

## Result

```text
SURVIVES — STRONG
```

### Survivor statement

```math
\boxed{\textbf{A shared interaction can contain different effective worlds because participants have different access to identity, provenance, intention, and history.}}
```

---

# S8 — Structural order and allocated priority are independent relations

## Source spread

- Genesis 25 — birth order and separately transacted birthright relation.
- Genesis 43 — age/birth-order seating and unequal portion allocation coexist.
- Genesis 48 — known firstborn order is deliberately opposed by hand/blessing priority.
- Genesis 49 — firstborn status remains while future excellency/authority is assigned differently.

## Vocabulary-stripped cases

### Case A

```text
Two agents have an inherited chronological order.
A separate status relation can be transferred or assigned without changing chronology.
```

### Case B

```text
A group is physically ordered according to inherited rank.
A resource allocation gives one non-leading member a larger share.
```

### Case C

```text
A first-ranked candidate is positioned to receive expected priority.
A senior allocator knowingly assigns priority to the second-ranked candidate instead.
The first-ranked fact is explicitly acknowledged and remains unchanged.
```

## Minimal common graph

```math
\boxed{
Order_{type_1}(a,b)
\neq
Order_{type_2}(a,b)
}
```

## Reverse-reconstruction requirements

Every ordering edge needs a relation type:

```text
birth
age
seating
resource share
blessing priority
authority
succession
```

## Result

```text
SURVIVES — STRONG
```

### Survivor statement

```math
\boxed{\textbf{Ordering is relation-specific; one ordering dimension does not determine another.}}
```

---

# S9 — Environment does not uniquely determine trajectory

## Source spread

- Genesis 13 — resource abundance plus limited shared land capacity produces separation.
- Genesis 26 — repeated well disputes produce different local outcomes.
- Genesis 41 — anticipated famine plus prior storage produces later response capacity.
- Genesis 47 — one famine coincides with household growth under protected settlement and staged asset exhaustion/concentration elsewhere.

## Vocabulary-stripped cases

### Case A

```text
Two resource-rich subgroups occupy a shared environment whose local capacity does not support continued co-location.
They separate geographically.
```

### Case B

```text
A resource conflict repeats across multiple sites.
Similar dispute form does not yield identical relational outcomes at every site.
```

### Case C

```text
A population receives advance information about a future environmental shock.
It accumulates a durable resource during favorable conditions.
When the shock arrives, stored capacity changes what actions remain available.
```

### Case D

```text
Two populations inhabit the same broad adverse environment.
One occupies a provisioned, institutionally protected settlement and grows.
Another exhausts successive asset classes and enters new ownership/labor relations.
```

## Minimal common graph

A single environment variable is insufficient.

Minimal candidate:

```math
\boxed{
Trajectory
=
f(EnvironmentState,ResourceState,InstitutionalPosition,PriorPreparation)
}
```

This is a descriptive dependency form, not yet a causal equation.

## Reverse-reconstruction requirements

Must retain starting state and institutional/resource position.

## Result

```text
SURVIVES — WEAKER / COMPOSITE
```

### Survivor statement

```math
\boxed{\textbf{A common environment constrains but does not uniquely determine system trajectory; starting state and access structure matter.}}
```

---

# S10 — Retrospective representation can add meaning without erasing history

## Source spread

- Genesis 31 — one shared household history receives multiple competing retrospective accounts.
- Genesis 42–44 — later participant reports add, compress, rephrase, or re-time earlier interaction details.
- Genesis 45 — a participant explicitly preserves the earlier human transfer action while adding a higher-level causal/preservation account.
- Genesis 50 — the same participant states both hostile human intent and beneficial higher-level purpose.

## Vocabulary-stripped cases

### Case A

```text
Multiple agents participate in one history.
Later they produce different explanations of what the history means or why it occurred.
The common past event graph remains distinct from each retrospective representation.
```

### Case B

```text
A later report of an earlier dialogue contains additional or re-timed detail.
The later report becomes new evidence about the past but does not overwrite the primary record.
```

### Case C

```text
An earlier harmful action is explicitly retained as an agent-level event.
A later participant adds a second causal/purpose account that treats the same trajectory as contributing to a broader preservation outcome.
The later account does not retroactively grant the earlier actors that purpose or information.
```

## Minimal common graph

```math
\boxed{
E_{past}
+
R_{i,t+n}(E_{past})
}
```

with:

```math
\boxed{
R_{i,t+n}(E_{past})
\not\Rightarrow
I_{agents,t}(R_{i,t+n})
}
```

## Reverse-reconstruction requirements

Must retain:

```text
primary event record
later speaker
later time
causal vs purpose claim
whether the later claim is narrator-certified or participant representation
earlier agent information state
```

## Result

```text
SURVIVES — STRONG
```

### Survivor statement

```math
\boxed{\textbf{Later representations can add causal or purposive structure without rewriting prior events or prior information states.}}
```

---

# 11. Survivors after first vocabulary stripping

The first pass leaves the following structures intact without requiring Genesis-specific vocabulary:

```text
S1  world/access/representation separation
S2  provenance-sensitive evidence
S3  persistent object / changing function
S4  future representation / realization separation
S5  persistent obligation state machine
S6  typed authority routing
S7  asymmetric information topology
S8  relation-specific ordering / priority
S9  environment × starting position → trajectory (composite)
S10 retrospective meaning without event erasure
```

These are not yet one architecture.

They overlap.

For example:

```text
S2 requires S1 and S7.
S5 uses S4 plus persistence.
S6 often conditions S5 and resource transitions.
S10 requires S1, provenance, memory, and temporal layering.
```

The next pass must therefore discover dependency structure among the survivors rather than merely listing them.

---

# 12. Emerging dependency graph

A preliminary dependency graph suggested by the stripping tests is:

```text
PERSISTENT IDENTITY
    ↓
WORLD / ACCESS / REPRESENTATION SEPARATION
    ↓
PER-AGENT INFORMATION TOPOLOGY
    ↓
REPORT / INFERENCE / PROVENANCE STRUCTURE
    ↓
ACTION + AUTHORITY ROUTING
    ↓
WORLD-STATE TRANSITION

PERSISTENCE
    ├── persistent objects
    ├── memory / retrospective representations
    └── obligations

TEMPORAL REPRESENTATION
    ├── future states
    ├── trigger conditions
    └── realization / non-realization

TYPED RELATION DIMENSIONS
    ├── ownership / possession / access
    ├── structural order / allocated priority
    ├── role / authority
    └── group / member state
```

This graph is still provisional.

It is, however, more constrained than the original five-layer sketch because the source corpus shows that **persistence, provenance, authority, and temporal status cannot be represented as decorations on a single state-transition loop**.

---

# 13. What did not survive as a primitive

Several tempting abstractions are currently rejected as too lossy.

## REJECT — one generic `INFORMATION` type

Why:

```text
observation
report
memory
belief
interpretation
prediction
fear
causal explanation
```

produce different downstream relations in the corpus.

## REJECT — one generic `POWER` scalar

Why:

```text
ownership
authority
delegation
authorization
allocation
execution
```

are demonstrably non-equivalent.

## REJECT — one generic `EVIDENCE` node without provenance

Why:

Genesis 31 / 37 / 38 / 39 / 44 directly show that object presence and authenticity do not determine event-history accuracy.

## REJECT — one generic `FUTURE` edge

Why:

```text
forecast
fear
promise
request
threat
blessing/future statement
```

have different commitment and realization semantics.

## REJECT — one generic `ORDER` scalar

Why:

birth, seating, resource share, blessing priority, authority, and succession can diverge.

## REJECT — `STATE → ACTION → STATE` alone

Why:

It cannot represent the source-level consequences of:

```text
asymmetric access
false representation
provenance corruption
memory
obligation persistence
authority routing
future non-realization
```

The simple transition loop remains useful, but it is not sufficient architecture.

---

# 14. Immediate next question

The source-stripping pass now changes the research question again.

It is no longer merely:

> What repeats across Genesis?

It is:

```math
\boxed{\textbf{What is the smallest typed architecture from which all ten surviving invariants can be reconstructed without Genesis vocabulary?}}
```

The next artifact should therefore be a dependency/minimization pass, not an external-domain test.

It should attempt to derive the survivors from a smaller set of primitives while preserving the explicit anti-collapse constraints documented here.
