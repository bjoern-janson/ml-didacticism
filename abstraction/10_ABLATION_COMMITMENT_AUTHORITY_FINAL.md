# Final Adversarial Ablation — COMMITMENT and AUTHORITY

**Depends on:**
- `abstraction/00_ABSTRACTION_PROTOCOL.md`
- `abstraction/01_RELATION_INVENTORY.md`
- `abstraction/02_INVARIANT_STRIPPING_TESTS.md`
- `abstraction/03_MINIMAL_ARCHITECTURE.md`
- `abstraction/04_ABLATION_COMMITMENT_AUTHORITY.md`
- `abstraction/05_ABLATION_STATE_ACCESS.md`
- `abstraction/06_ABLATION_EVENT.md`
- `abstraction/07_ABLATION_RELATION.md`
- `abstraction/08_ABLATION_TIME.md`
- `abstraction/09_ABLATION_REPRESENTATION.md`

**Purpose:** retest the two provisional semantic kernels `COMMITMENT` and `AUTHORITY` against the much smaller basis earned after the carrier ablations  
**Status:** final semantic-kernel ablation pass over the Genesis source corpus; no external-domain testing

The architecture entering this pass is:

```math
\boxed{
\mathcal A^{(7)}
=
\{ENTITY,RELATION,REPRESENTATION,COMMITMENT,AUTHORITY\}
+
\{SOURCE\_PROVENANCE,OPEN\}
}
```

The governing rule remains:

```math
\boxed{\textbf{delete only what the corpus allows us to delete.}}
```

This pass attacks:

```math
\boxed{COMMITMENT\qquad AUTHORITY}
```

individually and jointly.

A successful deletion requires:

```text
1. source distinctions remain reconstructible;
2. no removed semantic bit reappears as an unrestricted parameter;
3. source-earned local predicates may remain;
4. no new abstraction is introduced merely to make the visible basis smaller.
```

---

# 0. Why this retest is legitimate after `04`

`04` provisionally retained narrow `COMMITMENT` and `AUTHORITY` kernels because the architecture at that stage still contained a large carrier set:

```text
ENTITY
STATE
EVENT
RELATION
TIME
ACCESS
REPRESENTATION
COMMITMENT
AUTHORITY
```

Subsequent ablations changed the dependency structure substantially:

```text
STATE  → derived relation view
ACCESS → derived information-relation family
EVENT  → derived temporal-relation motif
TIME   → derived temporal-relation family
RELATION → irreducible typed predication/incidence carrier
REPRESENTATION → irreducible non-world assertion-scope kernel
```

Therefore the question must be reopened.

The important new fact is:

```math
\boxed{
\text{typed source predicates are already independently required by }RELATION.
}
```

So a source distinction such as:

```text
requests
promises
swears
becomes surety
appoints
authorizes
commands
refuses
allocates
```

need not justify a second umbrella primitive merely because the predicates belong to a useful semantic family.

This is exactly the logic that allowed:

```text
SEES / UNDERSTANDS / RECOGNIZES / SEARCHES
```

to survive while the umbrella `ACCESS` primitive died.

Thus the present question is not:

```text
Do commitment-like and authority-like relations occur?
```

They plainly do.

It is:

```math
\boxed{
\textbf{Do those source-earned typed relations require an additional semantic kernel beyond RELATION + REPRESENTATION?}
}
```

---

# 1. Anti-cheat rule

The hidden-parameter audit remains strict.

Invalid commitment reductions:

```text
COMMITMENT removed
→ RELATION(..., commitment=true)

COMMITMENT removed
→ RELATION(..., force="binding")

COMMITMENT removed
→ REPRESENTATION(..., normative_force=...)
```

Invalid authority reductions:

```text
AUTHORITY removed
→ RELATION(..., authority=true)

AUTHORITY removed
→ RELATION(..., decision_right=...)

AUTHORITY removed
→ ENTITY(role="authorized decider")
```

These merely move the kernel.

However, source-earned predicates are allowed:

```text
REQUESTS
PROMISES
SWEARS
SURETY_FOR
COMMANDS
APPOINTS
SETS_OVER
PERMITS
REFUSES
ALLOCATES
```

provided they remain independently typed predicates rather than values of one hidden commitment/authority field.

This is not tax evasion because the architecture already requires source-constrained predicate identity for all relations.

The governing distinction is:

```math
\boxed{
\text{local predicate distinction}
\neq
\text{umbrella semantic primitive}
}
```

---

