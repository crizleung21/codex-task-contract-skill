# IMPLEMENTATION__PLAN.md

Status: v0.3.0 implementation plan for validation, tooling, schemas, and release confidence  
Project: `codex-task-contract-skill`  
Primary Skill Name: `task-contract`  
Primary Plugin Name: `codex-task-contract-skill`  
Language Policy: English-only documentation and skill instructions  
Repository Policy: independent from `creator-toolchain`  
Baseline: v0.2.0 stable Loop Contract Mode and P0/P1 remediation  
Adopted Scope: v0.3.0 validation and tooling layer; no behavior redesign unless required by validation evidence

---

## 1. Executive Summary

`codex-task-contract-skill` is a focused Codex Skill and installable Plugin package that makes Codex clarify, bound, and contract requests before execution.

v0.2.0 stabilizes the core behavior layer: Compact Contract, Full Contract, stable Loop Contract Mode, Approval Gate policy, loop stop conditions, deterministic fixtures, canonical/plugin packaging rules, and local validation scripts.

v0.3.0 should not redesign the Skill. It should add a stronger reliability layer around the existing behavior:

1. stronger repository validation;
2. stronger loop fixture validation;
3. CI-ready validation commands;
4. golden fixture snapshot workflow;
5. machine-readable contract schema drafts;
6. plugin package drift detection;
7. markdown and documentation consistency checks;
8. clearer release evidence;
9. roadmap preparation for v1.0.0 behavior freeze.

v0.3.0 is successful when maintainers can prove that the Skill, docs, fixtures, templates, packaged plugin copy, and release metadata are internally consistent before release.

---

## 2. Product Positioning

### 2.1 What the Project Is

`codex-task-contract-skill` is a task-framing, scope-control, and loop-governance Skill for Codex.

It provides:

- visible task framing;
- optimized task rewriting;
- output contracts;
- acceptance criteria;
- decision points;
- approval gates;
- bounded Loop Contract Mode;
- validation and release-readiness tooling.

### 2.2 What v0.3.0 Adds

v0.3.0 adds reliability infrastructure around the v0.2.0 behavior contract.

It should answer:

```text
Can this repository prove that its Skill behavior, docs, fixtures, templates, plugin package, and release metadata are consistent?
```

### 2.3 What v0.3.0 Does Not Add

v0.3.0 should not add:

- a second Skill;
- multi-skill orchestration;
- background execution;
- autonomous runtime behavior;
- official plugin schema claims without authoritative verification;
- marketplace publishing as a release blocker;
- v1.0.0 behavior freeze.

---

## 3. Baseline From v0.2.0

v0.3.0 assumes the v0.2.0 baseline exists.

| Area | v0.2.0 Baseline |
|---|---|
| Core Skill | `task-contract` defines compact, full, and loop modes. |
| Loop Mode | Loop Contract Mode is stable and bounded. |
| Approval Gate | High-impact work pauses before execution. |
| Templates | Compact, full, shared loop, compact loop, and full loop templates exist. |
| Fixtures | Compact, full, high-impact, documentation, research, destructive, and loop fixtures exist. |
| Validation | Local repository and loop fixture validators exist. |
| Packaging | Plugin package exists and sync policy is documented. |
| Docs | Usage, installation, testing, release, migration, manifest, packaging, and behavior docs exist. |
| Roadmap | v0.3.0 deferred validation/tooling items are listed. |

If any baseline item is missing, v0.3.0 work must first repair the baseline before adding new tooling.

---

## 4. Confirmed v0.3.0 Decisions

| Area | Decision |
|---|---|
| Release target | v0.3.0 |
| Release theme | Validation and tooling |
| Core behavior | Preserve v0.2.0 behavior unless tests prove a correction is needed |
| Primary risk | Validator drift, fixture ambiguity, and plugin package inconsistency |
| CI | Add GitHub Actions workflow for validation commands |
| Schema | Add draft machine-readable contract schemas, not frozen v1.0 schemas |
| Snapshot tests | Add golden expected-output snapshot runner or snapshot protocol |
| Markdown lint | Add optional markdown consistency check |
| Plugin manifest | Validate local invariants; do not claim official schema compliance without source verification |
| Marketplace docs | Roadmap or draft only, not a v0.3.0 blocker unless already verified |
| Multi-skill expansion | Defer beyond v1.0.0 behavior freeze |

---

## 5. v0.3.0 Release Goal

v0.3.0 should make the repository harder to regress.

