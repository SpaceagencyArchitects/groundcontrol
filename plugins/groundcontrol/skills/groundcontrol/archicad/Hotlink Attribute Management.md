# Hotlink Attribute Management

Note:
- do not change existing attributes from spa template unless the change applies to ~every~ linked project file.
## Option A: Attribute.pln

![](Hotlink%20Attribute%20Management/Screenshot%202026-03-18%20at%209.39.32%E2%80%AFam.png)

## Option B: Attribute.xml

![](Hotlink%20Attribute%20Management/Screenshot%202026-03-18%20at%209.39.42%E2%80%AFam.png)
- new attributes created in Project A and B have a project/file specific prefix. eg Project A surface attributes is *A_Wall Tile 1, Project B surface is *B_Wall Tile 1. The * prefix enables searching for project specific attributes in the attribute manager. The A, B prefix prevents clashes of attribute names created in different project files.



## What does not work?
- Once a file has been hotlinked into another project, ArchiCAD creates a new attributes in the host file for any new attribute in the source file. Subsequently, attributes in the host file are not updated if they are changed in the source file. The attribute manager must be used to sync changes.


#groundcontrol/archicad