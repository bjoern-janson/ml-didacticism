#!/usr/bin/env python3
"""Shared world semantics and gold authority accounting for the research-memory prototype.

This module is evaluator-side infrastructure. It is not learner logic.
"""
from __future__ import annotations

from copy import deepcopy
from itertools import product
from typing import Dict, Mapping, Sequence, Set, Tuple

PathT = Tuple[str, ...]


def _dedupe_tuple(items: Sequence[str]) -> PathT:
    return tuple(dict.fromkeys(items))


def is_epistemic(t: Mapping) -> bool:
    return t.get("authority_kind", "epistemic") == "epistemic"


def transformation_index(world: Mapping) -> dict[str, dict]:
    return {t["id"]: dict(t) for t in world["transformations"]}


def base_claim_ids(world: Mapping) -> set[str]:
    produced = {t["output"] for t in world["transformations"] if is_epistemic(t)}
    return set(world["claims"]) - produced


def initial_state(world: Mapping) -> dict:
    return {
        "instance_active": {
            t["id"]: True
            for t in world["transformations"]
            if is_epistemic(t)
        },
        "operator_validity": dict(world.get("operator_validity", {})),
        "scope_override": {},
    }


def apply_defeater(world: Mapping, state: Mapping) -> dict:
    """Apply evaluator-known defeater semantics to an authority state."""
    post = deepcopy(state)
    d = world["defeater_gold"]
    kind = d["kind"]

    if kind == "INSTANCE_APPLICABILITY":
        target = d["target_instance"]
        if target in post["instance_active"]:
            post["instance_active"][target] = False
    elif kind == "OPERATOR_VALIDITY":
        operator = d["target_operator"]
        post["operator_validity"][operator] = False
        for t in world["transformations"]:
            if is_epistemic(t) and t["operator"] == operator:
                post["instance_active"][t["id"]] = False
    elif kind == "SCOPE_NARROW":
        post["scope_override"][d["target_instance"]] = d["new_scope"]
    elif kind == "OPERATIONAL_ONLY":
        pass
    else:
        raise ValueError(f"unknown defeater kind: {kind}")
    return post


def derive_paths(world: Mapping, state: Mapping) -> tuple[dict[str, Set[PathT]], set[str]]:
    """Derive active warrant paths and active epistemic transformation instances."""
    transforms = list(world["transformations"])
    paths: Dict[str, Set[PathT]] = {k: {()} for k in base_claim_ids(world)}
    active_instances: set[str] = set()

    changed = True
    while changed:
        changed = False
        for t in transforms:
            if not is_epistemic(t):
                continue
            if not state["instance_active"].get(t["id"], False):
                continue
            if not state["operator_validity"].get(t["operator"], True):
                continue

            input_paths = []
            for i, inp in enumerate(t["inputs"]):
                pset = set(paths.get(inp, set()))
                binding = t.get("source_binding") if i == 0 else None
                if binding:
                    pset = {p for p in pset if binding in p}
                input_paths.append(pset)

            if not input_paths or any(not p for p in input_paths):
                continue

            combos: set[PathT] = {()}
            for pset in input_paths:
                next_combos: set[PathT] = set()
                for a, b in product(combos, pset):
                    next_combos.add(_dedupe_tuple(a + b))
                combos = next_combos

            out_paths = {_dedupe_tuple(p + (t["id"],)) for p in combos}
            before = set(paths.get(t["output"], set()))
            after = before | out_paths
            if after != before:
                paths[t["output"]] = after
                changed = True
            if t["id"] not in active_instances:
                active_instances.add(t["id"])
                changed = True

    clean = {
        k: {p for p in ps if p}
        for k, ps in paths.items()
        if any(p for p in ps)
    }
    return clean, active_instances


def derive_gold(world: Mapping) -> dict:
    """Derive the typed post-defeater authority delta from full private semantics."""
    pre = initial_state(world)
    post = apply_defeater(world, pre)
    pre_paths, pre_active = derive_paths(world, pre)
    post_paths, post_active = derive_paths(world, post)
    t_index = transformation_index(world)

    d = world["defeater_gold"]
    kind = d["kind"]
    if kind in {"INSTANCE_APPLICABILITY", "SCOPE_NARROW"}:
        direct = [d["target_instance"]]
        locus = {"kind": kind, "target_instances": direct}
    elif kind == "OPERATOR_VALIDITY":
        direct = sorted(
            t["id"] for t in world["transformations"]
            if is_epistemic(t) and t["operator"] == d["target_operator"]
        )
        locus = {"kind": kind, "target_operator": d["target_operator"], "target_instances": direct}
    elif kind == "OPERATIONAL_ONLY":
        direct = [d["target_instance"]]
        locus = {"kind": kind, "target_instances": direct}
    else:
        raise ValueError(kind)

    affected_instances = sorted(pre_active - post_active)
    narrowed = {}
    if kind == "SCOPE_NARROW":
        target = d["target_instance"]
        narrowed[t_index[target]["output"]] = d["new_scope"]

    produced_claims = sorted({t["output"] for t in world["transformations"] if is_epistemic(t)})
    reopened, retained, recompute = [], [], []
    removed_paths = []

    for claim in produced_claims:
        pre_ps = set(pre_paths.get(claim, set()))
        post_ps = set(post_paths.get(claim, set()))
        for p in sorted(pre_ps - post_ps):
            removed_paths.append({"claim": claim, "path": list(p)})
        if claim in narrowed:
            recompute.append(claim)
        elif not post_ps:
            reopened.append(claim)
            if pre_ps:
                recompute.append(claim)
        else:
            retained.append(claim)
            if pre_ps != post_ps:
                recompute.append(claim)

    history = sorted(t["id"] for t in world["transformations"])

    return {
        "scenario_id": world["id"],
        "defeater_locus": locus,
        "affected_authority_instances": affected_instances,
        "removed_warrant_paths": removed_paths,
        "reopened_claims": sorted(reopened),
        "retained_claims": sorted(retained),
        "narrowed_scopes": dict(sorted(narrowed.items())),
        "required_recomputations": sorted(recompute),
        "preserved_history": history,
        "active_warrant_paths": {
            claim: [list(p) for p in sorted(post_paths.get(claim, set()))]
            for claim in produced_claims
        },
    }


def current_outputs(world: Mapping) -> list[str]:
    """Present-task output shared by all policies before a defeater."""
    pre_paths, _ = derive_paths(world, initial_state(world))
    return sorted(k for k, paths in pre_paths.items() if paths)
