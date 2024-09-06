---
title: "A50a2 3D Document Detail"
---
Another way of creating detail documentation based on the model is with the use of 3D Documents (3DD). 3DDs are 3D-based, but static documentation views, projected from a floor plan or a 3D window, which enable us to add dimensions, labels and graphical enhancements. This output can be more descriptive and understandable for contractors than a standard 2D detail drawing; it can still be part of a standard documentation set. 
We can display properties, classifications and other associated information using associative labels. 3DD-specific features include the ability to display hidden lines of elements, shadows and dimensioning of any plane in the 3D view.

![Pasted image 20230131161223](notes/1_Documentation%20Codex/1d_ArchiCAD/_assets/Pasted%20image%2020230131161223.png)

Step 1
Isolate a section of the model in a 3D view (perspective or axonometric) or a floor plan using the cutting planes and/or Marquee Tool.

Step 2
Create a 3D Document from that view. Apart from the settings inherited from the source view, we can define the appearance of the 3D Document from within its own settings. Save a view of the 3D Document with the required settings  (i.e. layer combination, scale, pen set, model view, graphic override, renovation status, partial structure display).

Step 3
In 3D Documents, place associative labels, dimensions, text or further embellish the document by adding images, fills and lines.

Step 4
The 3D Document view is placed on a layout in the same way as any other type of drawing.

![Pasted image 20230131162007](notes/1_Documentation%20Codex/1d_ArchiCAD/_assets/Pasted%20image%2020230131162007.png)

To avoid over modelling we can model in detail only those parts of the model from where the 3D Documents will be saved. The main reason for this is to avoid large numbers of polygons and the performance slowdowns caused by them.

ADVANTAGES:
- The 3D Document retains a live link to the model.
- All documentation is stored in the same file (unless another strategy is used to manage file sizes in large projects).
- All model information can be used as a basis for detail information.
- Element properties can be queried (e.g. using Labels) at the detailing level.
- Consistency among all views: floor plans, sections, elevations, details.
- A detailed model means better ability to schedule information.
- Easier management of details through naming and numbering.
- Best suited for very complex details that cannot be communicated in 2D.

DISADVANTAGES
- Annotations from the source view cannot be transferred to a 3D Document.
- Potentially large file size.
- Requires advanced and specialized modeling skills.
- Can be time-consuming to transfer information between similar details to achieve consistency across the project.
- It's not cost effective for black and white printing.
- Details don’t have correct relevant position when exported in BIMx.
- Cannot be used as a standard detailing workflow throughout an entire project.