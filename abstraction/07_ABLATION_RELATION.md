# Adversarial Ablation — RELATION

**Depends on:**
- `abstraction/00_ABSTRACTION_PROTOCOL.md`
- `abstraction/01_RELATION_INVENTORY.md`
- `abstraction/02_INVARIANT_STRIPPING_TESTS.md`
- `abstraction/03_MINIMAL_ARCHITECTURE.md`
- `abstraction/04_ABLATION_COMMITMENT_AUTHORITY.md`
- `abstraction/05_ABLATION_STATE_ACCESS.md`
- `abstraction/06_ABLATION_EVENT.md`

**Purpose:** test whether `RELATION` is a primitive historical carrier or can be reconstructed from `ENTITY`, event-like history, and temporal structure without hiding relational semantics inside another carrier  
**Status:** adversarial carrier ablation pass; no external-domain testing; `TIME` and `ENTITY` are explicitly out of scope as deletion targets in this file

The architecture entering this pass is the actual result of `06`:

```math
\boxed{
\mathcal A^{(4)}
=
\{ENTITY,RELATION,TIME,REPRESENTATION,COMMITMENT,AUTHORITY\}
+
\{SOURCE\_PROVENANCE,OPEN\}
}
```

`06` established:

```text
EVENT: DERIVABLE
```

by replacing a separate event carrier with an ordered history of temporally located relation instances.

Therefore this pass cannot casually restore `EVENT` and declare `RELATION` eliminated. Any event-centric replacement must itself work **without relational participant/role structure**.

The governing criterion is:

```math
\boxed{\textbf{A relation is primitive only if its truth/occurrence cannot be losslessly reconstructed from the retained carriers without reintroducing relational incidence under another name.}}
```

---

# 0. Kill hypotheses

Three attacks are required.

```math
\boxed{R\rightarrow EVENT}
```

```math
\boxed{R\rightarrow ENTITY+EVENT}
```

```math
\boxed{R\rightarrow EVENT+TIME}
```

Because `EVENT` was eliminated in `06`, these are counterfactual replacement tests rather than assumptions that `EVENT` is still primitive.

A successful reduction must show that an event-centric substrate can encode all source-required structure while **forbidding** any field or edge that already carries the removed relational semantics.

---

# 1. Anti-cheat rule — relational incidence may not hide inside another record

The hidden-parameter audit from `04`–`06` remains binding.

The following are invalid reductions:

```text
RELATION removed
→ EVENT(type="parent", actor=A, child=B)

RELATION removed
→ EVENT(kind="owns", owner=A, object=O)

RELATION removed
→ ENTITY(location=P)

RELATION removed
→ ENTITY(parent=A)

RELATION removed
→ EVENT(participants={actor:A,target:B,object:O})

RELATION removed
→ ASSERTION(predicate="recognizes", args=[A,B])
```

Why are these invalid?

Because each representation still contains the same mathematical object:

```text
predicate / role schema
+
arguments
+
incidence between them
```

Changing the outer noun from `RELATION` to `EVENT`, `ATTRIBUTE`, `ASSERTION`, `PROPERTY`, or `FIELD` does not eliminate relational structure.

Formally:

```math
\boxed{
\text{removed relational incidence}
\rightarrow
\text{same incidence encoded as event fields/attributes}
\Rightarrow
\text{ABLATION FAILS}
}
```

The decisive question is:

```text
If all generic relational association is forbidden,
what remaining carrier tells us that A is parent of B,
A is at P,
A recognizes B,
or O belongs to A?
```

If the answer is a structured tuple connecting those objects, the relation has returned.

---

# 2. What `RELATION` currently means

The current carrier is deliberately minimal.

It is not a fixed ontology such as:

```text
PARENT
OWNS
LOCATED_AT
RECOGNIZES
```

as separate architecture primitives.

It is the capacity to preserve a source-earned typed predication/incidence instance:

```math
\boxed{
r_k=\langle predicate,arguments,polarity,temporal\ support,provenance\rangle
}
```

with generic relation-instance identity so repeated occurrences are not collapsed.

The source predicate may remain locally specific until a quotient is earned.

Thus the ablation target is not the lexical vocabulary. It is the **generic structural fact that entities/records can stand in typed n-ary relations**.

---

# 3. Attack A — `RELATION → EVENT`

## 3.1 Easy-looking dynamic case

Suppose:

```text
A gives object O to B.
```

An event-centric encoding proposes:

```text
GIVE_EVENT(A,O,B,t)
```

But this is already an n-ary relation instance:

```math
GIVE(A,O,B,t).
```

If `GIVE_EVENT` has fields:

```text
actor=A
object=O
recipient=B
```

then the actor/object/recipient incidence is relational structure.

If those fields are removed, the event record no longer says **who gave what to whom**.

