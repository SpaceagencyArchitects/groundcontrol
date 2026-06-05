# Tagging of Elements in ArchiCAD

## Three Tracks

ArchiCAD uses three distinct mechanisms to tag and code building elements. Each track serves a different purpose and outputs information differently.

| Track | Mechanism | Elements | Code Source | Primary Output | Naming Convention |
|---|---|---|---|---|---|
| **1A — Type / Construction** | Composite or Complex Profile | Wall Type · Ceiling Type · Roof Type · Flooring System | Auto-generated from `[bracket]` in composite/profile name | Code label on drawings; per-sheet + master keynote legend | `WT[E1] - External wall with timber cladding` |
| **1B — Type / Construction** | Keynote | Wall Protection · Joinery Type · Handrail/Balustrade · Joinery Finish · Sanitary Fixture | Keynote | Code label on drawings; per-sheet + master keynote legend | `[TRM-01] - 90×18 MDF skirting` |
| **2 — Applied Finish** | Surface attribute | Wall Finish · Paint Colour · Floor Finish | Auto-generated from `[bracket]` in surface name | Code label on drawing; manual entry in A80 schedules | `[TIL-1] - Honed white tile` |
| **3 — Scheduled Element** | Element ID (manually set) | Door · Window · Electrical Fixture | Set manually | Interactive schedule (A70) | `123.1` (door), `W01` (window) |


## Keynotes
In ArchiCAD, each keynote is made up of the following information.
* a Code (see [[Abbreviations and Codes]])
* Title - brief description of item (for keynote legends)
* Description (for labels to go on drawings)
  * Scheduled element/finish - refer to schedule, typically for items labelled using code only, eg paint finishes, tiles, sanitary or tapware items or composites, eg wall types, ceilings, cladding.
  * System or complex item - detailed description to be used in label
* Natspec reference or [[A80 - Schedules]] Number

## Codes
For the full list of system, material and finish codes used in the spA drawing set, see [[Abbreviations and Codes]].

## Element Table

| Element               | Sub-type                     | Track  | Code Source                 | Code Example                                                 | Schedule                                                     | Drawing Annotation                                           | Notes                                                        |
|-----------------------|------------------------------|--------|-----------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Wall Finish           | Covering / Tiling / Cladding | 2      | Surface attribute           | `[TIL-1]`, `[COV-1]`, `[CLAD-1]`                             | Manual entry in A80 schedule                                 | Code label on A60 elevations                                 |                                                              |
| Paint                 | Type — wall and ceiling      | 1*     | Keynote                     | `PT1`                                                        | Manual entry in A80 or specification                         | Key label on A60 elevations and A14 ceilings                 | *Not composite-derived. Spec covers paint system. Covers wall and ceiling paint types. |
| Paint                 | Colour                       | 1B + 2 | Keynote + Surface attribute | `PT-W1/04`<br>PT-W1 = Keynote<br>04 = surface code, eg 'COL[04] - Black Caviar' | PT = Manual entry in specification (type of paint only)<br>COL = Keynote schedule on legend or Colour schedule in A80 | Colour code appended to paint key label: `PT1/04`            | Colour lives in A80 and legend only.                         |
| Wall Type             | Type                         | 1      | Composite + Keynote         | `WT[E1] - External wall with cladding`                       | 2D drawing with full keynote labels on A00 legend sheet      | Code label on A10 plans                                      | Covers internal, external, and partition wall types. Use interactive schedule for checking only. |
| Wall Protection       | Type                         | 1      | Complex Profile + Keynote   | `[TRM-01] - 90×18 MDF skirting`, `[TRM-02] - Powder-coated crash rail` | Per-sheet keynote legend on A60; master keynote schedule on A00 | Key label on A60 elevations                                  | TRM codes cover skirtings, architraves, crash rails, corner guards, wall capping. Fold finish description into keynote — no separate finish row. |
| Ceiling Type          | Type + FCL                   | 1      | Composite + Keynote         | `[CLG-P1] - Suspended plasterboard`                          | 2D drawing with full keynote labels on A00 legend sheet      | Code label on A14 RCPs                                       | FCL annotated separately via label/dimension. Use interactive schedule for checking only. |
| Roof Type             | Type                         | 1      | Composite + Keynote         | `[RFS-01] - Standing seam metal`                             | 2D drawing with full keynote labels on A00 legend sheet      | Code label on A10 roof plans                                 | Use interactive schedule for checking only.                  |
| Flooring System       | Substrate / Build-up         | 1      | Composite                   | `[FLS-01] - 20mm timber on battens`                          | 2D drawing with full keynote labels on A00 legend sheet      | Code label on A60/A10 plans                                  | Covers substrate and build-up only. Finish covered by Floor Finish row. Use interactive schedule for checking only. |
| Floor Finish          | Finish                       | 2      | Surface attribute           | `[FL-1]`, `[TIL-2]`, `[CPT-1]`                               | Manual entry in A80 schedule                                 | Code label on A60/A10 plans                                  |                                                              |
| Joinery               | Type                         | 1      | Keynote                     | `JN[K1] - Kitchen joinery`                                   | Per-sheet keynote legend on A60; interior master keynote on A60 legend sheet | Key label on A65/A10 plans                                   | Reference to A65 in keynote.                                 |
| Joinery               | Finish                       | 2      | Keynote                     | `[JF-01]`, `[MTF-01]`, `[LAM-01]`                            | Per-sheet keynote legend on A60; interior master keynote on A60 legend sheet; manual entry in A80 schedule | Key label on A60 elevations                                  |                                                              |
| Handrail / Balustrade | Type                         | 1      | Keynote                     | `HR-1`, `HR-2`                                               | Per-sheet keynote legend on A40/A60; master keynote schedule on A00 | Key label on A40 drawings                                    | Finish folded into keynote description — finish is invariant per type. No separate finish row. |
| Window                | Number + Type                | 3      | Element ID + type property  | `W01`, `101.W1`                                              | A70 interactive schedule + 2D type elevation in A70 Part 1   | Number label on A10 GA plans and A20 external elevations     |                                                              |
| Door                  | Number + Type                | 3      | Element ID + type property  | `123.1`                                                      | A70 interactive schedule + 2D type elevation in A70 Part 1   | Number label on A10 GA plans                                 |                                                              |
| Electrical Fixture    | Type                         | 3      | Element ID                  | `LT-01`, `GP-01`                                             | Manual entry in A80 lighting schedule (or refer to consultant) | Code label on A14 RCPs, A16 electrical drawings and A60 room layouts |                                                              |
| Sanitary Fixture      | Type                         | 3      | Keynote                     | `SW-01`                                                      | Per-sheet keynote legend on A60; interior master keynote on A60 legend sheet; manual entry in A80 schedule | Key label on A60 room layouts                                |                                                              |

#groundcontrol #groundcontrol/principles #groundcontrol/archicad
