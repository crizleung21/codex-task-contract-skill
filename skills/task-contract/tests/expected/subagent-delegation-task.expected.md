Mode: Full Contract with Subagent Delegation

## Auto-Skeleton
- **Role**: Codebase Researcher & Auditor
- **Raw Task**: Spawn subagent to audit doc folder
- **Optimized Task**: Delegate markdown lint check to subagent to identify syntax errors, so that main documentation is validated.
- **Object**: docs/
- **Context**: Parent needs markdown syntax audit.
- **Constraints**: Subagent must not write files.
- **Output**: Subagent audit report.
- **Acceptance**: Return lint errors.

## Subagent Delegation
- **Parent Conversation ID**: parent-123
- **Subagent Role**: Doc Auditor
- **Allowed Scope**: `docs/*`
- **Constraints**: No file writes, no recursion.
- **Acceptance Criteria**: All docs verified, markdown errors list returned.
