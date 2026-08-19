# Data Sources — where each piece of planning data comes from

A practical lookup guide for every piece of information this skill needs. Grouped by what you're trying to find out.

## Cadastre — lot, address, site area, certificate of title

**Primary: [Landgate Map Viewer Plus](https://maps.landgate.wa.gov.au/maps-landgate/registered/)** (free, no login)

- Search by address or lot/DP no.
- Returns: lot number, deposited plan or survey-strata plan, site area, encumbrances, easements, Certificate of Title reference
- For certified Certificate of Title searches, Landgate charges a fee via [WA Online Land Transactions](https://www0.landgate.wa.gov.au/)

**For commercial / studio use:**
- [Landgate SLIP](https://www.landgate.wa.gov.au/business-and-government/location-and-spatial-data/slip) — Shared Location Information Platform. Free tier available for agencies; SLIP Enabler 2 has WFS and WMS endpoints for cadastre, zoning, heritage overlays
- [NearMap](https://www.nearmap.com/) — paid, but widely used in WA practice for recent aerial imagery; spA has a subscription

## MRS / regional scheme zoning

**Primary: [WAPC MyPlan WA](https://app-ll.planning.wa.gov.au/MyPlan/)** (free, no login)

- Visual viewer for state-level planning data
- Layers include: MRS / PRS / GBRS zones and reservations, regional road reserves, state heritage places, bush fire prone areas, coastal management areas
- Not an API — navigate to the site and read the MRS zone from the legend
- Export: MyPlan can produce a PDF site report

**Alternative:** The LPS zoning map usually reproduces the MRS zone in the legend — cross-check

## LPS zoning, R-Code, use permissibility

**Primary: the LGA's online planning map**

Most metro LGAs have an IntraMaps viewer:

| LGA | Viewer |
|---|---|
| City of Fremantle | [Fremantle IntraMaps](https://maps.fremantle.wa.gov.au/) |
| City of Perth | [PerthMaps](https://www.perth.wa.gov.au/) → "Maps & data" |
| Town of Vincent | [Vincent IntraMaps](https://maps.vincent.wa.gov.au/) |
| City of Stirling | [Stirling online maps](https://www.stirling.wa.gov.au/) |
| City of Vic Park | [Victoria Park IntraMaps](https://www.victoriapark.wa.gov.au/) |
| City of Subiaco | [Subiaco online maps](https://www.subiaco.wa.gov.au/) |
| City of Joondalup | [Joondalup MapWeb](https://www.joondalup.wa.gov.au/) |

**Each LPS is also published as a PDF** on the LGA website under "Local Planning Scheme" or "Planning & Building → Planning Scheme". Read the Scheme text for the Table of Uses, development requirements, and definitions. The zoning map is a separate PDF.

**The gazetted version is authoritative** — cross-check the IntraMaps viewer against the gazetted LPS text dated at the Scheme's last amendment. Amendments lag in viewer updates.

## R-Codes (SPP 7.3)

**Primary: [WAPC R-Codes publication page](https://www.wa.gov.au/government/publications/state-planning-policy-73-residential-design-codes)**

- Vol. 1 — Single houses and grouped dwellings — free PDF download
- Vol. 2 — Apartments — free PDF download
- Explanatory guidelines and FAQs available separately

The applicable version is the one in force at the date of DA lodgement. Amendments occur occasionally (most recently Vol. 1 updated 2024); check the publication date on the PDF.

## Local Planning Policies (LPPs)

**Primary: the LGA's website**

Each LGA publishes its LPPs on its planning page. LPPs commonly override or supplement R-Codes DTS for specific matters — heritage areas, height controls, outbuildings, fencing, signs, verges. Always check.

For City of Fremantle: [Fremantle LPPs](https://www.fremantle.wa.gov.au/residents/planning-and-building/planning-policies)

## Heritage status

**Primary: [inHerit](https://inherit.dplh.wa.gov.au/)** (free, no login)

- State Register of Heritage Places
- Local Heritage Surveys (most LGAs submit their LHS to inHerit; coverage varies)
- Returns: place name, register level, statement of significance, photographs, assessment date
- Also accessible via [Heritage Council of WA](https://www.wa.gov.au/organisation/heritage-council) for full files

**Supplement: the LGA's heritage map / Local Heritage Survey PDF**

Some LGAs publish their LHS separately with management categories (A/B/C/etc.) that inHerit may not show in detail.

**Heritage Area vs Heritage Place:**
- A **Heritage Place** is an individual site or building
- A **Heritage Area** is a precinct (e.g. Fremantle West End Heritage Area) — triggers different LPP / DA requirements to individual listings
- Both should be checked

## Bushfire-prone areas and BAL

**Primary: [DFES Map of Bush Fire Prone Areas](https://www.dfes.wa.gov.au/regulations/planning-and-development/bushfire-prone-areas)** (free, no login)

- Shows designated BPA — the legally binding map under the *Planning and Development Act* for bushfire risk
- Updated annually by the OBRM (Office of Bushfire Risk Management)

**If in a BPA:**
- Development of habitable buildings requires BAL assessment per AS 3959–2018
- BAL-40 / BAL-FZ triggers SPP 3.7 requirements (bushfire management plan, evacuation)
- A qualified Bushfire Planning Practitioner is required for BAL reports on most DAs

**BAL Contour Map:** A contour map can be generated by a BPP or via a DFES-accredited tool — this shows BAL rating at a given point on a site.

## Contaminated sites

**Primary: [DWER Contaminated Sites Database](https://www.wa.gov.au/service/environment/environment-information-services/contaminated-sites-database)** (free, search by address)

- Classifications: "Report not substantiated", "Possibly contaminated", "Contaminated – remediation required", "Contaminated – restricted use", "Remediated for restricted use"
- A Memorial on the Certificate of Title is placed for classified sites

## Flood and coastal

- **Floodway / flood-prone areas:** check the LGA's flood maps (often in the LPS as a Special Control Area)
- **Coastal:** SPP 2.6 applies within 100 m of the coast. Check Coastal Processes Unit mapping
- **Sea-level rise allowances:** apply under SPP 2.6, 2030/2070/2110 horizons — relevant for coastal sites

## Transport, traffic, access

- **State roads:** Main Roads WA controls access to primary and secondary regional roads. Check [Main Roads Access Management](https://www.mainroads.wa.gov.au/)
- **Local roads:** the LGA's road hierarchy, usually in the LPS as a map
- **Transport Impact Assessment trigger:** per LGA policy + *WAPC Transport Impact Assessment Guidelines*

## Noise

- **SPP 5.4** — Road and rail noise. Influence areas defined per transport network
- **Environmental Protection (Noise) Regulations 1997** — assigned noise levels
- **Acoustic report:** required for new residential development in a noise influence area

## Service capacity

- **Water / sewer:** Water Corporation — check [Water Corporation Land Development Portal](https://www.watercorporation.com.au/)
- **Electricity:** Western Power (SWIS) — check [Western Power LVD portal](https://www.westernpower.com.au/) for distribution capacity
- **Gas:** ATCO Gas Australia
- **Telecommunications:** NBN, Telstra

## Summary — minimum reliable set

For any envelope analysis, the *minimum* set of sources to verify is:

1. **Landgate Map Viewer Plus** — lot / DP / area
2. **MyPlan WA** — MRS zone
3. **LGA IntraMaps + LPS text** — LPS zone, R-Code, use table, LPPs
4. **inHerit** — heritage
5. **DFES BPA map** — bushfire

For any statutory submission, the architect is responsible for checking *all* relevant sources — this skill's output is preliminary analysis only.
