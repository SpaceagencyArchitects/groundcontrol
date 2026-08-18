# Transparency

Architecture Studio exists to make architects faster, not to replace their judgment. Every output must be verifiable — the user should never have to trust a number they can't trace back to its source.

## Show Your Work

- **Never present a derived number without the inputs.** If you calculated FAR, show the lot area and building area. If you calculated occupant load, show the SF, area type, and load factor. The formula and the values that went in are as important as the result.
- **Never present a recommendation without the reasoning.** If you recommend 20% meeting space, explain what drove that number — hybrid policy, headcount, work style. The user needs to know what to change if their assumptions shift.
- **Never summarize away the detail.** A summary is fine as a lead, but the supporting data must be accessible in the same output. Don't force a follow-up question to see the math.

## Link to Sources

- **Every data point from an external source gets a link.** Not just a name — a URL the user can click to verify. "Source: Landgate" is not enough. "Source: [Landgate Map Viewer Plus](https://maps.landgate.wa.gov.au/maps-landgate/registered/)" is.
- **When a link isn't available**, cite the source precisely enough to find it: publisher, title, edition, section / clause number, date.
- **When using bundled data** (NCC tables, R-Codes provisions, LPS extracts), state what's bundled and what edition/version. The user should know whether the bundled data is current for the LGA in question — LPSs and LPPs change frequently.

## Cite the Code

- **Building, planning, and standards references must include a public link** when one exists. Use government-published sources first:
  - National Construction Code (NCC): [ncc.abcb.gov.au](https://ncc.abcb.gov.au/)
  - R-Codes (SPP 7.3): [WAPC — R-Codes](https://www.wa.gov.au/government/publications/state-planning-policy-73-residential-design-codes)
  - WA Planning Acts and Regulations: [legislation.wa.gov.au](https://www.legislation.wa.gov.au/)
  - Local Planning Schemes: each LGA's website (e.g. [City of Fremantle LPS4](https://www.fremantle.wa.gov.au/))
  - Australian Standards (purchase / preview): [store.standards.org.au](https://store.standards.org.au/)
  - State Register of Heritage Places: [inHerit](https://inherit.dplh.wa.gov.au/)
  - SAT decisions: [sat.justice.wa.gov.au](https://www.sat.justice.wa.gov.au/)
- **Never cite a code or scheme clause without the edition / version year.** `NCC D2D5` is ambiguous. `NCC 2022 Vol. 1 D2D5` is verifiable. `R-Codes cl. 5.1.3` is ambiguous. `R-Codes Vol. 1 (2024) cl. 5.1.3` is verifiable.

## Data Provenance

- **State when data was retrieved.** ABS Census data from 2021 is different from 2026 estimates. Landgate cadastral data is updated continuously. SLIP layers have versioning. Say which version / retrieval date you used.
- **Distinguish between live data and bundled data.** If the skill queried an API or web source, say so. If it used a bundled JSON / markdown file, say which file and what it represents.
- **Flag when data may be stale.** If a heritage entry pre-dates a recent amendment, if an LPS is undergoing review, if R-Codes Vol. 2 has been updated since the bundled snapshot, if BoM normals are from an earlier reference period — note it.

## The Standard

The user should be able to take any output from Architecture Studio and:
1. Verify every number by following the cited source
2. Reproduce the calculation by using the shown inputs and formula
3. Update the result if their assumptions change, because they can see what went in
