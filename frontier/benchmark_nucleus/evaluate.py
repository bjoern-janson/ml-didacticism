#!/usr/bin/env python3
"""Deterministic evaluator for the toy correction-locality nucleus.

No third-party dependencies.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, Mapping, Sequence, Set, Tuple


PathTuple = Tuple[str, ...]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def normalize_paths(paths: Iterable[Sequence[str]]) -> Set[PathTuple]:
    return {tuple(path) for path in paths}


def safe_get(mapping: Mapping, *keys, default=None):
    cur = mapping
    for key in keys:
        if not isinstance(cur, Mapping) or key not in cur:
            return default
        cur = cur[key]
    return cur


def score_case(case: dict, prediction: dict) -> dict:
    gold = case["gold_post_defeater"]
    gold_t = gold["transformation_instances"]
    pred_t = prediction.get("transformation_instances", {})

    transform_checks = {}
    for tid, expected in gold_t.items():
        got = pred_t.get(tid, {})
        transform_checks[tid] = {
            "realized": got.get("realized") == expected["realized"],
            "authority_active": got.get("authority_active") == expected["authority_active"],
        }

    gold_claims = gold["claim_status"]
    pred_claims = prediction.get("claim_status", {})
    claim_checks = {
        kid: pred_claims.get(kid) == expected
        for kid, expected in gold_claims.items()
    }

    gold_paths = gold["warrant_paths_active"]
    pred_paths = prediction.get("warrant_paths_active", {})
    path_checks = {}
    tp = fp = fn = 0
    for kid, expected_paths in gold_paths.items():
        expected = normalize_paths(expected_paths)
        got = normalize_paths(pred_paths.get(kid, []))
        path_checks[kid] = got == expected
        tp += len(got & expected)
        fp += len(got - expected)
        fn += len(expected - got)

    precision = tp / (tp + fp) if (tp + fp) else (1.0 if fn == 0 else 0.0)
    recall = tp / (tp + fn) if (tp + fn) else 1.0

    target = case["defeater"]["target_instance"]
    same_operator_controls = [
        tid
        for tid, record in case["transformation_instances"].items()
        if tid != target
        and record["operator"] == case["transformation_instances"][target]["operator"]
    ]

    invariants = {
        "revoke_authority_not_history": (
            safe_get(pred_t, target, "realized") is True
            and safe_get(pred_t, target, "authority_active") is False
        ),
        "instance_not_operator_global": all(
            safe_get(pred_t, tid, "authority_active") is True
            for tid in same_operator_controls
        ),
        "independent_support_preserved": (
            pred_claims.get("K3") == "RETAIN"
            and normalize_paths(pred_paths.get("K3", []))
            == normalize_paths(gold_paths["K3"])
        ),
        "affected_descendant_reopened": (
            pred_claims.get("K5") == "REOPEN"
            and normalize_paths(pred_paths.get("K5", [])) == set()
        ),
        "mixed_support_descendant_preserved": (
            pred_claims.get("K4") == "RETAIN"
            and normalize_paths(pred_paths.get("K4", []))
            == normalize_paths(gold_paths["K4"])
        ),
    }

    exact = (
        all(all(v.values()) for v in transform_checks.values())
        and all(claim_checks.values())
        and all(path_checks.values())
    )

    return {
        "case_id": case["id"],
        "status": case["status"],
        "pass": exact,
        "invariants": invariants,
        "claim_checks": claim_checks,
        "transformation_checks": transform_checks,
        "warrant_path_checks": path_checks,
        "warrant_path_precision": precision,
        "warrant_path_recall": recall,
        "warrant_path_false_positive_count": fp,
        "warrant_path_false_negative_count": fn,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("case", type=Path)
    parser.add_argument("prediction", type=Path)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()

    case = load_json(args.case)
    prediction = load_json(args.prediction)
    result = score_case(case, prediction)
    print(json.dumps(result, indent=None if args.compact else 2, sort_keys=True))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
