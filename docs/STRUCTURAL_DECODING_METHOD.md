# Structural Decoding Method

**Status:** working method / revisable / not a theological claim

> **Current-reader note:** this document records **derivation-era parsing notation**, not the final primitive architecture. Convenient categories here such as `STATE`, `EVENT`, `TIME`, `ACCESS`, `AUTHORITY`, `COMMITMENT`, and `ENTITY` were later subjected to explicit ablation. The frozen result is [`../abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md`](../abstraction/12_GENESIS_ARCHITECTURE_FREEZE.md): `RELATION + REPRESENTATION`, with `SOURCE_PROVENANCE + OPEN`. Read this file for method lineage and chapter-reading discipline, not as the current ontology specification.

This document governs the structural layer only. Corpus preparation happens first under [`AI_PARSABLE_CORPUS.md`](AI_PARSABLE_CORPUS.md).

The project order is:

```math
\boxed{
\text{raw KJV}
\rightarrow
\text{normalized corpus}
\rightarrow
\text{mechanical annotations}
\rightarrow
\text{structural decoding}
\rightarrow
\text{bounded interpretation}
}
```

The structural layer asks:

> **What information structure is this text preserving?**

The governing boundary is:

```math
\boxed{\text{TEXT} \neq \text{STRUCTURAL PARSE} \neq \text{INTERPRETATION}}
```

A structural parse may be useful while still being incomplete, contestable, or non-unique.

The strongest symbol discipline is:

```math
\boxed{\textbf{Every formal symbol must correspond to something actually recoverable from the text.}}
```

If a passage does not identify whether something is causal, intentional, predictive, normative, or otherwise typed, preserve the gap as **OPEN** rather than completing it by assumption.

---

# 1. Structural decoding pipeline

Once the machine-legible source layer exists, structural decoding proceeds as:

```math
\boxed{
\text{source text + mechanical spans}
\rightarrow
\text{optional plain rendering}
\rightarrow
\text{typed structural parse}
\rightarrow
\text{causal / temporal relations}
\rightarrow
\text{bounded interpretation}
}
```

The plain rendering is optional and explicitly lossy. It never replaces `text_kjv` or `text_normalized`.

Mechanical annotation is not structural interpretation. A token or span labelled `command`, `negation`, or `question` does not by itself establish intention, causation, normativity, or theological meaning.

---

# 2. Core typed objects

Use a type only when the text supports it.

```math
S_t = \text{state described at time / stage }t
```

```math
R_t = \text{representation, distinction, category, or represented rule}
```

```math
\hat P_t = \text{prediction, prospective claim, or represented future consequence}
```

```math
A_t = \text{action or transformation}
```

```math
C_{t+1} = \text{observed / narrated consequence}
```

```math
\Pi_{t+1} = \text{provenance or causal attribution supplied by the text}
```

```math
\mathcal A(S_t) = \text{available / represented action structure from state }S_t
```

```math
\mathcal P(S_t) = \text{actions explicitly permitted in state }S_t
```

```math
\mathcal F_H(S_t) = \text{reachable future structure from }S_t\text{ over horizon }H
```

When useful, distinguish an utterance or instruction from its subsequent transformation:

```math
U_t = \text{textually reported utterance / instruction}
```

The neutral first-pass relation is:

```math
U_t \rightarrow \text{subsequent narrated transition}
```

not automatically:

```math
U_t \equiv \text{complete causal mechanism}.
```

Likewise:

```math
\boxed{\mathcal A(S_t) \neq \mathcal P(S_t)}
```

and:

```math
\boxed{\mathcal P(S_t) \neq \hat P_t.}
```

---

# 3. Non-collapse rules

Preserve these distinctions unless the text itself supplies a bridge:

```math
\boxed{R_t \neq S_{t+1}}
```

```math
\boxed{\hat P_t \neq C_{t+1}}
```

```math
\boxed{C_{t+1} \neq \Pi_{t+1}}
```

```math
\boxed{S_{t+1} \neq \mathcal A(S_{t+1})}
```

