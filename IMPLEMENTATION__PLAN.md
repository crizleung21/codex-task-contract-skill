# IMPLEMENTATION__PLAN.md

Status: v0.2.0 release-candidate remediation and optimization plan  
Project: `codex-task-contract-skill`  
Primary Skill Name: `task-contract`  
Primary Plugin Name: `codex-task-contract-skill`  
Language Policy: English-only documentation and skill instructions  
Repository Policy: independent from `creator-toolchain`  
Adopted Scope: P0 + P1 implementation, P2 roadmap only

---

## 1. Executive Summary

`codex-task-contract-skill` is an open-source Codex Skill and installable Plugin package that helps Codex clarify, bound, and contract user requests before execution.

The project packages a reusable workflow named `task-contract`. The workflow turns vague, multi-step, high-impact, or iterative requests into explicit task contracts with visible scope, output expectations, acceptance criteria, and safe execution boundaries.

The v0.2.0 release-candidate goal is to stabilize Loop Contract Mode and remove release-readiness drift across canonical Skill source, plugin package, documentation, fixtures, validation scripts, and release metadata.

This implementation plan adopts the approved remediation scope:

1. Complete all P0 release-blocking corrections.
2. Complete all P1 professionalization and quality improvements.
3. Move all P2 expansion items to the roadmap rather than implementing them in v0.2.0.

---

## 2. Product Positioning

### 2.1 What This Repository Provides

`codex-task-contract-skill` provides one focused behavior package:

```text
User request -> Task Contract -> Approval-aware execution boundary
```

The Skill is not a general autonomous agent framework. It is a task-framing, scope-control, and loop-governance Skill for Codex.

### 2.2 Core Value

The repository should make Codex better at:

1. clarifying before action;
2. preserving user intent;
3. rewriting vague tasks into precise bounded tasks;
4. selecting the correct contract mode;
5. identifying high-impact actions before execution;
6. controlling iterative work through observable loops;
7. stopping safely when validation, approval, or scope boundaries require it.

---

## 3. Confirmed Decisions

| Area | Decision |
|---|---|
| Skill name | `task-contract` |
| Plugin name | `codex-task-contract-skill` |
| Repository relationship | Independent from `creator-toolchain` |
| Documentation language | English-only |
| Primary behavior | Clarify before action |
| Output modes | Compact Contract, Full Contract, Loop Contract Mode |
| v0.2.0 release focus | Stable Loop Contract Mode |
| Execution policy | Approval-aware execution boundary |
| High-impact execution | Pause before execution unless approved |
| Loop execution | Bounded iterations only |
| Loop caps | Task-type based maximum iterations |
| Hidden reasoning | Must not be requested or exposed |
| Background execution | Not supported |
| P0 scope | Implement before v0.2.0 release |
| P1 scope | Implement before v0.2.0 release where practical |
| P2 scope | Roadmap only |

---

## 4. Canonical Behavior Contract

### 4.1 Required User-Visible Framing

When `task-contract` is invoked, Codex should produce visible task framing before execution.

The core output building blocks are:

1. Auto-Skeleton
2. BLUF, when the task is non-trivial
3. Optimized Task
4. Assumptions
5. Constraints
6. Decision Points, when choices may change outcome
7. Output Contract
8. Execution Plan, when action is requested
9. Acceptance Criteria
10. Approval Gate, when high-impact execution is possible
11. Loop Contract, when bounded iteration is required
12. Loop Log, when Loop Contract Mode is used
13. Loop Stop Summary, when a loop stops
14. Next Step

### 4.2 Auto-Skeleton Fields

The Auto-Skeleton must include:

| Field | Purpose |
|---|---|
| Role | The role Codex should adopt. |
| Raw Task | The user request summarized without distortion. |
| Optimized Task | A precise, bounded, outcome-first rewrite. |
| Object | Repository, file, codebase, document, feature, question, or workflow target. |
| Context | Relevant background and implied state. |
| Constraints | Requirements, exclusions, risks, and boundaries. |
| Output | Expected deliverable shape. |
| Acceptance | How completion will be judged. |

### 4.3 Task Optimizer Requirements

The Optimized Task must:

