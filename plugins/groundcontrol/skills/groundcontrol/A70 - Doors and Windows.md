# A70 - Doors and Windows   
**A701-A799**  
**A71.## (DOORS)**  
**A72.## (WINDOWS)**  
## DOOR SCHEDULE  
  
Doors schedules vary between projects, depending on complexity of doors and repetition.
Typically, door schedules include two parts.  
  
### Part 1: Door Type Information  
Door elevations, typically at 1:50, visually describe each door type used in the project.  
  
#### Typical Content:  
* Door type reference (linked to schedule and drawing tags)  
* number and configuration of door leaves.  
* Indicative setting-out of door hardware, mechanical grilles, vision panels, door furniture, etc  
* Schematic representation of closers, locks, hold-opens, access control equipment, etc  
  
#### ArchiCAD setup:  
Door type elevations can be generated using  
* interactive schedule  
* 2D drawings on a worksheet or   
* 'live' elevations of door using the elevation tool  
  
### Part 2: Door Type Schedule  
A tabular schedule of every door in the project, used to describe the door, it performance requirements and specific hardware items.  
  
Unless a specific item of hardware (eg handle, push plate) is specified and scheduled in the schedule, best practice is to describe  
* what the hardware item (eg lock, hinge) must do,  
* what it must look like (finish, size)  
* how it is operated, and  
* what it must interface with  
Final hardware selection, coding, and compatibility with fire, access control, and door manufacturer requirements to be confirmed by specialist hardware supplier.

Examples:  
```
Mortice latch and deadbolt, lever handle operation, keyed to corridor side, thumb turn to room side, free egress at all times.
```
  
```
Fire-rated mortice lockset with latch and deadbolt, lever handle operation, free egress without key, suitable for integration with access control.
```
  
**Rule of Thumb:** **If a competent hardware consultant can code it correctly without calling you, you've given the right amount of detail.**  
Too little detail → RFIs  
Too much detail → unintended specification liability.

Reference — mortice lock functions:  
[Mortice lock function chart](A70%20-%20Doors%20and%20Windows/mortice-lock-function-chart.pdf)<!-- {"embed":"true", "preview":"true"} -->

#### Typical Content:  
* Storey [use on larger projects only]  
* Door number [Consists of 2 parts, i.e. room number and D1, D2, D3 etc]  
* Location [Room Number / Room Name of room the door opens into]  
* Door type [refers to 1:50 door type elevation]  
* Frame type [reference door 1:5 details]  
* Door seals [functional description preferred, but can be coded if specific seals are required]  
* Door leaf type  
* Door leaf finish [description of finish only. Paint type is described in the specification and colour in the room finishes schedule or A6 room elevations]  
* Door leaf width and height *  
* Door leaf thickness *  
* Performance requirement [Fire rating, Acoustic, Smoke]  
* Door protection  
* Vision panel type  
* Door grille/undercut  
* Door stop  
* Lock/latch/catch [Functional description]  
* Electric locking [Yes / No / Performance note]  
* Furniture [Typically coded and scheduled; Lever/ Pull handle / push plates]  
* Closer [Function description]  
* Electromagnetic hold open [Yes / No / Performance note]  
* Reed switch [Yes / No / Performance note]  
* Special hardware [Performance note or coded  
* Sign type **  
* Sign text   
* Notes [describe performance related specifics]  
  
** Statutory signage, e.g. FIRE DOORS KEEP CLOSED, is scheduled here. Wayfinding signage is scheduled in [[A80 - Schedules]].  
  
**SPECIAL HARDWARE ITEMS TO SCHEDULE OR NOTE:**  
* Door closers for sliding doors (soft close on both ends)  
  
#### ArchiCAD Setup  
Tabular door schedules are set up as interactive schedules in ArchiCAD using a combination of library part parameters and custom properties associated with doors.  
A typical schedule is included in the spA template.  
  
### DOOR DETAILS (1:10, 1:5)  
Generic details applicable to most doors in the schedule are documented in the A75 subseries.  
Special conditions/specific interface details are to be shown in [[A50 - Interface Details]].   
Typically include details of internal doors only. External doors are described in [[A20 - External Elevations]] and [[A50 - Interface Details]]s.  
  
* Dimensions describing the geometry of door frames - all other variables e.g. partition thickness indicate as 'VARIES'  
* Dimensions and description of vision panels, grilles and similar  
  
## WINDOW SCHEDULE  
  
Generally they follow the same principles as the door schedule described above and include two parts:  
  
### Part 1: Window Type Information  
Window elevations (1:50) visually describe each window type used in the project and a schedule listing common properties.
  
**Typical elevation content:**  
* Window type reference (linked to schedule and drawing tags)  
* Configuration of frames and sashes.  
* Indicative setting-out of hardware, furniture, manifestation etc  
**Typical schedule content:**
- frame type
- frame finishes [description of finish only. Paint type is described in the specification and colour in the room finishes schedule or A6 room elevations]   
* hardware, furniture, security, screens, seals (functional requirements)  
* glazing type, including U-Value and SHGC  
* additional notes (eg. special subsills with integrated drainage)  

#### ArchiCAD setup:  
Window type elevations can be generated using  
* interactive schedule showing the elevation and other content in tabular form. If choosing this option, the scheduled content is incorporated into this schedule;
* 2D drawings with annotations or, requires a seperate interactive schedule for scheduled content; or
* 'live' elevations with annotations, requires a seperate interactive schedule for scheduled content.

### Part 2: Window Schedule  
A tabular schedule of every window type listing its location(s) in the project.  
  
#### Typical Content of Tabular Schedule:  
- Window type (reference 1:50 elevation)  
- Window number   
- Location (building, storey)
- Quantity  

## Examples:  
[Sample dw schedule 1.pdf](A70%20-%20Doors%20and%20Windows/Sample%20dw%20schedule%201.pdf)<!-- {"embed":"true", "preview":"true"} -->
[Sample dw schedule 2.pdf](A70%20-%20Doors%20and%20Windows/Sample%20dw%20schedule%202.pdf)<!-- {"embed":"true", "preview":"true"} -->
[Sample dw schedule 3.pdf](A70%20-%20Doors%20and%20Windows/Sample%20dw%20schedule%203.pdf)<!-- {"embed":"true", "preview":"true"} -->
  
Legends:  
![](A70%20-%20Doors%20and%20Windows/IMG_5281.png)
![](A70%20-%20Doors%20and%20Windows/IMG_5280.jpeg)
![](A70%20-%20Doors%20and%20Windows/IMG_5279.png)
![](A70%20-%20Doors%20and%20Windows/IMG_5278.png)

---
**See also:** [[Tagging of Elements in ArchiCAD]] for door and window element ID and type conventions; [[Classification and Properties]] for ArchiCAD interactive schedule setup.

#groundcontrol #groundcontrol/drawing-series
