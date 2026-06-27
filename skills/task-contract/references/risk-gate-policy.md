# Risk Gate Policy

The Risk Gate keeps the Skill reviewable before high-impact work begins.

## Rule

Low-risk work may proceed after a clear contract is produced. High-impact work must pause for user approval.

## High-Impact Examples

- Broad repository restructuring.
- Large refactors.
- Public interface changes.
- Dependency or release changes.
- Any loop that needs to change scope after repeated failure.

## Template

```md
## Risk Gate

This task includes high-impact work: [reason].

Recommended next action: review the contract and confirm before execution.
```
