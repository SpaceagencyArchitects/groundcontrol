# GROUNDCONTROL — skill authoring conventions

Applies to every skill in this plugin, and to any skill exported for standalone install.

## 1. Keep SKILL.md light
`SKILL.md` holds the trigger `description`, when-to-use, and brief step-by-step guidance only — **target under 500 lines**. Long reference material, templates, code, and boilerplate go in subfolders (below); `SKILL.md` points at them rather than inlining them. Flag any `SKILL.md` over 500 lines for slimming.

## 2. Bundle references in `references/`
Long-form reference content lives in a `references/` subfolder inside the skill: zoning / BAL code checklists, CAD/BIM drafting standards, the GROUNDCONTROL codex pages, source lists. `SKILL.md` references these; it does not reproduce them.

- **groundcontrol codex:** the docsify site publishes the `references/` folder **only**, so the codex is viewable outside Claude. Set `basePath` to `plugins/groundcontrol/skills/groundcontrol/references`.

## 3. Standard subfolders — used where required
Consistent, plural names. No custom variants.

- `references/` — reference docs, checklists, standards (human- and Claude-readable)
- `templates/` — starting-point files the skill fills in (e.g. the transmittal `.xlsx`)
- `assets/` — fonts, logos, images, static resources
- `scripts/` — helper scripts the skill runs
- `rules/` — bundled practice conventions (for standalone / exported skills; in-plugin skills may instead reference the shared `../../rules/`)

## 4. Agent fallback — a skill must run without its agent
Skills must work even when the orchestrating agent isn't loaded (e.g. installed standalone, without the plugin). Where a skill would hand off to an agent, write it as a fallback:

> If the `<agent>` playbook is available at `../../agents/`, follow it. Otherwise, perform these steps directly: …

with the fallback steps inlined. **Agents and the `studio` router stay plugin-only**; every worker skill stands on its own.
