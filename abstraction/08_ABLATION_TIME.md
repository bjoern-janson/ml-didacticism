# Adversarial Ablation — TIME

**Depends on:**
- `abstraction/00_ABSTRACTION_PROTOCOL.md`
- `abstraction/01_RELATION_INVENTORY.md`
- `abstraction/02_INVARIANT_STRIPPING_TESTS.md`
- `abstraction/03_MINIMAL_ARCHITECTURE.md`
- `abstraction/04_ABLATION_COMMITMENT_AUTHORITY.md`
- `abstraction/05_ABLATION_STATE_ACCESS.md`
- `abstraction/06_ABLATION_EVENT.md`
- `abstraction/07_ABLATION_RELATION.md`

**Purpose:** test whether `TIME` is a primitive historical carrier or whether temporal order, extent, metric, and future/past status can be represented as typed relations over addressable relation instances and source quantities  
**Status:** adversarial carrier ablation pass; no semantic-kernel ablation; `REPRESENTATION`, `COMMITMENT`, and `AUTHORITY` are explicitly out of scope

The architecture entering this pass is:

```math
\boxed{
\mathcal A^{(5)}
=
\{ENTITY,RELATION,TIME,REPRESENTATION,COMMITMENT,AUTHORITY\}
+
\{SOURCE\_PROVENANCE,OPEN\}
}
```

The governing criterion is:

```math
\boxed{\textbf{A temporal carrier is primitive only if removing it prevents lossless reconstruction of temporal order, extent, metric, or future/past status required by the corpus.}}
```

This pass attacks one candidate only:

```math
\boxed{TIME}
```

---

# 0. What `07` already established

`07` retained a primitive **typed predication/incidence** carrier and `06` had already removed `EVENT` as a separate ontological category.

The resulting historical substrate was written approximately as:

```math
\mathcal H=\{r_k@T_k\}_{k=1}^{n}
```

The `@T_k` notation is now under attack.

It cannot simply remain as a hidden field if `TIME` is declared removed.

The question is therefore not:

```text
Can we stop writing the word TIME?
```

It is:

```math
\boxed{\textbf{Can temporal structure be made explicit entirely through the already-earned relation carrier?}}
```

---

# 1. Anti-cheat constraints

The hidden-parameter audit remains binding.

The following reductions are invalid:

```text
TIME removed
→ RELATION(..., timestamp=t)

TIME removed
→ RELATION(..., start=t1, end=t2)

TIME removed
→ ENTITY(kind="time_point")

TIME removed
→ record.temporal_support=[t1,t2]

TIME removed
→ occurrence.order_index=17
```

These merely hide the removed carrier in a field or reified time object.

Likewise, this is invalid:

```text
RELATION(type="anything", temporal_semantics=<arbitrary free object>)
```

because an unrestricted temporal payload would recreate `TIME` under another name.

However, explicit source-earned temporal predicates are allowed to remain as ordinary typed relation instances:

```text
BEFORE(r1,r2)
AFTER(r2,r1)
SAME_TIME(r1,r2)
DURING(r1,r2)
OVERLAPS(r1,r2)
DURATION(r1,40,DAY)
ELAPSED_BETWEEN(r1,r2,7,DAY)
MONTH_INDEX(r,2)
DAY_INDEX(r,17)
AGE_AT(person,r,600,YEAR)
```

Why is this not cheating?

Because these are not hidden fields attached to every assertion. They are **explicit predications in the same relation substrate already required for parenthood, location, possession, recognition, and every other source-earned dimension**.

This is the same distinction that allowed `ACCESS` to be removed while `SEES`, `UNDERSTANDS`, `RECOGNIZES`, and `SEARCHES` remained.

Thus:

```math
\boxed{
\text{temporal predicate survives}
\not\Rightarrow
\text{TIME carrier survives}
}
```

The ablation succeeds only if no separate temporal address-space or hidden temporal support field remains necessary.

---

# 2. Temporal structure is not one thing

The corpus forces at least four distinctions:

```text
1. order
2. simultaneity / relative placement
3. extent / persistence
4. metric / calendar indexing
```

and a fifth semantic use:

```text
5. future/past relation of represented content to current history
```

The ablation must test each independently.

A result of the form:

```text
order derivable, metric irreducible
```

would be a legitimate partial-survival result.

Do not force a binary verdict before testing the dimensions separately.

---

# 3. Test T1 — simple order

The corpus repeatedly requires ordered histories:

```text
proposal → acceptance → implementation
request → promise → oath
search → discovery/non-discovery → response
attempt → refusal → unchanged target allocation
instruction → preparation → proximal action → interruption
```

