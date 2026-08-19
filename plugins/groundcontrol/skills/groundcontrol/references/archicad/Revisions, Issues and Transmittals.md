# Revisions, Issues and Transmittals

How drawing changes are recorded, revised and issued using ArchiCAD Revision Management (Document > Revision Management). The system automates revision IDs, revision histories, the drawing list and the transmittal record — the manual work is limited to marking changes and closing the issue.

## The Workflow

### During documentation

1. **Make the change** in the model or on the layout.
2. **Mark the change** using the Change Marker tool:

![](Revisions%2C%20Issues%20and%20Transmittals/image.png)

- First create a change in the Change Manager, then place a change marker and link it to this change (Place linked Marker). For changes affecting multiple sheets, place a cloud on the relevant layouts and link it to the same change. Do not create a new change for each instance.

> **Change Naming**
> **Change ID**: sequential per project and per user (eg. `DW-01` for a change made by Dimmity). You will have to set this for the first change you create in a project, subsequent changes will pick up a change automatically. This avoids clashes with other users in Teamwork models.
> **Description**: short and specific, 3-4 words max, noting what changed, not why (e.g. "Door D07 relocated").

- For **schedule pages, cover and other non-model sheets**, either
  - place a marker-head-only Change Marker (no cloud) directly on the affected layout, or

    ![](Revisions%2C%20Issues%20and%20Transmittals/change%20marker%201.png)

  - add the change to the layout itself.

    ![](Revisions%2C%20Issues%20and%20Transmittals/Add%20change%20to%20layout.png)

  - also add the change to the cover and index layouts of the schedule.

### At issue time

1. **Create a new transmittal set**:
   - Create a 'New Transmittal Set' in Book Settings.

   ![](Revisions%2C%20Issues%20and%20Transmittals/New%20transmittal.png)

   - Every layout that has not been issued previously or gained a change since the last issue is automatically included. Remove any that are not ready to be transmitted. (Alternatively remove all and add only the layouts to be included in the current issue).
   - Add the 'TRANSMITTAL' layout.
   - Close the Transmittal Set.
2. **Publish drawings using 'Layouts in current Transmittal Set'**
3. **Publish schedules** by selecting the folder of the schedule (eg. `A801 Finishes and Materials`) and use 'selected items'. This publishes all sheets and preserves pdf bookmarking.
4. If required, publish other formats (dwg, ifc, BIMx, etc)
5. Move the published documents into the ISSUE folder and, if using, the _CURRENT DOCUMENTS folder, archive superceeded drawings.
6. Create an updated ARCHITECTURAL DRAWING REGISTER using the finder shortcut.

## Notes

- Reference: [Graphisoft — Revision Management Workflow](https://help.graphisoft.com/AC/27/INT/_AC27_Help/070_Documentation/070_Documentation-98.htm)

#groundcontrol #groundcontrol/archicad
