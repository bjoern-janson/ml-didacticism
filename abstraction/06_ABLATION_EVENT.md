# Adversarial Ablation — EVENT

**Depends on:**
- `abstraction/00_ABSTRACTION_PROTOCOL.md`
- `abstraction/01_RELATION_INVENTORY.md`
- `abstraction/02_INVARIANT_STRIPPING_TESTS.md`
- `abstraction/03_MINIMAL_ARCHITECTURE.md`
- `abstraction/04_ABLATION_COMMITMENT_AUTHORITY.md`
- `abstraction/05_ABLATION_STATE_ACCESS.md`

**Purpose:** test whether `EVENT` is a primitive historical carrier or a derived view over temporally indexed typed relation instances  
**Status:** adversarial carrier ablation pass; no external-domain testing; no further carrier is attacked in this file

The architecture entering this pass is:

```math
\boxed{
\mathcal A^{(3)}
=
\{ENTITY,EVENT,RELATION,TIME,REPRESENTATION,COMMITMENT,AUTHORITY\}
+
\{SOURCE\_PROVENANCE,OPEN\}
}
```

The governing criterion is:

```math
\boxed{\textbf{An architectural carrier is primitive only if removing it destroys source-earned historical structure that cannot be reconstructed by the retained carriers.}}
```

This pass attacks one candidate only:

```math
\boxed{EVENT}
```

---

# 0. The naive kill hypothesis

The first proposed reduction is:

```math
\boxed{
EVENT(e)
\stackrel{?}{=}
\Gamma(t^+)-\Gamma(t^-)
}
```

where:

```math
\Gamma(t)=\{r\mid r\text{ holds at }t\}.
```

This hypothesis is immediately too weak.

The Genesis corpus contains historically important occurrences that do not produce the intended terminal relational change:

```text
failed attempts
interrupted actions
failed searches
rejected corrections
questions
warnings
reports
requests
weeping
remembering
```

Therefore:

```math
\boxed{
\textbf{EVENT is not equivalent to successful relational change.}
}
```

But that does **not yet** prove that `EVENT` must remain a primitive.

A second reduction remains available:

```math
\boxed{
\text{historical occurrence}
\stackrel{?}{=}
\text{temporally bounded typed relation instance}
}
```

This is the actual ablation tested below.

---

# 1. Anti-cheat constraints

The hidden-parameter audit from `04` and `05` remains binding.

The following are invalid reductions:

```text
EVENT removed
→ RELATION(type="event", ...)

EVENT removed
→ RELATION(..., occurrence=true)

EVENT removed
→ RELATION(..., event_id=E17)

EVENT removed
→ ENTITY(kind="event")
```

These merely move the primitive.

However, source-earned predicates such as:

```text
moves
searches
attempts
interrupts
asks
answers
reports
weeps
binds
opens
finds
refuses
```

may remain as typed relation assertions.

This is the same discipline used in `05` to eliminate the umbrella `ACCESS` primitive while retaining `RECOGNIZES`, `UNDERSTANDS`, `SEARCHES`, and other source-required distinctions.

Thus:

```math
\boxed{
\text{local occurrent predicate survives}
\not\Rightarrow
\text{EVENT umbrella is primitive}
}
```

The retained `RELATION` carrier is understood as a **temporal multirelation**: relation assertions are individual records with arguments, temporal support/order, polarity where needed, and source provenance. Repeated assertions are therefore not collapsed merely because predicate and arguments match.

No generic `event` bit is added.

---

# 2. Required test classes

A successful `EVENT` ablation must reconstruct all three classes:

```text
A. occurrence associated with relational change
B. occurrence without successful target-state change
C. occurrence whose own happening is source-significant
```

It must additionally preserve:

```text
occurrence order
participants
attempt/interruption/completion distinctions
search procedure and result
speech occurrence even without downstream action
provenance history
endpoint-equivalent but historically different trajectories
```

---

# 3. Class A — occurrence with relational change

Movement is the easy case.

A state/event encoding might store:

```text
AT(A,P1)
MOVE_EVENT(A,P1→P2,t)
AT(A,P2)
```

The event-free encoding is:

```text
AT(A,P1) over T0
MOVES(A,P1,P2) at t_m
AT(A,P2) over T1
```

`MOVES` is a source-earned dynamic predicate represented as one temporally bounded relation assertion.

The transition can still be queried as:

