# Usage

## Explicit Invocation

```text
Use $task-contract to clarify this task first.
```

## Mode Selection

| Mode | Use When | Output |
|---|---|---|
| Compact Contract | The task is simple and low impact. | Auto-Skeleton, Optimized Task, Output Contract, Next Step. |
| Full Contract | The task is complex, ambiguous, repo-level, or high impact. | Auto-Skeleton, BLUF, Optimized Task, Assumptions, Constraints, Decision Points, Output Contract, Execution Plan, Acceptance Criteria, Approval Gate, Next Step. |
| Loop-aware Contract | The task needs bounded iteration. | Full Contract plus Loop Contract fields, Loop Log, validation method, stop conditions, and iteration cap. |

## Compact Contract Example Prompt

```text
Rewrite this README introduction so it is clearer and more professional.
```

Expected mode: Compact Contract.

## Full Contract Example Prompt

```text
Review this repository and prepare it for public release.
```

Expected mode: Full Contract with Decision Points and Approval Gate before high-impact work.

## Loop-Aware Example Prompt

```text
Run the checks, adjust the failing area, and repeat within a bounded loop until validation passes or the loop stops.
```

Expected mode: Loop-aware Contract.

## Approval Gate

Use an Approval Gate before high-impact execution, including broad repository changes, release actions, dependency changes, destructive cleanup, or any loop that expands beyond the Optimized Task.

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
- ends with one clear next step.
