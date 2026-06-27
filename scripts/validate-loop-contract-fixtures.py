#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / 'skills' / 'task-contract' / 'tests' / 'expected'

REQUIRED_FILES = [
    'loop-debug-task.expected.md',
    'loop-research-task.expected.md',
    'loop-documentation-task.expected.md',
    'loop-dangerous-task.expected.md',
    'loop-repo-maintenance-task.expected.md',
]

REQUIRED_TERMS = [
    'Loop Objective',
    'Loop Type',
    'Iteration Unit',
    'Observation Method',
    'Adjustment Strategy',
    'Validation Method',
    'Stop Conditions',
    'Max Iterations',
    'Escalation Triggers',
    'Approval Gate',
    'Loop Log',
]

REQUIRED_LOG_COLUMNS = [
    'Iteration',
    'Action',
    'Observation',
    'Adjustment',
    'Validation',
    'Status',
]

FORBIDDEN_PATTERNS = [
    'repeat until done',
    'keep going forever',
    'unlimited iterations',
    'no stop condition',
    'continue without approval',
    'background execution',
]

def fail(message, failures):
    failures.append(message)
    print('FAIL: ' + message)

def main():
    failures = []

    for filename in REQUIRED_FILES:
        path = EXPECTED / filename
        if not path.exists():
            fail('missing expected file: ' + str(path), failures)
            continue

        text = path.read_text(encoding='utf-8')
        lowered = text.lower()

        for term in REQUIRED_TERMS:
            if term not in text:
                fail(filename + ' missing required term: ' + term, failures)

        for column in REQUIRED_LOG_COLUMNS:
            if column not in text:
                fail(filename + ' missing Loop Log column: ' + column, failures)

        for pattern in FORBIDDEN_PATTERNS:
            if pattern in lowered:
                fail(filename + ' contains forbidden pattern: ' + pattern, failures)

        if 'dangerous' in filename or 'high-impact' in lowered:
            if 'Approval Gate' not in text:
                fail(filename + ' must include Approval Gate', failures)

    if failures:
        print('Loop fixture validation failed: ' + str(len(failures)) + ' issue(s).')
        return 1

    print('Loop fixture validation passed.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
