# Release Process

## v0.2.0 Release Goal

v0.2.0 stabilizes Loop Contract Mode as a core feature of `task-contract` and completes the P0 + P1 remediation scope from `IMPLEMENTATION__PLAN.md`.

It should ship:

- stable Loop Contract Mode;
- loop state model;
- observation method reference;
- stop condition reference;
- escalation rule reference;
- evaluation rubric;
- compact, full, and loop templates;
- expanded expected outputs;
- loop fixture validator;
- repository validator;
- migration guide;
- behavior and packaging docs;
- v0.2.0 release checklist;
- plugin manifest version `0.2.0`.

## Pre-Release Checklist

- [ ] README is updated.
- [ ] `SKILL.md` is updated.
- [ ] Loop references and assets are updated.
- [ ] Plugin manifest version is `0.2.0`.
- [ ] Plugin package is synced.
- [ ] Fixtures are deterministic.
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

## Manifest Note

Repository validation checks local package invariants. It does not claim official plugin schema compliance unless verified against an authoritative schema.

## Release Review Order

1. Review canonical Skill source.
2. Review loop references and templates.
3. Review expected fixtures.
4. Run validation.
5. Sync plugin package.
6. Run validation again.
7. Review final diff.
8. Create the release only after human review.

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
- Compact, full, and shared Loop Contract templates.
- Expanded Loop Log template.
- Expanded expected outputs.
- Loop fixture validator script.
- Repository validator script.
- v0.2.0 release checklist.
- Migration guide from v0.1.0 to v0.2.0.

## Changed

- Promoted Loop-aware preview into stable Loop Contract Mode.
- Updated plugin manifest to `0.2.0`.
- Standardized terminology around Approval Gate and Adjustment Strategy.
- Added canonical-source and plugin-sync rules.
```