```math
\boxed{
AT(A,P1)
\rightarrow
MOVES(A,P1,P2)
\rightarrow
AT(A,P2)
}
```

No separate `EVENT` node contributes additional source information.

### Result

```text
EVENT not required for occurrence-with-change cases.
```

---

# 4. Class B1 — failed correction attempt with unchanged target allocation

Source discriminator: Genesis 48.

The chapter preserves:

```text
right hand remains on younger son
subordinate sees mismatch
subordinate is displeased
subordinate attempts to move senior agent's hand
subordinate verbally requests correction
senior agent refuses
senior allocation remains
```

The target allocation before and after the correction attempt can remain the same.

Therefore the naive delta model fails:

```math
\boxed{
\Delta\Gamma_{target}\approx 0
\quad\not\Rightarrow\quad
\text{nothing happened}
}
```

But `EVENT` is still not forced.

Represent directly:

```text
HAND_ON(senior,right,younger) over interval
SEES(subordinate,HAND_ON(...)) at t1
DISPLEASES(subordinate,observed-allocation) at t2
ATTEMPTS(subordinate,move-hand,younger→elder) at t3
REQUESTS(subordinate,senior,put-right-hand-on-elder) at t4
REFUSES(senior,requested-correction) at t5
HAND_ON(senior,right,younger) continues
```

The failed attempt survives as a relation assertion even though the intended allocation relation never changes.

No `EVENT` node is necessary.

### Hidden-parameter audit

Passes.

No field such as:

```text
occurred=true
```

is required. `ATTEMPTS`, `REQUESTS`, and `REFUSES` are the source-level predicates whose occurrence the text requires.

### Result

```text
Failed attempt does not force primitive EVENT.
```

---

# 5. Class B2 — interrupted action

Source discriminator: Genesis 22.

The source-level structure requires:

```text
instruction
preparation
movement
binding
hand stretched forth
taking knife
proximal action toward slaying
interruption
new instruction
alternative provision
```

The intended terminal relation:

```text
Isaac slain
```

is not established.

Therefore:

```math
\boxed{
\text{specified action}
\neq
\text{proximal attempted action}
\neq
\text{completed action}
}
```

Again, endpoint differences alone are insufficient.

But the event-free relation history can preserve the sequence directly:

```text
BINDS(actor,target) at t1
STRETCHES_HAND(actor) at t2
TAKES(actor,knife) at t3
DIRECTED_TOWARD(actor,slay,target) at t4
CALLS(interrupting-speaker,actor) at t5
PROHIBITS(interrupting-speaker,harm-to-target) at t6
OBSERVES(actor,alternative-object) at t7
OFFERS(actor,alternative-object) at t8
```

with temporal order:

```math
\boxed{t_1<t_2<t_3<t_4<t_5<t_6<t_7<t_8}
```

The exact local predicates remain provenance-bound to the source parse.

No completed slaying relation is inserted.

### Result

```text
Interrupted action does not force primitive EVENT.
```

---

# 6. Class B3 — failed search versus successful search

The search pair is a strong discriminator because the procedure itself matters independently of whether an object is found.

## Genesis 31 — failed discovery

Required history:

```text
hidden object exists
searcher searches relevant locations
object is not discovered
object remains present
```

Represent:

```text
OBJECT_AT(O,L) over interval
SEARCHES(searcher,location_1) at t1
SEARCHES(searcher,location_2) at t2
...
source-supported non-discovery result
OBJECT_AT(O,L) continues
```

The search relations remain in history despite no successful discovery transition.

## Genesis 44 — successful ordered discovery

Required history:

```text
sacks opened
search proceeds eldest → youngest
cup located in youngest brother's sack
```

Represent:

```text
OPENS(person_i,sack_i) at t0
SEARCHES(steward,sack_eldest) at t1
SEARCHES(steward,sack_next) at t2
...
SEARCHES(steward,sack_youngest) at tn
FINDS(steward,cup,sack_youngest) at tn+
```

The distinction:

```math
\boxed{
\text{search procedure}
\neq
\text{search result}
}
```

survives without an `EVENT` carrier.

### Result

```text
Search procedure/result structure does not force primitive EVENT.
```

---

# 7. Class C — speech acts whose occurrence matters even without later execution

Speech is a particularly important test because a request, warning, report, accusation, question, promise, or oath can occur even if no later physical action realizes its content.

