# Release Process

## v0.5.0 Release Goal

v0.5.0 is a behavior-strengthening release that normalizes contract mode taxonomy, implements semantic contract validation, centralizes release target validation, verifies installation layout with smoke testing, and hardens subagent delegation boundaries.

It should ship:
- Normalized mode taxonomy in `base_mode` and `modifiers`;
- Centralized release target validation via `scripts/validate-release-consistency.py`;
- Behavior-level semantic validator `scripts/validate-contract-semantics.py`;
- Coverage matrix document `skills/task-contract/tests/FIXTURE_MATRIX.md`;
- Hardened `schemas/subagent-contract.schema.json` with path, tool, evidence, merge, and failure boundaries;
- Updated subagent delegation policy and templates;
- Installation smoke test script `scripts/smoke-test-installation.sh`;
- Packaged plugin manifest version `0.5.0`.

## Pre-Release Checklist

- [ ] README is updated for v0.5.0.
- [ ] `IMPLEMENTATION__PLAN.md` is v0.5.0.
- [ ] Plugin manifest version is `0.5.0`.
- [ ] Plugin package is synced.
- [ ] Draft schemas exist and validate.
- [ ] Loop fixtures validate.
- [ ] Release consistency validates.
- [ ] Documentation validates.
- [ ] Snapshot protocol validates.
- [ ] Loop regression runner passes.
- [ ] Semantic contract validation passes.
- [ ] Installation smoke test passes.
- [ ] GitHub Actions workflow exists and passes.
- [ ] Changelog includes v0.5.0 notes.
- [ ] `docs/v0.5.0-release-checklist.md` is complete.

## Validation Commands

Run from the repository root:

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

## Manifest Note

Repository validation checks local package invariants only. It does not claim official plugin schema compliance unless verified against an authoritative schema.

## Release Review Order

1. Review v0.5.0 implementation plan.
2. Review normalized mode taxonomy across schemas and validators.
3. Review release consistency and semantic contract validators.
4. Review fixture coverage matrix in `FIXTURE_MATRIX.md`.
5. Review hardened subagent contract fields and policy.
6. Sync plugin package.
7. Run local validation.
8. Confirm CI is green.
9. Review final diff.
10. Create the release only after human review.

## GitHub Release Notes Draft

Title:

```text
v0.5.0 — Behavior Validation, Mode Taxonomy, and Subagent Boundary Hardening
```

Body:

```md
## Added

- Semantic contract validator script `scripts/validate-contract-semantics.py`.
- Release consistency validator script `scripts/validate-release-consistency.py`.
- Installation smoke test script `scripts/smoke-test-installation.sh`.
- Fixture matrix mapping document `skills/task-contract/tests/FIXTURE_MATRIX.md`.
- Subagent delegation usage examples to documentation.

## Changed

- Upgraded release target and all active files to v0.5.0.
- Normalized contract mode taxonomy across schemas, validators, fixtures, docs, and snapshots using `base_mode` and `modifiers`.
- Strengthened `schemas/subagent-contract.schema.json` with allowed/forbidden paths and tools, handoff inputs, evidence requirements, merge policy, and failure policy.
- Hardened Subagent delegation policy and template in `skills/task-contract/references/subagent-delegation-policy.md` and `skills/task-contract/assets/subagent-contract-template.md`.
- Improved CI and local validation parity by aligning validator scripts and execution order.

## Notes

The v0.5.0 schemas are draft schemas. Official plugin schema validation remains deferred until an authoritative schema source is verified.
```

## Tags

Use semantic version tags:

- `v0.1.0` for Task Contract MVP.
- `v0.2.0` for stable Loop Contract Mode.
- `v0.3.0` for validation and tooling.
- `v0.4.0` for core subagent delegation and loop validation.
- `v0.5.0` for behavior validation, mode taxonomy, and subagent boundary hardening.