# 2. Target A — kill `COMMITMENT`

## 2.1 Strongest reduction hypothesis

Try to represent every commitment-like structure using only:

```text
ENTITY
RELATION
REPRESENTATION
```

with source-earned relational predicates.

A future content object is a representation scope:

```math
\rho_X = \text{structured content in which }X\text{ occurs later / conditionally}
```

Then speech/relational distinctions may be represented as:

```text
REQUESTS(A,B,rho_X)
PROMISES(B,A,rho_X)
SWEARS(B,A,rho_X)
SURETY_FOR(A,B,rho_condition,rho_consequence)
```

The question is whether a further relation of the form:

```text
COMMITMENT(B,rho_X)
```

adds independently required structure.

---

# 3. Commitment witness C1 — request without promise

Source discriminator: Genesis 40.

Joseph requests that the butler, when restored, remember him, mention him to Pharaoh, and help bring him out.

The chapter explicitly supplies no butler promise.

Required distinction:

```math
\boxed{
\text{future action requested}
\neq
\text{future action promised}
}
```

Represent without `COMMITMENT`:

```text
rho_release = structured future content

REQUESTS(Joseph,butler,rho_release)
```

and crucially:

```text
no source-supported PROMISES(butler,Joseph,rho_release)
```

The later forgetting/non-remembrance history is then represented independently.

Nothing is lost.

The difference between request and promise is carried by two source-earned predicate identities, not by a generic binding-force scalar.

### Result

```text
Request-without-promise does not force a COMMITMENT kernel.
```

---

# 4. Commitment witness C2 — promise versus oath over nearly identical content

Source discriminator: Genesis 47.

The chapter gives:

```text
Jacob requests burial outside Egypt
Joseph says: I will do as thou hast said
Jacob says: swear unto me
Joseph swears
```

The future content remains approximately:

```math
\rho_B = \text{Joseph performs the requested burial transfer after Jacob dies}
```

A kernel-based representation might say:

```text
PROMISE creates commitment
OATH strengthens commitment
```

But the source-level distinction is already reconstructible as:

```text
r1 = REQUESTS(Jacob,Joseph,rho_B)
r2 = PROMISES(Joseph,Jacob,rho_B)
r3 = REQUESTS_OATH(Jacob,Joseph,rho_B)
r4 = SWEARS(Joseph,Jacob,rho_B)

BEFORE(r1,r2)
BEFORE(r2,r3)
BEFORE(r3,r4)
```

where `REQUESTS_OATH` may remain as the source-specific request `swear unto me`, or be represented through the speech content without creating a universal oath-request ontology.

Later Genesis 50 supplies execution:

```text
PERFORMS / BURIES / CARRIES
```

linked historically to the earlier request/promise/oath sequence.

No extra scalar such as:

```text
binding_force = 1,2,3
```

is required.

The corpus requires:

```math
\boxed{
\text{promise}\neq\text{oath}
}
```

but does not require an additional universal quantity called `commitment force` beyond preserving those relational forms.

### Result

```text
Promise/oath strengthening does not force a separate COMMITMENT kernel.
```

---

# 5. Commitment witness C3 — surety with conditional consequence

Source discriminator: Genesis 43, activated in Genesis 44.

Judah says in substance:

```text
Judah → surety for Benjamin
if Benjamin is not returned / set before Jacob
→ Judah bears blame
```

This looks more complex than promise/oath because it has conditional consequence structure.

But `REPRESENTATION` already provides structured non-world/future/conditional content scopes.

Represent:

```text
rho_condition = Benjamin not returned to Jacob
rho_consequence = Judah bears blame

SURETY_FOR(Judah,Benjamin,Jacob,rho_condition,rho_consequence)
```

Then Genesis 44 supplies later crisis relations:

```text
Benjamin faces detention
Judah reconstructs prior household history
Judah proposes self-substitution
```

The surety relation remains part of history and may be queried as a precursor to Judah's later proposal.

No separate `COMMITMENT` edge is needed to preserve:

```text
who undertook the surety
for whom
before whom
under what condition
with what stated consequence
```

### Hidden-parameter audit

`SURETY_FOR` is allowed only because surety is a source-earned local predicate/relation.

This would fail if encoded as:

```text
RELATION(type="commitment", subtype="surety", force=...)
```

The reduced architecture does not do that.

### Result

```text
Conditional surety does not force an umbrella COMMITMENT kernel.
```

---

# 6. Commitment minimal-counterexample search

