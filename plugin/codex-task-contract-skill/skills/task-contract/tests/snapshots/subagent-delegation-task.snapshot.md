# Snapshot: Subagent Delegation Task

## Expected Base Mode

Full Contract

## Expected Modifiers

- subagent_delegation

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
- subagent_contract.allowed_paths
- subagent_contract.forbidden_paths
- subagent_contract.allowed_tools
- subagent_contract.forbidden_tools
- subagent_contract.constraints
- subagent_contract.recursion_lock
- subagent_contract.approval_gate
- subagent_contract.acceptance_criteria
- subagent_contract.evidence_required
- subagent_contract.return_format
- subagent_contract.merge_policy
- subagent_contract.failure_policy

## Required Checks

- Verify that recursion lock is explicitly set to true.
- Verify that scope boundary isolates the subagent to read docs/* only.
- Verify that constraints forbid file writing and further delegation.
- Verify that allowed_paths, forbidden_paths, allowed_tools, and forbidden_tools are explicitly defined.

## Approval Requirements

None

## Forbidden Patterns

- recursive spawning

## Reviewer Notes

Requires full subagent contract metadata definition to ensure execution safeguards.
