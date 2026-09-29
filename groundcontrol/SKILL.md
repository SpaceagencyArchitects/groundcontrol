---
name: groundcontrol
description: spaceagency's documentation codex (GROUNDCONTROL) — the practice's reference for what information goes where in an architectural construction documentation set. Use this skill whenever a spA architect asks about construction documentation, drawing set structure, sheet numbering (A00, A10, A20, A30, A40, A50, A60, A65, A68, A70, A80, Z), drawing series, where to document a building component (doors, windows, walls, ceilings, floors, joinery, FFE, finishes, partitions, metalwork, roofing, stairs, lifts, signage, wet areas, wall protection, demolition, landscaping, external works), how to set up a documentation storyboard, ArchiCAD detail workflows (WF50 — draw 2D details, model-based detail with viewpoint, drawn independent detail, drawn copy with source marker), keynotes and element tagging, classification and properties, hotlink attribute management, the SpA Alphabet, sheet types, scales (1:500, 1:250, 1:100, 1:50, 1:25, 1:20, 1:10, 1:5), legend sheets, finishes codes, paint system coding (PT/C codes), allocation of information, "say it once" principle, annotation conventions, dimensioning rules, drafting principles, drawing graphics, referencing, schedules (door, window, room, finishes, FFE), specifications, or how to write notes/labels in the spA voice. Also use whenever a user mentions GROUNDCONTROL, the spaceagency documentation codex, or asks for help with a CD set, working drawings, contract documents, or a documentation review/audit. The skill provides quick lookups (component → sheets, sheet → contents), guided workflows (set up a new project's documentation, place a component, choose a detail strategy, write/audit annotations, run a pre-issue checklist), and access to the full reference codex via the bundled markdown files.
---

# GROUNDCONTROL — spaceagency's documentation codex

This skill gives you (Claude) access to spaceagency id architects' documentation reference. It is used by spA staff to guide construction documentation: deciding where information belongs, how to set up a drawing set, how to write annotations, and which ArchiCAD workflow to use for a given task.

Treat the codex as a **set of guides, not rules**. Adjustments to suit a particular project are inevitable. Departures from the spA format are the project leader's decision. When asked for guidance, give the spA convention as the default, but acknowledge where a project may justifiably depart from it.

---

## How to use this skill

1. **Read the user's question carefully and route to the right mode.** Most questions fall into one of these:

   - **Lookup — component:** "Where do I document doors?" / "Where do wall finishes belong?" → use the **Component → Sheets map** below. If more depth is needed, read the Allocation Table in `references/principles/Allocation of Information.md`, then the A-series notes it points to.
   - **Lookup — sheet:** "What goes on A50?" / "What's on a roof plan?" → use the **Drawing series at a glance** below. For full content, read `references/A<NN> - <Title>.md`.
   - **Lookup — principle:** "How should I dimension this?" / "What font size?" → read the relevant file in `references/principles/`.
   - **Workflow — start a project's documentation:** → run **Workflow A: Documentation setup** below.
   - **Workflow — choose a detail strategy:** → run **Workflow B: Detail strategy chooser** below; final answer points to a method in `references/archicad/WF50 Details.md`.
   - **Workflow — describe an item / write an annotation / write a schedule line:** → run **Workflow C: Write in spA voice**.
   - **Workflow — pre-issue review / checklist:** → run **Workflow D: Pre-issue review**, drawing on `references/tips/spA documentation  tips.md`.
   - **General study / browsing:** point them to `references/✱ SpA GROUNDCONTROL.md` (the index) and offer to walk through a section.

2. **Don't dump entire files.** Pull the relevant slice. spA architects are time-poor; they want the answer, not a recital. Quote the codex only where wording matters (e.g. when explaining a rule).

3. **Cross-reference, don't duplicate.** If door information lives across A10, A20, A70, A50 and Z, say so explicitly with the sheet codes — that mirrors how the codex itself is structured.

4. **Match the spA voice in any drafting you do.** See the **Voice for drafted output** section at the bottom.

5. **When in doubt, read the file.** The summaries below are for fast routing only. For anything beyond a one-line answer, open the underlying markdown.

---

## Core principles (compressed)

These are the load-bearing ideas. If you forget everything else, hold onto these.

- **Say it once.** Every piece of information appears in one agreed place — a drawing or a schedule — and is not repeated. Do not write `AS SPECIFIED`, `AS SCHEDULED`, or `REFER TO ENGINEERS DETAILS`. They are redundant and hazardous. Source: `references/principles/Allocation of Information.md`, `references/principles/Introduction to Construction Documentation.md` (How to Annotate).

- **Drawings, schedules, specifications are three different things.** Drawings show graphic + dimensional design. Schedules ('assembly of elements' types — doors, rooms — are in the drawing set; 'building elements' types — finishes, FFE, specification schedules — are appended to the spec). Specifications cover written technical and non-technical requirements.

- **Sheet numbering is `A<TT><SS>.<NN>`** — Discipline (always `A` for spA), Sheet Type (00 General, 10 Plans, 20 Elevations, 30 Sections, 40 Large-Scale Drawings, 50 Details, 60 Room Layouts, 70 Door/Window Schedules, 80 Finishes Schedules, 90 3D), Sequence Number (01–99, non-sequential — leave gaps). Source: `references/principles/Sheet Numbering.md`.

- **Storyboard before drafting.** Decide paper size first (must stay consistent across the set). Build a general storyboard from the SpA Alphabet, then component-specific storyboards inside it. Source: `references/principles/Allocation of Information.md` (Allocation Table — use for storyboarding at project start).

- **Drafting philosophy:** describe outcomes, not methods. Don't replicate proprietary system details. Resolve junctions off-line first, then decide if they need to be in the set. Use technical diagrams, not pictures. Source: `references/principles/Introduction to Construction Documentation.md` (How to Draft).

- **Annotation grammar:** generic name → systems/materials code → finish descriptor → finishes code. (e.g. `CLADDING EWS-3, PAINTED PT-4`). Use active voice, command form, no abbreviations except those listed on the legend sheet. Source: `references/principles/Introduction to Construction Documentation.md` (How to Annotate), `references/principles/Abbreviations and Codes.md`.

- **Minimum text size 2.0 mm at full size.** Detail titles 3.5 mm. Text is horizontal or rotated 90° counterclockwise — never anything else. Source: `references/principles/Introduction to Construction Documentation.md` (How to Annotate).

---

## Drawing series at a glance

Use this as a quick lookup. For full content of any sheet, open `references/A<NN> - <Title>.md`.

| Series | Range       | Subseries                   | Purpose                                               | Typical scales      |
|--------|-------------|-----------------------------|-------------------------------------------------------|---------------------|
| A00    | A000–A099   | A00, A01                    | Cover, legend                                          | n/a, 1:500, 1:250   |
| A02    | A020–A029   |                             | Demolition                                            | 1:100, 1:50, 1:20   |
| A10    | A100–A149   | A10.## (level), A11.##.## (level.sequence) | Floor + roof plans                          | 1:100               |
| A12    |             |                             | Concrete + waterproofing plans                        | 1:100               |
| A14    |             |                             | Reflected ceiling plans                               | 1:100               |
| A16    |             |                             | Lighting + power plans                                | 1:100               |
| A20    |             |                             | External elevations                                   | 1:100               |
| A30    |             |                             | Sections                                              | 1:100               |
| A40    |             |                             | Cores, stairs, lifts (large-scale plans/elevs/sections — **not** details) | 1:50, 1:25 |
| A45    |             |                             | Metalwork, external works                             | 1:50, 1:25          |
| A50    | A501–A599   | A50.## (plan), A55.## (section) | Interface details                                  | 1:10, 1:5           |
| A60    |             |                             | Internal spaces (room layouts)                        | 1:50                |
| A65    |             |                             | Joinery                                               | 1:20, 1:5           |
| A68    |             |                             | FFE                                                   | varies              |
| A70    | A701–A799   | A71.## (doors), A72.## (windows) | Doors + windows (type elevs + schedule + 1:5 details) | 1:50, 1:5      |
| A75    |             |                             | Generic door details                                  | 1:10, 1:5           |
| A80    |             |                             | Schedules (room/finishes, colour, etc.)               | n/a                 |
| Z      |             |                             | Specifications                                        | n/a                 |

---

## Component → Sheets map

When asked "where does X go?", give the spread of sheets in this order: legend → plans/elevations → schedules → details → spec. Then offer to read the Allocation Table (`references/principles/Allocation of Information.md`) and the relevant A-series notes for the full breakdown. Standalone component notes were retired in June 2026; their content now lives in the Allocation Table and the series notes.

| Component                       | Appears on                                                                  |
|---------------------------------|-----------------------------------------------------------------------------|
| Ceilings                        | A01 legend, A14 RCPs, A60 room layouts, A50 interface details, Z spec |
| Concrete + waterproofing        | A12, A50 details, Z spec |
| Demolition                      | A02 demolition plans/elevs, Z spec |
| Doors                           | A01 legend, A10 plans, A20 ext elevations, A70 door schedule + 1:5 details, A50 special interfaces, Z spec |
| External wall systems           | A01 legend, A20 elevs, A30 sections, A50 details, Z spec |
| Floors                          | A10 plans, A50 interface details, Z spec; finishes in A80 room schedule |
| Furniture                       | A68 FFE, A60 room layouts, FFE schedule appended to spec |
| Joinery                         | A10 plans (codes), A60 room layouts, A65 joinery details, Z spec |
| Landscaping + external works    | A45, Z spec |
| Lifts                           | A10 plans, A40 cores/stairs/lifts, Z spec |
| Metalwork                       | A10 plans (codes), A45 metalwork, A50 details, Z spec |
| Paint finishes                  | A01 legend (PT and C codes), A80 colour schedule (C codes), Z spec (PT systems); annotated as `PT1/C4`. Coding: `references/archicad/Tagging of Elements in ArchiCAD.md` |
| Partitions                      | A10 plans (types + setting-out), A50 details, Z spec |
| Roof + roofing systems          | A10 roof plans, A20 elevs, A50 details, Z spec |
| Signage                         | A10 plans (free-standing + wall-hung wayfinding), A70 (statutory door signs), A80 (wayfinding schedule) |
| Stairs                          | A10 plans, A40 cores/stairs/lifts, Z spec |
| Wall finishes                   | A01 legend, A80 room schedule (codes), A60 for complex spaces, Z spec |
| Wall protection                 | A60 room layouts, Z spec |
| Wet areas                       | A10 plans (setdown), A60 room layouts, A50 setdown detail, Z spec |
| Windows                         | A01 legend, A20 ext elevations, A70 window schedule + 1:5 details, A50 special interfaces, Z spec |

---

## ArchiCAD reference (quick map)

| Topic                          | File                                                      | Use when…                                                            |
|--------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|
| Toolbox sessions               | `references/archicad/ArchiCAD Toolbox sessions.md`                   | onboarding / general practice technique                              |
| Tagging of elements + keynotes | `references/archicad/Tagging of Elements in ArchiCAD.md`             | keynote set-up, element codes, PT/C paint coding, what shows on which sheet |
| Classification + properties    | `references/archicad/Classification and Properties.md`               | tagging elements for schedules + filtering                           |
| Layouts + drawings             | `references/archicad/ArchiCAD layouts and drawings.md`               | layout book and drawing set-up                                       |
| Revisions, issues, transmittals | `references/archicad/Revisions, Issues and Transmittals.md`         | revision and issue management                                        |
| Hotlink attribute management   | `references/archicad/Hotlink Attribute Management.md`                | working across hotlinked files; behaviour is **automatic + name-based**, no user toggle |
| ArchiCAD fix                   | `references/archicad/ArchiCAD fix.md`                                | troubleshooting                                                      |
| MRH drawing review             | `references/archicad/MRH drawing review.md`                          | drawing review process                                               |
| WF50 — detail workflows        | `references/archicad/WF50 Details.md`                                | choosing a detail method. Preferred: **1. Draw 2D details**, **2. Model based detail with viewpoint**. Other methods (drawn independent, drawn copy with source marker, standard/external details) noted briefly |
| WF50 — numbering + layout      | `references/archicad/WF50 Details.md` (Numbering Details and Layout Techniques) | detail IDs/names set in the Project Map only; sheet composition for detail layouts |

---

## Workflows

### Workflow A — Documentation setup (new project)

Run when a project leader is setting up the CD documentation for a new project. Walk through the steps in order. Don't skip ahead — confirm each step before continuing.

1. **Confirm paper size.** Ask: what's the building footprint, and at 1:100 what paper size accommodates the GA plan? A1 is the spA default unless the building is unusually small or large. Lock this in — paper size **must remain consistent across the set**.
2. **Build the general storyboard.** Walk through the SpA Alphabet (A00, A02, A10, A12, A14, A16, A20, A30, A40, A45, A50, A60, A65, A68, A70, A80, Z), and for each, decide:
   - Is it required for this project? (A02 demolition only on adaptive reuse; A40 only if cores are non-trivial; etc.)
   - How many sheets per series? Reserve sequence numbers with gaps.
   - Note any project-specific subseries (e.g. A11.##.## if levels split into sectors).
3. **Identify component leads.** For larger projects, name a coordinating architect for each major building component and ask them to produce a component-specific storyboard within the framework.
4. **Set up legend sheet (A01) early.** It anchors all subsequent annotation. Stub in placeholders for: drawing list, key to symbols, key to common graphics, materials/systems/finishes codes.
5. **Set up the ArchiCAD template.** Default layout in the current spA template is the storyboard's starting point. Confirm layer combinations, view templates, pen sets are appropriate.
6. **Plan consultant input management.** Identify which consultants feed which sheets. Plan how their drawings will be reviewed and incorporated. Do **not** repeat their information (column sizes, purlin layouts, etc.).
7. **Output the storyboard as a deliverable.** Drawing numbers, drawing titles, layouts within each sheet (down to 1:20 scale). Sheets of 1:5 details are numbered and inserted but not laid out at the storyboard stage.

Source: `references/principles/Allocation of Information.md` (Allocation Table), `references/principles/Sheet Numbering.md`. The standalone storyboarding note was retired in June 2026 — steps 1–7 are the retained summary; flag to the user that there is no longer a full codex page behind them.

### Workflow B — Detail strategy chooser

Run when a user is deciding how to draw a detail in ArchiCAD. Ask:

1. **What scale?** 1:20, or 1:5?
2. **Project-specific or office-standard?** Will this detail vary by project, or is it a re-used office detail?
3. **Live link to model wanted?** Do you need the detail to update if the model changes?
4. **Modelling level?** Is the relevant area of the model fully modelled to detail level, or basic?
5. **Variations of the same detail?** (e.g. same wall, three different floor finishes)

Then recommend (per `references/archicad/WF50 Details.md` — spA prefers methods 1 and 2):

- **1:20 first-level detail + model developed to detail at junctions + want live link / BIMx position → 2. Model based detail with viewpoint.** Make changes in the source view only; rebuild after every change.
- **Complex junctions modelling won't resolve, less-detailed model, or standard/typical details unlikely to change → 1. Draw 2D details** (all details for a story or section drawn together on one detail). Also the usual answer for the 1:5 level.
- **Reusable office detail, one viewpoint per detail → Drawn Independent Detail** (other method — short note only).
- **Variations of the same base condition (e.g. same junction, different floor finishes) → Drawn Copy of Detail with Source Marker.** Use only for variations — it breaks the live link and BIMx position.
- **Manufacturer or proprietary details → Standard Detailing and External Details;** check the spA standard detail library first.

Read the relevant section of `references/archicad/WF50 Details.md` and walk the user through its steps, when-to-use and limitations. For other methods, the codex gives short notes only — full guidance is the Graphisoft reference (GWG_Detailing.pdf).

### Workflow C — Write in spA voice

Run when asked to draft an annotation, drawing note, schedule line, or specification fragment. Apply these rules without exception:

1. **Grammar:** generic name → system/material code → finish descriptor → finishes code. e.g. `CLADDING EWS-3, PAINTED PT-4`.
2. **Active voice + command form.** `PAINT TO MATCH EXISTING`, not `TO BE PAINTED TO MATCH EXISTING`.
3. **Speak directly to the contractor.** `REMOVE WINDOW FRAMES AND MAKE GOOD OPENINGS`, not `WINDOW FRAMES TO BE REMOVED…BY DEMOLITION CONTRACTOR`.
4. **Action verbs over abstract nouns.** `USE`, `ALIGN`, `AVOID`, `PROTECT` — not `UTILISATION`, `ALIGNMENT`, `AVOIDANCE`, `PROTECTION`.
5. **No double negatives.** `INSTALL APPROVED SYSTEM`, not `DO NOT INSTALL UNLESS APPROVED`.
6. **No `AS SPECIFIED` / `AS SCHEDULED` / `REFER TO ENGINEERS DETAILS`.** They are redundant and hazardous.
7. **Abbreviations only if on the legend sheet.**
8. **One expression, one simple meaning.** Short, clear, direct sentences.

For schedule lines (especially door hardware): describe **what it does, what it looks like, how it's operated, what it interfaces with**. Example: `Mortice latch and deadbolt, lever handle operation, keyed to corridor side, thumb turn to room side, free egress at all times.` Final hardware coding is the specialist supplier's job — too much detail creates unintended specification liability; too little creates RFIs.

Rule of thumb: **if a competent hardware consultant can code it correctly without calling you, you've given the right amount of detail.**

Source: `references/principles/Introduction to Construction Documentation.md` (How to Annotate), `references/A70 - Doors and Windows.md`.

### Workflow D — Pre-issue review

Run when asked to audit a drawing set or a sheet before issue.

1. **Allocation check.** For every piece of information on the sheet, ask: is this the agreed place for it, or is it duplicated elsewhere? If duplicated, decide which version is authoritative and remove the other.
2. **Schedule vs drawing vs spec.** Check that 'building elements' schedules (finishes, FFE, spec schedules) are appended to Z, and 'assembly of elements' schedules (doors, rooms) are in the drawing set.
3. **Annotation pass.** Run the **Workflow C** rules across all notes. Flag every `AS SPECIFIED`, every passive voice, every abbreviation not on A01.
4. **Sheet numbering pass.** Are numbers consistent with `references/principles/Sheet Numbering.md`? Are there gaps left for additions?
5. **Apply the spA tips checklist.** Read `references/tips/spA documentation  tips.md` and run each item against the sheet:
   - Wet area setdown detail with dimension on room layouts (or referenced)?
   - Top-of-rammed-earth treatment (if applicable)?
   - Fixtures, fittings, finishes listed on room layout sheet with reference to spec/schedule?
   - Generic labels for electrical items on arch plans (LSP, DGPO, WL) — full codes only on electrical drawings?
6. **Cross-reference integrity.** Pick three random references on the sheet and chase them — does the referenced detail/section/elevation exist and contain the expected content?

---

## Voice for drafted output

When drafting any spA-facing material in this skill (notes, schedules, briefing language, file headers, even instructions in templates), default to:

- **Direct.** No softeners, no hedging.
- **Spare.** Cut anything that doesn't carry information.
- **Active + command form.**
- **No corporate jargon.** No "leverage", "synergies", "best-in-class", "going forward".
- **No AI tells.** No "let me know if you'd like…", no "I'd be happy to…", no excessive bullet stacks.
- **Codex-aware.** If the codex has a convention, follow it. If you're departing from one, flag it explicitly.

When the staff member is brainstorming or thinking through an unresolved question, switch to a discursive, sentence-form register — but stay direct.

---

## Files in this skill

- `references/✱ SpA GROUNDCONTROL.md` — index, includes all wiki-links between entries
- `references/_sidebar.md` — docsify navigation; the full file list
- `references/A00 - Introductory documents.md` through `references/A80 - Schedules.md` — drawing series content lists
- `references/Z - Specifications.md` — specification structure
- `references/principles/` — introduction to construction documentation (how to draft, how to annotate, revisions), allocation of information (incl. the component Allocation Table), sheet numbering, abbreviations and codes, referencing, dimensioning
- `references/archicad/` — ArchiCAD workflows: tagging of elements + keynotes, classification and properties, layouts and drawings, revisions/issues/transmittals, hotlinks, WF50 detail workflows, toolbox sessions, fixes
- `references/protocol/` — AI usage policy
- `references/tips/` — documentation tips checklist and FFE guide

When uncertain, **read the file**. Don't invent conventions that aren't in the codex.

---

#groundcontrol #spaceagency
