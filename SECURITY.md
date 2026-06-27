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

The Skill must not encourage unsafe autonomy. It must require confirmation before:

- destructive file changes;
- broad refactors;
- dependency installation;
- security boundary changes;
- commits, pushes, releases, or pull requests;
- any high-risk loop execution.
