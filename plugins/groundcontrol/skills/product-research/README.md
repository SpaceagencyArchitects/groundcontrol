# Product Research

FF&E product research. Give it a brief, it searches the web, and comes back with a curated shortlist as a CSV ready to import into **Programa** (or any FF&E scheduling tool).

## How it works

```
Brief → Search → Candidates → Pick → CSV → import into Programa
```

1. **Brief** — Tell Claude what you're looking for ("round walnut dining table under $3k")
2. **Research** — Claude searches across brands, trade platforms, and design publications
3. **Candidates** — Get 6–10 options with specs, pricing, and reasoning
4. **Pick** — Choose which products to keep
5. **CSV** — Written to `./ffe-research-YYYY-MM-DD.csv`, ready to import into Programa

## Where it fits

Programa captures products you've already found and owns the schedule, procurement, and client approvals. This skill does the part Programa can't: **open-ended discovery and curation from a brief.** Its output is an import-ready CSV — the hand-off point to Programa.

## Usage

```
/product-research
```

Then describe what you need — loose or specific:

```
# Loose
"acoustic panels for a tech office lobby"

# Specific
"round dining table, 48-54" dia, solid walnut or oak,
steel base, under $3,000, needs to ship in 6 weeks"
```

## What it understands

Category, use context, style, materials, dimensions, budget, sustainability certs, lead time, quantity, indoor/outdoor, brand preferences, and must-haves. **Only mention what matters — it works with whatever you give it.**

## Works with

| Skill / tool | How |
|------|-----|
| **Programa** | Import the CSV as a new schedule, then map columns |
| `/product-spec-pdf-parser` | For rep PDF price books instead of web products |

## License

MIT
