# Usage

## Explicit Invocation

```text
Use $task-contract to clarify this task first.
```

## Mode Selection

The task-contract Skill uses a structured mode taxonomy consisting of a base mode and optional behavior modifiers:

| Base Mode | Select When | Output |
|---|---|---|
| Compact Contract | The task is simple and low impact. | Auto-Skeleton, Optimized Task, Output Contract, Next Step. |
| Full Contract | The task is complex, ambiguous, repo-level, or high impact. | Auto-Skeleton, BLUF, Optimized Task, Assumptions, Constraints, Decision Points, Output Contract, Execution Plan, Acceptance Criteria, Approval Gate, Next Step. |
| Loop Contract Mode | The task needs bounded iteration through observation, adjustment, validation, and safe stopping. | Full Contract plus Loop Contract, Loop Log, Validation Method, Stop Conditions, Escalation Triggers, Approval Gate when needed. |

Available modifiers:
- `approval_gate`: Applied when high-impact execution must block for user confirmation.
- `subagent_delegation`: Applied when tasks are delegated to subagents.

## Compact Contract Example Prompt

```text
Rewrite this README introduction so it is clearer and more professional.
```

Expected mode: Compact Contract (no modifiers).

## Full Contract Example Prompt

```text
Review this repository and prepare it for public release.
```

Expected base mode: Full Contract (with `approval_gate` modifier before high-impact work).

## Loop Contract Example Prompt

```text
Run the checks, adjust the failing area, and repeat within a bounded loop until validation passes or the loop stops.
```

Expected base mode: Loop Contract Mode.

Required loop fields:

- Loop Objective
- Loop Type
- Iteration Unit
- Observation Method
- Adjustment Strategy
- Validation Method
- Stop Conditions
- Max Iterations
- Escalation Triggers
- Approval Gate
- Loop Log

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

1. Produce a parent Full Contract.
2. Identify bounded subagent contracts.
3. Define allowed paths and tools per subagent.
4. Set recursion lock to true by default.
5. Require evidence from each subagent.
6. Block broad execution until parent approval.

## Approval Gate

Use an Approval Gate before high-impact execution, including broad repository changes, release actions, dependency changes, destructive cleanup, public behavior changes, or any loop that expands beyond the Optimized Task.

## Good Output Criteria

A good task contract:

- preserves the user's intent;
- defines the work object;
- bounds the scope;
- names assumptions;
- states constraints;
- defines output format;
- defines acceptance criteria;
- adds Decision Points when choices matter;
- uses an Approval Gate when needed;
- uses bounded Loop Contract Mode when iteration is required;
- uses bounded Subagent Contract when delegating;
- ends with one clear next step.
