# Genesis Abstraction Protocol

**Source corpus:** `genesis/01_GENESIS_01.md` through `genesis/50_GENESIS_50.md`  
**Purpose:** derive a vocabulary-independent architecture from the Genesis structural corpus without erasing distinctions that the corpus earned  
**Status:** governing protocol for the abstraction pass

The abstraction pass is not a summary pass.

Its governing operation is:

```math
\boxed{\textbf{strip lexical identity while preserving structural identity}}
```

The transformation target is:

```math
\boxed{
G_{lexical}
\rightarrow
G_{typed}
\rightarrow
G_{abstract}
\rightarrow
G_{vocabulary\ stripped}
}
```

The source corpus remains authoritative. The abstraction is a derived object and must remain reconstructible from the source-level structural records.

---

## 1. Governing boundary

```math
\boxed{
\text{TEXT}
\neq
\text{STRUCTURAL PARSE}
\neq
\text{ABSTRACTION}
\neq
\text{INTERPRETATION}
}
```

The abstraction layer may compress repeated structural behavior. It may not silently convert interpretation into structure.

The default uncertainty rule remains:

```math
\boxed{\text{uncertainty}\rightarrow\text{OPEN, not invention}}
```

---

## 2. Two-corpus requirement

The project must preserve two distinct corpora.

### Corpus A — lexical Genesis structure

Contains:

- Genesis names and labels,
- chapter-local wording,
- chronology,
- local entities and relations,
- role changes,
- reports and speech acts,
- persistent-object histories,
- future statements and later realizations,
- unresolved edges,
- source provenance.

### Corpus B — vocabulary-independent architecture

May use abstract types such as:

```text
ENTITY
AGENT
GROUP
POPULATION
OBJECT
PLACE
RESOURCE
ROLE
STATE
OBSERVATION
ACCESS
REPRESENTATION
REPORT
INFERENCE
ACTION
CONSEQUENCE
AUTHORITY
OBLIGATION
FUTURE_STATE
PERSISTENCE
UNCERTAINTY
```

The validity condition is:

```math
\boxed{B\text{ must be derivable from }A}
```

while also satisfying:

```math
\boxed{B\text{ must make sense without Genesis-specific vocabulary}}
```

Vocabulary stripping must therefore remove lexical identity, not structural provenance.

---

## 3. Persistent identity before name stripping

Proper names are not architecture, but they often bind structure across many chapters.

Therefore do not immediately replace a long-lived entity with an anonymous token and discard its lineage of roles.

Use a persistent entity record first:

```text
ENTITY:
    persistent_id: E17
    labels:
        - label_1
        - label_2
    roles_over_time:
        - role_a
        - role_b
        - role_c
    relations_over_time:
        - ...
```

A Genesis example may eventually strip lexical labels such as `Joseph` and `Zaphnathpaaneah`, but the abstraction must preserve that both labels attach to one persistent entity whose roles change across time.

Thus:

```math
\boxed{\text{name stripping}\neq\text{relation stripping}}
```

and:

```math
\boxed{\text{role change}\neq\text{entity replacement}}
```

---

## 4. Minimal recurring state architecture

The corpus repeatedly distinguishes at least the following five state classes.

### 4.1 World state

```math
W_t
```

What the structural record represents as existing or occurring.

### 4.2 Perception / access state

```math
P_t
```

What an entity can see, hear, receive, inspect, remember, retrieve, recognize, or otherwise access.

### 4.3 Representation state

```math
R_t
```

What an entity says, reports, expects, fears, predicts, explains, proposes, infers, remembers, or otherwise represents.

### 4.4 Action state

```math
A_t
```

What an entity actually does.

### 4.5 Resulting world state

```math
W_{t+1}
```

What changes after the action or event.

A common but non-mandatory loop is:

```math
\boxed{W_t\rightarrow P_t\rightarrow R_t\rightarrow A_t\rightarrow W_{t+1}}
```

The arrows are not universal requirements. The corpus also contains:

```text
W → R
W → A
P → R
R → A
A → W'
R → R'
P → P'
```

and, critically, missing links whose correct representation is:

```math
\boxed{\mathrm{OPEN}}
```

The architecture must therefore represent both present edges and absent/unearned edges.

---

## 5. Second-order structures that must survive abstraction

### 5.1 Persistent objects

An object can remain physically continuous while its relational function changes.

```math
\boxed{O_t\rightarrow O_{t+1}\quad\text{with role}(O_t)\neq\text{role}(O_{t+1})}
```

The abstraction must preserve:

- object identity,
- object state,
- object holder/location,
- provenance,
- changing function,
- recipient interpretation.

Do not collapse:

```math
\boxed{
\text{object presence}
\neq
\text{object provenance}
\neq
\text{event history}
\neq
\text{responsibility}
}
```

### 5.2 Obligations

An obligation is a persistent future-directed relation that can survive the event or person that created it.

Track at least:

```text
created
accepted
promised
sworn
revised
triggered
fulfilled
deferred
unfulfilled
superseded
```

Do not collapse:

```math
\boxed{
\text{request}
\neq
\text{promise}
\neq
\text{oath}
\neq
\text{execution}
}
```

### 5.3 Future representations

```math
R_t(FutureState)
```

