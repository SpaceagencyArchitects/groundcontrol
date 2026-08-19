# Updating GROUNDCONTROL

How codex content flows to the GitHub Pages site and the Claude plugin — and how to run an update.

## How the pieces fit together

```
this repository                      ← source of truth (the markdown codex)
  plugins/groundcontrol/skills/groundcontrol/references/
        │
        ├──▶ docsify site            spaceagencyarchitects.github.io/groundcontrol
        │    (index.html renders the markdown; updates automatically on push)
        │
        └──▶ Claude plugin           installed by staff via the plugin marketplace
             (marketplace.json / plugin.json define the version)
```

**The markdown files in this repo are authoritative.** Edit them directly — with Claude or in an editor like VS Code — then bump the version, commit, and push.

> The codex was previously mirrored *out of* Bear notes tagged `#groundcontrol`, with Bear as the source of truth. That flow is retired: the repo is now authoritative and Bear is no longer part of the pipeline. Edit here, not in Bear.

## Repo conventions

- One markdown file per codex note, named after the note title.
- Codex content lives in `references/`. Folders follow topic: `references/principles/`, `references/archicad/`, `references/tips/`, `references/protocol/`. Drawing-series notes (A00–Z) sit at the `references/` root. (`SKILL.md` stays at the skill root and light.)
- Note attachments (images, PDFs) go in a subfolder named after the note, e.g. `archicad/ArchiCAD fix/`. Image links in the markdown are URL-encoded relative paths.
- Files carry a hashtag tag line at the bottom (a convention retained from the codex's origins) — keep it for consistency.
- New notes must be added to `references/_sidebar.md` (docsify navigation).
- Plugin version lives in **two files, three places**: `.claude-plugin/marketplace.json` (`metadata.version` and `plugins[0].version`) and `plugins/groundcontrol/.claude-plugin/plugin.json` (`version`). Bump all three together — minor bump (1.x.0) for content additions/changes.

## Running an update

1. **Edit the markdown** in `plugins/groundcontrol/skills/groundcontrol/references/`. With Claude: connect the repo folder in Cowork (or run Claude Code in it) and describe the change — Claude edits the files applying the codex conventions. A new note goes in the right folder and into `references/_sidebar.md`; a new lookup category also gets a row in the skill-root `SKILL.md`. New images go in the note's attachment subfolder, referenced by URL-encoded relative path.
2. **Bump the version** (three places, above).
3. **Validate**: `claude plugin validate .` from the repo root.
4. **Commit and push** to `main`.
5. **Verify**: the docsify site updates within a few minutes of the push; check a changed page renders with its images.

## Publish setup

These are already in place; recorded here in case they need to be rebuilt.

**Git push credentials.** When you edit and push on your own Mac (this repo lives at `~/Developer/groundcontrol`, outside iCloud), a plain `git push` authenticates via the macOS keychain or `gh` — nothing special needed. If Claude ever pushes from a sandbox that can't reach the keychain, authenticate via a plain-text credentials file at `.git/credentials` (inside the repo's `.git` folder — never committed):

```
https://SpaceagencyArchitects:<fine-grained-PAT>@github.com
```

The token is a GitHub fine-grained personal access token scoped to **this repository only**, with **Contents: Read and write** permission and an expiry date. When it expires, generate a new one (GitHub → Settings → Developer settings → Fine-grained personal access tokens) and rewrite the file. Push with:

```
git -c credential.helper="store --file=<repo>/.git/credentials" push origin main
```

Sandbox commits are authored explicitly since that environment has no git identity:

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

- The repo now lives at `~/Developer/groundcontrol`, outside iCloud, so git operates on plain local files — no offloaded-stub or stale `.git/index.lock` issues. If you ever move it back under iCloud Drive or the Desktop/Documents folders, beware both.
- Large attachments (e.g. big detailing PDFs) live in the note's attachment subfolder in the repo and are served directly by GitHub Pages — keep file sizes reasonable.
