GROUNDCONTROL — FINDER SHORTCUTS (source)
=========================================

Editable source for three spaceagency Finder shortcuts. Each folder holds the
full script, the Python engine on its own (easier to edit), and the user README.

  Issue Drawings/
      filer.py                              engine
      Issue Drawings - shell script.txt     full script (wraps filer.py)
      README.txt                            what it does / how to use
    -> Select issued files, choose the project folder; MOVES them into
       YYMMDD_revisions and COPIES them into __CURRENT DOCUMENTS/ARCHITECT/<series>,
       archiving superseded revisions. TRANSMITTAL files are renamed
       YYMMDD_TRANSMITTAL and go to the revisions folder only.

  Make a Document Register/
      register.py                           engine (includes the letterhead as
                                            base64 in TEMPLATE_B64)
      SPAA_Letterhead_v0.docx               source letterhead
      BUILD NOTES.txt                       how to edit / re-embed the template
      Make a Document Register - shell script.txt
      README.txt
    -> Right-click a folder; builds a Word register of the PDFs (grouped by
       subfolder) on the spA letterhead, saved to a _document register subfolder.

  Archive Superseded Revisions/
      archive.py                            engine
      Archive Superseded Revisions - shell script.txt
      README.txt
    -> Right-click a folder; recursively keeps the highest revision of each
       drawing and moves the rest into _archive folders in place.

SHARED CONVENTIONS
------------------
- File name format:  NUMBER_REVISION NAME.pdf   (e.g. A100_01 Ground Floor.pdf)
  No underscore = no revision.
- Revision ranking: numeric (01,02) > alphabetical (A,B) > none.
- Series folder = drawing number's letter + first digit (A100 -> A1).
- Folders starting with "_" are skipped when scanning.
- Nothing is overwritten; name clashes are renamed " (2)".

HOW THESE ARE USED
------------------
Each script goes into either a Finder Quick Action (.workflow) or an Apple
Shortcut (Run Shell Script action, /bin/bash, pass input as arguments). To
rebuild a Quick Action .workflow or an Apple Shortcut from a script, paste the
"... - shell script.txt" body into the relevant Run Shell Script box.

Requirements on each Mac: /usr/bin/python3 (Command Line Tools) and, for the
register, the KMR Waldenburg Halbschmal font.
