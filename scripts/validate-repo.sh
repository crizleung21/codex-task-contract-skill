#!/usr/bin/env bash
set -euo pipefail
python3 scripts/validate-repo.py
python3 scripts/validate-plugin-sync.py
