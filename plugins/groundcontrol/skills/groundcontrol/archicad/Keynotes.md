# Keynotes

## Keynote system with labels
In ArchiCAD, each keynote is made up of the following information.
* a Code (see [[Abbreviations and Codes]])
* Title - brief description of item (for keynote legends)
* Description (for labels to go on drawings)
  * Scheduled element/finish - refer to schedule, typically for items labelled using code only, eg paint finishes, tiles, sanitary or tapware items or composites, eg wall types, ceilings, cladding.
  * System or complex item - detailed description to be used in label
* Natspec reference or [[A80 - Schedules]] Number

## Finishes, Fixtures, Equipment, Sanitaryware
1. Add a keynote (code and title) for every finish, fixture, equipment, sanitaryware etc. Descriptions and references can be added later as decisions are made
2. Create an A4 page for each item that needs to be schedules - add the schedule document number in the corresponding keynotes ‘reference’ field

## Wall, Ceiling types
1. Make a keynote for each wall and ceiling type. This can start as a placeholder, but should eventually include a detailed description of the wall or ceiling.
2. Create a corresponding composite with the same [code]

## Paint finishes
1. Create a keynote for each paint system (e.g. PT1, PT2). One keynote per system — the same PT code applies to walls, ceilings, trims, and joinery where the same system is used. Do not create separate PT codes per substrate.
2. Create a C code for each colour (e.g. C1, C4).
3. Create a corresponding ArchiCAD surface attribute for each colour, named using the C code in brackets — e.g. [C4] - Warm white. This surface is used to colour walls and other elements in plan and elevation views.
4. When annotating on schedules or drawings, combine the paint system code and colour code with a slash — e.g. PT1/C4 = paint system PT1 in colour C4.

The PT code is a cross-reference to the Z Specification. The C code is a cross-reference to the A80 Colour Schedule. Both codes are listed on the A00 Legend Sheet with references to their respective documents. See [[Paint Finishes]].
## Room Layouts/Elevations
* Add a keynote schedule for finishes, fixtures, equipment, sanitaryware to each sheet, listing codes, description and reference to spec or schedule

#groundcontrol/archicad