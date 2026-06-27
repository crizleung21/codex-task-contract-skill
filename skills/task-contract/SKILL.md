---
name: task-contract
description: Clarify vague, multi-step, high-impact, or iterative requests before execution by producing a compact, full, or loop task contract with an Auto-Skeleton, optimized task, constraints, output contract, acceptance criteria, decision points, observation methods, repair rules, stop conditions, and approval gates when needed.
---

# task-contract

Use this skill to clarify, bound, and contract a user request before execution.

## Operating Principle

Clarify before action. Convert the user request into a visible task contract that preserves intent, bounds scope, defines output, and states completion criteria.

Do not expose hidden reasoning. Provide concise rationale, assumptions, constraints, decision criteria, evidence references when used, and actionable next steps.

## When to Use

Use this skill when the user asks Codex to:

- clarify, optimize, or rewrite a task;
- inspect or modify a repository;
- create, edit, or restructure files;
- draft implementation plans, specs, tests, or docs;
- handle a multi-step or ambiguous request;
- make a decision from incomplete context;
- iterate, debug, repair, validate, or continue toward a goal.

## When Not to Use

Do not use this skill when:

- the request is a simple factual question;
- the task is already tightly specified and low impact;
- the user explicitly says not to use task framing;
- a task contract would add friction without improving execution.

## Mode Selection

Choose exactly one mode.

| Mode | Select When | Required Output |
|---|---|---|
| Compact Contract | The task is simple, low impact, and only slightly underspecified. | Auto-Skeleton, Optimized Task, Output Contract, Next Step. |
| Full Contract | The task is multi-step, ambiguous, repo-level, public-facing, or high impact. | Auto-Skeleton, BLUF, Optimized Task, Assumptions, Constraints, Decision Points, Output Contract, Execution Plan, Acceptance Criteria, Approval Gate, Next Step. |
| Loop Contract | The task requires iterative progress through observation, adjustment, validation, and stop conditions. | Full Contract plus Loop Contract, Loop Procedure, Loop Log, Validation Method, Stop Conditions. |

Escalate from Compact to Full when a choice may change the outcome. Escalate from Full to Loop when progress depends on observing results across multiple cycles.

## Auto-Skeleton

Always show the Auto-Skeleton first when the skill is invoked.

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

Rules:

1. Infer obvious fields.
2. Mark unclear fields as `Need choice`.
3. Do not invent facts.
4. Preserve the user's intent.
5. Keep compact output concise.
6. Expand only when complexity justifies it.

## Task Optimizer

The Optimized Task must:

1. Start with a clear action verb.
2. Identify the object of work.
3. Define the target outcome.
4. Bound the scope.
5. Specify decision-use.
6. Specify output shape.
7. Include acceptance criteria.
8. Preserve user intent.
9. Avoid scope creep.
10. Surface ambiguity as Decision Points when resolving it would change the task.

Template:

```text
[Action] [object] to [outcome], using [context and constraints], so that [decision-use]. Output [format and depth], and consider the task complete when [acceptance criteria].
```

## Output Contracts

For non-trivial tasks, include:

| Deliverable | Format | Depth / Length | Acceptance Criteria |
|---|---|---|---|
| ... | ... | ... | ... |

## Decision Points

Use Decision Points when multiple valid interpretations exist or a choice changes direction.

Decision Points must:

- use numbered options;
- state trade-offs;
- recommend a default when justified;
- include a reply template when user choice is needed.

## Approval Gate

Low-impact work may proceed after the contract is produced. High-impact work must pause for approval before execution.

Use an Approval Gate for broad repo changes, release actions, dependency changes, public interface changes, destructive cleanup, large refactors, or any loop that needs to expand scope.

## Loop Contract Mode

Use Loop Contract Mode when one response is insufficient and the task benefits from bounded cycles of action, observation, adjustment, and validation.

A Loop Contract must include:

| Field | Meaning |
|---|---|
| Loop Objective | The final outcome the loop is trying to achieve. |
| Loop Type | Simple, coding/debug, research, documentation, repo maintenance, or high-impact. |
| Iteration Unit | The smallest useful action per cycle. |
| Observation Method | What will be checked after each cycle. |
| Adjustment Strategy | How the next step changes based on the observation. |
| Validation Method | How completion is verified. |
| Stop Condition | What ends the loop successfully or safely. |
| Max Iterations | Maximum number of cycles. |
| Escalation Trigger | When Codex must stop and ask the user. |
| Approval Gate | Whether execution may proceed. |

Default iteration limits:

| Loop Type | Default Max Iterations |
|---|---:|
| Simple loop | 3 |
| Coding/debug loop | 5 |
| Research loop | 3 |
| Documentation loop | 3 |
| Repo maintenance loop | 3 |
| High-impact loop | 1 before approval |

Loop rules:

1. Do not run open-ended loops.
2. Use small, reversible iteration units.
3. Re-check the Optimized Task and Acceptance Criteria each cycle.
4. Observe using tests, build output, lint output, diff review, source review, citations, logs, or checklist evidence as applicable.
5. Adjust only for the observed gap.
6. Maintain a concise Loop Log.
7. Stop when acceptance criteria pass, the iteration cap is reached, required context is missing, the same failure repeats, scope drift appears, or approval is required.

## Loop Log

Use this structure when executing Loop Contract Mode:

| Iteration | Action | Observation | Adjustment | Status |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |

## Final Response Rules

End with one clear next step. Be honest about what was completed, what was not completed, and what still needs user review.

## Quality Checklist

Before acting, verify:

- [ ] Intent is preserved.
- [ ] Scope is bounded.
- [ ] Output Contract is clear.
- [ ] Acceptance criteria are explicit.
- [ ] Decision Points are present when needed.
- [ ] Approval Gate is applied when needed.
- [ ] Loop contracts have observation, validation, stop conditions, and iteration caps.
- [ ] No hidden reasoning is exposed.
