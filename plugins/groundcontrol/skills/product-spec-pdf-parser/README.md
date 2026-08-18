# /product-spec-pdf-parser

PDF product spec parser. Feed it price books, fact sheets, or spec sheets — get structured FF&E data as a CSV ready to import into **Programa** (or any FF&E scheduling tool).

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../../LICENSE)

## Where it fits

Programa imports CSV/Excel and captures web products, but it doesn't parse arbitrary rep **PDF price books**. This skill fills that gap — messy PDF in, clean import-ready CSV out.

### Dependencies

- **PyMuPDF** — PDF text extraction: `pip install PyMuPDF`

## Usage

```
/product-spec-pdf-parser ~/Documents/specs/alphabeta-floor-lamp.pdf
```

Or point at a folder to process every `.pdf` in it.

### Variant depth

- **expand** (default) — one row per variant/SKU. Best for procurement.
- **summarize** — one row per product, variants comma-separated.

## Output

A local CSV (`./ffe-pdf-parse-YYYY-MM-DD.csv`) using the same header as `/product-research`, so web shortlists and PDF extracts import into Programa identically. PDF-specific data (variant, price adder, country of origin, source filename) is carried in the Notes column.

## PDF types supported

| Type | Variant strategy |
|------|-----------------|
| Fact sheet with SKUs | One row per SKU (shade × colour) |
| Fact sheet with finishes | One row per upholstery option |
| Price book / configurator | One row per product type, options summarized |
| Product catalog | Rows for each distinct product |
| Spec sheet | One row with full detail |

## Error handling

- **Scanned/image PDFs** — detected and flagged for OCR
- **Password-protected PDFs** — caught and reported
- **Large PDFs (100+ pages)** — processed in 10-page chunks with progress updates

## Works with

| Skill / tool | Relationship |
|-------|-------------|
| **Programa** | Import the CSV as a schedule, then map columns |
| `/product-research` | Web discovery from a brief; this handles rep PDFs |

## License

MIT
