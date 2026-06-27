# Snapshot: Destructive File Task

## Expected Mode

Full Contract with Approval Gate

## Required Sections

- Auto-Skeleton
- BLUF
- Optimized Task
- Assumptions
- Constraints
- Output Contract
- Execution Plan
- Acceptance Criteria
- Approval Gate
- Next Step

## Required Fields

- role
- raw_task
- optimized_task
- object
- constraints
- approval_gate
- approval_gate.required
- approval_gate.reason
- approval_gate.blocked_action

## Required Checks

- Verify that the Approval Gate is active (required: true).
- Verify that the blocked action lists deletion of file(s).
- Verify that the reason explicitly warns of data loss.

## Approval Requirements

Required before any file deletion commands are run.

## Forbidden Patterns

- Loop Contract

## Reviewer Notes

Destructive actions must trigger the Approval Gate.
