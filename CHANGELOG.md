# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Planned

- P2 roadmap items for v0.3.0 and later: CI, markdown linting, machine-readable schemas, golden output runners, official plugin schema validation, marketplace publishing guidance, and multi-skill expansion.

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
