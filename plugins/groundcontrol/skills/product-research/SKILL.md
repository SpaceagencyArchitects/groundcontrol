---
name: product-research
description: FF&E product research — receives a brief from the designer, searches the web for matching products, and returns a curated shortlist as a CSV ready to import into Programa (or any FF&E scheduling tool).
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - WebFetch
  - WebSearch
  - AskUserQuestion
---

# /product-research — Product Research

## Conventions (spA)

Full detail in the plugin's `../../rules/` folder.

- **Metric & Australian English** by default; **WA** context unless stated otherwise.
- **AI-assisted output** supporting the architect's judgment — flag assumptions and anything unverified (`../../rules/professional-disclaimer.md`).

Receives a brief from a designer, researches products across the web, and returns a curated shortlist of candidates. Selected products are written to a local CSV the designer can import into **Programa** (the practice's FF&E system of record) or hand to any scheduling tool.

> **Where this sits:** Programa captures products you've *already found* (web clipper, URL paste) and owns the schedule, procurement, and client approvals. This skill does the part Programa can't — open-ended discovery and curation *from a brief*. Its output is an import-ready CSV, not a live schedule.

## How It Works

```
Designer gives a brief
        ↓
Claude searches the web
        ↓
Presents candidates with specs + reasoning
        ↓
Designer picks winners
        ↓
Written to a CSV → import into Programa
```

## Step 1: Take the Brief

The designer describes what they're looking for. A brief can be loose or specific:

**Loose:** "I need acoustic panels for a tech office lobby"

**Specific:** "Round dining table, 48–54" diameter, solid walnut or oak, steel or brass base, under $3,000, in stock or <6 week lead time"

### What to capture from the brief

Extract as many of these as the designer provides. **Don't ask for fields they didn't mention** — work with what you have: category, use context, style/aesthetic, materials, dimensions, budget, sustainability (GREENGUARD, FSC, Cradle to Cradle, recycled content), lead time, quantity, indoor/outdoor, must-haves (stackable, COM available, weatherproof), and brand preferences/exclusions.

**Don't interview the designer.** If the brief is "acoustic panels for a lobby," that's enough to start searching. Clarify *after* showing initial results if needed.

## Step 2: Research

Search the web for products matching the brief. Use multiple targeted queries to cover different angles — category + material, design-focused, trade/contract, specific brands the designer mentioned, and sustainability if relevant. Run **3–5 searches** depending on brief complexity. Aim for breadth — different price points, brands, styles.

### For each candidate found

Attempt to fetch the product page with WebFetch to extract full specs. If the page is JS-rendered and returns no data, use the search-result snippet + general knowledge, and note specs as "unverified." **Target 6–10 candidates** that genuinely match the brief. Don't pad the list with weak matches.

## Step 3: Present Candidates

Show results as a numbered shortlist with enough detail to evaluate, then a summary table. Lead with the summary table if there are 6+ candidates.

### Presentation rules

- **Include "Why"** for each — why it matches the brief, and flag any compromises.
- **Flag trade-offs honestly** — "veneer not solid", "over budget but worth seeing", "long lead time".
- **Don't oversell** — if a product is a weak match, say so or leave it out.
- **Be opinionated.** The designer wants a knowledgeable research assistant, not a search engine.

## Step 4: Write the import CSV

When the designer picks candidates ("save 1, 3, and 5"), write them to a local CSV ready to import into Programa.

- **Default path:** `./ffe-research-YYYY-MM-DD.csv` (ask if the designer wants a project-specific name).
- **One row per product.** Leave a field blank (empty string) rather than guessing.
- **Header (Programa-friendly, maps cleanly on import):**

```
Category,Brand,Product Name,Designer,SKU,Link,Description,W,D,H,Unit,Materials,Finish,List Price,Currency,Lead Time,Image URL,Tags,Notes,Source
```

- **Notes** — put the "Why" reasoning and any flagged trade-offs here.
- **Tags** — from brief context (e.g. `lobby-reno, walnut`).
- **Source** — `research`.
- **Unit** — the unit for the W/D/H figures (e.g. `mm`, `in`). Keep dimensions in the manufacturer's stated unit; don't convert.

### After writing

```
✓ Wrote 3 products to ffe-research-2026-08-16.csv
  Import into Programa: New schedule → Import → CSV, then map columns.

Want me to refine the search? Different style, budget, or materials?
```

If the designer has a rep PDF price book instead of web products, hand off to `/product-spec-pdf-parser`.

## Step 5 (Optional): Iterate

The designer may refine — "more like #1 but cheaper", "outdoor versions", "any with GREENGUARD?", "compare #1 and #3". Each iteration can append more rows to the CSV.

## Conversation Style

- **Don't over-ask before searching.** A one-line brief is enough to start.
- **Show results, then refine.** It's faster to react to real options than to specify everything upfront.
- **Know the industry.** Reference relevant brands, designers, trade platforms; understand contract vs residential, COM/COL, lead times, certifications.

## Notes

- **JS-rendered product pages** are common (Hem, Muuto, Vitra, etc.). If WebFetch returns no data, use search snippets + general knowledge and note when specs are unverified.
- **The CSV is a hand-off, not a database.** Programa is the system of record once products are imported — this skill's job ends at a clean, import-ready shortlist.
