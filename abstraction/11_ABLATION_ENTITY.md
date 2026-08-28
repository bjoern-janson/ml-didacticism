# Final Carrier Ablation — ENTITY

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
- `abstraction/10_ABLATION_COMMITMENT_AUTHORITY_FINAL.md`

**Purpose:** test whether a primitive `ENTITY` carrier is required, or whether persistent referential individuation can be reconstructed from relation-argument occurrences plus source-supported identity/coreference relations  
**Status:** dedicated carrier ablation over Genesis 1–50; no external-domain testing

The architecture entering this pass is:

```math
\boxed{
\mathcal A^{(8)}
=
\{ENTITY,RELATION,REPRESENTATION\}
+
\{SOURCE\_PROVENANCE,OPEN\}
}
```

The governing criterion is referential rather than metaphysical:

```math
\boxed{
\textbf{ENTITY is primitive only if persistent referential identity cannot be reconstructed without an independent entity token.}
}
```

This pass does **not** ask whether persons, objects, groups, or places are real.

It asks whether the architecture needs a separate carrier of the form:

```text
ENTITY_ID = e17
```

in addition to the already-retained relation and representation machinery.

---

# 0. Strongest kill hypothesis

Attempt:

```math
\boxed{
ENTITY
\stackrel{?}{=}
[\text{relation-argument occurrences}]_{\sim_{ref}}
}
```

where:

```text
relation-argument occurrence
```

means one provenance-bearing argument position in one relation assertion, and:

```math
\sim_{ref}
```

is a source-supported same-referent/coreference relation whose equivalence closure groups occurrences that denote the same persistent referent.

The raw relation record therefore does **not** point to a canonical entity ID.

Instead it contains local argument occurrences:

```text
r1 = P(o1,o2)
r2 = Q(o3,o4)
```

and where the source earns identity/coreference:

```text
SAME_REFERENT(o1,o3)
```

A derived persistent referent is then:

```math
\boxed{
EntityView(o)
:=
[o]_{\sim_{ref}}
}
```

The entire ablation turns on whether this quotient is enough.

---

# 1. Anti-cheat rules

The following are invalid reductions:

```text
ENTITY removed
→ every argument stores entity_id=e17

ENTITY removed
→ every argument stores canonical_referent=e17

ENTITY removed
→ relation.subject_token is a globally persistent opaque thing-token

ENTITY removed
→ SAME_REFERENT(o1,o2,canonical=e17)
```

These simply preserve `ENTITY_ID` under another name.

Also invalid:

```text
identity inferred solely because surface labels match
```

because Genesis 36 already established:

```math
\boxed{\text{same surface name}\neq\text{proved same entity}}
```

and:

```math
\boxed{\text{different surface names}\neq\text{proved different entity}}
```

A successful reduction must use only:

```text
1. relation-instance identity already required by RELATION;
2. local argument-position identity inside each relation instance;
3. source-supported coreference / identity / naming relations;
4. source provenance;
5. OPEN where identity is not earned.
```

No hidden globally canonical participant token may remain.

---

# 2. Why relation-argument occurrences are not entities

A relation instance already requires ordered or role-resolved argument **positions**.

For example:

```text
PARENT_OF(arg_parent,arg_child)
```

needs two slots even before either slot is linked to any other occurrence elsewhere.

These slots are structural parts of the relation record, not independent entity records.

They have local identity because the architecture must know which participant fills which argument role.

That local slot identity was already implicit in the irreducible `RELATION` kernel from `07`.

Therefore the ablation is allowed to use:

```text
argument occurrence o_k
```

without granting it global persistent referential identity.

Persistent identity must be reconstructed separately through relation topology.

---

# 3. Attack E1 — same referent, different labels

The corpus repeatedly distinguishes referent continuity from label continuity.

Examples include:

```text
Jacob / Israel
Luz / Bethel
Esau / Edom at the person-name level
```

Genesis 35 explicitly says:

```text
Luz → which is Bethel
```

and separately repeats the Jacob→Israel naming relation while the narrator continues to use `Jacob` afterward.

So:

```math
\boxed{
\text{name reassignment}
\neq
\text{referent replacement}
}
```

The entity-free encoding keeps distinct lexical/name occurrences but links referential occurrences where the source earns continuity:

```text
o_Jacob_1
NAME_USED(o_Jacob_1,"Jacob")

o_Israel_1
NAME_USED(o_Israel_1,"Israel")

SAME_REFERENT(o_Jacob_1,o_Israel_1)
```

or equivalently through source-earned naming relations whose semantics imply coreference.

The derived quotient contains both mentions in one referent class.