A separate time coordinate is not required to preserve these sequences.

Because relation instances are already addressable records, encode:

```text
BEFORE(r_proposal,r_acceptance)
BEFORE(r_acceptance,r_implementation)
```

or, where the source earns only a local sequence:

```text
NEXT_IN_SOURCE(r1,r2)
```

without manufacturing an absolute clock.

The same endpoint can therefore retain different histories:

```text
H1:
ATTEMPTS(A,X)
REFUSES(B,X)

H2:
no attempt
```

although the final allocation relation is identical.

The history differs because H1 contains additional relation instances plus ordering relations.

### Result

```text
Temporal order does not force primitive TIME.
```

---

# 4. Test T2 — counterfactual ordering identity

Consider two histories with the same non-temporal relation inventory:

```text
H1:
A-operation
then
B-operation

H2:
B-operation
then
A-operation
```

If order matters, the architecture must distinguish them.

Without a time carrier:

```text
H1:
BEFORE(r_A,r_B)

H2:
BEFORE(r_B,r_A)
```

The difference is structurally explicit.

Thus:

```math
\boxed{
\text{same participating relations}
\neq
\text{same history when temporal-order relations differ}
}
```

No global time variable is necessary.

### Result

```text
Endpoint-equivalent but differently ordered histories remain distinguishable.
```

---

# 5. Test T3 — simultaneity and common indexing

Genesis 7 gives dense same-day structure.

The flood onset is indexed to:

```text
Noah's 600th year
second month
seventeenth day
```

and the chapter places multiple operations on that same indexed day, including water-source changes and the ark-entry/closure sequence.

A time-carrier encoding might assign:

```text
t = <600th year, month 2, day 17>
```

to each relation instance.

The time-free encoding can instead store explicit shared-index relations:

```text
AGE_AT(Noah,r_flood_onset,600,YEAR)
MONTH_INDEX(r_flood_onset,2)
DAY_INDEX(r_flood_onset,17)
SAME_TIME(r_fountains_open,r_flood_onset)
SAME_TIME(r_windows_open,r_flood_onset)
```

or give the same calendar-component relations directly to each source assertion where that is what the text supports.

The important point is that **calendar indexing becomes relational content**, not an external carrier coordinate.

### Result

```text
Simultaneity/common calendar placement does not force primitive TIME.
```

---

# 6. Test T4 — exact duration / temporal metric

This is the strongest rescue attempt for `TIME`.

Genesis 7 explicitly distinguishes:

```text
7 days → waiting interval before flood onset
40 days + 40 nights → rain duration
40 days → flood/water-rise duration marker
150 days → waters prevailing
```

Genesis 8 adds:

```text
150-day boundary
40-day wait before opening ark window
7-day wait before second dove release
another 7-day wait before third dove release
```

Genesis 50 separately gives:

```text
40 days → embalming
70 days → Egyptian mourning
7 days → mourning at Atad
```

These quantities cannot be replaced by order alone.

Formally:

```math
BEFORE(r_1,r_2)
```

does not determine:

```math
\Delta(r_1,r_2)=7\text{ days}.
```

But this proves only that **metric content is required**, not that `TIME` must be a separate carrier.

Represent the source quantities explicitly:

```text
ELAPSED_BETWEEN(r_instruction,r_flood_onset,7,DAY)
DURATION(r_rain,40,DAY)
DURATION(r_waters_prevail,150,DAY)
DURATION(r_embalming,40,DAY)
DURATION(r_egyptian_mourning,70,DAY)
DURATION(r_atad_mourning,7,DAY)
```

Here:

```text
7, 40, 70, 150
```

are source quantity values and:

```text
DAY
```

is a source unit label/value.

No temporal coordinate object is introduced.

Therefore the metric survives as **typed quantitative relation content**.

### Critical distinction

```math
\boxed{
\text{temporal order}
\neq
\text{temporal metric}
}
```

Both are required.

Neither requires a separate `TIME` carrier under the current corpus.

### Result

```text
Exact duration blocks order-only reduction but does not rescue primitive TIME.
```

---

# 7. Test T5 — same order, different duration

Use the adversarial pair:

```text
H1:
A
wait 1 day
B

H2:
A
wait 100 years
B
```

The ordering relation is identical:

```text
BEFORE(A,B)
```

but the histories are not temporally equivalent.

The relation-only substrate distinguishes them through metric predicates:

```text
H1:
ELAPSED_BETWEEN(r_A,r_B,1,DAY)

H2:
ELAPSED_BETWEEN(r_A,r_B,100,YEAR)
```

Thus temporal metric is a dimension independent from order.

This test prevents an overly aggressive collapse to a mere partial-order graph.

