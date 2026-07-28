# groundcontrol

**spaceagency's documentation codex — distributed as a Claude plugin.**

GROUNDCONTROL is the practice's reference for what information goes where in a construction documentation set. This repository serves it as a Claude Code plugin, so any spA staff member can install it once and have it available across all their conversations with Claude.

A browsable version of the codex is available at **[spaceagencyarchitects.github.io/groundcontrol](https://spaceagencyarchitects.github.io/groundcontrol)**.

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
- "Should this be a model-based or drawn independent detail?"
- "Can you review this drawing note?"
- "Run the pre-issue checklist over this sheet."

For the full set of triggers and workflows, see `plugins/groundcontrol/skills/groundcontrol/SKILL.md`.

---

## Repository structure

```
groundcontrol/                                 ← repo root = marketplace + Docsify site
├── index.html                                  ← Docsify entry point (GitHub Pages)
├── .nojekyll                                   ← disables Jekyll processing
├── .claude-plugin/
│   └── marketplace.json                        ← marketplace catalog
├── plugins/
│   └── groundcontrol/                          ← the plugin
│       ├── .claude-plugin/
│       │   └── plugin.json                     ← plugin manifest
│       └── skills/
│           └── groundcontrol/                  ← the skill itself
│               ├── SKILL.md                    ← entry point + lookup tables + workflows
│               ├── _sidebar.md                 ← Docsify navigation
│               ├── ✱ SpA GROUNDCONTROL.md      ← codex index
│               ├── A00 ... A80.md              ← drawing series
│               ├── Z - Specifications.md
│               ├── principles/                 ← drafting fundamentals
│               ├── archicad/                   ← ArchiCAD workflows and tagging
│               ├── protocol/                   ← practice policies (AI usage etc)
│               └── tips/                       ← tips and checklists
├── README.md
└── LICENSE
```

## Maintaining the codex

> **Full process, including the Claude-assisted Bear → GitHub → Docsify workflow and its one-time setup (Bear attachment access, push credentials), is documented in [UPDATING.md](UPDATING.md).**

The Bear notes tagged `#groundcontrol` are the source of truth. The repo is kept in sync manually:

- **Edit content** → update the note in Bear, then sync to the matching `.md` file in `plugins/groundcontrol/skills/groundcontrol/`.
- **Add a new note** → create the Bear note with the appropriate `#groundcontrol` sub-tag, write the file to the correct subfolder, add it to `_sidebar.md`.
- **Delete a note** → delete from Bear, `git rm` the file, remove from `_sidebar.md`.
- **Add a new lookup category** (e.g. a new component, a new sheet series) → also add a row to the lookup tables in `SKILL.md`.
- **Bump the version** when changes warrant a re-pull from staff: update `version` in both `.claude-plugin/marketplace.json` and `plugins/groundcontrol/.claude-plugin/plugin.json`. Then push. Staff run `/plugin marketplace update groundcontrol`.

## Docsify (web site)

The codex is published as a static site via GitHub Pages using [Docsify](https://docsify.js.org). No build step — Docsify renders the markdown files directly from the repo.

To preview locally:
```bash
npx docsify-cli serve .
```
Then open [http://localhost:3000](http://localhost:3000).

To remove the site: `git rm index.html .nojekyll plugins/groundcontrol/skills/groundcontrol/_sidebar.md` and disable GitHub Pages in repo settings.

## Validation before pushing

If you have Claude Code locally, run:

```
claude plugin validate .
```

from the repo root. This catches manifest errors before staff hit them.

## Guides not rules

The codex frames itself as guides, not rules — adjustments to suit a particular project are inevitable, and are the project leader's call. The skill follows that posture.
