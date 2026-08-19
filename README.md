# GROUNDCONTROL

**spaceagency's practice codex and WA project toolkit — distributed as a Claude plugin.**

GROUNDCONTROL started as the practice's documentation codex — the reference for *what information goes where* in a construction set — and now also carries the WA project workflows spA runs day to day: site analysis, due diligence, planning envelopes, materials research, presentations, and drawing transmittals. It installs once as a single Claude plugin, so any staff member has the whole toolkit available across their conversations with Claude.

A browsable version of the codex is published at **[spaceagencyarchitects.github.io/groundcontrol](https://spaceagencyarchitects.github.io/groundcontrol)**.

> This README is the index of what the plugin contains today. For *how to edit and publish* the codex, see [UPDATING.md](UPDATING.md); for *how Claude should work in this repo*, see [CLAUDE.md](CLAUDE.md).

---

## What's inside

One plugin, `groundcontrol`, containing **13 skills, 3 agents, 8 rules, and 3 hooks**. Everything is reached the same way — describe your task to Claude (or start at `/studio`) and the right piece is selected automatically.

### The codex

| Skill | What it does |
|-------|--------------|
| **groundcontrol** | The documentation codex. Where every building component belongs in the drawing set, sheet numbering (A00–Z), ArchiCAD detail workflows, the SpA Alphabet, drafting principles, and the spA voice. Quick lookups (component → sheets, sheet → contents), guided workflows (set up a set, place a component, choose a detail strategy, run a pre-issue checklist), and the full reference codex as markdown. |

### WA site analysis & due diligence

| Skill | What it does |
|-------|--------------|
| **wa-property-report** | Full WA due-diligence report — cadastre, Certificate of Title, encumbrances, heritage, DA/SAT history, contamination, bushfire, coastal, Aboriginal heritage. |
| **planning-analysis-wa** | The planning envelope — MRS/LPS zone, R-Code, plot ratio, height, setbacks, open space, heritage, BAL. Emits a JSON block for `/zoning-envelope`. |
| **zoning-envelope** | Interactive 3D zoning-envelope viewer generated from a planning analysis. |
| **environmental-analysis** | Climate & environment — temperature, rain, wind, sun angles, flood, bushfire, soil, topography. |
| **mobility-analysis** | Transit & access — train, bus, bike, pedestrian infrastructure, walk scores, airport. |
| **demographics-analysis** | Population, income, age, housing market, and employment from ABS / .id / REIWA. |
| **history** | Neighbourhood context, heritage, architectural character, Traditional Owner context, planned development. |

### Documentation & issue

| Skill | What it does |
|-------|--------------|
| **transmittal** | Build or update a spA drawing issue register / transmittal (xlsx) from a project's issue folders — who received which revision, when. Ships with the spA template. |

### Materials research → Programa

| Skill | What it does |
|-------|--------------|
| **product-research** | FF&E discovery from a brief — returns a curated shortlist as an import-ready CSV for Programa. |
| **product-spec-pdf-parser** | Extracts structured product specs from rep PDFs (price books, fact sheets) into a Programa-ready CSV. |

### Presentation & routing

| Skill | What it does |
|-------|--------------|
| **slide-deck-generator** | Self-contained HTML slide decks in the spaceagency design system — editorial layout, Helvetica, clean white. |
| **studio** | The smart router. Describe a task and it points you at the right skill or agent — start here if unsure. |

### Agents

Agents synthesise several skills into one end-to-end brief.

| Agent | What it does |
|-------|--------------|
| **wa-planning-expert** | WA due diligence + planning envelope in one pass — title, heritage, constraints, buildable envelope, 3D. Knows MRS → LPS → LPP → R-Codes → SPPs and the WA data sources. |
| **site-planner** | Synthesises a full pre-design site brief — climate, environment, transit, demographics, neighbourhood — from the site-analysis skills. |
| **product-and-materials-researcher** | The research front-end to Programa: open-ended discovery from a brief and parsing rep PDFs, ending at a clean CSV. |

### Rules (always-on)

Loaded automatically behind every skill — Western Australia is the default jurisdiction.

`units-and-measurements` · `code-citations` · `code-currency` · `professional-disclaimer` · `natspec-formatting` · `terminology` · `output-formatting` · `transparency`

`code-currency` is the one to know: skills must confirm a code, standard, or rating-tool edition is the current in-force version before relying on it, rather than asserting a fixed edition as current.

### Hooks

`post-output-metadata` (stamps outputs) · `post-write-disclaimer-check` (checks the WA disclaimer is present) · `pre-commit-spec-lint` (lints specs before commit). Enable via the snippet in `plugins/groundcontrol/hooks/settings-snippet.json`.

---

## Install (Claude Code)

```
/plugin marketplace add SpaceagencyArchitects/groundcontrol
/plugin install groundcontrol@groundcontrol
```

Pull updates after a change, or uninstall:

```
/plugin marketplace update groundcontrol
/plugin uninstall groundcontrol@groundcontrol
```

## Install (Claude.ai web/mobile)

Claude.ai uses a manual upload rather than the marketplace command. To load *just the codex skill*: clone this repo, zip `plugins/groundcontrol/skills/groundcontrol/`, then in Claude.ai go to **Settings → Capabilities → Skills → Upload custom skill** and select the zip.

## Use

After install, skills activate automatically from what you ask — you rarely need to name them:

- "Where do I document the wall finishes?" → **groundcontrol**
- "What can we build at 48 Swanbourne St, Fremantle?" → **wa-planning-expert / planning-analysis-wa**
- "Build the transmittal for the Margaret River set." → **transmittal**
- "Find me task chairs, mesh back, $800–1200." → **product-research**
- "I don't know which tool I need…" → **studio** routes you.

---

## Repository structure

```
groundcontrol/                        ← repo root = marketplace + Docsify site + Obsidian vault
├── README.md                          ← this index
├── CLAUDE.md                          ← operating guide for Claude in this repo
├── UPDATING.md                        ← editing + publish procedures
├── ATTRIBUTION.md                     ← upstream MIT attribution
├── LICENSE
├── index.html  ·  .nojekyll           ← Docsify (GitHub Pages)
├── .claude-plugin/
│   └── marketplace.json               ← marketplace catalog
└── plugins/
    └── groundcontrol/                 ← the plugin
        ├── .claude-plugin/plugin.json ← plugin manifest
        ├── skills/                    ← 14 skills (codex content under skills/groundcontrol/references/)
        ├── agents/                    ← 3 agents
        ├── rules/                     ← 8 always-on rules
        └── hooks/                     ← 3 hooks + settings snippet
```

Only the codex skill's `references/` folder is published to the Docsify site — `basePath` is scoped to `skills/groundcontrol/references/`, so `SKILL.md` and the sibling workflow skills stay off the public page.

## Editing on your workstation

This repo doubles as an **Obsidian vault** — open the `groundcontrol/` folder as a vault to browse and edit the codex markdown, the skill/agent notes, and these READMEs with live preview and backlinks. It also opens cleanly in VS Code.

Two things to keep the vault from fighting the published site:

- **Keep Obsidian's config out of git.** Obsidian writes a `.obsidian/` workspace folder; it's listed in `.gitignore` so your personal layout isn't committed.
- **Link the docsify way, not the wiki way.** The codex renders on GitHub Pages via Docsify, which follows relative-path links (`[A50](./A50 - Interface Details.md)`) and the `references/_sidebar.md` nav — not Obsidian `[[wikilinks]]`. When you add or rename a codex note, update `references/_sidebar.md` so it appears on the site.

## Maintaining the codex

**This repository is the source of truth for the codex.** Edit the codex markdown in `plugins/groundcontrol/skills/groundcontrol/references/` directly — with Claude (it applies the codex's own conventions) or by hand in Obsidian / VS Code.

- **Edit / add / delete a note** → change the file, and update `references/_sidebar.md` to match.
- **New lookup category** (component, sheet series) → also add a row to the lookup tables in the codex `SKILL.md`.
- **Bump the version** when a change should reach staff: set the version in three places — `metadata.version` and `plugins[0].version` in `.claude-plugin/marketplace.json`, and `version` in `plugins/groundcontrol/.claude-plugin/plugin.json` — keep them identical, then push. Staff run `/plugin marketplace update groundcontrol`.

Full editing, credential, and publish detail is in [UPDATING.md](UPDATING.md); Claude working here should also read [CLAUDE.md](CLAUDE.md).

## Docsify (web site)

Published via GitHub Pages using [Docsify](https://docsify.js.org) — no build step. Preview locally:

```bash
npx docsify-cli serve .
```

## Validation before pushing

From the repo root, if you have Claude Code locally:

```
claude plugin validate .
```

This catches manifest errors before staff hit them.

## Guides, not rules

The codex frames itself as guides, not rules — adjustments to suit a project are inevitable and are the project leader's call. The skills follow that posture.

## Attribution & licence

The WA workflow skills began as a fork of Alpaca Design Lab's architecture skills (MIT); the upstream notice is preserved in [ATTRIBUTION.md](ATTRIBUTION.md). This repository is MIT licensed — see [LICENSE](LICENSE).
