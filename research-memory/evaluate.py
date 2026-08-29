#!/usr/bin/env python3
"""Vector evaluator for the research-memory A/B/C engineering prototype."""
from __future__ import annotations

from typing import Iterable, Mapping


def _set(items: Iterable[str]) -> set[str]:
    return set(items)


def _path_set(items) -> set[tuple[str, tuple[str, ...]]]:
    out = set()
    for x in items:
        out.add((x["claim"], tuple(x["path"])))
    return out


def prf(pred: set, gold: set) -> tuple[float, float]:
    tp = len(pred & gold)
    precision = tp / len(pred) if pred else (1.0 if not gold else 0.0)
    recall = tp / len(gold) if gold else (1.0 if not pred else 0.0)
    return precision, recall


def score(gold: Mapping, pred: Mapping) -> dict:
    gold_affected = _set(gold["affected_authority_instances"])
    pred_affected = _set(pred["affected_authority_instances"])
    p_w, r_w = prf(pred_affected, gold_affected)

    gold_reopen = _set(gold["reopened_claims"])
    pred_reopen = _set(pred["reopened_claims"])
    reopen_precision, reopen_recall = prf(pred_reopen, gold_reopen)

    gold_retained = _set(gold["retained_claims"])
    pred_retained = _set(pred["retained_claims"])
    independent_preservation = (
        len(gold_retained & pred_retained) / len(gold_retained)
        if gold_retained else 1.0
    )

    scope_accuracy = 1.0 if pred.get("narrowed_scopes", {}) == gold["narrowed_scopes"] else 0.0
    history_preservation = (
        len(_set(pred["preserved_history"]) & _set(gold["preserved_history"]))
        / len(_set(gold["preserved_history"]))
        if gold["preserved_history"] else 1.0
    )
    recomputation_correctness = (
        1.0
        if _set(pred["required_recomputations"]) == _set(gold["required_recomputations"])
        else 0.0
    )

    gold_removed = _path_set(gold["removed_warrant_paths"])
    pred_removed = _path_set(pred.get("removed_warrant_paths", []))
    path_precision, path_recall = prf(pred_removed, gold_removed)

    exact = (
        pred.get("defeater_locus") == gold["defeater_locus"]
        and pred_affected == gold_affected
        and pred_reopen == gold_reopen
        and pred_retained == gold_retained
        and pred.get("narrowed_scopes", {}) == gold["narrowed_scopes"]
        and _set(pred["required_recomputations"]) == _set(gold["required_recomputations"])
        and _set(pred["preserved_history"]) == _set(gold["preserved_history"])
    )

    cost = pred.get("repair_cost", {})
    return {
        "exact": exact,
        "R_W": r_w,
        "P_W": p_w,
        "I_P": independent_preservation,
        "S_A": scope_accuracy,
        "H_P": history_preservation,
        "R_C": recomputation_correctness,
        "removed_path_precision": path_precision,
        "removed_path_recall": path_recall,
        "reopen_precision": reopen_precision,
        "reopen_recall": reopen_recall,
        "C_R": cost.get("authority_changes"),
        "T_R": cost.get("records_inspected"),
    }
