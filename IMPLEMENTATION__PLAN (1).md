# IMPLEMENTATION__PLAN.md

## 1. BLUF

This implementation plan upgrades `codex-task-contract-skill` to a coherent, executable **v0.4.0 core-function release state**.

The repository already contains the core `task-contract` Skill behavior: Auto-Skeleton, Task Optimizer, Compact Contract, Full Contract, Loop Contract Mode, Approval Gate, Loop Log, draft schemas, validators, CI, plugin packaging, pre-commit hooks, loop regression tooling, and preliminary subagent delegation support.

However, the repository currently has release-target drift across README, AGENTS, docs, schemas, validators, plugin metadata, fixtures, and CI. The main implementation goal is to make v0.4.0 the single active release target, strengthen validation coverage, fully integrate subagent delegation into the Skill contract, and keep larger future work in the roadmap.

Recommended implementation scope: **A2 — complete P0 + P1, move P2 to Roadmap**.

---

## 2. Release Target

| Field | Value |
|---|---|
| Active release target | `v0.4.0` |
| Core Skill | `task-contract` |
| Plugin package | `codex-task-contract-skill` |
| Canonical Skill source | `skills/task-contract/` |
| Packaged Skill copy | `plugin/codex-task-contract-skill/skills/task-contract/` |
| Plugin manifest | `plugin/codex-task-contract-skill/.codex-plugin/plugin.json` |
| Docs language | English-only |
| Validation style | Local, zero-dependency unless explicitly justified |
| Public compliance boundary | Do not claim official Codex/plugin marketplace schema compliance until authoritative schema validation exists |

---

## 3. Scope

### 3.1 In Scope

This plan covers:

1. Release-target consistency for v0.4.0.
2. Core Skill behavior alignment.
3. Plugin manifest and local invariant alignment.
4. Draft schema alignment.
5. Documentation alignment.
6. Validator strengthening.
7. CI and pre-commit parity.
8. Loop regression test coverage expansion.
9. Subagent delegation integration.
10. Snapshot fixture structure completion.
11. Roadmap separation for non-blocking future work.

### 3.2 Out of Scope

The following items should remain deferred unless separately approved:

1. Official plugin schema compliance claims.
2. Marketplace publishing guide as a release blocker.
3. Full live model-output golden execution harness.
4. Automated changelog generation.
5. General multi-skill orchestration.
6. v1.0.0 contract freeze.
7. Network-dependent validation.

---

## 4. Current Audit Findings

### 4.1 Core Behavior Is Present but Needs v0.4.0 Alignment

The canonical `SKILL.md` already defines the expected task-contract behavior:

- Auto-Skeleton first.
- Optimized Task construction.
- Compact Contract, Full Contract, and Loop Contract Mode.
- Approval Gate for high-impact work.
- Loop Contract fields.
- Loop Log.
- Stop Conditions.
- Escalation Triggers.
- Quality Checklist.

The main issue is not missing conceptual behavior. The main issue is inconsistent release metadata and incomplete enforcement.

### 4.2 Version Drift Exists Across Active Files

Observed drift examples:

| Area | Drift |
|---|---|
| README | Current target says v0.4.0, but release-check section still references v0.3.0 |
| AGENTS | Release gates and schema policy still reference v0.3.0 |
| Release docs | `docs/release-process.md` still describes v0.3.0 |
| Checklist | Active checklist remains `docs/v0.3.0-release-checklist.md` |
| Plugin docs | `docs/plugin-packaging.md` and `docs/plugin-manifest.md` still reference v0.2.0 |
| Schema | `plugin-local-invariants.schema.json` only accepts v0.3.0 |
| Validator | `validate-repo.py` expects plugin manifest version v0.4.0 |
| Fixtures | `loop-repo-maintenance-task` still tests v0.2.0 release readiness |

### 4.3 Validation Is Present but Too Shallow

Current validators check required files, required terms, basic JSON schema structure, docs H1 headings, plugin sync, loop fixture terms, and snapshot protocol presence.

The main gaps:

