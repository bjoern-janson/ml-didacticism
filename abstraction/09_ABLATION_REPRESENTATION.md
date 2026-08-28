# Adversarial Ablation — REPRESENTATION

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

**Purpose:** test whether `REPRESENTATION` is a primitive semantic kernel or whether every agent-relative, false, future, hypothetical, reported, and retrospective content structure can be reconstructed from the ordinary historical relation graph without a distinct assertion/content scope  
**Status:** adversarial semantic-kernel ablation pass; `COMMITMENT` and `AUTHORITY` are explicitly out of scope

The architecture entering this pass is:

```math
\boxed{
\mathcal A^{(6)}
=
\{ENTITY,RELATION,REPRESENTATION,COMMITMENT,AUTHORITY\}
+
\{SOURCE\_PROVENANCE,OPEN\}
}
```

The governing criterion is:

```math
\boxed{\textbf{REPRESENTATION is primitive only if removing it prevents the architecture from storing structured content that may differ from world/history truth without contaminating the world/history graph.}}
```

This pass attacks one candidate only:

```math
\boxed{REPRESENTATION}
```

---

# 0. What the previous ablations leave us with

`STATE`, `ACCESS`, `EVENT`, and `TIME` have all been removed as separate primitives.

`RELATION` survived as the irreducible carrier of typed predication/incidence.

The historical substrate is therefore a provenance-bearing multirelation over persistent/addressable entities and relation instances, including temporal relations among relation instances.

The question now is whether agent-relative models are merely selections/projections of that historical graph or whether the architecture needs a second assertion scope in which relation structure can be represented without being asserted as history.

The strongest kill hypothesis is:

```math
\boxed{
R_i
\stackrel{?}{=}
\Pi_i(\mathcal H)
}
```

where:

```text
H = source-supported historical relation graph
Pi_i = information-selection projection available to agent i
```

If every representation is only a subset/view of actual history, `REPRESENTATION` dies.

---

# 1. Anti-cheat constraints

A reduction fails if representation semantics are merely hidden inside `RELATION`, `ENTITY`, or an unrestricted context field.

Invalid examples:

```text
REPRESENTATION removed
→ RELATION(type="represents", holder=A, content=<arbitrary graph>)

REPRESENTATION removed
→ RELATION(type="believes", content=<arbitrary graph>)

REPRESENTATION removed
→ ENTITY(kind="proposition", graph=<arbitrary graph>)

REPRESENTATION removed
→ relation.context_id=agent_world_17

REPRESENTATION removed
→ relation.assertion_scope="hypothetical"
```

These are not reductions if the hidden payload supplies exactly the missing distinction:

```text
this relation is content of an agent/model
but is not asserted as historical/world truth
```

Likewise, it is not sufficient to serialize represented content as an opaque string. The reduction must preserve the internal structural distinctions that motivated the Genesis parse.

For example:

```text
"Joseph is dead"
```

cannot be stored merely as text if the architecture is supposed to reconstruct:

```text
subject = Joseph
predicate = dead
holder = Jacob/family
mode = represented belief/report/fear as locally earned
relation to actual Joseph-alive history
```

The required test is therefore semantic, not syntactic:

```math
\boxed{
\text{Can ordinary world/history relations alone encode non-world content without a distinct content/assertion scope?}
}
```

---

# 2. Candidate reduction A — representation as information projection

Attempt:

```math
\boxed{
R_i=\Pi_i(\mathcal H)
}
```

This says an agent's represented world is nothing more than the historical relations that are available to that agent.

This reduction would be attractive because `ACCESS` has already been deleted as an umbrella primitive; concrete information-bearing predicates such as `SEES`, `HEARS`, `RECOGNIZES`, `RECEIVES`, and `UNDERSTANDS` remain ordinary relations.

The question is whether those accessible relations fully determine represented content.

They do not.

---

# 3. Witness R1 — correct object recognition, false event model

Source discriminator: Genesis 37.

The source-supported history includes:

