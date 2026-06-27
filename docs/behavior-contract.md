# Behavior Contract

This document defines the stable behavior expected from the `task-contract` Skill.

## Primary Principle

Clarify before action.

The Skill must preserve user intent, bound scope, define output, state acceptance criteria, surface meaningful choices, and pause for approval before high-impact work.

## Modes

| Mode | Use When | Required Sections |
|---|---|---|
| Compact Contract | Simple, low-impact, slightly underspecified task. | Auto-Skeleton, Optimized Task, Output Contract, Next Step. |
| Full Contract | Complex, ambiguous, repo-level, public-facing, or high-impact task. | Auto-Skeleton, BLUF, Optimized Task, Assumptions, Constraints, Decision Points, Output Contract, Execution Plan, Acceptance Criteria, Approval Gate, Next Step. |
| Loop Contract Mode | Iterative task needing observation, adjustment, validation, and safe stopping. | Full Contract plus Loop Contract, Loop Procedure, Loop Log, Validation Method, Stop Conditions, Escalation Triggers, Approval Gate, Next Step. |

## Auto-Skeleton

| Field | Purpose |
|---|---|
| Role | Role Codex should adopt. |
| Raw Task | User request summarized without distortion. |
| Optimized Task | Precise, bounded, outcome-first rewrite. |
| Object | Target repository, file, document, feature, question, or workflow. |
| Context | Relevant background and implied state. |
| Constraints | Requirements, exclusions, risks, and boundaries. |
| Output | Expected deliverable shape. |
| Acceptance | How completion will be judged. |

## Loop Contract Mode

Every Loop Contract must include Loop Objective, Loop Type, Iteration Unit, Observation Method, Adjustment Strategy, Validation Method, Stop Conditions, Max Iterations, Escalation Triggers, Approval Gate, and Loop Log.

## Done Criteria

A contract is complete when the user can clearly see the intended work, excluded scope, expected output, success criteria, approval status, and next step.
