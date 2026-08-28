# Genesis-Derived Architecture Freeze — AG/1

**Status:** FROZEN / FOSSILIZED  
**Derivation anchor:** repository state immediately after `abstraction/11_ABLATION_ENTITY.md`, commit `cb0d1e32a9fe066dba92941e2f01c8817e0a1c98`  
**Source corpus:** Genesis 1–50 first-pass structural decode, provenance-bound to the pinned KJV corpus  
**Purpose:** preserve the Genesis-derived architecture exactly as earned before any external-domain reconstruction test can influence it

This file is not a living design document.

It freezes the result of the Genesis abstraction/minimization sequence:

```math
\boxed{
\mathcal A_G
=
\{RELATION,\ REPRESENTATION\}
+
\{SOURCE\_PROVENANCE,\ OPEN\}
}
```

The calibrated claim is:

```math
\boxed{
\textbf{Among the architectural candidates explicitly adversarially tested against Genesis 1–50, the surviving non-meta basis is }\{RELATION,REPRESENTATION\}.
}
```

The claim ceiling is equally binding:

```math
\boxed{
\textbf{No claim is made here that this architecture is domain-general, universal, uniquely minimal, or mathematically unreducible under every possible formalism.}
}
```

---

# 1. Freeze rule

From this point forward, external-domain tests may:

```text
PASS
FAIL
EXPOSE A MISSING DISTINCTION
```

They may **not** modify this frozen architecture in place.

If a later corpus forces a new primitive or exposes a failure of one of the Genesis reductions, that result belongs in a new artifact/version, for example:

```text
AG/1              # this frozen Genesis-derived result
AG/1 + failure    # external reconstruction failure record
A_ext/1           # separately proposed revised architecture, if warranted
```

The Genesis fossil remains unchanged.

Formally:

```math
\boxed{
\text{external evidence may challenge }\mathcal A_G
\quad\text{but may not rewrite the historical fact that Genesis produced }\mathcal A_G.
}
```

This is a causal cut between derivation and transportability testing.

---

# 2. Primitive 1 — RELATION

`RELATION` is the surviving historical/assertional carrier.

It means the capacity to preserve a **source-earned typed predication/incidence instance** with role-resolved argument occurrences.

A minimal relation instance has the abstract form:

```math
\boxed{
r_k=P_k(o_1,\ldots,o_n)
}
```

where:

```text
P_k        → source-constrained predicate identity

o_i        → provenance-bearing local argument occurrence

role/order  → preserved where required by the predicate

polarity    → explicit only when the source earns a negative assertion

multiplicity→ distinct relation occurrences remain distinct when the source distinguishes them

provenance  → every assertion remains traceable to source evidence
```

Important constraints:

```math
\boxed{
\text{same lexical predicate}\neq\text{same relation occurrence}
}
```

```math
\boxed{
\text{same argument properties}\neq\text{same referent}
}
```

```math
\boxed{
\text{absence of a relation}\neq\text{explicit negation}\neq OPEN
}
```

Relations may target other relation instances and representation scopes.

This permits higher-order structure without adding a new carrier.

Examples of relation families that remain source-earned vocabulary, not architecture primitives:

```text
PARENT_OF
SPOUSE_OF
POSSESSES
LOCATED_AT
RECOGNIZES
REPORTS
REQUESTS
PROMISES
SWEARS
APPOINTS
PERMITS
REFUSES
BEFORE
DURATION
SAME_REFERENT
```

The relation vocabulary may remain large.

The architecture remains small.

---

# 3. Primitive 2 — REPRESENTATION

`REPRESENTATION` is the surviving **assertion-scope kernel**.

It is required because the corpus repeatedly contains structured relational content that must exist without being promoted into historical truth.

Let:

```math
\mathcal H
```

be the historical assertion graph.

A representation scope `\rho` contains structured relational content such that:

```math
\boxed{
r\in content(\rho)
\not\Rightarrow
r\in\mathcal H
}
```

while the historical fact that a holder/source reports, fears, predicts, asks, interprets, remembers, dreams, or otherwise operates over `\rho` may itself be asserted in `\mathcal H`.

A useful abstract form is:

```math
\boxed{
\rho=
\langle
source/holder,\ content\ graph,\ source\text{-}earned\ mode,\ provenance
\rangle
}
```

with these restrictions:

```text
source/holder → included only where the source earns one

content graph → uses the same typed relation vocabulary as history

mode → source-earned operation such as report/fear/forecast/question; not a free psychological field

provenance → independently preserved
```

`REPRESENTATION` does **not** mean:

```text
BELIEF
all mental state
confidence
endorsement
truth value
psychological mechanism
```

unless the source separately establishes those relations.

The decisive architecture boundary is:

```math
\boxed{
\textbf{historical assertion}
\neq
\textbf{scoped relational content}
}
```

This supports simultaneously:

```text
history:
    Joseph alive

representation:
    Jacob → Joseph dead
```

without contradiction.

It also supports:

```text
future content before realization
counterfactual content
reports of prior reports
false inference
accusation
fear
forecast
retrospective causal explanation
nested representation
```

