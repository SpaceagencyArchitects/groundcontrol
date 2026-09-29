#!/usr/bin/env bash
# Package the GROUNDCONTROL codex as an uploadable Claude skill zip.
# Output: dist/groundcontrol.zip  (upload in Claude: Customize → Skills → Upload)
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
rm -f dist/groundcontrol.zip
zip -rq dist/groundcontrol.zip groundcontrol \
  -x '*/.obsidian/*' '*.DS_Store' '*/._*'
echo "Built dist/groundcontrol.zip ($(du -h dist/groundcontrol.zip | cut -f1))"
