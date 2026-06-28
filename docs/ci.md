# CI

Status: v0.5.0 CI guide.

The CI workflow must mirror the local release validation sequence as closely as possible.

## Workflow

```text
.github/workflows/validate.yml
```

The workflow runs on:
- push;
- pull request;
- workflow dispatch.

## CI Steps

The workflow runs the following validation sequence:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-release-consistency.py
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
python3 scripts/validate-contract-semantics.py
bash scripts/smoke-test-installation.sh
```

## Local Parity

Before release, run the same commands locally from the repository root:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-release-consistency.py
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
python3 scripts/validate-contract-semantics.py
bash scripts/smoke-test-installation.sh
git status
```

## Network Boundary

v0.5.0 validation should use committed repository files only. Validation must not require network access.

## Release Gate

A v0.5.0 tag should not be created until the latest CI run is green and local validation has passed after plugin package sync.
