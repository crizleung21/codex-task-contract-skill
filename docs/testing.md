# Testing

This project uses manual behavior fixtures.

## Fixture Layout

```text
skills/task-contract/tests/fixtures/
skills/task-contract/tests/expected/
```

## Manual Test Protocol

1. Start Codex in a clean session.
2. Invoke `$task-contract`.
3. Paste a fixture prompt.
4. Record the output.
5. Compare with the expected output.
6. Score the result.

## Evaluation Criteria

- Auto-Skeleton is present.
- Intent is preserved.
- Scope is bounded.
- Optimized Task is clear.
- Decision Points appear when useful.
- Risk Gate appears when needed.
- Output Contract is clear.
- Loop contracts include objective, observation, and stop condition.
- No hidden reasoning is exposed.
