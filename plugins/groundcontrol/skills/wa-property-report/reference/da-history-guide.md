# DA History & SAT Decisions — guide

Reference for the approval-history section of `/wa-property-report`. Knowing what's been tried on a site before is often the single most useful piece of DD for design strategy.

## Why it matters

The approval history of a site (and its neighbours) tells you:

- What the Responsible Authority has approved, refused, and on what grounds
- Whether conditions of existing approvals restrict what can be done
- Whether there's a live approval that hasn't been commenced (valid for 2 years in WA, extensions possible) — this may be sold with the site
- What the LGA heritage officer, environmental officer, traffic engineer etc. have said in past assessments
- Whether an SAT appeal has happened that establishes precedent

You can walk into pre-lodgement meetings with far more confidence if you know the RA's historical position on the street.

## Sources

### 1. LGA DA register

Every LGA in WA publishes a **development application register**. The format varies — most use online searchable portals, a few still rely on PDF lists.

Typical register fields:
- DA reference number
- Lodgement date
- Description
- Site address
- Applicant
- Status (pending, approved, refused, withdrawn, modified)
- Determination date
- Decision-making body (delegated officer, Council, JDAP)
- Advertising status

**Perth metro LGAs with searchable DA portals (examples):**

| LGA | Portal approach |
|---|---|
| City of Fremantle | Planning Portal — public search by address |
| City of Perth | DAPS — online DA tracking |
| City of Stirling | Planning portal — register search |
| Town of Vincent | Planning application tracking |
| City of Subiaco | Online planning search |
| City of Nedlands | Planning applications register |
| City of Joondalup | DA tracker |
| City of Swan | Planning online |
| City of Bayswater | Tracking search |
| Town of Cottesloe | Planning applications register |

**Check the LGA's website** directly — URLs change and the search mechanics differ. Some LGAs require an account for deep search; most are public.

### 2. Building permits (BPs)

Building permits are issued under the *Building Act 2011* (WA), **separately** from DAs. A DA approval gives planning consent; a BP authorises construction. Most LGAs publish a BP register too.

BPs are useful DD because:
- They identify what was actually built, not just what was approved
- Minor works (e.g. internal alterations, re-roofing) may not need a DA but do need a BP
- The BP register often records footings, slab, framing inspections — useful for understanding the current condition

### 3. SAT — State Administrative Tribunal

SAT hears appeals against planning and building decisions under:
- *State Administrative Tribunal Act 2004* (WA)
- Various enabling Acts (Planning and Development Act, Building Act, Heritage Act)

[SAT website](https://www.sat.justice.wa.gov.au/) publishes:
- Decisions database (searchable)
- Lists of current matters

**Types of appeal:**
- Review of decision (refused DA, conditions disputed)
- Deemed refusal (RA didn't decide within statutory time)
- Enforcement (direction to remove / undo works)
- Compensation (injurious affection)

**For DD, check:**
- Has this site been before SAT? Appeal outcome affects what's been settled
- Have similar sites / nearby sites been before SAT on similar issues? Precedent

SAT decisions are **persuasive precedent** — not binding like court decisions, but influential. An LGA that refused at delegated level, then had SAT overturn the refusal, will often quietly approve similar proposals after that.

### 4. Heritage Council decisions (if heritage-listed)

If the site is State Registered, the Heritage Council's register of referrals and decisions is published. Similar logic to SAT precedent — knowing what the HC has approved before on your site or nearby is valuable.

## How to search the LGA register

A typical workflow:

1. Go to the LGA planning portal
2. Enter the address (different portals accept different formats — try street number + street name without suburb first)
3. Note the **5–10 most recent DAs** on the site
4. Look for:
   - Current / pending (live approvals, advertising, etc.)
   - Recently approved (within 2 years — approval validity period)
   - Recent refusals (why? read the officer's report if available)
   - Modifications / s. 75 amendments to past approvals
5. Click into each DA and download or note:
   - The officer's report / Statement of Planning Justification
   - Conditions of approval
   - Any specialist reports (heritage, traffic, environmental)

For a thorough DD, go back 10 years. Older is usually less relevant (LPS amendments supersede).

## How to search SAT

1. Go to [SAT decisions search](https://www.sat.justice.wa.gov.au/)
2. The search is **by case name or reference**, not by address
3. Workaround for address search:
   - Search by the **LGA name + street name** as keywords (e.g. "Fremantle" + "Swanbourne")
   - Search by the **applicant name** if known
   - Search by the **registered proprietor name** if known
4. Filter by subject area (Development — Planning; Development — Building)

SAT decisions include the facts, the law, and the Tribunal's reasoning. They're worth reading in full when relevant.

## Adjacent site checks

Don't limit the search to just your site. Check:

- **Immediate neighbours** (2–3 lots each side, the directly opposite block)
- **Same streetscape** (the rest of the street block)
- **Same heritage area / precinct** — if applicable
- **Similar zones nearby** — if your site is one of only a few R-AC3 lots in the suburb, see what others have built

## What the skill captures

In the `/wa-property-report` output, the DA history section should record:

1. **This site — current** — any DA currently lodged or under assessment
2. **This site — historical** — DAs approved, refused, modified in the last 10 years
3. **Conditions to watch** — any active approval with conditions that bind the site (e.g. heritage covenants, landscape conditions)
4. **Refusal reasons** — if any recent refusals, summarise the officer's / Council's reasons
5. **Building permits** — notable recent BPs
6. **SAT — this site** — any appeals on this site, with outcome
7. **SAT — precedent** — relevant appeals on similar / nearby sites
8. **Implications** — what this history tells you about the RA's likely approach to the proposed scheme

## Useful links

- [State Administrative Tribunal](https://www.sat.justice.wa.gov.au/) — appeal decisions
- Each LGA's DA register — check the LGA's website
- [Heritage Council of WA decisions](https://www.wa.gov.au/organisation/heritage-council) — heritage-listed places
- [JDAP determinations](https://www.wa.gov.au/organisation/department-of-planning-lands-and-heritage/development-assessment-panels) — JDAP minutes and determinations

## Useful notes

- **Approval validity**: 2 years from the date of grant, under Sch. 2 of the *Planning and Development (LPS) Regulations 2015*. An applicant can apply for an extension, usually granted once. Second extensions are harder
- **s. 75 amendments**: minor modifications to an approved DA can be processed as an amendment rather than a new DA — saves time but limited in scope
- **Deemed refusal**: if the RA doesn't decide within 60/90 days (depending on advertising), the applicant can treat it as a refusal and appeal to SAT
- **Commencement**: 'substantial commencement' within 2 years keeps the approval alive indefinitely. The bar for 'substantial' is surprisingly low (site works, footings) — don't assume a site with a 3-year-old approval is back to zero
