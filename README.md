# codex-task-contract-skill

`codex-task-contract-skill` is an open-source Codex Skill and installable Plugin package that makes Codex clarify before it acts.

The included `task-contract` Skill converts vague, multi-step, high-impact, or iterative requests into explicit task contracts before execution.

## Status

Current release target: **v0.4.0**

v0.4.0 adds validation, tooling, draft schemas, CI, Git pre-commit hooks, loop regression tests, subagent delegation policies, and stronger release-readiness gates.

## What It Provides

- **Auto-Skeleton** for visible task framing.
- **Task Optimizer** for precise, bounded, outcome-first task rewriting.
- **Compact Contract** for simple low-impact tasks.
- **Full Contract** for complex, ambiguous, repo-level, public-facing, or high-impact tasks.
- **Stable Loop Contract Mode** for iterative tasks with objective, iteration unit, observation method, adjustment strategy, validation method, stop conditions, max iterations, escalation triggers, Approval Gate, and Loop Log.
- **Multi-Agent Sub-contracting** for task delegation with scope-bounded subagent contracts, parent references, and loop log syncing.
- **Approval Gate** before broad repository changes, public behavior changes, release metadata changes, dependency changes, destructive cleanup, security posture changes, commits, pushes, tags, releases, pull requests, or high-impact loop execution.
- **Draft schemas** for task contracts, Loop Contract Mode, expected outputs, subagent contracts, and local plugin invariants.
- **CI-ready validators** and **Regression test runner** for repository structure, plugin package sync, loop fixtures, schemas, docs, loop trajectories, and snapshot protocol.
- **Codex Plugin package** with `.codex-plugin/plugin.json`.

## Quick Usage

```text
Use $task-contract to clarify this request before editing files.
```

Expected behavior:

1. Build an Auto-Skeleton.
2. Rewrite the request into an Optimized Task.
3. Define constraints and an Output Contract.
4. Add Decision Points when a choice may change the outcome.
5. Apply an Approval Gate before high-impact execution.
6. Use Loop Contract Mode when iterative progress needs observation, validation, stop conditions, and iteration limits.
7. End with one clear next step.

## Project Structure

```text
skills/task-contract/             Canonical Codex Skill source
skills/task-contract/references/  Extended behavior rules
skills/task-contract/assets/      Output templates and examples
skills/task-contract/tests/       Manual behavior fixtures and snapshots
plugin/codex-task-contract-skill/ Installable Codex Plugin package
docs/                             Human-facing and maintainer documentation
schemas/                          v0.3.0 draft schemas
scripts/                          Maintenance, sync, and validation scripts
.github/workflows/                CI validation workflow
```

## Canonical Source and Plugin Sync

Canonical Skill source lives under:

```text
skills/task-contract/
```

The plugin package copy lives under:

```text
plugin/codex-task-contract-skill/skills/task-contract/
```

Update canonical source first, then sync the plugin package:

```bash
bash scripts/sync-plugin-package.sh
```

Do not manually edit the packaged Skill copy unless you are updating sync tooling or repairing drift identified by validation.

## Validation

Run the full local validation sequence before release review:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
git status
```

The validators check required files, local plugin manifest invariants, canonical/plugin sync drift, version consistency, terminology consistency, fixture determinism, loop fixture coverage, schema structure, documentation inventory, and snapshot protocol readiness.

## CI

GitHub Actions validation is defined in:

```text
.github/workflows/validate.yml
```

The workflow runs the same release-readiness checks used locally.

## v0.3.0 Release Check

Before tagging v0.3.0:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
git status
```

## Git Pre-commit Hooks

To prevent committing malformed schemas, un-synced plugin package folders, invalid documentation formatting, or failing loop fixtures, you can install the Git pre-commit hook:

```bash
bash scripts/install-git-hooks.sh
```

Once installed, the hook will run automatically on `git commit`. To bypass the validation checks, use:

```bash
git commit --no-verify
```

## License

MIT License.
