---
name: product-spec-pdf-parser
description: Extract structured FF&E product specs from PDF files — price books, fact sheets, and spec sheets — into a CSV ready to import into Programa (or any FF&E scheduling tool). Claude reads PyMuPDF-extracted text and structures products into rows.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
---

# /product-spec-pdf-parser — PDF Product Spec Parser

## Conventions (spA)

Full detail in the plugin's `../../rules/` folder.

- **Metric & Australian English** by default; **WA** context unless stated otherwise.
- **AI-assisted output** supporting the architect's judgment — flag assumptions and anything unverified (`../../rules/professional-disclaimer.md`).

Extract structured FF&E data from product PDFs — price books, fact sheets, configurator sheets, spec sheets. Uses PyMuPDF for text extraction and Claude's reasoning to parse wildly varying layouts into a standardized CSV.

> **Where this sits:** Programa imports CSV/Excel and captures products from the web, but it does not parse arbitrary rep **PDF price books**. This skill fills that gap — it turns messy PDFs into a clean CSV you import into Programa.

## Input

The user provides PDFs as file path(s), a folder (all `.pdf` files), or nothing (then ask). Also confirm **variant depth**: `expand` (one row per variant/SKU, default — best for procurement) or `summarize` (one row per product, variants comma-separated).

## Output

A local CSV ready to import into Programa. Default path: `./ffe-pdf-parse-YYYY-MM-DD.csv`. Same header as `/product-research`, so shortlists and PDF extracts import the same way:

```
Category,Brand,Product Name,Designer,SKU,Link,Description,W,D,H,Unit,Materials,Finish,List Price,Currency,Lead Time,Image URL,Tags,Notes,Source
```

Field notes:
- **Source** — `pdf-parser`. **Link / Image URL** — usually blank (no URL in a PDF).
- **Unit** — the unit for W/D/H as stated in the PDF; don't convert.
- **Notes** — carry PDF-only fields with `|` delimiters, e.g. `Variant: Diamond, Black | Price adder: +$130 (PostureFit SL) | Origin: Sweden | Source: alphabeta-fact-sheet.pdf`.

## Variant Handling

- **Fact sheets with SKUs** (e.g. Alphabeta lamp) — one row per SKU (shade shape × colour); Product Name repeats, Variant distinguishes.
- **Fact sheets with upholstery/finish combos** (e.g. Puffy chair) — one row per upholstery option; frame finish in Finish. Distinct products (chair + ottoman) each get their own rows.
- **Price books / configurators** (e.g. Aeron) — one row per distinct product type; base config in main fields, add-on costs noted as a price adder in Notes. Do NOT explode every permutation.
- **expand vs summarize** — expand = one row per variant/SKU; summarize = one row per product with comma-separated variants.

## Workflow

### Step 1: Get input
Identify PDF file(s) and confirm variant depth (default `expand`). If given a folder, list `.pdf` files and report the count.

### Step 2: Extract text (PyMuPDF)
Run via Bash:

```python
import fitz, sys, json
pdf_path = sys.argv[1]
doc = fitz.open(pdf_path)
pages = [{"page": i + 1, "text": p.get_text()} for i, p in enumerate(doc)]
doc.close()
print(json.dumps({"filename": pdf_path.split("/")[-1], "total_pages": len(pages), "pages": pages}))
```

### Step 3: Parse products with Claude
Read the extracted text and structure it. For ≤20 pages, process at once; for larger, process in 10-page chunks, carry forward context (brand, ongoing config table), then dedupe and merge.

1. Identify the document type (fact sheet, price book, configurator, catalog).
2. Extract global fields first — brand, designer, collection, warranty, certifications, country of origin.
3. Find product boundaries (headings, page breaks, new names).
4. Extract variants per the rules above.
5. Map dimensions carefully — parse "W × D × H" into separate W, D, H; record the Unit.
6. Distinguish base price from adders (base → List Price, adder → Notes).
7. Leave fields blank rather than guessing.

### Step 4: Present results
Show a summary markdown table: row count per PDF, any assumptions, and a sample of the first 10 rows if large. Ask: **"Does this look correct before I write the CSV?"**

### Step 5: Write the CSV
Write to the default path (or a project-specific name). Report:

```
Parsed: X products from Y PDF(s) → ffe-pdf-parse-2026-08-16.csv
- filename.pdf: N products
Import into Programa: New schedule → Import → CSV, then map columns.
Issues: [list any]
```

## Edge Cases

- **Scanned/image-only PDFs** — PyMuPDF returns empty/garbage text. Detect (very short text relative to page count) and tell the user to OCR first.
- **Multi-language PDFs** — extract as-is and note the language.
- **Tables as images** (common in price books) — flag missing data for manual review.
- **Password-protected PDFs** — PyMuPDF fails to open; catch and report.
- **Very large PDFs (100+ pages)** — 10-page chunks, progress every 20 pages.
- **Mixed product types in one PDF** — handle each type independently.
