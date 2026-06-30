# WF50 Details

## Drawing Details

The preferred approach is to extract details from the model with minimal 2D work. Model-based details allow element properties, classifications and descriptions to be displayed directly — but require a well-developed model and good BIM skills. For projects with less detailed models, 2D-based workflows are a practical alternative.

Choose the workflow based on the project's modelling depth and the nature of the detail:

---

## 1. Model Based Detail with Viewpoint

The preferred workflow where the model has been developed to sufficient detail. Uses an enlarged source view with 2D enhancements added on a separate layer. The detail view is generated from — and must always be rebuilt from — the source view. Never edit directly in the detail view.

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
- Combining 1:20 and 1:5 from this method becomes complex — consider [workflow 3 (Drawn Independent Detail)](#3-drawn-independent-detail) for the 1:5 level

---

## 2. 3D Document Detail

Use for complex conditions that cannot be adequately communicated in a standard 2D section or plan — where a 3D view genuinely aids contractor understanding. 3D Documents are static projected views, not live connections. They support associative labels, hidden lines, shadows, and dimensioning in any plane.

To manage file size and performance, model in detail only the parts of the model that will be used as 3D Document sources.

### Workflow

![](WF50.2%203D%20Document%20Detail/Pasted%20image%2020230131161223.png)

**Step 1**
Isolate the relevant part of the model using cutting planes and/or the Marquee Tool in a 3D or floor plan view.

**Step 2**
Create a 3D Document from that view. Define its appearance in the 3D Document settings — layer combination, scale, pen set, model view, graphic override, renovation status.

**Step 3**
Add associative labels, dimensions, text, images, fills and lines within the 3D Document.

**Step 4**
Place the 3D Document view on a layout in the same way as any other drawing.

![](WF50.2%203D%20Document%20Detail/Pasted%20image%2020230131162007.png)

### When to use
- Complex junctions or assemblies where a 2D detail would be unclear
- Selectively, as a supplement to the standard 2D set — not as the primary detailing method

### Limitations
- Requires advanced modelling skills and detailed model geometry
- Annotations from the source view cannot be transferred into the 3D Document
- Large file sizes
- Poor result for black and white printing
- Details do not have correct position in BIMx

---

## 3. Drawn Independent Detail

A fully 2D workflow. Details are drawn from scratch in an independent detail viewpoint, with no live connection to the model. Use *Trace & Reference* to check alignment with the model during drawing without creating a connection.

Use for standard or typical details that are unlikely to change with model updates, and for building or reusing a standard detail library.

### Workflow

![](WF50.3%20Drawn%20Independent%20Detail/Pasted%20image%2020230131171804.png)

**Step 1**
Create an independent detail viewpoint.

**Step 2**
Draw the detail using 2D document tools. Use *Trace & Reference* to reference model views for alignment if needed.

**Step 3**
Place the detail on a layout.

**Step 4**
Place a linked marker using the Detail Tool on the relevant model view, pointing to the drawing on a layout.

### When to use
- Standard or typical details independent of project-specific model content
- 1:5 details (not 1:20 — those are project-specific and depend on model updates)
- Building or drawing from a standard detail library
- Projects with less detailed modelling
- Incorporating external or supplier details (see [workflow 5](#5-standard-detailing-and-external-details))

### Limitations
- No live model connection — details must be manually updated when the design changes
- All content is static 2D; associative labels and element properties unavailable
- Consistency between model and details must be actively maintained

---

## 4. Drawn Copy of Detail with Source Marker

Use this workflow for **detail variations** — where the same base condition needs to be shown in several near-identical versions (e.g. the same junction with different floor finishes). For all other cases prefer [workflow 1 (Model Based Detail)](#1-model-based-detail-with-viewpoint) or [workflow 3 (Drawn Independent Detail)](#3-drawn-independent-detail). This method breaks the live model connection and makes revision tracking difficult.

Note: content copied using this method loses its correct position in BIMx.

### Workflow

![](WF50.4%20Drawn%20Copy%20of%20Detail%20with%20Source%20Marker/Pasted%20image%2020230131171600.png)

**Step 1**
Place a **source** detail marker (type: *Create a new detail viewpoint*) on a plan or section view.

**Step 2**
Before editing, consolidate the generated content to remove duplicate elements:
*Edit > Reshape > Linework Consolidate* and *Fill Consolidate*.

Then drag a copy of the consolidated content to one side and annotate the copy (dimensions, labels, fills). Leave the original generated content untouched — it must remain clean for rebuilds to work correctly.

**Step 3**
Save a view with the required settings (layer combination, scale, pen set, model view, graphic override, renovation status) and place on a layout.

> **Model changes:** rebuild the source content via right-click > *Rebuild from Source View* in the detail viewpoint. The rebuild updates only the original generated content — copied annotations are not affected.

### When to use
- Detail variations of the same base condition
- 1:5 details (not 1:20 — those are too project-specific and model-dependent for this approach)
- Less detailed models where 2D embellishment is the primary method and polygon count matters

### Limitations
- No live model connection — changes must be manually identified and applied
- All content is static 2D; associative labels and element properties unavailable
- Details can drift from design intent over time; consistency requires discipline
- Incorrect position in BIMx

---

## 5. Standard Detailing and External Details

Manufacturer and proprietary details (typically .pdf or .dwg) can be incorporated into the drawing set in two ways:

1. **Import or link** into a worksheet as an external drawing or hotlink, then place directly onto a layout as part of the documentation set.
2. **Explode and edit** — link and explode into a worksheet to modify, embellish, or incorporate as 2D content into a model-based or drawn detail.

SpA maintains a standard detail library in a separate ArchiCAD file on the server (Library section). Copy and paste details directly into the project file as needed.

---

## Numbering and Naming Details

**Rule:** Always set detail IDs and names in the **Project Map** only. Saved viewpoints in the View Map must always be set to *By Project Map*. This ensures cross-referencing is consistent across all layouts and controlled from a single location.

### ID Format

The detail ID should identify the drawing series and the source location:

- `A50/0.01` — plan detail 01, Ground Floor
- `A55/A.01` — section detail 01, Section A
- `A55/Typ01` — typical section detail
- `A60/Bar.01` — Bar Joinery detail
- `A80/01` — Window detail

### Detail Names

Use a concise description of the content — e.g. *Wall Junction*, *Box Gutter*. No need to include the word 'Detail' in the name.

### Marker and Layout Settings

- **Detail Markers:** reference the *first placed drawing of the selected viewpoint*; display *Drawing ID* and *Layout Name*
- **On the layout:** set Drawing ID to *By Layout*, Drawing Name to *By View: Name only*

---

## Detail Layout Techniques

A single source view can produce multiple placed drawings on a layout, and multiple source views can each contribute their own drawing. Three techniques cover most situations:

### 1. One source view — one drawing

All details are created side by side in a single view (independent detail or worksheet). One viewpoint is placed as a single drawing on the layout. Titles and numbers are managed manually.

Best for: generic details with no live model relationship — standard joinery types, door frame elevations, drawn profiles. Easy to create and compare variations of similar details.

Drawback: detail markers cannot be used for in-project navigation, making it hard to find or jump to a specific detail.

![](WF50.7%20Detail%20Layout%20Techniques/Pasted%20image%2020230202091307.png)

### 2. One source view — multiple drawings

Several details are created in one view, then the placed viewpoint is cropped multiple times on the layout — each crop shows one detail and gets its own drawing title and automatic ID. Linked markers can be set up after placement.

Best for: detail libraries at small-to-medium project scale. Use sparingly on large projects — placing the same view repeatedly increases file size.

![](WF50.7%20Detail%20Layout%20Techniques/Pasted%20image%2020230202091404.png)

### 3. Multiple source views — multiple drawings

Each detail has its own view, typically generated from the model (see [workflow 1](#1-model-based-detail-with-viewpoint)). Each view is placed individually on a layout.

This is the most common technique and the only one that fully supports detail marker navigation, auto-referencing, and correct BIMx position. Essential for any detail referenced from a GA plan or section.

![](WF50.7%20Detail%20Layout%20Techniques/Pasted%20image%2020230202091420.png)

#groundcontrol #groundcontrol/archicad