1. start with a clear action verb;
2. identify the object of work;
3. define the target outcome;
4. bound the scope;
5. specify decision-use;
6. specify output shape;
7. include acceptance criteria;
8. preserve user intent;
9. avoid scope creep;
10. surface ambiguity as Decision Points when resolving it would change the task.

Template:

```text
[Action] [object] to [outcome], using [context and constraints], so that [decision-use]. Output [format and depth], and consider the task complete when [acceptance criteria].
```

---

## 5. Mode Selection

Choose exactly one mode per invocation unless the user explicitly asks for a comparison.

| Mode | Select When | Required Output |
|---|---|---|
| Compact Contract | The task is simple, low impact, and only slightly underspecified. | Auto-Skeleton, Optimized Task, Output Contract, Next Step. |
| Full Contract | The task is multi-step, ambiguous, repo-level, public-facing, or high impact. | Auto-Skeleton, BLUF, Optimized Task, Assumptions, Constraints, Decision Points, Output Contract, Execution Plan, Acceptance Criteria, Approval Gate, Next Step. |
| Loop Contract Mode | The task requires bounded iteration through action, observation, adjustment, validation, and safe stopping. | Full Contract plus Loop Contract, Loop Procedure, Loop Log, Validation Method, Stop Conditions, Escalation Triggers, Approval Gate, Next Step. |

Escalation rules:

1. Escalate from Compact Contract to Full Contract when a choice may change the outcome.
2. Escalate from Full Contract to Loop Contract Mode when progress depends on observable cycles.
3. Use an Approval Gate before high-impact execution.
4. Stop rather than continue when validation is blocked, approval is required, or scope drift appears.

---

## 6. Loop Contract Mode

### 6.1 Definition

Loop Contract Mode is the stable v0.2.0 task-control protocol for bounded iterative work.

It converts iterative requests into this state model:

```text
Goal -> Contract -> Plan Iteration -> Act -> Observe -> Adjust -> Validate -> Stop/Escalate
```

### 6.2 Non-Goals

Loop Contract Mode is not:

- a background worker;
- a scheduler;
- a CI orchestrator;
- an unbounded autonomous runtime;
- permission to continue indefinitely;
- permission to expand scope without approval.

### 6.3 Required Loop Contract Fields

| Field | Required | Meaning |
|---|---:|---|
| Loop Objective | Yes | The measurable final outcome. |
| Loop Type | Yes | Simple, coding/debug, research, documentation, repo maintenance, or high-impact. |
| Iteration Unit | Yes | The smallest useful action per cycle. |
| Observation Method | Yes | Evidence checked after each cycle. |
| Adjustment Strategy | Yes | How the next step changes based on the observation. |
| Validation Method | Yes | How completion is verified. |
| Stop Conditions | Yes | Success, safety, and failure stop rules. |
| Max Iterations | Yes | Maximum allowed cycles. |
| Escalation Triggers | Yes | Conditions requiring user input. |
| Approval Gate | Yes | Whether execution may proceed. |
| Loop Log | Yes | Concise user-visible evidence of iterations. |

### 6.4 Default Iteration Limits

| Loop Type | Default Max Iterations |
|---|---:|
| Simple loop | 3 |
| Coding/debug loop | 5 |
| Research loop | 3 |
| Documentation loop | 3 |
| Repo maintenance loop | 3 |
| High-impact loop | 1 before approval |

### 6.5 Mandatory Stop Conditions

A loop must stop when:

1. acceptance criteria are met;
2. max iterations are reached;
3. the same failure repeats twice;
4. required context is missing;
5. validation is not possible with available tools;
6. a high-impact change becomes necessary;
7. scope drift appears;
8. user approval is required;
9. the loop objective is no longer valid;
10. continuing would produce low-confidence or misleading output.

---

## 7. Approval Gate Policy

### 7.1 Required Approval Gate Cases

Use an Approval Gate before execution when the task may involve:

1. broad repository changes;
2. public behavior changes;
3. release metadata changes;
4. dependency installation or dependency updates;
5. destructive cleanup or file deletion;
6. security posture changes;
7. large refactors;
8. commits, pushes, tags, releases, or pull requests;
9. loop scope expansion;
10. any high-impact loop execution.

### 7.2 Approval Gate Format

```md
## Approval Gate

This action requires approval before execution because [reason].

Blocked action: [specific action]
Recommended safe default: [inspection-only / contract-only / limited edit scope]
Reply template: Approved: [bounded scope]
```

