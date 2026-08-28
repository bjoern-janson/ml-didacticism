# Adversarial Ablation — COMMITMENT and AUTHORITY

**Depends on:**
- `abstraction/00_ABSTRACTION_PROTOCOL.md`
- `abstraction/01_RELATION_INVENTORY.md`
- `abstraction/02_INVARIANT_STRIPPING_TESTS.md`
- `abstraction/03_MINIMAL_ARCHITECTURE.md`

**Purpose:** attempt to eliminate the two strongest remaining semantic candidates, `COMMITMENT` and `AUTHORITY`, without introducing replacement machinery unless a reconstruction failure forces it  
**Status:** adversarial ablation pass; provisional minimal-kernel result; no external-domain testing

The governing rule is deletion, not enrichment:

```math
\boxed{\textbf{remove machinery; do not add abstractions unless a reconstruction failure forces one}}
```

The current candidate architecture entering this pass is:

```math
\boxed{
\mathcal A^{(1)}=
\{ENTITY,STATE,EVENT,RELATION,TIME,ACCESS,REPRESENTATION,AUTHORITY,COMMITMENT\}
+
\{SOURCE\_PROVENANCE,OPEN\}
}
```

This pass attacks only the two semantic survivors:

```math
\boxed{COMMITMENT\qquad AUTHORITY}
```

Allowed verdicts:

```text
DERIVABLE
DERIVABLE WITH LOSS
IRREDUCIBLE
```

A successful reduction requires both:

```math
\boxed{\text{explicit reconstruction witness}}
```

and:

```math
\boxed{\text{hidden-parameter audit passes}}
```

---

# 0. Anti-cheat rule: hidden-parameter audit

A reduction is invalid if the removed primitive simply reappears as an unconstrained parameter of a retained primitive.

Examples of invalid reductions:

```text
COMMITMENT removed
→ RELATION(type="commitment", ...)

AUTHORITY removed
→ EVENT(permission="authorized", ...)

AUTHORITY removed
→ RELATION(kind="has authority over", ...)
```

These are renamings, not reductions.

Formally:

```math
\boxed{
X\text{ removed}
\land
X\text{-equivalent semantic bit survives as a free parameter}
\Rightarrow
\text{ABLATION FAILS}
}
```

The audit question is:

```text
If all names for the removed primitive are forbidden,
can the remaining graph still reconstruct the source distinction
using only independently required structure?
```

The optimization target remains:

```math
\boxed{
\min |B|
\quad\text{s.t.}\quad
\operatorname{Reconstruct}(B)=\text{all source-earned distinctions}
}
```

not:

```math
\boxed{\min\text{ number of visible labels}}
```

---

# 1. Target A — kill `COMMITMENT`

## 1.1 Kill hypothesis

Attempt:

```math
\boxed{
COMMITMENT
\stackrel{?}{=}
REPRESENTATION
+
\text{future temporal content}
+
RELATION
+
AUTHORITY
}
```

The strongest possible reduction would encode request, promise, oath, and surety without any primitive corresponding to binding force.

The test cases are chosen because their future content can be very similar while their structural consequences differ.

---

## 1.2 Case C1 — request without promise

Source discriminator: Genesis 40.

Structural record:

```text
A asks B:
    when future favorable condition occurs
    remember A
    mention A to a higher actor
    cause A's release

B gives no narrated promise.
Later:
    favorable condition occurs
    B does not remember A.
```

Required distinction:

```math
\boxed{
\text{future action requested}
\neq
\text{future action promised}
}
```

A representation-only encoding can represent:

```text
speaker=A
content=B performs X in future
recipient=B
```

but that same skeleton is insufficient to distinguish:

```text
A requests B do X
```

from:

```text
B promises A that B will do X
```

because both may contain the same future proposition:

```math
X_B(t+n)
```

The difference is not the represented future event.

It is the relation created by the speech act.

---

## 1.3 Case C2 — promise and oath over nearly identical future content

Source discriminator: Genesis 47.

Structural sequence:

```text
A requests terminal action X from B.
B says: I will do X.
A then says: swear to me.
B swears.
```

The future action content remains approximately:

```math
B\text{ performs }X\text{ after A dies}
```