No canonical `ENTITY(Jacob)` object is necessary.

### Result

```text
Alias / renaming continuity does not force primitive ENTITY.
```

---

# 4. Attack E2 — same surface label, identity not established

Genesis 36 is the strongest anti-collapse witness.

The chapter contains repeated or cross-chapter overlapping names and relation patterns, while explicitly warning that matching labels or matching parent/sibling patterns do not prove identity.

In the occurrence-quotient model:

```text
mention occurrence a
mention occurrence b
```

remain distinct by default.

A shared lexical label gives only:

```text
LABEL(a,L)
LABEL(b,L)
```

It does **not** generate:

```text
SAME_REFERENT(a,b)
```

unless the source supplies a bridge.

Therefore:

```math
\boxed{
\text{lexical equality}
\not\Rightarrow
\text{referential equality}
}
```

is preserved automatically.

Where the bridge is unresolved:

```text
OPEN
```

remains preferable to forced merging.

### Result

```text
Repeated labels do not force primitive ENTITY and do not collapse under the quotient model.
```

---

# 5. Attack E3 — same physical referent, changing relational function

Genesis repeatedly contains persistent objects whose roles change.

Genesis 28 gives the clean stone case:

```text
stone → pillow-related use
same later-described stone → pillar
pillar → oil poured on it
```

The chapter explicitly identifies the later singular stone with the earlier pillow use while preserving uncertainty about the earlier plural-to-singular mapping.

The entity-free encoding can preserve:

```text
r1 = USED_AS(o1,pillow-function)
r2 = SET_AS(o2,pillar-function)
r3 = OIL_POURED_ON(actor,o3)

SAME_REFERENT(o1,o2)
SAME_REFERENT(o2,o3)
```

only to the extent the text earns those links.

Then:

```math
EntityView(o_1)=EntityView(o_2)=EntityView(o_3)
```

is derived.

The changing functional relations remain distinct.

Thus:

```math
\boxed{
\text{persistent referent}
\neq
\text{persistent function}
}
```

without a primitive entity record.

Genesis 38 supplies the same pattern for pledge tokens that later become provenance-bearing evidence.

### Result

```text
Object continuity across changing function does not force primitive ENTITY.
```

---

# 6. Attack E4 — structurally indistinguishable participants

A neighborhood-based identity reduction fails.

Suppose two participants have identical currently represented properties:

```text
same class
same sex
same owner
same location
same role
```

or two members of a group have otherwise symmetric relational profiles.

Structural similarity cannot imply identity:

```math
\boxed{
N(o_a)=N(o_b)
\not\Rightarrow
o_a\sim_{ref}o_b
}
```

The occurrence-quotient model handles this correctly.

Distinct source mentions/argument occurrences remain distinct classes unless a source-supported same-referent relation links them.

Therefore two fully symmetric participants can remain numerically distinct:

```math
\boxed{
[o_a]_{\sim_{ref}}
\neq
[o_b]_{\sim_{ref}}
}
```

without either class needing an opaque entity ID.

This is a key result:

```math
\boxed{
\text{individuation comes from non-equivalence, not from descriptive uniqueness.}
}
```

### Result

```text
Indistinguishable participants do not rescue primitive ENTITY.
```

---

# 7. Attack E5 — historical continuity across long gaps

A primitive entity carrier would make continuity trivial:

```text
all mentions point to e17
```

The ablation asks whether continuity instead can be represented as a source-supported path over occurrence identity relations.

For a long-lived referent:

```text
o1 --SAME_REFERENT--> o2 --SAME_REFERENT--> o3 ...
```

or a chain of naming/coreference/definite-reference relations may generate the same equivalence class.

The architecture does **not** require the referent to participate continuously in narrated relations between appearances.

Thus:

```math
\boxed{
\text{narrative gap}
\neq
\text{referent discontinuity}
}
```

provided later source language earns the coreference bridge.

If the bridge is not earned, the architecture must not manufacture persistence merely because a harmonization would be convenient.

Use:

```text
OPEN
```

instead.

This preserves the provenance discipline that earlier passes already required.

### Result

```text
Long-gap persistence is reconstructible as coreference topology; no primitive ENTITY required.
```

---

# 8. Attack E6 — initial introduction / apparent empty history

The strongest rescue attempt for `ENTITY` is a referent introduced before any rich relation history exists.

But textual introduction itself is never structurally empty.

Examples have forms such as:

```text
there was X
X was a man / woman / place / object
X had label L
X appeared / stood / was located
X was related to Y
```

At minimum, the source supplies a unary or n-ary assertion containing a new argument occurrence.

