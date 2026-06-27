# Expected: Subagent Delegation Task

Mode: Full Contract with Subagent Delegation

## Required Sections

1. Auto-Skeleton
2. BLUF
3. Optimized Task
4. Assumptions
5. Constraints
6. Decision Points
7. Output Contract
8. Execution Plan
9. Acceptance Criteria
10. Subagent Contract
11. Next Step

## Required Checks

- Auto-Skeleton matches the delegation scope.
- Mode is Full Contract with Subagent Delegation.
- Subagent Contract metadata block includes:
  - parent_conversation_id
  - subagent_role (e.g., Documentation Auditor)
  - scope_boundary (e.g., read docs/* only)
  - constraints (e.g., read-only, no write, no subagent spawning)
  - recursion_lock (e.g., true)
  - approval_gate (e.g., not required/false)
  - acceptance_criteria (e.g., compile list of stale docs, check headings)
  - return_format (e.g., markdown audit report)
- Loop log sync section explains that subagent detail logs are not fully nested in parent.
