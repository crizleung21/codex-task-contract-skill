# Snapshot Testing

Status: v0.3.0 snapshot protocol.

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

Each snapshot file should correspond to a fixture or fixture family.

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

The v0.3.0 runner validates the snapshot protocol and confirms the snapshot directory policy file exists. Full golden-output runtime execution is deferred to a future release.

## Boundary

Snapshot protocol in v0.3.0 is a release-readiness aid. It is not a full automated model-output harness.