Therefore:

```math
\boxed{
\text{event identity alone}
\not\Rightarrow
\text{participant-role structure}
}
```

and:

```math
\boxed{
EVENT(kind,args,time)
\equiv
\text{temporally located typed relation instance}
}
```

for this purpose.

The proposed reduction is a renaming.

---

# 4. Attack A hard witness — Genesis 36 typed graph

Genesis 36 is an adversarial case because its native representation is explicitly **not primarily an event chain**.

The structural corpus requires simultaneously distinct edges for:

```text
spouse
parent
sibling
concubine
household
migration
inhabitation
duke/classification
family
place
king
succession
territory
```

The chapter's own structural result is that:

```math
\boxed{
\text{genealogical relation}
\neq
\text{authority relation}
\neq
\text{territorial relation}
\neq
\text{political succession relation}
}
```

Attempted event conversion:

```text
PARENT_EVENT(A,B)
DUKE_EVENT(A,G)
TERRITORY_EVENT(A,P)
KING_EVENT(A,P)
```

fails the parameter audit.

`PARENT_EVENT(A,B)` still means:

```math
PARENT(A,B)
```

and `DUKE_EVENT(A,G)` still means:

```math
DUKE\_OF(A,G).
```

No historical occurrence semantics were gained.

More importantly, many of these records are **direct relation assertions**, not narrated origin events from which the relation must be inferred.

The source tells us the topology.

Inventing unseen establishment events would violate the source boundary.

Therefore:

```math
\boxed{
\text{directly asserted persistent relation}
\not\Rightarrow
\text{recoverable from narrated establishment event}
}
```

### Result

```text
R → EVENT fails on directly asserted topology.
```

---

# 5. Attack B — `RELATION → ENTITY + EVENT`

A common rescue attempt is relation reification.

Instead of:

```text
PARENT(A,B)
```

create:

```text
entity X = parenthood-instance
```

and associate:

```text
X.actor=A
X.child=B
```

This fails immediately.

The associations:

```text
X → A as parent
X → B as child
```

are themselves relations.

Replacing them with positional fields:

```text
X=[A,B]
```

only hides role semantics in tuple position.

Without an interpretation of position 1 versus position 2, the tuple is not `PARENT(A,B)`.

That interpretation is relational typing.

Thus:

```math
\boxed{
\text{reified relation entity}
+
\text{participant slots}
=
\text{relation under another representation}
}
```

### Result

```text
R → ENTITY + EVENT fails the hidden-incidence audit.
```

---

# 6. Attack C — `RELATION → EVENT + TIME`

This attack asks whether persistent truths can be reconstructed by replaying history.

Possible strategy:

```text
acquisition event
→ infer ownership until transfer event
```

or:

```text
movement event
→ infer location until next movement
```

This works only when all of the following are available:

```text
1. an establishment event is actually narrated,
2. the event's semantic effect is known,
3. persistence until a terminating event is licensed,
4. no direct relation assertion overrides or supplements that history.
```

Genesis does not guarantee those conditions.

---

# 7. Persistent-relation witness R1 — kinship / lineage

Kinship is frequently supplied directly as topology:

```text
A is parent of B
A is spouse of B
A is sibling of B
member belongs to lineage/group
```

A birth event is not narrated for every genealogical edge.

Therefore an event-only architecture has two options.

### Option 1 — invent origin events

```text
unseen birth event establishes parent relation
```

Rejected:

```math
\boxed{\text{not source-supported}}
```

### Option 2 — encode parenthood directly as an event record

```text
PARENT_EVENT(A,B)
```

Rejected:

```math
\boxed{\text{relation renamed as event}}
```

Thus the corpus requires the ability to assert a relation whose establishment history may be absent.

### Result

```text
Kinship/lineage blocks event-history-only reconstruction.
```

---

# 8. Persistent-relation witness R2 — possession after acquisition

Genesis 23 supplies both a rich acquisition history and a later durable property relation.

The local chain includes:

```text
burial need
→ request
→ negotiation
→ price
→ payment
→ witnessed formalization
→ field/cave made sure for possession
→ burial use
```

The historical path matters.

But the later corpus also needs the continuing relation:

```text
specific property remains the relevant burial possession
```

many chapters after the negotiation episode.

An event-only reconstruction proposes:

```text
replay purchase event
+ assume possession persists until transfer
```

But the persistence rule must answer:

```text
what relation was established?
what is its subject?
what is its object?
what terminates it?
```

Those are exactly the semantics of the possession relation.

If encoded as:

```text
ACQUIRE_EVENT(effect="A possesses O")
```

relation is smuggled into `effect`.

If encoded only as:

```text
ACQUIRE_EVENT(A,O)
```

then the architecture needs a domain-specific rule:

