# codex-task-contract-skill

`codex-task-contract-skill` is an open-source Codex Skill and installable Plugin package that makes Codex clarify before it acts.

The included `task-contract` Skill converts vague, multi-step, high-impact, or iterative requests into explicit task contracts before execution.

## Status

Current release target: **v0.1.0**

v0.1.0 is the first usable release candidate. It focuses on the Task Contract MVP while keeping Loop Contract Mode available as a documented preview pattern for iterative work.

## What It Provides

- **Auto-Skeleton** for visible task framing.
- **Task Optimizer** for precise, bounded, outcome-first task rewriting.
- **Compact Contract** for simple low-impact tasks.
- **Full Contract** for complex or high-impact tasks.
- **Loop-aware Contract** preview for iterative tasks with observation, adjustment, validation, stop conditions, and approval gates.
- **Codex Plugin package** with `.codex-plugin/plugin.json`.
- **Manual fixtures** for compact, full, high-impact, and loop-aware requests.

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
6. Use Loop Contract Mode when iterative progress needs observation and stop conditions.

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

## v0.1.0 Release Check

Before tagging v0.1.0:

```bash
bash scripts/validate-repo.sh
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
git status
```

Then review `docs/v0.1.0-release-checklist.md`.

## License

MIT License.
