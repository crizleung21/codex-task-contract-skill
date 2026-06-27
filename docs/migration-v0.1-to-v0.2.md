# Migration: v0.1.0 to v0.2.0

## Summary

v0.1.0 introduced Loop-aware preview coverage. v0.2.0 promotes that preview into stable Loop Contract Mode.

## What Changed

| Area | v0.1.0 | v0.2.0 |
|---|---|---|
| Loop feature status | Preview | Stable core feature |
| Terminology | Loop-aware Contract | Loop Contract Mode |
| Loop log | Basic | Includes validation column and stop summary |
| References | Single policy file | Policy plus observation, stop, escalation, rubric references |
| Templates | Basic loop template | Compact, full, and shared loop templates |
| Fixtures | Partial expected outputs | Deterministic expected outputs |
| Validation | Manual only | Manual plus lightweight validators |

## Terminology

Use:

- `Loop Contract Mode`
- `Adjustment Strategy`
- `Approval Gate`
- `Stop Conditions`
- `Escalation Triggers`

Historical terms may appear only when describing v0.1.0 behavior.

## Maintainer Checklist

- Review `skills/task-contract/SKILL.md`.
- Review loop reference files.
- Review compact, full, and loop templates.
- Review expected fixtures.
- Run validation commands.
- Confirm plugin manifest version is `0.2.0`.
