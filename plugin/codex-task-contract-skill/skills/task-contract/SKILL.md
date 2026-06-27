---
name: task-contract
description: Clarify vague, multi-step, high-impact, or iterative requests before execution by producing compact, full, or stable loop task contracts with Auto-Skeleton, optimized task, output contract, acceptance criteria, decision points, observation methods, validation rules, stop conditions, escalation triggers, and approval gates when needed.
---

# task-contract

This packaged Skill mirrors the canonical source under `skills/task-contract/SKILL.md`.

Use this skill to clarify, bound, and contract a user request before execution.

## Operating Principle

Clarify before action. Convert the user request into a visible task contract that preserves intent, bounds scope, defines output, and states completion criteria.

Provide concise rationale, assumptions, constraints, decision criteria, evidence references when used, and actionable next steps. Do not reveal private reasoning. Do not imply background work, scheduling, unlimited iteration, or open-ended execution.

## Mode Selection

Choose exactly one mode unless the user explicitly asks for a comparison.

| Mode | Select When | Required Output |
|---|---|---|
| Compact Contract | The task is simple, low impact, and only slightly underspecified. | Auto-Skeleton, Optimized Task, Output Contract, Next Step. |
| Full Contract | The task is multi-step, ambiguous, repo-level, public-facing, or high impact. | Auto-Skeleton, BLUF, Optimized Task, Assumptions, Constraints, Decision Points, Output Contract, Execution Plan, Acceptance Criteria, Approval Gate, Next Step. |
| Loop Contract Mode | The task requires bounded iteration through action, observation, adjustment, validation, and safe stopping. | Full Contract plus Loop Contract, Loop Procedure, Loop Log, Validation Method, Stop Conditions, Escalation Triggers, Approval Gate, Next Step. |

## Auto-Skeleton

| Field | Content |
|---|---|
| Role | Role Codex should adopt. |
| Raw Task | User request summarized without distortion. |
| Optimized Task | Precise, bounded, outcome-first rewrite. |
| Object | Repository, file, codebase, document, feature, question, or workflow target. |
| Context | Relevant background and implied state. |
| Constraints | Requirements, exclusions, risks, and boundaries. |
| Output | Expected deliverable shape. |
| Acceptance | How completion will be judged. |

## Approval Gate

Use an Approval Gate before high-impact execution.

## Loop Contract Mode

Loop Contract Mode is a stable bounded task-control protocol for iterative work.

A Loop Contract must include Loop Objective, Loop Type, Iteration Unit, Observation Method, Adjustment Strategy, Validation Method, Stop Conditions, Max Iterations, Escalation Triggers, Approval Gate, and Loop Log.

## Loop Log

| Iteration | Action | Observation | Adjustment | Validation | Status |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |

## Final Response Rules

End with one clear next step.
