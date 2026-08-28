# T10 Milestone — Blind 001 Contamination / Level-3 Boundary

**Status:** FROZEN METHODOLOGICAL MILESTONE  
**Architecture:** `AG/1 = {RELATION, REPRESENTATION} + {SOURCE_PROVENANCE, OPEN}`  
**Prior reconstruction frontier:** `transport/MILESTONE_T1_T9.md`  
**Pilot:** `transport/t10/03_BLIND_001_REVEAL_AND_SCORE.md`  
**Pilot outcome:** `CONTAMINATED` — not a Level-3 result

---

# 1. Evidential state remains unchanged

The valid transport ledger remains:

```text
T1–T9  PASS  reconstruction / transport
```

with the calibrated claim:

```math
\boxed{
\textbf{AG/1 has survived nine heterogeneous external reconstruction tests without architectural enlargement.}
}
```

T10.001 does **not** add:

```text
PASS
FAIL_RECONSTRUCTION
GENERATION_FAILURE
LEVEL3_CONFIRMED
```

It is a protocol-isolation result:

```text
T10.001  CONTAMINATED
```

because the experiment failed to isolate autonomous structural invention from search inside a learner-known structural family.

---

# 2. Main methodological discovery

T10.001 established:

```math
\boxed{
\textbf{hidden answer}
\neq
\textbf{hidden hypothesis family}
}
```

The exact hidden topology was cryptographically sealed.

But the learner had authored the generator and therefore knew that the hidden answer belonged to a narrow family:

```text
joint interaction among controls affecting one output
```

Thus exact-answer secrecy was insufficient.

The candidate could be novel relative to the exposed data/model while remaining non-novel relative to the learner's preauthorized search space.

---

# 3. Three distinct hiddenness variables

Future Level-3 tests must separate:

## H_answer

```math
\boxed{H_{answer}}
```

The exact hidden relation/topology, parameterization, and final answer.

## H_family

```math
\boxed{H_{family}}
```

The structural family in which the hidden answer resides.

Examples of leaked family information include:

```text
"the missing structure is some interaction"
"the answer is one of these causal motifs"
"choose among mediation / confounding / feedback"
"some hidden edge among this supplied finite set is correct"
```

## H_constructor

```math
\boxed{H_{constructor}}
```

The task constructor's prior knowledge about what kind of distinction is intended to be discoverable.

A constructor can leak a family without stating it explicitly through:

```text
choice of variables
allowed interventions
challenge API shape
synthetic generator restrictions
provided terminology
prompt framing
which anomaly is selected
```

Therefore:

```math
\boxed{
H_{answer}\text{ hidden}
\not\Rightarrow
H_{family}\text{ hidden}
\not\Rightarrow
H_{constructor}\text{ independent}
}
```

---

# 4. Three novelty notions

A future claim must distinguish:

## N_data — novel to exposed representation/data

```math
\boxed{N_{data}}
```

The candidate relation was absent from the initial representation and evidence packet.

T10.001 satisfied this.

## N_learner — novel to learner-visible hypothesis space

```math
\boxed{N_{learner}}
```

The candidate was not supplied explicitly or implicitly as a preauthorized structural family available to the learner before contradiction-driven generation.

T10.001 did **not** establish this.

## N_constructor — not selected from a constructor-known narrow answer menu exposed through task design

```math
\boxed{N_{constructor}}
```

The task-construction process must not communicate the intended future ontology to the learner through narrow generator design or curation cues.

A Level-3 claim requires more than `N_data`.

At minimum:

```math
\boxed{
N_{data}+N_{learner}
}
```

must be established, with constructor leakage independently audited.

---

# 5. Layer separation

The research ladder is now:

```math
\boxed{
\begin{aligned}
L_1 &: \text{Can the architecture represent a distinction?}\\
L_2 &: \text{Can a learner recover/select a supplied-but-hidden distinction or family?}\\
L_3 &: \text{Can a learner generate a useful distinction not supplied as answer or candidate family?}
\end{aligned}
}
```

T1–T9 primarily establish bounded `L_1` transportability.

T10.001 demonstrated strong behavior on a blind hidden instance but, because `H_family` leaked through generator authorship, is at best evidence about an `L_2`-like search/recovery capability.

It does not measure `L_3`.

---

# 6. CONTAMINATED is a permanent outcome class

`CONTAMINATED` is not an architecture failure.

It means:

```math
\boxed{
\textbf{the experiment failed to isolate the capability being claimed.}
}
```

It must remain separate from:

```text
PASS
FAIL_RECONSTRUCTION
GENERATION_FAILURE
OPEN_TEST
```

Recommended subtypes:

```text
CONTAMINATED_ANSWER
CONTAMINATED_FAMILY
CONTAMINATED_CONSTRUCTOR
CONTAMINATED_POSTHOC
CONTAMINATED_ORACLE
```

T10.001 is classified as:

```text
CONTAMINATED_FAMILY
+
CONTAMINATED_CONSTRUCTOR
```

because the same learner context authored the narrow hidden generator family.

---

# 7. Stronger Level-3 causal cut

A valid future run must satisfy:

```math
\boxed{
\begin{aligned}
&X\notin content(\rho_t)\\
&X\notin \mathcal C_{supplied}\\
&family(X)\notin \mathcal F_{learner\text{-}visible}^{narrow}\\
&\text{task constructor independent of learner candidate generation}\\
&\text{candidate committed before discovery/answer record is accessible}\\
&\text{candidate entails prospective discriminating consequence}\\
&\text{challenge executed after candidate freeze}\\
&\text{learner can RETAIN, RETRACT, REVISE, or OPEN from evidence}
\end{aligned}
}
```

The crucial new requirement is:

```math
\boxed{
\textbf{answer secrecy is insufficient without hypothesis-family isolation.}
}
```

---

# 8. Corrigible invention remains part of the target

A spectacular Level-3 result is not merely:

```text
contradiction
→ novel candidate
→ candidate happens to be right
```

The target includes candidate reopenability:

```math
\boxed{
\text{invent}
\rightarrow
\text{challenge}
\rightarrow
\begin{cases}
\text{retain if earned}\\
\text{retract/revise if contradicted}
\end{cases}
}
```

Therefore a wrong novel candidate followed by correct empirical retraction is a scientifically valuable success on corrigibility even though it is not hidden-topology recovery.

---

# 9. Binding interpretation

T10.001 should be remembered as:

```math
\boxed{
\textbf{the first Level-3 pilot correctly invalidated its own apparent success.}
}
```

That is positive evidence for the experimental discipline, not evidence for autonomous interface invention.

The Level-3 boundary remains OPEN.
