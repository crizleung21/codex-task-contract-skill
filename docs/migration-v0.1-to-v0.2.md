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
| Templates | Basic loop template | Full and compact stable templates |
| Fixtures | Partial expected outputs | Stable golden expected outputs |
| Validation | Manual only | Manual plus zero-dependency loop validator |

## Terminology

Use:

- `Loop Contract Mode`
- `Adjustment Strategy`
- `Approval Gate`
- `Stop Conditions`
- `Escalation Triggers`

Avoid:

- `autonomous mode`
- `background loop`
- `unlimited iteration`
- `repeat until done` without a defined stop condition

## Maintainer Checklist

- Review `skills/task-contract/SKILL.md`.
- Review new loop reference files.
- Review full and compact loop templates.
- Run `bash scripts/validate-loop-contract-fixtures.sh`.
- Confirm plugin manifest version is `0.2.0`.
