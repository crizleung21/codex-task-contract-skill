# Release Process

## v0.4.0 Release Goal

v0.4.0 is a core-function release that adds multi-agent subagent delegation support, incorporates a loop regression test runner, centralizes release parameters in a single configuration file, aligns schemas and plugin manifests, and establishes complete snapshot test coverage.

It should ship:
- Centralized configuration file `config/release.json`;
- Upgraded task-contract Skill with multi-agent sub-contracting;
- Loop regression test runner `scripts/test-loop-runner.py`;
- Complete snapshot test coverage (12 files) under `skills/task-contract/tests/snapshots/`;
- Documentation for behavior contract `docs/behavior-contract.md` and v0.4.0 release checklist `docs/v0.4.0-release-checklist.md`;
- Plugin manifest version `0.4.0`.

## Pre-Release Checklist

- [ ] README is updated for v0.4.0.
- [ ] `IMPLEMENTATION__PLAN.md` is v0.4.0.
- [ ] Plugin manifest version is `0.4.0`.
- [ ] Plugin package is synced.
- [ ] Draft schemas exist and validate.
- [ ] Loop fixtures validate.
- [ ] Documentation validates.
- [ ] Snapshot protocol validates.
- [ ] Loop regression runner passes.
- [ ] GitHub Actions workflow exists and passes.
- [ ] Changelog includes v0.4.0 notes.
- [ ] `docs/v0.4.0-release-checklist.md` is complete.

## Validation Commands

Run from the repository root:

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

## Manifest Note

Repository validation checks local package invariants only. It does not claim official plugin schema compliance unless verified against an authoritative schema.

## Release Review Order

1. Review v0.4.0 implementation plan.
2. Review multi-agent sub-contracting integration in `SKILL.md`.
3. Review draft schemas and behavior contract.
4. Review validators and loop regression runner.
5. Review snapshot test coverage.
6. Sync plugin package.
7. Run local validation.
8. Confirm CI is green.
9. Review final diff.
10. Create the release only after human review.

## GitHub Release Notes Draft

Title:

```text
v0.4.0 — Core Subagent Delegation and Loop Validation
```

Body:

```md
## Added

- Multi-agent sub-contracting integration into the canonical task-contract Skill.
- Centralized release configuration file `config/release.json`.
- Behavior contract documentation `docs/behavior-contract.md`.
- Subagent delegation task fixture and expected output.
- Snapshot files for all 12 expected fixtures.
- Loop regression test runner in CI and local validation.

## Changed

- Upgraded active release target and all active files to v0.4.0.
- Centralized validation scripts to read from release configuration.
- Aligned expected output schema modes and plugin manifest.
- Strengthened validators to fail on placeholders.
- Moved historical release checklist to `docs/archive/`.

## Notes

The v0.4.0 schemas are draft schemas. Official plugin schema validation remains deferred until an authoritative schema source is verified.
```

## Tags

Use semantic version tags:

- `v0.1.0` for Task Contract MVP.
- `v0.2.0` for stable Loop Contract Mode.
- `v0.3.0` for validation and tooling.
- `v0.4.0` for core subagent delegation and loop validation.
