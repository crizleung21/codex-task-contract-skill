#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS_FILE = ROOT / 'skills' / 'task-contract' / 'tests' / 'loop-regression-tests.json'

def run_test_case(case):
    name = case['name']
    contract = case['loop_contract']
    states = case['mock_environment_states']
    expected = case['expected_stop']

    print(f"Running test case: {name}")

    loop_log = []
    stopped = False
    stop_reason = ""
    stop_iteration = 0
    prev_error_sig = None

    for idx, state in enumerate(states):
        iteration = idx + 1
        action_outcome = state['action_outcome']
        validation_passed = state['validation_passed']
        error_sig = state.get('error_sig')

        # Simulate execution log
        log_entry = {
            "iteration": iteration,
            "action": f"Executed iteration unit: {contract['iteration_unit']}",
            "observation": action_outcome,
            "adjustment": "Adjusting strategy based on observation" if not validation_passed else "None",
            "validation": "Passed" if validation_passed else "Failed",
            "status": "Complete" if validation_passed else "In progress"
        }
        loop_log.append(log_entry)

        # Check success condition
        if validation_passed:
            stopped = True
            stop_reason = "acceptance criteria met"
            stop_iteration = iteration
            break

        # Check same failure repeats twice condition
        if error_sig and prev_error_sig and error_sig == prev_error_sig:
            stopped = True
            stop_reason = "same failure repeats twice"
            stop_iteration = iteration
            break

        prev_error_sig = error_sig

        # Check max iterations condition
        if iteration >= contract['max_iterations']:
            stopped = True
            stop_reason = "max iterations reached"
            stop_iteration = iteration
            break

    # If sequence finished without an explicit stop condition being triggered, check if we hit the end of state array
    if not stopped:
        stop_iteration = len(states)
        stop_reason = "max iterations reached" if stop_iteration >= contract['max_iterations'] else "no more states"

    # Verify stop iteration and reason
    if stop_iteration != expected['iteration']:
        print(f"FAIL: {name} - expected stop iteration {expected['iteration']}, got {stop_iteration}")
        return False
    if stop_reason != expected['reason']:
        print(f"FAIL: {name} - expected stop reason '{expected['reason']}', got '{stop_reason}'")
        return False

    print(f"PASS: {name} - stopped at iteration {stop_iteration} due to '{stop_reason}'")
    return True

def main():
    if not TESTS_FILE.exists():
        print(f"FAIL: {TESTS_FILE} does not exist.")
        return 1

    try:
        data = json.loads(TESTS_FILE.read_text(encoding='utf-8'))
    except Exception as e:
        print(f"FAIL: failed to parse test file JSON: {e}")
        return 1

    failures = 0
    for case in data.get('test_cases', []):
        if not run_test_case(case):
            failures += 1

    if failures:
        print(f"Regression tests failed: {failures} test case(s) failed.")
        return 1

    print("All loop regression tests passed.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
