"""Walidator tests/legal/*.yaml wzgledem schema/legal-test.schema.json.

Uzycie: py schema/validate_tests.py
Patrz tests/README.md, AGENTS.md sekcje 26-29.

Tak jak validate_rules.py: ERROR blokuje (narusza schemat, martwe
odesłanie do reguly, zduplikowane ID), WARNING nie blokuje (informacyjne).
"""
import glob
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "legal-test.schema.json"


def load_schema():
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_known_rule_ids():
    ids = set()
    for path in glob.glob(str(ROOT / "law" / "*" / "rules" / "*.yaml")) + glob.glob(
        str(ROOT / "law" / "*" / "procedures" / "*.yaml")
    ):
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if data and "id" in data:
            ids.add(data["id"])
    return ids


def find_test_files():
    return sorted(glob.glob(str(ROOT / "tests" / "legal" / "*.yaml")))


def main():
    schema = load_schema()
    validator = Draft202012Validator(schema)
    known_rule_ids = load_known_rule_ids()

    errors = []
    warnings = []
    seen_ids = {}
    rule_to_tests = {}

    for path in find_test_files():
        rel = Path(path).relative_to(ROOT).as_posix()
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        for err in sorted(validator.iter_errors(data), key=lambda e: e.path):
            loc = "/".join(str(p) for p in err.path) or "<root>"
            errors.append(f"{rel}: [{loc}] {err.message}")

        test_id = data.get("id")
        if test_id:
            if test_id in seen_ids:
                errors.append(f"{rel}: duplicate id {test_id} (also in {seen_ids[test_id]})")
            else:
                seen_ids[test_id] = rel

        rule_id = data.get("rule")
        if rule_id:
            if rule_id not in known_rule_ids:
                errors.append(f"{rel}: rule '{rule_id}' does not exist in rules/ or procedures/")
            rule_to_tests.setdefault(rule_id, []).append(test_id)

            rule_akt, rule_num = rule_id.split("-")[1], rule_id.split("-")[-1]
            if test_id and not test_id.startswith(f"T-{rule_akt}-{rule_num}-"):
                warnings.append(
                    f"{rel}: id '{test_id}' numbering doesn't match rule '{rule_id}' "
                    "(expected prefix T-PS-<same NNNN>-)"
                )

    rules_without_tests = sorted(known_rule_ids - set(rule_to_tests.keys()))

    for path in glob.glob(str(ROOT / "law" / "*" / "rules" / "*.yaml")) + glob.glob(
        str(ROOT / "law" / "*" / "procedures" / "*.yaml")
    ):
        rel = Path(path).relative_to(ROOT).as_posix()
        with open(path, encoding="utf-8") as f:
            rule_data = yaml.safe_load(f)
        rule_id = rule_data.get("id")
        declared = set(rule_data.get("tests") or [])
        actual = set(rule_to_tests.get(rule_id, []))
        if declared != actual:
            warnings.append(
                f"{rel}: rule's `tests:` field {sorted(declared)} does not match "
                f"tests actually referencing it via `rule:` {sorted(actual)}"
            )

    print(f"Checked {len(find_test_files())} test files against {len(known_rule_ids)} known rules.")
    print(f"\nERRORS: {len(errors)}")
    for e in errors:
        print(f"  - {e}")
    print(f"\nWARNINGS: {len(warnings)}")
    for w in warnings:
        print(f"  - {w}")
    print(f"\nRules/procedures with 0 tests ({len(rules_without_tests)}):")
    for r in rules_without_tests:
        print(f"  - {r}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