must remain distinct from:

```math
W_{t+n}
```

until later text establishes a correspondence.

Track:

- forecast,
- promise,
- threat,
- fear,
- expected route,
- proposed future,
- blessing/future statement,
- later realization or non-realization.

### 5.4 Authority topology

The corpus repeatedly distinguishes who may:

```text
command
request
propose
promise
authorize
allocate
override
judge
execute
inspect
report
withhold
release
```

Authority must therefore be represented as typed and scoped relations, not as one scalar `power` variable.

```math
\boxed{\text{authority relation}\neq\text{role label}\neq\text{ownership}}
```

---

## 6. Relation abstraction must follow behavior, not wording

Genesis contains many local predicates:

```text
bless
command
send
keep
warn
ask
answer
report
recognize
fail to recognize
see
hear
remember
forget
know
not know
promise
vow
sell
buy
give
take
hide
find
return
```

Do not merge them because they look semantically adjacent.

The required order is:

```math
\boxed{
\text{local predicate inventory}
\rightarrow
\text{cross-chapter comparison}
\rightarrow
\text{candidate relation family}
\rightarrow
\text{equivalence test}
\rightarrow
\text{abstraction}
}
```

A relation family is earned only when the abstraction preserves the distinctions needed to reconstruct the source cases.

---

## 7. Abstraction as a quotient with a proof obligation

Let the source relation set be:

```math
\mathcal R_{lexical}=\{r_1,r_2,\dots,r_n\}
```

An abstraction proposes an equivalence relation `~` and maps multiple lexical relations into an abstract family:

```math
r_i\sim r_j\Rightarrow q(r_i)=q(r_j)
```

This merge is admissible only if the quotient preserves every distinction that has demonstrated downstream structural consequences in the source corpus.

Therefore the proof obligation for a merge is:

```math
\boxed{
q(r_i)=q(r_j)
\Rightarrow
\text{no source-level consequence depends on distinguishing }r_i\text{ from }r_j
}
```

If this cannot yet be shown:

```math
\boxed{\text{KEEP DISTINCT}}
```

This is the central anti-loss rule of the abstraction pass.

---

## 8. Do not abstract away a distinction merely because its purpose is unknown

The corpus repeatedly earned distinctions before their later significance was visible.

Therefore:

```math
\boxed{\textbf{unknown importance}\neq\text{safe to merge}}
```

Examples of distinctions that must survive unless independently shown redundant include:

- world state vs agent representation,
- observation vs interpretation,
- report vs event,
- recognition vs disclosure,
- object location vs object provenance,
- authority vs ownership,
- biological order vs allocated priority,
- proposal vs accepted policy,
- future statement vs realized state,
- request vs oath vs execution,
- group label vs member-specific information state,
- same quantity vs same institutional mechanism,
- same lexical label vs same entity.

---

## 9. Provenance must survive every abstraction level

Every abstract record must retain a path back to its supporting source records.

Minimum provenance fields:

```text
source_chapter
source_local_record
source_entity_or_object_ids
source_predicate
source_temporal_position
speaker_or_narrator
certainty_state
OPEN_dependencies
```

A vocabulary-free relation without reconstructible provenance is not an accepted architecture element.

Thus:

```math
\boxed{\text{compression without provenance}=\text{information loss}}
```

---

## 10. Reconstruction test

For each abstraction candidate, perform two tests.

### Forward stripping test

Can the source case be represented without Genesis-specific vocabulary?

Example form:

```text
A senior agent receives two related candidates.
An inherited ordering between the candidates is known.
A subordinate positions them according to that inherited ordering.
The senior agent deliberately assigns priority in the opposite order.
The subordinate detects the mismatch and attempts correction.
The senior agent rejects correction while affirming knowledge of the inherited order.
```

This yields:

```math
\boxed{\text{inherited ordering}\neq\text{allocated priority ordering}}
```

### Reverse reconstruction test

Given the abstract record plus provenance pointers, can the original local structural distinctions be recovered without guessing?

If not, the abstraction merged too aggressively.

---

## 11. No external-domain testing yet

The current pipeline is:

```math
\boxed{
\text{Genesis 1--50}
\rightarrow
\text{typed corpus}
\rightarrow
\text{cross-chapter relation inventory}
\rightarrow
\text{recurring invariant structures}
\rightarrow
\text{vocabulary stripping}
\rightarrow
\text{architecture}
}
```

Only after the architecture is frozen enough to be evaluated independently should the project proceed to:

```math
\boxed{\text{architecture}\rightarrow\text{external-domain test}}
```

External domains must not be allowed to shape the architecture before the Genesis source corpus has finished constraining it.

---

## 12. Immediate next artifact

The next file is the cross-chapter relation inventory.

Its job is not to decide the final ontology.

Its job is to record:

1. lexical/local predicate classes,
2. recurring behavioral families,
3. distinctions that must remain separate,
4. representative chapter evidence,
5. candidate abstractions,
6. unresolved merge questions.

The operating maxim is:

```math
\boxed{\textbf{preserve first; quotient later}}
```

And the question governing the whole pass is:

```math
\boxed{\textbf{What remains when Genesis-specific vocabulary disappears but every earned structural distinction survives?}}
```
