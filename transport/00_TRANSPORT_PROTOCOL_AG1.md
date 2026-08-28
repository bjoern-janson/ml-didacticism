# AG/1 External Transport Protocol

**Status:** FROZEN TEST PROTOCOL  
**Architecture under test:** `abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md` (`AG/1`)  
**Purpose:** test transportability without allowing the external corpus to modify the frozen Genesis-derived architecture

The architecture under test is fixed:

```math
\boxed{
\mathcal A_G
=
\{RELATION,REPRESENTATION\}
+
\{SOURCE\_PROVENANCE,OPEN\}
}
```

The governing causal boundary is:

```math
\boxed{\mathcal A_G\ \textbf{cannot learn from the external corpus.}}
```

An external corpus may only:

```text
fit AG/1
or
expose a distinction AG/1 cannot reconstruct
```

It may not alter `AG/1` during the run.

---

# 1. Allowed machinery

## RELATION

The test may create new **source-earned typed predicates** required by the external corpus, for example:

```text
RUNS_ON
REPORTS
TIMES_OUT
DELETES
RESTORES
PROPOSES
EXECUTES
FAILS
RECOVERS
BEFORE
DURATION
SAME_REFERENT
```

New predicate vocabulary is not a new architecture primitive.

Each relation must preserve:

```text
role-resolved argument occurrences
source provenance
polarity where explicit
multiplicity / occurrence identity where required
```

## REPRESENTATION

The test may create scoped structured content whose internal relations are not thereby asserted into history:

```math
r\in content(\rho)\not\Rightarrow r\in\mathcal H
```

This includes source-earned:

```text
hypotheses
reports
suspicions
plans
forecasts
later causal analyses
counterfactuals
uncertain recovery expectations
```

No assumption is made that a representation is believed, correct, endorsed, or complete unless the corpus establishes that relation.

## SOURCE_PROVENANCE

Every historical assertion, representation scope, coreference bridge, and OPEN boundary must be traceable to the external source.

## OPEN

If the corpus does not justify an edge, identity bridge, causal link, temporal link, or interpretation, leave it OPEN.

```math
\boxed{\text{missing}\neq\text{false}\neq OPEN}
```

---

# 2. Forbidden rescue machinery

The following may not be introduced during a transport run:

```text
ENTITY as a primitive carrier
STATE as a primitive carrier
EVENT as a primitive carrier
TIME as a primitive carrier
ACCESS as a primitive carrier
COMMITMENT as a primitive kernel
AUTHORITY as a primitive kernel
```

Nor may they return as hidden fields:

```text
entity_id
state_blob
event_object
timestamp / hidden global clock
access=true
commitment_force
authority_level / decision_right
```

Likewise, `REPRESENTATION` may not be replaced or extended by an unrestricted generic context field whose only purpose is to rescue a failing case.

The anti-cheat rule is:

```math
\boxed{
\textbf{a deleted primitive may not reappear as an unrestricted parameter, opaque token, or renamed carrier.}
}
```

---

# 3. External-case reconstruction requirements

For each case, attempt to preserve at least the distinctions the source itself requires among:

```text
historical assertions
agent/source reports
agent/source hypotheses or explanations
plans/proposals
performed operations
observed outputs
later retrospective causal accounts
contradictory or incomplete information
object/data provenance
recipient inference
successful and failed actions
unrealized versus realized represented content
```

The test does **not** require every case to contain every class.

It requires lossless reconstruction of the distinctions that the external source actually supplies.

---

# 4. Verdict classes

Exactly one top-level verdict is assigned to each bounded test case.

## PASS

Use when all source-required distinctions reconstruct with:

```text
RELATION
+
REPRESENTATION
+
SOURCE_PROVENANCE
+
OPEN
```

and the hidden-parameter audit passes.

PASS does not mean AG/1 is universal. It means only that the tested case did not force a missing primitive.

