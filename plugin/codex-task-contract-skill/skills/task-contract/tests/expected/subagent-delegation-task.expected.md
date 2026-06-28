# Expected: Subagent Delegation Task

Mode: Full Contract with Subagent Delegation
Base Mode: Full Contract
Modifiers:
  - subagent_delegation

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
  - allowed_paths (e.g., docs/*)
  - forbidden_paths (e.g., schemas/*)
  - allowed_tools (e.g., view_file, list_dir)
  - forbidden_tools (e.g., write_to_file)
  - constraints (e.g., read-only, no write, no subagent spawning)
  - recursion_lock (e.g., true)
  - approval_gate (e.g., not required/false)
  - acceptance_criteria (e.g., compile list of stale docs, check headings)
  - evidence_required (e.g., screenshots, output files)
  - return_format (e.g., markdown audit report)
  - merge_policy (e.g., parent_only)
  - failure_policy (e.g., escalate_to_parent)
- Loop log sync section explains that subagent detail logs are not fully nested in parent.