To retain `COMMITMENT`, we need a pair of histories such that:

```text
all ENTITY relations are identical
all ordinary typed RELATION instances are identical
all REPRESENTATION content is identical
```

but the source still requires a different commitment state.

No tested Genesis pair satisfies this.

Whenever commitment-like force differs, the source also gives a different historical relation:

```text
request
promise
oath
surety
```

or a different conditional/content structure.

Thus the proposed minimal counterexample does not materialize.

What `04` called the irreducible binding residue is now reconstructible as an **analytic family over source-earned relations** once `RELATION` has been independently retained.

Define only as a view if useful:

```math
\boxed{
CommitmentView(Q)
:=
\text{query over promise/oath/surety and related future-content relations satisfying }Q
}
```

This view does not enter the primitive basis.

---

# 7. COMMITMENT verdict

The corpus requires distinct commitment-like predicates.

It does not require a separate umbrella semantic kernel in addition to typed relation identity and structured represented content.

Therefore:

```text
COMMITMENT: DERIVABLE
```

More precisely:

```math
\boxed{
\textbf{COMMITMENT is a derived relational family over future/scoped content, not an irreducible semantic kernel.}
}
```

This does **not** mean:

```text
request = promise = oath = surety.
```

It means:

```math
\boxed{
\text{their differences are preserved by typed relation structure itself.}
}
```

---

# 8. Target B — kill `AUTHORITY`

## 8.1 Strongest reduction hypothesis

Try to reconstruct authority-like topology using only:

```text
ENTITY
RELATION
REPRESENTATION
```

plus the source-earned relation history:

```text
commands
appoints
sets over
rules according to word
permits
requests
refuses
allocates
executes
owns
possesses
```

Do not create a free `decision_right` field.

The question is whether the source requires an additional assertion:

```text
AUTHORITY(actor,scope,target)
```

that cannot be reconstructed from the ordinary typed relations actually narrated.

---

# 9. Authority witness A1 — proposal versus appointment

Source discriminator: Genesis 41.

Joseph first proposes:

```text
Pharaoh should look out a discreet/wise man
Pharaoh should set that man over Egypt
Pharaoh should appoint officers
```

At this point:

```text
Joseph has proposed an administrative structure
```

but:

```text
Joseph has not appointed himself
```

Later Pharaoh says to Joseph:

```text
thou shalt be over my house
according unto thy word shall all my people be ruled
only in the throne will I be greater than thou
I have set thee over all the land of Egypt
```

and supplies public/material appointment markers.

Without `AUTHORITY`, preserve:

```text
PROPOSES(Joseph,rho_admin_plan)
SETS_OVER(Pharaoh,Joseph,Pharaoh_house)
RULED_ACCORDING_TO_WORD(people,Joseph)
GREATER_IN_THRONE_THAN(Pharaoh,Joseph)
SETS_OVER(Pharaoh,Joseph,Egypt)
```

These directly distinguish:

```math
\boxed{
\text{proposal}
\neq
\text{appointment}
\neq
\text{scope relations after appointment}
}
```

No separate `AUTHORITY=true` field is needed.

The authority topology is reconstructible from the ordinary relation graph.

### Result

```text
Proposal/appointment distinction does not force an AUTHORITY kernel.
```

---

# 10. Authority witness A2 — authorization versus execution

Source discriminator: Genesis 50.

Joseph has an existing sworn burial relation but still sends a request through Pharaoh's house:

```text
Joseph → Pharaoh's house → Pharaoh
request → go to Canaan, bury father, return
```

Pharaoh responds:

```text
go up
bury thy father
according as he made thee swear
```

Then Joseph and the funeral company perform the journey/burial.

Represent without `AUTHORITY`:

```text
REQUESTS(Joseph,Pharaoh,rho_depart_bury_return)
RESPONDS_WITH_GO_UP(Pharaoh,Joseph,rho_depart_bury_return)
PERFORMS(Joseph_and_company,rho_depart_bury_return)
```

or, if the abstraction has earned the local predicate:

```text
PERMITS(Pharaoh,Joseph,rho_depart_bury_return)
```

The important distinction remains:

```math
\boxed{
\text{request}
\neq
\text{Pharaoh response/permission}
\neq
\text{execution}
}
```

A generic `AUTHORITY` kernel adds no new source fact.

### Result

```text
Authorization/execution distinction does not force an AUTHORITY kernel.
```

---

# 11. Authority witness A3 — delegated scope without identity collapse

Genesis 41 preserves both:

```text
Joseph → set over Egypt / Pharaoh's house
```

and:

```text
Pharaoh → greater only in throne
```

This means delegation does not erase the delegator's differentiated position.

Represent directly as scope-sensitive typed relations.

A separate authority scalar would be weaker because it could hide the exact relational geometry.

Thus:

```math
\boxed{
\text{delegation topology}
=
\text{explicit scope/precedence relation graph}
}
```

for this source case.

### Result

```text
Delegation does not force an umbrella AUTHORITY primitive.
```

---

# 12. Authority witness A4 — Genesis 48 correction attempt

This was the strongest earlier rescue case for `AUTHORITY`.

The chapter gives:

```text
Joseph observes crossed hand placement
Joseph is displeased
Joseph attempts to move Jacob's hand
Joseph says the firstborn should receive the right hand
Jacob refuses
Jacob says he knows the birth order
Jacob retains the crossed allocation
Jacob explicitly sets Ephraim before Manasseh
```

Earlier abstraction language summarized this as:

```text
Joseph can attempt correction but lacks final allocation authority.
```

The final ablation asks whether that authority statement is actually required as a primitive source fact.

It is not.

The complete source-earned structure is already reconstructible as:

```text
SEES(Joseph,allocation)
DISPLEASED_BY(Joseph,allocation)
ATTEMPTS(Joseph,move_hand)
REQUESTS(Joseph,Jacob,rho_birth_order_aligned_hand)
REFUSES(Jacob,rho_correction)
KNOWS/ASSERTS_KNOWLEDGE(Jacob,birth_order)
MAINTAINS/SETS_BEFORE(Jacob,Ephraim,Manasseh)
```

The chapter directly gives the unsuccessful intervention and the final allocation.

No extra relation:

```text
AUTHORITY(Jacob,allocation)
```

is necessary to explain **what the text says happened**.

Indeed, adding a universal decision-right edge risks moving from description into a stronger institutional theory not explicitly supplied by the scene.

The safe corpus result is:

```math
\boxed{
\text{attempted modification}
\neq
\text{accepted modification}
\neq
\text{final relation}
}
```

That distinction is already preserved by ordinary relation history.

### Result

```text
Genesis 48 no longer rescues AUTHORITY as a separate kernel once typed relation history is retained.
```

---

# 13. Authority witness A5 — ownership, action, and command remain distinct without an umbrella

The corpus repeatedly distinguishes local relations such as:

```text
owns
possesses
commands
appoints
requests
performs
refuses
```

Removing `AUTHORITY` does not merge them because `RELATION` preserves predicate identity.

Therefore:

```math
\boxed{
OWNS(A,O)
\neq
COMMANDS(A,B,X)
\neq
PERFORMS(A,X)
}
```

without requiring:

```text
AUTHORITY(A,...)
```

as an additional universal edge.

This is the same structural lesson as earlier eliminations:

```text
preserving distinct local predicates
≠
requiring their umbrella category as a primitive.
```

---

# 14. Authority minimal-counterexample search

To retain `AUTHORITY`, we need two histories such that:

```text
all entities are the same
all source-earned typed relation instances are the same
all represented content is the same
```

but the source still requires a different decision-right topology.

No tested Genesis pair satisfies this.

Whenever the authority-like topology differs, the corpus supplies a different relation history or scope relation:

```text
appointment
command
permission/refusal
allocation
precedence statement
scope statement
```

A derived analytic view remains possible:

```math
\boxed{
AuthorityView(Q)
:=
\text{query over appointment/command/permission/scope/precedence relations satisfying }Q
}
```

but that view is not a primitive.

### Important restraint

Do not infer a complete institutional authority graph where the source only gives a local command, request, refusal, or successful act.

Removing the `AUTHORITY` kernel actually strengthens this restraint by preventing broad decision-right semantics from being automatically projected onto every local interaction.

---

# 15. AUTHORITY verdict

The corpus requires source-earned distinctions among:

```text
proposal
appointment
command
permission
refusal
execution
scope
precedence
ownership
possession
```

It does not require an additional semantic kernel called `AUTHORITY` once typed relation identity is already primitive.

Therefore:

```text
AUTHORITY: DERIVABLE
```

More precisely:

```math
\boxed{
\textbf{AUTHORITY is a derived relational topology over source-earned scope, appointment, command, permission, refusal, allocation, and precedence relations.}
}
```

This does **not** mean:

```text
capability = permission = appointment = command = execution.
```

It means their differences already live in the relational graph.