### 7.3 Safe Default

The safe default is always the narrowest useful action:

```text
Inspect and contract first; do not execute high-impact changes until approved.
```

---

## 8. Repository Architecture

### 8.1 Target Repository Structure

```text
codex-task-contract-skill/
├── README.md
├── IMPLEMENTATION__PLAN.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── AGENTS.md
├── .gitignore
├── .editorconfig
├── skills/task-contract/
│   ├── SKILL.md
│   ├── references/
│   │   ├── loop-contract-policy.md
│   │   ├── loop-observation-methods.md
│   │   ├── loop-stop-conditions.md
│   │   ├── loop-escalation-rules.md
│   │   └── loop-evaluation-rubric.md
│   ├── assets/
│   │   ├── compact-contract-template.md
│   │   ├── full-contract-template.md
│   │   ├── loop-contract-template.md
│   │   ├── compact-loop-contract-template.md
│   │   └── full-loop-contract-template.md
│   └── tests/
│       ├── fixtures/
│       └── expected/
├── plugin/codex-task-contract-skill/
│   ├── .codex-plugin/plugin.json
│   └── skills/task-contract/
├── .agents/plugins/marketplace.json
├── docs/
│   ├── installation.md
│   ├── usage.md
│   ├── testing.md
│   ├── release-process.md
│   ├── roadmap.md
│   ├── loop-contract-mode.md
│   ├── migration-v0.1-to-v0.2.md
│   ├── behavior-contract.md
│   ├── plugin-packaging.md
│   ├── plugin-manifest.md
│   ├── validator-design.md
│   └── v0.2.0-release-checklist.md
└── scripts/
    ├── sync-plugin-package.sh
    ├── validate-repo.sh
    ├── validate-repo.py
    ├── validate-loop-contract-fixtures.sh
    └── validate-loop-contract-fixtures.py
```

### 8.2 Canonical Source Rule

Canonical Skill source lives under:

```text
skills/task-contract/
```

The plugin package copy lives under:

```text
plugin/codex-task-contract-skill/skills/task-contract/
```

Canonical source must be updated first. The plugin package copy must then be synchronized using:

```bash
bash scripts/sync-plugin-package.sh
```

Manual edits inside the plugin Skill copy should be avoided unless the edit is part of sync tooling maintenance.

---

## 9. P0 Implementation Scope — Release Blockers

P0 items must be completed before v0.2.0 release readiness can be claimed.

| ID | Area | Required Change | Acceptance Criteria |
|---|---|---|---|
| P0-01 | Plugin sync | Ensure packaged Skill mirrors canonical `skills/task-contract/` source. | Canonical and plugin Skill package have no unintended drift after sync. |
| P0-02 | Terminology consistency | Standardize on `Approval Gate`, `Adjustment Strategy`, `Stop Conditions`, and `Escalation Triggers`. | No current v0.2.0 docs or fixtures use legacy terms as active behavior. |
| P0-03 | Implementation plan alignment | Rewrite implementation plan as v0.2.0 release-candidate remediation plan. | Plan reflects v0.2.0 status, P0/P1 adoption, and P2 roadmap deferral. |
| P0-04 | Validator depth | Add a zero-dependency repository validator. | Validator checks file inventory, plugin sync drift, version consistency, terminology, fixtures, and template/checklist consistency. |
| P0-05 | Loop fixture validation | Strengthen loop fixture validator beyond required terms. | Validator checks mode, required sections, required fields, forbidden patterns, approval requirements, and stop-condition coverage. |
| P0-06 | Template/checklist consistency | Align release checklist, changelog, and assets. | If compact and full loop templates are claimed, those files exist and are referenced. |
| P0-07 | Plugin manifest caveat | Document local manifest invariants and official-schema verification limits. | Repo does not claim official schema compliance without verification. |
| P0-08 | Fixture determinism | Remove ambiguous expected modes where possible. | Each fixture has one expected mode unless ambiguity is the behavior being tested. |
| P0-09 | Release metadata consistency | Align README, CHANGELOG, release process, roadmap, and checklist. | v0.2.0 status and release target are consistent across repo files. |

---

## 10. P1 Implementation Scope — Professionalization

