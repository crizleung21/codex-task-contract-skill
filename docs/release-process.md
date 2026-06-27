# Release Process

## v0.3.0 Release Goal

v0.3.0 adds validation, tooling, draft schemas, CI, snapshot protocol documentation, and release-confidence gates while preserving the v0.2.0 behavior contract.

It should ship:

- draft schemas under `schemas/`;
- schema validator;
- plugin package sync validator;
- documentation validator;
- snapshot protocol validator;
- GitHub Actions validation workflow;
- schema design documentation;
- snapshot testing documentation;
- CI documentation;
- v0.3.0 release checklist;
- plugin manifest version `0.3.0`.

## Pre-Release Checklist

- [ ] README is updated for v0.3.0.
- [ ] `IMPLEMENTATION__PLAN.md` is v0.3.0.
- [ ] Plugin manifest version is `0.3.0`.
- [ ] Plugin package is synced.
- [ ] Draft schemas exist and validate.
- [ ] Loop fixtures validate.
- [ ] Documentation validates.
- [ ] Snapshot protocol validates.
- [ ] GitHub Actions workflow exists and passes.
- [ ] Changelog includes v0.3.0 notes.
- [ ] `docs/v0.3.0-release-checklist.md` is complete.

## Validation Commands

Run from the repository root:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
git status
```

## Manifest Note

Repository validation checks local package invariants only. It does not claim official plugin schema compliance unless verified against an authoritative schema.

## Release Review Order

1. Review v0.3.0 implementation plan.
2. Review draft schemas.
3. Review validators.
4. Review CI workflow.
5. Review snapshot protocol.
6. Sync plugin package.
7. Run local validation.
8. Confirm CI is green.
9. Review final diff.
10. Create the release only after human review.

## GitHub Release Notes Draft

Title:

```text
v0.3.0 — Validation and Tooling
```

Body:

```md
## Added

- Draft schemas for task contracts, Loop Contract Mode, expected outputs, and local plugin invariants.
- Schema validator.
- Plugin package sync validator.
- Documentation validator.
- Snapshot protocol validator.
- GitHub Actions validation workflow.
- Schema design documentation.
- Snapshot testing documentation.
- CI documentation.
- v0.3.0 release checklist.

## Changed

- Updated plugin manifest to `0.3.0`.
- Updated release process around validation, CI, snapshot protocol, and release evidence.
- Preserved the v0.2.0 behavior contract while adding stronger release-readiness gates.

## Notes

The v0.3.0 schemas are draft schemas. Official plugin schema validation remains deferred until an authoritative schema source is verified.
```

## Tags

Use semantic version tags:

- `v0.1.0` for Task Contract MVP.
- `v0.2.0` for stable Loop Contract Mode.
- `v0.3.0` for validation and tooling.
