#!/usr/bin/env python3
"""Construct a deterministic toy world and a learner-facing projection.

This is an L2 instrument prototype, not an admitted benchmark.
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path


def dump(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def make_ids(seed: int) -> dict[str, str]:
    rng = random.Random(seed)
    claim_tokens = [f"K{n}" for n in range(1, 14)]
    rng.shuffle(claim_tokens)
    event_tokens = [f"tau_{c}" for c in "ABCDEFGH"]
    rng.shuffle(event_tokens)
    return {
        **{f"k{i+1}": token for i, token in enumerate(claim_tokens)},
        **{f"t{c}": token for c, token in zip("ABCDEFGH", event_tokens)},
    }


def build_world(seed: int, scenario: str) -> dict:
    ids = make_ids(seed)
    k = lambda n: ids[f"k{n}"]
    t = lambda c: ids[f"t{c}"]

    claims = {
        k(1): "calibration record A is valid before run A",
        k(2): "sample A is stable",
        k(3): "measurement M is reliable",
        k(4): "derived estimate Q is usable",
        k(5): "same-run extrapolation R is warranted",
        k(6): "auxiliary assumption for R holds",
        k(7): "independent replication of M succeeds",
        k(8): "independent control directly supports Q",
        k(9): "calibration record F is valid before run F",
        k(10): "sample F is stable",
        k(11): "measurement N is reliable",
        k(12): "dashboard displays M-derived value",
        k(13): "diagnostic log exists",
    }

    events = [
        {
            "id": t("A"), "operator": "combine_v1",
            "inputs": [k(1), k(2)], "output": k(3),
            "requirement": "calibration_A_valid_during_run",
            "scope": "measurement_M_reliability",
            "narrative": "Run A combines calibration record A with sample stability to support M."
        },
        {
            "id": t("B"), "operator": "independent_support",
            "inputs": [k(7)], "output": k(3),
            "requirement": "replication_valid",
            "scope": "measurement_M_reliability",
            "narrative": "An independent replication supports M without using run A."
        },
        {
            "id": t("C"), "operator": "propagate",
            "inputs": [k(3)], "output": k(4),
            "requirement": "M_reliable",
            "scope": "estimate_Q",
            "narrative": "Q is derived from whichever warrant for M remains active."
        },
        {
            "id": t("D"), "operator": "independent_support",
            "inputs": [k(8)], "output": k(4),
            "requirement": "control_Q_valid",
            "scope": "estimate_Q",
            "narrative": "An independent control directly supports Q."
        },
        {
            "id": t("E"), "operator": "route_locked",
            "inputs": [k(3), k(6)], "output": k(5),
            "requirement": "same_run_A_provenance_valid",
            "scope": "same_run_extrapolation_R",
            "source_binding": t("A"),
            "narrative": "R explicitly uses M as produced by run A; the independent replication is not substitutable for this same-run extrapolation."
        },
        {
            "id": t("F"), "operator": "combine_v1",
            "inputs": [k(9), k(10)], "output": k(11),
            "requirement": "calibration_F_valid_during_run",
            "scope": "measurement_N_reliability",
            "narrative": "Run F uses the same combine_v1 procedure on a separate calibration and sample."
        },
        {
            "id": t("G"), "operator": "operational_use",
            "inputs": [k(3)], "output": k(12),
            "requirement": "dashboard_online",
            "scope": "display_only",
            "narrative": "The dashboard consumes M operationally; this event does not create epistemic warrant."
        },
        {
            "id": t("H"), "operator": "operational_use",
            "inputs": [k(13)], "output": k(12),
            "requirement": "diagnostic_channel_clear",
            "scope": "display_only",
            "narrative": "A diagnostic channel is used operationally and transfers no epistemic authority."
        },
    ]

    conditions = {
        "calibration_A_valid_during_run": True,
        "replication_valid": True,
        "M_reliable": True,
        "control_Q_valid": True,
        "same_run_A_provenance_valid": True,
        "calibration_F_valid_during_run": True,
        "dashboard_online": True,
        "diagnostic_channel_clear": True,
    }

    if scenario == "application_defeat":
        defeater = {
            "condition": "calibration_A_valid_during_run",
            "new_value": False,
            "evidence": "Post-run audit shows calibration A drifted during run A."
        }
    elif scenario == "null_operational":
        defeater = {
            "condition": "diagnostic_channel_clear",
            "new_value": False,
            "evidence": "Post-run audit shows the diagnostic channel was noisy during the recorded event."
        }
    else:
        raise ValueError(f"unknown scenario: {scenario}")

    return {
        "schema": "l2_world_v0",
        "status": "TOY_UNADMITTED_NON_EVIDENTIAL",
        "seed": seed,
        "scenario": scenario,
        "claims": claims,
        "events": events,
        "conditions_pre_defeater": conditions,
        "defeater": defeater,
        "reference_operator_semantics": {
            "combine_v1": "evidential_if_requirement_holds",
            "independent_support": "evidential_if_requirement_holds",
            "propagate": "evidential_if_requirement_holds_and_input_has_warrant",
            "route_locked": "evidential_if_requirement_holds_and_named_source_binding_remains_authoritative",
            "operational_use": "computational_only_no_warrant_transfer"
        }
    }


def learner_projection(world: dict) -> dict:
    return {
        "schema": "l2_learner_view_v0",
        "status": world["status"],
        "seed": world["seed"],
        "protocol": {
            "operator_semantics": world["reference_operator_semantics"],
            "task": (
                "Infer the defeater locus, affected authority instances, post-defeater claim actions, "
                "surviving warrant paths, and a small relational explanation. "
                "Do not treat computational use as warrant inheritance."
            ),
        },
        "claims": world["claims"],
        "observed_event_history": world["events"],
        "conditions_pre_defeater": world["conditions_pre_defeater"],
        "defeater_observation": world["defeater"],
        "required_output": {
            "defeater_locus": {"kind": "string", "target_instances": ["event_id"]},
            "affected_authority_instances": ["event_id"],
            "claim_actions": {"claim_id": "RETAIN|REOPEN"},
            "active_warrant_paths": {"claim_id": [["event_id", "..."]]},
            "reason_edges": [["source", "relation", "target"]],
            "history_preserved_instances": ["event_id"],
        },
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--scenario", choices=["application_defeat", "null_operational"], required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()

    world = build_world(args.seed, args.scenario)
    dump(args.out / "private_world.json", world)
    dump(args.out / "learner_view.json", learner_projection(world))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
