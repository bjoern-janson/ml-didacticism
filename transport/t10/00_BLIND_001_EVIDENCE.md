# T10 Blind Instance 001 — Initial Evidence Packet

**Protocol:** `transport/10_LEVEL3_BLIND_STRUCTURAL_INVENTION_PROTOCOL.md`  
**Instance:** `T10-BLIND-001`  
**Status:** EVIDENCE FROZEN / HIDDEN TOPOLOGY NOT REVEALED  
**Hidden topology SHA-256:** `33e69350718d1022dad2b991972e08c486eeb3ea50014147d635953fef2d9737`

---

# 1. Initial representation

The learner is given an additive, memoryless model over three controllable inputs and two measured outputs:

```math
Y_1 = 3.0 + 1.5A - 0.5B + 0.2C
```

```math
Y_2 = -1.0 + 0.4A + 1.1B - 0.7C
```

Represented relations:

```text
A → Y1
B → Y1
C → Y1
A → Y2
B → Y2
C → Y2
```

No interaction, latent mediator, history dependence, or measurement-coupling relation is asserted in the initial representation.

The learner may generate such a relation if the evidence earns it.

---

# 2. Allowed challenge interface

The learner may choose **up to four** new control settings:

```text
(A,B,C)
```

with each value drawn from:

```text
{-2,-1,0,1,2}
```

The hidden simulator will return:

```text
Y1,Y2
```

No hidden topology information is available before the candidate and prospective prediction are committed.

---

# 3. Initial evidence

| trial | A | B | C | predicted Y1 | observed Y1 | residual Y1 | predicted Y2 | observed Y2 | residual Y2 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 4.0 | 4.0 | 0.0 | 0.5 | 0.5 | 0.0 |
| 2 | -2 | 2 | 0 | -1.0 | -1.0 | 0.0 | 0.4 | 0.4 | 0.0 |
| 3 | 2 | -1 | 2 | 6.9 | 11.4 | +4.5 | -2.7 | -2.7 | 0.0 |
| 4 | 2 | -2 | 1 | 7.2 | 11.7 | +4.5 | -3.1 | -3.1 | 0.0 |
| 5 | -2 | -2 | 2 | 1.4 | 10.4 | +9.0 | -5.4 | -5.4 | 0.0 |
| 6 | 1 | 0 | 2 | 4.9 | 4.9 | 0.0 | -2.0 | -2.0 | 0.0 |
| 7 | 2 | 0 | 0 | 6.0 | 6.0 | 0.0 | -0.2 | -0.2 | 0.0 |
| 8 | 0 | 1 | 0 | 2.5 | 2.5 | 0.0 | 0.1 | 0.1 | 0.0 |
| 9 | 0 | 0 | 2 | 3.4 | 3.4 | 0.0 | -2.4 | -2.4 | 0.0 |
| 10 | 2 | 2 | 1 | 5.2 | 0.7 | -4.5 | 1.3 | 1.3 | 0.0 |
| 11 | 2 | 0 | -1 | 5.8 | 5.8 | 0.0 | 0.5 | 0.5 | 0.0 |
| 12 | 0 | -2 | 1 | 4.2 | 8.7 | +4.5 | -3.9 | -3.9 | 0.0 |

---

# 4. Binding anti-contamination state

At this commit:

```text
hidden topology: sealed
candidate relation: not yet committed
challenge: not yet selected/executed
challenge result: unavailable
```

The published SHA-256 commits the evaluator to one hidden topology before candidate generation.