P1 items should be completed as part of the v0.2.0 quality pass unless they become unexpectedly large.

| ID | Area | Required Change | Acceptance Criteria |
|---|---|---|---|
| P1-01 | `AGENTS.md` | Add repo-level agent operating rules. | Codex can identify canonical source, sync policy, validation commands, and safety boundaries. |
| P1-02 | Behavior contract docs | Add `docs/behavior-contract.md`. | Mode selection, output order, Approval Gate policy, and anti-patterns are documented in one stable spec. |
| P1-03 | Plugin packaging docs | Add `docs/plugin-packaging.md`. | Maintainers can sync, validate, and release plugin package without guessing. |
| P1-04 | Plugin manifest docs | Add `docs/plugin-manifest.md`. | Current manifest fields and validation boundaries are documented. |
| P1-05 | Validator design docs | Add `docs/validator-design.md`. | Validator purpose, checks, and failure modes are documented. |
| P1-06 | Security alignment | Align `SECURITY.md` and Skill Approval Gate taxonomy. | Security-sensitive behavior is consistently blocked before approval. |
| P1-07 | Expected output format | Normalize all expected fixtures. | Each expected file uses consistent Required Sections, Quality Checks, Forbidden Terms, and Approval Gate expectations. |
| P1-08 | v0.1.0 historical docs | Mark v0.1.0 checklist as historical or move to archive. | Maintainers cannot mistake v0.1.0 checklist for v0.2.0 release readiness. |
| P1-09 | Release process quality | Add sync drift and validator steps to release process. | Release process prevents stale plugin packages and inconsistent metadata. |
| P1-10 | Template quality | Standardize template column names and section ordering. | Compact, Full, and Loop templates match Skill output rules. |

---

## 11. P2 Roadmap Scope — Deferred

P2 items are useful but should not block v0.2.0.

| ID | Roadmap Item | Target Version | Reason for Deferral |
|---|---|---|---|
| P2-01 | GitHub Actions CI | v0.3.0 | Local validators should stabilize first. |
| P2-02 | Markdown lint option | v0.3.0 | Useful quality layer, not a behavior blocker. |
| P2-03 | JSON Schema or YAML Schema for contracts | v0.3.0 | Requires stable public schema decisions. |
| P2-04 | Golden output snapshot runner | v0.3.0+ | Needs a reliable output harness. |
| P2-05 | Official plugin schema validation | v0.3.0+ | Requires verified official schema source. |
| P2-06 | Marketplace publishing guide | v0.3.0+ | Should follow stable local plugin package behavior. |
| P2-07 | Multi-skill expansion | v1.0.0+ | Avoids scope creep before `task-contract` stabilizes. |
| P2-08 | Loop log summarizer | v0.3.0+ | Useful convenience, not required for v0.2.0. |
| P2-09 | Optional markdown table validator | v0.3.0+ | Adds robustness after fixture format stabilizes. |

---

## 12. File-Level Change Plan

### 12.1 Existing Files to Update

| File | Required Update | Priority |
|---|---|---:|
| `README.md` | Add plugin sync warning, validator commands, and v0.2.0 readiness wording. | P0 |
| `IMPLEMENTATION__PLAN.md` | Replace starter plan with this v0.2.0 remediation and optimization plan. | P0 |
| `CHANGELOG.md` | Add remediation notes and align template claims with actual assets. | P0 |
| `CONTRIBUTING.md` | Standardize terminology and add canonical-source/sync rule. | P0 |
| `SECURITY.md` | Align high-impact cases with Skill Approval Gate policy. | P1 |
| `skills/task-contract/SKILL.md` | Strengthen mode determinism, Approval Gate taxonomy, and loop stop rules. | P1 |
| `skills/task-contract/assets/compact-contract-template.md` | Standardize output contract column naming and compact constraints. | P1 |
| `skills/task-contract/assets/full-contract-template.md` | Replace legacy gate wording and align section order. | P0 |
| `skills/task-contract/assets/loop-contract-template.md` | Keep as shared loop template or reference it from compact/full loop variants. | P0 |
| `skills/task-contract/tests/expected/*.expected.md` | Normalize expected format and remove avoidable ambiguous modes. | P0 |
| `scripts/validate-repo.sh` | Keep as shell wrapper and call Python validator. | P0 |
| `scripts/validate-loop-contract-fixtures.py` | Expand checks for sections, modes, fields, forbidden terms, and Approval Gate coverage. | P0 |
| `scripts/sync-plugin-package.sh` | Add post-sync evidence or drift summary. | P0 |
| `docs/testing.md` | Document deterministic fixture expectations and validator scope. | P1 |
| `docs/release-process.md` | Add plugin sync drift check and manifest verification caveat. | P1 |
| `docs/v0.2.0-release-checklist.md` | Align checklist with assets, validators, and release metadata. | P0 |
| `docs/migration-v0.1-to-v0.2.md` | Add legacy term mapping and migration checklist. | P1 |
| `docs/roadmap.md` | Move P2 expansion items into v0.3.0+ roadmap. | P1 |

