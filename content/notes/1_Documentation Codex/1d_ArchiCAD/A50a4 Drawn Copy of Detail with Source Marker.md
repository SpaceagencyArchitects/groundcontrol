---
title: "A50a4 Drawn Copy of Detail with Source Marker"
---
This method starts with placing a source detail marker to generate 2D content in a detail viewpoint. The 2D content will then be copied and completed with 2D elements like fills, lines, dimensions, labels, etc.

This workflow is good for detail variations (e.g. same cladding type, different floor finish, which are shown in several variations of the same detail).
Otherwise this workflow should be avoided, as changes cannot be tracked easily, details must be updated manually and can therefore become disassociated from the model and design intent.
This method also shifts the detail content relative to its position in the BIMx model.

## Workflow##

![Pasted image 20230131171600](notes/1_Documentation%20Codex/1d_ArchiCAD/_assets/Pasted%20image%2020230131171600.png)

Step 1
Place a **source** detail marker (Marker type: ‘Create a new detail viewpoint’) on a plan or section view.

Step 2
The detail viewpoint is generated with 2D content from a source view. Before any editing and copying takes place, it is useful to consolidate the lines and fills (*ArchiCAD menu 'Edit > Reshape > Linework Consolidate and Fill Consolidate'*) of the detail drawing to erase duplicate elements and clean up the drawing. Next, drag a copy of the generated content to the right side to edit and add more elements and annotations (dimensions, labels, etc.) to complete the detail.

Step 3
Save a view of the detail with the appropriate settings (i.e. layer combination, scale, pen set, model view, graphic override, renovation status, partial structure display) and place it onto a layout.

If the model changes, import the changes into a detail viewpoint using the ‘Rebuild from Source View’ option from the detail's context menu (right-click an empty area of the detail view). The rebuild process should only affect the original content and not the copied and additional content.

ADVANTAGES
- Referencing between detail markers and detail drawings makes navigation easy.  
- Easier management of details through naming and numbering.
- All documentation is stored in the same file (unless another strategy is used to manage file sizes in large projects).
- Models can be more basic and developed much faster without detailed modelling of junctions and specific elements.
- Easier navigation with the use of source markers, auto-referencing is possible.
- The number of polygons in the model is lower.
- We can engage the team members with less modelling skills for the detail creation.
- We can copy elements from other details.
- Use of Trace & reference is convenient to maintain relationship with model views.
- No additional layers and layer combinations are necessary for separating detail enhancement elements.
- Smaller file size, as details are placed on layouts, not cropped views.
- Best suited for generating the second level (e.g. 1:5) of details.

DISADVANTAGES
- Only some parts of the model information can be used as a basis for the detail.
- Details don’t have a live connection to the model. They must be manually updated to reflect changes from the model.
- Everything becomes 2D elements so model element information is not available and associative labels cannot be used.
- Can be time-consuming to transfer information between similar details to achieve consistency across the project.
- Time consuming if there are a lot of changes in the project.
- Results in a larger Project Map tree, requiring a consistent and logically-structured naming convention to be adopted by the project.
- We need to keep track of the model and the details’ consistency.
- Details don’t have correct relevant position when exported in BIMx.
- Not ideal for generating 1:20 details, as most of the time these are project-specific, and they heavily depend on the model content and updates.