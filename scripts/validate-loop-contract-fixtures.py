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

        # 1. Required terms presence
        for term in REQUIRED_TERMS:
            if term not in text:
                fail(filename + ' missing required term: ' + term, failures)

        # 2. Required columns in loop log
        for column in REQUIRED_LOG_COLUMNS:
            if column not in text:
                fail(filename + ' missing Loop Log column: ' + column, failures)

        # 3. Forbidden patterns check
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in lowered:
                fail(filename + ' contains forbidden pattern: ' + pattern, failures)

        # 4. Check placeholder-only values or empty sections
        placeholders = ['...', '[placeholder]', 'TBD', 'TODO']
        for placeholder in placeholders:
            if placeholder in text:
                fail(f'{filename} contains placeholder value "{placeholder}"', failures)

        # 5. Check if loops have iteration caps
        if 'Max Iterations' in text:
            # check that it's followed by a number or bounded description, not placeholder
            lines = text.splitlines()
            for line in lines:
                if 'Max Iterations' in line:
                    if '...' in line or 'TODO' in line or 'TBD' in line:
                        fail(f'{filename} has placeholder in Max Iterations: {line}', failures)

        # 6. High-impact loop checks
        if 'dangerous' in filename:
            if 'Approval Gate' not in text:
                fail(filename + ' must include Approval Gate', failures)
            
            # Must require Max Iterations is 1 before approval or similar
            if not any(phrase in text for phrase in ['1 before approval', 'Max Iterations is 1', 'Max Iterations of 1', 'Max Iterations: 1']):
                fail(filename + ' high-impact loop must specify Max Iterations as 1 before approval', failures)
            
            # Must state Approval Gate as blocking execution
            if not any(phrase in lowered for phrase in ['appears before execution', 'requires approval before execution', 'pause for approval', 'block', 'must pause', 'requires approval']):
                fail(filename + ' Approval Gate must state it blocks execution until approved', failures)

    if failures:
        print('Loop fixture validation failed: ' + str(len(failures)) + ' issue(s).')
        return 1

    print('Loop fixture validation passed.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
