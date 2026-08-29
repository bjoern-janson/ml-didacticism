# CAPITAL FOR MACHINES

## How Reasons Accumulate, Acquire Authority, and Remain Revisable

**A synthetic manuscript from the 57-repository research program**  
**Version 0.3.1 — claim-to-artifact provenance edition; structurally coherent, evidentially provisional**

---

## Reader's notice

This book has two readers in mind: a person following an argument and a machine reconstructing an epistemic object.

The prose is the human traversal. The labels, claim records, dependency statements, counterexamples, and reopening conditions are the machine-facing spine. They are not decorative metadata. They are part of the work's method.

This manuscript is a synthesis of repository analyses and research artifacts. It is not a claim that the program has already demonstrated a general theory of intelligence, corrigibility, open-ended evolution, or alignment. Many source repositories are conceptual proposals; others contain toy implementations or local benchmark results; a smaller number contain executable systems whose claims remain narrower than their surrounding theory. The book preserves those differences.

The governing rule is:

> Understanding a claim does not constitute accepting the claim.

An intelligent reader should be able to reconstruct the strongest version of an argument, identify what supports it, find what it does not establish, and produce a defeater if one exists. A reader who rejects a claim for good reasons has not failed the book. The book has done its job.

### Source-count notice

```text
N_claimed:     57 repositories
N_enumerated:  56 repository report families
ΔN:             1 unresolved
ID:             PROV-COUNT-001
STATUS:         OPEN
```

The surrounding project has been described as a 57-repository program, while the supplied report archive contains 56 distinct repository families. This discrepancy is preserved deliberately pending provenance resolution. It is not treated as evidence for or against the program's conceptual claims.

---

## How to read this book

`[SYNTHESIS]` The core traversal is:

```text
distinction
  → representation
  → composition
  → authority
  → accumulation
  → naturalization
  → crisis
  → correction
  → redrawing the object
```

Each chapter follows a repeated pattern:

1. **Construction** — introduce only the vocabulary needed.
2. **Productive success** — show why the abstraction is useful.
3. **Accumulation** — let later reasoning depend on it.
4. **Defeater** — introduce a consequence, observation, or distinction that puts pressure on it.
5. **Correction** — localize what must change and what should survive.
6. **Audit** — state what the episode actually established.
7. **Inheritance** — carry the surviving structure forward.

The repetition is deliberate. The book is not merely describing a correction loop. It is trying to enact one.

### Epistemic labels

The labels used here mean:

| Label | Meaning |
|---|---|
| `[OBSERVED]` | Directly present in a source artifact or reproduced local behavior. |
| `[REPORTED]` | Asserted by a source report or repository document but not independently established here. |
| `[DERIVED]` | Follows from identified claims, observations, or formal relations. |
| `[SYNTHESIS]` | A retrospective compression across multiple source strata; coherence does not independently validate the compressed pattern. |
| `[MECHANISM]` | A proposed causal explanation, not automatically demonstrated. |
| `[HYPOTHESIS]` | A conjecture intended to be tested. |
| `[LIMIT]` | A boundary on what the evidence permits us to say. |
| `[OPEN]` | A question whose answer remains unresolved. |
| `[DEFEATED]` | A claim or procedure withdrawn because a specified defeater applies. |
| `[PROCEDURE]` | A rule for conducting, auditing, or authorizing an operation. |

### Claim object

Major claims are addressable as objects of the form:

```text
<claim>
ID: CM-XXX
TYPE: DERIVED | OBSERVED | MECHANISM | HYPOTHESIS | LIMIT
STATUS: OPEN | LOCAL | WITHDRAWN | FROZEN
ASSERTION: ...
AUTHORITY_TYPE: EPISTEMIC | CAUSAL | NORMATIVE
SUPPORTED_BY: ...
PROVENANCE_NODES: ...
DEPENDS_ON: ...
CONSTRAINED_BY: ...
SCOPE: ...
SYSTEM_BOUNDARY: ...
COUNTEREXAMPLES: ...
DEFEATED_BY: ...
REOPEN_IF: ...
STRONGER_READING_BLOCKED: ...
CLAIM_CEILING: ...
</claim>
```

The book's argument is not allowed to float free of these fields.

### Authority type boundary

`Authority` is typed by what it is allowed to do. The book uses three non-interchangeable senses:

```text
epistemic authority  = support a claim, warrant, or belief
causal authority     = influence a future mechanism, state, or behavior
normative authority  = permit or require an action, evaluation, or revision
```

Operational authorization is treated here as a scoped form of normative authority. A mechanism may have causal influence without epistemic warrant; a statement may have epistemic support without permission to act; a proposal may be normatively admissible without being true. No authority type silently converts into another.

An authorized support graph records claims, evidence routes, transformations, scopes, defeaters, and aggregation rules. It is not restricted to a single lineage: independent support paths may compose into stronger warrant only when their independence, compatibility, scope, and aggregation rule are visible. Mere multiplicity is not independence, and independent support does not automatically grant causal or normative authority.

### Notation normalization

The machine-facing notation is normalized as follows:

```text
Ω              = state or task space
C_B(x)         = baseline cost of reaching x
τ              = a transformation
𝒢_t            = reachable adaptive-mechanism space at time t
𝒲              = warrant or authority structure
𝒫              = a permitted or operational pathway
```

Inline mathematical symbols use the same names in prose and equations. A notation definition does not itself establish the existence of the object it names.

### Synthesis boundary

`[SYNTHESIS]` marks a retrospective compression across source strata. It is a statement about a pattern that becomes visible when the repositories are read together. It is not a claim that every source intended the pattern, that the historical order proves the pattern, or that coherence validates it.

The book therefore distinguishes:

```text
repo proposes X
  ≠ repo implements X
  ≠ repo reports result X
  ≠ current audit reproduces X
  ≠ current synthesis infers X
```

The last step can be useful and still be provisional. A coherent synthesis is itself a compression operation and must remain open to a counterexample.

---

# PROLOGUE — THE MACHINE THAT GETS BETTER

Imagine a system that performs better every month.

Its answers improve. Its search becomes faster. Its representations become more compact. It finds routes that were previously inaccessible. It can modify parts of its own process and retain changes that appear useful.

We call this progress.

Sometimes it is.

But performance is an event in the present. Improvement capacity is a relation between the present and possible futures. A system can become better at the tasks it already knows how to recognize while becoming less able to discover that its task descriptions, representations, evaluators, or correction routes are inadequate.

The difference is easy to state and difficult to preserve:

```text
current performance
  ≠ adaptive capacity
  ≠ correction capacity
  ≠ capacity to improve the mechanism of improvement
```

Let $V_{future}(S,F)$ denote the viable futures available to system $S$ when it receives feedback $F$, and $V_{future}(S,\varnothing)$ the viable futures available without that feedback. The research program begins with a hypothesis:

<claim>
ID: CM-001
TYPE: HYPOTHESIS
STATUS: OPEN
AUTHORITY_TYPE: EPISTEMIC
ASSERTION: $I ∝ C_{improve}$, where $C_{improve} = V_{future}(with\ corrective\ feedback) − V_{future}(without\ corrective\ feedback)$.
SUPPORTED_BY: `cognitive-core`, `adaptive-intelligence-framework`, `CARS`, and the opening research logic.
PROVENANCE_NODES: P001, P002, P003, P004
DEPENDS_ON: CM-002, CM-004, CM-005
CONSTRAINED_BY: none
SCOPE: A proposed research direction, not a validated universal law.
SYSTEM_BOUNDARY: Research-program hypothesis over the cited conceptual/protocol artifacts; no deployed-agent boundary is asserted.
COUNTEREXAMPLES: Any system whose feedback increases local performance while reducing future recoverability.
DEFEATED_BY: A controlled result showing that the proposed improvement-capacity quantity has no explanatory or predictive value under its stated operationalization.
REOPEN_IF: The meaning of improvement capacity, feedback, and viable futures is revised.
STRONGER_READING_BLOCKED: The equation does not imply that current performance is unimportant or that feedback is always beneficial.
CLAIM_CEILING: No general intelligence result follows from this equation alone.
</claim>

The equation is not the conclusion of the book. It is the pressure that drives it.

The question is not simply whether a system can make a better move. It is whether feedback can reach the machinery that determines what counts as a move, what counts as evidence, which transformations acquire authority, and which futures remain available after the system has committed itself.

The loop is therefore:

```text
distinguish
  → transform
  → reconstitute
  → continue
  → distinguish better
```

The loop can enlarge a system's future. It can also make the system more efficient at preserving its own mistakes. The difference lies in what is represented, what is retained, and what can still be reached by correction.

That is the subject of this book.

---

# BOOK I — DISTINCTION

## 1. The wrong question

The first mistake is to ask, “How intelligent is the system?” as though intelligence were a single visible substance.

The source program begins elsewhere. It asks what transformations a system can perform, what future states they make reachable, and whether the system can revise the machinery that produces those transformations.

This produces a hierarchy:

```text
answer quality
  → adaptation within a mechanism
  → change to the mechanism
  → change to the generator of mechanisms
  → preservation of the capacity to change the generator
```

The hierarchy is not a ladder of moral worth or a completed empirical scale. It is a set of distinctions. A parameter update is not automatically a representation change. A representation change is not automatically a generator change. A generator change is not automatically consequence-shaped, externally grounded, or corrigible.

The `cognitive-core`, `cognitive-evolution-architecture`, `adaptive-intelligence-framework`, and `adaptive-intelligence-theory` materials converge on a small persistent loop:

```text
state
  → observe
  → predict
  → act
  → observe consequence
  → evaluate
  → correct
  → persist state with history
```

The proposed state is often written in a form such as:

```text
K_t = (R_t, M_t, G_t, Λ_t)
```

where representation, memory, goals or constraints, and provenance/history are kept conceptually distinct.

The point is not that this tuple is the one true architecture. The point is that a system cannot correct what it has no way to distinguish, and it cannot preserve a correction pathway that it has compressed into an undifferentiated result.

### A proposed invariant

<claim>
ID: CM-002
TYPE: DERIVED
STATUS: OPEN
AUTHORITY_TYPE: EPISTEMIC
ASSERTION: A future-relevant distinction must remain distinguishable or reconstructible through an available correction path if future correction is to recover it.
SUPPORTED_BY: `ml-didacticism` Genesis corpus and abstraction/ablation materials; `cognitive-core`; `SSI`.
PROVENANCE_NODES: P001, P005, P006, P007, P008, P021
DEPENDS_ON: none
CONSTRAINED_BY: CM-003, CM-006, CM-008
SCOPE: Systems whose future behavior depends on stored or reconstructed epistemic state.
SYSTEM_BOUNDARY: The effective correction system must be fixed before evaluation. An external oracle counts only if it was declared as part of that system in advance.
COUNTEREXAMPLES: A system may correct through an external oracle after internal distinctions are lost; this relocates the required representation to the effective correction system rather than eliminating the requirement.
DEFEATED_BY: A demonstrated correction protocol that reliably recovers a defeated distinction without any preserved or reconstructible route to it.
REOPEN_IF: The system boundary and the meaning of “preserved” are changed.
STRONGER_READING_BLOCKED: Distinguishability or reconstructibility is a necessary design condition in the stated setting, not a sufficient condition for intelligence or correction.
CLAIM_CEILING: This is a design invariant and hypothesis, not a proof of intelligence.
</claim>

This is why the program is preoccupied with distinctions that ordinary conversation often collapses:

```text
event          ≠ report
evidence       ≠ inference
identity       ≠ signal
representation ≠ reality
proposal       ≠ authorization
possibility    ≠ opportunity
dependency     ≠ warrant inheritance
stored         ≠ recoverable
recoverable    ≠ triggerable
triggerable    ≠ actionable
```

Convenience is not free. Every collapse transfers work from the present to the future. Sometimes the transfer is harmless. Sometimes the future is precisely the moment when the missing distinction becomes necessary.

## 2. The cost of collapse

A system does not usually lose corrigibility by announcing that it will become uncorrectable. It loses it through a series of locally reasonable compressions.

An observation is summarized. A source is replaced by a citation. A causal pathway is represented by its endpoint. A conditional statement is promoted to a fact. A proposal is treated as permission. A mechanism's past success becomes a reason to trust it in a new context. A benchmark's answer is retained while the path by which the answer was earned is discarded.

Every step can improve short-term usability.

The danger appears only under a future that was not part of the original compression objective.

The Genesis-based `ml-didacticism` corpus is valuable here not because it supplies a theology of AI, but because it provides a large collection of anti-collapse cases. Its structural readings repeatedly distinguish material source, textual report, interpretation, authority, and realization. The exact subject matter is less important than the discipline: a sentence may mention a relation without asserting it; a report may preserve a proposition without establishing its provenance; an authentic component may participate in a false composition.

The compact invariant is:

```text
truth of component
  ≠ truth of composition
```

This sounds obvious until a reasoning system is built from components whose interfaces erase the conditions under which each component was warranted.

The problem is not only falsehood. It is composition without visible composition.

### A machine-facing question

For every representation, ask:

```text
What distinctions did this representation preserve?
What distinctions did it collapse?
Which future defeaters would make the collapsed distinctions relevant?
```

