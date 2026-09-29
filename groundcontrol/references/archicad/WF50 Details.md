# WF50 Details

## Drawing Details

Choose the workflow based on the project's modelling depth and the nature of the detail.

**Preferred methods:**
1. Draw 2D details
2. Model based detail with viewpoint

Other methods are noted briefly below — for full guidance see the Graphisoft reference (GWG_Detailing.pdf, attached to the Bear note).

## 1. Draw 2D details

A 2D workflow similar to Drawn Independent Detail, except all details for a story or section are drawn together on one detail, rather than one detail per item.

### Workflow

**Step 1**
Create an independent detail viewpoint for each story and section that requires details. Save a view.

**Step 2**
Draw the 2D detail in place, using the plan or section view as a trace reference. Copy construction elements from the model into the detail to get started, then edit them.

**Step 3**
Place a cropped drawing of the view for each detail onto layouts.

**Step 4**
Place a linked marker on the plan or story (not the worksheet) and link it to the placed drawing.

### When to use
- Complex junction details where modelling is unlikely to achieve the correct outcome
- Less detailed models, where 2D embellishment is the primary method
- Standard or typical details unlikely to change with model updates

### Limitations
- No live model connection — update details manually when the design changes
- All content is static 2D; associative labels and element properties unavailable

## 2. Model based detail with viewpoint

Uses an enlarged source view with 2D enhancements added on a separate layer. The detail view is generated from — and must always be rebuilt from — the source view. Never edit directly in the detail view.

> The spA ArchiCAD template includes pre-set amplified views for Plan and Section Details (1:5, 1:10) and Stair Drawings (1:25).

### Workflow

![](WF50.1%20Model%20based%20detail%20with%20viewpoint/Pasted%20image%2020230131155116.png)

**Step 1**
Set up a model-based source view (floor plan or section) with appropriate settings — layer combination, scale, pen set, model view, graphic override, renovation status, partial structure display.

**Step 2**
In the source view, add 2D enhancements on detail layers (e.g. *5 Details*) — dimensions, associative labels, screws, membranes, library elements. These layers must be hidden in GA views.

**Step 3**
Place a **source marker** using the Detail Tool over the area to detail. Ensure *Copy construction elements only* is unticked to transfer 2D enhancements into the detail view.

> Make all subsequent changes in the source view only — never in the detail view. After any change, rebuild the detail via *Rebuild from model*.

**Step 4**
Save a viewpoint and place on a layout.

### When to use
- Model developed to high detail at junctions
- 1:20 level details (first level of detail)
- Where BIMx navigation and correct detail position matter
- Where element properties and associative labels should be queryable in labels

### Limitations
- Requires detailed modelling — unsuitable if junctions are not fully modelled
- Every model change requires a rebuild; editing the detail view directly breaks the connection
- Additional layers and layer combinations needed for detail-only elements
- Combining 1:20 and 1:5 from this method becomes complex — consider Drawn Independent Detail or Draw 2D details for the 1:5 level

## Other methods

Full guidance for these is in the Graphisoft reference (GWG_Detailing.pdf) — short notes only below.

**Drawn Independent Detail** — Fully 2D, no live model connection. One independent detail viewpoint per detail (compare to *Draw 2D details* above, which groups several details on one view). Use *Trace & Reference* to check alignment with the model while drawing. Good for standard or typical details and a reusable detail library.

**Drawn Copy of Detail with Source Marker** — For detail variations of the same base condition (e.g. same junction, different floor finishes). Places a source marker, then a consolidated copy of the generated content is dragged aside and annotated separately. Breaks the live model connection and loses correct position in BIMx — use only for variations; prefer *Draw 2D details* or *Model based detail with viewpoint* otherwise.

**Standard Detailing and External Details** — Import or link manufacturer and proprietary details (PDF or DWG) into a worksheet, then place directly onto a layout, or explode and edit into a model-based or drawn detail. SpA maintains a standard detail library in a separate ArchiCAD file on the server (Library section) — copy and paste details into the project file as needed.

## Numbering Details and Layout Techniques

### Numbering and Naming Details

**Rule:** Always set detail IDs and names in the **Project Map** only. Saved viewpoints in the View Map must always be set to *By Project Map*. This ensures cross-referencing is consistent across all layouts and controlled from a single location.

#### ID Format

The detail ID should identify the drawing series and the source location:

- `A50/0.01` — plan detail 01, Ground Floor
- `A55/A.01` — section detail 01, Section A
- `A55/Typ01` — typical section detail
- `A60/Bar01` — Bar Joinery detail
- `A80/01` — Window detail

#### Detail Names

Use a concise description of the content — e.g. *Wall Junction*, *Box Gutter*. No need to include the word 'Detail' in the name.

#### Marker and Layout Settings

- **Detail Markers:** reference the *first placed drawing of the selected viewpoint*; display *Drawing ID* and *Layout Name*
- **On the layout:** set Drawing ID to *By Layout*, Drawing Name to *By View: Name only*

### Detail Layout Techniques

A single source view can produce multiple placed drawings on a layout, and multiple source views can each contribute their own drawing. Two techniques cover most situations:

#### 1. One source view — multiple drawings

Several details are created in one view, then the placed viewpoint is cropped multiple times on the layout — each crop shows one detail and gets its own drawing title and automatic ID. Linked markers can be set up after placement.

Best for: detail libraries at small-to-medium project scale. Use sparingly on large projects — placing the same view repeatedly increases file size.

![](WF50.7%20Detail%20Layout%20Techniques/Pasted%20image%2020230202091404.png)

#### 2. Multiple source views — multiple drawings

Each detail has its own view, typically generated from the model (see *Model based detail with viewpoint*). Each view is placed individually on a layout.

This is the most common technique and the only one that fully supports detail marker navigation, auto-referencing, and correct BIMx position. Essential for any detail referenced from a GA plan or section.

![](WF50.7%20Detail%20Layout%20Techniques/Pasted%20image%2020230202091420.png)

**Other technique — one source view, one drawing:** all details drawn side by side in a single view, placed as one drawing; titles and numbers managed manually. Suits generic details with no model relationship (standard joinery types, door frame elevations, drawn profiles) and comparing variations. Detail markers can't be used for navigation — prefer the two techniques above where referencing matters.

#groundcontrol #groundcontrol/archicad
