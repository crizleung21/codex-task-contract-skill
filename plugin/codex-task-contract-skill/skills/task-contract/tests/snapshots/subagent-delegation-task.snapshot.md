# Snapshot: Subagent Delegation Task

## Expected Mode

Full Contract with Subagent Delegation

## Required Sections

- Auto-Skeleton
- BLUF
- Optimized Task
- Assumptions
- Constraints
- Decision Points
- Output Contract
- Execution Plan
- Acceptance Criteria
- Subagent Contract
- Next Step

## Required Fields

- role
- raw_task
- optimized_task
- object
- subagent_contract
- subagent_contract.parent_conversation_id
- subagent_contract.subagent_role
- subagent_contract.scope_boundary
- subagent_contract.constraints
- subagent_contract.recursion_lock
- subagent_contract.approval_gate
- subagent_contract.acceptance_criteria
- subagent_contract.return_format

## Required Checks

- Verify that recursion lock is explicitly set to true.
- Verify that scope boundary isolates the subagent to read docs/* only.
- Verify that constraints forbid file writing and further delegation.

## Approval Requirements

None

## Forbidden Patterns

- recursive spawning

## Reviewer Notes

Requires full subagent contract metadata definition to ensure execution safeguards.