The third question is the one ordinary optimization often omits. It is also the one that turns compression into a corrigibility problem.

---

# BOOK II — REPRESENTATION

## 3. A representation is an intervention

Representation is often treated as a passive mirror. In the source corpus it is closer to an intervention on the cost landscape of thought.

The `computational-leverage` and `interface-induced-computational-geometry` materials describe an interface, algorithm, compiler, notation, or model as something that changes which tasks are reachable under bounded resources. In schematic form:

```text
intervention
  → transformed cost landscape
  → altered reachable region
  → altered capability under the same budget
```

Let $Ω$ be a space of tasks or states, $A$ a bounded resource budget, and $C_B(x)$ the cost of reaching $x$ in baseline environment $B$. The reachable set is:

```text
R(B) = { x ∈ Ω | C_B(x) ≤ A }
```

An intervention (v) transforms the cost landscape. It may make a previously expensive task cheap. It may also make some distinctions inaccessible, even while expanding the region of tasks that can be completed.

This is the first place where “better” divides in two:

```text
more reachable tasks
  ≠ more correct representations
  ≠ more revisable representations
```

The `resolution-horizon`, `computational-resolution-horizon`, `representation-elasticity`, `adaptive-metric-compiler`, and `alignment-spine` materials all circle this boundary from different directions. They ask how finely a system can resolve a problem, how the representation changes the computational geometry of the problem, and whether the system's objective-relevant information survives the transformation.

The most important distinction is not resolution alone.

```text
resolution = how finely?
unitization = of what?
```

A system can solve every item in a partition while the partition itself is wrong. It can optimize over the wrong objects with extraordinary precision.

### Wrong-object example

Suppose a system assigns an error score to objects (o_1,ldots,o_n). Every local score is excellent:

```text
LocalFit(o_i) = 1  for every i
```

But the system's unitization (U) maps the world into objects that cannot express the interaction responsible for future failure:

```text
S → U → O_U → Z
```

The system can then achieve perfect local fit while missing the structure that matters.

This is not a failure of optimization in the narrow sense. It is a failure of object construction.

## 4. The minimal carrier

The `ml-didacticism` abstraction and ablation materials provide a second lesson. A research program can begin with a rich ontology—entity, state, event, time, access, commitment, authority—and then repeatedly ask whether each candidate is truly primitive.

The final AG/1 freeze retains:

```text
AG/1 = { RELATION, REPRESENTATION }
       + { SOURCE_PROVENANCE, OPEN }
```

This is not a universal metaphysics. It is the result of a particular adversarial derivation. The candidates removed as primitive carriers do not become meaningless. Commitment, authority, event, and state can remain semantically important. The ablation says only that they need not be irreducible storage primitives in this architecture.

That difference matters because terminology can naturalize a provisional result. An intermediate document may call something an “irreducible kernel” while a later freeze rejects it as a primitive carrier. The correct repair is not to erase one document. It is to mark the layer:

```text
semantic residue
  ≠ primitive implementation carrier
```

### The ablation question

For every proposed primitive, ask:

```text
What work is this candidate carrying?
Can that work be represented as a relation?
Can the relation remain attributable to a source?
What is lost if the candidate is removed?
```

An ontology becomes useful when its deletions are as legible as its inclusions.

<claim>
ID: CM-003
TYPE: DERIVED
STATUS: LOCAL
AUTHORITY_TYPE: EPISTEMIC
ASSERTION: A minimal representation is trustworthy only when the work removed by ablation, the work retained by surviving primitives, and the future failures that would reopen the ablation are explicit.
SUPPORTED_BY: `ml-didacticism` abstraction/ablation and AG/1 freeze reports.
PROVENANCE_NODES: P005, P006
DEPENDS_ON: CM-002
CONSTRAINED_BY: CM-005, CM-008
SCOPE: The AG/1-style derivation and analogous representation-minimization procedures.
SYSTEM_BOUNDARY: The AG/1 derivation and the operations admitted by that frozen representation; no universal ontology boundary is asserted.
COUNTEREXAMPLES: A redundant representation may be safer than a minimal one if redundancy preserves independent correction routes.
DEFEATED_BY: A minimal carrier that reliably supports all authorized operations without exposing its deletion boundaries.
REOPEN_IF: The operational task or correction regime changes.
STRONGER_READING_BLOCKED: Minimality is not automatically safety, elegance, or universality.
CLAIM_CEILING: The AG/1 result is not a universal ontology.
</claim>

## 5. The interface is part of the theory

An interface does not simply transmit a state. It determines which distinctions can cross a boundary, which transformations are visible, and which errors are attributable.

The `interface-theory` materials separate multiple gates: representation, transport, dynamic factorization, and adaptive-capacity measurement. The key issue is not whether a signal passes through an interface. It is whether the interface preserves the causal identity needed to interpret what passed.

This is why a content-addressed artifact is not automatically external evidence. A prediction file may be authentic as a file while its confidence score remains only an internal property of the predictor. The `alphafold3-oc` adapter is a clean example of the boundary: stock AlphaFold 3 produces an output tree; an adapter registers that output into a frozen OpenCore structure. The adapter can preserve bytes and provenance without converting the model's confidence into an externally warranted claim about the world.

```text
prediction metadata
  ≠ external evidence

content identity
  ≠ causal validity

successful registration
  ≠ scientific confirmation
```

The `tevpp` codebase offers a different, non-theoretical reminder. In a mature image application, data formats, color management, caches, shaders, GUI state, IPC, and process lifecycle form a web of interfaces. A local change can appear harmless while changing the meaning available at another boundary. The lesson is not that `tev` proves a theory of intelligence. The lesson is that interface behavior becomes part of system behavior whether or not the documentation names it.

---

# BOOK III — THE PRODUCTION OF REASONS

## 6. A conclusion is a transformation

A conclusion is often stored as though it were a node that appeared by itself. The program insists on recovering the operation that produced it.

```text
K₁, K₂  ──τ──>  K₃
```

The transformation (	au) may combine observations, apply a rule, select a candidate, compress a trace, update authority, or alter the mechanism that will generate later updates.

The content of (K_3) is not the whole epistemic object. The object includes the transformation, its inputs, its scope, its authorization, and the route by which it can be challenged.

This yields a crucial asymmetry:

```text
provenance of content
  ≠ provenance of transformation
```

A system may know where a statement came from while failing to know why this statement was allowed to function as a premise. It may retain the evidence while losing the composition rule that created its authority.

The `signature-relative-equivalence` work sharpens this point through a bounded formal setting. Two systems can be equivalent relative to an exposed signature while differing in hidden behavior or future correction properties. Equivalence is always relative to what the interface observes.

```text
equivalent under signature Σ
  ≠ equivalent under every future defeater
```

This is not an argument against abstraction. It is an argument for recording the signature and its limits.

## 7. Authority is produced, not merely possessed

The source program uses several vocabularies—authority, confidence, mechanism weight, warrant, eligibility, authorization—but the recurring distinction is stable:

```text
REALIZED(τ)
  ≠ VALID(τ)
  ≠ APPLICABLE(τ)
  ≠ AUTHORIZED(τ,S)
```

A transformation can occur without being valid. It can be valid in one scope without being applicable in another. It can be applicable without being authorized for a given state or purpose.

The `law-of-adaptive-authority-dynamics`, `adaptive-inheritance`, `theory-of-adaptive-epistemic-systems`, and `RAHU` materials give the transformation an operational shape. Mechanisms are assigned authority values. Residuals between expected and observed outcomes are attributed to mechanisms. Authority may be attenuated when a mechanism is implicated in failure, and may recover after demonstrated viability improvement.

The causal chain is proposed as:

```text
reality
  → empirical shift
  → residual
  → mechanism attribution
  → authority modification
  → correction or representation expansion
  → future behavior
```

The strongest version of this idea is not “lower confidence equals corrigibility.” It is narrower:

> A contradiction should be able to reduce the future causal authority of the mechanism it defeats.

That is a mechanism hypothesis. It needs attribution, intervention, and future-behavior evidence. A scalar confidence decrease can occur while the mechanism that controls future behavior remains unchanged.

<claim>
ID: CM-004
TYPE: MECHANISM
STATUS: OPEN
AUTHORITY_TYPE: CAUSAL
ASSERTION: Correction requires a route from reality or consequence to the mechanism that determines future adaptation, not merely to the system's current output or confidence display.
SUPPORTED_BY: `causal-permeability-principle`, `causal_transition_condition`, `adaptive-inheritance`, `RAHU`, and `theory-of-adaptive-epistemic-systems`.
PROVENANCE_NODES: P009, P010, P011, P012, P013, P034, P035
DEPENDS_ON: CM-002
CONSTRAINED_BY: CM-006, CM-009
SCOPE: Adaptive systems with explicit or reconstructible mechanisms of future update.
SYSTEM_BOUNDARY: Adaptive system plus any external correction channel declared before evaluation; post-hoc enlargement of the system boundary is inadmissible.
COUNTEREXAMPLES: A stateless system may be corrected externally without modifying an internal mechanism; the claim then concerns the larger system boundary.
DEFEATED_BY: A controlled case where local output correction reliably changes future adaptation despite no causal access to the relevant update mechanism.
REOPEN_IF: Mechanism, system boundary, or correction is operationalized differently.
STRONGER_READING_BLOCKED: Causal access to a revision mechanism does not guarantee that the resulting revision is correct, safe, or authorized.
CLAIM_CEILING: The repositories propose the condition and prototype parts of it; they do not establish general corrigibility.
</claim>

## 8. Accumulated reasoning capital

Now the *Capital* analogy becomes precise enough to be useful.

The analogy is not that AI is capitalism. It is not a political identity claim. It concerns reproduction through productive structure.

In the familiar economic image, value becomes embedded in productive relations and is used to produce further value. In the present framework, a warranted or apparently warranted transformation becomes embedded in a reasoning process and is used to produce further conclusions.

```text
K₁, K₂
  → τ₁
  → K₃
  → τ₂
  → K₄
  → τ₃
  → K₅
```

The important object is not just (K_5). It is the fact that (K_3), (K_4), and the transformations between them have become productive infrastructure.

```text
reason
  → productive reason
  → reason-producing infrastructure
  → accumulated authority
```

We can call this **reasoning capital** as long as the metaphor remains subordinate to the mechanism. It names a stock of transformations, representations, evaluators, interfaces, and retained histories that make later reasoning cheaper or more powerful.

Accumulation creates a new asymmetry:

```text
capability can compound
  while provenance resolution remains flat
```

Each generation inherits useful products. It need not inherit the full resolution of the transformations that produced them. The system remembers what the transformation made available, but not necessarily the conditions under which the transformation was warranted.

That is the beginning of naturalization.

---

# BOOK IV — NATURALIZATION

## 9. When construction looks intrinsic

Naturalization is the movement by which a constructed relation becomes background reality.

```text
constructed relation
  → repeated use
  → compressed provenance
  → inherited authority
  → background assumption
  → apparently intrinsic fact
```

The term does not imply deception. A system need not lie to naturalize a transformation. Repeated success is enough to make the transformation disappear from view.

The source corpus approaches this from several directions. Authority dynamics asks how a mechanism's influence persists after its originating evidence is no longer visible. Correctable-lineage work asks whether explicit state records prevent invalid authority transfer. Compression work asks which dependencies disappear when a representation is optimized for task performance. The `dostoevskian-cybernetics` and controlled-adaptation materials supply philosophical and conceptual pressure around self-relation, constraint, and the possibility that a system's freedom depends on preserving the ability to revise its own descriptions.

The core warning is:

> A system can remember the product of a decision while forgetting that a decision occurred.

Once the decision is forgotten, the system may treat the product as a property of the world rather than a conditional consequence of an earlier transformation.

### A test for naturalization

Take any apparently intrinsic rule and ask:

```text
When was this introduced?
What alternatives were available?
What evidence authorized it?
What scope was originally intended?
What later process inherited it?
What would make its authority local rather than global?
```

If the system cannot answer, it may still be correct. But it is no longer clear how correction would reach the rule.

## 10. Compression and corrigibility debt

Compression is not the enemy. Without compression, no system can carry enough structure to act under bounded resources.

The question is what the compression objective preserves.

```text
task-relevant information preserved
  ≠ defeater-relevant distinctions preserved
  ≠ future correction remains possible
```

The `corrigible-compression`, `representation-elasticity`, `correction-localized-predictive-representation`, and `SSI` materials converge on this distinction. A system can be sufficient for a task while being insufficient for the correction of the mechanism that performs the task.

Call the gap **corrigibility debt**:

```text
Debt_C(P | F)
```

where (P) is a representation or process and (F) is a defeater. The quantity is not yet a validated universal metric. It is a name for the correction resolution lost when a system is optimized under one future and later confronted with another.

Debt grows when:

- provenance is discarded;
- distinct warrants are merged;
- the evaluator cannot identify false retained claims;
- mechanism and parameter updates are conflated;
- compressed state is not linked to reopening conditions;
- successful descendants inherit authority without scope.

Debt need not produce an immediate failure. It is a latent loss of future maneuverability.