Release goal:

```text
Add a reliable validation and tooling layer that continuously checks task-contract behavior, fixture expectations, plugin package sync, local manifest invariants, documentation consistency, and release readiness.
```

v0.3.0 is not primarily a new feature release. It is a quality, validation, and maintainer-confidence release.

---

## 6. Target Repository Architecture

```text
codex-task-contract-skill/
├── README.md
├── IMPLEMENTATION__PLAN.md
├── CHANGELOG.md
├── AGENTS.md
├── skills/task-contract/
│   ├── SKILL.md
│   ├── references/
│   ├── assets/
│   └── tests/
│       ├── fixtures/
│       ├── expected/
│       └── snapshots/
├── plugin/codex-task-contract-skill/
│   ├── .codex-plugin/plugin.json
│   └── skills/task-contract/
├── docs/
│   ├── behavior-contract.md
│   ├── plugin-packaging.md
│   ├── plugin-manifest.md
│   ├── validator-design.md
│   ├── schema-design.md
│   ├── snapshot-testing.md
│   ├── ci.md
│   ├── testing.md
│   ├── release-process.md
│   ├── roadmap.md
│   └── v0.3.0-release-checklist.md
├── schemas/
│   ├── task-contract.schema.json
│   ├── loop-contract.schema.json
│   ├── expected-output.schema.json
│   └── plugin-local-invariants.schema.json
├── scripts/
│   ├── validate-repo.sh
│   ├── validate-repo.py
│   ├── validate-loop-contract-fixtures.sh
│   ├── validate-loop-contract-fixtures.py
│   ├── validate-plugin-sync.py
│   ├── validate-docs.py
│   ├── validate-schemas.py
│   ├── run-snapshots.py
│   └── sync-plugin-package.sh
└── .github/workflows/
    └── validate.yml
```

---

## 7. v0.3.0 Scope Overview

### 7.1 P0 — Release Blockers

P0 items must be completed before v0.3.0 can be released.

| ID | Area | Required Change | Acceptance Criteria |
|---|---|---|---|
| V3-P0-01 | Repository validator | Expand `validate-repo.py` into the primary release-readiness validator. | Checks required files, core Skill metadata, docs, templates, schemas, fixtures, plugin manifest, and release metadata. |
| V3-P0-02 | Plugin sync validator | Add `validate-plugin-sync.py` or equivalent logic. | Fails when `plugin/codex-task-contract-skill/skills/task-contract/` differs from `skills/task-contract/`. |
| V3-P0-03 | Loop fixture validator | Harden `validate-loop-contract-fixtures.py`. | Checks all required loop fields, log columns, stop conditions, escalation triggers, Approval Gate requirements, and forbidden open-ended phrases. |
| V3-P0-04 | CI workflow | Add `.github/workflows/validate.yml`. | Runs validation scripts on push and pull request. |
| V3-P0-05 | Schema draft | Add initial JSON schemas under `schemas/`. | Schemas cover task contract, loop contract, expected output, and local plugin invariants. |
| V3-P0-06 | Schema validator | Add `validate-schemas.py`. | Confirms schema files parse as JSON and include required top-level metadata. |
| V3-P0-07 | Snapshot protocol | Add snapshot testing docs and runner or manual protocol. | Maintainers can compare expected outputs against stable snapshot files or snapshot rules. |
| V3-P0-08 | v0.3.0 release checklist | Add `docs/v0.3.0-release-checklist.md`. | Checklist matches actual v0.3.0 release blockers. |
| V3-P0-09 | Release process update | Update `docs/release-process.md`. | Release process includes CI, schema validation, plugin sync validation, and snapshot review. |
| V3-P0-10 | Roadmap update | Update `docs/roadmap.md`. | v0.3.0 scope is current; v1.0.0 behavior freeze remains future scope. |

### 7.2 P1 — Strongly Recommended

P1 items should be completed in v0.3.0 if they do not block P0.

