# Release Process

## v0.2.0 Release Goal

v0.2.0 stabilizes Loop Contract Mode as a core feature of `task-contract`.

It should ship:

- stable Loop Contract Mode;
- loop state model;
- observation method reference;
- stop condition reference;
- escalation rule reference;
- evaluation rubric;
- full and compact loop templates;
- expanded loop expected outputs;
- loop fixture validator;
- migration guide;
- v0.2.0 release checklist;
- plugin manifest version `0.2.0`.

## Pre-Release Checklist

- [ ] README is updated.
- [ ] `SKILL.md` is updated.
- [ ] Loop references and assets are updated.
- [ ] Plugin manifest version is `0.2.0`.
- [ ] Plugin package is synced.
- [ ] Loop fixtures are reviewed.
- [ ] Changelog includes v0.2.0 notes.
- [ ] `docs/v0.2.0-release-checklist.md` is complete.

## Validation Commands

```bash
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
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
bash scripts/validate-loop-contract-fixtures.sh
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
git status
git add .
git commit -m "chore: sync plugin package for v0.2.0" # only if sync changed files
git tag v0.2.0
git push origin main --tags
```

## GitHub Release Notes Draft

Title:

```text
v0.2.0 — Stable Loop Contract Mode
```

Body:

```md
## Added

- Stable Loop Contract Mode.
- Loop state model.
- Loop observation method reference.
- Loop stop condition taxonomy.
- Loop escalation rules.
- Loop evaluation rubric.
- Full and compact Loop Contract templates.
- Expanded Loop Log template.
- Expanded loop golden expected outputs.
- Loop fixture validator script.
- v0.2.0 release checklist.
- Migration guide from v0.1.0 to v0.2.0.

## Changed

- Promoted Loop-aware preview into stable Loop Contract Mode.
- Updated plugin manifest to `0.2.0`.
- Standardized terminology around Approval Gate and Adjustment Strategy.
```

## Tags

Use semantic versions:

- `v0.1.0` for the first MVP.
- `v0.2.0` for stable Loop Contract Mode.