```math
ACQUIRE(A,O,t_0)
\Rightarrow
POSSESSES(A,O,t>t_0)
```

and `POSSESSES` has reappeared in the derived truth language.

This does not show that every persistent relation must be stored eagerly.

It shows something narrower and more important:

```math
\boxed{
\textbf{event history can explain or derive a relation instance, but cannot eliminate relational truth as a representational form.}
}
```

### Result

```text
Acquisition history does not eliminate persistent relation semantics.
```

---

# 9. Persistent-relation witness R3 — location

A movement sequence may support:

```text
AT(A,P1)
→ MOVES(A,P1,P2)
→ AT(A,P2)
```

Could location be reconstructed from movement history alone?

Only partially.

The corpus also contains source assertions of location without a narrated arrival event and descriptions such as:

```text
person/object is in location P
population dwells in region P
object is inside container C
```

If event history is incomplete, direct spatial truth still must be representable.

Furthermore:

```text
MOVE_EVENT(A,P1,P2)
```

already contains spatial incidence between A, P1, and P2.

So movement cannot serve as a non-relational foundation for location.

### Result

```text
Location blocks pure event-derived reconstruction.
```

---

# 10. Occurrent-relation witness R4 — recognition

Genesis 42 requires:

```math
\boxed{
RECOGNIZES(A,B,t)
\land
\neg RECOGNIZES(B,A,t)
}
```

This is transient and information-bearing.

An event-centric rewrite:

```text
RECOGNITION_EVENT(A,B,t)
```

does not reduce anything.

It is the same predicate application with an event suffix.

If all participant roles are removed from the event record, the architecture loses who recognized whom.

Therefore even a highly occurrent relation does not become non-relational merely because it happens at a point in time.

### Result

```text
Occurrent predicates also require relational incidence.
```

---

# 11. Semantic-kernel witness R5 — AUTHORITY

`04` established the irreducible authority residue:

```math
AUTHORITY(actor,action\_class,scope,target,t).
```

Suppose generic `RELATION` is removed while `AUTHORITY` remains as a special semantic kernel.

This does not by itself fail—the architecture can permit specialized kernels.

But it reveals an important boundary:

```math
\boxed{AUTHORITY\text{ is itself relational in arity/structure.}}
```

Its irreducibility does **not** eliminate the need for a generic way to connect ordinary entities outside authority semantics.

Trying to use `AUTHORITY` as the universal association carrier would collapse non-authority facts into authority.

Thus specialized semantic kernels cannot replace the generic relation substrate.

---

# 12. Semantic-kernel witness R6 — COMMITMENT

The same reasoning applies to:

```math
COMMITMENT(actor,future\_content,t).
```

`COMMITMENT` is a specialized relation family earned by ablation.

It cannot represent:

```text
parenthood
location
possession
recognition
membership
spatial adjacency
resource quantity relation
```

without semantic corruption.

Therefore:

```math
\boxed{
\text{specialized relational kernels}
\neq
\text{generic relational carrier}
}
```

---

# 13. Semantic-kernel witness R7 — REPRESENTATION

`REPRESENTATION(holder,content,time,...)` also has relational form.

Could the whole world graph be moved into representations and thereby eliminate generic relations?

No.

That would collapse the source-earned distinction:

```math
\boxed{
\text{world/history relation}
\neq
\text{agent representation of relation/history}
}
```

A world assertion such as:

```text
object is in container C
```

must remain distinguishable from:

```text
agent represents object as being in container C
```

Therefore representation cannot serve as the generic relation substrate without destroying one of the strongest corpus invariants.

---

# 14. The circularity test created by `06`

`06` eliminated `EVENT` by showing:

```math
\boxed{
\text{historical occurrence}
=
\text{temporally located typed relation instance(s)}
}
```

Could `07` now eliminate relation by saying:

```math
\boxed{
\text{relation}
=
\text{event history}
}
```

Only if the restored event carrier can be defined independently of relation.

It cannot.

Any event record rich enough to preserve Genesis structure requires at least:

```text
predicate/kind
participants
participant roles or argument positions
object/target incidence
temporal support
```

That is the same typed n-ary predication structure that `RELATION` already provides.

Therefore the proposed cycle:

```math
RELATION\to EVENT\to RELATION
```

is not mutual derivability between two independent primitives.

It is two surface encodings of one deeper carrier form.

For the present architecture, the less redundant form is the one already retained after `06`:

```math
\boxed{\text{typed temporal relation instance}}
```

because it covers both persistent truths and occurrences without requiring two ontological classes.

---

# 15. Can `RELATION` be replaced by predicates + tuples?

Another possible reduction is:

```text
PREDICATE
+
ARGUMENT LIST
+
TIME
```

instead of `RELATION`.

This does not reduce the basis.