```text
Joseph → alive after sale
coat → genuinely Joseph's
coat → removed from Joseph
coat → blood applied
coat → presented/sent to Jacob
Jacob → recognizes coat
```

Jacob then supplies the event-history conclusion:

```text
evil beast → devoured Joseph
Joseph → rent in pieces / dead in Jacob's represented history
```

while the historical graph simultaneously preserves:

```text
Joseph → alive
Joseph → transported/sold into Egypt
```

The decisive distinction is:

```math
\boxed{
\text{correctly recognized object}
\not\Rightarrow
\text{correct represented event history}
}
```

An information projection can contain the coat and Jacob's recognition of it.

It does not contain the false historical edge:

```text
BEAST_DEVOURS(beast,Joseph)
```

because that edge is not in source-supported history.

Therefore the false relation must exist somewhere other than the world/history assertion graph.

If it is inserted into the ordinary graph, the architecture becomes contradictory rather than agent-relative:

```text
Joseph alive in Egypt
AND
Joseph killed by beast
```

The corpus does not present these as two world truths.

It presents one world history plus Jacob's false represented history.

### Result

```text
Representation is not reducible to information selection/projection.
```

---

# 4. Witness R2 — conflicting observations do not equal final classification

Source discriminator: Genesis 27.

The historical/source relation graph gives Isaac multiple signals:

```text
voice → Jacob-like
hands/tactile profile → Esau-like
clothing/smell → Esau-associated
visitor's spoken identity claim → "I am Esau"
```

Isaac actively tests the visitor and eventually blesses Jacob while failing to identify him as Jacob.

The architecture must preserve:

```math
\boxed{
\text{identity-bearing observations}
\neq
\text{recipient identity judgment}
}
```

If representation were only the set of observations available to Isaac, there would be no architectural location for the integrated classification:

```text
visitor = Esau
```

as distinct from the conflicting evidence used to reach it.

The final classification is not another observation copied from history.

It is an agent-level content structure produced under conflicting evidence.

### Result

```text
Representation is not reducible to the set of observed relations.
```

---

# 5. Witness R3 — represented future without current world counterpart

Genesis repeatedly contains represented future structures.

Examples include descendant futures, future movement, future birth, future conflict, future burial/transfer, and future lineage differentiation.

The general form is:

```math
\boxed{
R_i(F)
\quad\land\quad
F\notin\mathcal H_{current}
}
```

`08` already showed that temporal future/past status can be expressed through explicit temporal relations rather than a primitive `TIME` carrier.

But that does not solve the current problem.

The relation fragment `F` is still **not presently asserted history**.

The architecture must preserve:

```text
future content exists as represented content now
```

without asserting:

```text
future content has already occurred in history
```

For example, Genesis 50 ends with a sworn future bone-transfer relation while Joseph's body remains in a coffin in Egypt.

Thus:

```math
\boxed{
\text{represented future relation}
\neq
\text{current/historical relation}
}
```

A projection of current history cannot contain a relation that is not yet historical.

### Result

```text
Future-directed content blocks representation-as-current-world-projection.
```

---

# 6. Witness R4 — counterfactual/hypothetical relation sets

Source discriminator: Genesis 18.

Abraham's dialogue introduces a series of hypothetical population conditions:

```text
IF 50 righteous found → spare
IF 45 → not destroy
IF 40 → not do it
IF 30 → not do it
IF 20 → not destroy
IF 10 → not destroy
```

The chapter explicitly distinguishes:

```math
\boxed{
\text{hypothetical righteous count}
\neq
\text{observed righteous count}
}
```

These relation sets need not be actual historical states.

Therefore the architecture must be able to encode:

```text
conditional graph fragment C
result graph fragment Q
relation IF(C,Q)
```

without promoting `C` to world truth.

If the reduction introduces a generic `HYPOTHETICAL_CONTEXT` or `possible_world_id` to solve this problem, the hidden-parameter audit fails unless that new machinery is independently shown to be a smaller, more general primitive than representation.

No such reduction is earned here.

### Result

```text
Counterfactual content requires non-world assertion scope.
```

---

