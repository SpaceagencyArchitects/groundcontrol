# wa-property-report

Comprehensive due-diligence report for a site in Western Australia. One guided workflow, one structured report, all the checks an architect needs before design work starts.

## What it covers

- **Cadastre & Title** — lot / plan, site area, proprietor, encumbrances (easements, covenants, caveats, Memorials)
- **Heritage** — State Register (inHerit), Local Heritage Survey, Heritage Areas, adjoining listings
- **DA history** — LGA DA register, building permits, SAT appeals and precedents
- **Contamination** — DWER Contaminated Sites Database classifications
- **Bushfire** — DFES Bush Fire Prone Areas designation + BAL implications
- **Coastal** — SPP 2.6 setback horizons, CHRMAP declarations
- **Flood** — LGA flood mapping, floodway designation
- **Aboriginal heritage** — AHIS registered and other recorded places
- **Flora, fauna, TECs** — NatureMap, DBCA, significant trees
- **Acid sulfate soils** — DWER risk mapping
- **Services** — overhead / in-ground infrastructure notes

## When to run it

- Before entering a conditional contract for a site purchase
- At project inception, even for sites already owned by the client
- Before a pre-DA design feasibility
- Before formal DA lodgement, as a final sweep for missed issues

## Output

A single markdown report (`property-report-[address-slug].md`) structured into:

1. Summary table + overall risk rating
2. Findings across all 11 check areas
3. Traffic-light risk summary
4. Recommended specialist consultants
5. Sources and dates

## Scope — be honest

This skill is a **guided workflow**. It does not:

- Buy Certificate of Title searches (user does this via Landgate, ~$29.20)
- Replace a conveyancing lawyer's title review
- Replace a Phase 1 / Phase 2 Environmental Site Assessment
- Replace an s. 18 consent assessment under the *Aboriginal Heritage Act 1972* (WA)

What it does:

- Makes sure no data source is missed
- Applies WA-specific interpretation to the findings
- Produces a report that stands on its own for client, file, or consultant handover
- Flags material issues with consistent traffic-light status

## Sources used

Every external source the workflow touches, with a link:

- [Landgate Map Viewer Plus](https://maps.landgate.wa.gov.au/maps-landgate/registered/) — free cadastre
- [WA Online Land Transactions](https://www0.landgate.wa.gov.au/) — paid certified searches
- [inHerit](https://inherit.dplh.wa.gov.au/) — State + Local heritage register
- LGA DA register — each LGA publishes on its own website
- [State Administrative Tribunal](https://www.sat.justice.wa.gov.au/) — appeal decisions
- [DWER Contaminated Sites Database](https://www.wa.gov.au/service/environment/environment-information-services/contaminated-sites-database)
- [DFES Map of Bush Fire Prone Areas](https://www.dfes.wa.gov.au/regulations/planning-and-development/bushfire-prone-areas)
- [AHIS — Aboriginal Heritage Inquiry System](https://www.wa.gov.au/organisation/department-of-planning-lands-and-heritage/aboriginal-heritage-inquiry-system-ahis)
- [NatureMap (DBCA)](https://naturemap.dbca.wa.gov.au/)

## Related

- [`/planning-analysis-wa`](../planning-analysis-wa/) — envelope analysis (complements DD — run both for a full pre-design workup)
- `reference/landgate-guide.md`, `reference/heritage-guide.md`, `reference/da-history-guide.md`, `reference/environmental-guide.md` — the bundled reference material the skill draws on

## License

MIT
