# CLAUDE.md — GROUNDCONTROL codex

Operating guide for Claude working in this repository. Pair with `README.md`. Hold to the spA posture: **guides, not rules**; **say it once**.

## What this repo is

The GROUNDCONTROL documentation codex, and nothing else. One repo, two outputs:

- **Standalone Claude skill** — `groundcontrol/` (`SKILL.md` + `references/`). Packaged by `scripts/package-skill.sh` into `dist/groundcontrol.zip` for upload. Not a plugin: no manifests, no version files.
- **Docsify site** — `index.html` + `.nojekyll` publish `groundcontrol/references/` at spaceagencyarchitects.github.io/groundcontrol, deploying from `main` on push.

The WA workflow plugin lives in a separate repo (`spa_wa-architect-skills`). Don't add workflow skills, agents, rules or hooks here.

## Golden rules when editing

- **Content lives in `groundcontrol/references/`.** Drawing-series notes (`A00`–`Z`) at its root; topic notes in `principles/`, `archicad/`, `protocol/`, `tips/`. Attachments in `attachments/<note name>/`, referenced by URL-encoded relative path.
- **`SKILL.md` stays light** — triggers, lookup tables, workflows; under 500 lines. Every `references/…` path it names must exist. After any rename or deletion, re-check.
- **Navigation.** Any note added, renamed or removed is also updated in `references/_sidebar.md`.
- **Links.** Docsify relative links, not Obsidian `[[wikilinks]]` or `![[embeds]]`.
- **Voice.** Terse, imperative, say-it-once. Don't restyle the codex into generic prose.

## Committing and pushing

**Only commit or push when Tobias asks.** Push target is `origin main`. If a plain `git push` doesn't authenticate from a sandbox, use a repo-scoped fine-grained PAT in `.git/credentials` (never committed):

```
git -c user.name="spaceagency" -c user.email="tobias@spaceagency.com.au" commit -m "..."
git -c credential.helper="store --file=$(pwd)/.git/credentials" push origin main
```

## After a content change

Push, check the page renders on the site, then rebuild the zip if staff need the update in Claude.
