#!/usr/bin/env python3
"""Score an L2 learner prediction against private gold."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def norm_paths(x: dict) -> dict:
    return {k: {tuple(p) for p in v} for k, v in x.items()}


def norm_edges(x) -> set[tuple[str, str, str]]:
    return {tuple(e) for e in x}


def score(gold: dict, pred: dict) -> dict:
    checks = {}
    checks["defeater_locus"] = pred.get("defeater_locus") == gold["defeater_locus"]
    checks["affected_authority_instances"] = sorted(pred.get("affected_authority_instances", [])) == sorted(gold["affected_authority_instances"])
    checks["claim_actions"] = pred.get("claim_actions") == gold["claim_actions"]
    checks["active_warrant_paths"] = norm_paths(pred.get("active_warrant_paths", {})) == norm_paths(gold["active_warrant_paths"])
    checks["reason_edges"] = norm_edges(pred.get("reason_edges", [])) == norm_edges(gold["reason_edges"])
    checks["history_preserved_instances"] = sorted(pred.get("history_preserved_instances", [])) == sorted(gold["history_preserved_instances"])

    return {
        "pass": all(checks.values()),
        "checks": checks,
        "status": gold["status"],
        "scenario": gold["scenario"],
        "seed": gold["seed"],
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("gold", type=Path)
    p.add_argument("prediction", type=Path)
    args = p.parse_args()
    result = score(load(args.gold), load(args.prediction))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
