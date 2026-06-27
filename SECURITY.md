# Security Policy

## Supported Versions

This project is pre-1.0. Security-sensitive behavior should be reviewed before public use.

| Version | Supported |
|---|---|
| main | Yes |
| pre-1.0 releases | Best effort |

## Reporting a Vulnerability

Please open a private security advisory or contact the maintainer through GitHub.

## Security Design Rules

The Skill must not encourage unsafe autonomy. It must pause at an Approval Gate before:

- destructive file changes;
- broad repository changes;
- large refactors;
- dependency installation or dependency updates;
- public behavior changes;
- release metadata changes;
- security posture or security boundary changes;
- commits, pushes, tags, releases, or pull requests;
- any high-impact loop execution;
- any loop scope expansion beyond the approved task contract.

## Safe Defaults

When security impact is unclear, the Skill should default to inspection-only work and ask for bounded approval before execution.

The Skill must not:

- imply background execution;
- continue indefinitely;
- bypass approval for high-impact actions;
- hide uncertainty or failed validation;
- request or expose hidden reasoning.
