#!/bin/bash
# pre-commit-spec-lint.sh
# Fires before git commit — scans staged .md files for malformed NATSPEC worksection references.
# Default spec system: NATSPEC (see rules/natspec-formatting.md).
# Valid:   0181 Concrete in situ ; D0411 Brick and block construction
# Invalid: 01-81 ; 01.81 ; 0181 — Concrete in situ ; CSI-style 09 29 00

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Only run on git commit commands
if [[ "$COMMAND" != git\ commit* ]]; then
  exit 0
fi

# Get list of staged markdown files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null | grep '\.md$')

if [ -z "$STAGED_FILES" ]; then
  exit 0
fi

# Regex note: we post-filter every pattern with a spec/NATSPEC keyword filter so that
# dates (`2018`), standards (`AS 3600`), and legislation clauses (`s. 162`) aren't
# flagged as malformed worksections.
SPEC_CONTEXT='worksection|NATSPEC|specification|\bspec '

ERRORS=""

while IFS= read -r FILE; do
  [ -f "$FILE" ] || continue

  # 1. Dashed format:  01-81  → should be  0181
  BAD_DASHED=$(grep -nE '\bD?[0-9]{2}-[0-9]{2}\b' "$FILE" 2>/dev/null | grep -iE "$SPEC_CONTEXT")
  if [ -n "$BAD_DASHED" ]; then
    ERRORS="$ERRORS\n$FILE: NATSPEC worksection number uses dashes (use '0181' not '01-81'):\n$BAD_DASHED\n"
  fi

  # 2. Dotted format:  01.81  → should be  0181
  BAD_DOTTED=$(grep -nE '\bD?[0-9]{2}\.[0-9]{2}\b' "$FILE" 2>/dev/null | grep -iE "$SPEC_CONTEXT")
  if [ -n "$BAD_DOTTED" ]; then
    ERRORS="$ERRORS\n$FILE: NATSPEC worksection number uses dots (use '0181' not '01.81'):\n$BAD_DOTTED\n"
  fi

  # 3. Em-dash or hyphen between code and title:  0181 — Concrete in situ  → should be  0181 Concrete in situ
  BAD_DASH_SEP=$(grep -nE '\bD?[0-9]{4}[[:space:]]*[—-][[:space:]]*[A-Z]' "$FILE" 2>/dev/null | grep -iE "$SPEC_CONTEXT")
  if [ -n "$BAD_DASH_SEP" ]; then
    ERRORS="$ERRORS\n$FILE: NATSPEC worksection uses dash/em-dash before title (use '0181 Concrete in situ' not '0181 — Concrete in situ'):\n$BAD_DASH_SEP\n"
  fi

  # 4. CSI MasterFormat 6-digit section numbers — wrong system for this studio
  BAD_CSI_STYLE=$(grep -nE '\b[0-9]{2} [0-9]{2} [0-9]{2}\b' "$FILE" 2>/dev/null | grep -iE 'section|spec|division|MasterFormat|CSI')
  if [ -n "$BAD_CSI_STYLE" ]; then
    ERRORS="$ERRORS\n$FILE: CSI MasterFormat 6-digit section numbers found — this studio uses NATSPEC (4-digit worksection codes). For overseas projects declare the system at the head of the spec:\n$BAD_CSI_STYLE\n"
  fi

  # 5. Bare worksection code with no title — looks like '0181' on its own in a spec line
  BAD_NOTITLE=$(grep -nE '\bD?[0-9]{4}\b[[:space:]]*$' "$FILE" 2>/dev/null | grep -iE "$SPEC_CONTEXT")
  if [ -n "$BAD_NOTITLE" ]; then
    ERRORS="$ERRORS\n$FILE: NATSPEC worksection reference missing title (use '0181 Concrete in situ'):\n$BAD_NOTITLE\n"
  fi

done <<< "$STAGED_FILES"

if [ -n "$ERRORS" ]; then
  echo -e "NATSPEC formatting issues found in staged files:\n$ERRORS" >&2
  echo "Fix these before committing, or see rules/natspec-formatting.md for conventions." >&2
  # Warn but don't block — exit 0 to allow commit, change to exit 2 to enforce
  exit 0
fi

exit 0
