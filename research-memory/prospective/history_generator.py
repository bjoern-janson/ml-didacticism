#!/usr/bin/env python3
"""Generate a prospective research history before any defeater exists.

The generator emits only accumulated claims/transformations. It does not choose,
name, or encode a future defeater.
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path


def _claim(content: str) -> dict:
    return {"content": content}


def _t(
    tid: str, operator: str, inputs: list[str], output: str, *,
    source: str, authority_scope: str = "S", authority_kind: str = "epistemic",
    source_binding: str | None = None, recorded_at: int | None = None,
) -> dict:
    x = {
        "id": tid,
        "operator": operator,
        "inputs": list(inputs),
        "output": output,
        "source": source,
        "authority_scope": authority_scope,
        "authority_kind": authority_kind,
    }
    if source_binding is not None:
        x["source_binding"] = source_binding
    if recorded_at is not None:
        x["recorded_at"] = recorded_at
    return x


def build_history(seed: int = 101) -> dict:
    """Build a small accumulated history with several warrant geometries.

    The seed only changes the interleaving of independent research streams;
    it does not select a future defeater.
    """
    rng = random.Random(seed)

    claims = {
        "K1": _claim("calibration A was valid before run A"),
        "K2": _claim("sample A was stable"),
        "K3": _claim("independent replication input for M"),
        "K4": _claim("independent control input for Q"),
        "K5": _claim("calibration F was valid before run F"),
        "K6": _claim("sample F was stable"),
        "K7": _claim("same-run auxiliary condition for R"),
        "K8": _claim("diagnostic stream input"),
        "K9": _claim("measurement M is reliable"),
        "K10": _claim("derived estimate Q is usable"),
        "K11": _claim("same-run extrapolation R is warranted"),
        "K12": _claim("measurement N is reliable"),
        "K13": _claim("broad-scope use of M is warranted"),
        "K14": _claim("dashboard value is available"),
        "K15": _claim("downstream synthesis from R"),
    }

    stream_a = [
        _t("tau_A", "combine_v1", ["K1", "K2"], "K9",
           source="SRC_A", recorded_at=1),
        _t("tau_B", "independent_support", ["K3"], "K9",
           source="SRC_B", recorded_at=2),
        _t("tau_C", "propagate", ["K9"], "K10",
           source="SRC_C", recorded_at=3),
        _t("tau_D", "independent_support", ["K4"], "K10",
           source="SRC_D", recorded_at=4),
        _t("tau_E", "route_locked", ["K9", "K7"], "K11",
           source="SRC_E", source_binding="tau_A", recorded_at=5),
        _t("tau_I", "propagate", ["K11"], "K15",
           source="SRC_I", recorded_at=6),
        _t("tau_G", "scope_promote", ["K9"], "K13",
           source="SRC_G", authority_scope="S_BROAD", recorded_at=7),
        _t("tau_H", "operational_use", ["K8"], "K14",
           source="SRC_H", authority_kind="operational", recorded_at=8),
    ]
    stream_f = [
        _t("tau_F", "combine_v1", ["K5", "K6"], "K12",
           source="SRC_F", recorded_at=1),
    ]

    insert_at = rng.randrange(0, len(stream_a) + 1)
    transformations = list(stream_a)
    transformations.insert(insert_at, stream_f[0])
    for i, t in enumerate(transformations, start=1):
        t["recorded_at"] = i

    return {
        "id": f"prospective_history_{seed}",
        "schema": "prospective_research_history_v0",
        "status": "ENGINEERING_PROTOTYPE_NON_EVIDENTIAL",
        "seed": seed,
        "claims": claims,
        "transformations": transformations,
        "operator_validity": {
            "combine_v1": True,
            "independent_support": True,
            "propagate": True,
            "route_locked": True,
            "scope_promote": True,
            "operational_use": True,
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=101)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    args.out.write_text(json.dumps(build_history(args.seed), indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
