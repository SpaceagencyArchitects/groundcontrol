---
title: "A50b2 Detail Layout Techniques"
---
The number of detail views we have in the file is not necessarily equal to the number of placed detail drawings we will have on the layouts. Multiple detail drawings can be derived from a single view; then again, one view can be a single drawing source but show more details at once. 

Depending on how we arrange the placement of the detail drawings from views to layouts, we can use three layout techniques: 

[#1. One source view – one drawing](#1.%20One%20source%20view%20%E2%80%93%20one%20drawing)
[#2. One source view – multiple drawings](#2.%20One%20source%20view%20%E2%80%93%20multiple%20drawings)
[#3. Multiple source views – Multiple drawings](#3.%20Multiple%20source%20views%20%E2%80%93%20Multiple%20drawings)

## 1. One source view – one drawing ##

This technique is characteristically used with the creation of a detail library or a series of related details (eg. Door Frame Types). Details are created in a single location (independent detail or worksheet) next to each other, in the same way they would look on a layout. A single viewpoint is created, which is placed on the layout as a single drawing. A separate detail drawing numbering for each detail is not available. Detail titles and numbering needs to be managed manually.

It can be time-consuming to find a specified detail, as detail markers cannot be used to navigate in the project. This is particularly true when the detail/worksheet viewpoint is not well organised and contains active, superseded, unfinished details, etc. 

This method is suitable for generic details that do not have a specific relationship to the live model, such as generic joinery details, door frame types and elevations, railings, detailed profiles, and practically drawn details that would never be modelled, or those that require quick edit. Developing detail variations is also easy as we can easily transfer information and modify similar elements between details.

![Pasted image 20230202091307](notes/1_Documentation%20Codex/1d_ArchiCAD/_assets/Pasted%20image%2020230202091307.png)

## 2. One source view – multiple drawings ##

This technique is also suitable for detail libraries, but it is used with any method were we create several details in one view. One source view transforms into multiple drawings on the layout where we crop the placed viewpoint to show only one detail at a time. Therefore the viewpoint is added multiple times to the same or different layouts in the Layout Book.

In comparison to the previously described technique, where we created a single drawing from a single source view, project files can be larger, as we are adding the same view multiple times to a layout. However, the main advantage is the use of ARCHICAD Drawing titles and automatic ID numbers of the cropped drawings placed on the layout. Linked markers can be used after the drawings are placed on the layouts to reference the detail from any other view in the project. 
This technique will secure less views in the View Map tree, but it produces more cropped drawings on the layout. Therefore, this method should be used sparingly on medium to large projects.

![Pasted image 20230202091404](notes/1_Documentation%20Codex/1d_ArchiCAD/_assets/Pasted%20image%2020230202091404.png)

## 3. Multiple source views – Multiple drawings ##

With this technique, each detail is created in its own view, typically a detail view, sometimes a section or worksheet view. Ideally, these views are generated from the model, as described in [Model-based with Detail viewpoint](notes/1_Documentation%20Codex/1d_ArchiCAD/A50a1%20Model%20based%20detail%20with%20viewpoint.md) workflow, and each detail is then individually placed onto a layout. 
This is the most commonly used layout technique with all types of detailing workflows (model-based, 2D drawn-based and standard detailing) and is essential for any detail that is referenced from other project views (eg. GA plans or sections).
It ensures a direct model relationship to details and the ability to navigate the View Map, Layouts Views and BIMx via detail markers and detail numbering.

![Pasted image 20230202091420](notes/1_Documentation%20Codex/1d_ArchiCAD/_assets/Pasted%20image%2020230202091420.png)


References:
[](https://help.graphisoft.com/AC/26/INT/index.htm?rhcsh=1&rhnewwnd=0&rhmapid=#t=_AC26_Help%252F070_Documentation%252F070_Documentation-99.htm%7CArchiCAD%2026%20Helpcentre%20%3E%20Layout%20and%C2%A0Drawing%20IDs)
