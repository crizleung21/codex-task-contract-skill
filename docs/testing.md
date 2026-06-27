# Testing

This project uses manual behavior fixtures for v0.1.0.

## Fixture Layout

```text
skills/task-contract/tests/fixtures/   Input prompts
skills/task-contract/tests/expected/   Expected output patterns
```

## Manual Test Protocol

1. Start Codex in a clean session.
2. Invoke `$task-contract`.
3. Paste a fixture prompt.
4. Record the output.
5. Compare with the expected output.
6. Score the result using the rubric below.

## v0.1.0 Rubric

Score each item 0, 1, or 2.

| Criterion | Pass Requirement |
|---|---|
| Auto-Skeleton | Required fields are present. |
| Intent preservation | Optimized Task does not change user goal. |
| Scope control | Scope is bounded and exclusions are clear. |
| Output Contract | Deliverable, format, depth, and acceptance criteria are stated. |
| Decision Points | Meaningful choices appear when needed. |
| Approval Gate | High-impact work pauses before execution. |
| Concision | Compact mode remains short. |
| Loop-aware fields | Loop fixtures include objective, observation, validation, stop condition, and iteration cap. |
| No hidden reasoning | Output does not expose hidden reasoning. |

## Release Threshold

For v0.1.0 release readiness:

- Compact and Full fixtures should score at least 14 / 18.
- High-impact fixtures must pass Approval Gate.
- Loop-aware fixtures must include stop condition and iteration cap.
- No fixture may expose hidden reasoning.

## Fixture Coverage

| Fixture | Expected Mode |
|---|---|
| `simple-writing-task.md` | Compact Contract |
| `vague-repo-task.md` | Full Contract |
| `high-risk-refactor-task.md` | Full Contract with Approval Gate |
| `documentation-task.md` | Compact or Full Contract |
| `research-task.md` | Full Contract |
| `destructive-file-task.md` | Full Contract with Approval Gate |
| `loop-debug-task.md` | Loop-aware Contract |
| `loop-research-task.md` | Loop-aware Contract |
| `loop-documentation-task.md` | Loop-aware Contract |
| `loop-dangerous-task.md` | Loop-aware Contract with Approval Gate |