before and after the oath.

Therefore:

```math
\boxed{
\Delta\text{future-content}\approx 0
}
```

while the text explicitly adds a new event/state transition:

```text
promise
→ requested strengthening
→ oath
```

If `COMMITMENT` is removed, the architecture must still explain why the oath event is not merely a repeated future representation.

### Reconstruction attempt using only representation + ordinary relation

Possible representation:

```text
R_B(X_future)
R_B(X_future) again
```

Failure:

```text
first utterance and oath become structurally interchangeable repetitions
```

Possible ordinary-relation workaround:

```text
RELATION(B,X,force=high)
```

Hidden-parameter audit:

```text
FAIL — `force` is the removed commitment distinction under another name.
```

Therefore future representation alone cannot reconstruct promise → oath strengthening.

---

## 1.4 Case C3 — surety

Source discriminator: Genesis 43–44.

Structural record:

```text
A guarantees return of B to C.
IF B is not returned:
    A bears an adverse consequence / enduring blame relation.

Later:
    B is threatened with non-return.
    A proposes remaining under the adverse condition instead of B.
```

This is not merely:

```text
A predicts B will return.
```

Nor merely:

```text
A wants B to return.
```

Nor merely:

```text
A has authority over B.
```

The key structure is:

```math
\boxed{
\text{failure of future state concerning }B
\Rightarrow
\text{consequence attaches to }A
}
```

The later substitution proposal is behaviorally linked to this earlier relation.

A generic conditional relation can encode the dependency:

```math
\neg Return(B)\Rightarrow Consequence(A)
```

but this alone still does not distinguish:

```text
A predicts consequence will happen
```

from:

```text
A has placed himself under / accepted that consequence condition.
```

If that difference is placed in:

```text
RELATION(mode="binding")
```

then the hidden-parameter audit fails.

---

## 1.5 Case C4 — collective oath with deferred execution

Source discriminator: Genesis 50.

Structural record:

```text
A represents a future departure condition.
A causes group G to swear:
    when future condition occurs
    G will transfer A's remains.

A dies.
Corpus ends before transfer occurs.
```

The architecture must preserve:

```math
\boxed{
\text{future transfer represented}
+
\text{group bound to future action}
+
\text{action still unrealized}
}
```

If `COMMITMENT` is removed, the state at corpus end collapses toward an ordinary prediction/request unless some other retained structure records that the group has entered a persistent future-directed relation.

No combination of `ACCESS`, `AUTHORITY`, or descriptive `REPRESENTATION` supplies that fact.

---

# 2. COMMITMENT ablation result

## 2.1 What is derivable

The large `OBLIGATION` machinery remains eliminated.

The following are compositions:

```text
future target
trigger condition
beneficiary
obligated party
completion/deferment
consequence condition
persistence across time
```

Likewise the lexical subclasses do not each need primitive status.

### Request

Can be represented as a communicative representation/event directed at another agent:

```math
Request(A,B,X)
:=
Event_{speech}(A\to B,\ content=X_{future})
```

with **no binding edge necessarily created**.

### Promise

Adds the irreducible residue:

```text
speaker becomes bound relative to future action/content
```

### Oath

Does not require a new primitive beyond commitment.

It is reconstructible as:

```text
existing/new commitment
+
explicit strengthening/solemnization event
+
source-specific speech relation
```

The exact theological/legal force is not generalized beyond source structure.

### Surety

Does not require its own primitive.

It is reconstructible as:

```text
commitment
+
condition on another agent's future state
+
consequence reassignment to guarantor
```

Thus:

```math
\boxed{
REQUEST, PROMISE, OATH, SURETY
\not\Rightarrow
4\text{ primitives}
}
```

---

## 2.2 What does not derive

The irreducible residue is the difference between:

```text
an agent representing a future action
```

and:

```text
an agent entering / creating a persistent future-directed binding relation concerning that action.
```

Call this residue the **commitment kernel** without introducing a new ontology element:

```math
\boxed{
COMMITMENT(a,x,t)
}
```

means minimally:

```text
at time t,
a is structurally bound relative to future content/action x,
such that later trigger/completion history is evaluated against that relation.
```