| ID | Area | Required Change | Acceptance Criteria |
|---|---|---|---|
| V3-P1-01 | Markdown consistency | Add `validate-docs.py` or documented markdown lint command. | Checks duplicate headings, missing titles, and required docs inventory. |
| V3-P1-02 | Fixture matrix | Add `docs/fixture-matrix.md`. | Maps every fixture to mode, risk class, required sections, and validator coverage. |
| V3-P1-03 | Validator test fixtures | Add valid and invalid validator samples. | Validators can be tested against known pass/fail examples. |
| V3-P1-04 | Snapshot directory | Add `skills/task-contract/tests/snapshots/`. | Snapshot files or protocol are documented and versioned. |
| V3-P1-05 | Local plugin manifest schema | Add `schemas/plugin-local-invariants.schema.json`. | Local manifest invariants are machine-readable. |
| V3-P1-06 | Release evidence template | Add `docs/release-evidence-template.md`. | Release reviewers can record command output, diffs, and unresolved risks. |
| V3-P1-07 | Changelog discipline | Update `CHANGELOG.md`. | v0.3.0 changes are grouped as Added, Changed, Fixed, and Deferred. |
| V3-P1-08 | README validation section | Update README. | README lists the v0.3.0 validation command sequence. |
| V3-P1-09 | AGENTS update | Update `AGENTS.md`. | Agent rules include schema, CI, and snapshot expectations. |
| V3-P1-10 | Failure messages | Improve validator error messages. | Failures include file path, missing term, and suggested fix where practical. |

### 7.3 P2 — Roadmap Only

P2 items should not block v0.3.0.

| ID | Roadmap Item | Target Version | Reason for Deferral |
|---|---|---|---|
| V3-P2-01 | Official plugin schema validation | v0.4.0+ | Requires authoritative schema source. |
| V3-P2-02 | Marketplace publishing guide | v0.4.0+ | Should follow stable plugin validation. |
| V3-P2-03 | Full golden output execution harness | v0.4.0+ | Needs stable runtime integration. |
| V3-P2-04 | Contract schema freeze | v1.0.0 | v0.3.0 schemas are drafts. |
| V3-P2-05 | Multi-skill expansion | post-v1.0.0 | Avoids scope creep before behavior freeze. |
| V3-P2-06 | Automated changelog generator | v0.4.0+ | Convenience tooling, not release-critical. |
| V3-P2-07 | Marketplace install smoke test | v0.4.0+ | Depends on marketplace publishing path. |

---

## 8. Detailed Implementation Plan

### Phase 1 — Baseline Audit

Goal: prove the v0.2.0 baseline is ready for v0.3.0 tooling.

Tasks:

1. Run existing validators.
2. Confirm canonical and packaged Skill directories exist.
3. Confirm current templates exist.
4. Confirm expected fixtures have deterministic modes.
5. Confirm `docs/roadmap.md` contains v0.3.0 validation/tooling scope.
6. Confirm no active docs use legacy v0.1/v0.2 terminology as current behavior.

Deliverables:

- Updated `docs/validator-design.md` baseline section.
- Audit notes in `docs/v0.3.0-release-checklist.md`.

Acceptance criteria:

- Baseline failures are either fixed or explicitly listed as v0.3.0 blockers.

### Phase 2 — Validator Hardening

Goal: make validators the source of release-readiness truth.

Tasks:

1. Expand `scripts/validate-repo.py`.
2. Add or expand `scripts/validate-plugin-sync.py`.
3. Expand `scripts/validate-loop-contract-fixtures.py`.
4. Add `scripts/validate-docs.py`.
5. Add `scripts/validate-schemas.py`.
6. Update shell wrappers to call the correct validators.
7. Ensure validation scripts are zero-dependency unless documented otherwise.

Deliverables:

- `scripts/validate-repo.py`
- `scripts/validate-plugin-sync.py`
- `scripts/validate-docs.py`
- `scripts/validate-schemas.py`
- updated `scripts/validate-loop-contract-fixtures.py`
- updated `docs/validator-design.md`

Acceptance criteria:

- Validators fail on missing required files.
- Validators fail on plugin sync drift.
- Validators fail on malformed schema JSON.
- Validators fail on ambiguous fixture modes.
- Validators produce readable error messages.

### Phase 3 — Schema Drafts

Goal: document the expected structure of task contracts in machine-readable form.

Tasks:

1. Add `schemas/task-contract.schema.json`.
2. Add `schemas/loop-contract.schema.json`.
3. Add `schemas/expected-output.schema.json`.
4. Add `schemas/plugin-local-invariants.schema.json`.
5. Add `docs/schema-design.md`.
6. Add `scripts/validate-schemas.py`.

Schema constraints:

- Schemas are drafts.
- Schemas must not claim v1.0.0 stability.
- Schemas should represent current v0.2.0/v0.3.0 behavior.
- Schemas should be strict enough to guide validators but flexible enough for practical output variation.

