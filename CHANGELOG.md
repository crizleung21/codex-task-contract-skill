# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Planned

- P2 roadmap items for v0.6.0 and later: official plugin schema validation, marketplace publishing guidance, full golden-output execution harness, automated changelog generation, and multi-skill expansion after v1.0.0 behavior freeze.

## [0.5.0] - Release Candidate

### Added
- Semantic contract validator script `scripts/validate-contract-semantics.py`.
- Release consistency validator script `scripts/validate-release-consistency.py`.
- Installation smoke test script `scripts/smoke-test-installation.sh`.
- Fixture matrix mapping document `skills/task-contract/tests/FIXTURE_MATRIX.md`.
- Subagent delegation usage examples to documentation.

### Changed
- Upgraded release target and all active files to v0.5.0.
- Normalized contract mode taxonomy across schemas, validators, fixtures, docs, and snapshots using `base_mode` and `modifiers`.
- Strengthened `schemas/subagent-contract.schema.json` with allowed/forbidden paths and tools, handoff inputs, evidence requirements, merge policy, and failure policy.
- Hardened Subagent delegation policy and template in `skills/task-contract/references/subagent-delegation-policy.md` and `skills/task-contract/assets/subagent-contract-template.md`.
- Improved CI and local validation parity by aligning validator scripts and execution order.

## [0.4.0] - Released

### Added
- Multi-agent sub-contracting integration into the canonical task-contract Skill.
- Release configuration file `config/release.json` for centralized versioning.
- Behavior contract documentation `docs/behavior-contract.md`.
- Subagent delegation task fixture and expected output.
- Snapshot files for all 12 fixtures under `skills/task-contract/tests/snapshots/`.
- Loop regression test runner in CI and local validation.

### Changed
- Upgraded release target and all active files to v0.4.0.
- Centralized validation scripts to read from release configuration.
- Aligned plugin manifest schema (`schemas/plugin-local-invariants.schema.json`) and expected output mode enums.
- Strengthened snapshot and loop contract validators to fail on placeholders.
- Archived `docs/v0.3.0-release-checklist.md` to historical directory.

## [0.3.0] - Released

### Added

- v0.3.0 validation and tooling implementation plan.
- Draft schemas for task contracts, Loop Contract Mode, expected outputs, and local plugin invariants.
- Schema validator script.
- Plugin package sync validator script.
- Documentation validator script.
- Snapshot protocol validator script.
- GitHub Actions validation workflow.
- Schema design documentation.
- Snapshot testing documentation.
- CI documentation.
- v0.3.0 release checklist.
- Snapshot directory policy.

### Changed

- Updated README for v0.3.0 release validation.
- Updated plugin manifest version to 0.3.0.
- Updated release process for schema validation, plugin sync validation, docs validation, snapshot protocol validation, and CI review.
- Updated roadmap to treat v0.3.0 as the validation and tooling release.
- Updated repository validation wrapper to include plugin sync validation.
- Preserved the v0.2.0 behavior contract while adding release-readiness infrastructure.

### Fixed

- Added explicit validation gates for schema drift, plugin package drift, documentation drift, and missing snapshot protocol files.
- Clarified that local plugin invariant validation is not an official plugin schema compliance claim.

### Deferred

- Official plugin schema validation.
- Marketplace publishing guide.
- Full golden-output execution harness.
- Contract schema freeze.
- Multi-skill expansion.

## [0.2.0] - Release Candidate

### Added

- Stable Loop Contract Mode.
- Loop state model.
- Loop observation method reference.
- Loop stop condition reference.
- Loop escalation rule reference.
- Loop evaluation rubric.
- Shared Loop Contract template.
- Compact Loop Contract template.
- Full Loop Contract template.
- Expanded Loop Log template.
- Expanded loop golden expected outputs.
- Loop repo maintenance fixture and expected output.
- Loop fixture validator script.
- Repository validator script.
- v0.2.0 release checklist.
- Migration guide from v0.1.0 to v0.2.0.
- Behavior contract documentation.
- Plugin packaging documentation.
- Plugin manifest documentation.
- Validator design documentation.
- `AGENTS.md` repository operating rules.

### Changed

- Promoted Loop-aware preview to stable Loop Contract Mode.
- Updated plugin manifest version to 0.2.0.
- Standardized active terminology around Approval Gate, Adjustment Strategy, Stop Conditions, and Escalation Triggers.
- Strengthened Approval Gate coverage for broad repository changes, public behavior changes, release metadata, dependencies, destructive cleanup, security posture changes, commits, pushes, tags, releases, pull requests, and high-impact loop execution.
- Made expected fixture modes deterministic where ambiguity is not the behavior being tested.
- Added canonical-source and plugin-sync rules to prevent packaged Skill drift.
- Moved P2 expansion work to the roadmap.

### Fixed

- Prevented release-readiness drift between canonical Skill source and the packaged plugin copy.
- Aligned release checklist, changelog, templates, fixture expectations, and validators.
- Clarified that local plugin manifest validation is not a claim of official schema compliance.

## [0.1.0] - Release Candidate

### Added

- Canonical `task-contract` Skill source.
- Auto-Skeleton behavior.
- Task Optimizer rules.
- Compact Contract mode.
- Full Contract mode.
- Loop-aware Contract preview support.
- Output Contract format.
- Decision Point pattern.
- Approval Gate / confirmation behavior for high-impact work.
- Codex Plugin package scaffold.
- Local marketplace metadata.
- Documentation set.
- Manual behavior fixtures and expected outputs.
- Repository validation and plugin sync scripts.
