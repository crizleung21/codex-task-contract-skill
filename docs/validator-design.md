# Validator Design

This document records the local validation scope for v0.5.0.

v0.5.0 validators are release-readiness checks. They are not a substitute for human review.

## Configuration-Driven Validation

All validator scripts must read version targets, schema versions, and directory paths from the central release config file `config/release.json`. Hardcoded version constants in validators are prohibited.

## Repository Validator

`validate-repo.py` should check:
- required file inventory (including `IMPLEMENTATION__PLAN.md`, `config/release.json`, and `docs/behavior-contract.md`);
- Skill metadata;
- plugin manifest local invariants;
- plugin version matches `config/release.json` release target;
- fixture mode consistency (using `base_mode` and `modifiers` taxonomy);
- template inventory;
- schema inventory;
- release checklist inventory (matching active `v0.5.0-release-checklist.md`);
- CI workflow inventory;
- snapshot protocol inventory;
- fixture matrix file `FIXTURE_MATRIX.md`.

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

## Release Consistency Validator

`validate-release-consistency.py` should check:
- plugin manifest version matches release configuration;
- schema version defaults match release configuration;
- active release checklist exists;
- active documentation and scripts do not contain stale release gate or check references to previous versions;
- CI validation steps include all v0.5.0 checks.

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
- snapshot headers check for `## Expected Base Mode` and `## Expected Modifiers`;
- no snapshot file contains placeholder content or empty required sections.

## Loop Regression Test Runner

`test-loop-runner.py` should check:
- mock loop states simulate the contract runner behavior;
- the execution correctly evaluates stop conditions (e.g., success, max iterations, approval required, or repeated error);
- recursion locks and subagent delegation logs are verified;
- high-impact loops stop after one iteration when approval is required.

## Semantic Contract Validator

`validate-contract-semantics.py` should check:
- every fixture output has an Auto-Skeleton first;
- every fixture output ends with a singular clear next step;
- high-risk tasks require Approval Gates;
- loop fixtures specify max iteration caps and stop conditions;
- subagent delegation contracts require all boundary metadata (recursion locks, allowed/forbidden paths and tools, evidence required, merge and failure policies).

## Installation Smoke Tester

`smoke-test-installation.sh` should check:
- packaged plugin folder structure exists;
- plugin manifest matches configuration;
- local marketplace plugins list matches target;
- plugin sync validation passes;
- release consistency checks pass.

## Boundary

Validators should remain zero-dependency unless a dependency is explicitly documented and justified.
