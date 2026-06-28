# Installation

## Skill Source

Canonical Skill source:

```text
skills/task-contract/SKILL.md
```

## Plugin Package

Plugin package:

```text
plugin/codex-task-contract-skill/
```

Plugin manifest:

```text
plugin/codex-task-contract-skill/.codex-plugin/plugin.json
```

## Local Marketplace

Local marketplace metadata:

```text
.agents/plugins/marketplace.json
```

## Verification

After installation, you can verify the layout using the local smoke test:

```bash
bash scripts/smoke-test-installation.sh
```

To verify the behavior in Codex, invoke:

```text
Use $task-contract to clarify this request before editing files.
```

Expected result: Codex produces an Auto-Skeleton and a task contract before execution.