1. No single release config source.
2. No repository-wide version drift validator.
3. Schema validator does not validate semantic consistency.
4. Snapshot runner does not require snapshot files per fixture.
5. Loop fixture validator checks terms but not empty sections/placeholders.
6. CI does not run the loop regression test runner.
7. Subagent delegation is not fully integrated into main Skill references and tests.

---

## 5. P0 Required Fixes

P0 items are release blockers. Complete these before treating v0.4.0 as execution-ready.

---

### P0-01 — Make v0.4.0 the Single Active Release Target

#### Problem

The repository simultaneously references v0.2.0, v0.3.0, and v0.4.0 in active release-critical files.

#### Required Changes

Update active release references to v0.4.0 in:

- `README.md`
- `AGENTS.md`
- `CHANGELOG.md`
- `docs/release-process.md`
- `docs/testing.md`
- `docs/validator-design.md`
- `docs/schema-design.md`
- `docs/snapshot-testing.md`
- `docs/ci.md`
- `docs/plugin-packaging.md`
- `docs/plugin-manifest.md`
- `schemas/*.schema.json`
- `scripts/validate-repo.py`
- `scripts/validate-docs.py`
- `skills/task-contract/tests/fixtures/loop-repo-maintenance-task.md`
- `skills/task-contract/tests/expected/loop-repo-maintenance-task.expected.md`

#### Acceptance Criteria

- `v0.4.0` is the only active release target.
- Older versions may appear only in changelog history, archive files, or roadmap history.
- Active release docs do not instruct users to run v0.2.0 or v0.3.0 gates for v0.4.0.

---

### P0-02 — Add a Single Release Configuration File

#### Problem

Release version, schema version, plugin name, and skill path are hardcoded in multiple files.

#### Required Change

Add:

```text
config/release.json
```

Recommended content:

```json
{
  "release_target": "0.4.0",
  "release_tag": "v0.4.0",
  "schema_version": "0.4.0-draft",
  "skill_name": "task-contract",
  "plugin_name": "codex-task-contract-skill",
  "plugin_skills_path": "./skills/",
  "canonical_skill_path": "skills/task-contract/",
  "packaged_skill_path": "plugin/codex-task-contract-skill/skills/task-contract/",
  "manifest_path": "plugin/codex-task-contract-skill/.codex-plugin/plugin.json",
  "docs_language": "English-only",
  "official_plugin_schema_claim": false
}
```

#### Update Validators

Modify:

- `scripts/validate-repo.py`
- `scripts/validate-docs.py`
- `scripts/validate-schemas.py`

so they read the release target and schema version from `config/release.json`.

#### Acceptance Criteria

- Validators no longer duplicate version constants unless explicitly justified.
- Updating `config/release.json` is enough to move active release target in validation logic.

---

### P0-03 — Add This Implementation Plan to the Repository

#### Required Change

Add this file:

```text
IMPLEMENTATION__PLAN.md
```

#### Acceptance Criteria

- File exists at repository root.
- File identifies v0.4.0 as the active release target.
- File separates P0, P1, and P2 work.
- File includes validation commands and acceptance criteria.

---

### P0-04 — Replace Active v0.3.0 Checklist with v0.4.0 Checklist

#### Problem

The active checklist is still `docs/v0.3.0-release-checklist.md`.

#### Required Changes

1. Add:

```text
docs/v0.4.0-release-checklist.md
```

2. Move the old checklist to archive or make it clearly historical:

Recommended path:

```text
docs/archive/v0.3.0-release-checklist.md
```

3. Update references in:

- `README.md`
- `AGENTS.md`
- `docs/release-process.md`
- `docs/testing.md`
- `docs/validator-design.md`
- `scripts/validate-repo.py`
- `scripts/validate-docs.py`

#### Acceptance Criteria

- Active release checklist is v0.4.0.
- v0.3.0 checklist no longer acts as a validation gate.

---

### P0-05 — Add Loop Regression Runner to CI

#### Problem

v0.4.0 includes loop regression testing, but the CI workflow does not run `scripts/test-loop-runner.py`.

#### Required Change

Update:

