# City of Fremantle — Local Planning Scheme No. 4 (LPS4)

Structural guide for applying Fremantle LPS4 in the `/planning-analysis-wa` skill. This file gives the **framework** of LPS4 — its zones, how to read the Scheme, where LPPs fit — so the skill can produce a properly structured analysis.

> **This file is a guide, not a copy of the Scheme.** Clause numbers, plot ratios, density codes, and use permissibilities must always be verified against the **currently-gazetted LPS4 text** on the City of Fremantle website before being relied on for any DA.

## Authoritative sources

Always verify against these before finalising an analysis:

- [City of Fremantle — LPS4 page](https://www.fremantle.wa.gov.au/) → Planning and Building → Local Planning Scheme
- [Gazetted LPS4 scheme text (PDF)](https://www.fremantle.wa.gov.au/) — current consolidated version
- [LPS4 zoning maps (PDF)](https://www.fremantle.wa.gov.au/) — all 12 map sheets
- [Fremantle IntraMaps viewer](https://maps.fremantle.wa.gov.au/) — interactive zoning, R-Code, heritage overlay
- [Local Planning Policies](https://www.fremantle.wa.gov.au/residents/planning-and-building/planning-policies) — operational policies that override or supplement LPS4
- [Local Heritage Survey](https://www.fremantle.wa.gov.au/) — heritage listings with management categories

## Geographic scope

LPS4 covers the **City of Fremantle LGA**: Fremantle, White Gum Valley, Beaconsfield, South Fremantle, Hilton, O'Connor (parts), Samson (parts), and the port / fishing industry land around the harbour.

**Not covered by LPS4**:
- **North Fremantle** — within City of Fremantle but governed by LPS4; historically had separate controls but now part of the consolidated LPS4
- **East Fremantle** — separate LGA (Town of East Fremantle, LPS3)
- **Port land** — Fremantle Ports land is Crown land; LPS4 applies to the city-side of the port boundary

Confirm the LGA boundary on IntraMaps before proceeding.

## Zone categories in LPS4

LPS4 has several zone families. Always cite the **exact zone name** as shown on the zoning map — sub-variants matter.

### Residential zones
- `Residential R[x]` — standard residential, various R-Codes (R20, R25, R30, R40, R60, R80, R100)
- Density codes are set on the zoning map, not in the Scheme text

### Mixed Use / Commercial zones
- `Mixed Use` — with allocated R-Code (commonly R60 / R-AC3 or R80 / R-AC3)
- `City Centre` — the primary CBD zone (central Fremantle)
- `Local Centre` — neighbourhood-scale commercial centres
- `District Centre` — larger commercial centres

### City Centre / Activity Centre zones
- `City Centre` zone covers the Fremantle CBD
- Sub-precincts with specific built-form controls — refer to the City Centre Strategy and the LPS4 city-centre clauses
- The West End sits within the City Centre zone but is subject to the West End Heritage Area provisions

### Industrial zones
- `Industrial` — light / general industry (around O'Connor, parts of South Fremantle)
- `Service Commercial` — hybrid service / commercial uses

### Special zones
- `Development` — areas subject to a structure plan (e.g. former Kim Beazley Lodge site, Point Street)
- `Special Use` — site-specific uses listed in Schedule 2

### Reserves
- `Public Purpose` — civic, hospital, school
- `Parks and Recreation` — public open space
- `Primary Regional Roads` — state roads (controlled by MRS + Main Roads)

## Heritage overlays — critical to Fremantle

Fremantle has the highest heritage listing density in WA. The heritage layer is separate from the zone — a site can be in *any* zone and also be:

| Heritage overlay | Authority | Controls |
|---|---|---|
| **State Registered Place** (*Heritage Act 2018*) | Heritage Council of WA | Full HIS + Heritage Council referral. LPS4 cannot approve substantial works without Heritage Council concurrence |
| **Local Heritage Survey** | City of Fremantle | Management categories A / B / C — controls vary |
| **West End Heritage Area** | City of Fremantle (LPS4 + LPP) | Most stringent local heritage controls; design review required for most works; specific materiality, fenestration, and height expectations |
| **Other Heritage Areas** (East Fremantle boundary, South Fremantle, etc.) | City of Fremantle | Similar to West End but with area-specific LPPs |

Any analysis in Fremantle **must** include a heritage check. If any heritage overlay applies, the envelope analysis is qualified by the heritage controls, and a **Heritage Impact Statement (HIS)** by a qualified heritage consultant will be required for most DAs.

## Typical bulk controls (representative — verify in Scheme text)

These are **typical patterns** in Fremantle LPS4 — they illustrate what to look for, not the specific values to apply. Always verify in the current Scheme.

| Zone | Typical R-Code | Typical plot ratio (Vol. 2 path) | Typical height | Typical street setback |
|---|---|---|---|---|
| Residential R20 | R20 | Vol. 1 only | 6 m (pitched) / 7 m (flat) | 6 m (varies) |
| Residential R40 | R40 | 0.6 | 2–3 storeys | 4 m (varies) |
| Mixed Use (general) | R60 / R-AC3 | 1.5 | LPS sets height — commonly 4 storeys outside the West End | 0–4 m |
| City Centre (outside West End) | R-AC3 | 1.5+ | Varies by precinct — commonly 4–6 storeys | 0 (built to boundary) |
| West End Heritage Area | Varies | Generally low — heritage controls dominate | Commonly 3–4 storeys, matching existing streetwall | 0 (infill matching context) |

**Caveat:** Specific plot ratios, heights, and setbacks are set by the Scheme text for each zone — *and* by LPPs — *and* sometimes by structure plans. Always layer the checks.

## Local Planning Policies (LPPs) — the operational layer

LPPs are where Fremantle's design character is really controlled. Key LPPs to check for any site in Fremantle include:

| LPP (indicative) | What it controls |
|---|---|
| LPP — Heritage Areas (various) | Infill guidelines, materiality, streetwall heights, fenestration |
| LPP — West End Heritage Area | Strict controls — design review, heritage interpretation |
| LPP — Car Parking | Car parking rates for non-residential uses, bike parking, cash-in-lieu provisions |
| LPP — Sign | Signage controls across all zones |
| LPP — Outdoor Dining | Footpath trading on commercial streets |
| LPP — Fencing | Front and side fence heights in residential zones |
| LPP — Setbacks from Road Reserve | Additional street-reserve setback requirements |
| LPP — Design Review | Triggers for Design Review Panel referral |
| LPP — Verge Treatment | Verge landscaping, crossovers |
| LPP — Trees and Landscape | Tree retention, canopy requirements |

**Always check the full LPP list** on the City of Fremantle website at DA time — new LPPs are added, old ones updated. Note the LPP version and adoption date.

## Table of Uses — key notes

- LPS4 uses the **P / D / A / X** system (post-2015)
- Older versions of LPS4 used the legacy codes — treat legacy codes per `use-classes.md`
- The Table of Uses is in the Scheme text (not the zoning map)
- Special uses are in Schedule 2 — site-specific permissibilities overriding the main Table of Uses
- Additional Use Areas are in Schedule 3 — spatial overlays permitting specific uses on specific lots

## Application paths & Responsible Authority

- **Local government (default)** — most DAs. Delegated to officers for minor; to Council for complex, controversial, or LPP non-compliance
- **JDAP (Metro Inner-South)** — triggered by cost of development thresholds (see `overview.md`). Fremantle falls within the Metro Inner-South JDAP
- **WAPC** — strata subdivision, MRS reservations, regional matters
- **Heritage Council** — State Registered Places

Design Review Panel: Fremantle has a standing Design Review Panel for larger / significant projects — referral is required for schemes meeting the DRP trigger LPP.

## Fremantle-specific considerations

- **Port influence area** — noise, light, traffic from port operations; relevant for residential near the harbour
- **ANEF contours** — aircraft noise (Jandakot Airport) — relevant for residential south of the LGA
- **Cipher Creek / Booyeembara** — former landfills, ground condition considerations
- **Coastal hazard** — parts of South Fremantle and the beachfront are within SPP 2.6 coastal planning setbacks
- **Groundwater-sensitive zones** — South Fremantle has shallow groundwater; important for basement development
- **Acid sulfate soils** — low-lying parts of the LGA

## How this file is used by the skill

When `/planning-analysis-wa` identifies that the site's LGA is City of Fremantle, the skill:

1. Loads this file alongside the R-Codes reference
2. Prompts the user to confirm the LPS4 zone, R-Code, and heritage status from IntraMaps + inHerit + LHS
3. Asks the user to check the current Scheme text for the specific zone's bulk controls (plot ratio, height, setbacks) — either by referencing the PDF or by running a web fetch of the Scheme
4. Applies this file's heritage / LPP / DRP framework to the analysis
5. Writes a report that cites **LPS4 cl. [x]** explicitly wherever a Scheme provision is applied, with a note directing the reader to the gazetted Scheme text

## Updating this file

When Fremantle LPS4 is amended (which happens several times a year for minor amendments, occasionally for major amendments):

1. Check the City of Fremantle planning page for the current consolidated Scheme text
2. Note any new / modified zones, clauses, or Schedule entries
3. Update this file with the new framework
4. Commit with a clear message stating the Scheme version / gazettal date

**Do not** embed specific plot ratios or clause numbers in this file from memory — always derive them from the live Scheme text at analysis time.
