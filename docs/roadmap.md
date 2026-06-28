# Roadmap

## v0.1.0 — Task Contract MVP

Status: released.

- Canonical `task-contract` Skill.
- Auto-Skeleton.
- Task Optimizer.
- Compact Contract mode.
- Full Contract mode.
- Loop-aware Contract preview.
- Plugin package scaffold.
- Local marketplace metadata.
- Core docs.
- Manual fixtures.
- v0.1.0 release checklist.

## v0.2.0 — Stable Loop Contract Mode

Status: released.

- Stable loop state model.
- Expanded loop policy reference.
- Observation method reference.
- Stop condition reference.
- Escalation rule reference.
- Loop evaluation rubric.
- Compact, full, and shared loop templates.
- Stronger expected outputs.
- Loop fixture validator.
- Repository validator.
- Plugin package sync policy.
- v0.2.0 release checklist.

## v0.3.0 — Validation and Tooling

Status: released.

- GitHub Actions validation workflow.
- Draft task contract schema.
- Draft Loop Contract schema.
- Draft expected output schema.
- Draft local plugin invariant schema.
- Schema validator.
- Plugin package sync validator.
- Documentation validator.
- Snapshot protocol validator.
- Schema design documentation.
- Snapshot testing documentation.
- CI documentation.
- v0.3.0 release checklist.

## v0.4.0 — Core Subagent Delegation and Loop Validation

Status: released.

Release goal: integrate multi-agent subagent delegation support, incorporate loop regression testing in CI, centralize versioning, and complete snapshot test coverage.

- Centralized configuration file `config/release.json`.
- Upgraded task-contract Skill with multi-agent sub-contracting.
- Subagent contract markdown template and schema alignment.
- Behavior contract documentation `docs/behavior-contract.md`.
- Subagent delegation task fixture and expected output.
- Complete snapshot test coverage (12 files).
- Loop regression runner in CI.

## v0.5.0 — Behavior Validation, Mode Taxonomy, and Subagent Boundary Hardening

Status: release candidate.

Release goal: normalize contract mode taxonomy, implement semantic contract validation, centralize release target validation, verify installation with smoke testing, and harden subagent boundaries.

- Normalized contract mode taxonomy into `base_mode` and `modifiers`.
- Release consistency validator script to detect version target drift.
- Semantic contract validator to enforce behavior-level rules.
- Fixture coverage mapping with `FIXTURE_MATRIX.md`.
- Upgraded `subagent-contract.schema.json` with path, tool, evidence, merge, and failure boundaries.
- Hardened Subagent delegation policy and markdown templates.
- Installation smoke test script for packaging verification.

## Deferred (Roadmap for v0.6.0 and later)

- Official plugin schema validation after authoritative source confirmation.
- Marketplace publishing guide.
- Full live execution integration (Golden Output Harness).
- Automated changelog generator.
- Contract schema freeze (target: v1.0.0).
- General multi-skill orchestration.

## v1.0.0 — Stable Contract

- Freeze core output schema.
- Publish stable behavior spec.
- Provide migration notes.
- Add stable release examples.
