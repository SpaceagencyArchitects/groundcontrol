---
name: spa-style
description: Apply the spaceagency house style to ANY Word document (.docx) — set the in-house font (KMR Waldenburg), strip bold, capitalise headings, set heading spacing, remove the header rule, clean and re-add heading bookmarks, tidy blank paragraphs, place the practice logo, and fill company details. Use when the user wants to "format this doc to our house style", "apply spaceagency formatting", "brand this document", "make this on-brand", "format this letter/report", or points at a .docx and asks to apply the practice font/logo/style. For NATSPEC specifications specifically, use the `natspec` skill instead (it wraps these same formatters plus spec-only steps).
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

# /spa-style — spaceagency house-style formatter for any docx

Formats **any** Word document to the practice house style in one pass. Unlike the
`natspec` skill (which is specific to NATSPEC specifications), this works on
letters, reports, schedules, briefs — anything in `.docx`. Every parameter lives
in **`spa-style.json`**, so changing the font, spacing or logo is a one-line
edit that then applies to every document.

## What it does

Driven by `spa-style.json`, `scripts/format_docx.py` runs the portable
formatters in order:

1. **Font & weight** — sets **KMR Waldenburg** everywhere (styles, document
   defaults, theme, runs, headers/footers); strips **all bold** (the font is a
   single weight, so faux-bold looks wrong); sets **all-caps headings**.
2. **Paragraphs** — heading spacing (default H1 24/12, H2 18/6, H3 12/6, H4 6/6
   pt) and removes the horizontal **rule across the top of every page** (the
   Header style border).
3. **Bookmarks** — removes clutter bookmarks (keeps TOC anchors) and adds a
   clean named bookmark to each heading for navigation.
4. **Tidy** — collapses runs of blank paragraphs to one and strips the stray
   soft line breaks a Pages/Word round-trip injects.
5. **Logo** — places `assets/logo.png` at a `{{logo}}` token you type where you
   want it (default 3 cm wide), and/or in the page header (`"in_header": true`).
6. **Company** — replaces a `{{company}}` token with the practice details.

## Run it

```bash
# format any document with the saved house style
python scripts/format_docx.py "input.docx" "output.docx"

# use a project-specific parameter file instead of the default
python scripts/format_docx.py "input.docx" "output.docx" --config /path/spa-style.json
```

To include the logo, type `{{logo}}` in the document where it should sit (and
`{{company}}` for the address block); or set `"logo": {"in_header": true}` in
the config to put the logo in the header instead. Install the font once before
rendering a PDF: `cp assets/KMR-Waldenburg-BuchHalbschmal.ttf ~/.fonts/ && fc-cache -f`.

## Individual tools

Each step is also a standalone script under `scripts/` (all import the bundled
`docxlib.py`, so the skill is self-contained):

| Script | Does |
|---|---|
| `apply_font.py in out [font] --no-bold --caps-headings` | font + weight + caps |
| `style_tweaks.py in out --remove-header-line --blank-header --heading Heading3:12:6` | header rule, blank header, heading spacing |
| `remove_bookmarks.py in out --keep-toc` | strip clutter bookmarks |
| `bookmark_headings.py in out [--levels 1,2]` | add named heading bookmarks (by outline level) |
| `collapse_blanks.py in out [--remove-all] [--strip-soft-breaks]` | tidy blank paragraphs / soft breaks |
| `place_logo.py in out --logo assets/logo.png --width-cm 3 [--header]` | logo at `{{logo}}` token / header |

## Parameters (`spa-style.json`)

| Key | Meaning |
|---|---|
| `font` | family name (must match the installed font; default `KMR Waldenburg`) |
| `no_bold`, `caps_headings` | house style toggles |
| `heading_spacing` | `{styleId: [before_pt, after_pt]}` (standard Word style IDs are `Heading1`–`Heading9`) |
| `remove_header_line`, `clean_bookmarks`, `bookmark_headings`, `collapse_blanks`, `strip_soft_breaks` | on/off |
| `logo` | `file`, `width_cm`, `token`, `in_header` |
| `company` | `token`, `name`, `address`, `phone`, `email` |

## Notes & guardrails

- **Headings are matched by style ID / outline level.** Standard Word documents
  use `Heading1`–`Heading9`; a Pages round-trip renames them (`Heading`,
  `Heading 2`, …). `bookmark_headings.py` handles both (it reads outline level);
  for `caps_headings` and `heading_spacing` on a renamed file, add the renamed
  IDs to `heading_spacing` and re-run.
- **Non-destructive to content** — it only changes formatting, bookmarks and
  blank spacing; body text is preserved. Keep the original as a copy.
- **Font must be installed** on the machine that renders the final PDF, or Word/
  LibreOffice substitutes a lookalike.

## Assets
`assets/KMR-Waldenburg-BuchHalbschmal.ttf` (in-house font) ·
`assets/logo.png` (practice logo).
