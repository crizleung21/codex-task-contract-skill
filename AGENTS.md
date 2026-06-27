# AGENTS.md

This repository contains one canonical Codex Skill: `task-contract`.

## Core Rule

Clarify before action. Preserve user intent, bound scope, define output, and state acceptance criteria before execution.

## Canonical Source

Canonical Skill source lives under:

```text
skills/task-contract/
```

The plugin package copy lives under:

```text
plugin/codex-task-contract-skill/skills/task-contract/
```

Update canonical source first. Then sync the plugin package.

## Validation

Before release review, run the repository validators and confirm the plugin package copy matches canonical source.

## Approval Boundary

Pause for approval before broad repository changes, public behavior changes, release metadata changes, dependency changes, file deletion, security posture changes, large refactors, commits, pushes, tags, releases, pull requests, or high-impact loop execution.

## Loop Boundary

Loop Contract Mode must use a finite max iteration count, visible observation evidence, validation method, stop conditions, escalation triggers, and a concise Loop Log.

## Documentation Policy

Keep repository documentation and Skill instructions English-only.

## Style

- Prefer precise, bounded edits.
- Update fixtures when behavior changes.
- Keep P2 expansion work in the roadmap.
- Do not edit packaged Skill files directly unless maintaining sync tooling.