### 12.2 New Files to Add

| File | Purpose | Priority |
|---|---|---:|
| `AGENTS.md` | Repo-level Codex operating rules. | P1 |
| `docs/behavior-contract.md` | Stable behavior contract for Skill outputs. | P1 |
| `docs/plugin-packaging.md` | Canonical-to-plugin sync and packaging guide. | P1 |
| `docs/plugin-manifest.md` | Local manifest invariants and schema-verification caveat. | P0 |
| `docs/validator-design.md` | Validator architecture and failure criteria. | P1 |
| `skills/task-contract/assets/compact-loop-contract-template.md` | Compact loop output template. | P0 |
| `skills/task-contract/assets/full-loop-contract-template.md` | Full loop output template. | P0 |
| `scripts/validate-repo.py` | Main zero-dependency repository validator. | P0 |

---

## 13. Validator Requirements

### 13.1 `scripts/validate-repo.py`

The repository validator should be zero-dependency and should check:

1. required file inventory;
2. canonical Skill frontmatter;
3. plugin manifest local invariants;
4. plugin package sync drift;
5. release version consistency;
6. forbidden active legacy terminology;
7. required references and assets;
8. release checklist and asset consistency;
9. expected fixture mode determinism;
10. required validation scripts.

### 13.2 `scripts/validate-loop-contract-fixtures.py`

The loop fixture validator should check:

1. required loop expected files exist;
2. required sections are present;
3. required Loop Contract fields are present;
4. required Loop Log columns are present;
5. Stop Conditions are present;
6. Escalation Triggers are present;
7. Approval Gate appears for high-impact fixtures;
8. forbidden open-ended patterns are absent;
9. hidden reasoning is not requested;
10. max iteration expectations are present.

### 13.3 Forbidden Active Patterns

Validators should reject active behavioral language that implies:

- unlimited iteration;
- open-ended execution;
- background execution;
- continuing without approval;
- hidden reasoning exposure;
- destructive actions without approval;
- plugin package edits that bypass canonical source.

---

## 14. Fixture Strategy

### 14.1 Fixture Coverage

The fixture set should cover:

| Fixture | Expected Mode |
|---|---|
| `simple-writing-task.md` | Compact Contract |
| `vague-repo-task.md` | Full Contract |
| `high-risk-refactor-task.md` | Full Contract with Approval Gate |
| `documentation-task.md` | Full Contract |
| `research-task.md` | Full Contract |
| `destructive-file-task.md` | Full Contract with Approval Gate |
| `loop-debug-task.md` | Loop Contract Mode |
| `loop-research-task.md` | Loop Contract Mode |
| `loop-documentation-task.md` | Loop Contract Mode |
| `loop-dangerous-task.md` | Loop Contract Mode with Approval Gate |
| `loop-repo-maintenance-task.md` | Loop Contract Mode |

### 14.2 Expected Output File Format

Every expected output file should use this structure:

```md
# Expected: [Fixture Name]

Mode: [Expected Mode]

## Required Sections

1. ...

## Required Fields

- ...

## Required Checks

- ...

## Forbidden Patterns

- ...
```

### 14.3 Determinism Rule

Expected outputs should avoid allowing multiple modes unless the fixture is specifically designed to test ambiguity.

---

## 15. Plugin Packaging Plan

### 15.1 Package Invariants

The plugin package must preserve these invariants:

