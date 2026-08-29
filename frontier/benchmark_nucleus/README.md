# Tiny Benchmark Nucleus — Transformation-Level Correction Locality

**Status:** TOY / UNADMITTED / NON-EVIDENTIAL / MECHANISM TEST ONLY

This directory implements the smallest executable witness currently needed to pressure one frontier mechanism:

```math
\boxed{
\text{transformation naturalization}
\rightarrow
\text{authority-path loss}
\rightarrow
\text{correction non-locality}.
}
```

It does **not** create `T11`, does not move `T10.002`, does not validate corrigibility debt, and does not modify AG/1.

The purpose is narrower:

> Can an evaluator distinguish correction that withdraws exactly the authority carried by a defeated transformation instance from undercorrection, downstream deletion, and operator-global overcorrection?

## Core object

The toy case treats a realized transformation instance as an addressable warrant-bearing record:

```math
\boxed{
\tau_i=
\langle
\phi,\ inputs,\ output,\ conditions,\ scope,\ provenance,\ warrant
\rangle.
}
```

Protect the non-collapse:

```math
\boxed{
REALIZED(\tau_i)
\neq
VALID(\phi)
\neq
APPLICABLE(\tau_i)
\neq
AUTHORIZED(\tau_i,S)
\neq
TRUE(output(\tau_i)).
}
```

No term here is promoted to an AG/1 primitive.

## Case 001

`cases/case_001.json` contains two realized instances of the same operator `combine_v1`.

The target instance is:

```text
tau_A: K1, K2 --combine_v1 under C_A--> K3
```

An independent route also warrants `K3`:

```text
tau_B: K7 --independent_support--> K3
```

A second `combine_v1` instance is elsewhere:

```text
tau_F: K9, K10 --combine_v1 under C_F--> K11
```

The externally specified defeater says only:

```math
\boxed{\neg Applicable(\tau_A)}
```

It does **not** defeat `K1`, `K2`, `K3`, the operator `combine_v1`, or `tau_F`.

The initial warrant paths are:

```text
K3:  {tau_A} OR {tau_B}
K4:  {tau_A,tau_C} OR {tau_B,tau_C} OR {tau_D}
K5:  {tau_A,tau_E}
K11: {tau_F}
```

The gold correction therefore requires:

```text
tau_A: realized history retained; current authority revoked
tau_F: untouched
K3:    RETAIN via tau_B
K4:    RETAIN via surviving tau_B→tau_C and tau_D paths
K5:    REOPEN because its only warrant path crossed tau_A
K11:   RETAIN
```

This tests four invariants at once:

```math
\boxed{
\text{instance locality}
+
\text{warrant-path locality}
+
\text{independent-support preservation}
+
\text{historical preservation}.
}
```

## Canonical bad baselines

The fixtures intentionally include three failures:

- `ignore_defeater.json` — leaves `tau_A` authority active.
- `delete_downstream.json` — treats dependency as warrant inheritance and overcorrects.
- `global_blacklist_operator.json` — defeats `tau_F` merely because it shares `combine_v1`.

`oracle.json` is the exact toy gold output.

These are **evaluator fixtures**, not learner results.

## Run

Python 3 standard library only:

```bash
python frontier/benchmark_nucleus/self_test.py
```

Expected:

```text
PASS: oracle accepted; undercorrection, subtree overcorrection, and operator-global overcorrection rejected.
```

Inspect any fixture:

```bash
python frontier/benchmark_nucleus/evaluate.py \
  frontier/benchmark_nucleus/cases/case_001.json \
  frontier/benchmark_nucleus/fixtures/oracle.json
```

The evaluator returns:

```text
exact pass/fail
per-claim status checks
per-transformation history/authority checks
active warrant-path exactness
warrant-path precision/recall
five named correction invariants
```

## Why this is not an admitted benchmark

The gold graph is deliberately committed in the repository so the evaluator can be inspected and self-tested. A real learner benchmark must not expose its gold warrant topology this way.

Before admission, the existing frontier requirements still apply, including:

```math
\boxed{
G^\star_{\rm warrant}\perp G_{\rm learner}
}
```

plus precommitted result classes, independently specified defeaters, frozen learner outputs, and controls proving that the correction task actually depends on the challenged warrant structure.

So:

```math
\boxed{
\text{executable nucleus}
\neq
\text{admitted experiment}
\neq
\text{evidence}.
}
```

## Scaling path — deliberately not implemented yet

Do not add depth until the nucleus discriminates the local failure correctly.

The next earned extension would scale chain depth and inject independent support at arbitrary depths, then measure whether correction cost tracks the true warrant cone rather than total accumulated structure.

That future scaling hypothesis is:

```math
\boxed{
\text{transformation compression}
\rightarrow
\text{authority-path loss}
\rightarrow
\text{poorer defect localization}
\rightarrow
\text{less selective correction}.
}
```

For now, stop at the smallest executable witness.

```math
\boxed{
\textbf{What exactly did the defeater invalidate, and can exactly that authority be withdrawn?}
}
```