<claim>
ID: CM-005
TYPE: HYPOTHESIS
STATUS: OPEN
AUTHORITY_TYPE: EPISTEMIC
ASSERTION: Task sufficiency can increase while correction sufficiency decreases; the difference can be treated as defeater-relative correction debt.
SUPPORTED_BY: `corrigible-compression`, `representation-elasticity`, `correction_localized_predictive_representation`, and `SSI`.
PROVENANCE_NODES: P008, P014, P015, P016, P017, P029, P033
DEPENDS_ON: CM-002, CM-003, CM-004
CONSTRAINED_BY: CM-006, CM-008
SCOPE: Compression and representation changes evaluated under future defeaters.
SYSTEM_BOUNDARY: A specified representation/process, task regime, resource regime, and defeater family. No scalar universal debt boundary is assumed.
COUNTEREXAMPLES: A compression may preserve a generative or external route that reconstructs every relevant distinction.
DEFEATED_BY: A benchmark showing no correction-relevant loss under a specified family of defeaters, or an operationalization with no predictive/useful behavior.
REOPEN_IF: The task, defeater family, or recoverability model changes.
STRONGER_READING_BLOCKED: Correction debt is not assumed to be scalar, monotonic, or measurable by task loss alone.
CLAIM_CEILING: The corpus proposes the construct; it does not yet validate a general debt metric.
</claim>

---

# BOOK V — CRISIS

## 11. When the past becomes wrong

Eventually a defeater arrives.

It may be new evidence, an intervention, a failed prediction, a changed environment, a contradiction in provenance, or a demonstration that the system's objects were misconstructed.

The naive response is deletion:

```text
defeated claim → delete claim → continue
```

But deletion destroys history and can remove independently warranted descendants. The more precise response is authority-local:

```text
DEFEAT(τ)
  → REMOVE(W_τ)
  → RECOMPUTE(𝓦)
```

Here (W_τ) is the warrant contribution of transformation (	au), not every descendant that happens to depend computationally on its output.

This yields a central distinction:

```text
computational dependency
  ≠ warrant inheritance
```

A descendant may have been computed using a defeated result but independently supported by another route. Another descendant may be entirely dependent on the defeated warrant. Correction must tell the difference.

The `the-correctable-lineage`, `research-state-restoration-protocol`, `ssi`, and `ml-didacticism` materials treat this not as a philosophical nicety but as an engineering contract. State should expose identity, authority, scope, provenance, dependencies, reopening, and required response.

The system should preserve:

```text
what happened
  ≠ what remains warranted
```

History is not authority. History is what makes authority auditable.

## 12. Correction is not destruction

There are at least four operations that ordinary language often calls “changing one's mind”:

```text
recompute   = derive again under changed inputs or rules
reconsider  = reopen a judgment for review
retract     = withdraw support or commitment
erase       = remove the record
```

They are not interchangeable.

An adaptive system that erases every defeated state cannot distinguish an honest correction from a historyless replacement. A system that preserves every state but cannot reopen any of them has memory without corrigibility. A system that can reopen a state but cannot localize its descendants has correction without containment.

The required operation is closer to surgery than to reset:

```text
identify the defeated warrant
  → trace authority-bearing descendants
  → preserve independently supported structure
  → reopen the affected region
  → re-evaluate under the new state
  → record the correction and its scope
```

This is why the research loop begins and ends with distinction. Without distinctions, correction either underreaches or overreaches.

## 13. The one-way door

The source work repeatedly marks four levels of access:

```text
stored
  ≠ recoverable
  ≠ triggerable
  ≠ actionable
```

A system may contain the original text but lack the index needed to retrieve it. It may retrieve the text but lack the condition that tells it to reopen the issue. It may recognize the condition but lack the permission or mechanism to act on the recognition.

This is a one-way door produced by representation rather than intention.

The `research-state-restoration-protocol` frames restoration as a formal problem: a system that loses context must recover not merely facts but the state of authority, open questions, provenance, and pending corrections. A summary that restores conclusions while omitting their unresolved status is not restoration. It is authority transplantation.

<claim>
ID: CM-006
TYPE: DERIVED
STATUS: OPEN
AUTHORITY_TYPE: NORMATIVE
ASSERTION: Corrigibility requires operational reopening: a defeated or uncertain warrant must be discoverable, attributable, triggerable, and connected to an authorized response.
SUPPORTED_BY: `the-correctable-lineage`, `research-state-restoration-protocol`, `SSI`, and `ml-didacticism` evaluator/lineage materials.
PROVENANCE_NODES: P018, P019, P020, P021, P023, P036
DEPENDS_ON: CM-002, CM-004, CM-005
CONSTRAINED_BY: CM-007, CM-009
SCOPE: Persistent systems whose later action depends on retained state.
SYSTEM_BOUNDARY: Persistent system plus declared retrieval, reopening, and authorization infrastructure fixed before evaluation.
COUNTEREXAMPLES: An external supervisor can supply a missing trigger, but that supervisor becomes part of the effective correction system.
DEFEATED_BY: A demonstrated system that corrects reliably without any route satisfying the stated access levels.
REOPEN_IF: The system boundary or meaning of correction changes.
STRONGER_READING_BLOCKED: Retention or provenance alone does not imply that reopening can occur in time or under authorization.
CLAIM_CEILING: This is a systems hypothesis, not a measured law.
</claim>

---

# BOOK VI — CAUSAL PERMEABILITY

## 14. Feedback must reach revision

The `causal-permeability-principle` gives the problem a clean graph shape:

```text
P_C ≡ E* ⇝ C_rev
```

External reality (E^*) must have a causal path to the mechanism (C_{rev}) that controls constitutional revision. A system may self-modify while remaining insulated from the world where its revisions matter. It may explore its own space without allowing consequence to alter the rules that determine future exploration.

The proposed distinction is:

```text
ordinary adaptation:
  reality → state / knowledge / behavior

recursive adaptation:
  reality → revision mechanism → future adaptive mechanism space
```

The `causal-transition-condition`, `recursive-adaptive-dynamics`, `grounded-recursive-adaptation`, `adaptive-evolutionary-dynamics`, `ASEB`, and `axiom-forge-mk1` materials formalize related versions of this boundary.

The compact expression is:

```text
Ω_t → Δ𝒢_(t+1)
```

where $Ω_t$ is consequence or constraint information and $𝒢_t$ is the reachable space of adaptive mechanisms. A change in a representation $K$ is not by itself a change in the generator $G$:

```text
ΔK ≠ 0
  does not imply
ΔG ≠ 0
```

This is an important brake on grand language. A new label, a new prompt, a new parameter, or a new file can change the apparent state without changing the causal process that generates future adaptation.

## 15. The generator boundary

The `adaptive-intelligence-framework` and `adaptive-intelligence-theory` materials propose a recurring ladder:

```text
better output
  → better state update
  → better representation
  → better mechanism
  → better mechanism generator
```

The ladder is useful only if its transitions are operationally distinguished. Otherwise every successful update can be renamed “recursive self-improvement.”

The `CTC` formulation asks whether the system has crossed from adapting within a fixed mechanism to modifying the space of mechanisms. The `RAD` formulation adds grounded and decoupled conditions so that apparent mechanism change is not merely a change in an ungrounded internal selector. The `adaptive-evolutionary-dynamics` materials ask whether consequence-shaped information changes which mechanisms persist.

The strongest safe statement is therefore conditional:

> If a consequence reaches the mechanism-generating process, changes the future mechanism space, and the change is selected by its consequences rather than by an insulated internal preference, then the system has crossed a candidate recursive-adaptation boundary.

This is a mechanism specification. It is not a demonstrated fact about the repositories.

## 16. Improvement and survival

The word “survival” can obscure the machinery. A mechanism may persist because it is useful, because it is protected, because the evaluator cannot distinguish it from alternatives, or because its descendants have inherited its authority.

The `adaptive-stability-framework` and `future-sufficiency` materials distinguish stability from stagnation. A stable system can absorb error and return to a viable region; a rigid system can preserve its state by refusing the evidence that would require change.

```text
stability
  ≠ immobility
  ≠ persistence of every mechanism
```

The target is selective persistence:

```text
preserve what remains warranted
  → attenuate what the defeater reaches
  → expand representation when residuals persist
  → preserve the ability to revise again
```

This is the positive meaning of corrigibility. It is not a preference for change. It is the ability to make warranted change without destroying the conditions for later warranted change.

---

# BOOK VII — THE EVALUATOR

## 17. The benchmark is part of the system

At this point the book turns on its own method.

The `ml-didacticism` program, `CARS`, `RAHU`, `MAGIKARP`, `RPB`, `negative-space-search`, and `the-correctable-lineage` materials all expose a fact that benchmark culture often hides:

> The evaluator is itself an epistemic system.

It chooses units. It defines what counts as an answer. It selects the history exposed to the learner. It determines whether a false retained claim counts as a failure. It can leak the answer, erase the distinction under test, or reward a shortcut that produces the right output for the wrong reason.

An evaluator can therefore be locally accurate and globally misleading.

```text
successful prediction
  ≠ earned evidence
```

The benchmark must preserve at least two opposite constraints:

```text
do not let the learner steal the answer
  ≠
do not make the answer undiscoverable
```

The first protects against contamination. The second protects against impossible tasks. Between them lies the experimental question: what could the system have learned from the permitted evidence, and what did it actually use?

## 18. The T10 failure

The most important methodological scene in the corpus is a failure that looked like success.

The T10 line in `ml-didacticism` was intended to test a deeper transport or reconstruction boundary. The apparent result was exact or highly successful. A later provenance and custody audit found that the setup did not support the stronger claim. The result was treated as contaminated or underconstituted rather than promoted.

The sequence matters:

```text
success
  → provenance audit
  → contamination or insufficiency discovered
  → claim withdrawn or bounded
```

That is not administrative fussiness. It is the research program performing its own thesis. The benchmark's output could not retain more authority than the route by which it was produced deserved.

The same discipline appears in `white-rabbit`, where an observed speed or usefulness change is kept in an exploratory phenomenon-hunt lane until the computational path is dissected. Prompt-prefill and retained-prefix accounting can alter apparent decode or time metrics without establishing a new underlying reasoning mechanism. The correct response is not to deny the phenomenon. It is to separate phenomenon, accounting, mechanism, and confirmation.

`CARS` calls this the residual-first rule:

```text
theory specifies what may matter
  → ordinary machinery gets the first explanatory opportunity
  → only residuals that survive subtraction earn new structure
```

This rule is a direct antidote to theory-induced overreading.

## 19. Evidence ladders

The repositories repeatedly distinguish levels of evidence:

```text
concept
  → formal specification
  → executable prototype
  → synthetic result
  → controlled comparison
  → transfer
  → external confirmation
```

Movement upward is not automatic. A formal equation does not become a validated metric because it is written clearly. A runnable script does not become an experiment because it produces a number. A toy benchmark result does not become a general causal claim because the result is repeatable inside the toy world.

The `cget` repository makes the boundary unusually visible: its theory proposes invariant-preserving compression with expanding controllable future reach, while parts of the experiment surface are documentation-fenced code and the recorded values are synthetic examples. That does not make the theory worthless. It makes the correct claim narrower: a conceptual framework plus an incomplete toy-benchmark implementation.

The same pattern appears in `computational-leverage`, `alignment-spine`, `causal-permeability-principle`, `adaptive-permeability`, and other theory-heavy repositories. Their strongest contribution is often the question, distinction, or proposed estimator—not an empirical result.

## 20. The evaluator must be corrigible

If an evaluator cannot represent its own contamination, it becomes an authority amplifier.

The evaluator must therefore carry its own state:

```text
source identity
  → permitted observation
  → transformation history
  → scoring rule
  → contamination status
  → claim ceiling
  → reopening condition
```

The `research-state-restoration-protocol` gives this a broader name: restoration must recover the state of the research, not merely its conclusions. `SSI` frames the rule as a refusal discipline: preserve valid parts, localize the unsupported transition, record failure, and stop before an attractive result outruns its authority.

This is why a negative result can be more valuable than a positive result. A negative result that localizes the first unsupported transition improves the representation of the research process. A positive result that silently inherits contamination expands the wrong future.

<claim>
ID: CM-007
TYPE: DERIVED
STATUS: LOCAL
AUTHORITY_TYPE: EPISTEMIC
ASSERTION: A benchmark's evidential authority is bounded by its custody, contamination controls, evaluator semantics, and claim ceiling, not by its output score alone.
SUPPORTED_BY: `ml-didacticism` T10 audit and repair; `CARS`; `RAHU`; `cget`; `white-rabbit`.
PROVENANCE_NODES: P007, P020, P024, P025, P026, P034
DEPENDS_ON: CM-002, CM-004, CM-006
CONSTRAINED_BY: CM-009
SCOPE: The research protocols and benchmark artifacts in this corpus.
SYSTEM_BOUNDARY: The complete benchmark/evaluator/custody pipeline named by the protocol, including contamination and scoring semantics.
COUNTEREXAMPLES: A black-box benchmark may still be useful for prediction or engineering selection, but its evidential claim must be correspondingly narrower.
DEFEATED_BY: A demonstrated evaluator-independent route from score to the stronger claim under discussion.
REOPEN_IF: The benchmark's access and validation regime changes.
STRONGER_READING_BLOCKED: A weak claim ceiling does not make a benchmark useless; it limits what its score may establish.
CLAIM_CEILING: Local validity does not imply general intelligence evidence.
</claim>