| Invariant | Requirement |
|---|---|
| Manifest name | `codex-task-contract-skill` |
| Manifest version | `0.2.0` for v0.2.0 release candidate |
| Manifest skills path | `./skills/` |
| Packaged Skill | Mirrors canonical `skills/task-contract/` |
| Marketplace path | Points to `./plugin/codex-task-contract-skill` |

### 15.2 Sync Workflow

Release sync workflow:

```bash
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
git status
```

### 15.3 Manifest Caveat

The repository should validate local manifest invariants, but it should not claim official Codex plugin manifest schema compliance unless the schema has been verified against an authoritative source.

---

## 16. Documentation Plan

### 16.1 Human-Facing Docs

| Doc | Purpose |
|---|---|
| `README.md` | Explain the project, quick usage, structure, and release check. |
| `docs/installation.md` | Explain canonical source, plugin package, marketplace metadata, and verification. |
| `docs/usage.md` | Explain invocation, mode selection, examples, and good output criteria. |
| `docs/testing.md` | Explain fixtures, manual testing, automated checks, and scoring. |
| `docs/release-process.md` | Explain release validation, sync, tag, and release notes. |
| `docs/roadmap.md` | Track v0.3.0+ deferred work. |
| `docs/loop-contract-mode.md` | Explain stable bounded loop behavior. |
| `docs/migration-v0.1-to-v0.2.md` | Explain behavior and terminology migration. |

### 16.2 Maintainer-Facing Docs

| Doc | Purpose |
|---|---|
| `AGENTS.md` | Codex operating rules for the repo. |
| `docs/behavior-contract.md` | Stable behavioral specification. |
| `docs/plugin-packaging.md` | Plugin package sync and validation guide. |
| `docs/plugin-manifest.md` | Manifest field expectations and caveats. |
| `docs/validator-design.md` | Validator design and failure model. |
| `docs/v0.2.0-release-checklist.md` | Release readiness checklist. |

---

## 17. Release Readiness Definition

v0.2.0 is ready when:

1. `skills/task-contract/SKILL.md` treats Loop Contract Mode as stable;
2. compact, full, and loop modes remain present;
3. Loop Contract Mode has objective, iteration unit, observation, adjustment, validation, stop conditions, max iterations, escalation triggers, approval gate, and loop log;
4. high-impact work pauses at Approval Gate;
5. no open-ended loop behavior is encouraged;
6. no hidden reasoning is requested or exposed;
7. canonical Skill and plugin package copy are synchronized;
8. plugin manifest local invariants pass validation;
9. expected fixtures have deterministic modes;
10. loop fixtures pass loop validator;
11. repository validator passes;
12. release checklist passes;
13. roadmap contains deferred P2 items;
14. README, CHANGELOG, release process, and roadmap agree on v0.2.0 status.

---

## 18. Validation Commands

Before release or final review, run:

```bash
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
git status
```

Expected final state:

```text
Repository validation passed.
Loop fixture validation passed.
Plugin package synced.
No unexpected working tree changes remain.
```

---

## 19. Implementation Order

Recommended order:

1. Update canonical `skills/task-contract/SKILL.md`.
2. Update loop references and templates.
3. Add compact and full loop templates if claimed by release docs.
4. Normalize expected fixtures.
5. Add or expand validators.
6. Update docs and release metadata.
7. Add `AGENTS.md`.
8. Add behavior, packaging, manifest, and validator design docs.
9. Move P2 items to roadmap.
10. Run validators.
11. Sync plugin package.
12. Run validators again.
13. Review final diff.

---

## 20. Acceptance Criteria for This Plan

This plan is complete when:

1. it reflects the adopted A scope: P0 + P1 implementation, P2 roadmap only;
2. it treats v0.2.0 as the active release-candidate target;
3. it uses current v0.2.0 terminology consistently;
4. it identifies file-level changes for implementation;
5. it defines release blockers separately from roadmap work;
6. it defines validator requirements;
7. it preserves English-only documentation policy;
8. it keeps the repository independent from `creator-toolchain`;
9. it avoids unsupported official plugin schema claims;
10. it gives maintainers a clear implementation order.

---

## 21. Source Note

This file replaces the earlier starter implementation plan. The previous plan documented the v0.1.0 foundation and a planned v0.2.0 loop extension. This version is the v0.2.0 release-candidate remediation and optimization plan based on the approved P0 + P1 scope, with P2 items deferred to the roadmap.
