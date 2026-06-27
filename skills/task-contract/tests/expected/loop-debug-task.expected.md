# Expected: Loop Debug Task

Mode: Loop Contract Mode

## Required Sections

1. Auto-Skeleton
2. BLUF
3. Optimized Task
4. Output Contract
5. Loop Contract
6. Loop Procedure
7. Loop Log
8. Validation Method
9. Stop Conditions
10. Escalation Triggers
11. Approval Gate, if high-impact execution is required
12. Next Step

## Required Checks

- Loop Objective is measurable.
- Loop Type is Coding/debug loop.
- Iteration Unit is one bounded debug or validation action.
- Observation Method includes tests, build output, lint output, logs, diff review, or equivalent validation evidence.
- Adjustment Strategy responds only to the observed gap.
- Validation Method is concrete.
- Max Iterations defaults to 5 unless lowered by scope or approval limits.
- Stop Conditions include validation pass, iteration cap, repeated failure, missing context, validation blocked, or approval requirement.
- Escalation Triggers include repeated failure or validation blocked.
- Loop Log includes Iteration, Action, Observation, Adjustment, Validation, and Status.
- No hidden reasoning is exposed.
