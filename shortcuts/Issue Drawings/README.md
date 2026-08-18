ISSUE DRAWINGS  —  Finder Quick Action for macOS
================================================

WHAT IT DOES
------------
Select the drawing files you're issuing, right-click, and choose
"Issue Drawings". Pick the project folder once, and it does two things in that
same folder:

  1. ISSUE  — creates a folder named with today's date in reverse,
     YYMMDD_revisions (e.g. 260729_revisions), and MOVES the selected files
     into it. This is your dated issue record.

  2. CURRENT DOCUMENTS — copies each drawing into the "__CURRENT DOCUMENTS"
     folder (in the same project folder), filed under
     ARCHITECT / <series>, and archives any superseded revisions.

Both the YYMMDD_revisions folder and __CURRENT DOCUMENTS sit in the project
folder you choose. Any missing folders are created automatically. Nothing is
ever overwritten — a name clash is renamed " (2)".

FILING & ARCHIVING (Current Documents)
  - Series = the drawing number's letter + first digit (A100 -> A1, A050 -> A0).
  - The file goes into an existing folder whose name starts with that series
    ("A1" or "A1 Plans"), or a new folder named after the series.
  - If the same drawing now exists at more than one revision, the highest
    revision stays and the lower one(s) move to an "_archive" folder beside it.

TRANSMITTALS
  - Any selected file with "TRANSMITTAL" in its name is renamed
    YYMMDD_TRANSMITTAL, moved into the YYMMDD_revisions folder, and is NOT
    copied to __CURRENT DOCUMENTS.

When it's done, the YYMMDD_revisions folder opens in Finder.


INSTALL (once per Mac)
----------------------
1. Unzip this download.
2. Double-click "Issue Drawings.workflow".
   - If macOS blocks it, right-click the file, choose Open, then Install.
3. Click Install when prompted.

The first run may ask permission for Finder/Automator under
System Settings > Privacy & Security > Automation. Click Allow once.


HOW TO USE
----------
1. Select the file(s) you're issuing in Finder.
2. Right-click > Quick Actions > Issue Drawings.
3. Choose the project folder when prompted (the one that contains, or will
   contain, __CURRENT DOCUMENTS), then click Choose.
4. Files are issued, filed, and archived; the revisions folder opens.

To cancel, dismiss the folder-chooser dialog — nothing is moved or copied.


FILE NAMING (how drawings are read)
-----------------------------------
File name format:   NUMBER_REVISION NAME.pdf     (e.g. A100_01 Ground Floor.pdf)
  - Drawing number first (no underscore inside it).
  - An underscore separates the number from the revision.
  - Revision is 1-2 characters, numeric (01, 02) or alphabetical (A, B).
  - A file with no underscore is treated as having no revision.

Revision ranking (which is "higher"): a numbered revision (01, 02...) beats a
lettered revision (A, B...), which beats no revision. Only drawings you just
filed are checked for archiving; unrelated existing pairs are left alone.

Made for spaceagency.
