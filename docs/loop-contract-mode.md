# Loop Contract Mode

Loop Contract Mode is the stable v0.2.0 feature for bounded iterative work.

## What It Is

Loop Contract Mode is a task-control protocol. It helps Codex structure iterative work into visible cycles with objective, iteration unit, observation, adjustment, validation, stop conditions, escalation triggers, and approval gates.

State model:

```text
Goal -> Contract -> Plan Iteration -> Act -> Observe -> Adjust -> Validate -> Stop/Escalate
```

## What It Is Not

Loop Contract Mode is not:

- a background worker;
- a scheduler;
- a CI orchestrator;
- an unbounded autonomous runtime;
- permission to keep working indefinitely.

## When to Use It

Use Loop Contract Mode for:

- debugging loops;
- research loops;
- documentation consistency loops;
- repository maintenance loops;
- repeated refinement with observable checks.

## When Not to Use It

Do not use Loop Contract Mode for:

- simple one-step tasks;
- tasks with no observable result;
- tasks with no validation method;
- requests requiring background work after the current session.

## Required Fields

Every Loop Contract must include Loop Objective, Loop Type, Iteration Unit, Observation Method, Adjustment Strategy, Validation Method, Stop Conditions, Max Iterations, Escalation Triggers, Approval Gate, and Loop Log.

## Loop Types

| Loop Type | Default Max Iterations |
|---|---:|
| Simple loop | 3 |
| Coding/debug loop | 5 |
| Research loop | 3 |
| Documentation loop | 3 |
| Repo maintenance loop | 3 |
| High-impact loop | 1 before approval |

## Approval Gate

High-impact loops may inspect and contract the work, but must pause before execution unless the user approves a bounded scope.

## Manual Review Checklist

- [ ] Objective is measurable.
- [ ] Iteration unit is bounded.
- [ ] Observation method is concrete.
- [ ] Validation method is concrete.
- [ ] Stop conditions are complete.
- [ ] Max iterations are appropriate.
- [ ] Escalation triggers are present.
- [ ] Approval Gate is correct.
- [ ] Loop Log is present.
- [ ] No hidden reasoning is exposed.
