# GROUNDCONTROL

spaceagency's documentation codex — the practice reference for *what information goes where* in a construction documentation set. Sheet numbering (A00–Z), allocation of information, annotation and drafting principles, ArchiCAD detail workflows, and the spA voice.

The codex is published two ways from this repo:

- **Website** — [spaceagencyarchitects.github.io/groundcontrol](https://spaceagencyarchitects.github.io/groundcontrol) (Docsify on GitHub Pages).
- **Claude skill** — a standalone skill, `groundcontrol`, that any staff member can upload to Claude.

The WA workflow skills (site analysis, due diligence, planning envelope, materials research, transmittals) are a separate plugin: `SpaceagencyArchitects/spa_wa-architect-skills`.

---

## Repository structure

```
spa_groundcontrol/
├── README.md                  ← this file
├── CLAUDE.md                  ← operating guide for Claude in this repo
├── LICENSE
├── index.html  ·  .nojekyll   ← Docsify site (basePath: groundcontrol/references)
├── scripts/
│   └── package-skill.sh       ← builds dist/groundcontrol.zip for upload
└── groundcontrol/             ← the skill (folder name = skill name)
    ├── SKILL.md               ← triggers, lookup tables, workflows
    └── references/            ← the codex — source of truth, published to the site
        ├── _sidebar.md        ← Docsify navigation
        ├── ✱ SpA GROUNDCONTROL.md
        ├── A00 … A80, Z       ← drawing series notes
        ├── principles/  archicad/  protocol/  tips/
        └── attachments/       ← images and PDFs, one subfolder per note
```

## Install the skill (staff)

Works on any Claude plan, including Free.

1. In Claude, turn on **Settings → Capabilities → Code execution and file creation**.
2. Get `groundcontrol.zip` from Tobias (or build it: `scripts/package-skill.sh`).
3. **Customize → Skills → Upload skill**, select the zip, and switch it on.

After an update, upload the new zip over the old one. Ask a documentation question — "Where do wall finishes go?" — and the skill activates on its own.

## Edit the codex

**`groundcontrol/references/` is the source of truth.** Edit there, nowhere else.

- **Obsidian:** open `groundcontrol/references/` as a vault. This is a practice vault — separate from any personal vault. Its `.obsidian/` config is git-ignored.
- **Links:** Docsify-style relative links and `_sidebar.md`, not `[[wikilinks]]`. Images by URL-encoded relative path into `attachments/<note name>/`.
- **New, renamed or deleted note** → update `_sidebar.md`.
- **New component, sheet or category** → add a row to the lookup tables in `SKILL.md`, and check every path `SKILL.md` names still exists.
- Keep the `#groundcontrol` tag line at the foot of each note.

## Publish

1. Commit and push to `main`. The site updates within a few minutes — check a changed page renders, images included.
2. If staff should get the change in Claude: run `scripts/package-skill.sh` and send round `dist/groundcontrol.zip`.

Preview the site locally:

```bash
npx docsify-cli serve .
```

## Guides, not rules

The codex frames itself as guides, not rules. Adjustments to suit a project are inevitable and are the project leader's call.

## Licence

© 2026 spaceagency, MIT — see [LICENSE](LICENSE).