# 7. Witness R5 — multiple agents can hold incompatible models of one history

Source discriminator: Genesis 42 and the Joseph recognition arc.

Historical/source structure:

```text
Joseph → alive
Joseph → present before brothers
Joseph → recognizes brothers
brothers → do not recognize Joseph
```

The brothers' family self-description includes:

```text
one brother → "is not"
```

while the absent/not-present brother is the living person standing before them.

Thus:

```math
\boxed{
\mathcal H(\text{Joseph alive/present})
\quad\land\quad
R_{brothers}(\text{Joseph absent/not})
}
```

The architecture must also allow:

```math
\boxed{
R_i(x)\neq R_j(x)
}
```

without turning disagreement into contradiction in the historical graph.

This is not merely unequal access.

The brothers receive new family/interrogation information while Joseph preserves his identity asymmetry; they actively operate from a different identity map.

### Result

```text
One history can support multiple incompatible agent-relative content graphs.
```

---

# 8. Witness R6 — represented content can be causally active while false or unrealized

Representation is not inert annotation.

Genesis supplies many cases where an agent's represented content changes action even when the represented proposition is not established as world truth.

Examples:

```text
Genesis 27:
identity judgment → blessing action

Genesis 37:
false death model → persistent mourning

Genesis 42:
Jacob fears harm to Benjamin → withholds Benjamin

Genesis 50:
brothers fear Joseph may requite them → send message + later submit themselves
```

Therefore:

```math
\boxed{
R_i(x)\text{ may be false/unrealized}
\quad\land\quad
R_i(x)\rightarrow A_i
}
```

where the action relation is historical even when `x` is not.

If the content is deleted because it is not world truth, the causal/decision structure cannot be reconstructed.

### Result

```text
Non-world content can remain historically consequential.
```

---

# 9. Witness R7 — reports preserve structured content without certifying it

Across Genesis, reports are repeatedly distinguished from the events they concern.

Examples include:

```text
Rebekah's report of Isaac's earlier instruction
Jacob's report of dream/history to Rachel and Leah
brothers' later report to Jacob of Joseph's conditions
Judah's retrospective reconstruction of prior interactions
Joseph's later report of Jacob's burial words
brothers' messenger-borne claim that Jacob commanded forgiveness
```

The general form is:

```math
\boxed{
E
\neq
R_i(E)
\neq
R_j(R_i(E))
}
```

A report may preserve, omit, expand, reorder, or reinterpret local content.

Therefore the content of a report cannot be identified with the historical graph fragment it purports to describe.

Nor can it be flattened into an opaque speech string if the architecture is to preserve actor, action, cause, timing, and provenance claims inside the report.

### Result

```text
Representation must support structured report content with independent provenance.
```

---

# 10. Witness R8 — representation can target representation

The corpus requires nested content.

A later agent can report, interpret, deny, remember, or react to another agent's earlier speech or represented history.

Examples include:

```text
original instruction
→ listener hears
→ listener later reports instruction to another agent
```

and:

```text
claimed prior command
→ messenger reports claim
→ recipient reacts to messenger-borne content
```

So representation cannot be limited to:

```text
holder → primitive world object
```

It must allow the target/content to include an addressable representation or relation-history fragment.

Formally:

```math
\boxed{
REP_i(\rho_j)
}
```

must be possible where `\rho_j` is another representation structure.

### Result

```text
Representation requires recursively addressable content.
```

---

# 11. Candidate reduction B — reify propositions as ordinary entities

A stronger kill attempt is:

```text
create entity P
P denotes proposition/graph fragment
BELIEVES(A,P)
REPORTS(A,B,P)
FEARS(A,P)
```

with no primitive `REPRESENTATION` object.

This looks promising until the internal content of `P` is reconstructed.

Suppose:

```text
P = "Joseph is dead"
```

If `P` is opaque, structural reconstruction fails.

If `P` contains the relation:

```text
DEAD(Joseph)
```

then the architecture must distinguish:

```text
DEAD(Joseph) contained in P
```

from:

```text
DEAD(Joseph) asserted in historical graph
```

Otherwise the false belief contaminates history.

That means the reduction needs an assertion-scope distinction of the form:

```text
relation r is locally asserted within content object P
but not asserted in H
```

If implemented as:

```text
relation.scope=P
```

or:

```text
IN_CONTEXT(P,r)
```

plus a privileged world/root context, the architecture has introduced the semantic mechanism that `REPRESENTATION` was carrying.

Calling it `CONTEXT`, `QUOTE`, `PROPOSITION`, `MODEL`, or `SCOPE` does not eliminate the distinction.

### Hidden-parameter audit

```text
FAIL as a cardinality reduction.
```

The reified-proposition approach may be a valid implementation syntax, but it does not remove the need for non-world assertion scope.

---

# 12. Candidate reduction C — make every relation explicitly context-relative

An even stronger proposal is to replace representation with a universal contextual graph:

```math
RELATION(context,predicate,args)
```

where one context is historical/world assertion and other contexts correspond to agents, reports, counterfactuals, futures, dreams, and so on.

This can encode the corpus.

But it does not minimize the architecture under the current rules.

Why?

Because `context` is now an unrestricted semantic dimension answering exactly the removed question:

```text
where is this relation asserted as holding?
```

The distinction between:

```text
world assertion
agent model
reported model
hypothetical model
future model
```

has not disappeared.

It has become a free context parameter.

Furthermore, a universal context carrier would be a **new abstraction introduced to replace one surviving kernel**, not a deletion forced by independent reconstruction failure.

The protocol forbids adding such machinery merely to obtain a smaller visible vocabulary.

### Result

```text
Universal-context rewrite is representational tax evasion, not ablation success.
```

---

# 13. What is actually derivable inside representation

The failure to eliminate the kernel does **not** justify separate primitives for every representational mode.

The following do not each become architectural primitives:

```text
BELIEF
REPORT
FEAR
FORECAST
ACCUSATION
INTERPRETATION
QUESTION
COUNTERFACTUAL
RETROSPECTIVE EXPLANATION
DREAM CONTENT
```

They can remain source-earned typed relations/operations around one representational kernel.

For example:

```text
REPORTS(A,B,rho)
FEARS(A,rho)
ACCUSES(A,B,rho)
QUESTIONS(A,rho)
INTERPRETS(A,rho)
```

where `rho` is a structured representational content scope.

The lexical mode matters when the source distinguishes it, but the architecture does not need nine independent content ontologies.

Likewise, represented temporal structure is supplied by ordinary temporal relations inside `rho`; represented authority, identity, causation, quantity, and spatial structure use the same typed relation vocabulary as the historical graph without asserting those internal relations historically.

Thus:

```math
\boxed{
\text{same relational vocabulary}
+
\text{different assertion scope}
}
```

is sufficient.

---

# 14. The irreducible representation kernel

The ablation isolates a narrower residue than a generic `BELIEF` or `MENTAL STATE` ontology.

The corpus requires a mechanism by which an addressable holder/source can be related to a **structured graph fragment whose internal relations are locally assertable as content without being asserted as historical truth**.

Call the surviving kernel `REPRESENTATION` without expanding it into a psychological theory.

A useful abstract shape is:

```math
\boxed{
\rho
=
\langle
holder/source,
content\ graph,
mode,
provenance
\rangle
}
```

where:

```text
content graph → structured typed relations
holder/source → agent/group/speaker/report origin where source earns it
mode → source-earned operation such as report/fear/forecast/accusation, not an unrestricted semantic garbage field
provenance → source/audit relation back to lexical corpus
```

The essential semantic rule is:

```math
\boxed{
r\in content(\rho)
\not\Rightarrow
r\in\mathcal H
}
```

while representations may themselves be historical facts:

```math
\boxed{
REPRESENTS(holder,\rho)
\in\mathcal H
}
```

This allows:

```text
world: Joseph alive
representation rho_Jacob: Joseph dead
historical fact: Jacob holds/expresses/acts from rho_Jacob
```

without contradiction.

