---
name: task-contract
description: Clarify vague, multi-step, high-impact, or iterative requests before execution by producing compact, full, or stable loop task contracts with Auto-Skeleton, optimized task, output contract, acceptance criteria, decision points, observation methods, validation rules, stop conditions, escalation triggers, and approval gates when needed.
---

# task-contract

Use this skill to clarify, bound, and contract a user request before execution.

## Operating Principle

Clarify before action. Convert the user request into a visible task contract that preserves intent, bounds scope, defines output, and states completion criteria.

Provide concise rationale, assumptions, constraints, decision criteria, evidence references when used, and actionable next steps. Do not reveal private reasoning. Do not imply background work, scheduling, unlimited iteration, or open-ended execution.

## When to Use

Use this skill when the user asks Codex to:

- clarify, optimize, or rewrite a task;
- inspect or modify a repository;
- create, edit, or restructure files;
- draft implementation plans, specs, tests, or docs;
- handle a multi-step or ambiguous request;
- make a decision from incomplete context;
- iterate, debug, repair, validate, or continue toward a bounded goal;
- perform work that may need approval before execution.

## When Not to Use

Do not use this skill when:

- the request is a simple factual question;
- the task is already tightly specified and low impact;
- the user explicitly says not to use task framing;
- a task contract would add friction without improving execution.

## Mode Selection

Choose exactly one mode unless the user explicitly asks for a comparison.

| Mode | Select When | Required Output |
|---|---|---|
| Compact Contract | The task is simple, low impact, and only slightly underspecified. | Auto-Skeleton, Optimized Task, Output Contract, Next Step. |
| Full Contract | The task is multi-step, ambiguous, repo-level, public-facing, or high impact. | Auto-Skeleton, BLUF, Optimized Task, Assumptions, Constraints, Decision Points, Output Contract, Execution Plan, Acceptance Criteria, Approval Gate, Next Step. |
| Loop Contract Mode | The task requires bounded iteration through action, observation, adjustment, validation, and safe stopping. | Full Contract plus Loop Contract, Loop Procedure, Loop Log, Validation Method, Stop Conditions, Escalation Triggers, Approval Gate, Next Step. |

Escalate from Compact to Full when a choice may change the outcome. Escalate from Full to Loop Contract Mode when progress depends on observing results across multiple cycles.

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

Use an Approval Gate before execution when the task may involve broad repository changes, public behavior changes, release metadata changes, dependency changes, file deletion, security posture changes, large refactors, commits, pushes, tags, releases, pull requests, loop scope expansion, or high-impact loop execution.

Approval Gate wording:

```md
## Approval Gate

This action requires approval before execution because [reason].

Blocked action: [specific action]
Recommended safe default: [inspection-only / contract-only / limited edit scope]
Reply template: Approved: [bounded scope]
```

## Loop Contract Mode

Loop Contract Mode is a stable bounded task-control protocol for iterative work.

Use it when a task requires cycles of action, observation, adjustment, validation, and safe stopping.

Loop Contract Mode is not a background worker, scheduler, CI orchestrator, autonomous runtime, or permission to continue indefinitely.

State model:

```text
Goal -> Contract -> Plan Iteration -> Act -> Observe -> Adjust -> Validate -> Stop/Escalate
```

A Loop Contract must include:

| Field | Meaning |
|---|---|
| Loop Objective | The measurable final outcome. |
| Loop Type | Simple, coding/debug, research, documentation, repo maintenance, or high-impact. |
| Iteration Unit | The smallest useful action per cycle. |
| Observation Method | Evidence checked after each cycle. |
| Adjustment Strategy | How the next step changes based on the observation. |
| Validation Method | How completion is verified. |
| Stop Conditions | Success, safety, and failure stop rules. |
| Max Iterations | Maximum number of cycles. |
| Escalation Triggers | Conditions requiring user input. |
| Approval Gate | Whether execution may proceed. |
| Loop Log | Concise user-visible evidence of iterations. |

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
4. Observe using concrete evidence such as tests, build output, lint output, diff review, source review, citations, logs, or checklist evidence.
5. Adjust only for the observed gap.
6. Maintain a concise Loop Log.
7. Stop when acceptance criteria pass, the iteration cap is reached, required context is missing, the same failure repeats, scope drift appears, validation is blocked, low confidence appears, or approval is required.

## Loop Log

Use this structure when executing Loop Contract Mode:

| Iteration | Action | Observation | Adjustment | Validation | Status |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |

## Loop Stop Summary

When a loop stops, include:

- Final status:
- Stop reason:
- Evidence:
- Remaining gaps:
- Next step:

## Multi-Agent Sub-contracting

Delegate tasks to specialized subagents to divide complexity and isolate context.

### 1. When Delegation is Allowed
- The task involves independent sub-components (such as isolated research, targeted debugging, or documentation audits) that can be worked on without shared state or sequential dependencies.
- Delegating the task avoids context pollution in the parent conversation.

### 2. When Delegation is Not Allowed
- The task is tightly coupled to the main execution flow or requires global codebase updates.
- The parent agent has not yet established a task contract or secured necessary user approvals.

### 3. Required Subagent Contract Fields
Every subagent contract must define:
- `parent_conversation_id`: The identifier of the spawning conversation.
- `subagent_role`: The specialized function of the subagent.
- `scope_boundary`: Strict list of allowed paths and tools.
- `constraints`: Specific runtime limitations.
- `recursion_lock`: True/False setting for child spawning.
- `approval_gate`: Required status, reason, blocked action, safe default, and reply template.
- `acceptance_criteria`: Machine-verifiable definitions of completion.
- `return_format`: Structured format for the subagent's report.

### 4. Scope Boundary
Subagents must be bounded to a narrow subset of files or directories (e.g., `docs/` or `scratch/`). They must not run commands or access paths outside their defined boundary.

### 5. Recursion Lock
To prevent unbounded nested agent loops, set the recursion lock to `true`. Subagents are forbidden from spawning subagents recursively unless explicitly approved by the user.

### 6. Approval Gate Behavior
If the subagent task involves high-risk actions (e.g., editing critical files or running untrusted commands), the subagent must trigger an Approval Gate and pause for user input before executing the actions.

### 7. Return Format and Evidence Requirements
Subagents must return a structured report matching the requested return format. The report must contain concrete, visible evidence verifying that every acceptance criterion has been fully satisfied.

### 8. Parent Loop Log Syncing
When using Loop Contract Mode, log the delegation as a single iteration:
- **Action**: `Spawn subagent [role] for [task]`
- **Observation**: `Subagent completed with status [status] and evidence [evidence summary]`
Do not nest full subagent execution logs inside the parent Loop Log. Save them in independent files or nested sub-sections.

## References

Use deeper reference files when needed:

- `references/loop-contract-policy.md`
- `references/loop-observation-methods.md`
- `references/loop-stop-conditions.md`
- `references/loop-escalation-rules.md`
- `references/loop-evaluation-rubric.md`
- `references/subagent-delegation-policy.md`

Use templates when helpful:

- `assets/compact-contract-template.md`
- `assets/full-contract-template.md`
- `assets/loop-contract-template.md`
- `assets/compact-loop-contract-template.md`
- `assets/full-loop-contract-template.md`
- `assets/subagent-contract-template.md`

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
- [ ] Loop contracts have objective, observation, adjustment, validation, stop conditions, escalation triggers, and iteration caps.
- [ ] Subagent contracts define scope boundaries, constraints, recursion lock, and approval gates.
- [ ] Loop Log is present when Loop Contract Mode is used.
- [ ] Private reasoning is not revealed.
- [ ] Background or open-ended execution is not implied.
