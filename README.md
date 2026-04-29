# groundcontrol

**spaceagency's documentation codex — distributed as a Claude plugin.**

GROUNDCONTROL is the practice's reference for what information goes where in a construction documentation set. This repository serves it as a Claude Code plugin, so any spA staff member can install it once and have it available across all their conversations with Claude.

---

## Install (Claude Code)

Two commands from inside Claude Code:

```
/plugin marketplace add SpaceagencyArchitects/groundcontrol
/plugin install groundcontrol@groundcontrol
```

> Append `@<branch-or-tag>` to the marketplace add command to pin to a specific version.

To pull updates after the codex changes:

```
/plugin marketplace update groundcontrol
```

To uninstall:

```
/plugin uninstall groundcontrol@groundcontrol
```

## Install (Claude.ai web/mobile)

Claude.ai uses a manual upload flow rather than the marketplace command:

1. Clone or download this repo.
2. Zip the `plugins/groundcontrol/skills/groundcontrol/` folder (just the skill, not the marketplace wrapper).
3. In Claude.ai, go to **Settings → Capabilities → Skills → Upload custom skill** and select the zip.

Once uploaded, the skill loads automatically whenever you ask Claude a documentation question.

## Use

After install, the skill activates automatically when you ask anything that touches construction documentation. You don't need to invoke it by name — Claude picks it up from cues like:

- "Where do I document the wall finishes?"
- "What goes on A50?"
- "I'm setting up the drawing set for a new project — walk me through it."
- "Should this detail be a WF50.1 or a WF50.3?"
- "Can you review this drawing note?"
- "Run the pre-issue checklist over this sheet."

For the full set of triggers and workflows, see `plugins/groundcontrol/skills/groundcontrol/SKILL.md`.

---

## Repository structure

```
groundcontrol/                                 ← repo root = marketplace
├── .claude-plugin/
│   └── marketplace.json                        ← marketplace catalog
├── plugins/
│   └── groundcontrol/                          ← the plugin
│       ├── .claude-plugin/
│       │   └── plugin.json                     ← plugin manifest
│       └── skills/
│           └── groundcontrol/                  ← the skill itself
│               ├── SKILL.md                    ← entry point + lookup tables + workflows
│               ├── ✱ SpA GROUNDCONTROL.md      ← codex index
│               ├── A00 ... A80 .md             ← drawing series files
│               ├── Z - Specifications.md
│               ├── principles/                 ← drafting fundamentals
│               ├── components/                 ← building elements
│               ├── archicad/                   ← ArchiCAD workflows (WF50.1–.4, keynotes, hotlinks)
│               └── tips/                       ← checklists
├── README.md
└── LICENSE
```

## Maintaining the codex

The skill reads the codex `.md` files as bundled reference content. To improve the skill's behaviour:

- **Add or edit a codex entry** → just edit the relevant file in `plugins/groundcontrol/skills/groundcontrol/`. No SKILL.md change needed; Claude picks up the change next time the skill loads.
- **Add a new lookup category** (e.g. a new component, a new sheet series) → also add a row to the lookup tables in `SKILL.md`.
- **Change a workflow** → edit the relevant section in `SKILL.md`.
- **Bump the version** when changes warrant a re-pull from staff: update `version` in both `.claude-plugin/marketplace.json` and `plugins/groundcontrol/.claude-plugin/plugin.json`. Then push. Staff run `/plugin marketplace update groundcontrol`.

Note: if `version` is omitted in either manifest, Claude Code treats every commit as a new version — fine for actively-developed internal use, less ideal once the codex stabilises.

## Validation before pushing

If you have Claude Code locally, run:

```
claude plugin validate .
```

from the repo root. This catches manifest errors before staff hit them.

## Guides not rules

The codex frames itself as guides, not rules — adjustments to suit a particular project are inevitable, and are the project leader's call. The skill follows that posture.
