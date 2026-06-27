# codex-task-contract-skill

`codex-task-contract-skill` is an open-source Codex Skill and installable Plugin package that makes Codex clarify before it acts.

The included `task-contract` Skill converts vague, multi-step, high-impact, or iterative requests into explicit task contracts before execution.

## Status

Current release target: **v0.2.0**

v0.2.0 stabilizes Loop Contract Mode as a core feature. It promotes the v0.1.0 loop-aware preview into a bounded task-control protocol for iterative work.

## What It Provides

- **Auto-Skeleton** for visible task framing.
- **Task Optimizer** for precise, bounded, outcome-first task rewriting.
- **Compact Contract** for simple low-impact tasks.
- **Full Contract** for complex or high-impact tasks.
- **Stable Loop Contract Mode** for iterative tasks with objective, iteration unit, observation method, adjustment strategy, validation method, stop conditions, max iterations, escalation triggers, approval gates, and Loop Log.
- **Codex Plugin package** with `.codex-plugin/plugin.json`.
- **Manual fixtures and validator** for compact, full, high-impact, and stable loop requests.

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

## Project Structure

```text
skills/task-contract/             Canonical Codex Skill source
skills/task-contract/references/  Extended behavior rules
skills/task-contract/assets/      Output templates and examples
skills/task-contract/tests/       Manual behavior fixtures
plugin/codex-task-contract-skill/ Installable Codex Plugin package
docs/                             Human-facing documentation
scripts/                          Maintenance and validation scripts
```

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
