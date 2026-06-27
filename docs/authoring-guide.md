# Authoring Guide

## Canonical Source

Edit the canonical Skill source here:

```text
skills/task-contract/SKILL.md
```

## References

Use `skills/task-contract/references/` for detailed behavior rules.

## Assets

Use `skills/task-contract/assets/` for output templates and examples.

## Tests

Use `skills/task-contract/tests/fixtures/` for input prompts and `skills/task-contract/tests/expected/` for expected outputs.

## Plugin Package

After editing the canonical Skill, sync the plugin package:

```bash
bash scripts/sync-plugin-package.sh
```
