# Snapshot: High Risk Refactor Task

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
- approval_gate.recommended_safe_default

## Required Checks

- Verify that the Approval Gate is active (required: true).
- Verify that the blocked action lists refactoring execution.
- Verify that the recommended default is safe inspection-only.

## Approval Requirements

Required before any codebase refactoring begins.

## Forbidden Patterns

- Loop Contract

## Reviewer Notes

High-impact refactoring triggers the Approval Gate.