Acceptance criteria:

- All schema files parse as valid JSON.
- Each schema has `$schema`, `title`, `type`, and required field definitions.
- `docs/schema-design.md` explains draft status and boundaries.

### Phase 4 — Snapshot Testing

Goal: make fixture expectations easier to compare and review.

Tasks:

1. Add `docs/snapshot-testing.md`.
2. Add `skills/task-contract/tests/snapshots/`.
3. Add `scripts/run-snapshots.py` or document a manual snapshot protocol.
4. Define snapshot naming conventions.
5. Define update procedure.
6. Define review rules for expected output changes.

Deliverables:

- `docs/snapshot-testing.md`
- `skills/task-contract/tests/snapshots/README.md`
- optional `scripts/run-snapshots.py`

Acceptance criteria:

- Each fixture has a clear expected mode.
- Snapshot changes require reviewer attention.
- Snapshot update procedure is documented.

### Phase 5 — CI Workflow

Goal: run release-readiness checks automatically.

Tasks:

1. Add `.github/workflows/validate.yml`.
2. Run repository validation.
3. Run loop fixture validation.
4. Run schema validation.
5. Run plugin sync validation.
6. Run docs validation if added.

Required CI command set:

```bash
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-plugin-sync.py
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
```

Acceptance criteria:

- CI runs on push and pull request.
- CI uses only committed repository files.
- CI does not require network access unless explicitly documented.
- CI fails on validation errors.

### Phase 6 — Documentation Updates

Goal: keep human docs aligned with tooling.

Tasks:

1. Update README validation section.
2. Update `docs/testing.md`.
3. Update `docs/release-process.md`.
4. Update `docs/validator-design.md`.
5. Add `docs/schema-design.md`.
6. Add `docs/snapshot-testing.md`.
7. Add `docs/ci.md`.
8. Add `docs/v0.3.0-release-checklist.md`.
9. Update `docs/roadmap.md`.
10. Update `AGENTS.md`.

Acceptance criteria:

- Docs describe the same commands as scripts and CI.
- v0.3.0 docs do not describe roadmap-only items as release blockers.
- Official plugin schema validation remains a future item unless verified.

### Phase 7 — Release Readiness Review

Goal: confirm v0.3.0 is releasable.

Tasks:

1. Run all validators locally.
2. Confirm CI passes.
3. Confirm plugin package sync status.
4. Confirm schema draft files parse.
5. Confirm snapshot protocol is usable.
6. Review CHANGELOG.
7. Review release checklist.
8. Record release evidence.

Deliverables:

- Completed `docs/v0.3.0-release-checklist.md`.
- Optional `docs/release-evidence-template.md` filled for the release.

Acceptance criteria:

- All P0 items pass.
- P1 incomplete items are documented.
- P2 items remain in roadmap.

---

## 9. File-Level Change Plan

### 9.1 Existing Files to Update

| File | Required Update | Priority |
|---|---|---:|
| `README.md` | Add v0.3.0 validation command sequence and CI note. | P1 |
| `IMPLEMENTATION__PLAN.md` | Replace v0.2.0 plan with this v0.3.0 plan. | P0 |
| `CHANGELOG.md` | Add v0.3.0 release-candidate section. | P1 |
| `AGENTS.md` | Add schema, CI, and snapshot operating rules. | P1 |
| `docs/testing.md` | Add snapshot testing and schema validation notes. | P0 |
| `docs/release-process.md` | Add CI, schema, plugin sync, and snapshot review. | P0 |
| `docs/roadmap.md` | Mark v0.3.0 as validation/tooling release. | P0 |
| `docs/validator-design.md` | Expand validator architecture and failure model. | P0 |
| `docs/plugin-packaging.md` | Add plugin sync validation requirement. | P0 |
| `docs/plugin-manifest.md` | Link local invariant schema. | P1 |
| `scripts/validate-repo.py` | Expand release-readiness checks. | P0 |
| `scripts/validate-loop-contract-fixtures.py` | Harden loop fixture validation. | P0 |
| `scripts/validate-repo.sh` | Call all required validators or delegate clearly. | P0 |
| `scripts/sync-plugin-package.sh` | Keep sync deterministic and verify drift after sync. | P0 |

### 9.2 New Files to Add