---

# 16. Joint ablation — remove COMMITMENT + AUTHORITY together

Independent deletion is not enough.

Test:

```math
\boxed{
\{COMMITMENT,AUTHORITY\}\rightarrow\varnothing
}
```

leaving:

```math
\boxed{
ENTITY+RELATION+REPRESENTATION
}
```

plus source provenance and `OPEN`.

The joint test must reconstruct:

```text
request without promise
promise then oath
conditional surety
future obligation later executed
future obligation still deferred
proposal without appointment
appointment with explicit scope
request → permission → execution
attempted correction → refusal → unchanged/final allocation
ownership ≠ command ≠ execution
```

All survive.

Why?

Because the retained basis still supports:

```text
1. persistent/addressable entities and relation instances;
2. source-constrained typed relation identity;
3. structured non-world/future/conditional content scopes;
4. relations whose arguments can include representation scopes and other relation instances;
5. explicit temporal relations as ordinary relations;
6. source provenance and OPEN boundaries.
```

Commitment-like history becomes motifs such as:

```text
REQUESTS
→ PROMISES
→ SWEARS
→ later PERFORMS / does not yet perform
```

Authority-like history becomes motifs such as:

```text
PROPOSES
→ APPOINTS / SETS_OVER
→ scope relations
→ COMMANDS / PERMITS / REFUSES
→ EXECUTES by same or different actor
```

Neither motif requires a hidden common semantic bit.

---

# 17. Cross-dependency test

Could the successful deletion of one kernel secretly rely on the other?

## Commitment without authority

Promise/oath/surety structures remain representable as ordinary typed relations over structured future/conditional content.

No generic authority relation is necessary to state that an actor promised or swore.

Therefore:

```math
\boxed{
COMMITMENT\text{-family reconstruction does not require AUTHORITY kernel.}
}
```

## Authority without commitment

Appointment, permission, refusal, scope, and precedence structures remain representable without a generic commitment relation.

Therefore:

```math
\boxed{
AUTHORITY\text{-family reconstruction does not require COMMITMENT kernel.}
}
```

## Joint conclusion

The earlier apparent semantic independence of the two kernels was real at the level of **families of relations**, but it did not imply two irreducible architectural primitives.

They are different derived families over the same relational substrate.

---

# 18. Hidden-parameter audit after joint deletion

Forbidden after deletion:

```text
relation.commitment_force
relation.authority_level
relation.decision_right
relation.binding_strength
representation.normative_force
entity.authority_role as universal semantic substitute
```

Allowed because independently required/source-earned:

```text
REQUESTS
PROMISES
SWEARS
SURETY_FOR
COMMANDS
APPOINTS
SETS_OVER
PERMITS
REFUSES
ALLOCATES
OWNS
POSSESSES
PERFORMS
```

and structured content scopes such as:

```text
rho_future
rho_condition
rho_consequence
```

The architecture does not contain a field answering:

```text
"how committed is this?"
```

or:

```text
"how much authority does this actor have?"
```

unless the source provides specific relational facts from which a query can be answered.

The audit passes.

---

# 19. Final verdict of this pass

```text
COMMITMENT: DERIVABLE
AUTHORITY: DERIVABLE
JOINT ABLATION: PASSES
```

Thus both provisional kernels from `04` are eliminated by the smaller architecture earned in `05`–`09`.

This is not a contradiction with `04`.

It is a dependency revision:

```math
\boxed{
\text{a candidate may appear irreducible under a larger/less settled basis and become derivable after a deeper carrier is itself isolated.}
}
```

The decisive deeper carrier was:

```math
\boxed{
RELATION = \text{typed predication/incidence with addressable instances}
}
```

plus:

```math
\boxed{
REPRESENTATION = \text{structured relational content under non-world assertion scope}
}
```

Once those were earned, separate commitment and authority umbrellas became redundant.

---

# 20. Revised minimal candidate architecture

Removing both kernels yields:

```math
\boxed{
\mathcal A^{(8)}
=
\underbrace{\{ENTITY,RELATION\}}_{historical\ substrate}
\cup
\underbrace{\{REPRESENTATION\}}_{assertion\text{-}scope\ kernel}
+
\underbrace{\{SOURCE\_PROVENANCE,OPEN\}}_{meta}
}
```

or compactly:

```math
\boxed{
ENTITY
+
RELATION
+
REPRESENTATION
}
```

with provenance and `OPEN` preserved outside the semantic basis.

