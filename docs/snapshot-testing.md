# Snapshot Testing

Status: v0.4.0 snapshot protocol.

Snapshot testing in this repository validates stable expected output structure, not exact natural-language prose.

The goal is to make release review easier by recording which sections, fields, checks, and forbidden patterns are expected for each fixture.

## Snapshot Scope

Snapshots may capture:
- expected mode;
- required sections;
- required Loop Contract fields;
- required Loop Log columns;
- approval requirements;
- forbidden open-ended loop patterns;
- reviewer notes.

Snapshots should not overfit exact wording unless a phrase is itself part of the behavior contract.

## Directory

```text
skills/task-contract/tests/snapshots/
```

Each expected fixture file must have a corresponding snapshot file.

Recommended naming:

```text
<fixture-name>.snapshot.md
```

Example:

```text
loop-debug-task.snapshot.md
```

## Review Rules

Snapshot changes require reviewer attention when they:
1. add or remove required sections;
2. change expected mode;
3. weaken approval gate requirements;
4. remove stop conditions;
5. remove escalation triggers;
6. change iteration cap expectations;
7. change forbidden open-ended loop patterns.

## Validation

Run:

```bash
python3 scripts/run-snapshots.py
```

The v0.4.0 runner validates that the snapshot directory policy file exists, a snapshot file exists for every fixture, and each snapshot file contains expected sections without placeholder content. A full automated model-output runtime execution harness remains deferred.

## Boundary

Snapshot protocol in v0.4.0 is a release-readiness aid. It is not a full automated model-output harness.
