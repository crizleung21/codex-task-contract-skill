# Loop Contract Policy

Loop Contract Mode is the v0.2.0 extension for bounded iterative work.

## Purpose

Convert a single prompt into a controlled loop:

```text
single prompt -> goal -> iteration plan -> observation -> repair -> validation -> stop
```

## Required Fields

| Field | Meaning |
|---|---|
| Loop Objective | The final outcome to achieve. |
| Loop Type | Coding, debug, research, documentation, review, repair, or repo maintenance. |
| Iteration Unit | The smallest useful action per cycle. |
| Observation Method | What Codex checks after each action. |
| Repair Strategy | How Codex responds to observed failure. |
| Validation Method | How Codex verifies completion. |
| Stop Condition | When the loop ends. |
| Max Iterations | Maximum allowed cycles. |
| Escalation Trigger | When Codex must ask the user. |
| Risk Gate | Whether work may proceed. |

## Default Iteration Limits

| Loop Type | Default Max Iterations |
|---|---:|
| Simple loop | 3 |
| Coding/debug loop | 5 |
| Research loop | 3 |
| Documentation loop | 3 |
| Repo maintenance loop | 3 |
| High-risk loop | 1 before confirmation |

## Stop Conditions

Stop when acceptance criteria are met, the iteration cap is reached, repeated failure appears, required context is missing, scope drift appears, or validation is not possible.

## Loop Log

Maintain a concise Loop Log with iteration, action, observation, repair, and status.