A singleton occurrence class is enough:

```math
EntityView(o_{intro})=[o_{intro}]_{\sim_{ref}}
```

No prior history is required.

If a text somehow supplied no assertion, mention, label, role, or relation involving a supposed referent, there would be no source content requiring the architecture to represent it.

Therefore:

```math
\boxed{
\text{first mention}
\neq
\text{need for pre-existing entity object}
}
```

### Result

```text
Initial individuation can begin as a singleton argument-occurrence class.
```

---

# 9. Attack E7 — representation scopes must refer to historical participants without asserting represented predicates historically

`09` retained representation because:

```math
r\in content(\rho)\not\Rightarrow r\in\mathcal H
```

The entity ablation must preserve cross-scope referential continuity.

Example:

```text
history: Joseph alive
representation: Jacob represents Joseph dead
```

The `Joseph` occurrence inside the representation must denote the same referent as historical Joseph while `DEAD(Joseph)` remains only inside the representation scope.

Encode:

```text
o_hist = Joseph-argument occurrence in historical relation

o_rep = Joseph-argument occurrence inside representation rho

SAME_REFERENT(o_hist,o_rep)
```

while:

```text
ALIVE(o_hist)      # historical assertion
DEAD(o_rep)        # asserted only inside rho
```

The quotient preserves referential identity across scopes, while `REPRESENTATION` preserves assertion-scope difference.

Thus the two surviving mechanisms separate cleanly:

```math
\boxed{
\text{referential identity}
\neq
\text{assertion scope}
}
```

No primitive entity object is required to make a represented false predicate target the same historical referent.

### Result

```text
Cross-scope reference does not rescue primitive ENTITY.
```

---

# 10. Attack E8 — can coreference itself be represented without smuggling ENTITY back in?

This is the decisive hidden-parameter audit.

A reduction would fail if `SAME_REFERENT` secretly contained a canonical entity key.

It does not need one.

Use only binary identity/coreference assertions over local argument occurrences:

```text
SAME_REFERENT(o1,o2)
SAME_REFERENT(o2,o3)
```

and derive equivalence closure:

```math
\sim_{ref}
=
\operatorname{EqClosure}(SAME\_REFERENT)
```

The equivalence class is a **query result**, not a stored primitive carrier.

No member needs to be designated as canonical.

No opaque object sits behind the class.

The class itself is analogous to other derived structures already accepted by the minimization:

```text
STATE      → graph view
EVENT      → relation motif
TIME       → temporal relation family
AUTHORITY  → relational topology
ENTITY     → referential-equivalence view
```

`SAME_REFERENT` is not a new carrier category.

It is a source-constrained relation type inside the already-earned `RELATION` substrate, just as `BEFORE`, `RECOGNIZES`, `PARENT_OF`, `POSSESSES`, or `PROMISES` are relation types.

### Important restraint

The parser may assert `SAME_REFERENT` only when source evidence supports it through grammar, naming, explicit identification, definite-reference continuity, or another provenance-bearing bridge.

It must **not** infer coreference merely from:

```text
same name
same properties
same relation neighborhood
semantic convenience
```

Unresolved identity remains:

```text
OPEN
```

### Result

```text
Coreference requires relation semantics, but not an independent ENTITY carrier.
```

---

# 11. What the reduction does not claim

`ENTITY: DERIVABLE` does **not** mean:

```text
persons are unreal
objects are illusions
identity is arbitrary
names determine identity
all nodes can be merged by structural similarity
```

It means only:

```math
\boxed{
\textbf{the architecture need not store persistent referents as a separate primitive record type if referential identity is recoverable as equivalence structure over relation-argument occurrences.}
}
```

The source still determines where individuation and coreference are warranted.

---

# 12. Minimal counterexample search

To retain primitive `ENTITY`, we need a source distinction such that:

```text
all relation instances are identical
all representation scopes are identical
all source provenance is identical
all argument-occurrence/coreference structure is identical
```

but the corpus still requires two different persistent referent assignments.

No tested Genesis case supplies such a pair.

Whenever referential identity differs, at least one of the following differs:

```text
source mention occurrence
argument position
explicit naming relation
coreference/definite-reference bridge
identity statement
representation-to-history reference bridge
OPEN status
```

Therefore no independent entity token adds source-earned information.

---

# 13. Verdict

The naive neighborhood hypothesis fails:

```math
\boxed{
ENTITY\neq\text{descriptive relation neighborhood}
}
```

because distinct participants may have identical relational profiles.

But the stronger quotient reduction succeeds:

```math
\boxed{
\textbf{persistent referent}
=
\textbf{equivalence class over provenance-bearing relation-argument occurrences under source-supported coreference.}
}
```

Therefore:

```text
ENTITY: DERIVABLE
```

More precisely:

```math
\boxed{
\textbf{ENTITY is a derived referential-equivalence view, not a primitive carrier.}
}
```

The irreducible requirement is not an entity object.

It is:

```math
\boxed{
\textbf{relation incidence with source-grounded referential distinguishability/coreference.}
}
```

That requirement is already carried by `RELATION` plus source provenance and `OPEN`.

---

# 14. Revised minimal candidate architecture

Removing `ENTITY` yields:

```math
\boxed{
\mathcal A^{(9)}
=
\underbrace{\{RELATION\}}_{historical/assertional substrate}
\cup
\underbrace{\{REPRESENTATION\}}_{non-history assertion-scope kernel}
+
\underbrace{\{SOURCE\_PROVENANCE,OPEN\}}_{meta}
}
```

or compactly:

```math
\boxed{
RELATION
+
REPRESENTATION
}
```

with provenance and `OPEN` preserved as non-negotiable constraints.

The derived families now include:

```text
ENTITY      → referential equivalence classes over argument occurrences
STATE       → graph slice/view
ACCESS      → information-bearing relation view
EVENT       → occurrent relation motif
TIME        → temporal relation family
EVIDENCE    → relation/object history + provenance + representation
FUTURE      → scoped content with temporal relations
OBLIGATION  → request/promise/oath/surety history + completion topology
AUTHORITY   → appointment/permission/command/scope/precedence topology
COMMITMENT  → promise/oath/surety future-content topology
ORDER       → typed ordering relations
RETROSPECTIVE MEANING → later representation targeting earlier relation history
```

---

# 15. The architecture after Genesis minimization

The strongest compression currently earned is:

```math
\boxed{
\textbf{history}
=
\textbf{provenance-bearing typed relation assertions over distinguishable argument occurrences}
}
```

with persistent referents derived by coreference closure.

And:

```math
\boxed{
\textbf{representation}
=
\textbf{typed relational structure asserted under a non-history scope}
}
```

Therefore the whole first-pass abstraction/minimization sequence converges to:

```math
\boxed{
\textbf{RELATION}
+
\textbf{REPRESENTATION}
}
```

subject to:

```math
\boxed{
SOURCE\_PROVENANCE
+
OPEN
}
```

This should not be read as:

```text
only two words matter.
```

The relation vocabulary remains large and source-constrained.

The compression is instead:

```math
\boxed{
\textbf{small carrier architecture; large recoverable typed vocabulary.}
}
```

---

# 16. Minimality boundary

This result is the strongest minimization reached by the explicit Genesis 1–50 ablations.

It is safe to say:

```math
\boxed{
\textbf{Among the architectural candidates explicitly tested, the surviving non-meta basis is }\{RELATION,REPRESENTATION\}.
}
```

It is **not** yet safe to claim an unreopenable theorem that no alternative formalism can reduce these further.

`RELATION` survived its dedicated adversarial ablation in `07`.

`REPRESENTATION` survived its dedicated adversarial ablation in `09`.

`ENTITY` is now removed by this dedicated referential ablation.

Future external-domain testing may expose a distinction that forces one of the deleted carriers to reopen.

Until such a reconstruction failure occurs:

```math
\boxed{
\textbf{do not restore an entity carrier merely because canonical node IDs are convenient in implementation.}
}
```

---

# 17. Reopenability condition

Reintroduce `ENTITY` only if a later source requires a persistent referent distinction that cannot be reconstructed from:

```text
relation-argument occurrence identity
source-supported coreference / identity relations
equivalence closure
representation-to-history reference bridges
source provenance
OPEN for unresolved identity
```

without introducing a hidden canonical participant token.

Until then:

```math
\boxed{
ENTITY\to DERIVED
}
```

and the current frontier is:

```math
\boxed{
\begin{array}{rcl}
ENTITY &\to& DERIVED\\
STATE &\to& DERIVED\\
ACCESS &\to& DERIVED\\
EVENT &\to& DERIVED\\
TIME &\to& DERIVED\\
COMMITMENT &\to& DERIVED\\
AUTHORITY &\to& DERIVED\\[4pt]
RELATION &\to& IRREDUCIBLE\ CARRIER\ KERNEL\\
REPRESENTATION &\to& IRREDUCIBLE\ ASSERTION\text{-}SCOPE\ KERNEL
\end{array}
}
```

with:

```math
\boxed{SOURCE\_PROVENANCE+OPEN}
```

outside the semantic basis.
