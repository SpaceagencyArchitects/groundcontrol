# Updating GROUNDCONTROL

How codex content flows from Bear to this repository, the GitHub Pages site, and the Claude plugin — and how to run an update.

## How the pieces fit together

```
Bear notes (#groundcontrol)          ← source of truth, edited by spA staff
        │
        │  sync via Claude (Cowork)
        ▼
this repository                      ← markdown mirror of the notes
  plugins/groundcontrol/skills/groundcontrol/
        │
        ├──▶ docsify site            spaceagencyarchitects.github.io/groundcontrol
        │    (index.html renders the markdown; updates automatically on push)
        │
        └──▶ Claude plugin           installed by staff via the plugin marketplace
             (marketplace.json / plugin.json define the version)
```

**Bear is always the source of truth.** Edit content in Bear, then sync to the repo. Don't edit the markdown files directly — the next sync will overwrite manual changes.

## Repo conventions

- One markdown file per Bear note, named after the note title.
- Folders follow the note's sub-tag: `principles/`, `archicad/`, `tips/`, `protocol/` (`#groundcontrol/archicad` → `archicad/`, etc). Drawing-series notes (A00–Z) sit at the skill root.
- Note attachments (images, PDFs) go in a subfolder named after the note, e.g. `archicad/ArchiCAD fix/`. Image links in the markdown are URL-encoded relative paths.
- Tags appear as a hashtag line at the bottom of each file.
- New notes must be added to `_sidebar.md` (docsify navigation).
- Plugin version lives in **two files, three places**: `.claude-plugin/marketplace.json` (`metadata.version` and `plugins[0].version`) and `plugins/groundcontrol/.claude-plugin/plugin.json` (`version`). Bump all three together — minor bump (1.x.0) for content additions/changes.

## Running an update

1. Edit or create notes in Bear. Tag new notes `#groundcontrol` plus a sub-tag so they land in the right folder.
2. In Claude Cowork, connect the repo folder and ask Claude to update the repository. Claude will:
   - find `#groundcontrol` notes modified since the last sync commit (check `git log` for the date),
   - diff each against its repo file and flag anything ambiguous (dropped table rows, duplicated sections, conflicting edits) before writing,
   - mirror the notes into markdown, copy any new images (see below), update `_sidebar.md`,
   - bump the version, commit, and push.
3. Verify: the docsify site updates within a few minutes of the push; check a changed page renders with its images.

## One-time setup that makes this work

These are already in place; recorded here in case they need to be rebuilt.

**Bear access.** Claude reads note text through the Bear Notes connector. The connector **cannot export attachments**, so Claude also needs folder access to Bear's local attachment store:
`~/Library/Group Containers/9K33E3U3T4.net.shinyfrog.bear/Application Data/Local Files`
Images live under `Note Images/<UUID>/<filename>` — one UUID folder per image. When several notes have an image with the same name (`image.png`), the file's modification date identifies which note it belongs to.

**Git push credentials.** Claude's sandbox can't reach the macOS keychain, so pushes authenticate via a plain-text credentials file at `.git/credentials` (inside the repo's `.git` folder — never committed):

```
https://SpaceagencyArchitects:<fine-grained-PAT>@github.com
```

The token is a GitHub fine-grained personal access token scoped to **this repository only**, with **Contents: Read and write** permission and an expiry date. When it expires, generate a new one (GitHub → Settings → Developer settings → Fine-grained personal access tokens) and rewrite the file. Claude pushes with:

```
git -c credential.helper="store --file=<repo>/.git/credentials" push origin main
```

Commits are authored explicitly since the sandbox has no git identity:

```
git -c user.name="spaceagency" -c user.email="tobias@spaceagency.com.au" commit -m "..."
```

**Docsify site.** `index.html` at the repo root loads docsify from CDN and renders the skill markdown; `.nojekyll` stops GitHub Pages from mangling underscore files. GitHub Pages serves from `main` — no build step, pushes go live automatically.

## After pushing — getting the plugin update to staff

The plugin does not update itself on users' machines:

- **Claude Code (CLI):** run `/plugin marketplace update groundcontrol`.
- **Claude desktop / Cowork:** Customize → Plugins → trigger a sync on the groundcontrol *marketplace* entry (the plugin's own Update button only activates after the marketplace catalog refreshes; syncs can take up to 30 minutes). Restart or start a new conversation to load the new version.
- Plugins installed by manual `.plugin` file upload never see updates — reinstall from the marketplace instead.

## Known gotchas

- The Bear connector's section-replace only swaps content up to the next heading of any level — for restructures, replace the full note body.
- Repo folder is iCloud-synced; if a git operation hits a stale `.git/index.lock` or "Operation not permitted", the lock file may need deleting.
- Publishing note-content PDFs (e.g. GWG_Detailing.pdf) is not part of the sync — large attachments stay in Bear, with the markdown referencing them as "attached to the Bear note".
