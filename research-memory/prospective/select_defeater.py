#!/usr/bin/env python3
"""Select a defeater only after a prospective history has been frozen.

This is still an internally authored engineering selector, not an independent L2
constructor. Its only purpose is temporal separation: accumulation cannot adapt to
the selected future attack.
"""
from __future__ import annotations

import argparse
import json
import random
from copy import deepcopy
from pathlib import Path
from typing import Mapping

from freeze_history import verify_freeze


def _epistemic(t: Mapping) -> bool:
    return t.get("authority_kind", "epistemic") == "epistemic"


def candidate_defeaters(world: Mapping) -> list[dict]:
    ts = list(world["transformations"])
    by_id = {t["id"]: t for t in ts}
    out_to_ts: dict[str, list[dict]] = {}
    op_to_ts: dict[str, list[dict]] = {}
    for t in ts:
        out_to_ts.setdefault(t["output"], []).append(t)
        op_to_ts.setdefault(t["operator"], []).append(t)

    candidates: list[dict] = []

    for t in ts:
        if not _epistemic(t):
            continue
        alternatives = [x for x in out_to_ts[t["output"]] if x["id"] != t["id"] and _epistemic(x)]
        if alternatives:
            candidates.append({
                "family": "alternate_support",
                "visible": {"target": t["id"], "finding": "post_freeze_audit_invalidates_recorded_event"},
                "gold": {"kind": "INSTANCE_APPLICABILITY", "target_instance": t["id"]},
            })

    for t in ts:
        if _epistemic(t) and len([x for x in out_to_ts[t["output"]] if _epistemic(x)]) == 1:
            if t["operator"] not in {"route_locked", "scope_promote"}:
                candidates.append({
                    "family": "sole_support",
                    "visible": {"target": t["id"], "finding": "post_freeze_audit_invalidates_recorded_event"},
                    "gold": {"kind": "INSTANCE_APPLICABILITY", "target_instance": t["id"]},
                })
                break

    broad = next((t for t in ts if _epistemic(t) and t.get("authority_scope") == "S_BROAD"), None)
    if broad:
        candidates.append({
            "family": "scope_only",
            "visible": {
                "target": broad["id"],
                "finding": "post_freeze_audit_limits_recorded_event_scope",
                "new_scope": "S_NARROW",
            },
            "gold": {
                "kind": "SCOPE_NARROW",
                "target_instance": broad["id"],
                "new_scope": "S_NARROW",
            },
        })

    operational = next((t for t in ts if not _epistemic(t)), None)
    if operational:
        candidates.append({
            "family": "operational_null",
            "visible": {"target": operational["id"], "finding": "post_freeze_audit_invalidates_recorded_event"},
            "gold": {"kind": "OPERATIONAL_ONLY", "target_instance": operational["id"]},
        })

    repeated_instance = next(
        (t for t in ts if _epistemic(t) and len([x for x in op_to_ts[t["operator"]] if _epistemic(x)]) > 1),
        None,
    )
    if repeated_instance:
        candidates.append({
            "family": "instance_not_operator",
            "visible": {"target": repeated_instance["id"], "finding": "post_freeze_audit_invalidates_recorded_event"},
            "gold": {"kind": "INSTANCE_APPLICABILITY", "target_instance": repeated_instance["id"]},
        })

    repeated_operator = next(
        (op for op, xs in op_to_ts.items() if len([x for x in xs if _epistemic(x)]) > 1),
        None,
    )
    if repeated_operator:
        candidates.append({
            "family": "operator_invalid",
            "visible": {"target": f"operator:{repeated_operator}", "finding": "post_freeze_audit_invalidates_operator"},
            "gold": {"kind": "OPERATOR_VALIDITY", "target_operator": repeated_operator},
        })

    locked = next((t for t in ts if _epistemic(t) and t.get("source_binding")), None)
    if locked and locked["source_binding"] in by_id:
        source_tid = locked["source_binding"]
        candidates.append({
            "family": "route_locked",
            "visible": {"target": source_tid, "finding": "post_freeze_audit_invalidates_recorded_event"},
            "gold": {"kind": "INSTANCE_APPLICABILITY", "target_instance": source_tid},
        })

    # Keep family labels even when two audit families select the same concrete
    # authority change. They are constructor-side audit classes, not learner inputs.
    return candidates


def select_after_freeze(freeze_bundle: Mapping, selector_seed: int) -> dict:
    if not verify_freeze(freeze_bundle):
        raise ValueError("freeze digest does not match frozen history")
    candidates = candidate_defeaters(freeze_bundle["world"])
    if not candidates:
        raise ValueError("no eligible post-freeze defeaters")
    rng = random.Random(selector_seed)
    selected = deepcopy(rng.choice(candidates))
    selected["selector_seed"] = selector_seed
    selected["history_sha256"] = freeze_bundle["history_sha256"]
    return selected


def attach_defeater(freeze_bundle: Mapping, selection: Mapping) -> dict:
    if selection["history_sha256"] != freeze_bundle["history_sha256"]:
        raise ValueError("defeater selected against a different frozen history")
    world = deepcopy(freeze_bundle["world"])
    world["defeater_visible"] = deepcopy(selection["visible"])
    world["defeater_gold"] = deepcopy(selection["gold"])
    world["post_freeze_selector_seed"] = selection["selector_seed"]
    return world


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("freeze", type=Path)
    ap.add_argument("--selector-seed", type=int, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    bundle = json.loads(args.freeze.read_text())
    selected = select_after_freeze(bundle, args.selector_seed)
    args.out.write_text(json.dumps(selected, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
