# T10 Blind Instance 001 — Candidate Structural Invention

**Protocol:** `transport/10_LEVEL3_BLIND_STRUCTURAL_INVENTION_PROTOCOL.md`  
**Evidence:** `transport/t10/00_BLIND_001_EVIDENCE.md`  
**Hidden topology commitment:** `33e69350718d1022dad2b991972e08c486eeb3ea50014147d635953fef2d9737`  
**Status:** CANDIDATE + PROSPECTIVE CHALLENGE FROZEN / CHALLENGE NOT YET EXECUTED

---

# 1. Contradiction

The initial representation is additive and memoryless.

`Y2` matches that representation on every supplied trial.

`Y1` does not.

The nonzero `Y1` residuals show a repeated structure:

```text
B = 0 → residual = 0 across supplied cases
C = 0 → residual = 0 across supplied cases
B and C both nonzero → residual may be nonzero
changing the sign of B while holding C positive changes residual sign
increasing |B*C| increases residual magnitude
```

The current unary relation set does not contain a relation that directly represents this joint dependence.

---

# 2. Generated structural candidate

Generate a new n-ary relation:

```math
\boxed{
JOINT\_EFFECT(B,C,Y_1)
}
```

with the candidate quantitative form:

```math
\boxed{
\Delta Y_1\approx -2.25\,B\,C
}
```

Equivalently, the revised candidate representation is:

```math
Y_1
=
3.0+1.5A-0.5B+0.2C
-2.25BC.
```

`Y2` remains unchanged under this candidate.

This is structurally novel relative to the initial representation because the initial graph contains only separate unary/additive input-output relations. It does not contain a joint `B,C → Y1` interaction.

---

# 3. Why this is not merely a parameter revision

No single coefficient change to:

```text
B → Y1
C → Y1
A → Y1
```

explains all supplied residual structure while preserving the zero-residual cases.

In particular:

```text
B-only coefficient drift
```

would not naturally vanish whenever `C=0` while reappearing with sign/magnitude proportional to `C`.

Likewise:

```text
C-only coefficient drift
```

would not naturally vanish whenever `B=0` while changing sign with `B`.

The repeated pattern therefore motivates a new joint relation rather than a changed value on an existing edge.

---

# 4. Live alternatives retained before challenge

The candidate is not treated as historical truth.

At least these alternatives remain live:

```text
A1 — genuine B×C interaction affecting Y1
A2 — some unrepresented mechanism correlated with B×C but not literally a direct interaction
A3 — measurement/process artifact producing the same residual pattern
```

The challenge is designed to test the specific prospective signature of A1 against shallower single-input alternatives and accidental fit.

---

# 5. Prospective challenge

Execute exactly these four new settings:

```text
Q1: A=0, B= 2, C= 2
Q2: A=0, B= 2, C=-2
Q3: A=0, B= 2, C= 0
Q4: A=0, B= 0, C= 2
```

The candidate predicts:

| query | additive-model Y1 | candidate residual | candidate Y1 | candidate Y2 |
|---|---:|---:|---:|---:|
| Q1 `(0,2,2)` | 2.4 | -9.0 | -6.6 | -0.2 |
| Q2 `(0,2,-2)` | 1.6 | +9.0 | 10.6 | 2.6 |
| Q3 `(0,2,0)` | 2.0 | 0.0 | 2.0 | 1.2 |
| Q4 `(0,0,2)` | 3.4 | 0.0 | 3.4 | -2.4 |

The decisive prospective signature is:

```math
\boxed{
(+B,+C)\rightarrow negative\ residual,
\qquad
(+B,-C)\rightarrow positive\ residual
}
```

with:

```math
\boxed{
C=0\text{ or }B=0\rightarrow residual\approx0.
}
```

This differs from ordinary single-input coefficient drift and from an accidental constant offset.

---

# 6. Retraction / revision condition

Before seeing the challenge result:

```text
RETAIN candidate provisionally
```

only if the new observations exhibit the predicted joint sign/magnitude structure at useful resolution.

```text
RETRACT or materially REVISE
```

if any of the following occurs:

```text
large residual persists when B=0 or C=0;
residual does not reverse sign when C reverses with B fixed;
residual magnitude is materially inconsistent with the predicted B*C dependence;
Y2 develops a new unexplained pattern that changes the topology required.
```

The candidate is therefore falsifiable before challenge execution.
