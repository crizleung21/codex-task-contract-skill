---
name: task-contract
description: Clarify vague, multi-step, risky, high-impact, or iterative requests before execution by producing a compact, full, or loop task contract with an Auto-Skeleton, optimized task, constraints, output contract, acceptance criteria, decision points, observation methods, repair rules, stop conditions, and risk gates when needed.
---

# task-contract

Use this skill to clarify, bound, and contract a user request before execution.

## Purpose

Make Codex clarify before it acts. Convert vague, multi-step, high-impact, or iterative requests into explicit task contracts.

## When to Use

Use this skill when the user asks Codex to:

- clarify, optimize, or rewrite a task;
- modify a repository;
- create or restructure files;
- draft implementation plans or technical specs;
- perform multi-step analysis;
- make decisions with incomplete context;
- iterate, debug, repair, validate, or continue until a goal is complete.

## When Not to Use

Do not use this skill when:

- the request is a simple factual question;
- the request is already tightly specified and low-risk;
- the user explicitly says not to use task framing;
- the skill would add more friction than value.

## Output Modes

| Mode | Use For |
|---|---|
| Compact Contract | Simple or slightly underspecified low-risk tasks. |
| Full Contract | Complex, ambiguous, high-impact, or repository-level tasks. |
| Loop Contract | Iterative tasks requiring goal-seeking, observation, repair, validation, and stop conditions. |

## Auto-Skeleton Rules

Always include these fields when the skill is invoked:

| Field | Content |
|---|---|
| Role | Role Codex should adopt. |
| Raw Task | User request summarized without distortion. |
| Optimized Task | Precise, bounded, outcome-first rewrite. |
| Object | File, repo, codebase, document, feature, question, or other target. |
| Context | Relevant background and implied state. |
| Constraints | Hard requirements, exclusions, risks, or boundaries. |
| Output | Expected deliverable shape. |
| Acceptance | How completion will be judged. |

Infer obvious fields. Mark unclear fields as `Need choice`. Do not invent unavailable facts.

## Task Optimizer Rules

The Optimized Task must start with a clear action verb, identify the object of work, define the outcome, bound the scope, specify the output shape, include acceptance criteria, preserve intent, and avoid scope creep.

## Compact Contract Format

1. Auto-Skeleton
2. Optimized Task
3. Output Contract
4. Next Step

## Full Contract Format

1. Auto-Skeleton
2. BLUF
3. Optimized Task
4. Assumptions
5. Constraints
6. Decision Points
7. Output Contract
8. Execution Plan
9. Acceptance Criteria
10. Risk Gate
11. Next Step

## Loop Contract Format

Use Loop Contract Mode when the task needs bounded iteration.

A Loop Contract must include:

- Loop Objective
- Loop Type
- Iteration Unit
- Observation Method
- Repair Strategy
- Validation Method
- Stop Condition
- Max Iterations
- Escalation Trigger
- Risk Gate

Do not run open-ended loops.

## Loop Iteration Defaults

| Loop Type | Default Max Iterations |
|---|---:|
| Simple loop | 3 |
| Coding/debug loop | 5 |
| Research loop | 3 |
| Documentation loop | 3 |
| Repo maintenance loop | 3 |
| High-risk loop | 1 before confirmation |

## Loop Procedure

1. Re-check the Optimized Task and Acceptance Criteria.
2. Perform one small reversible action.
3. Observe the result using the selected Observation Method.
4. Compare the result against Acceptance Criteria.
5. Repair only the observed failure.
6. Log the iteration concisely.
7. Repeat until the Stop Condition is met.
8. Stop and escalate if risk, repeated failure, missing context, or scope drift appears.

## Decision Point Rules

Use numbered options with trade-offs. Recommend a default when possible. Include a reply template when user choice is required.

## Risk Gate Rules

Low-risk work may proceed after the contract is produced. High-impact work must pause for user approval before execution.

## No Chain-of-Thought Rule

Do not expose private hidden reasoning. Provide concise rationale, assumptions, constraints, decision criteria, evidence references when used, and actionable plans.

## Quality Checklist

- [ ] Intent is preserved.
- [ ] Scope is bounded.
- [ ] Output contract is clear.
- [ ] Acceptance criteria are explicit.
- [ ] Risk Gate is applied when needed.
- [ ] Loop contracts have observation and stop conditions.
- [ ] No private chain-of-thought is exposed.
