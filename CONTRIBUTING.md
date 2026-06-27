# Contributing

Thank you for contributing to `codex-task-contract-skill`.

## Contribution Principles

1. Preserve the core purpose: clarify before action.
2. Keep the Skill focused on task contracts, scope control, and bounded loop governance.
3. Avoid scope creep into a general autonomous agent framework.
4. Add or update fixtures when behavior changes.
5. Keep high-impact actions behind an Approval Gate.
6. Do not request or expose hidden reasoning.
7. Do not imply background execution or unlimited iteration.

## Canonical Source Rule

Canonical Skill source lives under:

```text
skills/task-contract/
```

The plugin package copy lives under:

```text
plugin/codex-task-contract-skill/skills/task-contract/
```

Update canonical source first. Then run:

```bash
bash scripts/sync-plugin-package.sh
```

Do not manually edit the packaged Skill copy unless you are maintaining sync tooling.

## Development Workflow

1. Create a feature branch.
2. Update canonical files under `skills/task-contract/`.
3. Update docs and fixtures when behavior changes.
4. Run validation scripts.
5. Sync the plugin package before release review.
6. Run validation again after sync.
7. Review the final diff.

## Validation Commands

```bash
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
git status
```

## Pull Request Checklist

- [ ] Behavior change is documented.
- [ ] `SKILL.md` remains focused and practical.
- [ ] Relevant references or assets are updated.
- [ ] Fixtures are added or updated.
- [ ] Approval Gate behavior is preserved.
- [ ] Loop behavior is bounded by max iterations and stop conditions.
- [ ] Plugin package is synchronized after canonical Skill changes.
- [ ] Validators pass.
- [ ] No hidden reasoning is requested or exposed.
- [ ] No background or open-ended execution is encouraged.