## FAIL_RECONSTRUCTION

Use when a source-required distinction cannot be represented without adding architectural machinery not present in AG/1.

Required failure record:

```text
smallest failing witness
missing distinction
attempted AG/1 reconstruction
exact information lost or conflated
why new relation vocabulary alone is insufficient
```

Do **not** repair AG/1 in the same artifact.

## FAIL_HIDDEN_PARAMETER

Use when a reconstruction appears successful only because a deleted primitive has been smuggled back through a field, opaque token, carrier, or unrestricted parameter.

Required failure record:

```text
smuggled primitive
location of smuggling
why removing that hidden parameter breaks reconstruction
```

## OPEN_TEST

Use when the external source is too underspecified, ambiguous, or provenance-poor to decide whether AG/1 succeeds or fails.

OPEN_TEST is not a pass.

---

# 5. Unit of testing

A transport run should use a bounded, provenance-identifiable external corpus or incident.

For each run record:

```text
source title
source organization/author
publication date if available
source URL / stable identifier
scope included
scope excluded
```

Do not silently supplement the bounded source with external facts merely to make reconstruction easier.

If a second source is needed, add it explicitly to the corpus boundary before using it.

---

# 6. Reconstruction form

A transport artifact should contain:

```text
1. corpus boundary
2. source-native grammar / incident sequence
3. historical relation graph
4. representation scopes
5. provenance distinctions
6. OPEN edges
7. hidden-parameter audit
8. smallest potential failure witness
9. verdict
```

A convenient schematic form is:

```text
HISTORY
    PREDICATE(args...)

REPRESENTATION rho_1
    source/holder: ...
    mode: source-earned
    content:
        PREDICATE(args...)

PROVENANCE
    assertion -> source location

OPEN
    unresolved bridge
```

This is syntax only. It does not add a new primitive.

---

# 7. Vocabulary versus architecture

A critical transport distinction is:

```math
\boxed{
\text{new source predicate}\neq\text{new architecture primitive}
}
```

A software incident may force predicates Genesis never lexicalized, such as:

```text
REPLICATION_LAGS
PROCESS_HANGS
BACKUP_FAILS
EMAIL_REJECTED
RESTORE_FROM
```

Those are allowed if source-earned.

A transport failure occurs only when the case requires a new **structural species**, not merely new vocabulary.

---

# 8. Failure accumulation and architecture revision

One external failure does not modify AG/1.

The causal sequence is:

```math
\boxed{
AG/1
\rightarrow
external\ test
\rightarrow
failure\ record
\rightarrow
independent\ discrimination
\rightarrow
possible\ new\ architecture\ version
}
```

If revision is later warranted, create a new artifact/version such as:

```text
A_ext/1
AG/2
```

but never rewrite `12_GENESIS_ARCHITECTURE_FREEZE.md` or this protocol to make an earlier test pass.

---

# 9. Claim ceiling

A PASS supports only:

```math
\boxed{\textbf{AG/1 reconstructed this bounded external case without a new primitive.}}
```

A failure supports only:

```math
\boxed{\textbf{this bounded external case exposes a distinction not reconstructed by AG/1 under the frozen rules.}}
```

Neither result alone establishes universal sufficiency or universal failure.

---

# 10. First transport corpus selection

The first planned external corpus is a public software-incident postmortem rather than a literary, sacred, or philosophical text.

Selection criteria:

```text
empirical/technical
independent domain vocabulary
world/process assertions
multiple operators/systems
reports and hypotheses
performed actions
outcomes
incomplete or mistaken information
later causal analysis
recoverable source provenance
```

The intended first run is GitLab's January 31, 2017 database-outage postmortem.

The protocol above is frozen before incident-specific reconstruction decisions are made.

---

# Frozen transport invariant

```math
\boxed{
\textbf{The external corpus is allowed to falsify the fit; it is not allowed to teach AG/1 new primitives during the test.}
}
```
