# ArchiCAD layouts and drawings

- see [[Sheet Numbering]] for drawing numbers

## Naming viewpoints (Project Map)

Each new viewpoint is created and named (ID and Name) in the Project Map. Convention varies by type:

| View type | ID | Name |
|---|---|---|
| Stories | Set automatically, based on storey position in model | Describes storey position (e.g. Ground Floor, Mezzanine, Roof) |
| Sections & Elevations | Identifies function / position in drawing set (A20 = GA elevations, A30 = GA sections, A50 = Detail sections) | Describes elevation/section (e.g. Section A, North Elevation) |
| Interior Elevations | Identifies location by zone — use `<Zone Number>` or enter manually | `<Zone Name> <Number>` — Zone Name can be overridden, Number should not be |
| Worksheets & Details | Identifies drawing type (A50 = Plan detail, A55 = Section detail, A65 = Joinery detail) and detail reference number (for section details, include section ID, eg A55/A1 is detail 1 on Section A) | Short description of the drawing |

> **View Map:** leave ID and Name set to 'By Project Map' unless there's a specific reason to vary it (e.g. a second view of a section used outside its original A30 context, to generate A55 section details).

## Placing drawings on layouts

General setup — applies to every drawing:

- Don't change drawing scale — it's set by the viewpoint.
- Include Scale in Autotexting and Indexes, unless the drawing has an odd scale or departs from the layout's main scale (e.g. a 1:5 detail on a 1:25 room layout). ![](ArchiCAD%20layouts%20and%20drawings/image%204.png)
- Anchor Point: use Drawing's internal origin as anchor — this stops the drawing floating if the viewpoint changes. ![](ArchiCAD%20layouts%20and%20drawings/image%205.png)

| Drawing type | Drawing ID | Drawing Name | Drawing title |
|---|---|---|---|
| GA plans & elevations | By Layout, ID style '1, 2, 3, …' | By View: Name only | Only if more than one plan or elevation on the sheet. Show name only — switch off ID and scale. |
| Sections | By Layout, ID style 'A, B, C, …' | By View: Name only | Only if more than one section on the sheet. Show ID and name only. |
| All other drawings | By Layout | By View: Name only | Show ID and Name. Add scale only if it departs from the layout's general scale (e.g. a 1:5 detail on a 1:25 room layout). |

## Reference: what the Navigator tabs are

![](ArchiCAD%20layouts%20and%20drawings/image.png)

The four icons in ArchiCAD's Navigator tabs, from left to right:

**Project Map** (house icon) — every viewpoint in the project, organized into folders (Stories, Sections, Elevations, Details, Worksheets, 3D Documents, etc). Reflects the model's actual structure.

**View Map** (house-in-frame icon) — Views: saved, named versions of Project Map viewpoints with display settings attached (scale, layer combination, dimensions, etc), ready to place on layouts.

**Layout Book** (folded-page icon) — Layouts: the actual sheets used for printing, plotting or PDF export, onto which Views are placed as Drawings.

**Publisher Sets** (stacked-pages icon) — curated collections of Views or Layouts, bundled for output (PDF, DWG, BIMx).

All four are linked: a change in the model propagates through the Project Map into any Views, Layouts, and Publisher items built from it.

#groundcontrol #groundcontrol/archicad
