# Validator Design

This document records the intended local validation scope for v0.3.0.

v0.3.0 validators are release-readiness checks. They are not a substitute for human review.

## Repository Validator

`validate-repo.py` should check:

- required file inventory;
- Skill metadata;
- plugin manifest local invariants;
- plugin version for the active release;
- fixture mode consistency;
- template inventory;
- schema inventory;
- release checklist inventory;
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
- open-ended loop phrasing is absent.

## Schema Validator

`validate-schemas.py` should check:

- required schema files exist;
- schema files parse as JSON;
- top-level schema metadata exists;
- schemas use top-level `object` type;
- schemas define non-empty required fields;
- schema descriptions state draft status.

## Documentation Validator

`validate-docs.py` should check:

- required documentation files exist;
- each required documentation file has one H1 heading;
- v0.3.0 release checklist references validation commands.

## Snapshot Protocol Validator

`run-snapshots.py` should check:

- snapshot directory exists;
- snapshot README exists;
- snapshot testing documentation exists;
- snapshot protocol terms are present.

## Boundary

Validators should remain zero-dependency unless a dependency is explicitly documented and justified.
