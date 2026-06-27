# Subagent Delegation Policy

Status: v0.4.0 subagent delegation policy.

This reference defines the policy and safeguards when a parent agent delegates tasks to subagents.

## Core Principle

Divide and isolate. A parent agent must clarify, scope, and contract any delegated subagent task using a Sub-contract before spawning the subagent.

## Delegation Rules

1. **Necessity Check**: Only delegate when the task involves independent sub-components (such as dedicated research, isolated debugging, or doc compilation) that would clutter the parent's context.
2. **Scope Isolation**: Every subagent must be restricted to a strict directory or set of commands. Specify this under `scope_boundary` (e.g., `["read docs/*", "write scratch/*"]`).
3. **Acceptance Criteria**: The subagent contract must list clear, machine-verifiable or checklist-verifiable acceptance criteria.
4. **Recursion Lock**: Subagents are forbidden from spawning their own subagents recursively unless the parent's contract explicitly allows it.
5. **No Direct Execution of Broad Changes**: Subagents must not run broad repository edits, pushes, or releases. They are restricted to their delegated boundary.

## Loop Log Syncing

- Parent agents must log the delegation event in the main Loop Log:
  - Iteration Action: `Spawn subagent <id> for <task>`
  - Iteration Observation: `Subagent completed with status <success/fail>`
- Detailed subagent execution logs must not be fully nested inside the parent's Loop Log. Save them in independent files or nested sub-sections.
