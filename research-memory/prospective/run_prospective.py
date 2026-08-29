#!/usr/bin/env python3
"""Run prospective accumulation -> freeze -> post-freeze defeater -> A/B/C reassessment."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
if str(PARENT) not in sys.path:
    sys.path.insert(0, str(PARENT))

from evaluate import score
from model import derive_gold
from policies import POLICIES
from history_generator import build_history
from freeze_history import freeze_history, verify_freeze
from select_defeater import attach_defeater, select_after_freeze


def run(history_seed: int, selector_seed: int) -> dict:
    history = build_history(history_seed)
    frozen = freeze_history(history)
    assert verify_freeze(frozen)

    # Temporal cut: only now is a future defeater selected.
    selection = select_after_freeze(frozen, selector_seed)
    world = attach_defeater(frozen, selection)
    gold = derive_gold(world)

    policy_outputs = {}
    expected_now = frozen["present_outputs"]
    for Policy in POLICIES:
        policy = Policy(world)
        present = policy.present_outputs()
        if present != expected_now:
            raise AssertionError((Policy.name, present, expected_now))
        pred = policy.reassess(world["defeater_visible"])
        policy_outputs[Policy.name] = {
            "present_outputs": present,
            "prediction": pred,
            "metrics": score(gold, pred),
        }

    return {
        "schema": "prospective_memory_run_v0",
        "status": "ENGINEERING_PROTOTYPE_NON_EVIDENTIAL",
        "history_seed": history_seed,
        "selector_seed": selector_seed,
        "freeze": {
            "history_sha256": frozen["history_sha256"],
            "claim_count": frozen["claim_count"],
            "transformation_count": frozen["transformation_count"],
            "present_outputs": frozen["present_outputs"],
        },
        "post_freeze_defeater": selection,
        "gold": gold,
        "policies": policy_outputs,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--history-seed", type=int, default=101)
    ap.add_argument("--selector-seed", type=int, default=7)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    result = run(args.history_seed, args.selector_seed)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.out:
        args.out.write_text(text)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