without asserting their internal relations as world/history facts.

---

# 4. Meta-constraint — SOURCE_PROVENANCE

`SOURCE_PROVENANCE` is mandatory but is not counted as a semantic primitive.

Every relation assertion, representation scope, coreference bridge, abstraction decision, and `OPEN` boundary must remain traceable to its source basis.

The governing rule is:

```math
\boxed{
\textbf{abstraction may reduce ontology; it may not erase evidential lineage.}
}
```

Source/audit provenance must distinguish at least where applicable:

```text
narrator assertion
spoken content
reported prior speech
agent inference/representation
later retrospective report
parser-added derived view
OPEN / unresolved bridge
```

Semantic provenance may be represented inside the relation graph.

Audit provenance remains non-negotiable metadata linking the abstraction back to the lexical/source corpus.

---

# 5. Meta-constraint — OPEN

`OPEN` records a deliberately unforced edge.

It means:

```math
\boxed{
\text{the current source does not justify selecting one stronger relation/referential bridge over the remaining live alternatives.}
}
```

`OPEN` is not:

```text
false
absent
unknown in an unrestricted philosophical sense
permission to guess later without new evidence
```

It is a provenance-bearing epistemic boundary.

The architecture must preserve:

```math
\boxed{
\text{missing edge}\neq\text{negative edge}\neq\text{OPEN edge-status}
}
```

---

# 6. Derived referents after ENTITY deletion

Persistent referents are reconstructed rather than stored as primitive entity records.

Let `o_i` be local relation-argument occurrences.

Source-supported coreference relations induce:

```math
\sim_{ref}
=
\operatorname{EqClosure}(SAME\_REFERENT)
```

and a derived referent is:

```math
\boxed{
EntityView(o)=[o]_{\sim_{ref}}
}
```

No canonical `ENTITY_ID` is required.

The source may earn coreference through:

```text
explicit identity statement
renaming
naming relation
pronoun/definite-reference continuity
explicit retrieval of an earlier object/person/place
representation-to-history reference bridge
other provenance-bearing grammatical relation
```

It may **not** be inferred merely from:

```text
same name
same properties
same relation neighborhood
semantic convenience
```

This preserves:

```math
\boxed{
\text{name identity}\neq\text{referential identity}
}
```

and:

```math
\boxed{
\text{descriptive similarity}\neq\text{identity}
}
```

---

# 7. Deletion ledger

The following candidates were explicitly attacked and removed from the primitive basis.

| Candidate | Frozen verdict | Reconstruction witness / reason for deletion |
|---|---|---|
| `ENTITY` | DERIVED | Persistent referents reconstruct as equivalence classes over provenance-bearing relation-argument occurrences under source-supported coreference. Genesis 36 blocks name-based identity; Jacob/Israel and Luz/Bethel show label change without referent replacement; persistent objects preserve continuity across changing functions. |
| `STATE` | DERIVED | A state is a graph slice/view over relations. `not recognized`, `not present`, and `dead` remain different predicates; absence of an edge is not negation. Before/after differences reconstruct from relation history without a state object. |
| `ACCESS` | DERIVED | The corpus requires distinct predicates such as sees/hears/receives/recognizes/understands/remembers/searches/discovers, but no additional universal access bit. Genesis 31, 37, 42 and interpreter scenes preserve modality directly. |
| `EVENT` | DERIVED | Failed attempts, interrupted actions, searches, speech acts, and ordering survive as addressable relation instances/motifs. An event is not merely `ΔΓ`, but no separate event carrier is needed once occurrent relation instances are retained. |
| `TIME` | DERIVED | Temporal order, simultaneity, metric, duration, calendar index, and persistence boundaries are explicit relation families. Genesis 7–8 and 50 force `order ≠ metric`, but not a separate temporal address-space. |
| `COMMITMENT` | DERIVED | `REQUESTS ≠ PROMISES ≠ SWEARS ≠ SURETY_FOR` remain source-earned relation predicates over structured future/conditional content. Genesis 40, 43, 47, and 50 require the local distinctions but no additional universal binding-force bit. |
| `AUTHORITY` | DERIVED | `PROPOSES ≠ APPOINTS ≠ COMMANDS ≠ PERMITS ≠ REFUSES ≠ ALLOCATES ≠ PERFORMS` remain source-earned relations. Genesis 41, 48, and 50 preserve scope/precedence/failed override/authorization/execution without an additional decision-right bit. |

Secondary analytic families also remain derived rather than primitive, including:

```text
EVIDENCE
OBLIGATION
FUTURE
ORDER
INFORMATION_TOPOLOGY
RETROSPECTIVE_MEANING
PERSISTENT_OBJECT
```

Their exact reconstruction is recorded in the preceding abstraction/ablation artifacts.

---

# 8. Frozen composition rules

The architecture permits composition through relations over:

```text
local argument occurrences
other relation instances
representation scopes
source quantities/units
lexical/source anchors
```

It permits derived views such as:

```text
EntityView
StateView
EventView
TimeView
AccessView
AuthorityView
CommitmentView
```