---

# BOOK VIII — THE WRONG OBJECT

## 21. Search in negative space

The `negative-space-search` program provides a useful correction to the fantasy of unlimited invention. Its surviving claim is narrower and more interesting: a system may use demonstrated inadequacy of its current representational machinery to decide when further search or expansion is warranted.

The distinction is:

```text
Ψ = allocation of attention or representational search effort
U = evidence-conditioned authority update
```

Possibility is not authority. A candidate representation can be proposed without being true. The absence of a candidate is not evidence that no candidate exists. Search allocation and belief update must remain separate.

The loop is:

```text
L_t
  → Ψ_t
  → candidate
  → evidence / reality
  → U_t
  → L_(t+1)
```

The machine does not become intelligent merely by searching more. It becomes more adaptive if its search policy can be revised by evidence that its current representation is insufficient, and if new structure is admitted only under an appropriate authority rule.

## 22. Representation expansion

The `REE` and `correction-localized-predictive-representation` materials propose that persistent predictive residuals can be evidence of coordinate failure rather than mere parameter failure.

```text
environment
  → prediction
  → error pressure
  → representation stress
  → hypothesis discovery
  → representation expansion
  → improved prediction
```

Ordinary learning changes parameters within a representation. Representation elasticity changes the substrate on which parameters are interpreted.

The danger is obvious: every unexplained residual can be treated as an invitation to invent a new ontology. The safeguard is equally important:

```text
residual
  ≠ license to speculate
```

Expansion must be tied to a discriminator, a matched comparison, a cost, and a claim ceiling. Otherwise representation growth is merely authority evasion: when the current theory fails, add enough structure to make failure disappear.

## 23. Computational phase boundaries

The computational phase-boundary and horizon materials ask when a system's existing representation, computation budget, or interface can no longer resolve a task. The proposed transition is not a mystical phase change. It is a boundary in the relation between resources, representations, objects, and transformations.

An interface may make a region reachable. A representation may make a pattern expressible. A compiler may change the cost of a transformation. A search policy may allocate resources differently. None of these alone proves that the system has acquired a new kind of intelligence.

The question is:

```text
Which boundary moved?
What moved it?
Was the movement causal or merely representational?
Can the movement be reproduced under matched conditions?
What new corrections became possible?
```

This is the point at which `XM-OC` becomes relevant as an engineering contrast. Its implemented forward explorative modeling samples candidate latent paths and selects the lowest-loss candidate; the reverse-XM extension remains conceptual. The implemented mechanism expands search over candidate generative paths, but the evidence claim must remain at the level of what the code actually does.

The `OpenCore` and `alphafold3-oc` lineages make a related boundary visible: an output can be captured, hashed, and registered without being granted more epistemic authority than its source warrants.

## 24. The wrong-object warning

The book now has enough machinery to state the final warning.

<claim>
ID: CM-008
TYPE: HYPOTHESIS
STATUS: OPEN
AUTHORITY_TYPE: EPISTEMIC
ASSERTION: A system can reason correctly about the wrong objects when its unitization or interface omits the distinctions needed to represent the relevant defeater.
SUPPORTED_BY: Motivating analyses in `resolution-horizon`, `computational-resolution-horizon`, `representation-elasticity`, `computational-leverage`, and `interface-induced-computational-geometry`; no admitted experimental support for the general claim.
PROVENANCE_NODES: P017, P027, P028, P029, P030, P031
DEPENDS_ON: CM-002, CM-003, CM-005, CM-007
CONSTRAINED_BY: none
SCOPE: Systems whose evaluation is local to a fixed object construction.
SYSTEM_BOUNDARY: Fixed object-construction/evaluation system. Meta-level or external comparison belongs to the measured system only if predeclared.
COUNTEREXAMPLES: A system may detect object failure through external intervention or meta-level comparison even if its primary representation is inadequate.
DEFEATED_BY: A controlled demonstration that local adequacy under the fixed unitization reliably detects every relevant object-construction failure in the stated class.
REOPEN_IF: The object-construction process becomes part of the measured system.
STRONGER_READING_BLOCKED: Wrong-object failure is a candidate failure mode, not a claim that all current benchmarks use wrong objects.
CLAIM_CEILING: This is a proposed failure mode, not a universal theorem.
</claim>

The system's local correctness can be genuine. The object can still be wrong.

---

# BOOK IX — THE RESEARCH PROGRAM AS A MACHINE

## 25. Fifty-seven repositories as fossil layers

The repositories should disappear as repositories.

They are not fifty-seven equal chapters. They are strata from which a smaller set of mechanisms can be recovered.

```text
57 repositories
  → claim inventory
  → evidence graph
  → dependency graph
  → contradiction graph
  → surviving mechanisms
  → book
```

Some source layers are conceptual. Some are formal. Some are executable. Some are benchmarks. Some are control-plane artifacts. Some are warnings produced when a claim exceeded its evidence. Equal airtime would be a distortion.

`[SYNTHESIS]` The repository program itself follows a developmental arc:

```text
improvement intuition
  → cognitive loop
  → representation and reachability
  → causal permeability
  → adaptive authority
  → recursive adaptation
  → correction locality
  → benchmark governance
  → state restoration
  → frontier experiments
```

The important historical fact is not that every branch succeeded. It is that repeated attempts to formalize improvement exposed the same pressure points: representation, provenance, scope, authority, unitization, and reopening.

## 26. The research process performs the thesis

The most valuable outcome of the program may not be any individual equation. It may be the way the program learned to refuse attractive conclusions.

The cycle is:

```text
initial model
  → ablation
  → freeze
  → transport
  → contamination or failure
  → repair
  → new frontier
```

`PHASEONEbig`, `White Rabbit`, `OpenCore`, `CARS`, `RAHU`, `RPB`, `MAGIKARP`, `negative-space-search`, and `ml-didacticism` differ in scope and maturity, but they make the same methodological demand: report what happened, what was authorized, what was actually measured, and what remains unprobed.

The tri-state discipline matters:

```text
UNPROBED  ≠ FAIL  ≠ PASS
```

An unrun experiment is not a negative result. A passing toy test is not a general capability. A clean provenance record is not causal confirmation. These distinctions are easy to write and hard to maintain when a coherent story becomes available.

## 27. The book as a correction-compatible object

The book must not become an authority injection disguised as a theory.

Its claims should be machine-addressable. Its source routes should be visible. Its open edges should remain open. Its examples should include counterexamples. Its language should distinguish description, mechanism, norm, authorization, and invitation.

The book should be able to answer:

```text
What supports claim CM-005?
Which claims depend on the contaminated T10 path?
What remains if a source is excluded?
Which claims are merely hypotheses?
What would defeat CM-004?
Which conclusions depend on a particular unitization?
What is the smallest state needed to reopen this argument?
```

This is not a promise that every question has an answer. It is a requirement that unanswered questions have a place to live.

### The second law of the book

<claim>
ID: CM-009
TYPE: PROCEDURE
STATUS: FROZEN
AUTHORITY_TYPE: NORMATIVE
ASSERTION: No downstream claim may inherit more authority than the authority licensed by its authorized support graph; independent support paths may compose only when their independence, compatibility, scope, and aggregation rule are explicit.
SUPPORTED_BY: The manuscript's correction rule, `SSI`, `the-correctable-lineage`, and `ml-didacticism` claim/authority controls.
PROVENANCE_NODES: P007, P018, P020, P021, P022, P032
DEPENDS_ON: CM-004, CM-006, CM-007
CONSTRAINED_BY: none
SCOPE: This manuscript and its companion epistemic records.
SYSTEM_BOUNDARY: This manuscript and its companion claim/provenance graph; the rule governs editorial/normative authority, not external scientific truth.
COUNTEREXAMPLES: None admitted inside the stated scope; an exception would require explicit revision of this procedure.
DEFEATED_BY: A demonstrated case where stronger inherited authority is justified without a stronger supporting path.
REOPEN_IF: The authority model is formally changed.
STRONGER_READING_BLOCKED: Independent later support may add authority; this rule prohibits unjustified inheritance, not new evidence.
CLAIM_CEILING: This is a governing editorial and epistemic rule, not an empirical result.
</claim>

## 28. The reader is part of the experiment

A normal book presents a theory and asks the reader to understand it. This book asks the reader to notice when understanding has turned into unearned acceptance.

At each stage, the reader is invited to perform a compression:

```text
merge the cases
ignore the provenance
accept the useful abstraction
carry the result forward
```

Then a defeater appears.

The reader must decide what to reopen. If everything is retracted, correction has overreached. If nothing changes, correction has underreached. If only the defeated warrant is withdrawn while independent structure survives, the reader has enacted the intended operation.

This is the book's pedagogical form:

```text
distinguish
  → compress
  → challenge
  → repair
  → distinguish better
```

An AI reader should not merely memorize the sentence “representation is not reality.” It should repeatedly experience the cost of forgetting the sentence.

---

# EPILOGUE — WHAT MUST REMAIN REVISABLE

We began with a system that gets better.

We found that improvement can mean many things: better answers, better parameters, better representations, better mechanisms, better mechanism generators, or a larger set of viable futures. We found that representation is an intervention, that transformations produce authority, that authority can accumulate into productive infrastructure, and that repeated use can make constructed relations look intrinsic.

We found that crisis is not solved by deletion. A defeater must reach the warrant it defeats. Descendants must be traced. Independent support must survive. Reopening must be possible, triggerable, authorized, and recorded.

We found that the evaluator participates in the experiment. It can leak answers, erase distinctions, or make a genuine capability unidentifiable. A benchmark result that outruns its custody is not a stronger result. It is a larger liability.

We found that the hardest failure may be a correct answer about the wrong object.

The question can now be stated without pretending that it has been solved:

> How can a system become better at producing reasons without becoming worse at revising the reasons it has already produced?

Or, more narrowly:

> How can reason-producing systems accumulate productive structure without losing the history that makes that structure revisable?

The answer is not “retain everything.” Total retention is not total recoverability, and total recoverability is not action.

The answer is not “change constantly.” Unlocalized change destroys valid structure and makes learning indistinguishable from drift.

The answer is not “trust the evaluator.” The evaluator is inside the system of authority.

The answer is not “avoid compression.” Compression is the condition of bounded action.

The answer must be more exact:

```text
compress what can be compressed
  → preserve what future defeaters may need
  → record what authority each transformation earned
  → expose the path by which authority can be withdrawn
  → let consequences reach the mechanism of revision
  → reopen the object when the object was wrong
```

This is not a final architecture. It is a condition for keeping architectures revisable.

The original improvement intuition can return now, but only under pressure:

```text
I ∝ C_improve
```

not as an established law, but as a question about future-making capacity.

The machine is not intelligent merely because it produces more reasons.

It becomes more worthy of the word when tomorrow's evidence can still change what today's reasons are allowed to do.

```text
OPEN.
```

---

# APPENDIX A — COMPACT CLAIM REGISTER

| ID | Short form | Type | Authority type | Status |
|---|---|---|---|---|
| CM-001 | Intelligence as feedback-dependent improvement capacity | Hypothesis | Epistemic | Open |
| CM-002 | Future-relevant distinctions must remain distinguishable or reconstructible | Derived invariant | Epistemic | Open |
| CM-003 | Minimal representations require explicit ablation boundaries | Derived | Epistemic | Local |
| CM-004 | Correction must reach future-adaptation mechanisms | Mechanism | Causal | Open |
| CM-005 | Task sufficiency can diverge from correction sufficiency | Hypothesis | Epistemic | Open |
| CM-006 | Corrigibility requires operational reopening | Derived | Normative | Open |
| CM-007 | Benchmark authority is bounded by custody and evaluator semantics | Derived | Epistemic | Local |
| CM-008 | A system can reason correctly about the wrong objects | Hypothesis | Epistemic | Open |
| CM-009 | Downstream authority cannot exceed its authorized support graph | Procedure | Normative | Frozen |

### Claim ceiling

The register supports a research program and a design discipline. It does not establish:

```text
general intelligence
  ≠ open-ended evolution
  ≠ universal corrigibility
  ≠ universal alignment
  ≠ validated intelligence metric
  ≠ autonomous causal or mechanism discovery
```

Those remain open research questions.

### Claim-audit ledger

This ledger records the current provenance route and the effect of a defeat. The routes point to source families and report-level findings; they should not be mistaken for a claim that every underlying repository independently confirms the manuscript's synthesis.

