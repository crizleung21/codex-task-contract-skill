#!/usr/bin/env python3
"""Validate Loop Contract expected-output fixtures.

This script is intentionally zero-dependency and text-based. It checks that loop
expected outputs include the stable v0.2.0 Loop Contract fields and do not rely
on open-ended loop language.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "skills" / "task-contract" / "tests" / "expected"

REQUIRED_FILES = [
    "loop-debug-task.expected.md",
    "loop-research-task.expected.md",
    "loop-documentation-task.expected.md",
    "loop-dangerous-task.expected.md",
    "loop-repo-maintenance-task.expected.md",
]

REQUIRED_TERMS = [
    "Loop Objective",
    "Loop Type",
    "Iteration Unit",
    "Observation Method",
    "Adjustment Strategy",
    "Validation Method",
    "Stop Condition",
    "Max Iterations",
    "Escalation Trigger",
    "Loop Log",
]

FORBIDDEN_PATTERNS = [
    "repeat until done",
    "keep going forever",
    "unlimited iterations",
    "no stop condition",
    "continue without approval",
]


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL: {message}")


def main() -> int:
    failures: list[str] = []

    for filename in REQUIRED_FILES:
        path = EXPECTED / filename
        if not path.exists():
            fail(f"missing expected file: {path}", failures)
            continue

        text = path.read_text(encoding="utf-8")
        lowered = text.lower()

        for term in REQUIRED_TERMS:
            if term not in text:
                fail(f"{filename} missing required term: {term}", failures)

        for pattern in FORBIDDEN_PATTERNS:
            if pattern in lowered:
                fail(f"{filename} contains forbidden open-ended pattern: {pattern}", failures)

        if "dangerous" in filename or "high-impact" in text.lower():
            if "Approval Gate" not in text:
                fail(f"{filename} must include Approval Gate", failures)

    if failures:
        print(f"Loop fixture validation failed: {len(failures)} issue(s).")
        return 1

    print("Loop fixture validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