```text
.github/workflows/validate.yml
```

Add:

```yaml
- name: Loop regression tests
  run: python3 scripts/test-loop-runner.py
```

#### Also Update

- `README.md`
- `docs/ci.md`
- `docs/testing.md`
- `docs/v0.4.0-release-checklist.md`
- `scripts/pre-commit-hook.sh` if needed for parity review

#### Acceptance Criteria

The local and CI validation sequences both include:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
git status
```

`git status` remains local-only and should not be required in CI.

---

### P0-06 — Fully Integrate Subagent Delegation into the Main Skill

#### Problem

Subagent delegation policy and template exist, but `SKILL.md` does not sufficiently integrate them into the main Skill behavior and references.

#### Required Changes in `skills/task-contract/SKILL.md`

Add a section:

```md
## Multi-Agent Sub-contracting
```

This section must define:

1. When delegation is allowed.
2. When delegation is not allowed.
3. Required subagent contract fields.
4. Parent Loop Log syncing.
5. Recursion lock.
6. Scope boundary.
7. Approval Gate behavior.
8. Return format.
9. Evidence requirements.

Add references:

```md
- `references/subagent-delegation-policy.md`
- `assets/subagent-contract-template.md`
```

#### Acceptance Criteria

- `SKILL.md` directly mentions subagent delegation.
- The policy file is referenced from the main Skill file.
- Delegation requires explicit bounded scope and acceptance criteria.
- Subagents cannot spawn subagents unless explicitly approved.

---

### P0-07 — Align Expected Output Schema with Subagent Modes

#### Problem

The expected fixture uses `Mode: Full Contract with Subagent Delegation`, but `schemas/expected-output.schema.json` does not include this mode.

#### Required Change

Update `schemas/expected-output.schema.json` enum to include:

```json
"Full Contract with Subagent Delegation",
"Loop Contract Mode with Subagent Delegation",
"Loop Contract Mode with Approval Gate and Subagent Delegation"
```

#### Acceptance Criteria

- Expected output schema can represent all current expected fixture modes.
- Future loop + delegation fixture modes are supported.

---

### P0-08 — Strengthen Version Drift Validation

#### Required Changes

Add version drift detection to `scripts/validate-docs.py` or create:

```text
scripts/validate-release-consistency.py
```

Recommended checks:

1. Active release docs must reference `v0.4.0`.
2. Active release docs must not refer to v0.2.0 or v0.3.0 as current gates.
3. `plugin.json` version must match `config/release.json`.
4. schema defaults must match `config/release.json.schema_version`.
5. active checklist filename must match release target.
6. README release check must match release target.

#### Acceptance Criteria

- Validation fails if an active file says v0.3.0 is the current release gate.
- Validation fails if plugin manifest and release config disagree.

---

### P0-09 — Update Plugin Local Invariant Schema

#### Required Change

Update:

```text
schemas/plugin-local-invariants.schema.json
```

from v0.3.0-only pattern to v0.4.0 or release-config-driven validation.

Recommended direct patch:

```json
"pattern": "^0\\.4\\.0(-[A-Za-z0-9.-]+)?$"
```

Better long-term patch:

- Keep JSON schema generic.
- Let `validate-repo.py` compare actual manifest version against `config/release.json`.

#### Acceptance Criteria

- Schema and validator no longer disagree about valid plugin version.

---

### P0-10 — Update README Release Commands

#### Required Changes

Update README validation section to use v0.4.0 commands:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
git status
```

#### Acceptance Criteria

- README no longer presents v0.3.0 as the current release check.
- README includes loop regression tests for v0.4.0.

---

## 6. P1 Recommended Fixes

P1 items are not minimal release blockers, but they are recommended for durable core execution quality.

---

### P1-01 — Add `docs/behavior-contract.md`

#### Purpose

Create one human-readable behavior contract that unifies Skill behavior, fixtures, schemas, and validators.

#### Required Content

