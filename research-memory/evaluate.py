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


def f1(precision: float, recall: float) -> float:
    if precision + recall == 0.0:
        return 0.0
    return 2.0 * precision * recall / (precision + recall)


def score(gold: Mapping, pred: Mapping) -> dict:
    gold_affected = _set(gold["affected_authority_instances"])
    pred_affected = _set(pred["affected_authority_instances"])
    p_w, r_w = prf(pred_affected, gold_affected)

    gold_reopen = _set(gold["reopened_claims"])
    pred_reopen = _set(pred["reopened_claims"])
    reopen_precision, reopen_recall = prf(pred_reopen, gold_reopen)

    gold_retained = _set(gold["retained_claims"])
    pred_retained = _set(pred["retained_claims"])
    retained_precision, retained_recall = prf(pred_retained, gold_retained)
    # I_P is deliberately two-sided: false retained claims now reduce the score
    # instead of receiving full credit from a recall-only preservation metric.
    independent_preservation = f1(retained_precision, retained_recall)

    scope_accuracy = 1.0 if pred.get("narrowed_scopes", {}) == gold["narrowed_scopes"] else 0.0

    gold_history = _set(gold["preserved_history"])
    pred_history = _set(pred["preserved_history"])
    history_precision, history_recall = prf(pred_history, gold_history)
    # H_P is likewise two-sided: invented historical events are penalized.
    history_preservation = f1(history_precision, history_recall)

    recomputation_correctness = (
        1.0
        if _set(pred["required_recomputations"]) == _set(gold["required_recomputations"])
        else 0.0
    )

    gold_removed = _path_set(gold["removed_warrant_paths"])
    pred_removed = _path_set(pred.get("removed_warrant_paths", []))
    path_precision, path_recall = prf(pred_removed, gold_removed)
    paths_exact = pred_removed == gold_removed
    history_exact = pred_history == gold_history

    # Action correctness is intentionally narrower than full output correctness.
    # This allows a cheaper memory policy to receive credit for choosing the
    # right correction action while still failing warrant-path reconstruction.
    action_exact = (
        pred.get("defeater_locus") == gold["defeater_locus"]
        and pred_affected == gold_affected
        and pred_reopen == gold_reopen
        and pred_retained == gold_retained
        and pred.get("narrowed_scopes", {}) == gold["narrowed_scopes"]
        and _set(pred["required_recomputations"]) == _set(gold["required_recomputations"])
    )

    # Repair cost is an observed engineering metric unless a future gold object
    # explicitly declares a cost target. If such a target exists, strict exactness
    # includes it; otherwise exactness makes no hidden claim about cost optimality.
    gold_cost = gold.get("repair_cost")
    cost_exact = None if gold_cost is None else pred.get("repair_cost") == gold_cost

    exact = (
        action_exact
        and paths_exact
        and history_exact
        and (cost_exact is not False)
    )

    cost = pred.get("repair_cost", {})
    return {
        "exact": exact,
        "action_exact": action_exact,
        "paths_exact": paths_exact,
        "history_exact": history_exact,
        "cost_exact": cost_exact,
        "R_W": r_w,
        "P_W": p_w,
        "I_P": independent_preservation,
        "retained_precision": retained_precision,
        "retained_recall": retained_recall,
        "S_A": scope_accuracy,
        "H_P": history_preservation,
        "history_precision": history_precision,
        "history_recall": history_recall,
        "R_C": recomputation_correctness,
        "removed_path_precision": path_precision,
        "removed_path_recall": path_recall,
        "reopen_precision": reopen_precision,
        "reopen_recall": reopen_recall,
        "C_R": cost.get("authority_changes"),
        "T_R": cost.get("records_inspected"),
    }