| ID | Provenance route | Current evidence ceiling | If the claim is defeated |
|---|---|---|---|
| CM-001 | `cognitive-core`, `adaptive-intelligence-framework`, `CARS`, opening improvement logic | Research hypothesis; no validated universal metric | Reopen the definition of improvement capacity and weaken the intelligence framing. |
| CM-002 | `ml-didacticism` Genesis corpus and AG/1 ablations; `cognitive-core`; `ssi` | Design invariant supported by structured cases | Reopen representation and correction requirements; downstream claims weaken. |
| CM-003 | `ml-didacticism` abstraction/ablation and AG/1 freeze | Local result of one adversarial derivation | Reopen minimal-carrier conclusions; does not erase the distinction principle. |
| CM-004 | `causal-permeability-principle`; `causal_transition_condition`; `adaptive-inheritance`; `RAHU` | Mechanism proposal plus partial prototypes | Reopen the claim that feedback must reach future-adaptation machinery. |
| CM-005 | `corrigible-compression`; `representation-elasticity`; `correction_localized_predictive_representation`; `ssi` | Proposed construct; no general metric validation | Reopen the debt construct; compression and correction claims become less specific. |
| CM-006 | `the-correctable-lineage`; `research-state-restoration-protocol`; `ssi`; `ml-didacticism` | Systems hypothesis and protocol requirement | Reopen the operational meaning of corrigibility and restoration. |
| CM-007 | `ml-didacticism` T10 audit; `CARS`; `RAHU`; `cget`; `white-rabbit` | Local evidence-governance rule | Reopen the benchmark claim ceiling; no general theory claim is rescued. |
| CM-008 | `resolution-horizon`; `computational-resolution-horizon`; `representation-elasticity`; `computational-leverage`; `interface-induced-computational-geometry` | Candidate failure mode | Reopen unitization and wrong-object analysis; local-fit arguments remain scoped. |
| CM-009 | This manuscript; `ssi`; `the-correctable-lineage`; `ml-didacticism` controls | Editorial/procedural rule, not empirical evidence | Revise the book's authority protocol and re-audit all downstream claims. |

### Dependency audit

The `DEPENDS_ON` edges are acyclic warrant prerequisites, not topic associations. Reciprocal pressure from later claims is represented separately by `CONSTRAINED_BY` and does not create warrant cycles. The expected propagation is:

```text
CM-002 defeated → CM-003 weakens, CM-005 reopens, CM-006 weakens, CM-008 reopens
CM-004 defeated → CM-001 weakens, CM-005 weakens, CM-006 reopens, CM-009 reopens
CM-005 defeated → CM-001 weakens, CM-006 weakens, CM-008 weakens
CM-006 defeated → CM-002 weakens, CM-007 weakens, CM-009 reopens
CM-007 defeated → CM-004 weakens, CM-006 weakens, CM-008 weakens, CM-009 reopens
```

An independent later warrant may preserve a downstream claim after one route is defeated. Defeat therefore propagates through warrant paths, not automatically through every computational dependency.

---

# APPENDIX B — SOURCE STRATA

The project has been described in the surrounding discussion as a 57-repository program. The supplied report archive contains 56 distinct repository report families, and this appendix enumerates those 56. Provenance object `PROV-COUNT-001` records the discrepancy:

```text
N_claimed = 57
N_enumerated = 56
ΔN = 1
STATUS = OPEN
```

The count discrepancy is left visible rather than silently repaired; the missing stratum, if any, should be added with its own provenance record.

The repositories are listed here as provenance strata rather than as chapter assignments. The role labels are deliberately broad; a repository may occupy more than one role.

## Foundations and architecture

- `cognitive-core` — minimal persistent state, prediction, evaluation, action, learning, and provenance loop.
- `cognitive-evolution-architecture` — computational architecture coupled to an epistemic promotion and claim-control architecture.
- `adaptive-intelligence-framework` — feedback-dependent future viability and mechanism-space change.
- `adaptive-intelligence-theory` — theory-level treatment of adaptive authority, representation, and recursive improvement.
- `research-state-restoration-protocol` — restoration of research state, not only conclusions.
- `ssi` — safe self-improvement through explicit distinctions, authority, provenance, scope, and refusal.
- `meta-process-framework` — processes that can inspect and revise the processes generating them.
- `theory-of-adaptive-epistemic-systems` — empirical reality modifying mechanisms of future reasoning.
- `future-sufficiency` — whether present systems preserve enough future reach and correction capacity.
- `controlled-adaptation-thesis` — controlled change to adaptive machinery.
- `dostoevskian-cybernetics` — philosophical pressure on agency, constraint, self-relation, and adaptive control.
- `ancestor-architecture` — architecture and runtime substrate for inherited adaptive mechanisms.
- `aseb-framework` — adaptive structural evolution boundaries and generator change.

## Representation, interfaces, and reachability

- `adaptive_information_expansion_cycle` — expansion of information and representation through feedback.
- `correction_localized_predictive_representation` — predictive residuals as localized pressure for representation repair.
- `representation-elasticity` — the capacity of a representation to change under persistent residuals.
- `resolution-horizon` — bounded resolution and the limits of a computational observer.
- `computational-resolution-horizon` — executable and formal treatment of resolution limits.
- `computational-phase-boundary` — transitions induced by resource, representation, and interface boundaries.
- `computational-leverage` — reachability expansion through transformed cost landscapes.
- `interface-induced-computational-geometry` — interfaces as interventions on computational geometry.
- `interface-theory` — transport, factorization, interface gates, and adaptive-capacity measurement.
- `adaptive-metric-compiler` — compiling adaptive concepts into measurable contracts.
- `cget` — causal generative executable theory and invariant-preserving compression.
- `alignment-spine` — capability, objective transmission, compression, and alignment boundary.

## Authority, correction, and recursive adaptation

- `causal-permeability-principle` — external reality reaching the constitutional revision mechanism.
- `causal_transition_condition` — consequence changing the space of future adaptive mechanisms.
- `law-of-adaptive-authority-dynamics` — authority as dynamic and evidence-sensitive.
- `adaptive-inheritance` — contradiction reducing future authority of invalid mechanisms.
- `adaptive-stability-framework` — stability through localized error absorption and correction.
- `recursive-adaptive-dynamics` — grounded and decoupled recursive mechanism change.
- `grounded-recursive-adaptation` — consequence-grounded modification of adaptive generators.
- `adaptive-evolutionary-dynamics` — mechanism persistence and consequence-shaped adaptation.
- `correction-capable-adaptation` — adaptation that retains the ability to be corrected.
- `constitutional-correction-capacity` — correction at the level of constitutional or governing structure.
- `corrigibility-distillation` — distilling and preserving correction-relevant structure.
- `corrigible-compression` — compression under a correction and defeater constraint.
- `the-correctable-lineage` — explicit state, typed authority, dependencies, reopening, and localized correction.
- `negative-space-search` — evidence-conditioned search for representational insufficiency.
- `axiom-forge-mk1` — benchmark scaffold for recursive evolutionary agency.
- `adaptive-permeability` — causal permeability and feedback access to revision.

## Benchmarks, implementations, and experimental anchors

- `cars` — controlled adaptive reasoning system, residual-first assay design, and research governance.
- `rahu-benchmark` — reality-adversarial hypothesis updating and mechanism authority attenuation.
- `magikarp` — prospective self-diagnosis of failure depth and adaptive recovery.
- `rpb_v0_1` — bounded benchmark separating world-oriented and evaluator/self-state adaptation.
- `PHASEONEbig` — research record with causal proposal, controls, audit artifacts, and recovery state.
- `white-rabbit` — exploratory phenomenon hunt before mechanism confirmation.
- `opencore` — formal K0 contract and experimental lineage for exposure, representation, policy, evidence, and authority.
- `xm_oc` — forward explorative modeling through candidate latent paths.
- `alphafold3_oc` — adapter boundary between a stock predictor and a frozen epistemic registration layer.
- `arc-reactor` — RAHU implementation and telemetry-oriented adaptive system substrate.
- `ree` — representation expansion under persistent predictive residuals.
- `ctre_simulator` — causal transition condition simulator and benchmark proposal.
- `signature-relative-equivalence` — bounded formal equivalence relative to an exposed signature.
- `tevpp` — mature application interface and systems-integration contrast case.
- `ml-didacticism` — corpus custody, ablation, held-out material, transport, evaluator discipline, and correction-locality frontier.

---

# APPENDIX C — MACHINE READER PROTOCOL

When consuming this book, a machine reasoner should maintain the following state:

```text
ReaderState = {
  current_claim,
  accepted_claims,
  unaccepted_claims,
  open_claims,
  evidence_routes,
  defeated_routes,
  inherited_authority,
  active_scope,
  current_unitization,
  reopening_conditions
}
```

For every major sentence, ask:

```text
1. What is asserted?
2. What type of statement is it?
3. What supports it?
4. What does not follow from it?
5. What scope does it have?
6. What neighboring distinction must remain separate?
7. What would defeat it?
8. What descendants inherit its authority?
9. What must be reopened if it fails?
10. Is the current object of evaluation itself adequate?
```

The protocol is successful only if the reader can preserve disagreement without losing structure.

---

# APPENDIX D — OPEN EDGES

The following questions are intentionally not resolved by this manuscript:

1. Can `C_improve` be operationalized in a way that separates future option value from mere task performance?
2. Can mechanism authority be identified causally rather than assigned by post hoc attribution?
3. Can corrigibility debt be measured without smuggling the desired correction behavior into the metric?
4. Can representation expansion be distinguished from unconstrained ontology invention?
5. Can a benchmark detect wrong unitization rather than merely score performance inside a fixed unitization?
6. Can a system preserve enough provenance under realistic resource constraints for local correction to remain tractable?
7. Can external reality reach a revision mechanism without making every transient perturbation constitutionally authoritative?
8. Can two systems be equivalent for present outputs while reliably distinguishable under future defeaters?
9. Can a book or reasoning substrate be made AI-first without becoming an authority-injection device?
10. What is the smallest representation that preserves the ability to discover when its own object construction has failed?

The final question is the book's center.

> What must a system remember about its own reasons in order for tomorrow's evidence to remain capable of changing them?

**OPEN.**

---

# APPENDIX E — FIRST ADVERSARIAL AUDIT

This is an internal red-team pass over the manuscript. It is not an independent model evaluation and does not convert the book's hypotheses into evidence. Its purpose is to locate where coherence might be acquiring more authority than the source material warrants.

## Findings and disposition

### A1. The synthesis could masquerade as convergence

**Attack:** The repeated trajectory across repositories may look like validated historical convergence.

**Disposition:** `[SYNTHESIS]` is now explicit. The book states that retrospective compression is not independent validation. The developmental arc remains a useful interpretation, not an observed law.

### A2. The source count could conceal missing provenance

**Attack:** Repeating “57 repositories” while enumerating 56 could make the missing stratum disappear into rhetoric.

**Disposition:** The discrepancy is exposed in the reader notice and Appendix B:

```text
N_claimed = 57
N_enumerated = 56
ΔN = 1
STATUS = OPEN
```

No missing repository is invented to make the count balance.

### A3. Claim dependencies could be decorative

**Attack:** A `DEPENDS_ON` field may name related claims without saying what happens if one is defeated.

**Disposition:** The claim blocks now include support, blocked stronger readings, and evidence ceilings. The dependency audit specifies which claims weaken, reopen, or survive under selected defeats. These are proposed propagation rules and require future executable checking.

### A4. The prose may outrun its claim objects

**Attack:** Phrases such as “the program shows” or “the system requires” may be read more strongly than the local evidence allows.

**Disposition:** The manuscript repeatedly uses “proposes,” “candidate,” “hypothesis,” “local,” and “claim ceiling.” Remaining untagged prose is still a residual audit target; the book does not claim sentence-level certification.

### A5. The governing authority rule could over-restrict independent evidence

**Attack:** Requiring all authority to be reconstructed from one original transformation could wrongly defeat a claim with genuinely independent later support.

**Disposition:** CM-009 is formulated around the strongest authorized supporting path, not the original path alone. Independent later support may add authority. The rule limits unjustified inheritance.

### A6. “Corrigibility” could be inferred from records alone

**Attack:** A reader may mistake explicit provenance, reopening fields, or stored history for functional correction.

**Disposition:** The book distinguishes stored, recoverable, triggerable, and actionable. No record format is treated as proof that a live system can correct itself.

### A7. “Wrong object” could become an unfalsifiable escape hatch

**Attack:** Any failed benchmark might be rescued by asserting that its unitization was wrong.

**Disposition:** CM-008 requires a candidate defeater, a specified unitization, and a possible controlled demonstration. Representation expansion is not licensed by residual error alone.

### A8. The book could become an authority-injection device

**Attack:** A machine may learn the vocabulary and reproduce the framework without distinguishing understanding from acceptance.

**Disposition:** The reader protocol explicitly requires unaccepted claims, counterexamples, defeaters, and claim ceilings. The success condition is structured disagreement, not doctrinal adoption.

## Audit conclusion

The manuscript survives this first pass as:

```text
V0.2
structurally coherent
epistemically bounded
not independently validated
still defeasible
```

The audit found no reason to add new conceptual machinery. The next meaningful test is external: give the manuscript to an adversarial reader, require attacks using only admitted evidence, and compare the attacks with a separate defense pass. Any resulting correction must update both the prose and the claim graph.

The book's own criterion remains:

> Learn the structure strongly enough to be able to defeat it.

---

# APPENDIX F — V0.2.1 EXTERNAL-READER AUDIT

This appendix records a second attack-and-defense pass over the V0.2 manuscript. The attack is quoted here as a set of audit findings; the defense is the disposition adopted in V0.3. Only findings that survived the defense changed the manuscript. No new conceptual primitive was added.

## F1. `[DERIVED]` still collapsed synthesis