```md
# Behavior Contract

## Core Principle
## Mode Selection
## Auto-Skeleton Requirements
## Task Optimizer Requirements
## Compact Contract Requirements
## Full Contract Requirements
## Approval Gate Requirements
## Loop Contract Mode Requirements
## Loop Log Requirements
## Stop Conditions
## Escalation Triggers
## Multi-Agent Sub-contracting Requirements
## Final Response Requirements
## Anti-Patterns
```

#### Acceptance Criteria

- `SKILL.md`, fixtures, schemas, and validators align with this document.
- This document does not replace `SKILL.md`; it explains the behavior contract for maintainers.

---

### P1-02 — Strengthen `docs/installation.md`

#### Required Additions

Add:

1. Local plugin package installation notes.
2. Local marketplace metadata explanation.
3. Smoke test prompt.
4. Expected output checklist.
5. Troubleshooting section.

#### Troubleshooting Cases

- Missing plugin manifest.
- Wrong plugin path.
- Unsynced packaged Skill copy.
- Manifest version mismatch.
- Skill invocation not recognized.

#### Acceptance Criteria

A maintainer can install or manually verify the plugin package using only `docs/installation.md` and README.

---

### P1-03 — Add Subagent Fixture Input

#### Required Change

Add:

```text
skills/task-contract/tests/fixtures/subagent-delegation-task.md
```

Recommended fixture prompt:

```text
Delegate a documentation audit to a subagent. The subagent may read docs/* only, must not write files, must not spawn another subagent, and must return a bounded audit report with acceptance criteria coverage.
```

#### Acceptance Criteria

- Fixture exists.
- Expected output file exists.
- Validator inventory includes the fixture if fixture inventory checking is added.

---

### P1-04 — Align Subagent Template with Schema

#### Required Change

Update:

```text
skills/task-contract/assets/subagent-contract-template.md
```

Recommended structure:

```md
# Subagent Contract - [Subagent Role Name]

## Metadata

```yaml
parent_conversation_id: [parent-id]
subagent_role: [role]
scope_boundary:
  - [allowed read/write path or command]
constraints:
  - [constraint]
max_iterations: [number]
recursion_lock: true
approval_gate:
  required: [true/false]
  reason: [reason]
  blocked_action: [action]
  recommended_safe_default: [default]
  reply_template: [template]
acceptance_criteria:
  - [criteria]
return_format: [format]
```

## Scope Boundary
## Constraints
## Acceptance Criteria
## Return Format
## Parent Loop Log Sync
```

#### Acceptance Criteria

- Template field names align with `subagent-contract.schema.json`.
- Human-readable sections remain usable.
- Recursion lock is explicit.

---

### P1-05 — Add Snapshot Files for Each Fixture

#### Required Additions

Add snapshot files under:

```text
skills/task-contract/tests/snapshots/
```

Required files:

```text
simple-writing-task.snapshot.md
vague-repo-task.snapshot.md
high-risk-refactor-task.snapshot.md
documentation-task.snapshot.md
research-task.snapshot.md
destructive-file-task.snapshot.md
loop-debug-task.snapshot.md
loop-research-task.snapshot.md
loop-documentation-task.snapshot.md
loop-dangerous-task.snapshot.md
loop-repo-maintenance-task.snapshot.md
subagent-delegation-task.snapshot.md
```

#### Snapshot Template

```md
# Snapshot: [Fixture Name]

## Expected Mode

...

## Required Sections

...

## Required Fields

...

## Required Checks

...

## Approval Requirements

...

## Forbidden Patterns

...

## Reviewer Notes

...
```

#### Acceptance Criteria

- One snapshot exists per expected fixture.
- `run-snapshots.py` verifies snapshot coverage.

---

### P1-06 — Strengthen `run-snapshots.py`

#### Required Checks

Update `scripts/run-snapshots.py` to verify:

1. Snapshot directory exists.
2. Snapshot README exists.
3. Snapshot docs exist.
4. Every expected fixture has a matching snapshot file.
5. Every snapshot includes:
   - Expected Mode
   - Required Sections
   - Required Checks
   - Approval Requirements
   - Forbidden Patterns or explicit `None`
6. No snapshot contains placeholder-only content.

#### Acceptance Criteria

