# Structural Decoding Method

**Status:** working method / revisable / not a theological claim

This project uses modern ML, causal, temporal, and state-transition vocabulary to expose information structure in the King James Bible without pretending that the vocabulary is the text's own theory.

The primary question is:

> **What information structure is this text preserving?**

The governing boundary is:

```math
\boxed{\text{TEXT} \neq \text{STRUCTURAL PARSE} \neq \text{INTERPRETATION}}
```

A structural parse may be useful while still being incomplete, contestable, or non-unique.

---

# 1. Decoding pipeline

```math
\boxed{
\text{KJV surface text}
\rightarrow
\text{modern plain rendering}
\rightarrow
\text{typed structural parse}
\rightarrow
\text{causal / temporal relations}
\rightarrow
\text{bounded interpretation}
}
```

The plain rendering is not intended to replace the KJV. It only reduces surface-language friction.

The structural parse is not intended to settle theology. It identifies observable textual relations before stronger interpretation.

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
\mathcal A(S_t) = \text{available action structure from state }S_t
```

```math
\mathcal F_H(S_t) = \text{reachable future structure from }S_t\text{ over horizon }H
```

When useful, distinguish an utterance or instruction from its subsequent transformation rather than treating speech as the mechanism by assumption:

```math
U_t = \text{textually reported utterance / instruction}
```

Then the neutral first-pass relation is:

```math
U_t \rightarrow \text{subsequent narrated transition}
```

not automatically:

```math
U_t \equiv \text{complete causal mechanism}.
```

---

# 3. Non-collapse rules

Preserve these distinctions unless the text itself supplies a bridge:

```math
\boxed{R_t \neq S_{t+1}}
```

A representation can change without the represented world changing.

```math
\boxed{\hat P_t \neq C_{t+1}}
```

A prediction is not the consequence that later occurs.

```math
\boxed{C_{t+1} \neq \Pi_{t+1}}
```

What happened is not identical to an explanation of why it happened.

```math
\boxed{S_{t+1} \neq \mathcal A(S_{t+1})}
```

A state description is not identical to the actions available from that state.

```math
\boxed{\mathcal A(S_t) \neq \mathcal F_H(S_t)}
```

Available actions are not identical to the futures reachable through their consequences.

General reading rule:

> **Do not infer a state transition from a representation transition, or a causal explanation from an observed consequence, unless the text supplies the bridge.**

---

# 4. Structural operation vocabulary

The following labels are descriptive conveniences, not claims about authorial intent.

- **STATE** — a condition of the narrated system.
- **DISTINCTION** — separation of previously undifferentiated or jointly described elements.
- **NAMING** — assignment of a textual label.
- **CLASSIFICATION** — assignment to a type or category.
- **TRANSFORMATION** — narrated change from one state to another.
- **RELATION** — link between entities, classes, locations, roles, or resources.
- **ROLE** — functional or authority relation assigned to an entity.
- **RECURRENCE** — structure that reproduces or repeats over time.
- **TEMPORAL INDEX** — explicit ordering, cycle, duration, season, day, generation, or horizon marker.
- **PREDICTION** — represented prospective consequence or future state.
- **CONSEQUENCE** — later narrated state following an action or event.
- **PROVENANCE** — textual attribution of source, speaker, cause, lineage, or responsibility.
- **EVALUATION** — explicit positive/negative assessment of a state, action, or consequence.
- **ACTION-SPACE CHANGE** — change in what actions are available or forbidden.
- **FUTURE-SPACE CHANGE** — change in which future trajectories are reachable.

Do not create a type simply to fill a template.

---

# 5. Evidence / interpretation labels

Every strong statement should be mentally classifiable as one of:

### TEXTUAL

Directly stated or directly observable in the passage.

### STRUCTURAL

A low-assumption formal description of textual relations.

### INTERPRETIVE

A stronger hypothesis about what the structure means, why it exists, or what it teaches.

### OPEN

The text does not identify the answer, multiple parses remain live, or the needed bridge is absent.

The project should prefer `OPEN` over invented completion.

---

# 6. Chapter template

Each chapter should normally contain:

1. **Scope and boundary** — what is being parsed and what is not being claimed.
2. **Surface anchors** — short KJV phrases or verse references sufficient to locate the structure.
3. **Plain rendering** — minimal modern-language restatement.
4. **Typed parse** — states, distinctions, actions, predictions, consequences, relations, provenance, evaluation.
5. **Transition graph** — compressed sequence of changes.
6. **Future-space effects** — where the passage changes available actions or reachable futures.
7. **Non-inferences** — tempting conclusions the text does not yet license.
8. **Information-preservation candidate** — the smallest structural pattern apparently being preserved.
9. **Open questions** — ambiguities to carry forward rather than resolve by assumption.

---

# 7. Relation to causal displacement

A narrated transition may eventually motivate a counterfactual question such as:

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

The useful structural question is weaker:

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
- that one chapter's structural grammar must govern every later genre.

The method is successful when it makes the text **more legible while preserving uncertainty**, not when it forces every passage into one modern theory.