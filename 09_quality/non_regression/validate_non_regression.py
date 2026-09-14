#!/usr/bin/env python3
"""Validate locked non-regression invariants with deterministic guards.

The contract uses the JSON subset of YAML 1.2 so this validator has no
third-party dependency. Contract data never executes shell commands.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


DEFAULT_CONTRACT = Path("00_project/governance/NON_REGRESSION_CONTRACT.yaml")
SEMANTIC_AUTHORITY = Path(
    "00_project/governance/modules/engineering/NON_REGRESSION_CONTROL.md"
)
SUPPORTED_GUARDS = {
    "FILE_EXISTS",
    "TEXT_CONTAINS",
    "TEXT_NOT_CONTAINS",
    "REGEX_COUNT",
}
REQUIRED_RULE_FIELDS = {
    "id",
    "scope",
    "subject",
    "statement",
    "status",
    "introduced_by",
    "source",
    "change_requires",
    "supersedes",
    "superseded_by",
    "guards",
}
REQUIRED_FRAMEWORK_INVARIANTS = {
    "NRC-FWK-001",
    "NRC-FWK-002",
    "NRC-FWK-003",
    "NRC-FWK-004",
    "NRC-FWK-005",
}
REQUIRED_REPLACEMENT_CONTROLS = {
    "EXPLICIT_CHANGE_DECISION",
    "IMPACT_ANALYSIS",
    "NEW_INVARIANT_ID",
    "FORMAL_C04",
}


class ContractError(Exception):
    """The contract or one of its declared inputs is invalid."""


def repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def safe_file(root: Path, relative: object) -> Path:
    if not isinstance(relative, str) or not relative:
        raise ContractError("guard file must be a non-empty relative path")
    candidate = Path(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ContractError(f"guard file escapes repository root: {relative}")
    resolved = (root / candidate).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise ContractError(f"guard file escapes repository root: {relative}") from exc
    return resolved


def load_contract(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ContractError(f"contract not found: {path}") from exc
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ContractError(f"contract cannot be parsed: {exc}") from exc
    if not isinstance(data, dict):
        raise ContractError("contract root must be an object")
    return data


def validate_contract_shape(data: dict) -> list[dict]:
    if data.get("schema_version") != "1.0":
        raise ContractError("unsupported contract schema_version")
    if data.get("contract_owner") != DEFAULT_CONTRACT.as_posix():
        raise ContractError("contract_owner is invalid")
    if data.get("semantic_authority") != SEMANTIC_AUTHORITY.as_posix():
        raise ContractError("semantic_authority is invalid")
    if data.get("validator") != Path(__file__).resolve().relative_to(repository_root()).as_posix():
        raise ContractError("validator binding is invalid")

    change_policy = data.get("change_policy")
    if not isinstance(change_policy, dict):
        raise ContractError("change_policy must be an object")
    if change_policy.get("locked_in_place_semantic_edit") != "FORBIDDEN":
        raise ContractError("locked_in_place_semantic_edit must remain FORBIDDEN")
    if set(change_policy.get("replacement_requires") or []) != REQUIRED_REPLACEMENT_CONTROLS:
        raise ContractError("replacement_requires is invalid")
    if (
        change_policy.get("recurring_closed_finding")
        != "CREATE_NEW_FINDING_ID_WITH_REGRESSION_OF"
    ):
        raise ContractError("recurring_closed_finding policy is invalid")

    declared = data.get("allowed_guard_kinds")
    if set(declared or []) != SUPPORTED_GUARDS:
        raise ContractError("allowed_guard_kinds does not match validator support")
    required = set(data.get("required_invariant_fields") or [])
    if required != REQUIRED_RULE_FIELDS:
        raise ContractError("required_invariant_fields does not match the schema")
    allowed_statuses = set(data.get("allowed_statuses") or [])
    if allowed_statuses != {"PROPOSED", "LOCKED", "SUPERSEDED"}:
        raise ContractError("allowed_statuses is invalid")

    rules: list[dict] = []
    framework_ids: set[str] = set()
    guard_ids: set[str] = set()
    for group in ("framework_invariants", "project_invariants"):
        value = data.get(group)
        if not isinstance(value, list):
            raise ContractError(f"{group} must be a list")
        for rule in value:
            if not isinstance(rule, dict):
                raise ContractError(f"{group} contains a non-object rule")
            missing = REQUIRED_RULE_FIELDS - set(rule)
            if missing:
                raise ContractError(
                    f"invariant {rule.get('id', '<unknown>')} missing fields: "
                    + ", ".join(sorted(missing))
                )
            rule_id = rule["id"]
            if not isinstance(rule_id, str) or not rule_id:
                raise ContractError(f"{group} contains an invalid invariant id")
            for field in ("scope", "subject", "statement", "introduced_by", "source"):
                if not isinstance(rule[field], str) or not rule[field]:
                    raise ContractError(f"{rule_id}: {field} must be a non-empty string")
            expected_scope = "FRAMEWORK" if group == "framework_invariants" else "PROJECT"
            if rule["scope"] != expected_scope:
                raise ContractError(
                    f"{rule_id}: scope must be {expected_scope} in {group}"
                )
            if rule["status"] not in allowed_statuses:
                raise ContractError(f"{rule_id}: invalid status {rule['status']!r}")
            if not isinstance(rule["change_requires"], list) or not rule["change_requires"]:
                raise ContractError(f"{rule_id}: change_requires must be a non-empty list")
            if not all(isinstance(item, str) and item for item in rule["change_requires"]):
                raise ContractError(f"{rule_id}: change_requires contains an invalid item")
            if not REQUIRED_REPLACEMENT_CONTROLS.issubset(set(rule["change_requires"])):
                raise ContractError(f"{rule_id}: change_requires omits a mandatory control")
            for relation in ("supersedes", "superseded_by"):
                if rule[relation] is not None and (
                    not isinstance(rule[relation], str) or not rule[relation]
                ):
                    raise ContractError(f"{rule_id}: {relation} must be null or a non-empty id")
            if rule["status"] == "LOCKED" and rule["superseded_by"] is not None:
                raise ContractError(f"{rule_id}: LOCKED invariant cannot have superseded_by")
            if rule["status"] == "SUPERSEDED" and rule["superseded_by"] is None:
                raise ContractError(f"{rule_id}: SUPERSEDED invariant requires superseded_by")
            guards = rule["guards"]
            if not isinstance(guards, list):
                raise ContractError(f"{rule_id}: guards must be a list")
            for guard in guards:
                if not isinstance(guard, dict) or not isinstance(guard.get("id"), str):
                    raise ContractError(f"{rule_id}: invalid guard definition")
                guard_id = guard["id"]
                if not guard_id:
                    raise ContractError(f"{rule_id}: guard id must be non-empty")
                if guard_id in guard_ids:
                    raise ContractError(f"duplicate guard id: {guard_id}")
                guard_ids.add(guard_id)
            if group == "framework_invariants":
                framework_ids.add(rule_id)
            rules.append(rule)

    ids = [rule["id"] for rule in rules]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        raise ContractError("duplicate invariant ids: " + ", ".join(duplicates))
    missing_framework = REQUIRED_FRAMEWORK_INVARIANTS - framework_ids
    if missing_framework:
        raise ContractError(
            "required framework invariants missing: " + ", ".join(sorted(missing_framework))
        )

    by_id = {rule["id"]: rule for rule in rules}
    for rule in rules:
        predecessor_id = rule["supersedes"]
        successor_id = rule["superseded_by"]
        if predecessor_id is not None:
            predecessor = by_id.get(predecessor_id)
            if (
                predecessor is None
                or predecessor["scope"] != rule["scope"]
                or predecessor["superseded_by"] != rule["id"]
                or predecessor["status"] != "SUPERSEDED"
                or rule["status"] == "PROPOSED"
            ):
                raise ContractError(f"{rule['id']}: invalid supersedes relationship")
        if successor_id is not None:
            successor = by_id.get(successor_id)
            if (
                successor is None
                or successor["scope"] != rule["scope"]
                or successor["supersedes"] != rule["id"]
            ):
                raise ContractError(f"{rule['id']}: invalid superseded_by relationship")

    for rule in rules:
        if rule["status"] != "SUPERSEDED":
            continue
        current = rule
        visited: set[str] = set()
        while current["status"] == "SUPERSEDED":
            if current["id"] in visited:
                raise ContractError(f"{rule['id']}: supersession cycle detected")
            visited.add(current["id"])
            current = by_id[current["superseded_by"]]
        if current["status"] != "LOCKED":
            raise ContractError(
                f"{rule['id']}: active supersession chain must end in LOCKED"
            )

    for required_id in REQUIRED_FRAMEWORK_INVARIANTS:
        current = by_id[required_id]
        visited: set[str] = set()
        while current["status"] == "SUPERSEDED":
            if current["id"] in visited:
                raise ContractError(f"{required_id}: supersession cycle detected")
            visited.add(current["id"])
            current = by_id[current["superseded_by"]]
        if current["status"] != "LOCKED":
            raise ContractError(
                f"{required_id}: active supersession chain must end in LOCKED"
            )
    return rules


def run_guard(root: Path, guard: dict) -> tuple[bool, str]:
    guard_id = guard.get("id", "<unknown>")
    kind = guard.get("kind")
    if kind not in SUPPORTED_GUARDS:
        raise ContractError(f"{guard_id}: unsupported guard kind {kind!r}")
    path = safe_file(root, guard.get("file"))

    if kind == "FILE_EXISTS":
        return path.is_file(), f"file exists: {guard.get('file')}"
    if not path.is_file():
        raise ContractError(f"{guard_id}: input file not found: {guard.get('file')}")

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ContractError(f"{guard_id}: cannot read {guard.get('file')}: {exc}") from exc

    if kind in {"TEXT_CONTAINS", "TEXT_NOT_CONTAINS"}:
        value = guard.get("value")
        if not isinstance(value, str) or not value:
            raise ContractError(f"{guard_id}: value must be a non-empty string")
        present = value in text
        if kind == "TEXT_CONTAINS":
            return present, f"required text present in {guard.get('file')}"
        return not present, f"forbidden text absent from {guard.get('file')}"

    pattern = guard.get("pattern")
    expected = guard.get("expected_count")
    if not isinstance(pattern, str) or not isinstance(expected, int) or expected < 0:
        raise ContractError(f"{guard_id}: REGEX_COUNT requires pattern and non-negative expected_count")
    try:
        actual = len(re.findall(pattern, text))
    except re.error as exc:
        raise ContractError(f"{guard_id}: invalid regex: {exc}") from exc
    return actual == expected, f"regex count {actual}, expected {expected} in {guard.get('file')}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=repository_root())
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    contract_path = args.contract
    if not contract_path.is_absolute():
        contract_path = root / contract_path

    print("NON-REGRESSION VALIDATION")
    print(f"Root: {root}")
    print(f"Contract: {contract_path}")

    try:
        data = load_contract(contract_path)
        rules = validate_contract_shape(data)
        locked = [rule for rule in rules if rule["status"] == "LOCKED"]
        if not locked:
            raise ContractError("no LOCKED invariants are defined")

        failures: list[str] = []
        executed_guard_ids: set[str] = set()
        for rule in locked:
            guards = rule["guards"]
            if not isinstance(guards, list) or not guards:
                raise ContractError(f"{rule['id']}: LOCKED invariant has no guards")
            print(f"\n{rule['id']} {rule['subject']}")
            for guard in guards:
                guard_id = guard["id"]
                executed_guard_ids.add(guard_id)
                passed, detail = run_guard(root, guard)
                print(f"  {'PASS' if passed else 'FAIL'} {guard_id}: {detail}")
                if not passed:
                    failures.append(f"{rule['id']} / {guard_id}: {detail}")
    except ContractError as exc:
        print(f"\nRESULT: INVALID ({exc})")
        return 2

    if failures:
        print("\nVIOLATIONS")
        for failure in failures:
            print(f"- {failure}")
        print("\nRESULT: FAIL")
        return 1

    print(f"\nLocked invariants: {len(locked)}")
    print(f"Guards executed: {len(executed_guard_ids)}")
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