### Result

```text
A partial order alone is insufficient; relation + explicit metric is sufficient.
```

---

# 8. Test T6 — calendar index without absolute chronology

Genesis 8 supplies multiple calendar-like markers:

```text
7th month / 17th day → ark rests
10th month / 1st day → mountain tops visible
601st year / 1st month / 1st day → waters dried / direct observation
2nd month / 27th day → earth dried
```

The chapter itself warns against manufacturing a total absolute chronology beyond the supplied anchors.

That fits the relational reduction well.

Store exactly the supplied index relations:

```text
MONTH_INDEX(r_ark_rests,7)
DAY_INDEX(r_ark_rests,17)

MONTH_INDEX(r_mountain_tops_visible,10)
DAY_INDEX(r_mountain_tops_visible,1)

AGE_YEAR_INDEX(Noah,r_ground_dry_observation,601)
MONTH_INDEX(r_ground_dry_observation,1)
DAY_INDEX(r_ground_dry_observation,1)

MONTH_INDEX(r_earth_dried,2)
DAY_INDEX(r_earth_dried,27)
```

and explicit BEFORE/AFTER relations where the source supplies the sequence.

Do **not** invent a hidden absolute timestamp to unify them unless the corpus later forces such reconstruction.

### Result

```text
Calendar-like indexing survives as explicit relation content without primitive TIME.
```

---

# 9. Test T7 — persistence intervals

This is the most important anti-cheat test after metric.

The old representation might write:

```text
POSSESSES(A,O) @ [t1,t4)
```

That notation is forbidden if `TIME` is removed.

The time-free historical representation instead uses the relation instance itself plus explicit boundary/history relations when the source earns them.

Example pattern:

```text
r_possess = POSSESSES(A,O)

ESTABLISHED_BY(r_possess,r_acquisition)
BEFORE(r_acquisition,r_later_use)
STILL_RELEVANT_AT(r_possess,r_later_use)
```

or, where a later transfer terminates the relation:

```text
TERMINATED_BY(r_possess,r_transfer)
```

The exact vocabulary should remain source-constrained; no universal persistence state machine is added.

For Genesis 23 → 49 → 50, the key requirement is that an earlier acquired burial-property relation remains available to later burial specification/execution.

The architecture does **not** need to infer a fully observed continuous timeline of the property's status between every chapter.

It needs to preserve:

```math
\boxed{
\text{earlier relation established}
\neq
\text{later relation invocation/use}
}
```

and any explicit continuation/termination information actually supplied.

### Important restraint

Absence of a termination relation is not automatically proof of eternal persistence.

Where persistence beyond the source is uncertain:

```text
OPEN
```

remains available.

### Result

```text
Persistence does not force hidden start/end time fields.
```

---

# 10. Test T8 — future representation versus realization

A major corpus invariant is:

```math
\boxed{
\text{future representation}
\neq
\text{later realization}
}
```

Can that survive without `TIME`?

Yes, if represented content and source-history assertions can themselves participate in temporal relations.

Suppose:

```text
r_rep = REPRESENTATION(A,F)
r_now = current speech/history relation
```

The represented content may include:

```text
AFTER(F,r_now)
```

or a source-specific future operator represented within the content graph.

Later, if the source narrates a corresponding relation instance:

```text
r_realized
```

then the architecture may add:

```text
AFTER(r_realized,r_rep)
CORRESPONDS(r_realized,F)
```

where correspondence is earned by the text.

Genesis 7 supplies a clean example:

```text
after seven days → flood onset represented
later → after seven days, flood waters upon earth
```

Genesis 50 supplies the opposite completion status:

```text
future bone transfer represented + sworn
Joseph dies
corpus ends with coffin in Egypt
```

No corresponding transfer relation is present yet.

Therefore:

```math
\boxed{
\text{future/past status}
=
\text{relative temporal relation inside history/representation}
}
```

rather than a value on a primitive clock.

### Result

```text
Future/realization separation does not force primitive TIME.
```

---

# 11. Test T9 — duration overlap and underdetermination

Genesis 50 gives:

```text
embalming → 40 days
Egyptian mourning → 70 days
```

The chapter-level parse correctly preserves them as separately timed processes.

But the exact overlap relation between those two intervals should not be invented merely from the two quantities.

Therefore the architecture must distinguish:

```text
DURATION(r_embalming,40,DAY)
DURATION(r_mourning,70,DAY)
```

from an additional claim such as:

```text
OVERLAPS(r_embalming,r_mourning)
```

unless the text actually earns it.

This is another place where explicit relation encoding is safer than a hidden global timeline solver.

### Result

