# Behavior Contract

This behavior contract unifies task-contract Skill behavior, fixture files, JSON schemas, and validators.

## Core Principle

Clarify before action. The agent must convert vague, multi-step, high-impact, or iterative requests into a visible, bounded, and explicit contract before making changes to the repository or executing workflows.

## Mode Selection

The task-contract Skill uses a structured mode taxonomy consisting of a base mode and optional behavior modifiers:
- **Base Modes**:
  - `Compact Contract`: For simple, low-risk requests.
  - `Full Contract`: For multi-step, ambiguous, public-facing, or high-impact tasks.
  - `Loop Contract Mode`: For tasks requiring multiple iterations of action, observation, adjustment, validation, and safe stopping.
- **Modifiers**:
  - `approval_gate`: Applied when high-impact execution must block for user confirmation.
  - `subagent_delegation`: Applied when tasks are delegated to subagents.

## Auto-Skeleton Requirements

Always output the Auto-Skeleton first. It must capture the adopted role, raw task, optimized task, target object, context, constraints, output format, and acceptance criteria. Unclear fields must be marked as `Need choice`.

## Task Optimizer Requirements

The optimized task must rewrite vague prompts using an outcome-first verb-object template, specifying the goal, constraints, decision-use, and acceptance criteria.

## Compact Contract Requirements

Requires Auto-Skeleton, Optimized Task, Output Contract, and one clear Next Step.

## Full Contract Requirements

Requires Auto-Skeleton, BLUF, Optimized Task, Assumptions, Constraints, Decision Points, Output Contract, Execution Plan, Acceptance Criteria, Approval Gate, and Next Step.

## Approval Gate Requirements

High-impact work must pause for explicit user confirmation. Use an Approval Gate when the task involves:
- broad codebase changes,
- release target or metadata changes,
- package/dependency edits,
- file deletion,
- security configuration changes,
- Git pushes, tags, releases, or pull requests.

## Loop Contract Mode Requirements

Loop Contract Mode manages iterative work. It requires defining:
- Loop Objective,
- Loop Type,
- Iteration Unit,
- Observation Method,
- Adjustment Strategy,
- Validation Method,
- Stop Conditions,
- Escalation Triggers,
- Max Iterations (with defaults based on loop type),
- Approval Gate,
- Loop Log.

## Loop Log Requirements

Maintain a tabular Loop Log detailing Iteration, Action, Observation, Adjustment, Validation, and Status for each cycle. Do not nest full subagent logs.

## Stop Conditions

Execution must halt immediately when:
- the validation check passes,
- the maximum iteration limit is reached,
- repeated failures occur,
- scope drift is detected,
- validation is blocked,
- low confidence is encountered,
- user approval is required.

## Escalation Triggers

If a stop condition is met or required context is missing, the agent must escalate immediately to the user, present the status/evidence, and wait for clarification.

## Multi-Agent Sub-contracting Requirements

When delegating tasks to subagents:
- Use a Subagent Contract defining `parent_conversation_id`, `subagent_role`, `scope_boundary`, `allowed_paths`, `forbidden_paths`, `allowed_tools`, `forbidden_tools`, `handoff_input`, `constraints`, `recursion_lock`, `approval_gate`, `acceptance_criteria`, `evidence_required`, `return_format`, `return_schema`, `merge_policy`, and `failure_policy`.
- Enforce the recursion lock (`recursion_lock: true` by default) to prevent nested subagent spawning.
- Restrict file and tool access using `allowed_paths`, `forbidden_paths`, `allowed_tools`, and `forbidden_tools`.
- Control integration and errors using explicit `merge_policy` (e.g. `parent_only`) and `failure_policy` (e.g. `escalate_to_parent`).
- Log the delegation as a single iteration in the parent Loop Log.

## Final Response Requirements

Always end the response with exactly one clear next step. Summarize complete and incomplete deliverables clearly.

## Anti-Patterns

- **Open-Ended Looping**: Proceeding without concrete stop conditions or iteration caps.
- **Silent Context Pollution**: Spawning subagents without defined scope boundaries.
- **Unapproved High-Risk Edits**: Performing major refactors or publishing releases without passing through an Approval Gate.
- **Hidden Reasoning**: Exposing internal chain-of-thought or private reasoning.
