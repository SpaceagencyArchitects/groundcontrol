---
name: planning-analysis-wa
description: Analyse the planning envelope for a site in Western Australia — MRS / LPS zone, R-Code, plot ratio, height, setbacks, open space, heritage, and BAL context. Produces a structured report and JSON block compatible with /zoning-envelope for 3D visualisation.
allowed-tools:
  - Read
  - Write
  - Edit
  - WebFetch
  - AskUserQuestion
  - Bash
  - Glob
  - Grep
user-invocable: true
---

# /planning-analysis-wa — Planning Envelope Analysis (Western Australia)

## Conventions (spA)

Apply before producing output; full detail in the plugin's `../../rules/` folder.

- **Metric & WA default** — metric (SI), Australian English, Western Australia jurisdiction unless the user states otherwise.
- **Verify code currency** — never rely on a code, standard, or rating-tool edition without confirming it is the current in-force version against the official source; state the edition and the date checked, or flag it as unverified (`../../rules/code-currency.md`).
- **Professional disclaimer** — AI-assisted output supporting a registered architect's judgment, not a substitute for it. Don't assert regulatory compliance ("appears consistent with… subject to verification"); flag where specialist certification or a gazetted-source check is required (`../../rules/professional-disclaimer.md`).

Analyse the development envelope for a site in Western Australia against the applicable MRS zone, LPS zone, R-Code, and relevant SPPs. Produces a markdown report with a machine-readable envelope block for the `/zoning-envelope` 3D viewer.

**Default jurisdiction: WA.** Defaults to metric, Australian spelling, NCC / R-Codes / LPS citation conventions. Follows all rules in `../../rules/` (units, terminology, professional disclaimer, transparency).

## Honest scope

WA planning is layered (MRS → LPS → LPP → R-Codes → SPPs), and there is no single free public API that returns lot + zone + R-Code + setbacks for an arbitrary address the way NYC PLUTO does. This skill is therefore **guided-input first, automated-fetch second**:

- You provide the minimum reliable inputs (address, LGA, lot / DP no., R-Code if known)
- The skill attempts to enrich via public sources (WAPC MyPlan, inHerit, DFES BPA map) where feasible
- Where automation fails or data is ambiguous, the skill asks rather than guesses
- Every output states its source and flags assumptions

The value is in **structured rule application against the bundled regulation files**, not in any magical data lookup.

## Workflow

### Step 1: Gather inputs

Ask the user for the following, all at once, with sensible defaults and clear fallbacks:

| Input | Required? | Example | Why |
|---|---|---|---|
| Site address | Yes | `48 Swanbourne St, Fremantle WA 6160` | For titling and geocoding |
| Local Government Authority (LGA) | Yes | `City of Fremantle` | Determines which LPS applies |
| Lot no. / DP or Strata plan no. | Preferred | `Lot 22 on DP 415123` | Authoritative identifier; from Certificate of Title |
| Site area (m²) | Preferred | `612 m²` | From Certificate of Title or survey |
| MRS zone | If known | `Urban` | From WAPC MyPlan |
| LPS zone | If known | `Mixed Use` | From LGA LPS zoning map |
| R-Code | If known | `R60 / R-AC3` | From LPS zoning map or Scheme text |
| Heritage status | If known | `State Registered`, `Local Heritage Survey`, `Heritage Area`, or `None` | From inHerit / LGA survey |
| BAL designation | If known | `BPA / Not BPA` | From DFES Map of Bush Fire Prone Areas |
| Proposed use | Yes | `Grouped Dwelling`, `Multiple Dwelling`, `Mixed Use`, etc. | Determines permissibility and standards |

If the user doesn't know some values, proceed and try to resolve them in Step 2.

### Step 2: Enrich from public sources (best-effort)

Attempt these fetches in parallel. Do not fail the whole analysis if any one source is unavailable — just note it in the caveats.

#### 2a. MRS zone — WAPC MyPlan

