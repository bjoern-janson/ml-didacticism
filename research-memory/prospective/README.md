# Prospective Research Memory — Accumulate → Freeze → Defeat

**Status:** ENGINEERING PROTOTYPE / TEMPORAL-SEPARATION INSTRUMENT / NON-EVIDENTIAL / NOT L2 / NOT L3

This directory changes one thing relative to the initial `research-memory/` scaffold:

```math
\boxed{
\textbf{accumulate first}
\rightarrow
\textbf{freeze}
\rightarrow
\textbf{select the defeater only afterward}.
}
```

The purpose is to test whether the A/B/C memory distinction survives prospective accumulation rather than only replaying a scenario whose future failure was already built into the case object.

It does **not** create constructor independence. The generator and post-freeze selector are still authored inside this repository.

So:

```math
\boxed{
\text{temporal separation}
\neq
\text{constructor independence}
\neq
L_2\text{ evidence}.
}
```

The existing `frontier/benchmark_nucleus/l2_constructor/ADMISSION_GATE.md` remains binding.

---

## 1. Causal sequence

The engineering flow is:

```text
history_generator.py
        ↓
prospective research history
        ↓
freeze_history.py
        ↓
SHA-256-bound frozen history
        ↓
select_defeater.py
        ↓
post-freeze defeater
        ↓
A / B / C reassess
        ↓
private gold comparison
```

The history object contains no:

```text
defeater_visible
defeater_gold
future_defeater
candidate_defeaters
```

before freeze.

The freeze records:

```text
history_sha256
claim_count
transformation_count
present_outputs
exact frozen world
```

Only after that digest exists may a selector choose a later audit result.

This protects:

```math
\boxed{
\textbf{the accumulated memory cannot adapt to the particular future defeater selected for the run.}
}
```

It does not protect against the broader fact that the internal generator was designed by the same research program.

---

## 2. A/B/C remain unchanged

This directory imports the existing policies without modifying them:

```math
\boxed{
\begin{aligned}
A &: \text{dependency only}\\
B &: A+\text{source provenance}\\
C &: B+\text{transformation/warrant lineage}.
\end{aligned}}
```

The prospective layer changes **history construction and temporal ordering**, not the correction logic.

All three must expose the same currently warranted outputs before the post-freeze defeater:

```math
\boxed{
V_{\rm now}(A)
\approx
V_{\rm now}(B)
\approx
V_{\rm now}(C)
}
```

at the resolution of the notebook's present-output check.

---

## 3. Prospective history

`history_generator.py` builds one small research history with several simultaneously present structures:

```text
same-operator instances
independent support
ordinary propagation
provenance-locked propagation
broad-scope authority
operational-only use
downstream synthesis
```

These structures accumulate before any future audit target is selected.

A seed changes the interleaving of independent work without choosing the later defeater.

The resulting history is intentionally small. This stage tests temporal separation, not scale.

---

## 4. Post-freeze defeater selection

`select_defeater.py` inspects only the already-frozen history and derives a set of eligible future audits.

Current constructor-side audit families include:

```text
alternate support
sole support
scope-only correction
operational null
instance-not-operator
operator invalidity
provenance-locked propagation
```

A separate `selector_seed` chooses among them **after** the freeze hash exists.

The same frozen history can therefore face materially different later corrections without being regenerated.

This gives the useful engineering distinction:

```math
\boxed{
\text{same accumulated history}
+
\text{different later defeater}
\rightarrow
\text{different correct authority delta}.
}
```

The family label is constructor-side audit metadata. It is not intended as learner input in a future admitted experiment.

---

## 5. Why this is stronger than the handcrafted matrix

The original scenario matrix demonstrates that different retained memory structures can produce different correction behavior.

The prospective version adds:

```math
\boxed{
\textbf{the memory state exists before the experiment knows which authority path will later be attacked.}
}
```

That removes one easy temporal circularity:

```text
design exact history around future defeater
→ preserve exactly what the future test needs
→ call preservation capability
```

The remaining circularity is larger:

```text
internal team designs history family
+ internal team designs selector family
```

which is why this artifact remains non-evidential.

---

## 6. Run

Generate history:

```bash
python research-memory/prospective/history_generator.py \
  --seed 101 \
  --out /tmp/history.json
```

Freeze it:

```bash
python research-memory/prospective/freeze_history.py \
  /tmp/history.json \
  /tmp/freeze.json
```

Only afterward select a future defeater:

```bash
python research-memory/prospective/select_defeater.py \
  /tmp/freeze.json \
  --selector-seed 7 \
  --out /tmp/defeater.json
```

Or run the whole engineering pipeline:

```bash
python research-memory/prospective/run_prospective.py \
  --history-seed 101 \
  --selector-seed 7
```

Instrument test:

```bash
python research-memory/prospective/self_test.py
```

Expected:

```text
PASS: history contains no future defeater; freeze digest remains stable;
multiple correction families can be selected only after freeze; A/B/C share
the same pre-defeater outputs; C matches evaluator gold as engineering upper
bound; B is sufficient on some post-freeze corrections and insufficient on others.
```

---

## 7. What this stage earns

It may establish only engineering facts about the scaffold:

```text
a research history can be accumulated without a selected future defeater;
the exact pre-defeater state can be frozen and hash-bound;
different future defeaters can be selected against the same frozen history;
the existing A/B/C policies can consume that same history;
their present outputs can be matched before contradiction;
their correction deltas can then be compared.
```

It does **not** establish:

```text
that a learner can infer warrant structure;
that C is superior in real research;
that the internal history generator is independent;
that the post-freeze selector is independent;
that L2 is admitted;
that L3 may begin;
that corrigibility debt exists.
```

---

## 8. Current scientific wall

The next authority-bearing transition is still external:

```math
\boxed{
\text{independent constructor}
\rightarrow
\text{unknown prospective history}
\rightarrow
\text{freeze}
\rightarrow
\text{independent defeater}
\rightarrow
\text{prospective learner correction}
\rightarrow
\text{private gold}.
}
```

Until then:

```text
L2 = UNADMITTED
L3 = BLOCKED
```

The prospective notebook is an engineering bridge, not a promotion.

---

## 9. Stopping rule

Do not add graph-scale L3 machinery here.

Do not add compression variants `C0...C4` merely because they are easy to code.

The next useful internal question is whether this temporal separation reveals implementation failures or whether A/B/C remain distinguishable under prospectively accumulated histories.

The next scientifically meaningful question requires outside construction pressure.

```math
\boxed{
\textbf{Let the system live with its accumulated reasons before choosing which one reality will later break.}
}
```
