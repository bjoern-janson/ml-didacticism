#!/usr/bin/env python3
"""Run the deterministic A/B/C engineering comparison over the small scenario matrix."""
from __future__ import annotations

import json

from evaluate import score
from model import current_outputs, derive_gold
from policies import POLICIES
from scenarios import all_scenarios


def run() -> dict:
    results = []
    for world in all_scenarios():
        expected_now = current_outputs(world)
        policy_now = {}
        for Policy in POLICIES:
            p = Policy(world)
            policy_now[p.name] = p.present_outputs()
        present_equivalent = all(v == expected_now for v in policy_now.values())

        gold = derive_gold(world)
        policies = {}
        for Policy in POLICIES:
            p = Policy(world)
            pred = p.reassess(world["defeater_visible"])
            policies[p.name] = {
                "prediction": pred,
                "metrics": score(gold, pred),
            }

        results.append({
            "scenario_id": world["id"],
            "surface_anomaly": world["surface_anomaly"],
            "present_outputs": expected_now,
            "present_equivalent": present_equivalent,
            "gold": gold,
            "policies": policies,
        })
    return {
        "status": "ENGINEERING_PROTOTYPE_NON_EVIDENTIAL",
        "primary_question": (
            "Does preserving authority-producing lineage improve future selective correction?"
        ),
        "results": results,
    }


def main() -> int:
    data = run()
    print(json.dumps(data, indent=2, sort_keys=True))
    return 0 if all(r["present_equivalent"] for r in data["results"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