MyPlan WA is a web viewer, not an API, but the WFS layer behind it is sometimes reachable. In practice: if the user didn't supply the MRS zone, instruct them to check [MyPlan WA](https://app-ll.planning.wa.gov.au/MyPlan/) for the address and provide the MRS zone. Common values: `Urban`, `Urban Deferred`, `Industrial`, `Rural`, `Parks & Recreation`, `Railways`, `Primary Regional Roads`.

If the MRS zone is a **reservation** (anything in the Parks & Recreation / Public Purposes / Railways categories), development is generally not permitted as-of-right — flag this prominently and stop further envelope analysis. The Responsible Authority is usually the WAPC, not the LGA.

#### 2b. Heritage — inHerit

Check [inHerit](https://inherit.dplh.wa.gov.au/) — the State Register of Heritage Places plus LGA Local Heritage Surveys. Attempt via WebFetch using the site address. If a match is found, record:
- Place name and register reference
- Level of significance (`State Registered`, `Local Heritage Survey — Management Category A/B/C`, `Heritage Area`, etc.)
- Any public statement of significance

If heritage-listed, the envelope analysis must be accompanied by a flag that the *Heritage Act 2018* (WA) and/or the relevant LPP heritage provisions apply, and a Heritage Impact Statement (HIS) will likely be required.

#### 2c. Bushfire — DFES

The DFES Map of Bush Fire Prone Areas designates whether the site is in a designated BPA. If the user hasn't supplied this, ask them to check the [DFES BPA map](https://www.dfes.wa.gov.au/regulations/planning-and-development/bushfire-prone-areas). If BPA, note that:
- A Bushfire Attack Level (BAL) assessment is required for habitable buildings (generally BAL-12.5 or higher triggers additional construction requirements per AS 3959–2018)
- If BAL-40 or BAL-FZ, additional planning requirements under SPP 3.7 apply
- A Bushfire Management Plan (BMP) may be required

#### 2d. Cadastre — Landgate

If the user supplied a lot / DP no., confirm the site area. If not, ask them to check [Landgate Map Viewer Plus](https://maps.landgate.wa.gov.au/maps-landgate/registered/) for the Certificate of Title details.

For the envelope 3D viewer you need a lot polygon. Options, in order of preference:
1. User uploads a GeoJSON or simple [[x, y], …] polygon in metres (origin at southernmost point, Y increasing north)
2. User provides corner coordinates from a survey
3. Skill asks for lot dimensions (primary street frontage × depth) and constructs a rectangular approximation — flag this as approximate in the report

### Step 3: Load the bundled regulation files

Always read:
- `references/overview.md` — the WA planning framework primer (MRS → LPS → LPP hierarchy)
- `references/data-sources.md` — guide to where each piece of data comes from

Conditionally read, based on inputs:
- `references/mrs-zones.md` — if MRS zone is a reservation or the LGA is in a regional scheme area
- `references/r-codes-vol-1.md` — if R-Code is R5 through R100 and the proposed use is Single House or Grouped Dwelling
- `references/r-codes-vol-2.md` — if R-Code is R30+ with apartment form, or R-AC0 / R-AC1 / R-AC2 / R-AC3
- `references/use-classes.md` — for the P / D / A / X permissibility check
- `references/lps-[lga-slug].md` — the specific LPS file for the site's LGA (e.g. `lps-city-of-fremantle-lps4.md`)

If the LPS file for the relevant LGA is not bundled, tell the user:
> Sorry, this skill only has City of Fremantle LPS4 bundled at present. To continue, either (a) supply the key LPS controls for this site yourself (use table, plot ratio, height, setbacks, open space), or (b) ask me to add the LPS file for [LGA name] as a one-off before we proceed.

### Step 4: Determine permissibility (use table)

Using the proposed use + the LPS zone + the LPS Table of Uses:

- `P` — Permitted (as-of-right; no DA required under LPS deemed provisions if also meeting all deemed provisions and R-Code DTS)
- `D` — Discretionary (Responsible Authority may approve, subject to exercise of discretion)
- `A` — Advertised discretionary (as D, plus mandatory public advertising)
- `X` — Not permitted

State the LPS clause cited, the use class applied, and the resulting class.

If `X` (not permitted), the envelope analysis is still useful but note prominently that the use is not permitted under the current LPS and would require a Scheme Amendment, use interpretation, or different use.

### Step 5: Compute envelope — bulk controls

For a residential site under the R-Codes, compute:

**Density / yield (Vol. 1 — single & grouped dwellings):**
- Minimum / average / maximum site area per dwelling from the R-Code density table (`references/r-codes-vol-1.md`)
- Maximum number of dwellings = site area ÷ minimum site area per dwelling (round down)
- Note that average site area is the binding constraint in most cases, not minimum

**Density / yield (Vol. 2 — apartments):**
- Plot ratio from the R-Code (e.g. R40 → 0.6, R60 → 0.7, R80 → 0.8, R100 → 1.0, R-AC3 → 1.5)
- Maximum plot ratio area = plot ratio × site area
- Minimum average dwelling size and mix requirements per R-Codes Vol. 2

**Height:**
- Vol. 1: External wall height per R-Code (commonly 6 m for R20–R40, 9 m for R60+) with pitched roof allowance
- Vol. 2: Building height per R-Code storeys table (commonly 4 storeys for R40, 6 storeys for R60, 8 storeys for R80+) plus external wall height limits
- **Always** check the LPS for local height limits, which may be more restrictive than the R-Codes deemed provisions
- For activity centres, development zones, or special control areas — use the LPS / structure plan values

**Setbacks:**
- Vol. 1: Primary street, secondary street, side, rear setbacks from the R-Code setback table — these vary by R-Code, wall height, and whether the wall has major openings
- Vol. 2: Setbacks for apartment buildings per Vol. 2 deemed provisions + LPS requirements
- **Always** overlay any LPS or LPP setback requirements — these commonly override R-Codes DTS

**Site coverage & open space:**
- Open space requirement from the R-Code (commonly 45–60% for R20, decreasing to ~40% for R60, lower for higher codes)
- Private open space per dwelling
- Deep soil zones (Vol. 2 requirement for apartments)
- Communal open space (Vol. 2 apartments)

**Car parking:**
- R-Codes rates (1 bay per single house; 1 bay per 1-bed, 1.25 per 2-bed, 1.5 per 3-bed for grouped/multiple dwellings, varies)
- LPS parking rates for non-residential uses (cite LPS clause)
- Visitor parking requirements

**Discretionary / performance-based variations:**
- The R-Codes allow performance-based alternatives to DTS — note where a proposal might rely on design principles rather than DTS
- Note that discretion is exercised by the Responsible Authority, not assumed

### Step 6: Identify the Responsible Authority & approval path

Determine who decides the DA:

- **Local government** — default for most DAs
- **Joint Development Assessment Panel (JDAP)** — triggers:
  - Mandatory if estimated cost of development ≥ $10M
  - Opt-in between $2M (residential) / $20M (non-residential) and $10M
  - Per *Planning and Development (DAP) Regulations 2011*
- **WAPC** — strata / survey-strata subdivision, certain regional scheme applications, MRS reservations
- **Heritage Council of WA** — if State Registered under the *Heritage Act 2018*

State the trigger clearly. Note typical approval timeframes (60 days for DAs without advertising, 90 days with advertising) and that these are statutory but extensions are common.

### Step 7: Flag risks & further work

- **Heritage** — any place listed triggers HIS and conservation-plan considerations
- **Bushfire** — if BPA, flag BAL assessment and BMP scope
- **Flood / coastal** — if the site is in a floodway or within 100 m of coast, flag SPP 2.6 / DCP requirements
- **Traffic** — if the development meets the thresholds in Liveable Neighbourhoods or the LPS, a Transport Impact Assessment may be required
- **Acoustic** — if the site is within an influence area per SPP 5.4, an acoustic report may be required
- **Contaminated sites** — check the Contaminated Sites Database (DWER) for any classification

### Step 8: Present analysis — output format

Use the output template below. Always include the professional disclaimer per `../../rules/professional-disclaimer.md`.

### Step 9: Save report

Write to the current working directory:
- Filename: `planning-analysis-[address-slug].md`
- Example: `planning-analysis-48-swanbourne-st-fremantle.md`

Then optionally hand off to the 3D viewer:
> To generate an interactive 3D envelope viewer from this report, run: `/zoning-envelope planning-analysis-48-swanbourne-st-fremantle.md`

## Output template

```markdown
# Planning Analysis — [Address], [Suburb]

## Site Summary
| Parameter | Value | Source |
|---|---|---|
| Address | 48 Swanbourne St, Fremantle WA 6160 | User |
| LGA | City of Fremantle | User |
| Lot / Plan | Lot 22 on DP 415123 | Landgate |
| Site Area | 612 m² | Landgate |
| MRS Zone | Urban | WAPC MyPlan |
| LPS | LPS4 — City of Fremantle | Bundled |
| LPS Zone | Mixed Use | LPS4 cl. [x] |
| R-Code | R60 / R-AC3 | LPS4 Zoning Map |
| Heritage | State Registered — Fremantle West End Heritage Area | inHerit |
| BPA | Yes — BAL assessment required | DFES |
| Proposed Use | Mixed Use (ground-floor retail + 12 apartments) | User |

## Permissibility
| Parameter | Finding |
|---|---|
| LPS zone | Mixed Use |
| Proposed use class | Mixed Use (Retail + Multiple Dwelling) |
| Permissibility | D — Discretionary, per LPS4 cl. [x] Table [x] |
| Advertising | Required under LPS4 cl. [x] |

## Envelope — Bulk Controls

### Density & Yield
| Parameter | Vol. 1 / Vol. 2 | Value | Source |
|---|---|---|---|
| Density code | R60 (Vol. 1) | Min site area 180 m² / avg 200 m² / max 220 m² per dwelling | R-Codes Vol. 1 |
| Alternate density code | R-AC3 (Vol. 2) | Plot ratio 1.5 | R-Codes Vol. 2 |
| Max plot ratio area | R-AC3 | 918 m² | 1.5 × 612 m² |
| Max dwellings (Vol. 1 path) | R60 | 3 (612 ÷ 200) | Calculated |
| Max dwellings (Vol. 2 path) | R-AC3 | ~12 apartments @ avg 75 m² NSA | Calculated |

### Height
| Parameter | Value | Source |
|---|---|---|
| Max building height (LPS) | [x] m | LPS4 cl. [x] |
| Max storeys (R-Codes Vol. 2) | 6 | R-AC3 table |
| Max external wall height | [x] m | R-Codes |
| Binding height control | LPS (more restrictive) | — |

### Setbacks
| Boundary | DTS Setback | LPS Requirement | Binding |
|---|---|---|---|
| Primary street (Swanbourne) | [x] m | [x] m | [x] m |
| Side — north | [x] m | — | [x] m |
| Side — south | [x] m | — | [x] m |
| Rear | [x] m | — | [x] m |

### Open Space & Coverage
| Parameter | Requirement | Source |
|---|---|---|
| Open space (min) | 45% | R-Codes Vol. 1 |
| Private open space per dwelling | 30 m² | R-Codes |
| Communal open space (Vol. 2) | % of site | R-Codes Vol. 2 |
| Deep soil zone (Vol. 2) | % of site | R-Codes Vol. 2 |

### Parking
| Use | Rate | Bays required |
|---|---|---|
| Multiple Dwelling | [rate] | [x] |
| Retail | LPS rate | [x] |
| Visitor | [rate] | [x] |

## Responsible Authority
| Parameter | Value |
|---|---|
| DA determined by | [Local government / JDAP / WAPC] |
| JDAP trigger | [Yes — est. cost ≥ $X / No] |
| Statutory timeframe | 60 / 90 days |
| Advertising required | Yes / No |

## Risks & Further Work
- **Heritage** — …
- **Bushfire** — …
- **Traffic** — …
- **Acoustic** — …
- **Contamination** — …

## Development Potential — Scenarios

| Scenario | Path | Plot Ratio | GFA (m²) | Dwellings | Max Height | Notes |
|---|---|---|---|---|---|---|
| As-of-right Vol. 1 | R60 | — | — | 3 grouped | — | — |
| As-of-right Vol. 2 | R-AC3 | 1.5 | 918 | ~12 apartments | 6 storeys / LPS cap | — |
| Performance-based Vol. 2 | R-AC3 | 1.5 + discretion | — | — | — | Variation to setback / height via design principles |

## Envelope Data

Machine-readable block for `/zoning-envelope`. Units metric throughout.

```json
{
  "lot_poly": [[0, 0], [20, 0], [20, 30], [0, 30]],
  "unit": "m",
  "setbacks": { "front": 4, "rear": 3, "lateral1": 1.5, "lateral2": 1.5 },
  "volumes": [
    { "type": "base", "inset": 0, "h_bottom": 0, "h_top": 4, "label": "podium (retail + lobby)" },
    { "type": "tower", "inset": 3, "h_bottom": 4, "h_top": 22, "label": "apartment levels (5 storeys)" }
  ],
  "height_cap": 22,
  "info": { "title": "48 Swanbourne St", "zone": "R-AC3 Mixed Use (LPS4)", "id": "Lot 22 DP 415123", "area": "612 m²" },
  "stats": { "Plot Ratio": "1.5", "Max GFA": "918 m²", "Max Dwellings": "~12", "Max Storeys": "6" }
}
```

To generate the interactive 3D viewer:
`/zoning-envelope planning-analysis-48-swanbourne-st-fremantle.md`

## Caveats & Sources
- Site and cadastral data: [Landgate Map Viewer Plus](https://maps.landgate.wa.gov.au/maps-landgate/registered/), retrieved [date]
- MRS zone: [WAPC MyPlan](https://app-ll.planning.wa.gov.au/MyPlan/), retrieved [date]
- LPS4 controls: City of Fremantle Local Planning Scheme No. 4, as in force at [date] — [cofremantle.wa.gov.au](https://www.fremantle.wa.gov.au/)
- R-Codes: State Planning Policy 7.3 Residential Design Codes, Vol. 1 [version], Vol. 2 [version] — [WAPC R-Codes](https://www.wa.gov.au/government/publications/state-planning-policy-73-residential-design-codes)
- Heritage: [inHerit](https://inherit.dplh.wa.gov.au/), retrieved [date]
- Bushfire: [DFES Map of Bush Fire Prone Areas](https://www.dfes.wa.gov.au/regulations/planning-and-development/bushfire-prone-areas), retrieved [date]

> **Disclaimer:** This is an AI-generated analysis for preliminary planning purposes only. All findings must be verified by a registered architect, engineer, or other suitably qualified practitioner before use in design development, development applications, building permit submissions, or any other statutory submission. This output is not a substitute for professional advice, certified drawings, or engineering certification.
```

## Notes

- The R-Codes are deemed-to-satisfy provisions — performance-based alternatives under the design principles are always available but require discretion of the Responsible Authority
- The LPS and LPPs commonly override R-Codes DTS (more restrictive) — always apply the more restrictive control unless the LPS expressly allows the R-Code to prevail
- When the LPS introduces a "development zone" or "activity centre zone", the LPS text / structure plan is usually the primary control, not the R-Codes — flag and cite the correct instrument
- Regional schemes (MRS, Peel, Greater Bunbury) apply state-level zoning over LGA boundaries — check MyPlan for all sites, not just Perth metro
- City of Yes-equivalent reforms: as of 2026, the State Government is progressing **Design WA** (design-led planning), **Medium Density Code**, and **planning reform** — note these if the user's site may be affected