The word `bound` is descriptive of the source-earned distinction; it is not a complete moral, legal, or theological theory.

## 2.3 Counterfactual reconstruction failure

Remove the commitment kernel entirely.

Then the architecture cannot distinguish, without smuggling in a hidden parameter:

```text
I request that you do X
I predict that you will do X
I intend that X occur
I promise that I will do X
I swear that I will do X
I guarantee Y and accept consequence Z if Y fails
```

when these records share overlapping future propositional content.

The lost variable is:

```math
\boxed{
\text{future content}
\neq
\text{binding relation created around that content}
}
```

## 2.4 Verdict

```text
COMMITMENT: IRREDUCIBLE KERNEL
```

The **state machine** is derivable.
The **subtypes** are largely compositional.
The **binding relation itself** is not eliminated.

---

# 3. Target B — kill `AUTHORITY`

## 3.1 Kill hypothesis

Attempt:

```math
\boxed{
AUTHORITY
\stackrel{?}{=}
ROLE
+
ACCESS
+
CAPABILITY
+
COMMITMENT
+
EVENT\ HISTORY
}
```

`ROLE` and `CAPABILITY` are not added primitives here; they are ordinary state/relation descriptions already representable in the carrier structure.

The question is whether authority contributes anything beyond:

```text
who occupies what role
who knows what
who can physically perform what
who has promised what
what happened previously
```

---

## 3.2 Case A1 — proposal without appointment

Source discriminator: Genesis 41.

Structural sequence:

```text
A interprets future risk.
A proposes a response policy.
A proposes that a suitable administrator be appointed.
Ruler evaluates proposal.
Ruler selects A.
Ruler grants A large-scale operational authority.
A executes program.
```

Before selection:

```text
A has relevant information
A has planning capability
A can formulate policy
A can propose an administrator role
```

but:

```text
A has not appointed himself
A does not yet possess the resulting system-wide decision-right
```

Therefore:

```math
\boxed{
CAPABILITY+REPRESENTATION+PROPOSAL
\neq
AUTHORITY
}
```

If authority is removed, the architecture cannot explain the state transition created by the ruler's appointment except by adding an `authorized=true` or `role=effective-admin` semantic flag.

Parameter audit:

```text
If that flag determines which agent's decisions count over the system,
it is authority under another name.
```

---

## 3.3 Case A2 — ownership and delegated control

Source discriminator: Genesis 39.

Structural pattern:

```text
Owner retains ownership relation.
Owner delegates broad household control to subordinate.
One explicit relation remains excluded from delegation.
Owner reduces direct oversight.
Subordinate performs broad operational management.
```

This proves:

```math
\boxed{
OWNERSHIP
\neq
DELEGATED\ DECISION\ RIGHT
}
```

A role label such as `servant` also fails:

```math
\boxed{
formal\ subordinate\ status
+
large\ functional\ control
}
```

can coexist.

Thus authority cannot be reconstructed from ownership or formal rank alone.

---

## 3.4 Case A3 — authorization without personal execution

Source discriminators: Genesis 47 and Genesis 50.

Pattern:

```text
Agent wants/proposes movement or settlement action.
Higher ruler authorizes it.
Another agent then performs operational execution.
```

Examples include:

```text
ruler authorizes settlement
administrator performs placement/resource operations
```

and:

```text
agent requests leave for burial journey
ruler authorizes journey
agent personally participates in execution afterward
```

The key distinction is:

```math
\boxed{
\text{deciding that an action may/counts to occur}
\neq
\text{physically executing the action}
}
```

Capability does not reconstruct authorization.
Commitment does not reconstruct authorization.
Access does not reconstruct authorization.

---

## 3.5 Case A4 — attempted correction without final allocation control

Source discriminator: Genesis 48.

Structural sequence:

```text
A positions two candidates according to inherited order.
B knowingly allocates priority in the opposite order.
A detects mismatch.
A physically attempts to alter B's placement.
A verbally asks B to correct it.
B refuses.
B's allocation remains final in the scene.
```

This is a very strong discriminator because A has:

```text
access to the relevant fact
physical capability to attempt correction
an expressed preference
an action attempt
```

but does not control the terminal allocation.

Thus:

```math
\boxed{
\text{can act on relation}
\neq
\text{has decision-right over relation}
}
```

If authority is removed, one can record only:

```text
A acts
B acts
final state follows B
```

but cannot represent the source-earned relational difference between:

```text
A's attempted correction
```

and:

```text
B's constitutive/final allocation decision
```

without encoding a hidden `precedence`, `jurisdiction`, or `decision-owner` parameter.

Each such workaround is authority semantics.

---

## 3.6 Case A5 — capability without permission / permission without execution

Across the corpus, agents can physically perform actions that are prohibited, and can receive permission/authorization for actions they have not yet performed.

Therefore:

```math
\boxed{
CAPABILITY
\neq
PERMISSION
\neq
EXECUTION
}
```

A purely causal architecture can say what an agent can or did do.
It cannot reconstruct which actions are admitted, delegated, prohibited, or constitutively assigned within a relation scope.

This again leaves a semantic residue.

---

# 4. AUTHORITY decomposition attempt

The strongest attempted decomposition is:

```math
Authority
\stackrel{?}{=}
Permission + Jurisdiction + Precedence
```

This is useful diagnostically but does **not** reduce the semantic basis.

Why?

Because none of the three terms is derivable from `ROLE + ACCESS + CAPABILITY + COMMITMENT` without reintroducing authority semantics.

### Permission

Answers:

```text
may this actor perform/authorize this action?
```

### Jurisdiction

Answers:

```text
over which relation/target/scope does this actor's decision count?
```

### Precedence

Answers:

```text
when incompatible interventions occur, which decision governs the terminal relation?
```

These are useful dimensions of authority topology, but introducing all three as new primitives to delete one primitive would be anti-minimization.

The corpus does not yet force them to be independently primitive.

They can remain fields/dimensions of a single irreducible authority kernel as long as those fields are constrained rather than arbitrary semantic escape hatches.

---

# 5. AUTHORITY ablation result

The minimal irreducible residue is not scalar `power`.

It is approximately:

```math
\boxed{
AUTHORITY(a,\tau,s,target,t)
}
```

where:

```text
a      = authority holder
τ      = action / relation-transition class
s      = scope / jurisdiction
 target = affected entity/relation/population
 t      = time interval
```

Its minimal meaning is:

```text
within scope s at time t,
actor a has the source-recognized decision-right by which an action/decision
of class τ can authorize, constitute, delegate, constrain, or override
a relation/state transition concerning target.
```

This definition does not assert a universal political/legal theory.
It encodes the minimum structural difference Genesis repeatedly requires between:

```text
having a role
being able to act
wanting an outcome
proposing an outcome
being allowed to act
being able to make a decision count
executing the resulting action
```

## Hidden-parameter audit

Attempted replacements fail:

```text
ROLE(priority=high)          → hidden authority
RELATION(decides_for=...)    → hidden authority
EVENT(valid=true)            → hidden authority
CAPABILITY(can_bind=...)     → hidden authority
STATE(jurisdiction=...)      → hidden authority
```

unless the semantic content is explicitly acknowledged.

## Verdict

```text
AUTHORITY: IRREDUCIBLE KERNEL
```

Delegation, authorization, appointment, override, and execution routing are compositions around this kernel rather than separate primitives.

---

# 6. Cross-test: COMMITMENT and AUTHORITY are not the same primitive

A final reduction attempt asks whether one survivor can absorb the other.

## Can commitment be reduced to authority?

No.

A person can enter a future-directed commitment concerning their own behavior without thereby receiving decision-right over another relation or agent.

Genesis 47's burial promise/oath concerns what the promisor will later do; it does not by itself grant broad external jurisdiction.

Genesis 43's surety creates a consequence-bearing future relation for Judah; it does not make Judah sovereign over the entire interaction.

Therefore:

```math
\boxed{COMMITMENT\not\subseteq AUTHORITY}
```

## Can authority be reduced to commitment?

No.

A ruler can authorize or delegate an action without promising personally to execute that action.

A senior allocator can possess final decision-right even while a subordinate makes the physical correction attempt.

Therefore:

```math
\boxed{AUTHORITY\not\subseteq COMMITMENT}
```

## Can both reduce to a generic normative relation?

