---
name: transmittal
description: Build or update a spaceagency architectural drawing issue register / transmittal (xlsx) from a project's issue folders. Use when the user wants to produce, update, or rebuild a transmittal or drawing issue register, issue a drawing set, record who received which revision when, or reconstruct the issue history from the document folder. Triggers include "transmittal", "drawing issue register", "issue register", "DIR", "issue the set", "update the register", "build the register from the folder", "who got which revision".
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
user-invocable: true
---

# /transmittal — Drawing Issue Register & Transmittal

Builds the practice's **architectural drawing issue register / transmittal** as an Excel sheet: one row per drawing, one column per issue date, the revision issued at each date in the cell, in the spA template (black & white, KMR Waldenburg Buch Halbschmal). It reconstructs the whole history from the project's issue folders, so it can bootstrap a register for an existing project and re-generate it after every issue.

This is the record-and-document layer. It does **not** move or archive files — that stays with the Finder shortcut (see GROUNDCONTROL → *Revisions, Issues and Transmittals*). This skill reads the folders and writes the register; it never moves drawings.

## Conventions (spA)

- **Black & white only**, **KMR Waldenburg Buch Halbschmal** throughout, metric / Australian English. Match the template in `assets/transmittal-template.xlsx`.
- **Records-critical output.** A transmittal is a contractual record — verify the register against the drawings before it is issued, and never overstate: flag anything uncertain (missing revs, drawings not found) rather than guessing.

## When to use

- "Build / update the transmittal for <project>." (routine, after an issue)
- "Rebuild the drawing issue register from the folder." (bootstrap an existing project)
- "Who got revision X of sheet Y / what was issued on <date>?"

## Folder & filename convention

```
<PROJECT_ROOT>/                                  e.g. (2101) MARGARET RIVER HOTEL
  __CURRENT DOCUMENTS/
    ARCHITECT/                                   the discipline (only ARCHITECT for the spA transmittal)
      A0 Site/ A1 Plans/ … A9 External Works/    series folders — current PDFs
        _archive/                                superseded PDFs
  <YYMMDD>_<description>/                         one dated folder per issue (the description is ignored)
    <files issued at that date>  +  <YYMMDD>_TRANSMITTAL.pdf
```

- **Filename:** `<DrawingNo>_<Rev> <Name>.pdf` — e.g. `A000_07 COVER.pdf`. The revision is the token between the first `_` and the first space; the name may itself contain underscores.
- **Revision ID:** a 1–3 character alphanumeric (`07`, `A`, `C1`).
- **Missing revision in a filename is a user error** — flag it (see below); the ID and history are on the drawing (current rev + date bottom-right; revision history on the titleblock). Extract the correct ID, correct the filename, and record it.
- **`DELETED` sheets** (name is `DELETED`) are excluded from the register.

## Workflow

The register is fully derivable from the folders, so **"update after an issue" and "build from scratch" are the same operation** — re-scan the folder. There is no separate stored state to append to.

1. **Locate the project root** (the issue folder on OneDrive). Ask if not given.
2. **Scan** — run `scripts/scan_issues.py`:
   ```
   python3 scripts/scan_issues.py "<PROJECT_ROOT>" --discipline ARCHITECT --out scan.json
   ```
   Stdlib only — run it wherever the folder is reachable (on the device via the file bridge). It walks `__CURRENT DOCUMENTS/ARCHITECT` for the current set and each `<YYMMDD>_…` folder for the issue history, and lists any filenames missing a revision ID.
3. **Build** — run `scripts/build_transmittal.py` (needs `openpyxl`; `pip install openpyxl` if missing):
   ```
   python3 scripts/build_transmittal.py --data scan.json --out "<PROJECT_ROOT>/__CURRENT DOCUMENTS/ARCHITECT/_document register/<no>_<title>_Transmittal.xlsx"
   ```
   It reproduces the spA template layout from `assets/transmittal-template.xlsx`: header block, Current Rev column, one dated column per issue, series bands, and the Distribution / Method-of-Issue / Purpose-of-Issue / Issued-by rows. A **Notes** tab lists any flagged files.
4. **Write output to the discipline's `_document register/` folder** (as above) — that is the register's home.
5. **Report the flags** — the missing-revision filenames (to correct at source) and any drawing that was issued but is not in the current set (possibly superseded or renamed).

## What this skill does NOT do

- **It does not move, copy, or archive files** — the Finder shortcut owns that (deterministic, auditable). This skill only reads folders and writes the register xlsx.
- **Revision notes** (the per-revision descriptions) are not yet auto-populated: they live on the titleblock revision history. Adding them means reading each drawing's titleblock (a heavier pass) or taking them from the ArchiCAD change descriptions at issue time — offer this as a follow-on, don't fabricate them.

## Manual fields

The generated sheet leaves these for the issuer to complete: **To / Attn / Distribution / Method of Issue / Purpose of Issue / Issued by**, and the spA logo at top-left.

See also: GROUNDCONTROL → *Revisions, Issues and Transmittals* (how changes are marked and issued in ArchiCAD) and *A00 — Introductory documents* (the drawing list on A01).
