# Units & Measurements

These conventions apply to all skill outputs.

## System

- Default to **metric (SI)** units — Australian and Western Australian convention
- Include imperial equivalents in parentheses **only** when the output is explicitly being prepared for a US client or US-specified product
- Never mix unit systems within a single table, calculation, or paragraph
- Drawing dimensions in millimetres (mm) without unit suffix is standard Australian practice — match this convention when working in or referencing ArchiCAD/Revit/AutoCAD output

## Area

- Always specify which area type you are reporting:
  - **GFA** — Gross Floor Area (measured to the outer face of external walls; per NCC and R-Codes definitions)
  - **NLA** — Net Lettable Area (commercial leasing — per PCA Method of Measurement)
  - **NSA** — Net Saleable Area (residential apartments — strata-titled area)
  - **NFA** — Net Floor Area (functional area inside a room, excluding circulation, walls, services)
  - **Site Area** — area of the lot per Certificate of Title (Landgate)
  - **Plot Ratio Area** — area used to calculate plot ratio per the relevant Local Planning Scheme (often excludes lift cores, plant, balconies, etc. — definitions vary by LPS)
- Plot Ratio is expressed as a decimal (e.g., `R-AC3 = plot ratio 1.5`), not a percentage
- Site Coverage is expressed as a percentage of site area
- When converting between area types, state the efficiency factor used (e.g., "82% NLA-to-GFA efficiency")
- Abbreviate after first use: "Gross Floor Area (GFA)" → then "GFA" throughout

## Dimensions

- Format: **L × W × H** (length × width × height), separated by ` × ` (space-times-space)
- Default unit: millimetres (mm) for building elements, metres (m) for site dimensions and setbacks
- Examples: `3600 × 2700 × 2400` (mm, no unit suffix in drawing context); `12.5 m × 8.0 m` (site dimensions); `setback 4.5 m`
- Levels: use AHD (Australian Height Datum) for absolute levels — `RL 12.450 AHD`
- Areas: square metres (m²) — never `sq m` or `sqm` in formal output

## Quantities

- Always state the basis: "per storey", "per occupant", "per m²", "per dwelling"
- Round to appropriate precision: areas to nearest m² (or 0.1 m² for small spaces), dimensions to nearest mm, percentages to one decimal
- Large numbers: use spaces or commas per Australian convention — `1 250 m²` or `1,250 m²` (be consistent within a document); never use full stops as thousand separators
- Decimal separator: full stop (`12.5 m`), never comma

## Currency

- Default to AUD; format as `$1.2M` for headline figures, `$1,250,000` for precise values, `$/m²` for rates
- State "ex GST" or "incl. GST" explicitly on every fee or cost figure
