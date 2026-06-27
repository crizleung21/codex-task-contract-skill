# codex-task-contract-skill

`codex-task-contract-skill` is an open-source Codex Skill and installable Plugin package that makes Codex clarify before it acts.

The included `task-contract` Skill converts vague, multi-step, high-impact, or iterative requests into explicit task contracts before execution.

## Status

Current release target: **v0.2.0**

v0.2.0 stabilizes Loop Contract Mode as a core feature and applies the P0 + P1 remediation scope documented in `IMPLEMENTATION__PLAN.md`. P2 expansion items are deferred to the roadmap.

## What It Provides

- **Auto-Skeleton** for visible task framing.
- **Task Optimizer** for precise, bounded, outcome-first task rewriting.
- **Compact Contract** for simple low-impact tasks.
- **Full Contract** for complex, ambiguous, repo-level, public-facing, or high-impact tasks.
- **Stable Loop Contract Mode** for iterative tasks with objective, iteration unit, observation method, adjustment strategy, validation method, stop conditions, max iterations, escalation triggers, Approval Gate, and Loop Log.
- **Approval Gate** before broad repository changes, public behavior changes, release metadata changes, dependency changes, destructive cleanup, security posture changes, commits, pushes, tags, releases, pull requests, or high-impact loop execution.
- **Codex Plugin package** with `.codex-plugin/plugin.json`.
- **Manual fixtures and validators** for compact, full, high-impact, and stable loop requests.

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
skills/task-contract/tests/       Manual behavior fixtures
plugin/codex-task-contract-skill/ Installable Codex Plugin package
docs/                             Human-facing and maintainer documentation
scripts/                          Maintenance, sync, and validation scripts
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

Do not manually edit the packaged Skill copy unless you are updating sync tooling.

## Validation

Run the full local validation sequence before release review:

```bash
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
git status
```

The validators check required files, local plugin manifest invariants, canonical/plugin sync drift, version consistency, terminology consistency, fixture determinism, loop fixture coverage, and template/checklist consistency.

## v0.2.0 Release Check

Before tagging v0.2.0:

```bash
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
git status
```

Then review `docs/v0.2.0-release-checklist.md`.

## License

MIT License.
