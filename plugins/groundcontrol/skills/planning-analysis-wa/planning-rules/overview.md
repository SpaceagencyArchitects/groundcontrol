# WA Planning Framework — Overview

The Western Australian planning system is layered. Any development site is controlled by several instruments stacked on top of each other, and the analysis has to check each layer in order. This primer summarises the system at the level needed for envelope analysis.

## The hierarchy

From highest to lowest, each layer can only make things *more* restrictive than the one above it unless the lower instrument is expressly enabled to vary the higher:

```
┌─────────────────────────────────────────────────────────────────┐
│ State legislation                                               │
│   Planning and Development Act 2005 (WA)                        │
│   Planning and Development (LPS) Regulations 2015 (deemed prov.)│
│   Building Act 2011 / Building Regulations 2012                 │
│   Heritage Act 2018                                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Regional Schemes (where applicable)                             │
│   Metropolitan Region Scheme (MRS) — Perth metro                │
│   Peel Region Scheme (PRS)                                      │
│   Greater Bunbury Region Scheme (GBRS)                          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ State Planning Policies (SPPs)                                  │
│   SPP 3.7 Bushfire  · SPP 2.6 Coastal  · SPP 5.4 Noise          │
│   SPP 7.0 Design WA · SPP 7.3 R-Codes (Vol. 1 & 2)              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Local Planning Scheme (LPS) — one per LGA                       │
│   Zoning map · Table of Uses · Scheme text                      │
│   Special Control Areas · Additional Use Areas                  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Local Planning Policies (LPPs)                                  │
│   LGA-specific policies — often override deemed provisions      │
│   Heritage area policies · Design guidelines                    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Structure Plans / Activity Centre Plans / LDPs                  │
│   Precinct-scale controls, only where declared                  │
└─────────────────────────────────────────────────────────────────┘
```

## What each layer controls

| Layer | Controls | How it shows up |
|---|---|---|
| Act & Regulations | What must happen: DA assessment, deemed provisions, appeal rights | *Planning and Development Act 2005* ss. 162, 211; Regs Sch. 2 (deemed provisions) |
| MRS / Regional Scheme | Broad zone (Urban, Industrial, Rural) & reservations (Parks & Rec, Railways) | WAPC MyPlan viewer |
| SPPs | State-level overlays: bushfire, coastal, noise, R-Codes, Design WA | Apply everywhere, referenced in LPS |
| LPS | Specific zone (e.g. Mixed Use, R60), use table (P/D/A/X), bulk controls | LGA zoning map + Scheme text |
| LPPs | Area-specific variations — heritage, built form, sign controls | LGA website — "Local Planning Policies" |
| Structure Plan | Precinct controls for activity centres, LSP areas | Referenced in LPS |

## Deemed provisions (2015 Regs Sch. 2)

The *Planning and Development (Local Planning Schemes) Regulations 2015* attach a **Schedule 2 — deemed provisions** that apply to every LPS in WA unless expressly modified. The deemed provisions cover:

- Development applications (what triggers, what's exempt)
- Assessment procedure (timeframes, advertising, referrals)
- Decision-making bodies and delegations
- Amendments, structure plans, LDPs
- Interpretation rules

An LPS may have its own text too, but the deemed provisions always apply. Cite them as `Schedule 2 of the *Planning and Development (Local Planning Schemes) Regulations 2015* (WA), cl. [x]`.

## R-Codes — how they sit in the stack

The R-Codes (SPP 7.3) are a State Planning Policy incorporated by reference into every LPS in WA (including via the deemed provisions). They control:

- **Vol. 1** — Single houses and grouped dwellings (R5–R100+)
- **Vol. 2** — Apartments (R30+ with ≥4 storeys, or R-AC0 / R-AC1 / R-AC2 / R-AC3)

The R-Code for a site is set by the LPS zoning map (often as `Residential R40` or similar, or implicitly via the zone definition). Where an LPS assigns both a Vol. 1 and a Vol. 2 code (e.g. "R60/R-AC3"), **either pathway** is available to the applicant — choose the one that best suits the proposal.

## Use permissibility — P / D / A / X

Every LPS has a Table of Uses (or Zoning Table) that lists use classes across the rows and zones across the columns. Each cell shows:

| Code | Meaning | Advertising |
|---|---|---|
| P | **Permitted** — use is permitted if it meets all deemed provisions and R-Code DTS | Not required |
| D | **Discretionary** — may be approved at the discretion of the Responsible Authority | Sometimes |
| A | **Advertised discretionary** — as D, plus mandatory public advertising | Required |
| X | **Not permitted** — use is prohibited | — |

Note: many older LPSs used `P`, `AA`, `SA`, `IP` etc. If the LPS is older, translate to the current system and cite the original code. Use classes are defined in the LPS glossary or the Regulations Sch. 2 cl. 1.8.

## Responsible Authority

Who decides a DA depends on value, type, and location:

| Authority | When |
|---|---|
| Local government (LGA) | Default for most DAs; delegated to officers for minor, to Council for complex |
| Joint Development Assessment Panel (JDAP) | Estimated cost of development ≥ $10M is mandatory; opt-in between $2M (residential) / $20M (other) and $10M. Per *Planning and Development (DAP) Regulations 2011* |
| WAPC | Strata / survey-strata subdivision; MRS reservations; regional scheme applications; SAIs |
| Heritage Council of WA | State Registered Places require Heritage Council referral under *Heritage Act 2018* |
| Minister for Planning | Called-in applications; Section 76 / 211 actions |

Appeals go to the **State Administrative Tribunal (SAT)** within 28 days of determination — or 60 days after deemed refusal.

## Typical DA timelines (statutory)

| Pathway | Timeframe |
|---|---|
| DA without advertising | 60 days |
| DA with advertising | 90 days |
| Major development (JDAP) | 60 days from "responsible authority" date (often longer in practice) |
| Subdivision (WAPC) | 90 days |

In practice, clock-stops for Requests for Information and requests for extensions of time are common. Assume 6–12 months from lodgement to determination for a mid-complexity DA; longer for heritage or JDAP.

## What this skill assumes

This skill assumes the user will supply:

1. The address, LGA, lot no./DP no. (from Landgate)
2. The MRS zone (from MyPlan WA)
3. The LPS zone and R-Code (from the LGA's online viewer or the LPS zoning map PDF)
4. Heritage status (from inHerit and the LGA Local Heritage Survey)
5. BPA status (from DFES)

The skill then applies the bundled R-Codes, LPS, and deemed provisions to compute the envelope. This is a **preliminary** analysis only — detailed design and any formal submission must be verified by a registered architect and the relevant specialist consultants.