provided those views add no new primitive semantic bit.

The anti-cheat rule remains universal:

```math
\boxed{
\textbf{a deleted primitive may not reappear as an unrestricted field, hidden parameter, opaque canonical token, or renamed carrier.}
}
```

Examples forbidden under AG/1:

```text
entity_id=e17                    # hidden ENTITY carrier
relation.timestamp=t             # hidden TIME carrier
relation.access=true             # hidden ACCESS carrier
relation.commitment_force=high   # hidden COMMITMENT carrier
relation.decision_right=true     # hidden AUTHORITY carrier
relation.context=arbitrary       # unrestricted replacement for REPRESENTATION
```

Source-earned typed predicates are allowed because predicate identity is already independently required by `RELATION`.

---

# 9. Claim ceiling

AG/1 supports this claim:

```math
\boxed{
\textbf{Genesis 1–50 supports }\{RELATION,REPRESENTATION\}\textbf{ as the surviving non-meta minimal candidate under the explicit ablations performed.}
}
```

AG/1 does **not** support any of the following claims:

```text
RELATION + REPRESENTATION is universally sufficient.

RELATION + REPRESENTATION is mathematically unique.

No alternative formalism can reduce the architecture further.

Every domain can be losslessly reconstructed with AG/1.

Every source relation can be safely normalized into a small fixed vocabulary.

A transportability failure proves Genesis was parsed incorrectly.
```

The proper interpretation is:

```math
\boxed{
\textbf{Genesis supplied the distinctions; adversarial ablation determined which tested architectural umbrellas were unnecessary for reconstructing them.}
}
```

---

# 10. External-domain contamination boundary

An external test receives the frozen architecture:

```math
\boxed{
RELATION+REPRESENTATION+SOURCE\_PROVENANCE+OPEN
}
```

It may introduce new **source-earned relation predicates** if the external corpus itself contains new local relations.

It may **not** introduce a new architecture primitive during the reconstruction run.

If reconstruction appears to require one, record:

```text
FAILURE
missing distinction
minimal source witness
why RELATION + REPRESENTATION cannot encode it without hidden-parameter tax evasion
```

Then stop the run under AG/1.

Only after the test is closed may a separate architecture-revision artifact be proposed.

Therefore:

```math
\boxed{
\text{test failure}
\neq
\text{permission to redesign during the test}
}
```

This prevents the target domain from shaping the architecture it is supposed to evaluate.

---

# 11. Frozen transportability protocol

For a new corpus `D`, use only AG/1.

## Input

```text
1. frozen AG/1 architecture
2. external source corpus D
3. source provenance mechanism for D
```

The evaluator is not given permission to redesign the basis.

## Reconstruction

For every source distinction in `D`:

```text
1. encode source-earned typed relations;
2. preserve distinguishable local argument occurrences;
3. add source-supported coreference only when earned;
4. use REPRESENTATION whenever structured content must not be asserted as history;
5. preserve nested/report/future/hypothetical scopes where required;
6. record unresolved bridges as OPEN;
7. preserve provenance for every assertion and abstraction.
```

## Allowed outcome classes

```text
PASS
    All source-required distinctions reconstruct under AG/1.

FAIL_RECONSTRUCTION
    A source-required distinction cannot be encoded without loss.

FAIL_HIDDEN_PARAMETER
    Encoding is possible only by smuggling a deleted/new primitive into a field or token.

OPEN_TEST
    The source itself does not contain enough evidence to discriminate whether AG/1 is sufficient for a particular edge.
```

## On failure

Record the smallest counterexample:

```math
\boxed{
\text{minimal external witness}
+
\text{lost distinction}
+
\text{failed reconstruction}
}
```

Do not repair AG/1 inside the test.

---

# 12. Freeze boundary and versioning

This artifact freezes only the Genesis-derived result.

Later work may create:

```text
transport/...
failures/...
architecture/AG2_...
```

but must never rewrite the meaning of AG/1.

If later evidence forces reopening, preserve both states:

```math
\boxed{
AG/1
\neq
AG/2
}
```

with an explicit evidence trail explaining the transition.

A later architecture may supersede AG/1 for future use.

It cannot make AG/1 cease to be the result that was frozen before external-domain testing.

---

# 13. Final frozen compression

The Genesis 1–50 abstraction/minimization pass ends here:

```math
\boxed{
\textbf{history}
=
\textbf{provenance-bearing typed relational assertions over distinguishable argument occurrences}
}
```

Persistent referents are derived from source-grounded coreference structure.

And:

```math
\boxed{
\textbf{representation}
=
\textbf{typed relational structure asserted under a non-history scope}
}
```

The surviving non-meta basis among the explicitly tested candidates is therefore:

```math
\boxed{
\textbf{RELATION + REPRESENTATION}
}
```

subject to the non-negotiable constraints:

```math
\boxed{
SOURCE\_PROVENANCE+OPEN
}
```

The architectural phase derived from Genesis is now closed.

External reconstruction pressure begins only after this freeze.

```math
\boxed{\textbf{Decode the book. Freeze the result. Then test the result.}}
```