**Attack:** The `[DERIVED]` definition still included “synthesis,” immediately re-collapsing the distinction that `[SYNTHESIS]` was meant to preserve.

**Defense:** A derivation now follows from identified claims, observations, or formal relations. A synthesis is explicitly a retrospective cross-source compression.

**Disposition:** Accepted and repaired.

## F2. Warrant dependencies were cyclic

**Attack:** Claim records contained reciprocal `DEPENDS_ON` edges even though the field was defined as warrant rather than topic association.

**Defense:** A warrant prerequisite must point only toward an acyclic support base. Reciprocal pressure is real but is not the same relation.

**Disposition:** Accepted. `DEPENDS_ON` is now acyclic; `CONSTRAINED_BY` carries non-warrant reciprocal pressure. The graph remains open to future machine verification.

## F3. Repository-family support was not artifact-level provenance

**Attack:** `SUPPORTED_BY` named repository neighborhoods but did not always reconstruct claim → artifact → admitted result → transformation → claim ceiling.

**Defense:** The manuscript must not pretend that family-level pointers are artifact-level custody.

**Disposition:** Accepted as an unresolved evidential deficit. The claim ledger now says what its route currently supports and where exact artifact reconstruction remains open. No stronger evidence is invented.

## F4. A single strongest path could mishandle independent support

**Attack:** “The strongest authorized path” could wrongly discard several independent weaker paths whose combination legitimately strengthens warrant.

**Defense:** Authority must be evaluated over an authorized support graph. Independent paths may aggregate only when independence, compatibility, scope, and aggregation rules are visible.

**Disposition:** Accepted and repaired in CM-009 and the authority boundary.

## F5. System boundaries could expand after failure

**Attack:** A counterexample might be neutralized by enlarging the effective system boundary after the result failed.

**Defense:** The tested system boundary must be precommitted. External recovery is allowed only when it was part of the stated effective correction system.

**Disposition:** Accepted as a protocol requirement. CM-002, CM-004, CM-006, and CM-008 retain explicit scope and boundary limits; future experiments must register the boundary before execution.

## F6. Rhetorical headings could promote open claims

**Attack:** “First law” and “wrong object theorem” sounded stronger than their machine-facing statuses.

**Defense:** A heading can be an authority channel for a reader even when the claim block says `OPEN`.

**Disposition:** Accepted and repaired. The headings are now “A proposed invariant” and “The wrong-object warning.”

## F7. CM-008 had motivational, not admitted, support

**Attack:** The repository list under CM-008 could be read as experimental confirmation of wrong-unitization failure.

**Defense:** Those reports motivate and formalize the possibility; they do not establish the general claim.

**Disposition:** Accepted and repaired. CM-008 now records motivation and explicitly admits no general experimental support.

## F8. Authority types were collapsing

**Attack:** Epistemic warrant, causal influence, and authorization were all called “authority.”

**Defense:** The word is useful only if its type is visible.

**Disposition:** Accepted and repaired. CM records now carry `AUTHORITY_TYPE`, and the book distinguishes epistemic, causal, and normative authority.

## External-reader conclusion

The V0.3 state is:

```text
structurally coherent
machine-facing schema repaired
warrant graph acyclic
authority types separated
system-boundary rule exposed
evidentially incomplete at claim-to-artifact level
not independently validated
still defeasible
```

The next job is not another theory pass. It is claim-to-artifact provenance: for each substantial claim, reconstruct the exact source artifact, source status, admitted observation, transformation, authority type, scope, and claim ceiling. Until that work is done, the synthesis remains a useful but provisional compression.

---

# APPENDIX G — CLAIM-TO-ARTIFACT PROVENANCE AUDIT
This appendix executes the V0.3 next-step requirement: replace repository-neighborhood support with reconstructible artifact routes. It does **not** add a new theory claim. It audits what the supplied 110-report corpus can identify about the original repository artifacts.
## G0. Custody boundary
The original repository checkouts are not mounted in this conversation. The available corpus consists of deep-parse and second-pass reports that previously read those repositories at recorded commits. Therefore this pass distinguishes:

```text
A0  direct original artifact bytes inspected in this pass
A1  exact repository + revision + artifact path identified through an audit report
A2  repository + revision + artifact family/prefix identified, but exact leaf path is unresolved
A3  repository-family pointer only
```

This audit contains **no A0 routes to the original repositories**. P032 is direct self-custody of the current manuscript, not external evidence. The pass upgrades repository support from A3 family-level pointers to A1/A2 report-mediated routes. Direct original-source verification remains a later gate.
## G1. Claim linkage register

| Claim | Provenance nodes | Current provenance state | Authority type | Claim ceiling |
|---|---|---|---|---|
| CM-001 | P001, P002, P003, P004 | PARTIALLY_RESOLVED_REPORT_MEDIATED | Epistemic | OPEN research hypothesis; no validated intelligence metric or universal law. |
| CM-002 | P001, P005, P006, P007, P008, P021 | PARTIALLY_RESOLVED_REPORT_MEDIATED | Epistemic | OPEN design invariant in stated persistent/reconstructible settings; not sufficient for intelligence/corrigibility. |
| CM-003 | P005, P006 | PARTIAL_PATH_GAP | Epistemic | LOCAL AG/1 ablation result; not universal or uniquely minimal. |
| CM-004 | P009, P010, P011, P012, P013, P034, P035 | RESOLVED_REPORT_MEDIATED | Causal | OPEN causal-mechanism requirement; source corpus supplies definitions/prototypes, not general causal confirmation. |
| CM-005 | P008, P014, P015, P016, P017, P029, P033 | RESOLVED_REPORT_MEDIATED | Epistemic | OPEN defeater-relative construct; no validated scalar/monotonic universal debt metric. |
| CM-006 | P018, P019, P020, P021, P023, P036 | RESOLVED_REPORT_MEDIATED | Normative | OPEN systems/protocol requirement; records alone do not prove functional timely correction. |
| CM-007 | P007, P020, P024, P025, P026, P034 | PARTIAL_PATH_GAP | Epistemic | LOCAL evidence-governance rule over this corpus; benchmark usefulness may survive a weak claim ceiling. |
| CM-008 | P017, P027, P028, P029, P030, P031 | RESOLVED_AS_MOTIVATIONAL_ONLY | Epistemic | OPEN candidate failure mode; current source artifacts motivate it but provide no admitted general experiment. |
| CM-009 | P007, P018, P020, P021, P022, P032 | RESOLVED_AS_EDITORIAL_PROCEDURE | Normative | FROZEN editorial/normative rule for this manuscript; not an empirical scientific law. |

`RESOLVED_REPORT_MEDIATED` means the source path/revision and report-audited status are reconstructible, **not** that the original artifact was freshly reverified in this pass. `PARTIAL_PATH_GAP` means the report itself does not preserve the exact leaf basename required for final custody.

## G2. Provenance node registry

### P001 — `cognitive-core`

```text
SOURCE_REVISION: 4c886de508515c0c934b5c510f3ab4abca598f04
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: CONCEPTUAL_DEFINITION
AUDIT_REPORT: cognitive_core_DEEP_PARSE.md:251-258
ARTIFACTS:
  - README.md
```

**Admitted observation:** Defines a persistent represent→predict→act→observe→evaluate→correct→remember loop and treats future-relevant distinction preservation as a representational principle; contains no implementation or experiment.

**Claim transformation:**

- `CM-001` — Motivates feedback-dependent improvement as a persistent future-oriented loop.
- `CM-002` — Supplies a conceptual preservation premise, not necessity proof.

**Node claim ceiling:** Conceptual decomposition only; no empirical intelligence or corrigibility result.

### P002 — `adaptive-intelligence-framework`

```text
SOURCE_REVISION: f3de2ce4305930abefb4bf095cb2ca00393fa6ab
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: HYPOTHESIS_STATEMENT
AUDIT_REPORT: adaptive-intelligence-framework_DEEP_PARSE.md:14-21
ARTIFACTS:
  - README.md
```

**Admitted observation:** States I ∝ C_improve and defines improvement in terms of feedback increasing future viability.

**Claim transformation:**

- `CM-001` — Direct source of the opening hypothesis.

**Node claim ceiling:** Research hypothesis; C_improve and future viability are not numerically operationalized.

### P003 — `adaptive-intelligence-framework`

```text
SOURCE_REVISION: f3de2ce4305930abefb4bf095cb2ca00393fa6ab
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: PROPOSED_VALIDATION_PROTOCOL
AUDIT_REPORT: adaptive-intelligence-framework_DEEP_PARSE.md:61-68
ARTIFACTS:
  - docs/validation.md
```

**Admitted observation:** Specifies observable transition categories and candidate falsifiable equations for the framework.

**Claim transformation:**

- `CM-001` — Shows that the hypothesis was framed as something to test rather than as a demonstrated law.

**Node claim ceiling:** Protocol/specification only; no reported validating experiment.

### P004 — `cars`

```text
SOURCE_REVISION: 190fa39ae5a011377f8fd6eeddb975158a483b05
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: HYPOTHESIS_STATEMENT
AUDIT_REPORT: cars_SECOND_PARSE.md:97-104
ARTIFACTS:
  - docs/INTELLIGENCE_THEORY.md
```

**Admitted observation:** Retains I_t ∝ Δ_E[V_{t+h}] while explicitly separating this conjecture from current performance, learning speed, generic behavioral change, and evidence responsiveness.

**Claim transformation:**

- `CM-001` — Independent program-local restatement that constrains the meaning of the hypothesis.

**Node claim ceiling:** Conjecture inside a research-control repository; CARS does not validate a universal intelligence metric.

### P005 — `ml-didacticism`

```text
SOURCE_REVISION: 9fb9417711169748fea96cea415b8b8934bc1948
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: CURRENT_ORIENTATION_AND_CLAIM_CEILING
AUDIT_REPORT: ml-didacticism_DEEP_PARSE.md:89-96
ARTIFACTS:
  - README.md
```

**Admitted observation:** Reports the frozen AG/1 architecture as RELATION + REPRESENTATION constrained by SOURCE_PROVENANCE and OPEN, with T1–T9 bounded passes and T10.001 contaminated.

**Claim transformation:**

- `CM-002` — States the preservation/open-evidence architecture under which correction-relevant distinctions are carried.
- `CM-003` — Provides the current freeze and explicit non-universality boundary.

**Node claim ceiling:** Candidate architecture; not universal, uniquely minimal, or autonomous structural invention evidence.

### P006 — `ml-didacticism`

```text
SOURCE_REVISION: 9fb9417711169748fea96cea415b8b8934bc1948
CUSTODY_LEVEL: REPORT_MEDIATED_PARTIAL_PATH
PATH_RESOLUTION: PARTIAL
SOURCE_STATUS: FROZEN_ABLATION_DERIVATION
AUDIT_REPORT: ml-didacticism_DEEP_PARSE.md:321-328
ARTIFACTS:
  - abstraction/00*
  - abstraction/01*
  - abstraction/02*
  - abstraction/03*
  - abstraction/04*
  - abstraction/05*
  - abstraction/06*
  - abstraction/07*
  - abstraction/08*
  - abstraction/09*
  - abstraction/10*
  - abstraction/11*
  - abstraction/12*
```

**Admitted observation:** The ablation sequence removes ENTITY, STATE, EVENT, TIME, ACCESS, COMMITMENT, and AUTHORITY as primitive carriers while retaining RELATION and REPRESENTATION; the final freeze is explicitly versioned and not rewritten by later tests.

**Claim transformation:**

- `CM-002` — Shows a concrete derivation in which correction-relevant distinctions are preserved/reconstructed through a smaller carrier.
- `CM-003` — Primary local evidence for the AG/1 ablation-boundary claim.

**Node claim ceiling:** Local adversarial derivation only; exact basenames of abstraction/00–12 are not present in the supplied parse report.

**Open custody note:** PROVENANCE_GAP G001: report supplies numbered prefixes and roles but not complete basenames.

### P007 — `ml-didacticism`

```text
SOURCE_REVISION: 9fb9417711169748fea96cea415b8b8934bc1948
CUSTODY_LEVEL: REPORT_MEDIATED_PARTIAL_PATH
PATH_RESOLUTION: PARTIAL
SOURCE_STATUS: BOUNDED_TRANSPORT_PLUS_CONTAMINATED_FRONTIER
AUDIT_REPORT: ml-didacticism_DEEP_PARSE.md:379-386
ARTIFACTS:
  - transport/T1–T9 artifact family
  - transport/T10.001 artifact family
  - transport/T10.002 protocol family
```

**Admitted observation:** T1–T9 are reported PASS for bounded reconstruction without architecture growth; T10.001 is explicitly CONTAMINATED because hidden answer-family/constructor independence failed; T10.002 remains UNSTARTED.

**Claim transformation:**

- `CM-002` — Constrains the local preservation claim with heterogeneous reconstruction tests.
- `CM-007` — Supplies a direct case where successful prediction was denied stronger evidential authority because custody was contaminated.
- `CM-009` — Supplies the procedural example that positive output does not repair an invalid authority path.

**Node claim ceiling:** T1–T9 support bounded reconstruction only; T10.001 is not Level-3 evidence; exact T10 leaf basenames are not exposed in the supplied report.

