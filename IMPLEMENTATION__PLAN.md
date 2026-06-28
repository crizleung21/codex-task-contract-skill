# IMPLEMENTATION__PLAN.md

## 1. BLUF

This implementation plan upgrades `codex-task-contract-skill` from the v0.4.0 core-function release candidate into a coherent **v0.5.0 behavior-strengthening release**.

v0.4.0 established the core task-contract Skill surface: Auto-Skeleton, Task Optimizer, Compact Contract, Full Contract, Loop Contract Mode, Approval Gate, Loop Log, draft schemas, repository validators, CI checks, plugin package synchronization, snapshot coverage, loop regression tests, and preliminary multi-agent sub-contracting.

v0.5.0 focuses on strengthening execution reliability and maintainability by improving:

1. mode taxonomy consistency;
2. semantic contract validation;
3. fixture coverage visibility;
4. release consistency validation;
5. subagent contract safety boundaries;
6. installation smoke testing;
7. local/CI validation parity;
8. user-facing examples for delegation workflows;
9. roadmap preparation for golden output tests, contract linting, presets, and v1.0.0 behavior freeze.

The goal of v0.5.0 is **not** to claim official marketplace publishing readiness, official plugin schema compliance, or v1.0.0 schema stability. The goal is to make the Skill more reliable, testable, bounded, and safer for Codex repository-level workflows.

Recommended implementation scope: **complete all P0 and P1 items for v0.5.0; keep P2 items in the roadmap unless separately approved.**

---

## 2. Release Target

| Field | Value |
|---|---|
| Active release target | `v0.5.0` |
| Previous release target | `v0.4.0` |
| Core Skill | `task-contract` |
| Plugin package | `codex-task-contract-skill` |
| Canonical Skill source | `skills/task-contract/` |
| Packaged Skill copy | `plugin/codex-task-contract-skill/skills/task-contract/` |
| Plugin manifest | `plugin/codex-task-contract-skill/.codex-plugin/plugin.json` |
| Release configuration | `config/release.json` |
| Schemas directory | `schemas/` |
| Test fixtures | `skills/task-contract/tests/fixtures/` |
| Expected outputs | `skills/task-contract/tests/expected/` |
| Snapshots | `skills/task-contract/tests/snapshots/` |
| Docs language | English-only |
| Validation style | Local, deterministic, zero-network unless explicitly approved |
| Public compliance boundary | Do not claim official Codex/plugin marketplace schema compliance until authoritative schema validation exists |
| v1.0.0 boundary | Do not freeze public behavior contract in v0.5.0 |

---

## 3. Why v0.5.0 Exists

### 3.1 v0.4.0 Strengths

The repository already contains the major conceptual building blocks needed for a useful task-contract Skill:

1. **Auto-Skeleton** for visible task framing.
2. **Task Optimizer** for precise, bounded, outcome-first task rewriting.
3. **Compact Contract** for simple, low-impact tasks.
4. **Full Contract** for complex, ambiguous, repo-level, public-facing, or high-impact tasks.
5. **Loop Contract Mode** for bounded iterative work with observation, adjustment, validation, stop conditions, escalation triggers, and iteration caps.
6. **Approval Gate** for high-impact or destructive execution.
7. **Loop Log** for visible iteration evidence.
8. **Multi-Agent Sub-contracting** for bounded delegation.
9. **Draft schemas** for contract structures.
10. **Validation scripts** for repository structure, schemas, documentation, loop fixtures, snapshots, and plugin sync.
11. **CI workflow** for automated validation.
12. **Plugin package layout** for Codex/plugin installation.

These are strong foundations. The remaining work is not primarily about inventing new conceptual behavior. The remaining work is about making the behavior more internally consistent, more enforceable, and easier to verify.

### 3.2 v0.5.0 Gaps to Close

The v0.5.0 release should close the following gaps:

1. **Mode taxonomy drift**  
   Extended modes such as Approval Gate and Subagent Delegation exist in fixtures and validators, but the main task contract schema still treats mode mostly as a small base enum.

2. **Semantic validation gap**  
   Current validators mostly check files, terms, sections, schema structure, and snapshot presence. They do not deeply validate task-contract behavior semantics such as “Auto-Skeleton first,” “one clear next step,” “Decision Points include trade-offs,” or “high-impact loops stop before approval.”

3. **Fixture coverage visibility gap**  
   Fixtures exist, expected outputs exist, and snapshots exist, but there is no explicit fixture matrix showing coverage across base modes, modifiers, risk levels, Approval Gate requirements, Loop Contract use, and Subagent Delegation.

4. **Release consistency gap**  
   `config/release.json` centralizes release metadata, but release drift detection should become stricter and more reusable across future versions.

5. **Subagent safety gap**  
   Current Subagent Contract fields define basic delegation metadata, but they should be strengthened with explicit path, tool, evidence, merge, and failure boundaries.

6. **Installation verification gap**  
   Installation docs currently describe expected manual behavior, but a deterministic local smoke test should verify packaged Skill availability, manifest version, sync state, and marketplace metadata.

7. **Usage discoverability gap**  
   User-facing usage docs describe Compact, Full, and Loop Contract modes, but Subagent Delegation should be documented as a first-class usage pattern.

8. **Future harness gap**  
   Golden output testing, contract linting, and contract presets are valuable but should remain roadmap-level unless separately approved.

---

## 4. Current State Audit

