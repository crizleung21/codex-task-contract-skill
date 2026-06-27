# Validator Design

This document records the local validation scope for v0.4.0.

v0.4.0 validators are release-readiness checks. They are not a substitute for human review.

## Configuration-Driven Validation

All validator scripts must read version targets, schema versions, and directory paths from the central release config file `config/release.json`. Hardcoded version constants in validators are prohibited.

## Repository Validator

`validate-repo.py` should check:
- required file inventory (including `IMPLEMENTATION__PLAN.md`, `config/release.json`, and `docs/behavior-contract.md`);
- Skill metadata;
- plugin manifest local invariants;
- plugin version matches `config/release.json` release target;
- fixture mode consistency;
- template inventory;
- schema inventory;
- release checklist inventory (matching active `v0.4.0-release-checklist.md`);
- CI workflow inventory;
- snapshot protocol inventory.

## Plugin Sync Validator

`validate-plugin-sync.py` should check:
- canonical Skill directory exists;
- packaged Skill directory exists;
- file lists match;
- file contents match;
- drift paths are printed when mismatches exist.

## Loop Fixture Validator

`validate-loop-contract-fixtures.py` should check:
- loop expected files exist;
- required Loop Contract fields are present;
- Loop Log columns are present;
- Stop Conditions are present;
- Escalation Triggers are present;
- Approval Gate appears for high-impact fixtures;
- open-ended loop phrasing is absent;
- no sections are empty or contain placeholder values (e.g. `...`, `[placeholder]`, `TBD`, `TODO`).

## Schema Validator

`validate-schemas.py` should check:
- required schema files exist;
- schema files parse as JSON;
- top-level schema metadata exists;
- schemas use top-level `object` type;
- schemas define non-empty required fields;
- schema descriptions state draft status;
- `schema_version` defaults match `config/release.json`'s `schema_version`.

## Documentation Validator

`validate-docs.py` should check:
- required documentation files exist (including `docs/behavior-contract.md`);
- each required documentation file has one H1 heading;
- active checklist filename and content match the release target.

## Snapshot Protocol Validator

`run-snapshots.py` should check:
- snapshot directory exists;
- snapshot README exists;
- snapshot testing documentation exists;
- every expected fixture has a corresponding snapshot file in `skills/task-contract/tests/snapshots/`;
- no snapshot file contains placeholder content or empty required sections.

## Loop Regression Test Runner

`test-loop-runner.py` should check:
- mock loop states simulate the contract runner behavior;
- the execution correctly evaluates stop conditions (e.g., success, max iterations, approval required, or repeated error);
- recursion locks and subagent delegation logs are verified;
- high-impact loops stop after one iteration when approval is required.

## Boundary

Validators should remain zero-dependency unless a dependency is explicitly documented and justified.
