#!/bin/bash
# post-write-disclaimer-check.sh
# Fires after Write tool — checks that regulatory outputs include the professional disclaimer.
# Default jurisdiction: Western Australia. Keywords tuned to NCC / R-Codes / LPS / Heritage / BAL content.

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# Only check markdown reports (skip HTML, CSV, JSON, images)
if [[ "$FILE_PATH" != *.md ]]; then
  exit 0
fi

CONTENT=$(cat "$FILE_PATH" 2>/dev/null)
if [ -z "$CONTENT" ]; then
  exit 0
fi

# Look for regulatory indicators — WA practice context
REGULATORY=false

# Planning & zoning (LPS / LPP / MRS / R-Codes)
if echo "$CONTENT" | grep -qiE 'zoning|setback|plot ratio|height limit|site coverage|R-?Codes?|\bR[0-9]+\b|\bLPS[0-9]*\b|\bLPP\b|\bMRS\b|development (approval|application)|planning approval|permitted use|discretionary use|structure plan|activity centre'; then
  REGULATORY=true
# Building code (NCC / BCA / fire / egress)
elif echo "$CONTENT" | grep -qiE 'occupan(cy|t) load|egress|\bNCC\b|\bBCA\b|deemed-to-satisfy|\bDTS\b|performance solution|fire resistance level|\bFRL\b|building permit|occupancy permit|Class [1-9]\b'; then
  REGULATORY=true
# Environmental risk (bushfire / flood / acid sulfate / coastal / contamination)
elif echo "$CONTENT" | grep -qiE 'bushfire|\bBAL\b|bushfire attack level|flood|acid sulfate|coastal erosion|storm surge|SPP 2\.6|SPP 3\.7|contaminated (site|land)'; then
  REGULATORY=true
# Approval bodies / appeals
elif echo "$CONTENT" | grep -qiE '\bJDAP\b|\bLDAP\b|\bWAPC\b|\bSAT\b|\bDPLH\b|responsible authority|development assessment panel'; then
  REGULATORY=true
# Heritage (State Register / LHS / Burra Charter)
elif echo "$CONTENT" | grep -qiE 'heritage place|State Register|Municipal Inventory|Local Heritage Survey|\bLHS\b|Heritage Area|Burra Charter|conservation plan|heritage impact statement|\bHIS\b|inHerit'; then
  REGULATORY=true
fi

if [ "$REGULATORY" = false ]; then
  exit 0
fi

# Check for disclaimer — matches the WA disclaimer language in rules/professional-disclaimer.md
if echo "$CONTENT" | grep -qiE 'disclaimer|registered architect|suitably qualified practitioner|preliminary planning purposes'; then
  exit 0
fi

# Missing disclaimer on regulatory output — warn (don't block)
echo "WARNING: $FILE_PATH contains regulatory content (NCC / R-Codes / LPS / BAL / heritage / WAPC / SAT) but no professional disclaimer. Add the standard disclaimer from rules/professional-disclaimer.md." >&2
exit 0
