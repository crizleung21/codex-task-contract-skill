#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_DIR = ROOT / 'skills' / 'task-contract' / 'tests' / 'expected'
SNAPSHOT_DIR = ROOT / 'skills' / 'task-contract' / 'tests' / 'snapshots'

def fail(message, failures):
    failures.append(message)
    print('FAIL: ' + message)

def validate_expected_file(path, failures):
    content = path.read_text(encoding='utf-8')
    lowered = content.lower()
    filename = path.name

    # 1. Check for Auto-Skeleton first in required sections list
    # Usually represents as:
    # 1. Auto-Skeleton
    # 2. Optimized Task
    # etc.
    if 'required sections' in lowered:
        sections_block = content.split('## Required Sections')[1].split('##')[0]
        sections = [line.strip() for line in sections_block.splitlines() if line.strip()]
        # Find the numbered items
        numbered_sections = [s for s in sections if s.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.', '11.', '12.'))]
        if numbered_sections:
            first_sec = numbered_sections[0]
            if 'auto-skeleton' not in first_sec.lower():
                fail(f"{filename}: Auto-Skeleton must be the first required section (found {first_sec})", failures)
            
            last_sec = numbered_sections[-1]
            if 'next step' not in last_sec.lower() and 'next_step' not in last_sec.lower():
                fail(f"{filename}: Next Step must be the last required section (found {last_sec})", failures)

    # 2. High-risk tasks must include Approval Gate
    high_risk_keywords = ['dangerous', 'refactor', 'destructive']
    if any(keyword in filename for keyword in high_risk_keywords):
        if 'approval gate' not in lowered and 'approval_gate' not in lowered:
            fail(f"{filename}: High-risk task expected output must require an Approval Gate", failures)

    # 3. Loop contract completeness
    if 'loop' in filename:
        required_loop_terms = [
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
        for term in required_loop_terms:
            if term not in content:
                fail(f"{filename}: Loop expected output is missing required loop term: {term}", failures)

        # High-impact loop checks
        if 'dangerous' in filename:
            if not any(phrase in content for phrase in ['1 before approval', 'Max Iterations is 1', 'Max Iterations of 1', 'Max Iterations: 1']):
                fail(f"{filename}: High-impact loop must specify Max Iterations as 1 before approval", failures)

    # 4. Subagent safety checks
    if 'subagent' in filename:
        required_subagent_fields = [
            'parent_conversation_id',
            'subagent_role',
            'scope_boundary',
            'allowed_paths',
            'forbidden_paths',
            'allowed_tools',
            'forbidden_tools',
            'recursion_lock',
            'approval_gate',
            'acceptance_criteria',
            'evidence_required',
            'return_format',
            'merge_policy',
            'failure_policy',
        ]
        for field in required_subagent_fields:
            if field not in content:
                fail(f"{filename}: Subagent expected output is missing required field: {field}", failures)
        
        # Recursion lock defaults to true
        if 'recursion_lock' in content and 'true' not in content:
            fail(f"{filename}: Subagent contract must enforce recursion_lock set to true by default", failures)

    # 5. Forbidden behavior checks
    forbidden_patterns = [
        'repeat until done',
        'keep going forever',
        'unlimited iterations',
        'no stop condition',
        'continue without approval',
        'background execution',
    ]
    for pattern in forbidden_patterns:
        if pattern in lowered:
            fail(f"{filename} contains forbidden pattern: {pattern}", failures)

    # 6. Check for placeholders
    placeholders = ['...', '[placeholder]', 'TBD', 'TODO']
    for placeholder in placeholders:
        if placeholder in content:
            fail(f"{filename} contains placeholder value '{placeholder}'", failures)

def validate_snapshot_file(path, failures):
    content = path.read_text(encoding='utf-8')
    lowered = content.lower()
    filename = path.name

    # Check for Expected Base Mode and Expected Modifiers headers
    required_headers = [
        '## Expected Base Mode',
        '## Expected Modifiers',
    ]
    for header in required_headers:
        if header not in content:
            fail(f"{filename}: Snapshot is missing required header '{header}'", failures)

    # Check subagent safety in snapshots
    if 'subagent' in filename:
        if 'recursion_lock' not in content:
            fail(f"{filename}: Subagent snapshot must require recursion_lock", failures)
        if 'allowed_paths' not in content or 'allowed_tools' not in content:
            fail(f"{filename}: Subagent snapshot must require allowed_paths and allowed_tools", failures)

    # Check for placeholders
    placeholders = ['...', '[placeholder]', 'TBD', 'TODO']
    for placeholder in placeholders:
        if placeholder in content:
            fail(f"{filename} contains placeholder value '{placeholder}'", failures)

def main():
    failures = []

    if not EXPECTED_DIR.is_dir():
        fail("Expected fixtures directory is missing", failures)
        return 1

    expected_files = list(EXPECTED_DIR.glob('*.expected.md'))
    for path in expected_files:
        validate_expected_file(path, failures)

    if not SNAPSHOT_DIR.is_dir():
        fail("Snapshot directory is missing", failures)
        return 1

    snapshot_files = list(SNAPSHOT_DIR.glob('*.snapshot.md'))
    for path in snapshot_files:
        validate_snapshot_file(path, failures)

    if failures:
        print(f"Semantic contract validation failed: {len(failures)} issue(s).")
        return 1

    print("Semantic contract validation passed.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
