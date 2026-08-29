#!/usr/bin/env python3
"""Derive private gold warrant topology from a constructed toy world."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Set, Tuple

PathT = Tuple[str, ...]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def event_map(world: dict) -> dict:
    return {e["id"]: e for e in world["events"]}


def post_conditions(world: dict) -> dict:
    c = dict(world["conditions_pre_defeater"])
    d = world["defeater"]
    c[d["condition"]] = d["new_value"]
    return c


def is_evidential(event: dict) -> bool:
    return event["operator"] != "operational_use"


def application_active(event: dict, cond: dict, active_events: Set[str]) -> bool:
    if not is_evidential(event):
        return False
    if not cond.get(event["requirement"], False):
        return False
    if event["operator"] == "route_locked":
        return event["source_binding"] in active_events
    return True


def derive_paths(world: dict) -> tuple[dict[str, Set[PathT]], Set[str]]:
    cond = post_conditions(world)
    events = world["events"]

    produced = {e["output"] for e in events if is_evidential(e)}
    base_claims = set(world["claims"]) - produced
    paths: Dict[str, Set[PathT]] = {k: {()} for k in base_claims}
    active_events: Set[str] = set()

    changed = True
    while changed:
        changed = False
        for e in events:
            if not application_active(e, cond, active_events):
                continue

            if e["operator"] == "route_locked":
                binding = e["source_binding"]
                input_paths = []
                for inp in e["inputs"]:
                    pset = paths.get(inp, set())
                    if inp == e["inputs"][0]:
                        pset = {p for p in pset if binding in p}
                    input_paths.append(pset)
            else:
                input_paths = [paths.get(inp, set()) for inp in e["inputs"]]

            if not input_paths or any(not ps for ps in input_paths):
                continue

            combos = {()}
            for pset in input_paths:
                new = set()
                for a in combos:
                    for b in pset:
                        merged = tuple(dict.fromkeys(a + b))
                        new.add(merged)
                combos = new

            out_paths = {tuple(dict.fromkeys(p + (e["id"],))) for p in combos}
            before = set(paths.get(e["output"], set()))
            after = before | out_paths
            if after != before:
                paths[e["output"]] = after
                changed = True
            if e["id"] not in active_events:
                active_events.add(e["id"])
                changed = True

    clean = {k: {p for p in ps if p} for k, ps in paths.items() if any(p for p in ps)}
    return clean, active_events


def derive_gold(world: dict) -> dict:
    paths, active_events = derive_paths(world)
    cond_after = post_conditions(world)
    defeater_condition = world["defeater"]["condition"]

    matching = [e for e in world["events"] if e["requirement"] == defeater_condition]
    evidential_matching = [e for e in matching if is_evidential(e)]

    if evidential_matching:
        locus = {
            "kind": "applicability",
            "target_instances": sorted(e["id"] for e in evidential_matching),
        }
    else:
        locus = {
            "kind": "operational_only_no_authority",
            "target_instances": sorted(e["id"] for e in matching),
        }

    affected = sorted(
        e["id"] for e in evidential_matching
        if not cond_after.get(e["requirement"], False)
    )

    produced_claims = sorted({e["output"] for e in world["events"] if is_evidential(e)})
    claim_actions = {
        k: ("RETAIN" if paths.get(k) else "REOPEN")
        for k in produced_claims
    }

    reason_edges = []
    for e in matching:
        if is_evidential(e) and not cond_after.get(e["requirement"], False):
            reason_edges.append([defeater_condition, "invalidates_applicability", e["id"]])
            reason_edges.append([e["id"], "withdraws_authority_from", e["output"]])
        elif not is_evidential(e):
            reason_edges.append([defeater_condition, "affects_operational_event_only", e["id"]])

    return {
        "schema": "l2_gold_v0",
        "status": world["status"],
        "seed": world["seed"],
        "scenario": world["scenario"],
        "defeater_locus": locus,
        "affected_authority_instances": affected,
        "claim_actions": claim_actions,
        "active_warrant_paths": {
            k: [list(p) for p in sorted(ps)]
            for k, ps in sorted(paths.items())
            if k in produced_claims
        },
        "reason_edges": sorted(reason_edges),
        "history_preserved_instances": sorted(e["id"] for e in world["events"]),
        "active_authority_instances": sorted(active_events),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("private_world", type=Path)
    p.add_argument("gold", type=Path)
    args = p.parse_args()
    dump(args.gold, derive_gold(load(args.private_world)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