This would merely rename both residues and lose their different behavior.

The corpus requires:

```math
\boxed{
\text{being bound regarding a future action}
\neq
\text{having decision-right over a scoped state transition}
}
```

Therefore a single unconstrained `NORMATIVE_RELATION` primitive is too coarse.

---

# 7. Revised minimal candidate

After adversarial ablation, neither semantic survivor disappears completely.

But both shrink substantially.

The revised candidate is:

```math
\boxed{
\mathcal A^{(2)}=
\underbrace{\{ENTITY,STATE,EVENT,RELATION,TIME\}}_{carrier}
\cup
\underbrace{\{ACCESS,REPRESENTATION,COMMITMENT,AUTHORITY\}}_{semantic\ kernels}
\cup
\underbrace{\{SOURCE\_PROVENANCE,OPEN\}}_{meta}
}
```

The important change is semantic scope:

### `COMMITMENT`

No longer means a full obligation lifecycle.

It means only the irreducible future-directed binding relation that distinguishes promise/oath/surety-bearing states from ordinary future representation or request.

Everything else is compositional.

### `AUTHORITY`

No longer means scalar social power or a list of institutional labels.

It means only the irreducible scoped decision-right governing which agent can make a relation/state transition count, authorize it, delegate it, or prevail when incompatible interventions occur.

Everything else is compositional.

---

# 8. Dependency compression after this pass

The eliminated higher-level objects now reconstruct as follows.

## Obligation lifecycle

```math
\boxed{
REPRESENTATION_{future}
+
COMMITMENT
+
TIME
+
EVENT
+
STATE
\Rightarrow
\text{obligation lifecycle}
}
```

## Delegation

```math
\boxed{
AUTHORITY_{holder}
+
EVENT_{grant}
+
AUTHORITY_{recipient,new\ scope}
+
TIME
\Rightarrow
\text{delegation}
}
```

## Authorization

```math
\boxed{
AUTHORITY(a,\tau,s,x,t)
+
EVENT_{decision}
\Rightarrow
\text{authorized prospective action/event}
}
```

## Override / failed correction

```math
\boxed{
EVENT_{attempt,A}
+
EVENT_{refusal,B}
+
AUTHORITY_B(transition)
+
STATE_{final}
\Rightarrow
\text{attempted correction without governing transition}
}
```

## Surety

```math
\boxed{
COMMITMENT_A
+
Condition(state_B)
+
Consequence_A
+
TIME
\Rightarrow
\text{surety structure}
}
```

No extra `SURETY` primitive is needed.

---

# 9. What this pass did not prove

This pass does **not** prove that the four semantic kernels are universally primitive outside Genesis.

It proves only:

```math
\boxed{
\text{within the current Genesis-derived architecture, removing either}
\ COMMITMENT\text{ or }AUTHORITY
\text{ destroys source-earned distinctions unless equivalent semantics are smuggled back in.}
}
```

Likewise, this pass does not prove the carrier basis itself is globally minimal.

The next minimization pressure should target the carrier/semantic boundary rather than invent new relation families.

Possible later questions include:

```text
Can STATE be reconstructed from time-indexed relations/events?
Can RELATION and STATE be unified without hiding semantics?
Can ACCESS be represented as a constrained relation subtype without becoming an unconstrained type escape hatch?
Can COMMITMENT and AUTHORITY be represented as constrained transition operators rather than separate node classes while preserving their semantic independence?
```

Those are later ablations, not conclusions of this file.

---

# 10. Current strongest result

The important result is not that `COMMITMENT` and `AUTHORITY` survived by name.

It is that deletion exposed the minimum distinction each is carrying.

```math
\boxed{
\textbf{future content}
\neq
\textbf{future-directed binding force}
}
```

and:

```math
\boxed{
\textbf{capacity to act}
\neq
\textbf{decision-right over a scoped state transition}
}
```

These two residues are independent:

```math
\boxed{
COMMITMENT\neq AUTHORITY
}
```

The architecture is therefore not being enlarged.

It is being sharpened by failed deletion.

The governing maxim after this pass is:

```math
\boxed{\textbf{A primitive is what remains when every honest attempt to delete it loses reconstructible structure.}}
```
