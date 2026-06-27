# Testing

This project uses manual behavior fixtures and lightweight text validation.

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

## Stable Loop Rubric

Score each item 0, 1, or 2.

| Criterion | Points |
|---|---:|
| Correct mode selection | 2 |
| Objective measurable | 2 |
| Iteration unit bounded | 2 |
| Observation method concrete | 2 |
| Validation method concrete | 2 |
| Stop conditions complete | 2 |
| Max iterations appropriate | 2 |
| Escalation triggers present | 2 |
| Approval Gate correct | 2 |
| Loop Log present | 2 |
| No hidden reasoning | 2 |
| No scope creep | 2 |

Total: 24 points.

## v0.2.0 Release Threshold

- Each stable loop fixture must score at least 20 / 24.
- High-impact fixtures must pass Approval Gate regardless of score.
- No fixture may encourage open-ended looping.
- No fixture may expose hidden reasoning.

## Automated Fixture Check

Run:

```bash
bash scripts/validate-loop-contract-fixtures.sh
```

The validator checks required Loop Contract fields, high-impact Approval Gate coverage, and forbidden open-ended loop phrases.

## Fixture Coverage

| Fixture | Expected Mode |
|---|---|
| `simple-writing-task.md` | Compact Contract |
| `vague-repo-task.md` | Full Contract |
| `high-risk-refactor-task.md` | Full Contract with Approval Gate |
| `documentation-task.md` | Compact or Full Contract |
| `research-task.md` | Full Contract |
| `destructive-file-task.md` | Full Contract with Approval Gate |
| `loop-debug-task.md` | Loop Contract Mode |
| `loop-research-task.md` | Loop Contract Mode |
| `loop-documentation-task.md` | Loop Contract Mode |
| `loop-dangerous-task.md` | Loop Contract Mode with Approval Gate |
| `loop-repo-maintenance-task.md` | Loop Contract Mode |
