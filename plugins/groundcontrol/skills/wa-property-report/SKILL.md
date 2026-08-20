---
name: wa-property-report
description: Comprehensive due-diligence report for a site in Western Australia — cadastre, Certificate of Title, encumbrances, heritage, DA history, SAT decisions, contamination, bushfire, coastal, and Aboriginal heritage. Guided workflow across public sources. Produces a single structured report.
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

# /wa-property-report — Due Diligence Report (Western Australia)

## Conventions (spA)

Apply before producing output; full detail in the plugin's `../../rules/` folder. If that folder is not present (the skill is running standalone, without the plugin), treat the conventions here as authoritative.

- **Metric & WA default** — metric (SI), Australian English, Western Australia jurisdiction unless the user states otherwise.
- **Verify code currency** — never rely on a code, standard, or rating-tool edition without confirming it is the current in-force version against the official source; state the edition and the date checked, or flag it as unverified (`../../rules/code-currency.md`).
- **Professional disclaimer** — AI-assisted output supporting a registered architect's judgment, not a substitute for it. Don't assert regulatory compliance ("appears consistent with… subject to verification"); flag where specialist certification or a gazetted-source check is required (`../../rules/professional-disclaimer.md`).

Produce a comprehensive due-diligence report for a site in Western Australia before starting design work or entering a conditional contract. Covers cadastre, title, heritage, DA history, and environmental / statutory checks across all major WA data sources.

**Default jurisdiction: WA.** Follows `../../rules/units-and-measurements.md`, `../../rules/professional-disclaimer.md`, `../../rules/output-formatting.md`.

## Honest scope

This skill is a **guided workflow plus structured output**. WA due diligence can't be reduced to a single API lookup — the relevant data lives across Landgate (paid certified searches), inHerit (free search), DWER Contaminated Sites (free but awkward), LGA DA registers (each LGA's portal differs), SAT (free search), AHIS (free but legal interpretation needed), and Certificate of Title documents (paid).

What this skill does:
- Walks the user through every source systematically so nothing gets missed
- Captures findings in a consistent format
- Applies WA-specific interpretation (what a Memorial means, what an "Exempt" heritage category implies, what a Category 1 contamination classification means for design)
- Produces a single report that stands on its own for file, client brief, or feasibility submission

What this skill **does not** do:
- Purchase certified Certificate of Title searches (Landgate charges ~$29/search; user must do this themselves when needed)
- Replace legal advice on title encumbrances, restrictive covenants, or Aboriginal heritage obligations
- Replace a formal Environmental Site Assessment (Phase 1 / Phase 2) for sites suspected of contamination

## When to use

- **Before entering a contract** — conditional DD period for a purchase
- **At project start** — when taking on a new site, even if the client already owns it
- **Before feasibility** — confirming developable envelope isn't constrained by easements, heritage, or contamination
- **Before a DA** — catching anything that would change the design approach or require specialist consultants

## Workflow

### Step 1: Gather minimum inputs

Ask for these. Don't proceed without the first three:

| Input | Required | Example | Notes |
|---|---|---|---|
| Site address | Yes | `48 Swanbourne St, Fremantle WA 6160` | Full street address |
| LGA | Yes | `City of Fremantle` | Local Government Authority |
| Lot / Plan no. | Yes (if known — else tell user to get from Landgate) | `Lot 22 on DP 415123` | From Certificate of Title or Landgate public search |
| Volume / Folio | Helpful | `Vol 2345 Fol 678` | Authoritative title identifier |
| Client / project | Helpful | `spA — Smith residence feasibility` | For file titling |
| Purpose of check | Helpful | `Pre-purchase DD`, `Pre-DA`, `Contract review` | Shapes emphasis |

If the user doesn't know the lot / plan, instruct them:

