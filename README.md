# ML Didacticism

A structural reading project for the King James Bible (KJV) using machine-learning, causal, state-transition, representation, and information-processing language as an analytic lens.

The project is **not** a theological replacement, doctrinal paraphrase, or claim that ancient authors intended modern ML concepts.

The core discipline is:

```math
\boxed{\text{TEXT} \neq \text{STRUCTURAL PARSE} \neq \text{INTERPRETATION}}
```

The strongest symbol rule is:

```math
\boxed{\textbf{Every formal symbol must correspond to something actually recoverable from the text.}}
```

If a needed causal, intentional, predictive, normative, or other bridge is absent, mark it **OPEN** rather than completing it by assumption.

The working pipeline is:

```math
\boxed{
\text{KJV surface text}
\rightarrow
\text{plain-language rendering}
\rightarrow
\text{typed structural parse}
\rightarrow
\text{causal / temporal relations}
\rightarrow
\text{bounded interpretation}
}
```

The goal is to ask, passage by passage:

> **What information structure is this text preserving?**

Rather than beginning with a claim about what a passage ultimately means, the first pass separates objects such as:

```math
S_t = \text{state}
```

```math
R_t = \text{representation / represented distinction}
```

```math
\hat P_t = \text{prediction or prospective claim}
```

```math
A_t = \text{action / transformation}
```

```math
C_{t+1} = \text{observed consequence}
```

```math
\Pi_{t+1} = \text{provenance / causal attribution}
```

```math
\mathcal A(S_t) = \text{available / represented action structure}
```

```math
\mathcal P(S_t) = \text{explicitly permitted action structure}
```

```math
\mathcal F_H(S_t) = \text{reachable future structure over horizon }H
```

These types must not be silently collapsed:

```math
\boxed{
R \neq S,
\qquad
\hat P \neq C,
\qquad
C \neq \Pi,
\qquad
S \neq \mathcal A,
\qquad
\mathcal A \neq \mathcal P,
\qquad
\mathcal P \neq \hat P,
\qquad
\mathcal A \neq \mathcal F
}
```

Each bridge must be earned by the text.

## Project structure

- [`docs/STRUCTURAL_DECODING_METHOD.md`](docs/STRUCTURAL_DECODING_METHOD.md) — decoding rules and claim discipline.
- [`genesis/01_GENESIS_01.md`](genesis/01_GENESIS_01.md) — Genesis 1: world-level differentiation, relation, recurrence, and evaluation.
- [`genesis/02_GENESIS_02.md`](genesis/02_GENESIS_02.md) — Genesis 2: agent-environment structure, role, permission, constraint, prospective consequence, and relational reconfiguration.

## Reading rule

Do not infer a state transition from a representation transition, or a causal explanation from an observed consequence, unless the text supplies the bridge.

A useful recurring question is:

```math
\boxed{\textbf{Which futures became possible or impossible because this changed?}}
```

This repository starts from Genesis 1 and proceeds forward.