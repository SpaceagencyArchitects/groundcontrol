# Hooks

Hooks are event-driven automations that run automatically during Claude Code sessions. Unlike skills (invoked manually) and rules (reference documents), hooks fire on lifecycle events — after a file is written, before a commit, etc.

**Default jurisdiction: Western Australia.** Hooks are tuned to NCC / R-Codes / LPS / Heritage / NATSPEC conventions.

## Available Hooks

| Hook | Event | What it does |
|------|-------|-------------|
| [post-write-disclaimer-check](./post-write-disclaimer-check.sh) | After Write | Warns if a regulatory output (NCC, R-Codes, LPS, BAL, heritage, WAPC / SAT) is missing the professional disclaimer |
| [post-output-metadata](./post-output-metadata.sh) | After Write | Stamps markdown reports with YAML front matter (title, date, skill name) if missing |
| [pre-commit-spec-lint](./pre-commit-spec-lint.sh) | Before git commit | Scans staged markdown files for malformed NATSPEC worksection numbers |

## Installation

Hooks are opt-in — they run from your local Claude Code settings, not from the plugin automatically.

### Step 1: Make scripts executable

```bash
chmod +x ~/.claude/plugins/groundcontrol/hooks/*.sh
```

If you cloned the repo elsewhere, adjust the path accordingly.

### Step 2: Add to your Claude Code settings

Copy the hook configuration from [`settings-snippet.json`](./settings-snippet.json) into your Claude Code settings file:

- **All projects:** `~/.claude/settings.json`
- **Single project:** `.claude/settings.json` (in your project root)
- **Local only:** `.claude/settings.local.json` (gitignored)

Merge the `hooks` key into your existing settings. If you already have `PostToolUse` or `PreToolUse` hooks, add these entries to the existing arrays.

### Step 3: Verify

Run `/hooks` in Claude Code to confirm your hooks are loaded.

## Behavior

All three hooks **warn but do not block**. They print messages to stderr when issues are found but allow the action to proceed. To make any hook enforce (block the action), change `exit 0` to `exit 2` at the warning point in the script.

### post-write-disclaimer-check

Scans written `.md` files for WA regulatory keywords in five categories:

- **Planning & zoning** — zoning, setback, plot ratio, R-Codes, R20 / R40 / etc., LPS, LPP, MRS, development approval, permitted / discretionary use, structure plan
- **Building code** — NCC, BCA, occupancy / occupant load, egress, DTS, performance solution, FRL, building / occupancy permit, NCC Class
- **Environmental risk** — bushfire, BAL, flood, acid sulfate, coastal erosion, storm surge, SPP 2.6, SPP 3.7, contaminated site
- **Approval bodies** — JDAP, LDAP, WAPC, SAT, DPLH, responsible authority, DAP
- **Heritage** — State Register, Municipal Inventory, Local Heritage Survey / LHS, Heritage Area, Burra Charter, conservation plan, heritage impact statement, inHerit

If any keyword is found and no disclaimer is present, prints a warning. Skips non-markdown files, HTML decks, and data files.

### post-output-metadata

Prepends YAML front matter to new markdown reports that don't already have it. Skips README.md, SKILL.md, CLAUDE.md, and files inside rules/, hooks/, or .claude-plugin/ directories.

### pre-commit-spec-lint

Checks staged `.md` files for NATSPEC worksection formatting errors:

- Dashed format: `01-81` → should be `0181`
- Dotted format: `01.81` → should be `0181`
- Dash/em-dash before title: `0181 — Concrete in situ` → should be `0181 Concrete in situ`
- Missing title: `0181` alone → should be `0181 Concrete in situ`
- CSI MasterFormat 6-digit section numbers found (wrong system for this studio — flagged unless the spec declares CSI at the head, for overseas projects)

See [`rules/natspec-formatting.md`](../rules/natspec-formatting.md) for the full conventions.

## Customization

Each script is a standalone bash file. Edit to fit your workflow:

- Change warning to enforcement: replace `exit 0` with `exit 2` after the warning message
- Add more regulatory keywords to the disclaimer check
- Add project-specific metadata fields to the front matter stamp
- Adjust NATSPEC lint patterns for your in-house worksection conventions
