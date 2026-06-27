# Release Process

## v0.1.0 Release Goal

v0.1.0 is the first usable release of `codex-task-contract-skill`.

It should ship:

- canonical `task-contract` Skill source;
- compact and full task contract behavior;
- loop-aware preview behavior;
- plugin package scaffold;
- local marketplace metadata;
- manual behavior fixtures;
- validation and sync scripts;
- release-ready README and documentation.

## Pre-Release Checklist

- [ ] README is updated.
- [ ] `SKILL.md` is updated.
- [ ] References and assets are updated.
- [ ] Plugin manifest version is `0.1.0`.
- [ ] Plugin package is synced.
- [ ] Fixtures are reviewed.
- [ ] Changelog includes v0.1.0 notes.
- [ ] `docs/v0.1.0-release-checklist.md` is complete.

## Validation Commands

```bash
bash scripts/validate-repo.sh
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
git status
```

## Release Commands

Run only after review and merge:

```bash
git checkout main
git pull origin main
bash scripts/validate-repo.sh
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
git status
git add .
git commit -m "chore: sync plugin package for v0.1.0" # only if sync changed files
git tag v0.1.0
git push origin main --tags
```

## GitHub Release Notes Draft

Title:

```text
v0.1.0 — Task Contract MVP
```

Body:

```md
## Added

- Canonical `task-contract` Codex Skill.
- Auto-Skeleton task framing.
- Task Optimizer rules.
- Compact and Full Contract modes.
- Loop-aware Contract preview.
- Approval Gate for high-impact execution.
- Plugin package scaffold.
- Local marketplace metadata.
- Documentation, templates, references, fixtures, and validation scripts.

## Notes

Loop-aware behavior is included as preview coverage in v0.1.0. v0.2.0 will expand Loop Contract Mode as a stable core feature.
```

## Tags

Use semantic versions:

- `v0.1.0` for the first MVP.
- `v0.2.0` for stable Loop Contract Mode.
