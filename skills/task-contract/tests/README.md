# Test Fixtures

This directory contains manual behavior tests for the `task-contract` Skill.

## Layout

```text
fixtures/   Input prompts
expected/   Expected output patterns
```

## Protocol

1. Invoke `$task-contract`.
2. Paste a fixture prompt.
3. Compare the result with the expected output.
4. Score loop outputs with `references/loop-evaluation-rubric.md`.
5. Update expected files only when behavior intentionally changes.

## Loop Fixture Validation

Run:

```bash
bash scripts/validate-loop-contract-fixtures.sh
```

The validator checks that loop expected outputs contain the stable v0.2.0 Loop Contract fields and do not encourage open-ended loops.

## Stable Loop Expected Fields

Every loop expected output should include:

- Loop Objective
- Loop Type
- Iteration Unit
- Observation Method
- Adjustment Strategy
- Validation Method
- Stop Conditions
- Max Iterations
- Escalation Triggers
- Loop Log
- Approval Gate when applicable