A reduction that stores only downstream consequences fails.

But an event-free temporal relation history can store the speech act itself:

```text
ASKS(A,B,content) at t1
REPORTS(A,B,content) at t2
ACCUSES(A,B,content) at t3
WARNS(A,B,content) at t4
REQUESTS(A,B,future-content) at t5
```

where the representation content is carried by the retained `REPRESENTATION` kernel when the source distinction requires a represented proposition rather than merely a communicative surface.

For commitment-bearing speech:

```text
SWEARS(A,content) at t
+
COMMITMENT(A,content) begins/strengthens relative to t
```

For authority-bearing speech:

```text
AUTHORIZES(A,B,action-scope) at t
+
AUTHORITY(B,scope,...) begins/changes where source earns it
```

Thus:

```math
\boxed{
\text{speech occurrence}
\neq
\text{later performance}
}
```

remains fully representable.

No generic event object is necessary.

### Result

```text
Speech-act occurrence does not force primitive EVENT.
```

---

# 8. Endpoint-equivalent histories

A decisive challenge is whether two histories with identical terminal relation configurations can remain distinct.

Suppose:

```text
History H1:
A attempts correction
B refuses
original allocation persists
```

and:

```text
History H2:
no correction is attempted
original allocation persists
```

Then:

```math
\boxed{
\Gamma_{H1}(t_{final})
=
\Gamma_{H2}(t_{final})
}
```

but the histories are not equivalent.

The event-free temporal relation model preserves:

```text
H1 contains ATTEMPTS + REQUESTS + REFUSES assertions
H2 does not
```

Therefore:

```math
\boxed{
\text{same final relation slice}
\not\Rightarrow
\text{same temporal relation history}
}
```

This is the important correction to the naive event-ablation hypothesis.

The historical substrate is not merely endpoint snapshots.

It is the **ordered history of relation assertions**.

---

# 9. Event ordering

The corpus repeatedly distinguishes sequences such as:

```text
proposal → acceptance → implementation
search → non-discovery → later confrontation
attempt → interruption → substitution
promise → oath → trigger → execution
```

A final graph slice cannot recover these sequences.

But `TIME` already exists independently and can order relation instances:

```math
\boxed{
R_1@t_1
<
R_2@t_2
<
R_3@t_3
}
```

or, where only partial order is earned:

```math
\boxed{Before(R_1,R_2)}
```

No additional event-order primitive is required.

Thus:

```math
\boxed{
\text{occurrence order}
=
\text{temporal order over relation instances}
}
```

for the purposes of the current corpus.

---

# 10. Occurrence identity

This is the strongest candidate for rescuing `EVENT`.

The question is:

```math
\boxed{
\text{Can two distinct occurrences of the same predicate be represented without separate event entities?}
}
```

Yes, provided `RELATION` is a temporal **multirelation**, not a mathematical set that collapses duplicate assertions.

Two occurrences may be:

```text
r_1 = SPEAKS(A,B,C) at t1
r_2 = SPEAKS(A,B,C) at t2
```

with:

```math
\boxed{r_1\neq r_2}
```

because they are distinct relation-assertion records with different temporal position and provenance.

If the source distinguishes multiple occurrences at one coarse narrative time, the temporal model may preserve a source-earned partial order or multiplicity rather than inventing precise clock time.

This does not require:

```text
event_id
```

because relation instances already have record identity for source provenance and graph reference.

### Hidden-parameter audit

Passes only under this condition:

```math
\boxed{
\text{relation-instance identity is generic to all relation records, not a special identity granted only to occurrent predicates.}
}
```

If only event-like relations receive special IDs, `EVENT` has been smuggled back in.

---

# 11. Event bundling / composite occurrences

A second rescue attempt is that one ordinary-language event may contain many local predicates.

For example, a search episode may contain:

```text
opening containers
ordered inspection
object discovery/non-discovery
recipient reaction
```

An interrupted action may contain:

```text
preparation
proximal movement
interruption
replacement action
```

Does this require a primitive event node to bundle the substructure?

For the current corpus, no.

The bundle can be reconstructed as a graph motif over:

```text
shared participants
shared/ordered temporal interval
shared target/object where source earns it
source-local provenance
explicit causal/sequence relations where narrated
```

Define only as an analytic view:

```math
\boxed{
EventView(Q)
:=
\text{selected temporally related relation instances satisfying query }Q
}
```