```math
\boxed{
\text{duration known}
\neq
\text{complete interval topology known}
}
```

No primitive `TIME` is needed to preserve that uncertainty.

---

# 12. Joint temporal reconstruction

After removing `TIME`, the historical substrate must still reconstruct:

```text
order
simultaneity
exact elapsed quantities
exact duration quantities
calendar-like indices
persistence/termination where earned
future-relative content
partial temporal uncertainty
```

A generic example becomes:

```text
r1 = REQUESTS(A,B,X)
r2 = PROMISES(B,A,X)
r3 = SWEARS(B,A,X)
r4 = PERFORMS(B,X)

BEFORE(r1,r2)
BEFORE(r2,r3)
BEFORE(r3,r4)
ELAPSED_BETWEEN(r3,r4,q,unit)   # only if source supplies q/unit
```

No record contains:

```text
timestamp
start_time
end_time
time_id
```

Temporal structure is an explicit graph over relation instances.

---

# 13. Hidden-parameter audit

After removing `TIME`, inspect the retained architecture.

## Forbidden

```text
relation.timestamp
relation.interval
relation.temporal_support
relation.order_index
entity.kind=time
TIME_POINT
TIME_SPAN
```

## Allowed because they are explicit source-earned typed predications

```text
BEFORE(r1,r2)
SAME_TIME(r1,r2)
DURATION(r,40,DAY)
ELAPSED_BETWEEN(r1,r2,7,DAY)
MONTH_INDEX(r,2)
DAY_INDEX(r,17)
AGE_AT(person,r,600,YEAR)
```

The difference is crucial:

```math
\boxed{
\text{hidden temporal coordinate}
\neq
\text{explicit temporal relation in the graph}
}
```

No single remaining field answers:

```text
"what time is this relation at?"
```

Instead, temporal facts are reconstructed from the explicit temporal neighborhood of the relation instance.

The audit therefore passes.

---

# 14. Verdict

The strongest attempted rescue of primitive `TIME` is quantitative metric.

It proves:

```math
\boxed{
\text{temporal order alone is insufficient}
}
```

because the corpus explicitly preserves elapsed and duration quantities.

But metric itself is representable through typed quantitative relations over relation instances and source values/units.

Calendar indexing, simultaneity, persistence boundaries, and future/past status likewise reconstruct relationally.

Therefore:

```text
TIME: DERIVABLE
```

More precisely:

```math
\boxed{
\textbf{TIME is a derived relational family, not a primitive carrier.}
}
```

This does **not** mean temporal semantics disappear.

The corpus still requires at least:

```math
\boxed{
\text{temporal order}
\neq
\text{temporal metric}
}
```

and it sometimes requires calendar-like index, simultaneity, or persistence relations as well.

What disappears is the need for a separate temporal address-space in addition to the already-required relation substrate.

---

# 15. Revised architecture

Removing `TIME` yields:

```math
\boxed{
\mathcal A^{(6)}
=
\underbrace{\{ENTITY,RELATION\}}_{historical\ substrate}
\cup
\underbrace{\{REPRESENTATION,COMMITMENT,AUTHORITY\}}_{semantic\ kernels}
+
\underbrace{\{SOURCE\_PROVENANCE,OPEN\}}_{meta}
}
```

This is a five-element non-meta basis.

The historical substrate is no longer:

```text
entities + relations + external timeline
```

but:

```math
\boxed{
\textbf{persistent/addressable entities and relation instances, including explicit temporal relations among relation instances.}
}
```

`STATE` remains a derived graph view.

`EVENT` remains a derived motif over occurrent relation instances.

`ACCESS` remains a derived family over information-bearing relation instances.

`TIME` now becomes a derived family over temporal-order, metric, index, and extent relations.

---

# 16. Reopenability condition

Reintroduce a separate temporal carrier only if later reconstruction finds a source distinction that cannot be recovered from:

```text
relation-instance identity
explicit temporal-order relations
explicit duration/elapsed relations
source quantity + unit values
calendar/index relations
persistence-boundary relations where earned
source provenance
OPEN for unearned temporal edges
```

In particular, reopen `TIME` if an external corpus forces a temporal structure that cannot be expressed without a globally shared temporal object/coordinate whose semantics are not reducible to explicit relations.

Current Genesis evidence does not force that object.

Until such a failure appears:

```math
\boxed{\textbf{do not restore TIME merely because timestamp notation is convenient.}}
```

The current minimization frontier is therefore:

```math
\boxed{
ENTITY
+
RELATION
+
REPRESENTATION
+
COMMITMENT
+
AUTHORITY
}
```

with source provenance and `OPEN` preserved outside the semantic basis.

The next semantic wall is not attacked here.
