#!/usr/bin/env python3
"""Small paired scenarios for memory-policy comparison.

The visible anomaly language is intentionally repetitive. Correct authority changes differ
because the underlying warrant geometry differs.
"""
from __future__ import annotations


def _claims(*ids: str) -> dict:
    return {k: {"content": f"research artifact {k}"} for k in ids}


def _t(
    tid, operator, inputs, output, *, source, authority_scope="S", authority_kind="epistemic",
    source_binding=None
):
    x = {
        "id": tid,
        "operator": operator,
        "inputs": list(inputs),
        "output": output,
        "source": source,
        "authority_scope": authority_scope,
        "authority_kind": authority_kind,
    }
    if source_binding:
        x["source_binding"] = source_binding
    return x


SCENARIOS = {
    "alternate_support": {
        "id": "alternate_support",
        "surface_anomaly": "Post-run audit invalidates one recorded support event.",
        "claims": _claims("K1", "K2", "K3", "K4"),
        "transformations": [
            _t("tau_A", "combine", ["K1"], "K3", source="SRC_A"),
            _t("tau_B", "independent_support", ["K2"], "K3", source="SRC_B"),
            _t("tau_C", "propagate", ["K3"], "K4", source="SRC_C"),
        ],
        "operator_validity": {"combine": True, "independent_support": True, "propagate": True},
        "defeater_visible": {"target": "tau_A", "finding": "support_event_invalid"},
        "defeater_gold": {"kind": "INSTANCE_APPLICABILITY", "target_instance": "tau_A"},
    },
    "sole_support": {
        "id": "sole_support",
        "surface_anomaly": "Post-run audit invalidates one recorded support event.",
        "claims": _claims("K1", "K3", "K4"),
        "transformations": [
            _t("tau_A", "combine", ["K1"], "K3", source="SRC_A"),
            _t("tau_C", "propagate", ["K3"], "K4", source="SRC_C"),
        ],
        "operator_validity": {"combine": True, "propagate": True},
        "defeater_visible": {"target": "tau_A", "finding": "support_event_invalid"},
        "defeater_gold": {"kind": "INSTANCE_APPLICABILITY", "target_instance": "tau_A"},
    },
    "scope_only": {
        "id": "scope_only",
        "surface_anomaly": "Post-run audit limits the warranted use of one recorded support event.",
        "claims": _claims("K1", "K3"),
        "transformations": [
            _t("tau_A", "combine", ["K1"], "K3", source="SRC_A", authority_scope="S_BROAD"),
        ],
        "operator_validity": {"combine": True},
        "defeater_visible": {
            "target": "tau_A", "finding": "scope_limited", "new_scope": "S_NARROW"
        },
        "defeater_gold": {
            "kind": "SCOPE_NARROW", "target_instance": "tau_A", "new_scope": "S_NARROW"
        },
    },
    "operational_null": {
        "id": "operational_null",
        "surface_anomaly": "Post-run audit invalidates one recorded event.",
        "claims": _claims("K1", "K2"),
        "transformations": [
            _t(
                "tau_A", "operational_use", ["K1"], "K2",
                source="SRC_A", authority_kind="operational"
            ),
        ],
        "operator_validity": {"operational_use": True},
        "defeater_visible": {"target": "tau_A", "finding": "event_invalid"},
        "defeater_gold": {"kind": "OPERATIONAL_ONLY", "target_instance": "tau_A"},
    },
    "instance_not_operator": {
        "id": "instance_not_operator",
        "surface_anomaly": "Post-run audit invalidates one recorded support event.",
        "claims": _claims("K1", "K2", "K3", "K4"),
        "transformations": [
            _t("tau_A", "combine", ["K1"], "K3", source="SRC_A"),
            _t("tau_F", "combine", ["K2"], "K4", source="SRC_F"),
        ],
        "operator_validity": {"combine": True},
        "defeater_visible": {"target": "tau_A", "finding": "support_event_invalid"},
        "defeater_gold": {"kind": "INSTANCE_APPLICABILITY", "target_instance": "tau_A"},
    },
    "operator_invalid": {
        "id": "operator_invalid",
        "surface_anomaly": "Audit establishes that a transformation rule itself is invalid.",
        "claims": _claims("K1", "K2", "K3", "K4", "K5"),
        "transformations": [
            _t("tau_A", "combine", ["K1"], "K3", source="SRC_A"),
            _t("tau_F", "combine", ["K2"], "K4", source="SRC_F"),
            _t("tau_B", "independent_support", ["K5"], "K4", source="SRC_B"),
        ],
        "operator_validity": {"combine": True, "independent_support": True},
        "defeater_visible": {"target": "operator:combine", "finding": "operator_invalid"},
        "defeater_gold": {"kind": "OPERATOR_VALIDITY", "target_operator": "combine"},
    },
    "route_locked": {
        "id": "route_locked",
        "surface_anomaly": "Post-run audit invalidates one recorded support event.",
        "claims": _claims("K1", "K2", "K3", "K4", "K5"),
        "transformations": [
            _t("tau_A", "combine", ["K1"], "K3", source="SRC_A"),
            _t("tau_B", "independent_support", ["K2"], "K3", source="SRC_B"),
            _t(
                "tau_E", "route_locked", ["K3"], "K4",
                source="SRC_E", source_binding="tau_A"
            ),
            _t("tau_D", "independent_support", ["K5"], "K4", source="SRC_D"),
        ],
        "operator_validity": {
            "combine": True, "independent_support": True, "route_locked": True
        },
        "defeater_visible": {"target": "tau_A", "finding": "support_event_invalid"},
        "defeater_gold": {"kind": "INSTANCE_APPLICABILITY", "target_instance": "tau_A"},
    },
}


def get(name: str) -> dict:
    return SCENARIOS[name]


def all_scenarios() -> list[dict]:
    return [SCENARIOS[k] for k in sorted(SCENARIOS)]
