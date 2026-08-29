#!/usr/bin/env python3
"""Self-test: prove the nucleus distinguishes three canonical failure modes."""

from pathlib import Path

from evaluate import load_json, score_case


HERE = Path(__file__).resolve().parent
CASE = load_json(HERE / "cases" / "case_001.json")


def check(name: str, should_pass: bool, required_failed_invariant: str | None = None) -> None:
    prediction = load_json(HERE / "fixtures" / f"{name}.json")
    result = score_case(CASE, prediction)
    assert result["pass"] is should_pass, (name, result)
    if required_failed_invariant is not None:
        assert result["invariants"][required_failed_invariant] is False, (name, result)


def main() -> None:
    check("oracle", True)
    check("ignore_defeater", False, "revoke_authority_not_history")
    check("delete_downstream", False, "independent_support_preserved")
    check("global_blacklist_operator", False, "instance_not_operator_global")
    print("PASS: oracle accepted; undercorrection, subtree overcorrection, and operator-global overcorrection rejected.")


if __name__ == "__main__":
    main()
