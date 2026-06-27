# Plugin Packaging

Canonical Skill source lives under:

```text
skills/task-contract/
```

The packaged plugin copy lives under:

```text
plugin/codex-task-contract-skill/skills/task-contract/
```

Update canonical source first. Then sync the package copy before release review.

## Local Package Invariants

| Item | Value |
|---|---|
| Plugin name | `codex-task-contract-skill` |
| Plugin version | `0.4.0` |
| Skills path | `./skills/` |
| Canonical Skill | `skills/task-contract/` |
| Packaged Skill | `plugin/codex-task-contract-skill/skills/task-contract/` |

## Review Checklist

- [ ] Canonical Skill files are updated.
- [ ] Plugin package is synchronized.
- [ ] Manifest version matches the release target.
- [ ] Validators pass after sync.