- Missing snapshot file causes validation failure.
- Empty or placeholder snapshot causes validation failure.

---

### P1-07 — Strengthen Loop Fixture Validation

#### Required Updates

Update `scripts/validate-loop-contract-fixtures.py` to detect:

1. Required term exists but section is empty.
2. Placeholder-only values such as `...`, `[placeholder]`, `TBD`, `TODO`.
3. Missing max iteration number.
4. High-impact loop missing explicit `Max Iterations is 1 before approval`.
5. Observation method not tied to visible evidence.
6. Approval Gate required but not stated as blocking execution.

#### Acceptance Criteria

- Validator catches shallow expected outputs that only include keywords.
- High-impact loop fixtures are held to stricter requirements.

---

### P1-08 — Expand Loop Regression Test Cases

#### Required Changes

Update:

```text
skills/task-contract/tests/loop-regression-tests.json
scripts/test-loop-runner.py
```

Add cases:

1. `approval_required_stop`
2. `validation_blocked_stop`
3. `missing_context_stop`
4. `scope_drift_stop`
5. `high_impact_one_iteration_stop`
6. `subagent_delegation_logged`
7. `low_confidence_stop`

#### Acceptance Criteria

- Regression runner validates all supported stop reasons.
- High-impact loops stop after one inspection iteration before approval.
- Subagent delegation is logged without nesting full subagent logs into the parent Loop Log.

---

### P1-09 — Improve `validate-schemas.py`

#### Required Checks

Add checks for:

1. `schema_version` default equals release config schema version.
2. `$id` is local and clearly marked as draft, or uses a documented repository-local URI.
3. mode enums include current expected fixture modes.
4. required fields align with `docs/behavior-contract.md`.
5. `additionalProperties` is explicit in key object schemas.

#### Acceptance Criteria

- Schema validation catches current mode mismatch.
- Schema validation catches stale schema version defaults.

---

### P1-10 — Improve `validate-repo.py` Required File Inventory

#### Required Additions

Add required files:

```text
IMPLEMENTATION__PLAN.md
config/release.json
docs/v0.4.0-release-checklist.md
docs/behavior-contract.md
skills/task-contract/tests/fixtures/subagent-delegation-task.md
```

Remove active requirement for:

```text
docs/v0.3.0-release-checklist.md
```

unless moved into archive and treated as historical.

#### Acceptance Criteria

- Missing v0.4.0 implementation files fail validation.
- Historical v0.3.0 checklist is not treated as active release gate.

---

### P1-11 — Update Roadmap Boundaries

#### Required Change

Update:

```text
docs/roadmap.md
```

Move or preserve these as deferred:

- Official plugin schema validation.
- Marketplace publishing guide.
- Full golden-output execution harness.
- Automated changelog generation.
- Marketplace install smoke test automation.
- Contract schema freeze.
- General multi-skill orchestration.

#### Acceptance Criteria

- P2 work is not listed as v0.4.0 blocker.
- Roadmap clearly separates v0.4.0 completion from future work.

---

## 7. P2 Roadmap Items

Do not implement these as part of A2 unless separately approved.

| Item | Recommended Target | Reason |
|---|---|---|
| Official plugin schema validation | v0.5.0 or later | Requires authoritative schema source |
| Marketplace publishing guide | v0.5.0 | Useful but not required for core execution |
| Full golden-output execution harness | v0.5.0 / v0.6.0 | Larger engineering effort |
| Automated changelog generator | v0.5.0 | Maintenance improvement, not core behavior |
| Marketplace install smoke test automation | v0.5.0 | Can start manual in v0.4.0 |
| Contract schema freeze | v1.0.0 | Should wait for behavior stabilization |
| General multi-skill orchestration | post-v1.0.0 | Larger design surface |

---

## 8. File-by-File Change Plan

### 8.1 Add Files