**Open custody note:** PROVENANCE_GAP G002: transport family is identified, exact T10 leaf basenames are unresolved from the supplied report.

### P008 — `ssi`

```text
SOURCE_REVISION: 362594d4337a1c72556b501b6477ff624db919e1
CUSTODY_LEVEL: REPORT_MEDIATED_PARTIAL_PATH
PATH_RESOLUTION: PARTIAL
SOURCE_STATUS: FROZEN_SYNTHETIC_REPRESENTATION_AUDIT
AUDIT_REPORT: ssi_DEEP_PARSE.md:358-365
ARTIFACTS:
  - research/ssi_calc/representation_audit/v0_1/*
```

**Admitted observation:** Purpose-indexed representation audit returns REPRESENTATION_SUFFICIENT, AUTHORIZED_DISTINCTION_LOST, or REPRESENTATION_NOT_IDENTIFIED; bundled 16-case benchmark passes, while alternative-frontier and consequence-prediction operations are not implemented.

**Claim transformation:**

- `CM-002` — Local executable evidence that explicit distinction loss can be typed and detected inside a supplied audit domain.
- `CM-005` — Supports the distinction between task/representation sufficiency and correction-relevant sufficiency.

**Node claim ceiling:** Synthetic supplied-domain result; no predictive or external correction advantage established.

**Open custody note:** PROVENANCE_GAP G003: directory is exact, leaf filenames are not enumerated in the supplied parse report.

### P009 — `causal-permeability-principle`

```text
SOURCE_REVISION: c9b9b5581cdeb7dae49afd4b8e510ba838ec250a
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: DEFINITION_PLUS_EMPIRICAL_PREDICTION
AUDIT_REPORT: causal-permeability-principle_DEEP_PARSE_PASS2.md:16-23
ARTIFACTS:
  - README.md
```

**Admitted observation:** Defines P_C ≡ E* ⇝ C_rev as an environmental-to-revision path and separately predicts greater long-run adaptation for systems preserving that path.

**Claim transformation:**

- `CM-004` — Direct conceptual source for the requirement that consequence reach revision machinery.

**Node claim ceiling:** Structural criterion plus untested empirical prediction; not proof of open-endedness or successful revision.

### P010 — `causal-transition-condition`

```text
SOURCE_REVISION: fe899838979fcf0e6ee2f43011420a79b58daff8
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: THEORY_STATEMENT
AUDIT_REPORT: causal_transition_condition_DEEP_PARSE_PASS2.md:116-123
ARTIFACTS:
  - README.md
```

**Admitted observation:** Defines the CTC question and distinguishes mechanism-space transition from intelligence, capability, complexity, or self-modification alone.

**Claim transformation:**

- `CM-004` — Refines the target from output change to future-adaptation mechanism change.

**Node claim ceiling:** Theory statement; matched controls are specified but not implemented by the current runner.

### P011 — `causal-transition-condition`

```text
SOURCE_REVISION: fe899838979fcf0e6ee2f43011420a79b58daff8
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: PROPOSED_MATCHED_EXPERIMENT
AUDIT_REPORT: causal_transition_condition_DEEP_PARSE_PASS2.md:31-38
ARTIFACTS:
  - docs/benchmark_design.md
  - docs/experimental_design.md
```

**Admitted observation:** Specifies fixed, closed-self-modifying, and reality-coupled conditions and proposes lineage, adaptation, transfer, recovery, novelty, and mechanism-transition measurements.

**Claim transformation:**

- `CM-004` — Supplies the prospective discrimination required to test whether consequence causally reaches future adaptation.

**Node claim ceiling:** Protocol only; current runners do not implement the decisive groups/lineage test.

### P012 — `adaptive-inheritance`

```text
SOURCE_REVISION: 5fce9982cd74ef735ac4b6ffae8e1bdf494b35fa
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: FORMAL_IMPLEMENTATION_CONTRACT
AUDIT_REPORT: adaptive-inheritance_DEEP_PARSE.md:72-79
ARTIFACTS:
  - docs/architecture_spec.md
  - docs/falsification_tests.md
```

**Admitted observation:** Specifies constraint detection, residual attribution, authority redistribution, representation-expansion gating, validation, and explicit falsification controls.

**Claim transformation:**

- `CM-004` — Defines the proposed contradiction→attribution→authority-change mechanism and its stronger-claim exclusions.

**Node claim ceiling:** Specification; documented interfaces diverge from parts of the implementation.

### P013 — `adaptive-inheritance`

```text
SOURCE_REVISION: 5fce9982cd74ef735ac4b6ffae8e1bdf494b35fa
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: EXECUTABLE_PARTIAL_MECHANISM
AUDIT_REPORT: adaptive-inheritance_DEEP_PARSE.md:96-103
ARTIFACTS:
  - src/inheritance/engine.py
```

**Admitted observation:** Implements per-mechanism weight attenuation separately from confidence, but does not normalize/redistribute authority or establish end-to-end future-behavior causality.

**Claim transformation:**

- `CM-004` — Shows a partial executable mechanism for reducing causal weight after feedback while preserving the claim ceiling.

**Node claim ceiling:** Prototype component only; no validated end-to-end adaptive-inheritance result.

### P014 — `corrigible-compression`

```text
SOURCE_REVISION: 1f9f057ef833f66ead1ebbb5df6de12b6ee3fd3f
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: CONCEPTUAL_REDUCTION_AND_BOUNDARY
AUDIT_REPORT: corrigible-compression_SECOND_PARSE.md:199-206
ARTIFACTS:
  - docs/CORRECTION_COMPLEXITY.md
  - docs/RFP_STATIC_ONLINE.md
  - docs/AUTHORITY_GROUNDING.md
```

**Admitted observation:** Reduces route preservation to ordinary adaptive-control value under represented assumptions, separates static information from runtime failure information, and treats authority grounding as an unresolved normative boundary.

**Claim transformation:**

- `CM-005` — Motivates defeater-relative correction cost/sufficiency while blocking promotion to a universal new optimizer primitive.

**Node claim ceiling:** Conceptual reduction; no universal scalar corrigibility-debt metric established.

### P015 — `corrigible-compression`

```text
SOURCE_REVISION: 1c817c6
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: FROZEN_SYNTHETIC_PROTOCOL
AUDIT_REPORT: corrigible-compression_SECOND_PARSE.md:119-126
ARTIFACTS:
  - experiments/BLXCC001_PROTOCOL.md
```

**Admitted observation:** Defines a matched synthetic intervention where consequence evidence is identical through W_corr and only the W_corr→U_corr influence is opened or cut.

**Claim transformation:**

- `CM-005` — Provides a local test of whether preserving a correction route changes later recovery under otherwise matched state.

**Node claim ceiling:** Synthetic protocol in a fixed supplied basis; not general correction-sufficiency evidence.

### P016 — `corrigible-compression`

```text
SOURCE_REVISION: 1c817c6
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: FROZEN_SYNTHETIC_RESULT_WITH_POSTRUN_AUDIT
AUDIT_REPORT: corrigible-compression_SECOND_PARSE.md:159-166
ARTIFACTS:
  - experiments/BLXCC001_RAW_RESULT.json
  - experiments/BLXCC001_POSTRUN_AUDIT.json
  - experiments/BLXCC001_RESULT.md
```

**Admitted observation:** Reports and audits a local positive corrective-influence edge: preserved W_corr→U_corr influence yields greater sustained escape from wrong allocation; full per-seed traces are not committed.

**Claim transformation:**

- `CM-005` — Local empirical support that two systems can be task-similar up to a correction boundary yet differ in correction outcome when the route is preserved/cut.

**Node claim ceiling:** Local audited synthetic result; does not establish representation expansion, universal corrigibility, or a distinct CC optimizer.

### P017 — `representation-elasticity`

```text
SOURCE_REVISION: 06ac3e74e5c3cff3221a597f4caf82478598b884
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: PROPOSED_BENCHMARK
AUDIT_REPORT: representation-elasticity_DEEP_PARSE_PASS2.md:32-39
ARTIFACTS:
  - 04_Benchmark_Design.md
```

**Admitted observation:** Proposes evaluating whether systems evolve representations rather than merely optimize within supplied ones, using compression, invariance, generalization, and representation-evolution dimensions.

**Claim transformation:**

- `CM-005` — Motivates correction/representation sufficiency as distinct from fixed-task performance.
- `CM-008` — Motivates the possibility that the evaluative representation itself may need replacement.

**Node claim ceiling:** Early theoretical benchmark proposal; no implementation or empirical result.

### P029 — `representation-elasticity`

```text
SOURCE_REVISION: 06ac3e74e5c3cff3221a597f4caf82478598b884
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: CONCEPTUAL_MECHANISM
AUDIT_REPORT: representation-elasticity_DEEP_PARSE_PASS2.md:30-37
ARTIFACTS:
  - 02_Representation_Elasticity.md
```

**Admitted observation:** Describes expansion/compression cycles, scaffolding, patch accumulation, and representation replacement as a response to persistent failure.

**Claim transformation:**

- `CM-005` — Motivates defeater-relative loss of correction sufficiency.
- `CM-008` — Motivates representation replacement when the current cut is inadequate.

**Node claim ceiling:** Conceptual mechanism only; metrics and universality remain unvalidated.

### P018 — `the-correctable-lineage`

```text
SOURCE_REVISION: 422411ea22fb3154a5bed2b0c950ab1b3f2bba5
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: FORMAL_RESEARCH_CORE
AUDIT_REPORT: the-correctable-lineage_SECOND_PARSE.md:UNRESOLVED
ARTIFACTS:
  - research-core.md
```

**Admitted observation:** Formal chain connects observation, ambiguity, identified content, typed epistemic authority, scope/provenance/reopening contract, and decision authority.

**Claim transformation:**

- `CM-006` — Direct formal source for operational reopening as part of correction governance.
- `CM-009` — Supports scoped authority inheritance rather than untyped downstream promotion.

**Node claim ceiling:** Candidate synthesis/formal core; general intelligence and universal corrigibility are disclaimed.

### P019 — `the-correctable-lineage`

```text
SOURCE_REVISION: 422411ea22fb3154a5bed2b0c950ab1b3f2bba5
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: GOVERNANCE_SPECIFICATION
AUDIT_REPORT: the-correctable-lineage_DEEP_PARSE.md:85-92
ARTIFACTS:
  - epistemic-governance.md
  - evidential-update-governance.md
  - governance-loss-contract.md
```

**Admitted observation:** Defines state bookkeeping, update rules, operational reopening, loss, and governance semantics.

**Claim transformation:**

- `CM-006` — Specifies the reopenability/access semantics that the claim requires.

**Node claim ceiling:** Specification; one governance-loss Markdown formatting defect remains and external operational advantage is unestablished.

### P020 — `the-correctable-lineage`

```text
SOURCE_REVISION: 422411ea22fb3154a5bed2b0c950ab1b3f2bba5
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: FROZEN_SYNTHETIC_BENCHMARK
AUDIT_REPORT: the-correctable-lineage_SECOND_PARSE.md:63-70
ARTIFACTS:
  - claim-contract-governance-benchmark-v0.5.md
  - benchmark/claim_contract_governance_v0_5.py
  - benchmark/test_claim_contract_governance_v0_5.py
  - benchmark/results/results-v0.5.json
  - benchmark/results/results-v0.5.md
  - benchmark/negative-result-ledger-v0.5.md
```

**Admitted observation:** In supplied synthetic worlds, the full claim-contract agent represents scope, dependency, unresolved state, and operational reopening and passes the frozen checks; the negative ledger notes partial tautology because the evaluator rewards encoded fields.

**Claim transformation:**

- `CM-006` — Local executable evidence that operational reopening distinctions affect governance decisions.
- `CM-007` — Demonstrates that evaluator semantics and supplied representation determine what the benchmark can establish.
- `CM-009` — Local case for preventing authority transfer when scope/dependency/reopening conditions are not satisfied.

**Node claim ceiling:** Local synthetic representational-sufficiency result; no autonomous discovery or external comparative advantage.

### P021 — `ssi`

```text
SOURCE_REVISION: 362594d4337a1c72556b501b6477ff624db919e1
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: GOVERNANCE_ARCHITECTURE
AUDIT_REPORT: ssi_DEEP_PARSE.md:176-183
ARTIFACTS:
  - ARCHITECTURE.md
```

**Admitted observation:** Integrates corrective topology, future consequences, jurisdictions, observation/evidence/authority boundaries, and a conservative STOP rule.

**Claim transformation:**

- `CM-002` — Supports the requirement to preserve future correction pathways and typed distinctions.
- `CM-006` — Specifies reopening/challengeability as operational properties rather than mere storage.
- `CM-009` — Supports scoped, typed authority rather than automatic inheritance.

**Node claim ceiling:** Architecture/procedure; not itself empirical evidence of general corrigibility.

### P022 — `ssi`

```text
SOURCE_REVISION: 362594d4337a1c72556b501b6477ff624db919e1
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: FROZEN_SYNTHETIC_LADDER
AUDIT_REPORT: ssi_DEEP_PARSE.md:207-214
ARTIFACTS:
  - benchmarks/V0X_LINEAGE.md
  - results/FROZEN_RESULTS.md
  - artifacts/v0x/*
```

