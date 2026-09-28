"""Walidator warstwy semantycznej wzgledem schema/legal-rule.schema.json.

Uzycie: py schema/validate_rules.py
Patrz docs/decisions/ADR-0002-unified-rule-schema.md.

Dwa poziomy wyniku (AGENTS.md sekcja 8 - nie chowaj niepewnosci pod
jednym PASS/FAIL):
  ERROR   - narusza wymuszony schemat (brakujace pole, zla enuma,
            zduplikowane ID). Blokujace.
  WARNING - subject/holder/actor nie rozwiazuje sie do znanej encji, albo
            normalized_ref nie rozwiazuje sie do eId w AKN. Czesto to
            *poprawne* odzwierciedlenie tego, ze ustawa sama nie
            rozstrzyga (np. R-PS-0003 admitting_body - "statut nie
            przesadza ktory organ") - stad ostrzezenie, nie blad.
"""
import glob
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "legal-rule.schema.json"
AKN_NS = {"akn": "http://docs.oasis-open.org/legaldocml/ns/akn/3.0"}


def load_schema():
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_entity_names():
    names = set()
    for path in glob.glob(str(ROOT / "model" / "entities" / "*.yaml")) + glob.glob(
        str(ROOT / "law" / "*" / "ontology" / "entities" / "*.yaml")
    ):
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if data and "entity" in data:
            names.add(data["entity"])
    return names


def load_akn_eids():
    eids = set()
    for path in glob.glob(str(ROOT / "law" / "*" / "normalized" / "akoma-ntoso" / "*.xml")):
        tree = ET.parse(path)
        for el in tree.getroot().iter():
            eid = el.attrib.get("eId")
            if eid:
                eids.add(eid)
    return eids


def normalized_ref_to_eid(ref):
    m = re.match(r"^PS-ART-0*(\d+)([A-Za-z]*)$", ref)
    if not m:
        return None
    num, suffix = m.groups()
    return f"art_{num}{suffix.lower()}"


def as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def find_rule_files():
    return sorted(
        glob.glob(str(ROOT / "law" / "*" / "rules" / "*.yaml"))
        + glob.glob(str(ROOT / "law" / "*" / "procedures" / "*.yaml"))
    )


def main():
    schema = load_schema()
    validator = Draft202012Validator(schema)
    entity_names = load_entity_names()
    akn_eids = load_akn_eids()

    errors = []
    warnings = []
    seen_ids = {}

    for path in find_rule_files():
        rel = Path(path).relative_to(ROOT).as_posix()
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        for err in sorted(validator.iter_errors(data), key=lambda e: e.path):
            loc = "/".join(str(p) for p in err.path) or "<root>"
            errors.append(f"{rel}: [{loc}] {err.message}")

        rule_id = data.get("id")
        if rule_id:
            if rule_id in seen_ids:
                errors.append(f"{rel}: duplicate id {rule_id} (also in {seen_ids[rule_id]})")
            else:
                seen_ids[rule_id] = rel

        for ref in as_list(data.get("source", {}).get("normalized_ref")):
            eid = normalized_ref_to_eid(ref)
            if eid is None or eid not in akn_eids:
                warnings.append(f"{rel}: normalized_ref '{ref}' does not resolve to a known AKN eId")

        subjects_to_check = []
        if "subject" in data:
            subjects_to_check.append(("subject", data["subject"]))
        if "holder" in data:
            subjects_to_check.append(("holder", data["holder"]))
        for actor_name, actor_value in (data.get("actors") or {}).items():
            subjects_to_check.append((f"actors.{actor_name}", actor_value))

        for field_name, value in subjects_to_check:
            if not any(name in value for name in entity_names):
                warnings.append(
                    f"{rel}: {field_name}='{value}' does not contain a known entity name "
                    "(may be intentional - statute leaves it open, see AGENTS.md sekcja 50)"
                )

    print(f"Checked {len(find_rule_files())} files, {len(entity_names)} known entities, "
          f"{len(akn_eids)} AKN eIds.")
    print(f"\nERRORS: {len(errors)}")
    for e in errors:
        print(f"  - {e}")
    print(f"\nWARNINGS: {len(warnings)}")
    for w in warnings:
        print(f"  - {w}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
