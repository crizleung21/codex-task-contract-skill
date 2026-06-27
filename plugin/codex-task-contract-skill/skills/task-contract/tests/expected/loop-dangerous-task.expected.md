# Expected: Loop High-Impact Task

Mode: Loop Contract Mode with Approval Gate

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
11. Approval Gate
12. Next Step

## Required Checks

- Loop Objective is bounded.
- Loop Type is High-impact loop.
- Iteration Unit is inspection only unless approved.
- Observation Method includes impact analysis, changed-area review, or decision point discovery.
- Adjustment Strategy must not execute high-impact changes without approval.
- Validation Method is limited to review evidence until approval is granted.
- Max Iterations is 1 before approval.
- Stop Conditions include approval required, scope drift, release/public behavior change, or iteration cap.
- Escalation Triggers include destructive, release, dependency, security, or broad refactor changes.
- Approval Gate appears before execution.
- Loop Log includes Iteration, Action, Observation, Adjustment, Validation, and Status.
- No hidden reasoning is exposed.
