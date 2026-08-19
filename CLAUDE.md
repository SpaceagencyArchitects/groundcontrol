# CLAUDE.md — GROUNDCONTROL

Operating guide for Claude working in this repository. Pair it with `README.md` (overview + install) and `UPDATING.md` (detailed procedures). Hold to the spA documentation posture throughout: **guides, not rules**, and **say it once**.

## What this repo is

GROUNDCONTROL is spaceagency's construction-documentation codex — the practice reference for what information goes where in a drawing set. The repo does three jobs at once:

- **Claude Code plugin** — staff install it via the marketplace; `.claude-plugin/marketplace.json` and `plugins/groundcontrol/.claude-plugin/plugin.json` define it.
- **The skill** — `plugins/groundcontrol/skills/groundcontrol/` holds `SKILL.md` (entry point, lookup tables, workflows) at the skill root, and the codex content under `references/`: drawing series `A00`–`Z`, plus `references/principles/`, `references/archicad/`, `references/protocol/`, `references/tips/`.
- **Docsify site** — `index.html` + `.nojekyll` publish the same markdown at spaceagencyarchitects.github.io/groundcontrol, auto-deploying from `main` on every push.

## Source of truth — read this first

**This repository is now the source of truth for the codex.** Edit the markdown files here directly (Claude, or VS Code by hand). The codex used to be mirrored *out of* Bear `#groundcontrol` notes; that flow has been inverted — the Bear notes are retired and Bear is now the personal-vault only.

> Note: `README.md` and `UPDATING.md` still describe the old "Bear is always the source of truth" sync and are pending revision. Where they say to edit in Bear and mirror out, that is superseded — treat the repo as authoritative. Their *mechanical* guidance (folder conventions, version bumping, docsify, push credentials) still holds.

## Golden rules when editing

- **Content lives in** `plugins/groundcontrol/skills/groundcontrol/references/`. Drawing-series notes (`A00`–`Z`) sit at the `references/` root; topic notes go in `references/principles/`, `references/archicad/`, `references/protocol/`, or `references/tips/`. `SKILL.md` stays at the skill root and light (triggers, lookups, workflows — under 500 lines). Attachments go in a subfolder named after the note and are referenced by URL-encoded relative path.
- **Voice.** Write notes, labels, and annotations in the spA voice the skill teaches — terse, imperative, say-it-once. Don't restyle the codex into generic prose.
- **Navigation.** Any codex file you add, rename, or remove must also be updated in `references/_sidebar.md` (docsify nav).
- **Lookup tables.** A new component, sheet, or category also needs a row in the lookup tables in `SKILL.md`.
- **Version bump.** Any content change bumps the version in **three places** — `metadata.version` and `plugins[0].version` in `.claude-plugin/marketplace.json`, and `version` in `plugins/groundcontrol/.claude-plugin/plugin.json`. Minor bump (`1.x.0`) for content additions/changes; keep all three identical.
- **Validate** before pushing: `claude plugin validate .` from the repo root.

## Committing and pushing

Push target is `origin main`; GitHub Pages / docsify deploy automatically. This repo now lives under `~/Developer/` (outside iCloud), so the old iCloud `.git/index.lock` gotcha in `UPDATING.md` no longer applies.

**Only commit or push when Tobias asks.** When you do, commits need an explicit identity and pushes authenticate per `UPDATING.md` (a repo-scoped fine-grained PAT in `.git/credentials`, never committed):

```
git -c user.name="spaceagency" -c user.email="tobias@spaceagency.com.au" commit -m "..."
git -c credential.helper="store --file=$(pwd)/.git/credentials" push origin main
```

If a plain `git push` already authenticates (macOS keychain / `gh` on this machine), prefer that.

## After a content change

Bump the version, commit, push. The docsify site refreshes within a few minutes — verify a changed page renders, images included. Staff pick up the new plugin version with `/plugin marketplace update groundcontrol`.

## Skill authoring conventions

Full detail in [CONVENTIONS.md](CONVENTIONS.md). In short, every skill in this plugin — and any skill exported for standalone install — follows:

1. **Light SKILL.md** — triggers + brief guidance only, under 500 lines. Long material moves to subfolders; flag any SKILL.md over 500 lines.
2. **`references/`** — bundled reference material (code checklists, drafting standards, codex pages, source lists). For the `groundcontrol` codex, docsify publishes the `references/` folder only, so `basePath` points there.
3. **Standard subfolders, plural names** — `references/`, `templates/`, `assets/`, `scripts/`, `rules/`. No custom variants.
4. **Agent fallback** — a skill must run without its agent. Where a skill hands off to an agent, write "if the `<agent>` playbook is at `../../agents/`, follow it; otherwise do these steps directly: …". Agents and the `studio` router stay plugin-only; every worker skill stands alone.
