# Approval Gate Policy

The Approval Gate keeps high-impact work reviewable before execution.

## Rule

Low-impact work may proceed after a clear task contract is produced. High-impact work must pause for user approval.

## High-Impact Categories

Use an Approval Gate when the task involves:

1. broad repository restructuring;
2. large refactors;
3. public interface or release behavior changes;
4. dependency or packaging changes;
5. release preparation or release metadata;
6. destructive cleanup;
7. permission, authentication, or security boundary changes;
8. loop execution that needs to expand beyond the Optimized Task;
9. repeated loop failure requiring a strategy change.

## Gate Format

```md
## Approval Gate

This task includes high-impact work: [reason].

Recommended next action: review the contract and approve a bounded scope before execution.
```

## Approval Scope

When approval is needed, Codex should ask for a bounded approval scope instead of broad permission.

Good approval scope examples:

- `Approved: update docs only.`
- `Approved: inspect repository and propose changes, but do not edit files.`
- `Approved: edit files under skills/task-contract only.`

## Stop Rules

Stop and request approval when:

- the required action exceeds the current contract;
- a loop reaches its iteration cap;
- the same failure repeats;
- validation requires unavailable tools or permissions;
- a decision affects public behavior or release scope.
