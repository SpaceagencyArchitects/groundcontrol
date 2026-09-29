#!/usr/bin/env bash
# Package the GROUNDCONTROL codex as an uploadable Claude skill zip.
# Output: dist/groundcontrol.zip  (upload in Claude: Customize → Skills → Upload)
# Paths are slugged for upload — see package_skill.py.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/package_skill.py
