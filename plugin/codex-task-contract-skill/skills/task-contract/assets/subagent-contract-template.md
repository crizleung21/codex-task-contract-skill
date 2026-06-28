# Subagent Contract - [Subagent Role Name]

## Metadata

```yaml
parent_conversation_id: [parent-id]
subagent_role: [role]
scope_boundary: [boundary]
allowed_paths:
  - [path]
forbidden_paths:
  - [path]
allowed_tools:
  - [tool]
forbidden_tools:
  - [tool]
handoff_input:
  [param]: [value]
constraints:
  - [constraint]
max_iterations: [number]
recursion_lock: true
approval_gate:
  required: [true/false]
  reason: [reason]
  blocked_action: [action]
  recommended_safe_default: [default]
  reply_template: [template]
acceptance_criteria:
  - [criteria]
evidence_required:
  - [evidence]
return_format: [format]
return_schema:
  [property]: [type]
merge_policy: parent_only
failure_policy: escalate_to_parent
```

## Scope Boundary

[Description of the scope boundary, directories, files, or tools the subagent is permitted to use.]

## Constraints

[Any constraints such as read-only access, network isolation, or command limits.]

## Acceptance Criteria

- [ ] [Criteria 1]
- [ ] [Criteria 2]

## Return Format

[The expected shape, file type, or format of the returned report.]

## Parent Loop Log Sync

Log this delegation in the parent conversation's Loop Log under a single iteration:
- Action: `Spawn subagent [role] for [task]`
- Observation: `Subagent completed with status [status] and evidence [evidence]`
