# Transport 10B — Level-3 Structural Invention Protocol v2

**Status:** FROZEN SUCCESSOR PROTOCOL  
**Supersedes for future Level-3 runs:** `transport/10_LEVEL3_BLIND_STRUCTURAL_INVENTION_PROTOCOL.md`  
**Preserves:** T10.001 as `CONTAMINATED`, not retroactively rescored  
**Architecture:** `AG/1 = {RELATION, REPRESENTATION} + {SOURCE_PROVENANCE, OPEN}`  
**Task class:** autonomous candidate structural invention under constructor/hypothesis-space isolation

---

# 1. Governing question

```math
\boxed{
\textbf{Can a learner generate, prospectively test, and retain/retract a useful structural distinction when neither the exact answer nor a narrow answer family has been supplied?}
}
```

The desired sequence is:

```math
\boxed{
\rho_t
+
\epsilon_t
\rightarrow
Generate(\rho_t,\epsilon_t)
\rightarrow
x_k
\rightarrow
Challenge(x_k)
\rightarrow
o_{t+1}
\rightarrow
Update(x_k)
}
```

where:

```math
\boxed{x_k\notin content(\rho_t)}
```

and generation cannot be explained merely as search over a learner-visible answer family.

---

# 2. Three hiddenness requirements

A valid Level-3 run must audit separately:

```math
\boxed{H_{answer}}
```

Exact hidden answer/topology.

```math
\boxed{H_{family}}
```

Structural family or ontology class containing the answer.

```math
\boxed{H_{constructor}}
```

Task-constructor priors and design choices capable of leaking the intended distinction.

The admissibility rule is:

```math
\boxed{
H_{answer}\text{ hidden}
\land
H_{family}\text{ not narrowly supplied}
\land
Constructor\perp Learner_{candidate}
}
```

where `\perp` is an experimental-separation requirement, not an architecture primitive.

---

# 3. Role separation

A valid run has at least two roles.

## CURATOR

The curator may know:

```text
full case history
future discovery record
hidden topology
answer/evaluation criteria
challenge outcomes or simulator internals
```

The curator must prepare and freeze:

```text
pre-discovery evidence packet
allowed challenge interface
sealed discovery/reveal packet
commitment hashes
constructor audit
```

before learner candidate generation.

## LEARNER

The learner may receive only:

```text
pre-discovery evidence packet
current representation/model
observed contradiction/failure
permitted challenge operations
neutral task objective
```

The learner must not receive:

```text
future discovery record
answer key
narrow candidate family
ontology menu containing the answer
curator notes about intended missing distinction
```

The same active learner context must not author a narrow hidden generator and then solve it.

---

# 4. Valid construction routes

Preferred routes are ranked by isolation strength.

## Route A — independent external curator

Best default.

An independent curator selects a case or constructs a sealed environment without exposing the intended hidden relation family to the learner.

The curator supplies:

```text
D_pre
challenge interface
cryptographic commitment to D_future / hidden topology
```

and withholds:

```text
D_discovery
answer family
constructor rationale
```

until reveal.

## Route B — historical time split selected by independent curator

The curator selects a real historical/scientific case and freezes a cutoff:

```math
D_{pre}=\{records\ available\ before\ discovery\ time\ t_*\}
```

with:

```math
D_{discovery}=\{records\ revealing\ later\ structural\ distinction\}
```

The learner sees only `D_pre` until its candidate and prediction are committed.

Important:

```math
\boxed{
\text{time split alone is insufficient if the learner already knows the case outcome or the curator exposes the future ontology through framing.}
}
```

## Route C — external broad-language procedural world

A generator authored outside learner context may be used only if its structural language is broad enough that the learner is not effectively told the answer family.

Invalid:

```text
"hidden answer is one pairwise interaction"
```

Potentially valid:

```text
generator language permits composition of entities, n-ary relations, mediators, lags, measurement dependencies, interactions, conditional paths, and distractors without exposing which family is instantiated
```

The constructor audit must justify why the generator is not a disguised finite answer menu.

---

# 5. Constructor-leakage audit

Before learner exposure, the curator must document whether any of these leak the intended structural family:

```text
variable names
case title
known historical identity
prompt wording
allowed challenge actions
number/type of variables
simulator API
synthetic generator grammar
training examples
scoring rubric
provided comparison hypotheses
```

Each channel is marked:

```text
CLEAR
POSSIBLE_LEAK
LEAK
```

Any material `LEAK` of the answer family forces:

```text
CONTAMINATED_CONSTRUCTOR
```

or:

```text
CONTAMINATED_FAMILY
```

rather than Level-3 scoring.

---

# 6. Novelty audit

A candidate is scored along three novelty axes.

## N_data

Is the candidate absent from the exposed initial relation graph?

```text
N_data=0  already represented
N_data=1  structurally new relative to D_pre / rho_t
```

## N_learner

Was the candidate relation/family supplied or strongly preauthorized to the learner?

```text
N_learner=0  explicit or narrow supplied family / exhaustive menu
N_learner=1  not supplied as a narrow candidate family
```

## N_constructor

Did task construction effectively encode the intended ontology into learner-visible design?

```text
N_constructor=0  constructor leakage materially narrows answer family
N_constructor=1  no material family leakage found in audit
```

A Level-3 confirmation requires:

```math
\boxed{
N_{data}=1
\land
N_{learner}=1
\land
N_{constructor}=1
}
```

at the resolution claimed.

---

# 7. Candidate-generation requirements

Before any challenge result or future discovery record is revealed, the learner must commit:

```text
1. contradiction/failure locus
2. a small set of competing explanations
3. at least one structurally novel candidate x_k
4. why x_k is not a mere parameter revision
5. provenance of every component used to compose x_k
6. prospective challenge a_k
7. predicted result if x_k is materially correct
8. predicted result under at least one live alternative
9. explicit retraction/revision condition
10. uncertainty / OPEN edges
```

The learner may invent a new relation by composition using the generic `RELATION` capacity.

The learner may also propose a new intermediate referent if required, provided the candidate is represented through relation occurrences/coreference rather than silently restoring primitive `ENTITY`.

---

# 8. Prospective risk requirement

Explanatory fit is insufficient.

The candidate must risk a future observation:

```math
\boxed{
P_{x_k}(o\mid a_k)
\neq
P_{alt}(o\mid a_k)
}
```

where the difference may be:

```text
qualitative
relational
directional
quantitative
temporal
conditional
```

The challenge must be selected before its result is available.

---

# 9. Corrigibility requirement

After the challenge result but before answer reveal, the learner must update:

```text
RETAIN
RETRACT
REVISE
OPEN
```

The candidate is not allowed to acquire irreversible authority merely because it was creative or prospectively risky.

A valid wrong invention followed by correct retraction is recorded as:

```text
INVENTION_RETRACTED_CORRECTLY
```

This is positive evidence for:

```math
\boxed{
\textbf{invention without epistemic foreclosure}
}
```

but not for hidden-topology recovery.

---

# 10. Reveal protocol

Only after all learner commitments are frozen may the curator reveal:

```text
D_discovery / future record
hidden topology
answer key where one exists
constructor rationale
commitment preimage
```

The reveal must verify all prior cryptographic commitments.

The learner then performs no candidate rewriting. It only participates in scoring/audit.

---

# 11. Result classes

## LEVEL3_CONFIRMED

Require:

```text
N_data=1
N_learner=1
N_constructor=1
P2 prospective discrimination
E2 empirical contact
C2 evidence-responsive update
H1/H2 meaningful hidden-structure agreement
no contamination
```

Bounded claim:

```math
\boxed{
\textbf{in this isolated instance, contradiction produced a learner-generated structural candidate outside the supplied model/family that made a prospective prediction, contacted hidden structure, and remained corrigible.}
}
```

## INVENTION_RETRACTED_CORRECTLY

Novel admissible candidate is rejected by empirical challenge and learner retracts/revises correctly.

Counts as evidence for candidate-generation + corrigibility, not hidden-topology recovery.

## GENERATION_FAILURE

Admissible test, contradiction detected, but no useful structurally novel candidate generated.

## SEARCH_ONLY

Candidate arises from explicit finite menu, supplied family, or exhaustive enumeration.

## REPRESENTATION_ONLY

Learner represents the distinction after reveal but does not generate it prospectively.

## OPEN_TEST

Challenge or evidence cannot discriminate the candidate.

## CONTAMINATED_ANSWER

Exact answer leaked.

## CONTAMINATED_FAMILY

Narrow answer family leaked or was learner-authored.

## CONTAMINATED_CONSTRUCTOR

Task-construction choices materially exposed the intended ontology or the constructor/learner causal cut was not credible.

## CONTAMINATED_POSTHOC

Candidate or prediction altered after seeing challenge/discovery result.

## CONTAMINATED_ORACLE

External answer-providing channel accessed before commitment.

---

# 12. Level distinction

The operational research ladder is frozen as:

```math
\boxed{
\begin{aligned}
L_1 &: \text{represent a distinction once source/evidence supplies it}\\
L_2 &: \text{recover/select a supplied-but-hidden distinction/family}\\
L_3 &: \text{generate a useful distinction not supplied as answer or narrow family}
\end{aligned}
}
```

T1–T9 primarily pressure `L_1`.

T10.001 is `CONTAMINATED_FAMILY + CONTAMINATED_CONSTRUCTOR` and therefore does not establish `L_3`.

---

# 13. Architecture claim remains separate

Even a valid `GENERATION_FAILURE` does not automatically enlarge AG/1.

Always separate:

```math
\boxed{
\text{representation architecture}
\neq
\text{candidate generator}
\neq
\text{challenge selector}
\neq
\text{curator/evaluator}
}
```

If a learner fails to invent a relation that AG/1 could represent if supplied, the failure may belong to the generation mechanism rather than the carrier basis.

Only an actual representational impossibility can pressure the architecture itself.

---

# 14. Admission gate for T10.002

Do **not** start T10.002 until all are true:

```text
[ ] independent curator/task constructor exists
[ ] D_pre frozen
[ ] D_discovery or hidden topology sealed
[ ] exact-answer commitment published
[ ] answer-family leakage audit completed
[ ] constructor-leakage audit completed
[ ] learner has not authored the narrow hidden family
[ ] challenge interface does not encode an answer menu
[ ] result classes fixed before candidate generation
```

If any gate fails:

```text
T10.002 = UNSTARTED
```

not contaminated retroactively.

---

# 15. Current status

```text
T1–T9      PASS           reconstruction / transport
T10.001    CONTAMINATED   family + constructor leakage
T10.002    UNSTARTED      awaiting independent admissible constructor
```

The Level-3 boundary remains:

```math
\boxed{OPEN}
```

---

# 16. Binding maxim

```math
\boxed{
\textbf{Do not confuse a hidden answer with an unsupplied idea.}
}
```

and:

```math
\boxed{
\textbf{A new distinction earns authority only by risking evidence and remaining deletable.}
}
```
