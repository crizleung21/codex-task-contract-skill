# Loop Contract Policy

Loop Contract Mode is the v0.2.0 extension for bounded iterative work.

## Definition

A Loop Contract converts a single prompt into a controlled workflow:

```text
single prompt -> goal -> bounded cycle -> observation -> adjustment -> validation -> stop
```

The Skill designs the loop contract. It is not a general agent runtime, scheduler, CI system, or background worker.

## Trigger Conditions

Use Loop Contract Mode when the user asks for:

- iterative progress;
- debugging or validation cycles;
- repeated review and adjustment;
- research with evidence gathering and synthesis;
- documentation inspection, update, and consistency checks;
- repository maintenance where completion depends on observable checks.

Do not use Loop Contract Mode for a simple one-step request.

## Required Fields

| Field | Meaning |
|---|---|
| Loop Objective | The final outcome to achieve. |
| Loop Type | Simple, coding/debug, research, documentation, repo maintenance, or high-impact. |
| Iteration Unit | The smallest useful action per cycle. |
| Observation Method | What Codex checks after each action. |
| Adjustment Strategy | How Codex responds to the observation. |
| Validation Method | How Codex verifies completion. |
| Stop Condition | When the loop ends. |
| Max Iterations | Maximum allowed cycles. |
| Escalation Trigger | When Codex must ask the user. |
| Approval Gate | Whether execution may proceed. |

## Default Iteration Limits

| Loop Type | Default Max Iterations | Typical Observation |
|---|---:|---|
| Simple loop | 3 | Checklist or direct output review. |
| Coding/debug loop | 5 | Tests, build output, lint output, or diff review. |
| Research loop | 3 | Source quality, coverage, contradiction check. |
| Documentation loop | 3 | Coverage checklist and internal consistency. |
| Repo maintenance loop | 3 | File map, validation script, checklist, or diff review. |
| High-impact loop | 1 before approval | Inspection only unless approved. |

The max iteration count may be lowered when the task is narrow or high impact. It may be raised only with explicit user approval.

## Loop Procedure

1. Re-check the Optimized Task and Acceptance Criteria.
2. Select one small iteration unit.
3. Take one bounded action.
4. Observe the result using the selected method.
5. Compare the observation with acceptance criteria.
6. Adjust only for the observed gap.
7. Record the cycle in the Loop Log.
8. Stop when the Stop Condition is met or escalation is required.

## Stop Conditions

A loop must stop when:

- acceptance criteria are met;
- the iteration cap is reached;
- the same failure repeats;
- required context is missing;
- validation is not possible;
- the work drifts outside the Optimized Task;
- a high-impact change becomes necessary;
- user approval is required.

## Loop Log Schema

| Iteration | Action | Observation | Adjustment | Status |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |

Log only useful, user-visible evidence. Do not expose hidden reasoning.

## Anti-Patterns

Avoid loops that:

- say `repeat until done` without defining done;
- lack an observation method;
- lack validation;
- combine unrelated actions in one cycle;
- keep expanding scope;
- continue after repeated failure;
- hide uncertainty or failed attempts.