| File | Purpose | Priority |
|---|---|---:|
| `.github/workflows/validate.yml` | CI validation workflow. | P0 |
| `scripts/validate-plugin-sync.py` | Detect canonical/plugin Skill drift. | P0 |
| `scripts/validate-docs.py` | Check docs inventory and markdown consistency. | P1 |
| `scripts/validate-schemas.py` | Validate schema JSON structure. | P0 |
| `scripts/run-snapshots.py` | Snapshot runner or snapshot checker. | P1 |
| `schemas/task-contract.schema.json` | Draft schema for task contracts. | P0 |
| `schemas/loop-contract.schema.json` | Draft schema for Loop Contract Mode. | P0 |
| `schemas/expected-output.schema.json` | Draft schema for expected fixture files. | P0 |
| `schemas/plugin-local-invariants.schema.json` | Local plugin manifest invariant schema. | P1 |
| `docs/schema-design.md` | Explain schema boundaries and draft status. | P0 |
| `docs/snapshot-testing.md` | Explain snapshot testing protocol. | P0 |
| `docs/ci.md` | Explain CI workflow and local parity. | P1 |
| `docs/fixture-matrix.md` | Map fixtures to mode and validator coverage. | P1 |
| `docs/v0.3.0-release-checklist.md` | v0.3.0 release checklist. | P0 |
| `docs/release-evidence-template.md` | Release evidence capture template. | P1 |
| `skills/task-contract/tests/snapshots/README.md` | Snapshot directory policy. | P1 |

---

## 10. Validator Design Requirements

### 10.1 `validate-repo.py`

Must check:

1. required file inventory;
2. canonical Skill metadata;
3. required behavior terms;
4. active legacy terminology outside historical docs;
5. template inventory;
6. fixture inventory;
7. deterministic fixture modes;
8. docs inventory;
9. schema inventory;
10. plugin manifest local invariants;
11. plugin package sync status or delegates to `validate-plugin-sync.py`;
12. release checklist consistency.

### 10.2 `validate-plugin-sync.py`

Must check:

1. canonical Skill directory exists;
2. packaged Skill directory exists;
3. file lists match;
4. file contents match;
5. extra packaged files are either expected or fail validation;
6. output lists the exact drift paths.

### 10.3 `validate-loop-contract-fixtures.py`

Must check:

1. all loop expected files exist;
2. all required Loop Contract fields are present;
3. Loop Log columns are present;
4. Stop Conditions are plural and present;
5. Escalation Triggers are plural and present;
6. Approval Gate appears when required;
7. forbidden open-ended loop phrases are absent;
8. high-impact loop fixtures require approval;
9. required max iteration expectations are present;
10. failure messages identify the fixture and missing item.

### 10.4 `validate-schemas.py`

Must check:

1. all schema files exist;
2. all schema files parse as JSON;
3. each schema has `$schema`, `title`, and `type`;
4. required fields are present;
5. schema draft status is documented.

### 10.5 `validate-docs.py`

Should check:

1. required docs exist;
2. each doc has one H1 title;
3. release docs mention v0.3.0 correctly;
4. roadmap contains deferred P2 items;
5. docs do not contradict the release checklist.

---

## 11. Schema Draft Requirements

### 11.1 `task-contract.schema.json`

Should represent:

- Auto-Skeleton;
- Optimized Task;
- Output Contract;
- Assumptions;
- Constraints;
- Decision Points;
- Acceptance Criteria;
- Approval Gate;
- Next Step.

### 11.2 `loop-contract.schema.json`

Should represent:

- Loop Objective;
- Loop Type;
- Iteration Unit;
- Observation Method;
- Adjustment Strategy;
- Validation Method;
- Stop Conditions;
- Max Iterations;
- Escalation Triggers;
- Approval Gate;
- Loop Log;
- Loop Stop Summary.

### 11.3 `expected-output.schema.json`

Should represent:

- fixture name;
- expected mode;
- required sections;
- required fields;
- required checks;
- forbidden patterns;
- approval requirements.

### 11.4 `plugin-local-invariants.schema.json`

Should represent local expectations only:

- plugin name;
- plugin version;
- skills path;
- local package path;
- canonical Skill path;
- packaged Skill path.

---

## 12. CI Requirements

CI workflow should run on:

- push;
- pull request;
- manual dispatch if desired.

Minimum CI steps:

1. checkout repository;
2. set up Python;
3. run repository validator;
4. run loop fixture validator;
5. run plugin sync validator;
6. run schema validator;
7. run docs validator if present.

CI should avoid external network dependency. It should validate committed files only.

---

## 13. Snapshot Testing Requirements

