# planning-analysis-wa

Analyse the planning envelope for a site in Western Australia — MRS / LPS zone, R-Code, plot ratio, height, setbacks, open space, heritage, and BAL context. Produces a structured markdown report and a JSON block compatible with the existing `/zoning-envelope` 3D viewer.

## Usage

```
/planning-analysis-wa
```

The skill will ask for the site address, LGA, lot / DP number, proposed use, and any known planning controls. Where possible it will fetch data from public sources (WAPC MyPlan, inHerit, DFES Bush Fire Prone Area map) — where not, it prompts you for the values from your own Landgate and LGA research.

## What it covers

- MRS zone and reservations
- Local Planning Scheme zone and use permissibility (P / D / A / X)
- R-Code density / plot ratio / yield (R-Codes Vol. 1 & Vol. 2)
- Height, setbacks, open space, deep soil, communal open space
- Car parking rates
- Heritage status (State Register, Local Heritage Survey, Heritage Area)
- Bushfire-prone area designation and BAL implications
- Responsible Authority — local government, JDAP, or WAPC
- Scenarios — as-of-right vs. performance-based

## Bundled LPS files

| LGA | LPS | File | Status |
|---|---|---|---|
| City of Fremantle | LPS4 | `planning-rules/lps-city-of-fremantle-lps4.md` | ✅ Bundled |
| City of Perth | LPS26 | — | ➕ Request to add |
| Other LGAs | various | — | Either supply the LPS controls yourself, or ask to add the LPS |

Adding a new LPS is a one-file addition — drop a `lps-[lga-slug].md` in the `planning-rules/` folder following the existing template.

## Data sources

See [`planning-rules/data-sources.md`](./planning-rules/data-sources.md) for a full guide to where each piece of planning data comes from, including:

- Landgate (cadastre, Certificate of Title)
- WAPC MyPlan (MRS zoning)
- Each LGA's online map viewer (LPS zoning, R-Codes)
- inHerit (heritage register)
- DFES Map of Bush Fire Prone Areas
- Contaminated Sites Database (DWER)

## Output

Produces two deliverables:

1. **Markdown report** — `planning-analysis-[address-slug].md` in the current working directory, with summary, permissibility, bulk controls, responsible authority, risks, and scenarios
2. **JSON envelope block** embedded in the report — compatible with `/zoning-envelope` for a self-contained 3D HTML viewer

## Related

- [`/zoning-envelope`](../zoning-envelope/) — renders the JSON block as an interactive 3D envelope
- `../../rules/units-and-measurements.md`, `../../rules/code-citations.md`, `../../rules/professional-disclaimer.md` — govern the output format and language

## Caveats

- The R-Codes, LPS, and LPPs change — always verify the bundled LPS file against the currently-gazetted Scheme
- WA has no centralised clean public API for zoning; guided input + best-effort web fetches is the honest design
- This skill supports **preliminary planning analysis**. Before any submission, engage a registered architect and the relevant consultants for a definitive opinion