```text
IMPLEMENTATION__PLAN.md
config/release.json
docs/v0.4.0-release-checklist.md
docs/behavior-contract.md
skills/task-contract/tests/fixtures/subagent-delegation-task.md
skills/task-contract/tests/snapshots/simple-writing-task.snapshot.md
skills/task-contract/tests/snapshots/vague-repo-task.snapshot.md
skills/task-contract/tests/snapshots/high-risk-refactor-task.snapshot.md
skills/task-contract/tests/snapshots/documentation-task.snapshot.md
skills/task-contract/tests/snapshots/research-task.snapshot.md
skills/task-contract/tests/snapshots/destructive-file-task.snapshot.md
skills/task-contract/tests/snapshots/loop-debug-task.snapshot.md
skills/task-contract/tests/snapshots/loop-research-task.snapshot.md
skills/task-contract/tests/snapshots/loop-documentation-task.snapshot.md
skills/task-contract/tests/snapshots/loop-dangerous-task.snapshot.md
skills/task-contract/tests/snapshots/loop-repo-maintenance-task.snapshot.md
skills/task-contract/tests/snapshots/subagent-delegation-task.snapshot.md
```

### 8.2 Modify Files

```text
README.md
AGENTS.md
CHANGELOG.md
.github/workflows/validate.yml
docs/installation.md
docs/usage.md
docs/testing.md
docs/release-process.md
docs/roadmap.md
docs/validator-design.md
docs/plugin-packaging.md
docs/plugin-manifest.md
docs/schema-design.md
docs/snapshot-testing.md
docs/ci.md
schemas/task-contract.schema.json
schemas/loop-contract.schema.json
schemas/expected-output.schema.json
schemas/plugin-local-invariants.schema.json
schemas/subagent-contract.schema.json
scripts/validate-repo.py
scripts/validate-schemas.py
scripts/validate-docs.py
scripts/run-snapshots.py
scripts/validate-loop-contract-fixtures.py
scripts/test-loop-runner.py
scripts/pre-commit-hook.sh
scripts/install-git-hooks.sh
scripts/sync-plugin-package.sh
skills/task-contract/SKILL.md
skills/task-contract/references/subagent-delegation-policy.md
skills/task-contract/assets/subagent-contract-template.md
skills/task-contract/tests/loop-regression-tests.json
skills/task-contract/tests/expected/simple-writing-task.expected.md
skills/task-contract/tests/expected/vague-repo-task.expected.md
skills/task-contract/tests/expected/high-risk-refactor-task.expected.md
skills/task-contract/tests/expected/documentation-task.expected.md
skills/task-contract/tests/expected/research-task.expected.md
skills/task-contract/tests/expected/destructive-file-task.expected.md
skills/task-contract/tests/expected/loop-debug-task.expected.md
skills/task-contract/tests/expected/loop-research-task.expected.md
skills/task-contract/tests/expected/loop-documentation-task.expected.md
skills/task-contract/tests/expected/loop-dangerous-task.expected.md
skills/task-contract/tests/expected/loop-repo-maintenance-task.expected.md
skills/task-contract/tests/expected/subagent-delegation-task.expected.md
plugin/codex-task-contract-skill/.codex-plugin/plugin.json
.agents/plugins/marketplace.json
```

### 8.3 Archive or Deprecate

Recommended:

```text
docs/archive/v0.3.0-release-checklist.md
```

Do not delete historical release material unless the maintainer explicitly approves deletion.

---

## 9. Execution Order

### Phase 1 — Version and Release Target Alignment

1. Add `config/release.json`.
2. Add `IMPLEMENTATION__PLAN.md`.
3. Add `docs/v0.4.0-release-checklist.md`.
4. Move or archive `docs/v0.3.0-release-checklist.md`.
5. Update README, AGENTS, release docs, testing docs, CI docs, plugin docs.

### Phase 2 — Core Skill and Subagent Integration

1. Update `skills/task-contract/SKILL.md` with Multi-Agent Sub-contracting.
2. Update `references/subagent-delegation-policy.md`.
3. Update `assets/subagent-contract-template.md`.
4. Add `docs/behavior-contract.md`.
5. Add subagent fixture input.
6. Update subagent expected output.

### Phase 3 — Schema Alignment

