# codex-task-contract-skill

`codex-task-contract-skill` is an open-source Codex Skill and installable Plugin package that makes Codex clarify before it acts.

The included `task-contract` skill converts vague, multi-step, risky, high-impact, or iterative requests into explicit task contracts before execution.

## What It Provides

- **Auto-Skeleton** for visible task framing.
- **Task Optimizer** for precise, bounded, outcome-first task rewriting.
- **Compact Contract** for simple low-risk tasks.
- **Full Contract** for complex, ambiguous, or high-impact tasks.
- **Loop Contract Mode** planned for v0.2.0, turning single prompts into bounded agent loops with observation, repair, validation, stop conditions, iteration limits, and risk gates.
- **Codex Plugin packaging** for installable distribution.

## Repository Status

This repository is initialized from `IMPLEMENTATION__PLAN.md`.

- v0.1.0: Task Contract MVP.
- v0.2.0: Loop Contract Mode extension.

## Quick Usage

Explicit invocation:

```text
Use $task-contract to clarify this request before editing files.
```

Expected behavior:

1. Build an Auto-Skeleton.
2. Rewrite the task into an Optimized Task.
3. Define constraints and output contract.
4. Add decision points when intent may change.
5. Apply a Risk Gate before high-impact actions.
6. Use Loop Contract Mode for iterative goal-seeking tasks.

## Project Structure

```text
skills/task-contract/            Canonical Codex Skill source
plugin/codex-task-contract-skill/ Installable Codex Plugin package
docs/                            Human-facing documentation
scripts/                         Maintenance and validation scripts
```

## License

MIT License.
