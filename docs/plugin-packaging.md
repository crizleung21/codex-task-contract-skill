# Plugin Packaging

## Package Path

```text
plugin/codex-task-contract-skill/
```

## Manifest

```text
plugin/codex-task-contract-skill/.codex-plugin/plugin.json
```

## Required Manifest Fields

- `name`
- `version`
- `description`
- `skills`

## Sync Process

The canonical Skill source lives under `skills/task-contract/`. The plugin package copy should be synced before release.

```bash
bash scripts/sync-plugin-package.sh
```

## Local Marketplace

Use `.agents/plugins/marketplace.json` to test local installation metadata.
