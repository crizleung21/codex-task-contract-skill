# Testing

This project uses manual behavior fixtures, snapshot coverage, and lightweight text validation.

## Fixture Layout

```text
skills/task-contract/tests/fixtures/    Input prompts
skills/task-contract/tests/expected/    Expected output patterns
skills/task-contract/tests/snapshots/   Snapshot protocol files
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
| Private reasoning not revealed | 2 |
| No scope creep | 2 |

Total: 24 points.

## v0.4.0 Release Threshold

- Each stable loop fixture must score at least 20 / 24.
- High-impact fixtures must pass Approval Gate regardless of score.
- No fixture may encourage open-ended looping.
- No fixture may expose private reasoning.
- Schema validation must pass.
- Documentation validation must pass.
- Snapshot protocol validation must pass.
- Loop regression test runner must pass.
- Plugin package sync validation must pass.

## Automated Checks

Run:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
```

The validators check required files, plugin sync drift, required Loop Contract fields, high-impact Approval Gate coverage, open-ended loop phrasing, schema structure, documentation inventory, snapshot protocol completeness, and loop regression execution.

## Fixture Coverage

| Fixture | Expected Mode |
|---|---|
| `simple-writing-task.md` | Compact Contract |
| `vague-repo-task.md` | Full Contract |
| `high-risk-refactor-task.md` | Full Contract with Approval Gate |
| `documentation-task.md` | Full Contract |
| `research-task.md` | Full Contract |
| `destructive-file-task.md` | Full Contract with Approval Gate |
| `loop-debug-task.md` | Loop Contract Mode |
| `loop-research-task.md` | Loop Contract Mode |
| `loop-documentation-task.md` | Loop Contract Mode |
| `loop-dangerous-task.md` | Loop Contract Mode with Approval Gate |
| `loop-repo-maintenance-task.md` | Loop Contract Mode |
| `subagent-delegation-task.md` | Full Contract with Subagent Delegation |

## Expected Output File Format

Each expected output file should include:

1. Mode
2. Required Sections
3. Required Fields
4. Required Checks
5. Forbidden Patterns, when useful

## Snapshot Protocol

Snapshot protocol is documented in `docs/snapshot-testing.md` and `skills/task-contract/tests/snapshots/README.md`.

v0.4.0 snapshot validation checks that snapshot files exist for all fixtures and contain no placeholder content. A full automated model-output runtime execution harness remains deferred.

## Git Pre-commit Hook Integration

To ensure all repository validations are executed before any changes are committed, developers should install the Git pre-commit hook by running:

```bash
bash scripts/install-git-hooks.sh
```

### Automatic Validation Gates
Once installed, executing `git commit` triggers the following automated validation sequence:
1. **Plugin Package Sync check**: Copy canonical files and verify no package sync drift.
2. **Repository Validator**: Verify file inventories and key configurations.
3. **Loop Fixture Validator**: Inspect loop contract formatting, stops, and safe boundaries.
4. **Schema Validator**: Confirm schema drafts parse correctly.
5. **Documentation Validator**: Check heading syntax and document inventory.
6. **Snapshot Runner**: Validate versioned snapshots and protocols.
7. **Loop Regression Test Runner**: Verify loop contract trajectories using mock state sequences.

If any check fails, the commit is blocked and the error is printed.

### Bypassing Checks
In emergency scenarios where a commit must bypass validations, append `--no-verify` to your commit command:

```bash
git commit --no-verify
```

## Loop Regression Testing

The repository provides a dynamic loop regression testing tool:

```bash
python3 scripts/test-loop-runner.py
```

It reads mock loop state transitions and contract definitions from `skills/task-contract/tests/loop-regression-tests.json` and simulates the run, validating that the execution stops at the expected iteration due to the expected stop condition (e.g., success, max iterations, approval required, or repeated error).

To add a test case, edit the JSON file and append a case conforming to the schema definition.
