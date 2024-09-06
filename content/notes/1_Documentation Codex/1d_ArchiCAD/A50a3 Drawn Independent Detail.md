---
title: "A50a3 Drawn Independent Detail"
---
Drawing independent details resembles traditional way of 2D drawing. 
We can use ArchiCAD's Trace & Reference to reference model views as a base for a detail we are working on and to ensure that the detail - when referenced using a linked detail marker - appears in the correct relevant location in the BIMx model.
Several related details can be drawn on a a single detail view.

Starting from an independent detail view may be a suitable workflow for fixed standard or typical details, in particular where changes caused by rebuilding the detail from the model source are undesirable.

An independent detail viewpoint can be linked to a detail marker by placing a linked marker type onto a model view and pointing it to the placed drawing of the independent detail's viewpoint on a layout. 

Manually drawn details require manual changes during revisions.

## Workflow##

![Pasted image 20230131171804](notes/1_Documentation%20Codex/1d_ArchiCAD/_assets/Pasted%20image%2020230131171804.png)
Step 1
Create an independent detail viewpoint.

Step 2
Draw a detail using available 2D document tools. Trace & Reference option can be handy to reference the model views if needed.

Step 3
Place linked marker with the use of the detail tool on the model view and link it to the independent detail viewpoint. 

Step 4
Place the detail onto a layout.

ADVANTAGES

- Referencing between detail markers and detail drawings makes navigation easy. 
- Easier management of details through naming and numbering.
- All documentation is stored in the same file (unless another strategy is used to manage file sizes in large projects).
- Models can be more basic and developed much faster without detailed modelling of junctions and specific elements.
- The number of polygons in the model is lower.
- We can engage the team members with less modelling skills for the detail creation.
- We can copy elements from other details or bring external content into our file.
- Details created this way can easily be included as part of a standard detail library. 
-  No additional layers and layer combinations are necessary for separating detail enhancement elements.
- Smaller file size, as details are placed on layouts, not cropped views.
- Best suited for generating the second level (e.g.1:5) of details.

DISADVANTAGES

- Only some parts of the model information can be used as a basis for the detail.
- Details don’t have a live connection to the model. They must be manually updated to reflect changes from the model.
- Everything becomes 2D elements, so model element information is not available and associative labels cannot be used.
- Can be time-consuming to transfer information between similar details to achieve graphical consistency across the project.
- Time consuming if there are a lot of changes in the project.
- The information we add to the detail cannot be viewed in the main model views, as the link is not bi- directional and there is no connection to other views (e.g. sections, elevations).
- We need to keep track of the model and the details’ consistency.
- Might result in a larger Project Map tree, requiring a consistent and logically-structured naming convention to be adopted by the project.
- Details don’t have correct relevant position when exported in BIMx.
- Not ideal for generating 1:20 details, as most of the time these are project-specific, and they heavily depend on the model content and updates.

