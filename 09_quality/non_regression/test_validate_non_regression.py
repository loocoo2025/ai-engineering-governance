#!/usr/bin/env python3
"""Targeted tests for the non-regression validator."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
CONTRACT_RELATIVE = Path("00_project/governance/NON_REGRESSION_CONTRACT.yaml")
VALIDATOR = REPOSITORY_ROOT / "09_quality/non_regression/validate_non_regression.py"


class NonRegressionValidatorTests(unittest.TestCase):
    def make_fixture(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        contract = json.loads((REPOSITORY_ROOT / CONTRACT_RELATIVE).read_text(encoding="utf-8"))
        required_files = {
            guard["file"]
            for group in ("framework_invariants", "project_invariants")
            for invariant in contract[group]
            for guard in invariant["guards"]
        }
        required_files.add(CONTRACT_RELATIVE.as_posix())
        for relative in required_files:
            source = REPOSITORY_ROOT / relative
            destination = root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        return temporary, root

    def run_validator(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), "--root", str(root)],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_current_contract_passes(self) -> None:
        temporary, root = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        result = self.run_validator(root)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_guard_violation_returns_one(self) -> None:
        temporary, root = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        target = root / "00_project/governance/GOVERNANCE_EXECUTION_CONTRACTS.yaml"
        text = target.read_text(encoding="utf-8")
        target.write_text(
            text.replace("required_dispatch_limit: 1", "required_dispatch_limit: 2"),
            encoding="utf-8",
        )
        result = self.run_validator(root)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_invalid_contract_returns_two(self) -> None:
        temporary, root = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        (root / CONTRACT_RELATIVE).write_text("{", encoding="utf-8")
        result = self.run_validator(root)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_core_invariant_cannot_be_downgraded(self) -> None:
        temporary, root = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        path = root / CONTRACT_RELATIVE
        contract = json.loads(path.read_text(encoding="utf-8"))
        contract["framework_invariants"][0]["status"] = "PROPOSED"
        path.write_text(json.dumps(contract), encoding="utf-8")
        result = self.run_validator(root)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_locked_policy_cannot_be_weakened(self) -> None:
        temporary, root = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        path = root / CONTRACT_RELATIVE
        contract = json.loads(path.read_text(encoding="utf-8"))
        contract["change_policy"]["locked_in_place_semantic_edit"] = "ALLOWED"
        path.write_text(json.dumps(contract), encoding="utf-8")
        result = self.run_validator(root)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_invariant_cannot_omit_replacement_control(self) -> None:
        temporary, root = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        path = root / CONTRACT_RELATIVE
        contract = json.loads(path.read_text(encoding="utf-8"))
        contract["framework_invariants"][0]["change_requires"].remove(
            "NEW_INVARIANT_ID"
        )
        path.write_text(json.dumps(contract), encoding="utf-8")
        result = self.run_validator(root)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