### 4.1 Existing Implementation Plan Is v0.4.0-Oriented

The current implementation plan frames the repository as a v0.4.0 core-function release state. It identifies release alignment, validation, schemas, CI, plugin sync, and preliminary subagent delegation as the major focus.

However, the plan is no longer the right active execution blueprint after the v0.5.0 enhancement route has been selected. It should be rewritten to target v0.5.0, while keeping v0.4.0 as the previous baseline.

### 4.2 Mode Taxonomy Is Not Yet Fully Normalized

Current expected outputs and validators use extended mode labels such as:

- `Full Contract with Approval Gate`
- `Full Contract with Subagent Delegation`
- `Loop Contract Mode with Approval Gate`
- `Loop Contract Mode with Subagent Delegation`
- `Loop Contract Mode with Approval Gate and Subagent Delegation`

The main task contract schema should not rely on long string labels as the primary representation. The recommended v0.5.0 model is:

```json
{
  "base_mode": "Full Contract",
  "modifiers": ["approval_gate", "subagent_delegation"]
}
```

This separates the contract family from optional behavior modifiers and supports future expansion without multiplying mode strings.

### 4.3 Validation Is Present but Too Structural

Current validators are useful and should be preserved. However, v0.5.0 should add behavior-level validation to catch failures such as:

1. missing Auto-Skeleton;
2. Auto-Skeleton not appearing first;
3. vague Optimized Task;
4. Decision Points without trade-offs;
5. Approval Gate present but not blocking execution;
6. Loop Contract without clear stop conditions;
7. high-impact loop allowing too many iterations before approval;
8. Subagent Contract missing recursion lock;
9. final response containing multiple next steps;
10. hidden or background execution claims.

### 4.4 Subagent Delegation Exists but Needs Stronger Boundaries

The repository already defines Subagent Delegation behavior and a draft schema. v0.5.0 should harden this into a safer and more explicit delegation protocol by adding:

1. allowed paths;
2. forbidden paths;
3. allowed tools;
4. forbidden tools;
5. handoff input;
6. evidence requirements;
7. return schema;
8. merge policy;
9. failure policy.

This prevents delegation from becoming an unbounded execution path.

### 4.5 Installation Verification Should Become Testable

The installation documentation should remain human-readable, but v0.5.0 should add a smoke test that verifies the package can be installed and recognized at a file-layout level before any user relies on manual invocation.

---

## 5. Scope

### 5.1 In Scope for v0.5.0

This plan covers:

1. upgrading `IMPLEMENTATION__PLAN.md` to target v0.5.0;
2. updating release metadata to v0.5.0;
3. normalizing mode taxonomy across schemas, fixtures, validators, docs, and snapshots;
4. adding a release consistency validator;
5. adding a semantic contract validator;
6. adding a fixture matrix;
7. strengthening Subagent Contract schema and template fields;
8. updating Subagent Delegation policy and usage documentation;
9. adding installation smoke testing;
10. improving local/CI validation parity;
11. creating a v0.5.0 release checklist;
12. updating README, AGENTS, docs, changelog, and roadmap;
13. keeping P2 expansion work clearly separated from release blockers.

### 5.2 Out of Scope for v0.5.0

The following items are explicitly out of scope unless separately approved:

1. official marketplace publishing;
2. official plugin schema compliance claims;
3. network-dependent validation;
4. live model-output execution harness as a release blocker;
5. autonomous background work;
6. general multi-skill orchestration;
7. v1.0.0 behavior/schema freeze;
8. dependency-heavy validation tooling;
9. broad repository refactors unrelated to task-contract behavior;
10. destructive cleanup.

---

## 6. P0 Required Fixes

P0 items are release blockers. Complete these before treating v0.5.0 as execution-ready.

---

### P0-01 — Upgrade the Implementation Plan Target to v0.5.0

#### Problem

`IMPLEMENTATION__PLAN.md` currently describes a v0.4.0 core-function release state. The selected direction is now v0.5.0 behavior strengthening.

#### Required Changes

Update `IMPLEMENTATION__PLAN.md` so that it:

1. identifies `v0.5.0` as the active release target;
2. identifies `v0.4.0` as the previous baseline;
3. describes v0.5.0 as a behavior-strengthening release;
4. separates P0, P1, and P2 work;
5. includes validation strategy and implementation order;
6. makes P2 items roadmap-only unless separately approved.

#### Files to Update

```text
IMPLEMENTATION__PLAN.md
```

#### Acceptance Criteria

- `IMPLEMENTATION__PLAN.md` clearly targets v0.5.0.
- v0.4.0 appears only as historical or previous baseline context.
- P0/P1/P2 are all present and clearly separated.
- The plan can be executed without relying on conversation history.

---

### P0-02 — Update Central Release Configuration to v0.5.0

#### Problem

Release target, release tag, and schema version should be controlled by `config/release.json`. The active config must be updated before validators can enforce v0.5.0.

#### Required Changes

Update:

```text
config/release.json
```

Recommended content:

```json
{
  "release_target": "0.5.0",
  "release_tag": "v0.5.0",
  "schema_version": "0.5.0-draft",
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

#### Files to Update

```text
config/release.json
plugin/codex-task-contract-skill/.codex-plugin/plugin.json
README.md
AGENTS.md
CHANGELOG.md
docs/roadmap.md
docs/release-process.md
docs/v0.5.0-release-checklist.md
schemas/*.schema.json
```

#### Acceptance Criteria

- `config/release.json` uses `0.5.0`, `v0.5.0`, and `0.5.0-draft`.
- Plugin manifest version matches `config/release.json`.
- Active docs refer to v0.5.0 as the active target.
- Older release references remain only in changelog, roadmap, or archive context.

---

### P0-03 — Normalize Mode Taxonomy

#### Problem

The repository currently mixes base modes and extended behavior labels. Long string labels such as `Full Contract with Approval Gate` are useful for human-readable expected files, but they should not be the primary machine contract model.

#### Required Changes

Adopt this model across schemas, validators, fixtures, docs, and snapshots:

```json
{
  "base_mode": "Full Contract",
  "modifiers": ["approval_gate", "subagent_delegation"]
}
```

Supported base modes:

```text
Compact Contract
Full Contract
Loop Contract Mode
```

Supported v0.5.0 modifiers:

```text
approval_gate
subagent_delegation
```

Future modifiers may include:

```text
research_verified
repo_write_blocked
artifact_output
security_review
```

#### Files to Update

```text
schemas/task-contract.schema.json
schemas/expected-output.schema.json
schemas/loop-contract.schema.json
scripts/validate-repo.py
scripts/validate-schemas.py
skills/task-contract/tests/expected/*.expected.md
skills/task-contract/tests/snapshots/*.snapshot.md
docs/behavior-contract.md
docs/schema-design.md
docs/testing.md
docs/snapshot-testing.md
skills/task-contract/tests/FIXTURE_MATRIX.md
```

#### Recommended Schema Shape

```json
{
  "base_mode": {
    "type": "string",
    "enum": [
      "Compact Contract",
      "Full Contract",
      "Loop Contract Mode"
    ]
  },
  "modifiers": {
    "type": "array",
    "items": {
      "type": "string",
      "enum": [
        "approval_gate",
        "subagent_delegation"
      ]
    },
    "uniqueItems": true
  }
}
```

#### Backward Compatibility

Expected output files may keep a human-readable `Mode:` line, but validators should also require machine-readable metadata such as:

```yaml
Base Mode: Full Contract
Modifiers:
  - approval_gate
  - subagent_delegation
```

#### Acceptance Criteria

- Every fixture maps to exactly one `base_mode`.
- Every modifier is represented independently.
- `approval_gate` and `subagent_delegation` are not encoded only as long mode strings.
- `schemas/task-contract.schema.json`, `schemas/expected-output.schema.json`, and validators agree on the taxonomy.
- Backward-readable expected output files remain understandable to human maintainers.

---

### P0-04 — Add Release Consistency Validator

#### Problem

Release drift can reappear across README, AGENTS, docs, schemas, manifest, fixtures, and validators if only partial string checks are used.

#### Required Changes

Add:

```text
scripts/validate-release-consistency.py
```

The validator must read:

```text
config/release.json
```

and verify consistency across:

```text
README.md
AGENTS.md
CHANGELOG.md
docs/release-process.md
docs/testing.md
docs/ci.md
docs/schema-design.md
docs/snapshot-testing.md
docs/validator-design.md
docs/plugin-packaging.md
docs/plugin-manifest.md
docs/roadmap.md
docs/v0.5.0-release-checklist.md
plugin/codex-task-contract-skill/.codex-plugin/plugin.json
schemas/*.schema.json
.github/workflows/validate.yml
scripts/*.py
scripts/*.sh
```

#### Required Checks

1. Active release docs must reference `v0.5.0`.
2. Schema defaults must match `0.5.0-draft`.
3. Plugin manifest version must match `0.5.0`.
4. CI must include v0.5.0 validation commands.
5. The active checklist must be `docs/v0.5.0-release-checklist.md`.
6. Older versions must not be described as current release gates.
7. Old release references are allowed only in:
   - `CHANGELOG.md`;
   - `docs/roadmap.md`;
   - `docs/archive/`;
   - explicit previous-release context.

#### Acceptance Criteria

- Validator fails on stale active references to v0.4.0, v0.3.0, or v0.2.0.
- Validator reads release target from `config/release.json`.
- Validator does not require network access.
- Validator is included in local validation, CI, and pre-commit parity review.

---

### P0-05 — Complete v0.5.0 Release Checklist

#### Problem

A new release target requires a matching checklist. v0.4.0 checklists should not serve as active v0.5.0 release gates.

#### Required Changes

Add:

```text
docs/v0.5.0-release-checklist.md
```

The checklist must include:

1. scope confirmation;
2. required files;
3. local validation commands;
4. CI validation commands;
5. schema and taxonomy checks;
6. semantic validator checks;
7. fixture matrix checks;
8. subagent contract hardening checks;
9. installation smoke test;
10. human review;
11. tagging instructions;
12. release note summary.

#### Files to Update

```text
docs/v0.5.0-release-checklist.md
README.md
AGENTS.md
docs/release-process.md
docs/testing.md
docs/ci.md
docs/validator-design.md
```

#### Acceptance Criteria

- Active release checklist is v0.5.0.
- Older checklists remain historical only.
- Checklist includes all P0 and P1 validation gates.
- Checklist does not list P2 roadmap items as release blockers.

---

### P0-06 — Update Plugin Manifest and Package Sync Expectations

#### Problem

Plugin manifest metadata must match the v0.5.0 release target, and packaged Skill files must stay synchronized with the canonical Skill source.

#### Required Changes

Update:

```text
plugin/codex-task-contract-skill/.codex-plugin/plugin.json
```

Recommended content:

```json
{
  "name": "codex-task-contract-skill",
  "version": "0.5.0",
  "description": "A Codex plugin that installs the task-contract skill for converting vague, multi-step, high-impact, or iterative requests into compact, full, or stable loop task contracts before execution, with v0.5.0 behavior validation, taxonomy consistency, subagent boundaries, and tooling support.",
  "skills": "./skills/"
}
```

Then ensure:

```bash
bash scripts/sync-plugin-package.sh
python3 scripts/validate-plugin-sync.py
```

#### Acceptance Criteria

- Manifest version is `0.5.0`.
- Manifest skill path remains `./skills/`.
- Canonical and packaged Skill copies match after sync.
- Plugin sync validation passes.

---

## 7. P1 Functional Enhancements

P1 items are part of the recommended v0.5.0 release scope. They should be completed after P0 release consistency is in place.

---

### P1-01 — Add Semantic Contract Validator

#### Problem

Current validators mostly check structural presence, required terms, JSON schema shape, snapshot protocol, and loop fixture fields. They do not fully validate behavior semantics.

#### Required Changes

Add:

```text
scripts/validate-contract-semantics.py
```

This validator should inspect expected outputs and snapshots to verify behavior-level requirements.

#### Required Semantic Checks

1. **Auto-Skeleton first**
   - Output must begin with Auto-Skeleton when the Skill is invoked.
   - Auto-Skeleton must include Role, Raw Task, Optimized Task, Object, Context, Constraints, Output, and Acceptance.

2. **Optimized Task completeness**
   - Optimized Task must contain:
     - action verb;
     - object;
     - outcome;
     - scope boundary;
     - output shape;
     - acceptance criteria.

3. **Decision Point quality**
   - Decision Points must include numbered options.
   - Options must state trade-offs.
   - A recommended default must be present when justified.
   - A reply template must be present when user choice is needed.

4. **Approval Gate correctness**
   - High-risk tasks must include Approval Gate.
   - Approval Gate must identify:
     - reason;
     - blocked action;
     - recommended safe default;
     - reply template.
   - Approval Gate must clearly block execution until approval is given.

5. **Loop Contract completeness**
   - Loop contracts must include:
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
     - Loop Log.

6. **High-impact loop safety**
   - High-impact loops must use max iteration 1 before approval.
   - High-impact loops must stop before broad or destructive execution.

7. **Subagent safety**
   - Subagent contracts must include scope boundary.
   - `recursion_lock` must be true by default.
   - Subagent cannot spawn subagents unless explicitly approved.
   - Parent contract must control merge or final execution decision.

8. **Final response rule**
   - Output must end with exactly one clear next step.
   - Output must not contain multiple competing next steps.

9. **Forbidden behavior**
   - No open-ended loops.
   - No background execution claim.
   - No unapproved destructive action.
   - No hidden chain-of-thought request or exposure.
   - No unlimited iteration.

#### Files to Add or Update

```text
scripts/validate-contract-semantics.py
.github/workflows/validate.yml
scripts/pre-commit-hook.sh
docs/testing.md
docs/validator-design.md
docs/ci.md
docs/v0.5.0-release-checklist.md
```

#### Acceptance Criteria

- Validator fails on behavior-critical missing sections.
- Validator detects unsafe Approval Gate wording.
- Validator detects missing Loop stop conditions.
- Validator detects Subagent Contracts without recursion lock.
- Validator runs locally and in CI.
- Validator is deterministic and requires no network access.

---

### P1-02 — Add Fixture Matrix

#### Problem

Fixtures, expected outputs, and snapshots exist, but there is no single coverage matrix showing which behaviors are tested.

#### Required Changes

Add:

```text
skills/task-contract/tests/FIXTURE_MATRIX.md
```

#### Required Matrix Columns

```md
| Fixture | Base Mode | Modifiers | Risk Class | Approval Gate Required | Loop Required | Subagent Required | Expected Output | Snapshot | Validators |
|---|---|---|---|---|---|---|---|---|---|
```

#### Required Coverage Rows

At minimum, include all existing fixture families:

1. simple writing task;
2. vague repository task;
3. high-risk refactor task;
4. documentation task;
5. research task;
6. destructive file task;
7. loop debug task;
8. loop research task;
9. loop documentation task;
10. loop dangerous task;
11. loop repo maintenance task;
12. subagent delegation task.

#### Required Checks

The matrix should make it easy to confirm:

1. every fixture has a matching expected output;
2. every fixture has a matching snapshot;
3. every base mode is covered;
4. every v0.5.0 modifier is covered;
5. high-risk tasks trigger Approval Gate;
6. loop tasks include Loop Contract Mode;
7. subagent tasks include Subagent Contract metadata.

#### Files to Add or Update

```text
skills/task-contract/tests/FIXTURE_MATRIX.md
scripts/validate-repo.py
scripts/run-snapshots.py
docs/testing.md
docs/snapshot-testing.md
docs/v0.5.0-release-checklist.md
```

#### Acceptance Criteria

- Every fixture appears exactly once in the matrix.
- Every expected file maps to exactly one fixture.
- Every snapshot maps to exactly one fixture.
- Matrix identifies mode, modifiers, risk, and validator coverage.
- Repository validator checks that the matrix exists.

---

### P1-03 — Strengthen Subagent Contract Schema

#### Problem

Current Subagent Contract fields provide useful basic structure but do not fully constrain execution boundaries.

#### Required Changes

Update:

```text
schemas/subagent-contract.schema.json
```

Add fields:

```json
{
  "allowed_paths": {
    "type": "array",
    "items": { "type": "string", "minLength": 1 },
    "minItems": 1
  },
  "forbidden_paths": {
    "type": "array",
    "items": { "type": "string", "minLength": 1 }
  },
  "allowed_tools": {
    "type": "array",
    "items": { "type": "string", "minLength": 1 }
  },
  "forbidden_tools": {
    "type": "array",
    "items": { "type": "string", "minLength": 1 }
  },
  "handoff_input": {
    "type": "object"
  },
  "evidence_required": {
    "type": "array",
    "items": { "type": "string", "minLength": 1 },
    "minItems": 1
  },
  "return_schema": {
    "type": "object"
  },
  "merge_policy": {
    "type": "string",
    "enum": [
      "parent_only",
      "parent_review_required",
      "no_merge_allowed"
    ]
  },
  "failure_policy": {
    "type": "string",
    "enum": [
      "escalate_to_parent",
      "stop_without_retry",
      "retry_with_parent_approval"
    ]
  }
}
```

#### Recommended Required Fields

Add to required list:

```json
[
  "allowed_paths",
  "forbidden_paths",
  "allowed_tools",
  "forbidden_tools",
  "evidence_required",
  "merge_policy",
  "failure_policy"
]
```

#### Files to Update

```text
schemas/subagent-contract.schema.json
skills/task-contract/SKILL.md
skills/task-contract/references/subagent-delegation-policy.md
skills/task-contract/assets/subagent-contract-template.md
skills/task-contract/tests/expected/subagent-delegation-task.expected.md
skills/task-contract/tests/snapshots/subagent-delegation-task.snapshot.md
docs/behavior-contract.md
docs/schema-design.md
docs/usage.md
```

#### Acceptance Criteria

- Subagent Contract defines explicit path boundaries.
- Subagent Contract defines tool boundaries.
- Subagent Contract defines evidence requirements.
- Subagent Contract defines parent-controlled merge policy.
- Subagent Contract defines failure policy.
- Recursion lock remains required.
- Validators reject Subagent Contracts without boundary metadata.

---

### P1-04 — Update Subagent Delegation Policy and Template

#### Problem

The main Skill defines Subagent Delegation behavior, but the template and policy should be updated to reflect stronger v0.5.0 boundaries.

#### Required Changes

Update:

```text
skills/task-contract/references/subagent-delegation-policy.md
skills/task-contract/assets/subagent-contract-template.md
skills/task-contract/SKILL.md
```

#### Required Policy Additions

The policy must define:

1. subagent delegation is optional and scope-bounded;
2. parent contract must exist before delegation;
3. parent approval is required before high-impact delegated actions;
4. subagents cannot write outside `allowed_paths`;
5. subagents cannot use tools outside `allowed_tools`;
6. subagents cannot access `forbidden_paths`;
7. subagents cannot use `forbidden_tools`;
8. recursion lock defaults to true;
9. subagent output must include evidence required by the parent;
10. parent controls merge and final execution;
11. subagent failure escalates to the parent.

#### Required Template Sections

```md
## Subagent Contract

| Field | Value |
|---|---|
| parent_conversation_id | ... |
| subagent_role | ... |
| scope_boundary | ... |
| allowed_paths | ... |
| forbidden_paths | ... |
| allowed_tools | ... |
| forbidden_tools | ... |
| constraints | ... |
| recursion_lock | true |
| approval_gate | ... |
| acceptance_criteria | ... |
| evidence_required | ... |
| return_format | ... |
| return_schema | ... |
| merge_policy | parent_only |
| failure_policy | escalate_to_parent |
```

#### Acceptance Criteria

- Template matches schema.
- Policy matches schema.
- Main `SKILL.md` references strengthened policy and template.
- Expected output fixture includes v0.5.0 fields.
- Snapshot includes v0.5.0 fields.

---

### P1-05 — Add Subagent Delegation Usage Examples

#### Problem

Usage docs currently describe Compact, Full, and Loop Contract modes, but Subagent Delegation should become a first-class documented usage pattern.

#### Required Changes

Update:

```text
docs/usage.md
docs/behavior-contract.md
README.md
```

Add a section:

~~~md
## Subagent Delegation Example Prompt

```text
Use $task-contract to split this repository audit into bounded subagent contracts:
1. docs auditor
2. schema auditor
3. CI validator

Do not edit files until I approve the parent plan.
```

Expected mode:

```text
Base Mode: Full Contract
Modifiers:
  - subagent_delegation
  - approval_gate
```

Expected behavior:

1. produce a parent Full Contract;
2. identify bounded subagent contracts;
3. define allowed paths and tools per subagent;
4. set recursion lock to true;
5. require evidence from each subagent;
6. block broad execution until parent approval.
~~~

#### Acceptance Criteria

- Usage docs include at least one Subagent Delegation example.
- Example includes parent contract and bounded subcontracts.
- Example includes Approval Gate when edits are blocked.
- Example is consistent with v0.5.0 taxonomy.

---

### P1-06 — Add Installation Smoke Test

#### Problem

Installation verification is currently mostly manual. v0.5.0 should include deterministic file-layout and package checks.

#### Required Changes

Add:

```text
scripts/smoke-test-installation.sh
```

Recommended implementation:

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

test -f "$ROOT/config/release.json"
test -f "$ROOT/plugin/codex-task-contract-skill/.codex-plugin/plugin.json"
test -f "$ROOT/plugin/codex-task-contract-skill/skills/task-contract/SKILL.md"
test -f "$ROOT/.agents/plugins/marketplace.json"

python3 "$ROOT/scripts/validate-plugin-sync.py"
python3 "$ROOT/scripts/validate-release-consistency.py"

echo "Installation smoke test passed."
```

#### Files to Add or Update

```text
scripts/smoke-test-installation.sh
docs/installation.md
docs/testing.md
docs/ci.md
.github/workflows/validate.yml
docs/v0.5.0-release-checklist.md
```

#### Acceptance Criteria

- Smoke test verifies release config exists.
- Smoke test verifies plugin manifest exists.
- Smoke test verifies packaged Skill exists.
- Smoke test verifies marketplace metadata exists.
- Smoke test verifies plugin sync.
- Smoke test verifies release consistency.
- Smoke test runs locally and in CI.

---

### P1-07 — Improve CI and Local Validation Parity

#### Problem

Local release gates and CI checks should remain aligned. Any new v0.5.0 validator must be included consistently.

#### Required Local Validation Sequence

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-release-consistency.py
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
python3 scripts/validate-contract-semantics.py
bash scripts/smoke-test-installation.sh
git status
```

#### Required CI Validation Sequence

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-release-consistency.py
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
python3 scripts/validate-contract-semantics.py
bash scripts/smoke-test-installation.sh
```

`git status` remains local-only and should not be required in CI.

#### Files to Update

```text
.github/workflows/validate.yml
scripts/pre-commit-hook.sh
docs/ci.md
docs/testing.md
docs/release-process.md
docs/v0.5.0-release-checklist.md
README.md
AGENTS.md
```

#### Acceptance Criteria

- CI includes all non-interactive v0.5.0 checks.
- Local validation sequence includes all CI checks plus `git status`.
- Pre-commit hook either runs the same checks or documents a justified subset.
- Release checklist matches both local and CI validation.

---

### P1-08 — Update Documentation for v0.5.0

#### Problem

Docs must reflect v0.5.0 behavior, taxonomy, validators, and release boundaries.

#### Required Changes

Update:

```text
README.md
AGENTS.md
CHANGELOG.md
docs/usage.md
docs/installation.md
docs/testing.md
docs/release-process.md
docs/roadmap.md
docs/validator-design.md
docs/schema-design.md
docs/snapshot-testing.md
docs/ci.md
docs/behavior-contract.md
docs/plugin-packaging.md
docs/plugin-manifest.md
```

#### Required Documentation Updates

1. README states v0.5.0 release target.
2. README lists semantic validation and release consistency validation.
3. AGENTS lists v0.5.0 release gates.
4. CHANGELOG includes v0.5.0 release candidate section.
5. Usage docs include Subagent Delegation example.
6. Installation docs include smoke test.
7. Testing docs include all validators.
8. CI docs mirror local validation.
9. Schema docs explain `base_mode` and `modifiers`.
10. Roadmap moves P2 items to v0.6.0 or later.
11. Plugin docs avoid official compliance claims.

#### Acceptance Criteria

- Active docs consistently describe v0.5.0.
- Docs do not claim v1.0.0 schema stability.
- Docs do not claim official marketplace compliance.
- Docs match validators and schemas.

---

## 8. P2 Roadmap Enhancements

P2 items are valuable but should not block v0.5.0 unless separately approved.

---

### P2-01 — Golden Output Harness

#### Purpose

A golden output harness would validate generated task-contract outputs against snapshots, schemas, semantic validators, and normalized Markdown structure.

#### Future File

```text
scripts/run-golden-output-tests.py
```

#### Proposed Flow

```text
fixture prompt
-> candidate output
-> normalize markdown
-> validate base_mode/modifiers
-> validate required sections
-> validate schema
-> validate semantic rules
-> compare with snapshot expectations
-> report diff
```

#### Roadmap Acceptance Criteria

- Not required for v0.5.0.
- Can be implemented offline first.
- Live model integration must remain optional.
- Network-dependent tests must not block local validation.

---

### P2-02 — Contract Linter CLI

#### Purpose

A contract linter would allow maintainers to validate a generated contract output manually.

#### Future File

```text
scripts/lint-contract-output.py
```

#### Proposed Checks

1. missing Auto-Skeleton;
2. Auto-Skeleton not first;
3. vague Optimized Task;
4. missing Output Contract;
5. duplicate Next Steps;
6. Decision Points without trade-offs;
7. Approval Gate without blocked action;
8. Loop Contract without stop conditions;
9. Subagent Contract without recursion lock;
10. unsafe background execution claim.

#### Example Usage

```bash
python3 scripts/lint-contract-output.py path/to/output.md
```

#### Roadmap Acceptance Criteria

- Reuse semantic validator rules where possible.
- Does not require network access.
- Can lint arbitrary Markdown outputs.

---

### P2-03 — Contract Profile Presets

#### Purpose

Presets would reduce repeated mode-selection logic by defining reusable task profiles.

#### Future Directory

```text
skills/task-contract/presets/
```

#### Example Presets

```text
repo-audit.json
safe-refactor.json
docs-review.json
release-readiness.json
loop-debug.json
subagent-audit.json
```

#### Example Preset Shape

```json
{
  "preset_name": "repo-audit",
  "default_base_mode": "Full Contract",
  "default_modifiers": ["approval_gate"],
  "risk_level": "medium",
  "required_sections": [
    "Auto-Skeleton",
    "BLUF",
    "Optimized Task",
    "Output Contract",
    "Acceptance Criteria",
    "Approval Gate",
    "Next Step"
  ],
  "approval_gate_required_when": [
    "broad repository changes",
    "release metadata changes",
    "file deletion"
  ],
  "default_max_iterations": 3
}
```

#### Roadmap Acceptance Criteria

- Reuse v0.5.0 taxonomy.
- Do not introduce preset logic before schemas and validators stabilize.
- Keep presets optional.

---

### P2-04 — Marketplace Publishing Guide

#### Purpose

A future marketplace guide may document packaging and publishing workflow.

#### Future File

```text
docs/marketplace-publishing.md
```

#### Boundary

This should remain roadmap-only until official marketplace requirements and authoritative plugin schema validation are confirmed.

#### Roadmap Acceptance Criteria

- No unsupported compliance claim.
- Clearly distinguish local package validation from official marketplace acceptance.
- Include manual reviewer checklist only after authoritative requirements are known.

---

### P2-05 — v1.0.0 Behavior Freeze Preparation

#### Purpose

v1.0.0 should freeze stable behavior, schema names, mode taxonomy, and compatibility guarantees.

#### Future Work

1. freeze base modes;
2. freeze modifier vocabulary;
3. freeze schema field names;
4. freeze contract section order;
5. define migration policy;
6. add compatibility notes;
7. add stable example outputs;
8. add versioned schema migration docs.

#### Roadmap Acceptance Criteria

- v0.5.0 does not claim v1.0.0 stability.
- v0.5.0 produces enough validation evidence to inform v1.0.0.
- v1.0.0 freeze happens only after behavior has stabilized.

---

### P2-06 — General Multi-Skill Expansion

#### Purpose

Future versions may expand beyond a single `task-contract` Skill into a multi-skill control layer.

#### Boundary

Do not include this in v0.5.0. Multi-skill expansion should wait until:

1. `task-contract` behavior is stable;
2. subagent boundaries are tested;
3. preset model is defined;
4. v1.0.0 compatibility policy is drafted.

---

## 9. Validation Strategy

### 9.1 Local Validation

Run from repository root:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-release-consistency.py
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
python3 scripts/validate-contract-semantics.py
bash scripts/smoke-test-installation.sh
git status
```

### 9.2 CI Validation

CI should run all non-interactive checks:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-release-consistency.py
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
python3 scripts/validate-contract-semantics.py
bash scripts/smoke-test-installation.sh
```

### 9.3 Release Validation

Before tagging v0.5.0:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-release-consistency.py
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
python3 scripts/validate-contract-semantics.py
bash scripts/smoke-test-installation.sh
git status
```

Release is ready only when:

1. all local validation checks pass;
2. CI is green;
3. plugin package sync is clean;
4. release checklist is complete;
5. human review confirms behavior-impacting changes;
6. no unsupported official compliance claim exists.

---

## 10. Implementation Order

Follow this order to minimize drift and reduce rework.

### Phase 1 — Release Target and Plan

1. Replace `IMPLEMENTATION__PLAN.md` with this v0.5.0 plan.
2. Update `config/release.json` to v0.5.0.
3. Update plugin manifest to v0.5.0.
4. Add `docs/v0.5.0-release-checklist.md`.
5. Update README, AGENTS, CHANGELOG, and roadmap release target references.

### Phase 2 — Mode Taxonomy

6. Update schemas to use `base_mode` and `modifiers`.
7. Update expected outputs with base mode and modifiers.
8. Update snapshots with base mode and modifiers.
9. Update validators to understand taxonomy.
10. Update schema documentation and behavior contract.

### Phase 3 — Validators

11. Add `scripts/validate-release-consistency.py`.
12. Add `scripts/validate-contract-semantics.py`.
13. Update `scripts/validate-repo.py`.
14. Update `scripts/validate-schemas.py`.
15. Update `scripts/run-snapshots.py`.
16. Update loop fixture validation where needed.

### Phase 4 — Fixture Coverage

17. Add `skills/task-contract/tests/FIXTURE_MATRIX.md`.
18. Ensure every fixture maps to expected output and snapshot.
19. Add matrix validation to repository validation.

### Phase 5 — Subagent Hardening

20. Strengthen `schemas/subagent-contract.schema.json`.
21. Update `skills/task-contract/SKILL.md`.
22. Update `skills/task-contract/references/subagent-delegation-policy.md`.
23. Update `skills/task-contract/assets/subagent-contract-template.md`.
24. Update subagent fixture, expected output, and snapshot.

### Phase 6 — Installation and CI

25. Add `scripts/smoke-test-installation.sh`.
26. Update installation docs.
27. Update testing docs.
28. Update CI workflow.
29. Update pre-commit hook parity.
30. Run full validation.

### Phase 7 — Final Review

31. Review all docs for unsupported compliance claims.
32. Review all release version references.
33. Review all schemas for draft status.
34. Run final local validation.
35. Confirm CI is green.
36. Tag only after human approval.

---

## 11. Acceptance Criteria

### 11.1 Release-Level Acceptance

- v0.5.0 is the single active release target.
- v0.4.0 appears only as previous baseline, changelog history, roadmap history, or archive context.
- `config/release.json` controls active release target and schema version.
- Plugin manifest version matches config.
- Active release checklist is `docs/v0.5.0-release-checklist.md`.
- Local and CI validation sequences are aligned.
- P2 roadmap items are not release blockers.

### 11.2 Schema-Level Acceptance

- Schemas use `0.5.0-draft`.
- Schemas clearly state draft status.
- Schemas do not claim v1.0.0 stability.
- Mode taxonomy uses `base_mode` and `modifiers`.
- Subagent Contract schema includes path, tool, evidence, merge, and failure boundaries.
- Schema validator reads expected version from `config/release.json`.

### 11.3 Behavior-Level Acceptance

- Auto-Skeleton appears first when the Skill is invoked.
- Optimized Task preserves intent and bounds scope.
- Compact Contract remains low-friction.
- Full Contract includes Decision Points and Approval Gate when appropriate.
- Loop Contract Mode always includes finite iteration caps and stop conditions.
- High-impact loops stop before execution unless approved.
- Subagent Delegation is bounded, non-recursive by default, evidence-driven, and parent-controlled.
- Final response ends with one clear next step.
- The Skill does not imply background work, unlimited loops, or unapproved execution.

### 11.4 Test-Level Acceptance

- Every fixture has an expected output.
- Every fixture has a snapshot.
- Fixture matrix covers all fixtures.
- Repository validator checks required files and key terms.
- Release consistency validator catches stale active version references.
- Semantic validator catches behavior failures.
- Loop regression runner passes.
- Snapshot protocol validator passes.
- Installation smoke test passes.

### 11.5 Documentation-Level Acceptance

- README describes v0.5.0 accurately.
- AGENTS describes v0.5.0 release gates.
- Usage docs include Subagent Delegation examples.
- Installation docs include smoke test.
- Testing docs include all validators.
- Schema docs explain draft status and taxonomy.
- CI docs mirror local validation.
- Roadmap keeps P2 expansion work separate.
- Plugin docs avoid unsupported official compliance claims.

---

## 12. Out of Scope

The following must not be implemented as part of v0.5.0 unless separately approved:

1. official marketplace publishing;
2. official plugin schema compliance claim;
3. v1.0.0 schema freeze;
4. live model-output golden execution as a required release gate;
5. network-dependent validation;
6. autonomous multi-agent runtime;
7. broad multi-skill orchestration;
8. destructive cleanup;
9. large unrelated repository refactors;
10. dependency-heavy validator rewrites.

---

## 13. Final Review Checklist

### Plan Review

- [ ] `IMPLEMENTATION__PLAN.md` targets v0.5.0.
- [ ] v0.4.0 is described only as previous baseline.
- [ ] P0, P1, and P2 are clearly separated.
- [ ] Every P0 item has Problem, Required Changes, Files, and Acceptance Criteria.
- [ ] Every P1 item has Problem, Required Changes, Files, and Acceptance Criteria.
- [ ] P2 items are roadmap-only.
- [ ] Validation commands are complete.
- [ ] No unsupported official compliance claim is made.

### Implementation Review

- [ ] `config/release.json` updated to v0.5.0.
- [ ] Plugin manifest updated to v0.5.0.
- [ ] Active docs updated to v0.5.0.
- [ ] v0.5.0 release checklist exists.
- [ ] Mode taxonomy normalized.
- [ ] Release consistency validator added.
- [ ] Semantic contract validator added.
- [ ] Fixture matrix added.
- [ ] Subagent schema hardened.
- [ ] Installation smoke test added.
- [ ] CI updated.
- [ ] Pre-commit parity reviewed.

### Validation Review

- [ ] Plugin package sync passes.
- [ ] Repository validation passes.
- [ ] Loop fixture validation passes.
- [ ] Release consistency validation passes.
- [ ] Schema validation passes.
- [ ] Documentation validation passes.
- [ ] Snapshot validation passes.
- [ ] Loop regression tests pass.
- [ ] Semantic contract validation passes.
- [ ] Installation smoke test passes.
- [ ] `git status` is clean after sync or expected changes are committed.

### Human Review

- [ ] Maintainer reviewed behavior-impacting changes.
- [ ] Maintainer reviewed release metadata.
- [ ] Maintainer reviewed schema changes.
- [ ] Maintainer reviewed subagent safety boundaries.
- [ ] Maintainer confirmed P2 items are not release blockers.
- [ ] Maintainer approved tagging only after CI is green.

---

## 14. Tagging Plan

Tag only after all required checks pass and human review is complete.

```bash
git tag v0.5.0
git push origin main --tags
```

GitHub Release title:

```text
v0.5.0 — Behavior Validation, Mode Taxonomy, and Subagent Boundary Hardening
```

Suggested release note summary:

```md
v0.5.0 strengthens codex-task-contract-skill by normalizing contract mode taxonomy, adding semantic contract validation, improving release consistency checks, introducing fixture coverage mapping, hardening subagent delegation boundaries, adding installation smoke testing, and aligning local/CI validation for safer Codex repository workflows.
```

---

## 15. Next Step

Review and approve the first implementation phase: release target, central config, plugin manifest, release checklist, and active documentation updates.
