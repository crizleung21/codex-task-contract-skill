# IMPLEMENTATION__PLAN.md

Status: Executable starter implementation plan for v0.1.0 with planned v0.2.0 Loop Contract Mode extension  
Project: `codex-task-contract-skill`  
Primary Skill Name: `task-contract`  
Primary Plugin Name: `codex-task-contract-skill`  
Language Policy: English-only documentation and skill instructions  

---

## 1. Executive Summary

`codex-task-contract-skill` is an open-source Codex Skill and installable Plugin package that helps Codex clarify, bound, and contract a user request before execution.

The project packages a reusable workflow named `task-contract`. The workflow produces:

1. Auto-Skeleton
2. Optimized Task
3. Assumptions
4. Constraints
5. Output Contract
6. Decision Points
7. Risk Gate
8. Next Step

Starting in v0.2.0, the project adds Loop Contract Mode. This mode upgrades a single prompt into a bounded agent loop contract with objective, iteration unit, observation method, repair strategy, validation method, stop condition, max iterations, escalation trigger, and risk gate.

---

## 2. Confirmed Decisions

| Area | Decision |
|---|---|
| Skill name | `task-contract` |
| Language | English-only |
| Output modes | Compact, Full, Loop |
| Execution policy | Risk-based confirmation |
| Distribution | Skill + Plugin package |
| Repository | Independent from `creator-toolchain` |
| Loop feature | v0.2.0 core feature |
| Loop caps | Task-type based |
| Loop execution | Low-risk may execute, high-risk requires confirmation |

---

## 3. Repository Architecture

```text
codex-task-contract-skill/
├── README.md
├── IMPLEMENTATION__PLAN.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── .gitignore
├── .editorconfig
├── skills/task-contract/
│   ├── SKILL.md
│   ├── references/
│   ├── assets/
│   └── tests/
├── plugin/codex-task-contract-skill/
│   ├── .codex-plugin/plugin.json
│   └── skills/task-contract/
├── .agents/plugins/marketplace.json
├── docs/
└── scripts/
```

---

## 4. v0.1.0 Scope

v0.1.0 ships the instruction-only Task Contract Skill and installable Plugin package.

Required capabilities:

- Auto-Skeleton
- Task Optimizer
- Compact Contract
- Full Contract
- Output Contract
- Decision Points
- Risk Gate
- Manual fixtures
- Documentation
- Plugin packaging

---

## 5. v0.2.0 Scope: Loop Contract Mode

Loop Contract Mode converts:

```text
single prompt → goal → iteration plan → observation → repair → validation → stop
```

Required Loop Contract fields:

| Field | Required |
|---|---:|
| Loop Objective | Yes |
| Loop Type | Yes |
| Iteration Unit | Yes |
| Observation Method | Yes |
| Repair Strategy | Yes |
| Validation Method | Yes |
| Stop Condition | Yes |
| Max Iterations | Yes |
| Escalation Trigger | Yes |
| Risk Gate | Yes |

Default iteration limits:

| Loop Type | Max Iterations |
|---|---:|
| Simple loop | 3 |
| Coding/debug loop | 5 |
| Research loop | 3 |
| Documentation loop | 3 |
| Repo maintenance loop | 3 |
| High-risk loop | 1 before confirmation |

---

## 6. Implementation Phases

### P0 — Repository Foundation

Create base repo files, documentation, license, and contribution policy.

### P1 — Canonical Skill Source

Implement `skills/task-contract/SKILL.md`.

### P2 — References and Assets

Add schemas, behavior rules, templates, and examples.

### P3 — Plugin Package

Add `.codex-plugin/plugin.json` and synchronized Skill copy.

### P4 — Documentation

Write installation, usage, design, authoring, testing, packaging, release, roadmap, and loop engineering docs.

### P5 — Fixtures and Evaluation

Add manual fixtures and expected outputs for compact, full, high-risk, and loop contracts.

### P6 — Release v0.1.0

Tag first usable release.

### P7 — Release v0.2.0

Enable Loop Contract Mode as the next core feature.

---

## 7. Definition of Done

v0.1.0 is ready when:

1. `SKILL.md` exists and defines Task Contract behavior.
2. Plugin package exists.
3. Docs exist.
4. Fixtures exist.
5. Scripts exist.
6. Risk Gate is documented.
7. README explains installation and usage.

v0.2.0 is ready when:

1. Loop Contract Mode is in `SKILL.md`.
2. Loop policy reference exists.
3. Loop templates exist.
4. Loop fixtures exist.
5. Stop conditions are mandatory.
6. High-risk loops pause at Risk Gate.

---

## 8. Source Note

This repository was initialized from the detailed `IMPLEMENTATION__PLAN(6).md` prepared for the project. The repo files are organized as executable starter artifacts derived from that plan.