A predicate applied to an ordered argument tuple **is a relation instance**.

```math
\boxed{
P(a_1,\dots,a_n,t)
}
```

is precisely the mathematical form being called `RELATION` here.

Splitting it into:

```text
PREDICATE
ARGUMENT
INCIDENCE
```

would add carriers, not remove one.

Likewise, using hyperedges, facts, assertions, triples, quads, frames, or records changes representation syntax rather than the underlying requirement.

The minimization target is semantic/structural independence, not serialization format.

---

# 16. Relation-instance identity

`06` required generic record identity so repeated identical-looking occurrences are not collapsed.

That remains valid here.

Two relation instances may share:

```text
same predicate
same arguments
same coarse temporal label
```

while the source still distinguishes them by order or provenance.

Thus the retained carrier must support multiplicity:

```math
\boxed{
r_i\neq r_j}
```

when source provenance distinguishes two assertions/occurrences.

This is not a second primitive `EVENT_ID`.

It is generic instance identity for records in the temporal multirelation.

---

# 17. Parameter audit after failed deletion

Because the ablation fails, inspect the exact residue rather than restoring a large ontology.

The irreducible relation kernel requires only:

```text
predicate identity / typed dimension
ordered or role-resolved arguments
logical polarity where explicit
temporal support / order link
source provenance
relation-instance multiplicity
```

It does **not** require primitive objects for:

```text
STATE
EVENT
ACCESS
EVIDENCE
PROVENANCE-as-domain-object
FUTURE
OBLIGATION
ORDER
```

Those remain derived.

The relation kernel must also not silently merge local predicates whose distinction has not earned a quotient.

Thus:

```math
\boxed{\text{generic relation carrier}\neq\text{one generic semantic relation type}}
```

The carrier is generic; the predicate distinctions remain source-constrained.

---

# 18. Verdict

All three attempted reductions fail:

```text
R → EVENT              FAIL — event payload requires relational incidence; direct persistent topology lacks origin events
R → ENTITY + EVENT     FAIL — reified records require relational participant links or positional semantics
R → EVENT + TIME       FAIL — persistent/direct relations and event participation remain unreconstructible without relation semantics
```

Therefore:

```text
RELATION: IRREDUCIBLE CARRIER KERNEL
```

More precisely:

```math
\boxed{
\textbf{The corpus requires typed predication/incidence as a primitive representational form.}
}
```

The strongest reason is not merely that Genesis contains many relations.

It is:

```math
\boxed{
\textbf{neither historical occurrence, persistent topology, nor semantic-kernel structure can specify who/what stands in which role to whom/what without relational incidence.}
}
```

And the event-ablation result remains intact:

```math
\boxed{
EVENT\text{ remains derivable as a temporal-relation view.}
}
```

We do **not** need to restore `EVENT`.

---

# 19. Revised architecture

No cardinality reduction occurs in this pass.

The architecture remains:

```math
\boxed{
\mathcal A^{(5)}
=
\underbrace{\{ENTITY,RELATION,TIME\}}_{historical\ substrate}
\cup
\underbrace{\{REPRESENTATION,COMMITMENT,AUTHORITY\}}_{semantic\ kernels}
+
\underbrace{\{SOURCE\_PROVENANCE,OPEN\}}_{meta}
}
```

But `RELATION` is now narrower and better justified.

It does **not** mean:

```text
all semantics are one relation
```

It means:

```text
source-earned predicates require a primitive typed incidence form
```

while higher families are admitted only when separately earned.

The historical substrate can be pictured as:

```math
\boxed{
\mathcal H
=
\{r_k@T_k\}_{k=1}^{n}
}
```

where each `r_k` is a provenance-bearing typed relation instance over persistent entities or other addressable records.

`STATE` is a slice over `\mathcal H`.

`EVENT` is a temporal motif/view over `\mathcal H`.

`ACCESS` is an information-bearing projection over selected predicates in `\mathcal H`.

`PROVENANCE` in the domain sense is a history path through `\mathcal H`.

The next deletion frontier, if continued, is therefore not another large concept.

It is one of the remaining substrate carriers:

```math
\boxed{TIME\quad\text{or}\quad ENTITY}
```

Neither is attacked here.

---

# 20. Reopenability condition

Reopen `RELATION` only if a later minimization finds a genuinely non-relational primitive carrier that can encode:

```text
persistent topology
historical occurrence
participant roles
world-vs-representation separation
semantic-kernel arguments
multiplicity
```

without tuple-position semantics, role fields, participant edges, attributes, or predicate application.

Until such a witness exists:

```math
\boxed{\textbf{do not eliminate RELATION by changing serialization syntax.}}
```

The minimization frontier is now:

```math
\boxed{
ENTITY
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

with source provenance and `OPEN` outside the semantic basis.
