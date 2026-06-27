# Loop Contract Policy

Loop Contract Mode is the stable v0.2.0 protocol for bounded iterative work.

## Definition

A Loop Contract converts a user request into a controlled workflow:

```text
Goal -> Contract -> Plan Iteration -> Act -> Observe -> Adjust -> Validate -> Stop/Escalate
```

The Skill designs and governs the loop contract. It is not a general autonomous agent runtime, scheduler, background worker, CI system, or permission to continue indefinitely.

## Trigger Conditions

Use Loop Contract Mode when the user asks for:

- iterative progress;
- debugging or validation cycles;
- repeated review and adjustment;
- research with evidence gathering and synthesis;
- documentation inspection, update, and consistency checks;
- repository maintenance where completion depends on observable checks.

## Non-Trigger Conditions

Do not use Loop Contract Mode when:

- the task is a simple one-step request;
- no observation method is available;
- validation cannot be defined;
- the request is broad but not iterative;
- the loop would require background work after the current session.

## Required Fields

| Field | Meaning |
|---|---|
| Loop Objective | The measurable final outcome. |
| Loop Type | Simple, coding/debug, research, documentation, repo maintenance, or high-impact. |
| Iteration Unit | The smallest useful action per cycle. |
| Observation Method | Evidence checked after each cycle. |
| Adjustment Strategy | How Codex responds to observations. |
| Validation Method | How completion is verified. |
| Stop Conditions | Success, safety, and failure stop rules. |
| Max Iterations | Maximum allowed cycles. |
| Escalation Triggers | Conditions requiring user input. |
| Approval Gate | Whether execution may proceed. |
| Loop Log | Concise user-visible record of iterations. |

## Loop Types

| Loop Type | Default Max Iterations | Typical Evidence |
|---|---:|---|
| Simple loop | 3 | Checklist or direct output review. |
| Coding/debug loop | 5 | Tests, lint, build, logs, or diff. |
| Research loop | 3 | Source quality, coverage, contradiction review. |
| Documentation loop | 3 | Coverage checklist and consistency review. |
| Repo maintenance loop | 3 | File map, validation script, checklist, or diff review. |
| High-impact loop | 1 before approval | Inspection only unless approved. |

The max iteration count may be lowered when the task is narrow or high impact. It may be raised only with explicit user approval.

## Loop Procedure

1. Re-check the Optimized Task and Acceptance Criteria.
2. Select one bounded iteration unit.
3. Take one action.
4. Observe the result using the selected method.
5. Compare the observation with acceptance criteria.
6. Adjust only for the observed gap.
7. Record the cycle in the Loop Log.
8. Stop when a stop condition or escalation trigger is met.

## Stop Conditions

A loop must stop when:

- acceptance criteria are met;
- max iterations are reached;
- the same failure repeats twice;
- required context is missing;
- validation is not possible with available tools;
- a high-impact change becomes necessary;
- scope drift appears;
- user approval is required;
- the loop objective is no longer valid;
- continuing would produce low-confidence or misleading output.

## Escalation Triggers

Escalate when:

- multiple valid directions exist;
- required credentials or permissions are missing;
- validation cannot be performed;
- broad restructuring is needed;
- the loop would exceed the iteration cap;
- repeated failure appears;
- public behavior, release metadata, security posture, or dependencies may change;
- continuing would require assumptions that change the outcome.

## Approval Gate Rules

High-impact loops may inspect and contract the work, but must pause before execution unless the user has approved the bounded scope.

Approval Gate wording should identify:

- why the loop is high impact;
- what actions are blocked;
- what approval scope is requested;
- the recommended safe default.

## Loop Log Requirements

Use this schema:

| Iteration | Action | Observation | Adjustment | Validation | Status |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |

Log only useful, user-visible evidence. Do not expose hidden reasoning.

## Anti-Patterns

Avoid loops that:

- say `repeat until done` without defining done;
- lack an observation method;
- lack validation;
- combine unrelated actions in one cycle;
- keep expanding scope;
- continue after repeated failure;
- hide uncertainty or failed attempts;
- imply background execution.

## Stable Output Requirements

Every stable Loop Contract output must include objective, loop type, iteration unit, observation method, adjustment strategy, validation method, stop conditions, max iterations, escalation triggers, approval gate, loop log, and next step.

## Review Checklist

- [ ] Objective is measurable.
- [ ] Iteration unit is bounded.
- [ ] Observation method is concrete.
- [ ] Validation method is concrete.
- [ ] Stop conditions are complete.
- [ ] Max iterations are appropriate.
- [ ] Escalation triggers are present.
- [ ] Approval Gate is correct.
- [ ] Loop Log is present.
- [ ] No hidden reasoning is requested.
- [ ] No open-ended looping is encouraged.
