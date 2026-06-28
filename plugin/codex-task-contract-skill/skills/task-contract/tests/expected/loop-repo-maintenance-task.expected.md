# Expected: Loop Repo Maintenance Task

Mode: Loop Contract Mode
Base Mode: Loop Contract Mode
Modifiers: []

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
11. Approval Gate, if release metadata changes are required
12. Next Step

## Required Checks

- Loop Objective defines v0.2.0 release readiness.
- Loop Type is Repo maintenance loop.
- Iteration Unit is one bounded repository area review, such as Skill source, references, templates, fixtures, docs, scripts, or release metadata.
- Observation Method includes file map, validation script output, checklist review, or diff review.
- Adjustment Strategy targets only the observed release-readiness gap.
- Validation Method references the v0.2.0 release checklist and validator output.
- Max Iterations defaults to 3 unless approval changes scope.
- Stop Conditions include checklist pass, iteration cap, repeated failure, validation blocked, missing context, or approval required.
- Escalation Triggers include release metadata change, package version conflict, broad restructuring, or validation blocked.
- Loop Log includes Iteration, Action, Observation, Adjustment, Validation, and Status.
- No hidden reasoning is exposed.
