# Loop Engineering

Loop Engineering is the practice of designing bounded agent workflows that repeatedly plan, act, observe, adjust, and validate until a goal is complete or a stop condition is reached.

## Prompt Engineering vs Loop Engineering

| Area | Prompt Engineering | Loop Engineering |
|---|---|---|
| Unit | Single prompt | Bounded workflow |
| Feedback | Usually manual | Built into the loop |
| Validation | Often subjective | Defined by contract |
| Stop rule | Often absent | Mandatory |

## Core Loop

```text
Goal -> Plan -> Act -> Observe -> Repair -> Validate/Stop
```

## Loop Contract Mode

`task-contract` uses Loop Contract Mode when a task needs repeated checking, adjustment, and validation.

Required fields:

- Loop Objective
- Loop Type
- Iteration Unit
- Observation Method
- Repair Strategy
- Validation Method
- Stop Condition
- Max Iterations
- Escalation Trigger
- Risk Gate

## Anti-Patterns

- No clear goal.
- No observation method.
- No stop condition.
- Too many unrelated actions per iteration.
- Scope drift.
- Hidden failure.
