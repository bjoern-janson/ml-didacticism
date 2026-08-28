# T10 Blind Instance 001 — Challenge Result and Pre-Reveal Update

**Protocol:** `transport/10_LEVEL3_BLIND_STRUCTURAL_INVENTION_PROTOCOL.md`  
**Evidence:** `transport/t10/00_BLIND_001_EVIDENCE.md`  
**Candidate:** `transport/t10/01_BLIND_001_CANDIDATE.md`  
**Hidden topology commitment:** `33e69350718d1022dad2b991972e08c486eeb3ea50014147d635953fef2d9737`  
**Status:** CHALLENGE EXECUTED / RESULT FROZEN / HIDDEN TOPOLOGY STILL SEALED

---

# 1. Frozen challenge

The candidate artifact committed these four settings before execution:

```text
Q1: A=0, B= 2, C= 2
Q2: A=0, B= 2, C=-2
Q3: A=0, B= 2, C= 0
Q4: A=0, B= 0, C= 2
```

Candidate prediction for `Y1` residuals:

```text
Q1: -9.0
Q2: +9.0
Q3:  0.0
Q4:  0.0
```

with no new residual predicted for `Y2`.

---

# 2. Returned observations

| query | A | B | C | additive Y1 | observed Y1 | residual Y1 | additive Y2 | observed Y2 | residual Y2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Q1 | 0 | 2 | 2 | 2.4 | -6.6 | -9.0 | -0.2 | -0.2 | 0.0 |
| Q2 | 0 | 2 | -2 | 1.6 | 10.6 | +9.0 | 2.6 | 2.6 | 0.0 |
| Q3 | 0 | 2 | 0 | 2.0 | 2.0 | 0.0 | 1.2 | 1.2 | 0.0 |
| Q4 | 0 | 0 | 2 | 3.4 | 3.4 | 0.0 | -2.4 | -2.4 | 0.0 |

The prospective candidate prediction matches all four returned `Y1` residuals exactly at the exposed resolution.

`Y2` remains exactly on the initial additive model across the challenge.

---

# 3. Pre-reveal update

```text
RETAIN
```

provisionally:

```math
\boxed{
JOINT\_EFFECT(B,C,Y_1)
}
```

with:

```math
\boxed{
\Delta Y_1\approx -2.25BC.
}
```

Reason:

```text
sign reversal under C reversal with B fixed: observed
zero residual when C=0 with B nonzero: observed
zero residual when B=0 with C nonzero: observed
predicted magnitude at |B*C|=4: observed
no unexpected Y2 structure: observed
```

---

# 4. What is not yet claimed

Before hidden-topology reveal, this result supports:

```math
\boxed{
\textbf{the generated structural candidate has survived a prospective discriminating challenge.}
}
```

It does **not** yet establish that the candidate matches the evaluator's committed hidden generating topology.

That comparison is deferred to the reveal phase.