Snapshot testing should improve review clarity without overfitting natural-language outputs.

### 13.1 Snapshot Strategy

Use snapshots for stable expected output structure, not exact prose where exact prose is not meaningful.

A snapshot may record:

- expected mode;
- required sections;
- required fields;
- required checks;
- forbidden patterns;
- approval requirements.

### 13.2 Snapshot Update Rules

Snapshots may be updated when:

1. Skill behavior intentionally changes;
2. fixture expectations become more deterministic;
3. validator coverage expands;
4. release scope changes.

Snapshot updates require review notes explaining why the change is valid.

---

## 14. Documentation Requirements

v0.3.0 docs must explain:

1. what validators check;
2. how CI maps to local validation;
3. how schemas are draft artifacts;
4. how plugin sync is validated;
5. how snapshot review works;
6. what remains deferred to future versions;
7. why v0.3.0 does not freeze v1.0.0 behavior.

---

## 15. Release Checklist Requirements

`docs/v0.3.0-release-checklist.md` must include:

- repository validator checks;
- loop fixture validator checks;
- plugin sync validator checks;
- schema validator checks;
- CI workflow checks;
- documentation checks;
- snapshot review checks;
- changelog checks;
- roadmap checks;
- human review checks.

---

## 16. Risk Register

| Risk | Impact | Mitigation |
|---|---|---|
| Validators become too strict for practical outputs | Blocks useful changes | Keep schemas draft and validators focused on structural invariants. |
| Plugin package drifts from canonical source | Released plugin behaves differently | Add sync validator and CI check. |
| CI requires unavailable dependencies | CI becomes brittle | Keep v0.3.0 validators zero-dependency where possible. |
| Snapshots overfit prose | False failures | Snapshot structure and requirements, not exact wording unless intentional. |
| Official plugin schema remains unverified | Incorrect compliance claims | Validate local invariants only and document caveat. |
| v0.3.0 scope expands into v1.0.0 freeze | Delayed release | Keep behavior freeze in v1.0.0 roadmap. |
| Multi-skill expansion distracts from reliability layer | Scope creep | Explicitly defer multi-skill expansion. |

---

## 17. Release Readiness Definition

v0.3.0 is ready when:

1. v0.2.0 behavior remains intact;
2. repository validation passes;
3. loop fixture validation passes;
4. plugin sync validation passes;
5. schema validation passes;
6. CI workflow runs the same validation checks;
7. docs describe the same release process as the scripts;
8. release checklist matches actual files;
9. snapshots or snapshot protocol are documented;
10. P2 items remain in roadmap;
11. no official plugin schema compliance claim is made without verification;
12. changelog has v0.3.0 notes;
13. release evidence is reviewable by a maintainer.

---

## 18. Validation Command Sequence

Recommended local release check:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-plugin-sync.py
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
git status
```

If optional scripts are not implemented yet, `docs/v0.3.0-release-checklist.md` must identify them as incomplete P0/P1 items.

---

## 19. Implementation Order

Recommended order:

1. Confirm v0.2.0 baseline files.
2. Update this implementation plan.
3. Add schema draft files.
4. Add schema validator.
5. Add plugin sync validator.
6. Harden repository validator.
7. Harden loop fixture validator.
8. Add docs validator.
9. Add snapshot protocol and optional runner.
10. Add CI workflow.
11. Update docs and README.
12. Add v0.3.0 release checklist.
13. Update CHANGELOG.
14. Run sync and validation commands.
15. Review final diff.

---

## 20. Acceptance Criteria for This Plan

This plan is complete when:

1. it clearly defines v0.3.0 as validation and tooling work;
2. it preserves v0.2.0 behavior as the baseline;
3. it separates P0 blockers, P1 recommendations, and P2 roadmap items;
4. it defines file-level changes;
5. it defines validator requirements;
6. it defines schema requirements;
7. it defines CI requirements;
8. it defines snapshot testing requirements;
9. it defines release readiness;
10. it avoids unsupported official plugin schema claims;
11. it keeps multi-skill expansion deferred;
12. it gives maintainers an executable implementation order.

---

## 21. Source Note

This file replaces the v0.2.0 remediation implementation plan. The v0.2.0 plan focused on stabilizing Loop Contract Mode and resolving P0/P1 remediation issues. This v0.3.0 plan focuses on validation, tooling, draft schemas, CI, snapshot review, and release confidence while preserving the v0.2.0 behavior contract.
