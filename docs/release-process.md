# Release Process

## Pre-Release Checklist

- [ ] README is updated.
- [ ] `SKILL.md` is updated.
- [ ] References and assets are updated.
- [ ] Plugin package is synced.
- [ ] Fixtures are reviewed.
- [ ] Changelog is updated.
- [ ] Version is updated in plugin manifest.

## Commands

```bash
bash scripts/validate-repo.sh
bash scripts/sync-plugin-package.sh
git status
```

## Tags

Use semantic versions:

- `v0.1.0` for the first MVP.
- `v0.2.0` for Loop Contract Mode.
