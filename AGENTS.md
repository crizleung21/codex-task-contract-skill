# AGENTS.md

This repository contains one canonical Codex Skill: `task-contract`.

## Core Rule

Clarify before action. Preserve user intent, bound scope, define output, and state acceptance criteria before execution.

## Canonical Source

Canonical Skill source lives under:

```text
skills/task-contract/
```

The plugin package copy lives under:

```text
plugin/codex-task-contract-skill/skills/task-contract/
```

Update canonical source first. Then sync the plugin package.

## v0.5.0 Release Gates

Before release review, run:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-release-consistency.py
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
python3 scripts/validate-contract-semantics.py
bash scripts/smoke-test-installation.sh
git status
```

The package copy must match canonical source after sync.

## Schema Policy

Schemas under `schemas/` are v0.5.0 draft schemas. They are not v1.0.0 frozen public contracts and are not official plugin schema compliance claims.

## CI Policy

The CI workflow must mirror the local validation sequence. Do not tag a release until CI is green.

## Snapshot Policy

Snapshot protocol files live under:

```text
skills/task-contract/tests/snapshots/
```

Snapshots validate expected structure, not exact prose, unless exact prose is intentionally part of the behavior contract.

## Approval Boundary

Pause for approval before broad repository changes, public behavior changes, release metadata changes, dependency changes, file deletion, security posture changes, large refactors, commits, pushes, tags, releases, pull requests, or high-impact loop execution.

## Loop Boundary

Loop Contract Mode must use a finite max iteration count, visible observation evidence, validation method, stop conditions, escalation triggers, and a concise Loop Log.

## Documentation Policy

Keep repository documentation and Skill instructions English-only.

## Style

- Prefer precise, bounded edits.
- Update fixtures when behavior changes.
- Keep P2 expansion work in the roadmap.
- Do not edit packaged Skill files directly unless maintaining sync tooling or repairing validated drift.