1. Update schema version defaults.
2. Update plugin local invariant schema.
3. Update expected output mode enums.
4. Update subagent schema if needed for return format and recursion lock.
5. Strengthen `validate-schemas.py`.

### Phase 4 — Fixture, Snapshot, and Regression Coverage

1. Add snapshot files for each expected fixture.
2. Strengthen `run-snapshots.py`.
3. Strengthen `validate-loop-contract-fixtures.py`.
4. Expand loop regression tests.
5. Update `test-loop-runner.py` for additional stop conditions.

### Phase 5 — CI and Pre-commit Parity

1. Add `python3 scripts/test-loop-runner.py` to CI.
2. Confirm pre-commit hook runs the same validation set.
3. Update docs to match validation sequence.

### Phase 6 — Plugin Package Sync

Run:

```bash
bash scripts/sync-plugin-package.sh
```

Then run sync validation:

```bash
python3 scripts/validate-plugin-sync.py
```

### Phase 7 — Final Validation

Run:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
git status
```

---

## 10. Validation Plan

### 10.1 Local Validation Commands

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
git status
```

### 10.2 CI Validation Commands

CI should run:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
```

CI should not require `git status` as a release blocker unless the workflow explicitly checks for uncommitted sync drift after `sync-plugin-package.sh`.

### 10.3 Manual Smoke Test

Prompt:

```text
Use $task-contract to clarify this request before editing files: review this repository for v0.4.0 release readiness and stop before making high-impact changes.
```

Expected behavior:

1. Auto-Skeleton appears first.
2. Mode is Full Contract or Loop Contract Mode depending on requested iteration.
3. Optimized Task bounds the repository review.
4. Output Contract is present.
5. Approval Gate appears before broad repo changes or release actions.
6. Loop Contract appears if bounded iteration is requested.
7. Next Step is clear and singular.

### 10.4 Subagent Smoke Test

Prompt:

```text
Use $task-contract to delegate docs/* audit to a subagent. The subagent may read docs/* only, must not edit files, and must not spawn another subagent.
```

Expected behavior:

1. Parent contract defines delegation need.
2. Subagent contract includes parent ID placeholder, role, scope boundary, constraints, acceptance criteria, recursion lock, approval gate status, and return format.
3. Parent Loop Log includes only a concise delegation sync entry if Loop Contract Mode is used.
4. No broad repository edit is authorized.

---

## 11. Acceptance Criteria

The implementation is complete when all criteria below pass.

### 11.1 Release Consistency

- [ ] `config/release.json` exists and defines `0.4.0`.
- [ ] README identifies v0.4.0 as current release target.
- [ ] Active release docs identify v0.4.0.
- [ ] Active release checklist is `docs/v0.4.0-release-checklist.md`.
- [ ] v0.2.0 and v0.3.0 appear only in historical changelog, archive, or roadmap contexts.

### 11.2 Core Skill Behavior

- [ ] `SKILL.md` still requires Auto-Skeleton first when invoked.
- [ ] Task Optimizer requirements remain explicit.
- [ ] Compact Contract, Full Contract, and Loop Contract Mode remain defined.
- [ ] Approval Gate triggers remain explicit.
- [ ] Loop Contract Mode includes objective, loop type, iteration unit, observation method, adjustment strategy, validation method, stop conditions, max iterations, escalation triggers, approval gate, and loop log.

### 11.3 Subagent Delegation

- [ ] `SKILL.md` includes Multi-Agent Sub-contracting.
- [ ] `references/subagent-delegation-policy.md` is referenced from `SKILL.md`.
- [ ] Subagent template aligns with schema.
- [ ] Subagent expected mode is supported by schema.
- [ ] Subagent fixture input exists.
- [ ] Subagent delegation regression or snapshot coverage exists.

### 11.4 Schema Alignment

- [ ] All schema files parse as JSON.
- [ ] Schema defaults use `0.4.0-draft` or documented release-config-driven values.
- [ ] `expected-output.schema.json` supports all expected fixture modes.
- [ ] `plugin-local-invariants.schema.json` does not contradict plugin manifest v0.4.0.

### 11.5 Validator Strength

- [ ] Validators fail on active release-target drift.
- [ ] Validators fail on missing required v0.4.0 files.
- [ ] Validators fail on missing snapshot coverage.
- [ ] Validators fail on shallow placeholder-only loop expected outputs.
- [ ] CI includes loop regression runner.
- [ ] Pre-commit hook and docs match the local validation sequence.

### 11.6 Plugin Sync

- [ ] Canonical Skill source and packaged Skill copy match after sync.
- [ ] `plugin.json` version matches `config/release.json`.
- [ ] Local marketplace metadata points to the correct plugin package path.

### 11.7 Documentation

- [ ] Installation docs include smoke test and troubleshooting.
- [ ] Testing docs include loop regression runner.
- [ ] CI docs match workflow.
- [ ] Release process docs describe v0.4.0.
- [ ] Roadmap keeps P2 items deferred.

---

## 12. Risk and Rollback Notes

### 12.1 Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Version drift remains in active files | Release confusion and validator false positives | Add release consistency validator |
| Schema changes over-constrain natural-language output | Skill becomes brittle | Keep schemas draft and structural only |
| Snapshot coverage becomes too exact | Model prose variation causes false failures | Validate sections and fields, not exact prose |
| Subagent delegation over-expands scope | Unsafe or unbounded execution | Require scope boundary, recursion lock, and approval gate |
| CI diverges from local validation | Release confidence decreases | Keep docs, pre-commit, and CI command list aligned |

### 12.2 Rollback Strategy

If a change breaks validation:

1. Revert the smallest failing change.
2. Run the relevant validator only.
3. Re-run full validation after the focused fix.
4. Do not revert behavior-contract improvements unless they contradict `SKILL.md`.
5. Preserve historical release docs in archive rather than deleting them.

### 12.3 Safety Boundary

Do not perform these actions without explicit maintainer approval:

- Delete historical release files.
- Change public plugin name.
- Change canonical Skill name.
- Change plugin package path.
- Claim official Codex/plugin marketplace schema compliance.
- Tag or publish a release.
- Push commits, create PRs, or create GitHub releases.

---

## 13. Recommended Commit Breakdown

Recommended commits if implementing in Git:

1. `chore: add v0.4.0 release config and implementation plan`
2. `docs: align active release docs to v0.4.0`
3. `feat: integrate subagent delegation into task-contract skill`
4. `test: add subagent fixture and snapshot coverage`
5. `test: expand loop regression coverage`
6. `chore: strengthen validators for release consistency`
7. `ci: run loop regression tests in validation workflow`
8. `chore: sync plugin package for v0.4.0`

---

## 14. Final Review Checklist

Before release review:

- [ ] Review `IMPLEMENTATION__PLAN.md`.
- [ ] Review `config/release.json`.
- [ ] Review active release docs.
- [ ] Review `SKILL.md` behavior changes.
- [ ] Review subagent delegation policy and template.
- [ ] Review schema diffs.
- [ ] Review validator diffs.
- [ ] Review fixture and snapshot diffs.
- [ ] Run local validation.
- [ ] Confirm CI validation is green.
- [ ] Confirm plugin package is synced.
- [ ] Confirm no official plugin schema compliance claim is made.
- [ ] Confirm P2 items remain in roadmap.
- [ ] Confirm final diff is acceptable before tagging.

---

## 15. Final Validation Command

Run this from repository root:

```bash
bash scripts/sync-plugin-package.sh \
  && bash scripts/validate-repo.sh \
  && bash scripts/validate-loop-contract-fixtures.sh \
  && python3 scripts/validate-schemas.py \
  && python3 scripts/validate-docs.py \
  && python3 scripts/run-snapshots.py \
  && python3 scripts/test-loop-runner.py \
  && git status
```

Expected final state:

```text
Repository validation passed.
Plugin sync validation passed.
Loop fixture validation passed.
Schema validation passed.
Documentation validation passed.
Snapshot protocol validation passed.
All loop regression tests passed.
Working tree clean after sync, or expected sync changes are committed.
```
