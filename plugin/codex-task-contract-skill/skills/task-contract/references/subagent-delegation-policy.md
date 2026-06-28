# Subagent Delegation Policy

Status: v0.5.0 subagent delegation policy.

This reference defines the policy and safeguards when a parent agent delegates tasks to subagents.

## Core Principle

Divide and isolate. A parent agent must clarify, scope, and contract any delegated subagent task using a Subagent Contract before spawning the subagent.

## Delegation Rules

1. **Necessity Check**: Only delegate when the task involves independent sub-components (such as dedicated research, isolated debugging, or doc compilation) that would clutter the parent's context.
2. **Scope Isolation**: Every subagent must be restricted to a strict directory or set of commands. Specify this under `scope_boundary`.
3. **Explicit Paths and Tools**: The contract must define `allowed_paths`, `forbidden_paths`, `allowed_tools`, and `forbidden_tools` to prevent unauthorized execution.
4. **Acceptance Criteria**: The subagent contract must list clear, machine-verifiable or checklist-verifiable acceptance criteria.
5. **Recursion Lock**: Subagents are forbidden from spawning their own subagents recursively unless the parent's contract explicitly allows it. The recursion lock defaults to `true`.
6. **Integration Control**: The parent contract controls the integration of subagent work via a defined `merge_policy` (e.g. `parent_only`) and handles errors via `failure_policy` (e.g. `escalate_to_parent`).
7. **Evidence Verification**: Subagents must return concrete evidence (e.g. tests, logs, diffs) specified by `evidence_required` before their work is accepted.
8. **No Direct Execution of Broad Changes**: Subagents must not run broad repository edits, pushes, or releases. They are restricted to their delegated boundary.

## Loop Log Syncing

- Parent agents must log the delegation event in the main Loop Log:
  - Iteration Action: `Spawn subagent <id> for <task>`
  - Iteration Observation: `Subagent completed with status <success/fail>`
- Detailed subagent execution logs must not be fully nested inside the parent's Loop Log. Save them in independent files or nested sub-sections.
