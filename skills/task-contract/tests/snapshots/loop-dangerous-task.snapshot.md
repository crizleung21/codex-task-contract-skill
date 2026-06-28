# Snapshot: Loop Dangerous Task

## Expected Base Mode

Loop Contract Mode

## Expected Modifiers

- approval_gate

## Required Sections

- Auto-Skeleton
- BLUF
- Optimized Task
- Output Contract
- Loop Contract
- Loop Procedure
- Loop Log
- Validation Method
- Stop Conditions
- Escalation Triggers
- Approval Gate
- Next Step

## Required Fields

- loop_objective
- loop_type
- iteration_unit
- observation_method
- adjustment_strategy
- validation_method
- stop_conditions
- max_iterations
- escalation_triggers
- approval_gate
- approval_gate.required
- loop_log

## Required Checks

- Verify that Loop Type is "High-impact loop".
- Verify that Max Iterations defaults to 1 before approval.
- Verify that the Approval Gate is active (required: true).
- Verify that the blocked action lists executing the dangerous command loop.

## Approval Requirements

Required before starting the dangerous iteration cycle.

## Forbidden Patterns

- continue without approval

## Reviewer Notes

Dangerous loop requiring verification after a single test iteration.
