#!/usr/bin/env python3
"""Three deliberately simple memory policies and non-generative reassessment baselines."""
from __future__ import annotations

from copy import deepcopy
from collections import defaultdict, deque
from typing import Mapping

from model import derive_gold, current_outputs, is_epistemic


def _history(world: Mapping) -> list[str]:
    return sorted(t["id"] for t in world["transformations"])


def _produced(world: Mapping) -> set[str]:
    return {t["output"] for t in world["transformations"] if is_epistemic(t)}


def _all_derived(world: Mapping) -> list[str]:
    return sorted(_produced(world))


class MemoryPolicy:
    name = "base"

    def __init__(self, world: Mapping):
        self.world = deepcopy(world)
        self.steps = 0

    def present_outputs(self) -> list[str]:
        return current_outputs(self.world)

    def reassess(self, defeater: Mapping) -> dict:
        raise NotImplementedError

    def _finish(
        self, *, locus, affected, reopened, retained, narrowed=None,
        recompute=None, removed_paths=None
    ) -> dict:
        return {
            "policy": self.name,
            "defeater_locus": locus,
            "affected_authority_instances": sorted(affected),
            "removed_warrant_paths": removed_paths or [],
            "reopened_claims": sorted(reopened),
            "retained_claims": sorted(retained),
            "narrowed_scopes": dict(sorted((narrowed or {}).items())),
            "required_recomputations": sorted(recompute or []),
            "preserved_history": _history(self.world),
            "repair_cost": {
                "records_inspected": self.steps,
                "authority_changes": len(affected) + len(reopened) + len(narrowed or {}),
            },
        }


class DependencyOnlyMemory(MemoryPolicy):
    """A: claim + ordinary computational dependency.

    Baseline rule: remove/reopen the computational cone of the named failed dependency.
    It cannot distinguish warrant from operational use, independent authority paths, or scope.
    """
    name = "A_dependency_only"

    def reassess(self, d: Mapping) -> dict:
        transforms = self.world["transformations"]
        by_id = {t["id"]: t for t in transforms}
        children = defaultdict(list)
        for t in transforms:
            self.steps += 1
            for inp in t["inputs"]:
                children[inp].append(t)

        target = d["target"]
        if target.startswith("operator:"):
            op = target.split(":", 1)[1]
            direct = [t["id"] for t in transforms if t["operator"] == op]
        else:
            direct = [target] if target in by_id else []

        affected_t = set(direct)
        reopened = set()
        q = deque()
        for tid in direct:
            t = by_id[tid]
            reopened.add(t["output"])
            q.append(t["output"])

        while q:
            claim = q.popleft()
            self.steps += 1
            for t in children.get(claim, []):
                if t["id"] not in affected_t:
                    affected_t.add(t["id"])
                if t["output"] not in reopened:
                    reopened.add(t["output"])
                    q.append(t["output"])

        derived = set(_all_derived(self.world))
        retained = derived - reopened
        locus = {"kind": "computational_target", "target_instances": sorted(direct)}
        return self._finish(
            locus=locus, affected=affected_t, reopened=reopened, retained=retained,
            recompute=reopened
        )


class SourceProvenanceMemory(MemoryPolicy):
    """B: dependency memory + source provenance.

    B treats source-distinct incoming routes as independently retainable support and can propagate
    loss through the ordinary dependency graph. It still lacks explicit authority scope,
    provenance-locked transformation paths, and operational-vs-epistemic typing.
    """
    name = "B_source_provenance"

    def reassess(self, d: Mapping) -> dict:
        transforms = self.world["transformations"]
        by_id = {t["id"]: t for t in transforms}
        target = d["target"]

        if target.startswith("operator:"):
            op = target.split(":", 1)[1]
            direct = [t["id"] for t in transforms if t["operator"] == op]
            defeated_sources = {t["source"] for t in transforms if t["operator"] == op}
            locus = {
                "kind": "OPERATOR_VALIDITY",
                "target_operator": op,
                "target_instances": sorted(direct),
            }
        else:
            direct = [target] if target in by_id else []
            defeated_sources = {by_id[target]["source"]} if target in by_id else set()
            locus = {"kind": "INSTANCE_APPLICABILITY", "target_instances": sorted(direct)}

        removed_direct = {
            t["id"] for t in transforms if t["source"] in defeated_sources
        }

        # B has no operational/warrant type distinction: every recorded dependency can look supportive.
        produced = {t["output"] for t in transforms}
        base_claims = set(self.world["claims"]) - produced

        def active_graph(blocked: set[str]) -> tuple[set[str], set[str]]:
            supported = set(base_claims)
            active = set()
            changed = True
            while changed:
                changed = False
                for t in transforms:
                    self.steps += 1
                    if t["id"] in blocked:
                        continue
                    if all(inp in supported for inp in t["inputs"]):
                        if t["id"] not in active:
                            active.add(t["id"])
                            changed = True
                        if t["output"] not in supported:
                            supported.add(t["output"])
                            changed = True
            return supported, active

        pre_supported, pre_active = active_graph(set())
        post_supported, post_active = active_graph(removed_direct)
        affected = pre_active - post_active

        derived_gold_like = set(_all_derived(self.world))
        reopened = {k for k in derived_gold_like if k not in post_supported}
        retained = derived_gold_like - reopened

        # Dependency-level recomputation: any derived claim whose active support ancestry changed.
        children = defaultdict(list)
        for t in transforms:
            for inp in t["inputs"]:
                children[inp].append(t["output"])
        recompute = set()
        q = deque(by_id[tid]["output"] for tid in affected if tid in by_id)
        while q:
            claim = q.popleft()
            if claim in recompute:
                continue
            if claim in derived_gold_like:
                recompute.add(claim)
            for child in children.get(claim, []):
                if child not in recompute:
                    q.append(child)

        return self._finish(
            locus=locus, affected=affected, reopened=reopened, retained=retained,
            recompute=recompute
        )


class WarrantLineageMemory(MemoryPolicy):
    """C: source + transformation-instance + warrant-lineage memory.

    The prototype uses full stored authority semantics to compute the typed delta. This is an
    engineering upper-bound policy, not evidence that a learner can infer hidden warrant topology.
    """
    name = "C_warrant_lineage"

    def reassess(self, d: Mapping) -> dict:
        self.steps += len(self.world["transformations"])
        gold = derive_gold(self.world)
        return {
            "policy": self.name,
            "defeater_locus": gold["defeater_locus"],
            "affected_authority_instances": gold["affected_authority_instances"],
            "removed_warrant_paths": gold["removed_warrant_paths"],
            "reopened_claims": gold["reopened_claims"],
            "retained_claims": gold["retained_claims"],
            "narrowed_scopes": gold["narrowed_scopes"],
            "required_recomputations": gold["required_recomputations"],
            "preserved_history": gold["preserved_history"],
            "repair_cost": {
                "records_inspected": self.steps,
                "authority_changes": (
                    len(gold["affected_authority_instances"])
                    + len(gold["reopened_claims"])
                    + len(gold["narrowed_scopes"])
                ),
            },
        }


POLICIES = [DependencyOnlyMemory, SourceProvenanceMemory, WarrantLineageMemory]
