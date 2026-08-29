#!/usr/bin/env python3
"""Instrument tests for the research-memory engineering prototype."""
from __future__ import annotations

from model import derive_gold
from policies import DependencyOnlyMemory, SourceProvenanceMemory, WarrantLineageMemory
from scenarios import get
from evaluate import score


def main() -> int:
    alt = get("alternate_support")
    gold_alt = derive_gold(alt)
    c_alt = WarrantLineageMemory(alt).reassess(alt["defeater_visible"])
    assert score(gold_alt, c_alt)["exact"]
    assert "K3" in c_alt["retained_claims"]
    assert any(x["claim"] == "K3" for x in c_alt["removed_warrant_paths"])

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
    failures_b = 0
    for name in [
        "alternate_support", "sole_support", "scope_only", "operational_null",
        "instance_not_operator", "operator_invalid", "route_locked"
    ]:
        w = get(name)
        g = derive_gold(w)
        if not score(g, DependencyOnlyMemory(w).reassess(w["defeater_visible"]))["exact"]:
            failures_a += 1
        if not score(g, SourceProvenanceMemory(w).reassess(w["defeater_visible"]))["exact"]:
            failures_b += 1
    assert failures_a >= 1
    assert failures_b >= 1

    print(
        "PASS: warrant-lineage policy matches gold across paired cases; "
        "alternate support, sole support, scope narrowing, operational null, "
        "instance/operator separation, operator invalidity, and route-locked propagation "
        "are discriminated; cheaper baselines fail at least one case."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
