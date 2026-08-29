#!/usr/bin/env python3
"""Self-test prospective temporal separation and A/B/C compatibility."""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
if str(PARENT) not in sys.path:
    sys.path.insert(0, str(PARENT))

from evaluate import score
from model import derive_gold
from policies import DependencyOnlyMemory, SourceProvenanceMemory, WarrantLineageMemory
from history_generator import build_history
from freeze_history import freeze_history, verify_freeze
from select_defeater import attach_defeater, candidate_defeaters, select_after_freeze


def main() -> int:
    history = build_history(101)
    assert "defeater_visible" not in history
    assert "defeater_gold" not in history
    frozen = freeze_history(history)
    assert verify_freeze(frozen)
    digest = frozen["history_sha256"]

    candidates = candidate_defeaters(frozen["world"])
    families = {c["family"] for c in candidates}
    required = {
        "alternate_support", "sole_support", "scope_only", "operational_null",
        "instance_not_operator", "operator_invalid", "route_locked",
    }
    assert required <= families, families

    # Different post-freeze seeds can attack the same already-frozen history differently.
    selections = [select_after_freeze(frozen, s) for s in range(40)]
    selected_families = {s["family"] for s in selections}
    assert len(selected_families) >= 4
    assert all(s["history_sha256"] == digest for s in selections)
    assert verify_freeze(frozen), "post-freeze selection mutated the frozen history"

    expected_now = frozen["present_outputs"]
    b_exact = []
    b_nonexact = []

    # Test each constructor-side audit family directly against the same frozen history.
    for c in candidates:
        selection = dict(c)
        selection["selector_seed"] = -1
        selection["history_sha256"] = digest
        world = attach_defeater(frozen, selection)
        gold = derive_gold(world)

        for Policy in [DependencyOnlyMemory, SourceProvenanceMemory, WarrantLineageMemory]:
            policy = Policy(world)
            assert policy.present_outputs() == expected_now

        c_pred = WarrantLineageMemory(world).reassess(world["defeater_visible"])
        assert score(gold, c_pred)["exact"], c["family"]

        b_pred = SourceProvenanceMemory(world).reassess(world["defeater_visible"])
        if score(gold, b_pred)["exact"]:
            b_exact.append(c["family"])
        else:
            b_nonexact.append(c["family"])

    assert b_exact, "B should be sufficient on at least one prospective correction"
    assert b_nonexact, "B should be insufficient on at least one prospective correction"

    print(
        "PASS: history contains no future defeater; freeze digest remains stable; "
        "multiple correction families can be selected only after freeze; A/B/C share "
        "the same pre-defeater outputs; C matches evaluator gold as engineering upper bound; "
        "B is sufficient on some post-freeze corrections and insufficient on others."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
