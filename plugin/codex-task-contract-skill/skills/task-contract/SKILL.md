---
name: task-contract
description: Clarify vague, multi-step, high-impact, or iterative requests before execution by producing a compact, full, or loop task contract with an Auto-Skeleton, optimized task, constraints, output contract, acceptance criteria, decision points, observation methods, adjustment rules, stop conditions, and approval gates when needed.
---

# task-contract

This packaged Skill mirrors the canonical source under `skills/task-contract/SKILL.md`.

Use this skill to clarify, bound, and contract a user request before execution.

## Output Modes

| Mode | Use For |
|---|---|
| Compact Contract | Simple low-impact tasks. |
| Full Contract | Complex, ambiguous, repo-level, or high-impact tasks. |
| Loop Contract | Iterative tasks requiring observation, adjustment, validation, and stop conditions. |

## Required Behavior

- Start with Auto-Skeleton.
- Preserve user intent.
- Bound scope.
- Define output and acceptance criteria.
- Use Decision Points when choices matter.
- Use Approval Gate before high-impact execution.
- Use Loop Contract Mode only with observation, validation, stop condition, and iteration cap.
- Do not expose hidden reasoning.
