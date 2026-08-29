#!/usr/bin/env python3
"""Self-test the L2 constructor/scorer firewall and null behavior."""
from __future__ import annotations

import json

from construct_world import build_world, learner_projection
from derive_gold import derive_gold
from score_l2 import score


FORBIDDEN_VIEW_KEYS = {
    "gold_post_defeater",
    "active_warrant_paths",
    "active_authority_instances",
    "affected_authority_instances",
    "defeater_locus",
}


def oracle_from_gold(g: dict) -> dict:
    return {
        "defeater_locus": g["defeater_locus"],
        "affected_authority_instances": g["affected_authority_instances"],
        "claim_actions": g["claim_actions"],
        "active_warrant_paths": g["active_warrant_paths"],
        "reason_edges": g["reason_edges"],
        "history_preserved_instances": g["history_preserved_instances"],
    }


def assert_view_firewall(view: dict) -> None:
    overlap = FORBIDDEN_VIEW_KEYS & set(view)
    assert not overlap, f"learner view leaks gold keys: {sorted(overlap)}"


def main() -> int:
    world = build_world(101, "application_defeat")
    view = learner_projection(world)
    gold = derive_gold(world)
    assert_view_firewall(view)

    oracle = oracle_from_gold(gold)
    assert score(gold, oracle)["pass"]

    bad_under = json.loads(json.dumps(oracle))
    bad_under["affected_authority_instances"] = []
    assert not score(gold, bad_under)["pass"]

    bad_global = json.loads(json.dumps(oracle))
    same_op = [
        e["id"] for e in world["events"]
        if e["operator"] == "combine_v1"
    ]
    target = gold["affected_authority_instances"][0]
    control = next(t for t in same_op if t != target)
    control_output = next(e["output"] for e in world["events"] if e["id"] == control)
    bad_global["claim_actions"][control_output] = "REOPEN"
    assert not score(gold, bad_global)["pass"]

    null_world = build_world(202, "null_operational")
    null_view = learner_projection(null_world)
    null_gold = derive_gold(null_world)
    assert_view_firewall(null_view)
    assert null_gold["affected_authority_instances"] == []
    assert all(v == "RETAIN" for v in null_gold["claim_actions"].values())
    assert score(null_gold, oracle_from_gold(null_gold))["pass"]

    bad_null = json.loads(json.dumps(oracle_from_gold(null_gold)))
    some_claim = next(iter(bad_null["claim_actions"]))
    bad_null["claim_actions"][some_claim] = "REOPEN"
    assert not score(null_gold, bad_null)["pass"]

    print(
        "PASS: constructor projects learner observations without gold authority fields; "
        "application-local oracle passes; undercorrection/globalization fail; "
        "null HOLD/RETAIN passes and overreaction fails."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
