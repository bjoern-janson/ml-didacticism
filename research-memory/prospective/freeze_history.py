#!/usr/bin/env python3
"""Freeze a prospective history before any later defeater is selected."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Mapping

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
if str(PARENT) not in sys.path:
    sys.path.insert(0, str(PARENT))

from model import current_outputs


def canonical_bytes(obj: Mapping) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")


def freeze_history(world: Mapping) -> dict:
    forbidden = {"defeater_visible", "defeater_gold", "future_defeater", "candidate_defeaters"}
    overlap = forbidden & set(world)
    if overlap:
        raise ValueError(f"history is not prospective; found future-defeater fields: {sorted(overlap)}")
    frozen_world = deepcopy(dict(world))
    digest = hashlib.sha256(canonical_bytes(frozen_world)).hexdigest()
    return {
        "schema": "prospective_history_freeze_v0",
        "status": "FROZEN_ENGINEERING_HISTORY_NON_EVIDENTIAL",
        "history_sha256": digest,
        "claim_count": len(frozen_world["claims"]),
        "transformation_count": len(frozen_world["transformations"]),
        "present_outputs": current_outputs(frozen_world),
        "world": frozen_world,
    }


def verify_freeze(bundle: Mapping) -> bool:
    return bundle["history_sha256"] == hashlib.sha256(
        canonical_bytes(bundle["world"])
    ).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("history", type=Path)
    ap.add_argument("freeze", type=Path)
    args = ap.parse_args()
    world = json.loads(args.history.read_text())
    bundle = freeze_history(world)
    args.freeze.write_text(json.dumps(bundle, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
