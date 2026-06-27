# Schema Design

Status: v0.4.0 draft schema documentation.

The schemas in `schemas/` describe the structural expectations for task contracts, Loop Contract Mode, subagent delegation contracts, expected fixture outputs, and local plugin package invariants.

These schemas are draft artifacts. They are not v1.0.0 frozen public contracts and should not be represented as official Codex or plugin marketplace schemas.

## Schema Files

| File | Purpose |
|---|---|
| `schemas/task-contract.schema.json` | Draft structure for Compact, Full, and Loop task contract outputs. |
| `schemas/loop-contract.schema.json` | Draft structure for Loop Contract Mode fields, Loop Log, stop conditions, escalation triggers, and approval gates. |
| `schemas/subagent-contract.schema.json` | Draft structure for multi-agent subagent delegation contract metadata. |
| `schemas/expected-output.schema.json` | Draft structure for expected fixture and snapshot expectation metadata. |
| `schemas/plugin-local-invariants.schema.json` | Draft local-only plugin package invariant schema. |

## Design Principles

1. Preserve and strengthen the core behavior contract.
2. Validate structural invariants, not stylistic prose.
3. Keep schemas strict enough for maintainers and flexible enough for practical output variation.
4. Avoid official plugin schema compliance claims until an authoritative schema source is verified.
5. Centralize schema versioning through `config/release.json`.

## Required Top-Level Schema Fields

Each schema should include:
- `$schema`
- `$id` (repository-local URI or file-relative identifier)
- `title`
- `description`
- `type`
- `required`
- `properties`

## Validation

Run:

```bash
python3 scripts/validate-schemas.py
```

The validator checks required schema files, JSON parsing, required top-level fields, object type, non-empty required fields, version consistency with `config/release.json`, and draft-status wording.

## Release Boundary

v0.4.0 refines draft schemas and adds subagent contract validation. v1.0.0 is the appropriate target for freezing a stable external contract schema.