The kernel therefore supplies an **assertion-scope boundary**, not a claim that every representation is a belief or that every holder has a fully specified hidden mental state.

---

# 15. Five decisive reconstruction requirements

After attempted deletion, the architecture must still permit all five:

```math
\boxed{
1.\quad R_i(x)\neq\mathcal H(x)
}
```

```math
\boxed{
2.\quad R_i(x)\neq R_j(x)
}
```

```math
\boxed{
3.\quad R_i(x)\text{ may be false/nonactual while historically causally active}
}
```

```math
\boxed{
4.\quad R_i(F)\text{ may exist before }F\text{ is historical}
}
```

```math
\boxed{
5.\quad R_i(R_j(x))\text{ must be representable}
}
```

Every representation-free reduction tested here either fails one of these requirements or reintroduces a non-world assertion/context scope under another name.

---

# 16. Parameter audit

Because the deletion fails, keep only the exact residue required.

## Forbidden expansion

Do not infer primitive internal fields for:

```text
truth value
confidence
belief strength
intentionality
conscious endorsement
psychological mechanism
complete causal model
```

unless the source explicitly earns them.

Do not equate:

```text
REPORTS(rho)
```

with:

```text
BELIEVES(rho)
```

or:

```text
ACCUSES(rho)
```

with:

```text
BELIEVES(rho)
```

unless independent evidence establishes the belief relation.

The representation kernel preserves content and scope; it does not automatically infer endorsement.

## Required residue

The surviving kernel must support:

```text
structured content graph
non-world assertion scope
holder/source relation where earned
source-earned mode
recursive/nested content reference
independent source provenance
```

This is the minimum necessary to preserve the corpus distinctions.

---

# 17. Verdict

The projection hypothesis fails:

```math
\boxed{
R_i\neq\Pi_i(\mathcal H)
}
```

because agents construct false, future, hypothetical, retrospective, and integrated content that is not simply a subset of historical truth.

The proposition-entity reduction also fails as a true ablation because structurally rich proposition content requires a non-world assertion scope.

The universal-context rewrite fails the hidden-parameter audit because it merely renames the representation boundary.

Therefore:

```text
REPRESENTATION: IRREDUCIBLE KERNEL
```

More precisely:

```math
\boxed{
\textbf{The corpus requires a distinction between historical assertion and scoped relational content about history, possibility, future, or other representations.}
}
```

The deepest earned split is therefore:

```math
\boxed{
\textbf{world/history graph}
\neq
\textbf{models/content graphs over that world/history}
}
```

This is not a metaphysical claim about mind.

It is a representational requirement forced by the corpus.

---

# 18. Revised architecture

No cardinality reduction occurs in this pass.

The architecture remains:

```math
\boxed{
\mathcal A^{(7)}
=
\underbrace{\{ENTITY,RELATION\}}_{historical\ substrate}
\cup
\underbrace{\{REPRESENTATION,COMMITMENT,AUTHORITY\}}_{semantic\ kernels}
+
\underbrace{\{SOURCE\_PROVENANCE,OPEN\}}_{meta}
}
```

But `REPRESENTATION` is now much narrower and better justified.

It does **not** mean:

```text
all mental state
all information
all speech
all belief
```

It means:

```math
\boxed{
\text{structured relational content under a non-world assertion scope}
}
```

with source-earned holder/mode/provenance relations.

---

# 19. Reopenability condition

Reopen this result only if a later reconstruction shows that all of the following can be encoded without a distinct assertion/content scope:

```text
false agent models
future content before realization
counterfactual conditions
multiple incompatible agent models
structured reports with independent provenance
nested representation
causal action from false/unrealized content
```

and without introducing an equivalent `CONTEXT`, `MODEL`, `PROPOSITION_SCOPE`, `QUOTE`, or unrestricted relation parameter.

Until such a reconstruction succeeds:

```math
\boxed{\textbf{do not collapse represented relations into historical relations.}}
```

The current minimization frontier remains:

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

with source provenance and `OPEN` outside the semantic basis.
