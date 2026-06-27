# Loop Stop Conditions

Stable Loop Contract Mode must stop safely. A loop may not continue without a defined stop condition.

## Stop Condition Taxonomy

| Category | Stop Condition | Required Response |
|---|---|---|
| Success | Acceptance criteria are met. | Summarize evidence and final state. |
| Cap | Max iterations are reached. | Stop and report remaining gap. |
| Repeated failure | Same failure repeats twice. | Stop and propose strategy change. |
| Missing context | Required input is unavailable. | Ask for the specific missing item. |
| Validation blocked | Result cannot be verified. | State limitation and propose manual check. |
| Scope drift | Work exceeds the contract. | Stop and request approval. |
| High impact | Release, public behavior, security, dependency, destructive, or broad refactor change is needed. | Stop at Approval Gate. |
| Objective invalid | Original loop objective no longer applies. | Stop and explain why the objective changed. |
| Low confidence | Continuing would create misleading output. | Stop and state uncertainty. |

## Required Stop Summary

```md
## Loop Stop Summary

- Final status:
- Stop reason:
- Evidence:
- Remaining gaps:
- Next step:
```

## Rule

When any stop condition is met, do not continue the loop. Summarize the state and provide one next step.