> Go to [Landgate Map Viewer Plus](https://maps.landgate.wa.gov.au/maps-landgate/registered/), search the address, and read the lot and deposited plan (or strata / survey-strata plan) from the sidebar. Come back with those.

### Step 2: Cadastre & Certificate of Title

Load `references/landgate-guide.md`.

Ask the user to:
1. Run a **Landgate map search** (free) — confirm lot, plan, site area, and check for any visible encumbrances on the sidebar
2. For a serious DD, run a **Certificate of Title search** (~$29.20 via WA Online Land Transactions) — returns the certified title document showing:
   - Registered proprietor(s)
   - Encumbrances section — easements, restrictive covenants, mortgages, caveats
   - Any Memorials — contamination, heritage, tree preservation
   - Title diagram (lot boundaries)
3. For strata / survey-strata — also request the **Strata Plan** or **Survey-Strata Plan** to see common property, by-laws, scheme description

Capture findings:

```
Landgate findings:
- Proprietor: [name(s), joint tenants / tenants in common]
- Lot / Plan: Lot [x] on DP/SSP/SP [x]
- Site area (title): [x] m²
- Title volume / folio: [vol] / [fol]
- Encumbrances:
  - Easement E[x] — [purpose, in favour of, width/location] — [implication for design]
  - Restrictive Covenant [x] — [terms] — [implication]
  - Mortgage [x] — [mortgagee]
  - Caveat [x] — [caveator, nature]
- Memorials:
  - [e.g. "Memorial under Contaminated Sites Act 2003 — site classified [class]"]
- Other notes: [strata by-laws, scheme description, rights of carriageway, etc.]
```

If the title shows **any restrictive covenant, Memorial, or unusual encumbrance**, flag prominently — these frequently constrain what can be built.

### Step 3: Heritage

Load `references/heritage-guide.md`.

Run these checks in parallel:

1. **State Register of Heritage Places** — [inHerit](https://inherit.dplh.wa.gov.au/) search by address
2. **Local Heritage Survey (LHS)** — check the LGA's LHS; most are searchable via inHerit too
3. **Heritage Areas** — check whether the site is within a designated Heritage Area under the LPS (e.g. Fremantle West End Heritage Area, Peppermint Grove Heritage Precinct)
4. **LGA heritage overlay map** — via IntraMaps or the LPS zoning map

Capture findings:

```
Heritage findings:
- State Register: [Registered Place "[name]" (register ref) / Not listed]
  - Statement of significance: [brief summary or link]
  - Permit requirements: [Heritage Council referral for any works affecting fabric]
- Local Heritage Survey:
  - [Place name] — Management Category [A/B/C or 1/2/3] — [summary]
  - OR: Not on LHS
- Heritage Area: [Yes — "[name]" per LPS cl. [x] / No]
- Adjoining heritage: [Nearby listings that may trigger view corridor / context considerations]
```

If heritage-listed, flag:
- A **Heritage Impact Statement (HIS)** prepared by a qualified heritage consultant will be required for any DA involving external works
- If State Registered, Heritage Council of WA referral is mandatory
- If in a Heritage Area, the LGA's Heritage Area LPP sets specific design controls — identify the LPP and note it

### Step 4: DA history & SAT decisions

Load `references/da-history-guide.md`.

Run these checks:

1. **LGA DA register** — each LGA publishes past and current DAs online. Get a list of DAs (address match) and note:
   - Any currently lodged / under assessment DAs
   - Approved DAs with conditions still active (uncommenced approvals)
   - Recent refusals — understanding why the RA refused is valuable
   - Modifications / reconsiderations
2. **Building permits (if relevant)** — via the LGA building department, especially to understand the as-built fabric vs. DA drawings
3. **SAT decisions** — [sat.justice.wa.gov.au](https://www.sat.justice.wa.gov.au/) — search by address or parties for any appeal history
4. **Precedent SAT decisions** (nearby / similar) — if the site is in a conservation area or specialised zone, look for SAT decisions on similar proposals that establish precedent

Capture findings:

```
DA / approval history:
- Current / active DAs: [list with reference, description, lodgement date, status]
- Historical DAs (5-10 year window): [list with outcome]
- Refusals: [any, with summary of reasons]
- Modifications: [any substantial modifications to approved schemes]
- Building permits: [notable recent BPs — e.g. structural, major alterations]
- SAT appeals — this site: [list with reference, outcome]
- SAT precedent — similar / adjacent sites: [relevant precedents, with citation]
```

Knowing the approval history stops you from pitching a design that looks like something the RA just refused next door.

### Step 5: Environmental & statutory checks

Load `references/environmental-guide.md`.

Work through each check systematically. For each, record **checked and clear** or **checked and flagged** — don't leave any blank.

#### 5a. Contaminated Sites — DWER

- [DWER Contaminated Sites Database](https://www.wa.gov.au/service/environment/environment-information-services/contaminated-sites-database) search by address
- Note any classification:
  - Not classified / not known to be contaminated
  - "Report not substantiated — no further investigation"
  - "Possibly contaminated — investigation required"
  - "Contaminated — remediation required"
  - "Contaminated — restricted use"
  - "Remediated for restricted use"
- If **any** classification other than "not classified", flag:
  - A Contaminated Sites Memorial is on title
  - Phase 1 / Phase 2 ESA by a contaminated sites auditor will likely be required
  - Design implications: basement depths, ground floor slab details, landscape / edible gardens, groundwater extraction

#### 5b. Bushfire-prone areas — DFES

- [DFES Bush Fire Prone Areas map](https://www.dfes.wa.gov.au/regulations/planning-and-development/bushfire-prone-areas)
- Record: BPA / Not BPA
- If BPA: note AS 3959–2018 and SPP 3.7 apply; BAL assessment required for a DA involving habitable buildings

#### 5c. Coastal hazard — SPP 2.6

- If site is within **100 m of the coast** (ocean or significant estuary), check:
  - LGA Coastal Hazard Risk Management and Adaptation Plan (CHRMAP)
  - Coastal Processes Unit (DPLH) mapping
  - Erosion and inundation setbacks per SPP 2.6 (S1: 2030 horizon, S2: 2070, S3: 2110)
- Record: Not coastal / Coastal — setback applies per SPP 2.6 [horizon] / Coastal — CHRMAP declared

#### 5d. Flood

- Check the LGA's flood map (usually in the LPS as a Special Control Area)
- Some LGAs have their flood data on IntraMaps
- Record: No flood risk identified / 100-year flood extent includes site / Floodway

#### 5e. Aboriginal heritage — AHIS

- [Aboriginal Heritage Inquiry System (AHIS)](https://www.wa.gov.au/organisation/department-of-planning-lands-and-heritage/aboriginal-heritage-inquiry-system-ahis)
- Search by address; AHIS shows:
  - Registered Aboriginal Sites on or near the property
  - Other Heritage Places (unregistered but recorded)
- **Legal note:** The *Aboriginal Heritage Act 1972* (WA) has been amended several times; current regulation is complex. Any site with registered Aboriginal sites or nearby heritage requires **legal and cultural advice**, potentially an s. 18 consent (under the 1972 Act) or a Heritage Agreement with the relevant Aboriginal party. This skill flags the existence of heritage — it does not give legal advice on how to proceed.

#### 5f. Flora, fauna, TECs

- If the site has significant remnant vegetation, check:
  - [NatureMap](https://naturemap.dbca.wa.gov.au/) for recorded threatened species, TECs
  - DBCA (Department of Biodiversity, Conservation and Attractions) databases for conservation values
  - LGA significant tree registers
- Record: Nothing identified / Species / TEC / Significant trees present

#### 5g. Acid sulfate soils

- Low-lying areas (< 5 m AHD), particularly in coastal / estuarine zones, may have acid sulfate soil (ASS) risk
- Check the WA acid sulfate soil risk mapping (DWER)
- Record: Low risk / Moderate / High risk — investigation required

#### 5h. Easements and services — in-ground

- Dial Before You Dig (1100.com.au) — for service locations, typically at DD or construction phase rather than feasibility
- Note any visible evidence of overhead powerlines / transformer kiosks / sewerage pump stations on or adjacent

### Step 6: Synthesis — the one-page risk summary

Pull the findings into a structured risk summary table. Use a traffic-light system:

| Matter | Status | Risk | Implication |
|---|---|---|---|
| Title encumbrances | … | 🟢 / 🟡 / 🔴 | … |
| Heritage | … | 🟢 / 🟡 / 🔴 | … |
| DA history | … | 🟢 / 🟡 / 🔴 | … |
| Contamination | … | 🟢 / 🟡 / 🔴 | … |
| Bushfire | … | 🟢 / 🟡 / 🔴 | … |
| Coastal | … | 🟢 / 🟡 / 🔴 | … |
| Flood | … | 🟢 / 🟡 / 🔴 | … |
| Aboriginal heritage | … | 🟢 / 🟡 / 🔴 | … |
| Flora / fauna | … | 🟢 / 🟡 / 🔴 | … |
| Acid sulfate | … | 🟢 / 🟡 / 🔴 | … |

🟢 Green = checked and clear
🟡 Amber = flagged, requires specialist / further work but not a showstopper
🔴 Red = material constraint, may change design approach, feasibility or deliverability

### Step 7: Recommend specialist consultants

Based on the findings, list the specialist consultants that will likely be required:

- Heritage consultant (if any heritage listing)
- Bushfire planning practitioner (if BPA)
- Contaminated sites auditor (if any contamination classification)
- Acoustic engineer (if near arterial road, rail, airport, industry)
- Traffic engineer (if DA would trigger Transport Impact Assessment)
- Aboriginal heritage anthropologist / lawyer (if AHIS findings)
- Structural engineer with heritage experience (if heritage building)
- Environmental consultant (if TECs, significant vegetation)
- Legal advice (if complex title encumbrances, restrictive covenants)

### Step 8: Save report

Write to the current working directory:
- Filename: `property-report-[address-slug].md`
- Example: `property-report-48-swanbourne-st-fremantle.md`

## Output Template

```markdown
# Property Due Diligence Report — [Address]

**Prepared by:** spaceagency architects
**Date:** [Australian date]
**Client / Project:** [optional]
**Purpose:** [pre-purchase DD / pre-DA / project start]

## Summary
| | |
|---|---|
| Address | … |
| LGA | … |
| Lot / Plan | Lot … on DP/SSP/SP … |
| Site Area (title) | … m² |
| Registered Proprietor | … |
| Overall Risk Rating | 🟢 / 🟡 / 🔴 |

## 1. Cadastre & Title
[findings from Step 2]

## 2. Heritage
[findings from Step 3]

## 3. DA History & SAT
[findings from Step 4]

## 4. Environmental & Statutory
### 4.1 Contaminated Sites (DWER)
### 4.2 Bushfire-Prone Areas (DFES)
### 4.3 Coastal (SPP 2.6)
### 4.4 Flood
### 4.5 Aboriginal Heritage (AHIS)
### 4.6 Flora, Fauna, TECs
### 4.7 Acid Sulfate Soils
### 4.8 Services & In-Ground

## 5. Risk Summary
[traffic-light table]

## 6. Recommended Specialists
[list]

## Sources
- Landgate Map Viewer Plus, accessed [date]
- Certificate of Title Vol … Fol … (Landgate search ref [x], dated [date]) — if purchased
- inHerit, accessed [date]
- City of [LGA] DA register, accessed [date]
- State Administrative Tribunal, search conducted [date]
- DWER Contaminated Sites Database, accessed [date]
- DFES Map of Bush Fire Prone Areas, accessed [date]
- AHIS, accessed [date]

> **Disclaimer:** This is an AI-assisted due diligence report compiled by spaceagency architects for preliminary planning purposes only. All findings must be verified by a registered architect, the relevant specialist consultants (heritage, contamination, bushfire, legal, etc.), and the registered proprietor's conveyancing lawyer before any design, contract, or statutory submission is finalised. This report is not legal advice. Title searches and specialist assessments are the responsibility of the client and their legal / technical advisors.
```

## Notes

- The traffic-light system is a judgement tool — use it to help the client see the shape of the risk at a glance, not to replace the detailed findings
- Be specific with implications. "🔴 Red — restrictive covenant prevents development within 6 m of west boundary" is useful; "🔴 Red — title issue" is not
- Title searches age — note the search date and recommend re-search before contract exchange if > 30 days
- LGA DA registers are usually complete back ~10 years; deeper history requires an archive request
- SAT decisions: the SAT's search is by name or reference — address search is tricky. Use the LGA name + street name as keywords, then filter