This architecture can reconstruct the previously eliminated families as views/motifs:

```text
STATE       → graph slice/view
ACCESS      → information-bearing relation view
EVENT       → occurrent relation motif
TIME        → temporal relation family
EVIDENCE    → object/relation history + provenance + representation
FUTURE      → represented/scoped content with temporal relations
OBLIGATION  → request/promise/oath/surety history + later completion state
AUTHORITY   → appointment/permission/command/scope/precedence topology
COMMITMENT  → promise/oath/surety future-content topology
ORDER       → typed ordering relations
RETROSPECTIVE MEANING → later representation targeting earlier relation history
```

---

# 21. What the three surviving elements mean

## ENTITY

Persistent/addressable identity required so that relations can connect the same person/object/group/place/record across multiple assertions without lexical-name collapse.

This pass does **not** ablate `ENTITY`.

## RELATION

Primitive typed predication/incidence:

```math
P(a_1,\dots,a_n)
```

with source-constrained predicate identity, role/argument structure, polarity where explicit, multiplicity, and source provenance.

Relation instances may themselves be addressable so history, temporal structure, provenance, and higher-order relations remain expressible.

## REPRESENTATION

The irreducible assertion-scope boundary from `09`:

```math
\boxed{
r\in content(\rho)\not\Rightarrow r\in\mathcal H}
```

It permits structured false, future, hypothetical, reported, interpreted, or nested content without contaminating historical truth.

---

# 22. The deepest compression earned so far

The Genesis abstraction/minimization sequence now supports:

```math
\boxed{
\textbf{history}
=
\text{addressable entities standing in typed relations}
}
```

and:

```math
\boxed{
\textbf{representation}
=
\text{typed relational structure asserted under a non-history scope}
}
```

Most other architectural categories tested so far are recoverable as relation families, motifs, scopes, or graph queries.

This does **not** mean the lexical distinctions disappear.

Quite the opposite:

```math
\boxed{
\textbf{abstraction succeeds only because the local predicate distinctions remain recoverable.}
}
```

The minimal architecture is small; the source-earned relation vocabulary may remain large.

---

# 23. Minimality claim boundary

This pass earns a strong result, but the wording must remain calibrated.

It is safe to say:

```math
\boxed{
\textbf{Among all architectural candidates explicitly ablated through Genesis 1–50, the current surviving non-meta basis is }\{ENTITY,RELATION,REPRESENTATION\}.
}
```

It is not yet safe to claim a mathematical proof that no alternative encoding could ever reduce these further.

In particular:

```text
ENTITY has not yet received its own dedicated adversarial ablation artifact.
```

`RELATION` and `REPRESENTATION` have both survived dedicated attacks.

Therefore this file calls the result:

```text
current minimal candidate architecture
```

rather than an unreopenable final ontology.

---

# 24. Reopenability

Reopen `COMMITMENT` only if later reconstruction produces two source states with identical entity/relation/representation structure but a source-required difference in binding force that cannot be represented by source-earned predicates.

Reopen `AUTHORITY` only if later reconstruction produces two source states with identical entity/relation/representation structure but a source-required difference in decision-right topology not recoverable from appointment, command, permission, refusal, scope, precedence, or related source-earned relations.

Until such failures occur:

```math
\boxed{\textbf{do not restore semantic umbrellas merely because they are convenient analytic labels.}}
```

---

# 25. Current minimization frontier

```math
\boxed{
\begin{array}{rcl}
STATE &\to& DERIVED\\
ACCESS &\to& DERIVED\\
EVENT &\to& DERIVED\\
TIME &\to& DERIVED\\
COMMITMENT &\to& DERIVED\\
AUTHORITY &\to& DERIVED\\[4pt]
RELATION &\to& IRREDUCIBLE\ CARRIER\ KERNEL\\
REPRESENTATION &\to& IRREDUCIBLE\ ASSERTION\text{-}SCOPE\ KERNEL\\
ENTITY &\to& RETAINED\ /\ NOT\ YET\ DEDICATEDLY\ ABLATED
\end{array}
}
```

with:

```math
\boxed{SOURCE\_PROVENANCE+OPEN}
```

preserved as non-negotiable meta-constraints.

The current candidate is therefore:

```math
\boxed{
\mathcal A_{candidate}
=
\{ENTITY,RELATION,REPRESENTATION\}
+
\{SOURCE\_PROVENANCE,OPEN\}
}
```

This is the smallest architecture the completed ablation sequence has earned so far from the Genesis corpus.
