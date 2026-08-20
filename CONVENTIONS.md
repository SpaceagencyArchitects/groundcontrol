# GROUNDCONTROL — skill authoring conventions

> **Canonical source:** the **GROUNDCONTROL Skill Authoring Guide** lives in the spaceagency `spa_claude` Cowork project (`skill-authoring-guide.md`) and is the authoritative version. This file is a repo-local summary — if the two ever differ, the project guide wins. Keep them in sync when either changes.

Applies to every skill in this plugin, and to any skill exported for standalone install.

1. **Keep SKILL.md light** — triggers + brief guidance only, under 500 lines. Long material moves to subfolders; flag any SKILL.md over 500 lines.

2. **Bundle references in `references/`** — code checklists, drafting standards, codex pages, source lists. For the `groundcontrol` codex, docsify publishes the `references/` folder only, so `basePath` points there.

3. **Standard subfolders, plural names** — `references/`, `templates/`, `assets/`, `scripts/`, `rules/`. No custom variants.

4. **Skills degrade gracefully without the plugin.**
   - **Agents:** where a skill hands off to an agent, write "if the `<agent>` playbook is at `../../agents/`, follow it; otherwise do these steps directly: …". Agents and the `studio` router stay plugin-only.
   - **Rules:** where a skill references the shared `../../rules/` folder, its inline "Conventions (spA)" block carries the load-bearing conventions and states that, when the rules folder isn't present, those inline conventions are authoritative. For full-fidelity standalone packages, bundle a `rules/` copy into the export.