This view may be useful for chapter summaries, but it is not part of the primitive basis.

### Important limit

If a later corpus forces reference to an occurrence that cannot be reconstructed from its constituent relation assertions and temporal/provenance structure, `EVENT` must be reopened.

Current Genesis evidence does not yet force that reopening.

---

# 12. Provenance without EVENT

Earlier passes derived semantic provenance from persistent identity plus historical ancestry.

With `EVENT` removed, the ancestry becomes an ordered path over relation instances rather than event nodes.

For a persistent object `O`:

```math
\boxed{
History(O)
=
\langle r_1,r_2,\dots,r_n\rangle
}
```

where the relevant relation instances may include:

```text
POSSESSES
TRANSFERS
HIDES
ALTERS
PRESENTS
PLANTS
FINDS
REPORTS-ABOUT
```

and `TIME` supplies order.

Thus a Genesis 44-style provenance chain remains:

```text
controller instructs placement
→ intermediary places object
→ target departs unaware
→ search occurs
→ object is found
```

without requiring any generic event entity.

Actual history and reported history remain distinct because `REPRESENTATION` can target a relation-history fragment that differs from the source-supported relation history.

Therefore:

```math
\boxed{
\text{provenance does not rescue EVENT as primitive.}
}
```

---

# 13. Parameter audit

After removing `EVENT`, inspect the retained architecture for hidden reintroduction.

## Forbidden

```text
RELATION(..., event=true)
RELATION(..., occurrence_type=...)
ENTITY(kind=event)
event_id
EVENT_STATUS
```

## Allowed because independently required

```text
source predicate identity
relation-instance identity
relation arguments / participants
temporal support / order
logical polarity
source provenance
REPRESENTATION
COMMITMENT kernel
AUTHORITY kernel
OPEN
```

No single retained parameter answers:

```text
"is this an event?"
```

The architecture simply records that particular source predicates hold/occur over particular temporal supports.

The event/non-event distinction becomes an analytic classification over relation predicates, not a semantic carrier bit.

The hidden-parameter audit therefore passes.

---

# 14. Verdict

The naive hypothesis fails:

```math
\boxed{
EVENT
\neq
\Gamma(t^+)-\Gamma(t^-)
}
```

because failed, interrupted, non-state-changing, and speech occurrences matter.

But the stronger ablation succeeds:

```math
\boxed{
\text{historical occurrence}
=
\text{temporally located typed relation instance(s)}
}
```

for every tested Genesis discriminator.

Therefore:

```text
EVENT: DERIVABLE
```

More precisely:

```math
\boxed{
\textbf{EVENT is a derived temporal-relation view, not a primitive carrier.}
}
```

The corpus still requires a history of what happened.

What it does **not** require is a separate ontological category called `EVENT` in addition to temporally indexed relation assertions.

---

# 15. Revised architecture

Removing `EVENT` yields:

```math
\boxed{
\mathcal A^{(4)}
=
\underbrace{\{ENTITY,RELATION,TIME\}}_{historical\ substrate}
\cup
\underbrace{\{REPRESENTATION,COMMITMENT,AUTHORITY\}}_{semantic\ kernels}
+
\underbrace{\{SOURCE\_PROVENANCE,OPEN\}}_{meta}
}
```

This is a six-element non-meta basis.

The key historical result is not:

```math
\text{events do not matter}.
```

It is:

```math
\boxed{
\textbf{What happened is carried by temporal relation history; it need not be carried by a separate EVENT object.}
}
```

And the strongest counterintuitive result of this pass is:

```math
\boxed{
\textbf{EVENT}\neq\textbf{STATE TRANSITION}
\quad\textbf{while}\quad
\textbf{EVENT primitive is still eliminable.}
}
```

Failed attempts, interruptions, searches, speech acts, and emotional actions survive because they remain explicit relation assertions even when they produce no terminal relational change.

---

# 16. Reopenability condition

This deletion is provisional and must remain reopenable.

Reintroduce an event-like primitive only if later reconstruction finds a source distinction requiring an occurrence to possess semantic identity that cannot be recovered from:

```text
relation-instance identity
participants
temporal support/order
relation-history neighborhood
source provenance
```

Until such a failure appears:

```math
\boxed{\textbf{do not restore EVENT merely because event language is convenient.}}
```

The current minimization frontier is therefore:

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

with source provenance and `OPEN` preserved outside the semantic basis.
