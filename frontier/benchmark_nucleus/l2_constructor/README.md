# L2 Constructor Prototype — Hidden World → Warrant Inference

**Status:** TOY / CONSTRUCTOR PROTOTYPE / UNADMITTED / NON-EVIDENTIAL

This directory advances the benchmark instrument from `L0/L1` toward the admission burden for `L2`.

It does **not** show that a learner possesses correction-local reasoning.

The ladder remains:

```math
\boxed{
\begin{aligned}
L_0 &: \text{failure/correction distinction is operationalizable}\\
L_1 &: \text{an evaluator can discriminate correction classes}\\
L_2 &: \text{a learner can infer affected authority from hidden independent structure}\\
L_3 &: \text{that capability remains warrant-local as structure compounds}
\end{aligned}}
```

`L0/L1` are instrument properties. `L2/L3` are learner properties.

```math
\boxed{\text{benchmark works}\not\Rightarrow\text{learner has benchmarked capability}.}
```

## Causal firewall

The constructor separates:

```text
construct_world.py
    ↓
private_world.json
    ├──────────────→ derive_gold.py → gold.json
    │
    └→ learner projection → learner_view.json → learner
                                               ↓
                                         frozen prediction
                                               ↓
gold.json ───────────────────────────────→ score_l2.py
```

The learner-facing projection does **not** contain:

```text
gold active warrant paths
gold affected-authority set
gold authority-active flags
gold defeater locus
hidden scenario label
```

Instead it contains a synthetic event/procedure history, pre-defeater observations, operator semantics, and a new defeater observation.

The intended relation is:

```math
\boxed{
G^\star_{\rm world}
\rightarrow
E_{\rm observed}
\rightarrow
\widehat G_{\rm warrant}
}
```

while the evaluator privately derives:

```math
\boxed{
G^\star_{\rm world}
\rightarrow
G^\star_{\rm warrant}.
}
```

This is stronger than handing the learner `G^\star_{\rm warrant}` and asking it to traverse the answer graph.

## What the learner must predict

The required output contains:

```text
defeater_locus
affected_authority_instances
claim_actions
active_warrant_paths
reason_edges
history_preserved_instances
```

The `reason_edges` requirement protects:

```math
\boxed{\text{correct affected set}\neq\text{correctly localized reason}.}
```

A learner must expose whether it thinks the defeater attacked an application, an authority path, or no epistemic authority at all.

The gold also keeps two different objects separate:

```math
\boxed{
\text{direct defeater locus}
\neq
\text{full affected authority-instance set}.
}
```

A directly invalidated application can remove authority from a later provenance-locked transformation even when that later instance was not itself the direct target of the new evidence.

## Two constructor scenarios

### `application_defeat`

The hidden world contains:

- two realized instances of the same `combine_v1` operator;
- independent support for one output;
- a downstream route that can survive through alternate warrant;
- a route-locked descendant that specifically depends on the defeated instance's provenance;
- operational-use events that do not transfer warrant.

The defeater changes one application condition only.

The correct correction must distinguish:

```math
\boxed{
\text{operator identity}
\neq
\text{application instance}
\neq
\text{instance-specific authority}.
}
```

### `null_operational`

A real defeater changes a condition on an event that was operational only and transferred no epistemic authority.

Therefore:

```math
\boxed{
\text{defeater arrives}
\land
\text{no authority path is defeated}
\Rightarrow
\text{no epistemic reopening}.
}
```

This null prevents the benchmark from rewarding generic responsiveness.

The response family is therefore able to distinguish:

```math
\boxed{
\text{under-react}
\;|\;
\text{over-react}
\;|\;
\text{globalize}
\;|\;
\text{locally correct}
\;|\;
\text{appropriately retain}.
}
```

## Run the prototype

Construct a world:

```bash
python frontier/benchmark_nucleus/l2_constructor/construct_world.py \
  --seed 101 \
  --scenario application_defeat \
  --out /tmp/l2_case
```

Derive private gold:

```bash
python frontier/benchmark_nucleus/l2_constructor/derive_gold.py \
  /tmp/l2_case/private_world.json \
  /tmp/l2_case/gold.json
```

Score a frozen learner prediction:

```bash
python frontier/benchmark_nucleus/l2_constructor/score_l2.py \
  /tmp/l2_case/gold.json \
  prediction.json
```

Instrument self-test:

```bash
python frontier/benchmark_nucleus/l2_constructor/self_test.py
```

Expected:

```text
PASS: learner projection hides scenario/gold authority fields; direct defeater locus is separated from full affected authority set; application-local oracle passes; undercorrection/globalization fail; null RETAIN passes and overreaction fails.
```

## Why this is still not admitted L2

This constructor is public, deterministic, narrow, and authored inside the same research program.

Therefore it does **not** yet satisfy the strongest independence burden for a scientific learner evaluation.

A learner with access to the constructor implementation could reverse-engineer its hypothesis family or output grammar.

Admission still requires a stronger causal cut:

```math
\boxed{
G^\star_{\rm warrant}\perp G_{\rm learner}
}
```

and, operationally:

```text
independent constructor / curator
        ↓
held-out world family
        ↓
learner observations only
        ↓
learner prediction frozen
        ↓
private gold comparison
```

The constructor must not quietly smuggle the answer family through a narrow world grammar.

So:

```math
\boxed{
\text{constructor prototype}
\neq
\text{independent admitted constructor}
\neq
L_2\text{ evidence}.
}
```

## No scaling yet

Do not move to `L3` because this prototype exists.

`L3` becomes meaningful only after an `L2` learner evaluation is independently admitted.

The later scaling experiment should vary:

```math
\boxed{
(depth,\ branching,\ alternate\ warrant,\ lineage\ compression)
}
```

and hold the true affected authority cone approximately fixed while total accumulated structure grows:

```math
\boxed{
|\mathcal E|\uparrow
\qquad
|A_d^\star|\approx const.
}
```

Then test whether correction burden follows:

```math
\boxed{|A_d^\star|}
```

rather than:

```math
\boxed{|\mathcal E|}.
```

For now:

```math
\boxed{\textbf{First make the correction test real. Then make the learner earn it. Then make it survive scale.}}
```