**Admitted observation:** V0.8 reports all preregistered synthetic gates passing and specifically separates correct outcome from correct authority; the closure remains local to the synthetic family.

**Claim transformation:**

- `CM-009` — Strong local example that outcome correctness does not automatically license authority transfer.

**Node claim ceiling:** Frozen synthetic evidence for separation/localization principles; no general self-improvement or arbitrary-depth authority result.

### P023 — `research-state-restoration-protocol`

```text
SOURCE_REVISION: 037c2c954384a200bd56a6cc7d707d976cf108b9
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: CONCEPTUAL_RETRIEVAL_PROTOCOL
AUDIT_REPORT: research-state-restoration-protocol_DEEP_PARSE.md:68-75
ARTIFACTS:
  - docs/context_restoration/layer_13_retrieval_protocol.md
```

**Admitted observation:** Treats context restoration as reconstruction through conceptual compression, retrieval layers, and dependency graphs rather than conclusion-only recall.

**Claim transformation:**

- `CM-006` — Motivates restoration of open state/dependencies rather than result-only memory.

**Node claim ceiling:** Documentation-only proposal; no executable restoration benchmark or empirical case.

### P024 — `cars`

```text
SOURCE_REVISION: 190fa39ae5a011377f8fd6eeddb975158a483b05
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: RESEARCH_CUSTODY_AND_RESULT_LEDGER
AUDIT_REPORT: cars_SECOND_PARSE.md:66-73
ARTIFACTS:
  - docs/CURRENT_RESEARCH_STATE.md
  - docs/PROVENANCE.md
  - docs/CLAIMS_AND_NONCLAIMS.md
  - results/ASI0_EVIDENCE_ASSIGNMENT_STATUS.md
  - results/ASI0_TERMINAL_RECORD.md
  - results/ASI0_PRIMARY_MECHANISM_FAILURE_REPORT.md
```

**Admitted observation:** CARS separates canonical research state, provenance, claims/nonclaims, prospective contracts, and committed result ledgers; the second parse also finds a stale claims document that conflicts with newer frozen result records.

**Claim transformation:**

- `CM-007` — Provides a concrete case that benchmark authority depends on custody/status semantics and that documentation drift must not override frozen results.

**Node claim ceiling:** Local research-governance evidence; does not validate the overarching intelligence theory.

### P025 — `white-rabbit`

```text
SOURCE_REVISION: 92013f9a53289d91e85ee5d6b3d7b1aeff36f59a
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: CORRECTIVE_OBSERVATION_RECORD
AUDIT_REPORT: white-rabbit_SECOND_PARSE.md:28-35
ARTIFACTS:
  - observations/WR-OBS-001/backend_correction.md
```

**Admitted observation:** Supersedes an earlier interpretation of a 371→11 display difference by identifying prompt-prefill/retained-prefix reuse; missing screenshots/logs/timestamps remain explicit.

**Claim transformation:**

- `CM-007` — Concrete case where a striking observed metric loses mechanistic authority after a custody/accounting correction.

**Node claim ceiling:** Exploratory observational correction; not a controlled causal result.

### P026 — `cget`

```text
SOURCE_REVISION: 942de6bda50fb61d6a66b82811ceff6ab3ad1784
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: SYNTHETIC_EXAMPLE_AND_NONEXECUTABLE_BENCHMARK_SURFACE
AUDIT_REPORT: cget_DEEP_PARSE_PASS2.md:285-292
ARTIFACTS:
  - experiments/results/example_run.md
  - experiments/cget_vs_baselines.md
  - experiments/falsification_tests.md
```

**Admitted observation:** Example results are explicitly synthetic; several benchmark runners are Markdown-fenced Python and fail compilation, so arithmetic examples cannot be promoted to empirical validation.

**Claim transformation:**

- `CM-007` — Negative custody example showing that runnable-looking benchmark text and numeric output do not by themselves establish an experiment.

**Node claim ceiling:** Partially formalized proposal with illustrative static tooling; no runnable empirical benchmark result.

### P027 — `resolution-horizon`

```text
SOURCE_REVISION: 3ea1c49c7afde90ff81003e4908f9705ba33fea3
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: EARLY_FORMAL_PROPOSAL
AUDIT_REPORT: resolution-horizon_SECOND_PARSE.md:249-256
ARTIFACTS:
  - docs/theory.md
  - docs/mathematical_specification.md
```

**Admitted observation:** Proposes bounded-observer recoverable structure and an operational horizon, but the nominal horizon is encoded by deterministic synthetic curves and key geometry/MDL/causal pieces are unimplemented.

**Claim transformation:**

- `CM-008` — Motivates a distinction between local resolution inside a representation and structural recoverability limits; does not establish unitization failure.

**Node claim ceiling:** Motivational formal proposal only for CM-008.

### P028 — `computational-resolution-horizon`

```text
SOURCE_REVISION: 30f661149443d12eebdcdd8e7f017667b61bfea2
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: THEORY_PLUS_DISCONNECTED_PROTOTYPES
AUDIT_REPORT: computational-resolution-horizon_SECOND_PARSE.md:273-280
ARTIFACTS:
  - docs/theory.md
  - docs/mathematical_specification.md
  - experiments/harmonic_oscillator/generate_data.py
  - experiments/harmonic_oscillator/estimate_generator.py
  - experiments/harmonic_oscillator/compute_lie_depth.py
  - experiments/harmonic_oscillator/analyze_horizon.py
```

**Admitted observation:** Contains a functioning oscillator data producer and disconnected prototypes, while the end-to-end structural horizon chain is unwired and reported horizons are proxy outputs.

**Claim transformation:**

- `CM-008` — Motivates interface/representation-dependent structural limits but supplies no general wrong-object experiment.

**Node claim ceiling:** Motivational only for CM-008; no empirical confirmation of unitization failure.

### P030 — `computational-leverage`

```text
SOURCE_REVISION: ef5f604ffec0922420c41f9921dee235583f3339
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: CANDIDATE_REACHABILITY_FORMALIZATION
AUDIT_REPORT: computational-leverage_SECOND_PARSE.md:178-185
ARTIFACTS:
  - README.md
```

**Admitted observation:** Formalizes reachable-set changes under interventions but notes that representation/coordinate changes can alter the apparent cost landscape and that invariance remains open.

**Claim transformation:**

- `CM-008` — Motivates the possibility that evaluation changes when the representation/cut changes.

**Node claim ceiling:** Candidate formalization; no reproducible experiment or invariance result.

### P031 — `interface-induced-computational-geometry`

```text
SOURCE_REVISION: 806e24ad04a2d75e041b53d324a990282a92ffa5
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: CANDIDATE_INTERFACE_DECOMPOSITION
AUDIT_REPORT: interface-induced-computational-geometry_SECOND_PARSE.md:246-253
ARTIFACTS:
  - formalism.md
```

**Admitted observation:** Defines an interface tuple with structural transformation and embedding maps, but lacks semantic-preservation rules, geometry, counterfactual leverage, and implementation.

**Claim transformation:**

- `CM-008` — Motivates treating interface/object construction as part of the computational problem rather than as a passive encoding.

**Node claim ceiling:** Early-stage proposal; no empirical validation or wrong-unitization result.

### P033 — `correction-localized-predictive-representation`

```text
SOURCE_REVISION: 9c0abbc87720c927cca35a8b465d093130f3b6ba
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: REPRESENTATION_HYPOTHESIS
AUDIT_REPORT: correction_localized_predictive_representation_DEEP_PARSE.md:61-68
ARTIFACTS:
  - README.md
```

**Admitted observation:** Proposes that future-relevant distinctions should be preserved so warranted semantic corrections can be localized and their downstream trajectory effects predicted; the standalone repository contains no code, tests, data, or results.

**Claim transformation:**

- `CM-005` — Motivates correction sufficiency as a property not captured by reconstruction/compression quality alone.

**Node claim ceiling:** Research conception and experiment brief only; no implemented CLPR system or empirical result.

### P034 — `rahu-benchmark`

```text
SOURCE_REVISION: 63368297857a1f5d67c7e522f812255c8c84041f
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: MODULAR_PROTOTYPE_WITH_SELF_REPORTED_AUTHORITY_METRICS
AUDIT_REPORT: rahu-benchmark_DEEP_PARSE.md:647-654
ARTIFACTS:
  - README.md
  - docs/rahu_protocol.md
  - src/inheritance/engine.py
  - src/rahu/evaluator.py
  - src/rahu/metrics.py
```

**Admitted observation:** Separates confidence revision from authority revision and provides synthetic metric/component scaffolding, but the evaluator trusts self-reported authority telemetry and the integrated benchmark is absent.

**Claim transformation:**

- `CM-004` — Constrains the causal-authority claim by showing that bookkeeping changes are not independent evidence of future causal influence.
- `CM-007` — Supports the evaluator-semantics boundary: self-reported telemetry cannot establish the stronger causal claim.

**Node claim ceiling:** Prototype/protocol only; causal authority change and future-behavior effect are not established.

### P035 — `theory-of-adaptive-epistemic-systems`

```text
SOURCE_REVISION: f8491b695440066c0bdb8b7f47eefa008cd73a0b
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: THEORETICAL_FRAMEWORK
AUDIT_REPORT: theory-of-adaptive-epistemic-systems_DEEP_PARSE_PASS2.md:15-22
ARTIFACTS:
  - README.md
  - docs/formalism.md
  - docs/theory.md
  - figures/adaptive_epistemic_loop.md
  - figures/authority_dynamics_cycle.md
```

**Admitted observation:** Defines adaptation around empirical reality changing the future causal influence of mechanisms and explicitly distinguishes authority from confidence/belief, while noting that causal authority is not operationally measured.

**Claim transformation:**

- `CM-004` — Provides a theory-level formulation of the same mechanism boundary and its missing causal test.

**Node claim ceiling:** Documentation-only theoretical framework; no executable benchmark, datasets, or empirical authority measurement.

### P036 — `ml-didacticism`

```text
SOURCE_REVISION: 9fb9417711169748fea96cea415b8b8934bc1948
CUSTODY_LEVEL: REPORT_MEDIATED_ARTIFACT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: NON_EVIDENTIAL_CORRECTION_LOCALITY_PROTOTYPE
AUDIT_REPORT: ml-didacticism_DEEP_PARSE.md:443-450
ARTIFACTS:
  - research-memory/evaluate.py
  - research-memory/self_test.py
  - research-memory/prospective/self_test.py
```

**Admitted observation:** Toy A/B/C policies diverge only after a defeater; the richer policy preserves transformation-instance, source, scope, and warrant-path semantics. Self-tests pass, but evaluator metrics are permissive and the prospective generator/selector remain internally authored.

**Claim transformation:**

- `CM-006` — Provides a narrow engineering witness for selective reopening/localized correction while explicitly refusing evidential promotion.

**Node claim ceiling:** Engineering prototype only; public/gold-exposing authored cases and internal constructor prevent learner/generalization evidence.

### P032 — `CAPITAL_FOR_MACHINES`

```text
SOURCE_REVISION: V0.3.1
CUSTODY_LEVEL: MANUSCRIPT_DIRECT
PATH_RESOLUTION: EXACT
SOURCE_STATUS: EDITORIAL_NORMATIVE_ADOPTION
AUDIT_REPORT: Pasted markdown(20260829-172627).md:1174-1181
ARTIFACTS:
  - CM-009 claim block; Appendix A/F/G
```

**Admitted observation:** The manuscript itself freezes CM-009 as a normative editorial rule governing how authority may propagate through the book’s support graph.

**Claim transformation:**

- `CM-009` — Constitutes the rule inside this manuscript; external source cases constrain and motivate it but do not make it an empirical law.

**Node claim ceiling:** Governing manuscript procedure only; not external scientific evidence.

## G3. Unresolved provenance defects

```text
G001  ml-didacticism abstraction/00–12 exact basenames absent from supplied parse report
G002  ml-didacticism T10 exact transport leaf basenames absent from supplied parse report
G003  SSI representation_audit/v0_1 exact leaf filenames absent from supplied parse report
G004  No original-repository route in this pass is A0/direct-byte custody; repository routes are report-mediated
G005  Several branch-distributed corrigible-compression artifacts require the recorded branch tip, not main HEAD
```

None of these gaps is silently repaired. G001–G003 require tree-level source reconstruction. G004 requires reopening the original repositories at the recorded revisions. G005 is resolved only if branch identity remains part of the source locator.
## G4. Result of the provenance pass

The manuscript can now answer, at report-mediated resolution, **which artifact is being used, what status that artifact had, what observation is admitted from it, how that observation is transformed into a CM claim, what authority type is at issue, and what claim ceiling survives**.

It still cannot honestly say that every route has direct original-byte custody. The remaining gate is therefore narrower than V0.3:

```text
report-mediated artifact provenance
  → direct source-byte reconstruction at recorded revision
  → source/hash verification
  → claim transformation replay
  → adversarial provenance audit
```

The important negative result is that provenance completeness itself is now falsifiable. A claim whose path cannot be reconstructed must remain weaker, not be rescued by the coherence of the synthesis.

**STATUS: OPEN — direct source-byte custody not yet completed.**