```math
\boxed{\mathcal A(S_t) \neq \mathcal P(S_t)}
```

```math
\boxed{\mathcal P(S_t) \neq \hat P_t}
```

```math
\boxed{\mathcal A(S_t) \neq \mathcal F_H(S_t)}
```

General reading rule:

> **Do not infer a state transition from a representation transition, or a causal explanation from an observed consequence, unless the text supplies the bridge.**

---

# 4. Structural operation vocabulary

The labels below are descriptive conveniences, not claims about authorial intent.

- **STATE** — condition of the narrated system.
- **DISTINCTION** — separation of previously jointly described elements.
- **NAMING** — assignment of a textual label.
- **CLASSIFICATION** — assignment to a type or category.
- **TRANSFORMATION** — narrated change from one state to another.
- **RELATION** — link between entities, classes, locations, roles, or resources.
- **ROLE** — functional or authority relation assigned to an entity.
- **RECURRENCE** — structure that reproduces or repeats over time.
- **TEMPORAL INDEX** — ordering, cycle, duration, season, day, generation, or horizon marker.
- **PREDICTION** — represented prospective consequence or future state.
- **CONSEQUENCE** — later narrated state following an action or event.
- **PROVENANCE** — textual attribution of source, speaker, cause, lineage, or responsibility.
- **EVALUATION** — explicit positive/negative assessment of a state, action, or consequence.
- **AVAILABLE ACTION** — action represented as an executable or conditionally reachable branch.
- **PERMISSION** — explicit normative allowance or prohibition associated with an action.
- **ACTION-SPACE CHANGE** — change in what actions are available or forbidden.
- **FUTURE-SPACE CHANGE** — change in which future trajectories are reachable.

Do not create a type simply to fill a template.

---

# 5. Evidence / interpretation labels

Every strong statement should be classifiable as one of:

### TEXTUAL

Directly stated or directly observable in the passage.

### STRUCTURAL

A low-assumption formal description of textual relations.

### INTERPRETIVE

A stronger hypothesis about what the structure means, why it exists, or what it teaches.

### OPEN

The text does not identify the answer, multiple parses remain live, or the needed bridge is absent.

Prefer `OPEN` over invented completion.

---

# 6. Chapter template

Each chapter should normally contain:

1. **Scope and boundary**.
2. **Surface anchors**.
3. **Optional plain rendering**.
4. **Typed parse**.
5. **Transition graph**.
6. **Future-space effects**.
7. **Non-inferences**.
8. **Information-preservation candidate**.
9. **Open questions**.

The canonical source for every chapter remains the verse corpus; plain renderings and chapter notes are derived aids.

---

# 7. Relation to causal displacement

A narrated transition may motivate a counterfactual question such as:

```math
\Phi_H
=
D_{\rm KL}\!\left(
P(X_{t:t+H}\mid do(Y=1),C)
\middle\|
P(X_{t:t+H}\mid do(Y=0),C)
\right).
```

But a biblical narrative normally does **not** provide the matched counterfactual distribution needed to estimate this quantity.

Therefore the text can identify candidate causal transitions without by itself establishing numerical causal displacement.

The weaker structural question is:

```math
\boxed{\textbf{Which futures became possible or impossible because this changed?}}
```

---

# 8. Claim discipline

Do not claim merely from a structural resemblance:

- that the Bible is literally a machine-learning system;
- that ancient authors intended ML concepts;
- that a structural parse establishes a theological doctrine;
- that narrative sequence alone proves causation;
- that repeated language proves an engineered error-correcting code;
- that a named category is ontologically exhaustive;
- that an explicit evaluation supplies a universal value function;
- that a present-day interpretation recovers the historical generating process;
- that one chapter's structural grammar must govern every later genre;
- that physical availability, textual availability, permission, and prediction are interchangeable;
- that a symbol may be introduced merely because it would make the formalism look complete;
- that a mechanical annotation is evidence for an unstated interpretation.

The method is successful when it makes the text **more legible while preserving uncertainty**, not when it forces every passage into one modern theory.
