# Landgate & Certificate of Title — guide

Reference for the cadastre and title checks in `/wa-property-report`.

## Landgate — what it is

Landgate is the WA government agency that maintains the **Register of Titles** and the cadastral database for the State. Every property in WA has a Certificate of Title (or is Crown Land); every title is held in Landgate's Register.

## Two levels of Landgate search

### 1. Free public search — Map Viewer Plus

[Landgate Map Viewer Plus](https://maps.landgate.wa.gov.au/maps-landgate/registered/)

- Free, no login
- Search by address, lot/DP, or coordinates
- Returns: lot number, deposited plan / strata / survey-strata plan, site area, title volume/folio, zoning overlay, aerial imagery
- **Cannot return**: the Encumbrances section of the title, the full list of Memorials, registered proprietor details

Use Map Viewer Plus to confirm the lot exists, get the plan number, and estimate site area. For any serious DD, move to a paid Certificate of Title search.

### 2. Paid certified search — WA Online Land Transactions

[WA Online Land Transactions](https://www0.landgate.wa.gov.au/)

- Requires a login (free to register)
- Pay-per-search model
- Current Certificate of Title: approx. **$29.20** (as at 2026 — check current fee)
- Returns the **full certified Certificate of Title** PDF showing:
  - Registered proprietor(s) — names + ownership structure (joint tenants / tenants in common)
  - Encumbrances — easements, restrictive covenants, mortgages, caveats
  - Memorials — statutory markings (contamination, heritage, Aboriginal heritage agreements, etc.)
  - Title diagram
- Searches are **point-in-time** — title age matters. Treat a search > 30 days old as stale; re-search before contract exchange

Associated paid searches often needed:
- **Deposited Plan / Strata Plan / Survey-Strata Plan** — the cadastral plan referenced by the title
- **Easement documents** — the registered document creating an easement (shows the terms, not just the location)
- **Restrictive covenant documents** — the registered document setting the terms

## Reading a Certificate of Title

A typical WA Certificate of Title has the following structure:

### 1. Header
- Title volume and folio (e.g. `Vol 2345 Fol 678`)
- Date of duplicate
- Duplicate status

### 2. Land description
- Lot and plan reference (e.g. `Lot 22 on Deposited Plan 415123`)
- Address

### 3. Registered proprietor
- Name(s)
- Type of ownership:
  - **Joint tenants** — right of survivorship; on death of one owner, the whole passes to the survivor
  - **Tenants in common** — defined share (often 50/50 but can be any split); share passes by will
  - **Single proprietor**

### 4. Limitations, interests, encumbrances & notifications
The critical section. Lists anything registered against the title:

#### Easements
- **Easement in gross** — in favour of a utility (Water Corporation, Western Power, Telstra / NBN)
- **Easement appurtenant** — in favour of another lot (e.g. right of carriageway, right to drainage)
- Reference the **registered document number** (e.g. `Easement J123456`) — you need to retrieve this to read the specific terms
- For design implications, record:
  - Purpose (sewer, drainage, access, services)
  - Width and location on the lot (usually shown on the Deposited Plan)
  - In whose favour (Water Corp, adjoining lot, etc.)
  - Whether building over the easement is permitted (usually not; occasional exceptions with written consent)

#### Restrictive covenants
- Private restrictions (typically in favour of the original subdivider or an adjoining lot)
- Common in Perth metro residential subdivisions (e.g. materiality, minimum floor area, "one dwelling per lot", building envelopes)
- **Difficult to remove**; binding on successors
- Common covenant terms:
  - Minimum floor area (e.g. 180 m² dwelling)
  - Roof material (e.g. no metal roof, or only Colorbond in certain colours)
  - External materials (e.g. brick face required, no render-only)
  - Front fence restrictions
  - Setback requirements beyond R-Codes DTS
  - "One dwelling per lot" — preventing subdivision
- Read the covenant document — do not rely on a summary

#### Mortgages
- Registered mortgage in favour of a lender
- Mortgagor consent is required for some activities (e.g. demolition, substantial alterations) — check loan terms
- Discharge on settlement

#### Caveats
- A warning lodged by someone claiming an interest
- Types: **caveat** (any claim), **absolute caveat**, **caveat prohibiting dealings**
- Must be dealt with before transfer
- Common sources: deposits held by a buyer, family disputes, charging orders

### 5. Memorials
Statutory markings that don't fit elsewhere. Most common in WA:

| Memorial | Meaning | Implications |
|---|---|---|
| **Contaminated Sites Act 2003** | DWER has classified the site | Phase 1 / 2 ESA likely required; disclosure on sale |
| **Heritage Act 2018** | State Registered Place | Heritage Council referral for works |
| **Tree Preservation Order** | LGA TPO on specific trees | Tree cannot be removed without LGA consent |
| **Planning and Development Act 2005 s. 150** | Conditional planning approval registered | Approval runs with the land |
| **Land Administration Act 1997** | Crown condition (e.g. resumption reserve) | Compulsory acquisition risk |
| **Aboriginal Heritage Act** | Heritage agreement or site | Statutory obligations under AHA |

Memorials are **not** easements or covenants — they are notifications of statutory status. They cannot be "removed" by agreement; they're removed only when the underlying statutory status changes.

## Strata and survey-strata titles

If the site is strata- or survey-strata titled:

- The site lot is shown on a **Strata Plan (SP)** or **Survey-Strata Plan (SSP)** rather than a Deposited Plan (DP)
- Common property is shared with other lots in the scheme — don't rely on the individual lot boundary alone
- **Scheme By-Laws** apply in addition to title — retrieve and review them
- **Body Corporate** (now "Strata Company") has management responsibility for common areas
- **Scheme Description** defines lots, common property, unit entitlements
- For strata residential works, strata company consent is usually required in addition to DA and building permit

## What to do with the findings

In the `/wa-property-report` output, the cadastre section should record:

1. Title identifier (Vol/Fol)
2. Lot / plan reference
3. Proprietor(s) and ownership structure
4. **Each encumbrance** with document number, type, and its design implication
5. **Each Memorial** with the underlying statute
6. Strata / by-laws if applicable
7. The date and reference of the Landgate search

For each encumbrance and Memorial, write a one-line **implication** — what this means for design. That's the part a client reads, not the document number.

## Escalation

Always recommend the client's conveyancing lawyer review the title before contract. This skill:
- Reads and summarises what's on the title
- Flags implications for design and feasibility
- Does **not** provide legal advice on whether encumbrances can be varied, removed, or worked around

## Useful links

- [Landgate Map Viewer Plus](https://maps.landgate.wa.gov.au/maps-landgate/registered/) — free public cadastre
- [WA Online Land Transactions](https://www0.landgate.wa.gov.au/) — paid certified searches
- [Landgate — Understanding Titles](https://www.landgate.wa.gov.au/property-reports-and-research/information-for-property-owners) — the agency's explainer
- [Landgate fee schedule](https://www.landgate.wa.gov.au/about-landgate/access-to-information/fees-and-charges) — current prices
