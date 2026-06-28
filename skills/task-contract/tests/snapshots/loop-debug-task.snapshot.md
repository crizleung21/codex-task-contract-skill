# Snapshot: Loop Debug Task

## Expected Base Mode

Loop Contract Mode

## Expected Modifiers

[]

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
- loop_log

## Required Checks

- Verify that Loop Type is "Coding/debug loop".
- Verify that Max Iterations defaults to 5.
- Verify that Loop Log is present.

## Approval Requirements

None

## Forbidden Patterns

- open-ended looping
- background worker

## Reviewer Notes

Iterative debugging requiring build/test validation at each cycle.
