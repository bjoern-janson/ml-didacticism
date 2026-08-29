#!/usr/bin/env python3
"""Instrument tests for the research-memory engineering prototype."""
from __future__ import annotations

from copy import deepcopy

from model import derive_gold
from policies import DependencyOnlyMemory, SourceProvenanceMemory, WarrantLineageMemory
from scenarios import get
from evaluate import score


CASES = [
    "alternate_support",
    "sole_support",
    "scope_only",
    "operational_null",
    "instance_not_operator",
    "operator_invalid",
    "route_locked",
]


def main() -> int:
    alt = get("alternate_support")
    gold_alt = derive_gold(alt)
    c_alt = WarrantLineageMemory(alt).reassess(alt["defeater_visible"])
    alt_score = score(gold_alt, c_alt)
    assert alt_score["exact"]
    assert "K3" in c_alt["retained_claims"]
    assert any(x["claim"] == "K3" for x in c_alt["removed_warrant_paths"])

    # Regression: false retained claims must reduce preservation quality.
    false_retained = deepcopy(c_alt)
    false_retained["retained_claims"].append("K999")
    s = score(gold_alt, false_retained)
    assert s["I_P"] < 1.0
    assert s["retained_precision"] < 1.0
    assert not s["exact"]

    # Regression: invented history must reduce historical-preservation quality.
    false_history = deepcopy(c_alt)
    false_history["preserved_history"].append("tau_extra")
    s = score(gold_alt, false_history)
    assert s["H_P"] < 1.0
    assert s["history_precision"] < 1.0
    assert not s["exact"]

    # Regression: correct action with missing warrant paths is not strict exactness.
    missing_paths = deepcopy(c_alt)
    missing_paths["removed_warrant_paths"] = []
    s = score(gold_alt, missing_paths)
    assert s["action_exact"]
    assert not s["paths_exact"]
    assert s["removed_path_recall"] == 0.0
    assert not s["exact"]

    sole = get("sole_support")
    c_sole = WarrantLineageMemory(sole).reassess(sole["defeater_visible"])
    assert "K3" in c_sole["reopened_claims"]

    scope = get("scope_only")
    c_scope = WarrantLineageMemory(scope).reassess(scope["defeater_visible"])
    assert c_scope["narrowed_scopes"] == {"K3": "S_NARROW"}
    assert "K3" not in c_scope["reopened_claims"]

    null = get("operational_null")
    gold_null = derive_gold(null)
    c_null = WarrantLineageMemory(null).reassess(null["defeater_visible"])
    assert score(gold_null, c_null)["exact"]
    assert c_null["affected_authority_instances"] == []
    assert c_null["reopened_claims"] == []

    inst = get("instance_not_operator")
    c_inst = WarrantLineageMemory(inst).reassess(inst["defeater_visible"])
    assert "K3" in c_inst["reopened_claims"]
    assert "K4" in c_inst["retained_claims"]

    op = get("operator_invalid")
    c_op = WarrantLineageMemory(op).reassess(op["defeater_visible"])
    assert set(c_op["affected_authority_instances"]) == {"tau_A", "tau_F"}
    assert "K3" in c_op["reopened_claims"]
    assert "K4" in c_op["retained_claims"]

    route = get("route_locked")
    gold_route = derive_gold(route)
    c_route = WarrantLineageMemory(route).reassess(route["defeater_visible"])
    assert score(gold_route, c_route)["exact"]
    assert set(c_route["affected_authority_instances"]) == {"tau_A", "tau_E"}
    assert "K3" in c_route["retained_claims"]
    assert "K4" in c_route["retained_claims"]

    failures_a = 0
    b_action_hits = []
    b_action_misses = []
    for name in CASES:
        w = get(name)
        g = derive_gold(w)
        a_score = score(g, DependencyOnlyMemory(w).reassess(w["defeater_visible"]))
        b_score = score(g, SourceProvenanceMemory(w).reassess(w["defeater_visible"]))
        c_score = score(g, WarrantLineageMemory(w).reassess(w["defeater_visible"]))
        assert c_score["exact"], name
        if not a_score["action_exact"]:
            failures_a += 1
        if b_score["action_exact"]:
            b_action_hits.append(name)
        else:
            b_action_misses.append(name)

    assert failures_a >= 1
    assert b_action_hits, "B should choose the correct correction action on at least one case"
    assert b_action_misses, "B should fail the correction action on at least one case"

    print(
        "PASS: strict evaluator penalizes false retention/history and missing warrant paths; "
        "warrant-lineage policy matches strict gold across paired cases; cheaper baselines "
        "remain mixed at the action level rather than being preordained winners or losers."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
