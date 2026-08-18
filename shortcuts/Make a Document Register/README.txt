CREATE DRAWING REGISTER  —  Finder Quick Action for macOS
=========================================================

WHAT IT DOES
------------
Right-click any folder in Finder and choose "Create Drawing Register".
It scans that folder (and all its subfolders), reads the PDF drawing files,
and produces a Word document listing every drawing in a table:

    Drawing No.  |  Drawing Title  |  Rev

Drawings are grouped by the folder they live in (each folder name appears as a
heading above its drawings) and sorted by drawing number within each group.

The document is built on the spaceagency letterhead — it carries the header
logo and footer, and all text is set in KMR Waldenburg Halbschmal with no bold
or italics. The letterhead is built into the shortcut, so there is nothing
extra to supply.

The Word file is saved in a subfolder named "_document register" inside the
folder you right-clicked (created automatically if it doesn't exist), named:
    YYMMDD_Document Register.docx        (e.g. 260721_Document Register.docx)
Finder opens and highlights it when it's done.


INSTALL (once per Mac)
----------------------
1. Unzip this download.
2. Double-click "Create Drawing Register.workflow".
   - If macOS blocks it ("unidentified developer"), instead right-click the
     file and choose Open, then click Install.
3. Click Install when prompted.

Nothing else to install — no Python or other setup needed.

The first time you run it, macOS may ask permission for Finder/Automator to
run the action (or show it under System Settings > Privacy & Security >
Automation). Click Allow / OK once.

FONT: For the register to display correctly, the font "KMR Waldenburg
Halbschmal" must be installed on the Mac (it is the practice's standard font).
If it is missing, Word will substitute another font — the text is still correct,
it just won't look right. Install the font via Font Book if needed.


HOW TO USE
----------
1. In Finder, right-click the folder containing your drawings.
2. Choose Quick Actions > Create Drawing Register.
   (On some setups it appears directly in the right-click menu.)
3. The register opens in the folder a moment later.

Run it again any time the drawings change — it just makes a fresh dated file.


FOLDER REQUIREMENTS
-------------------
- Point it at the top folder of your set. It looks through every subfolder.
- Any folder whose name starts with an underscore ( _ ) is IGNORED, along with
  everything inside it. Use this to keep things out of the register — e.g.
  "_archive", "_WIP", "_superseded". (The "_document register" output folder
  also starts with _, so previous registers are never scanned.)
- Each subfolder that contains drawings becomes a heading in the register,
  labelled with that folder's name. Drawings sitting directly in the folder you
  right-clicked appear first, under that folder's name.
- You need permission to save into the folder (the "_document register"
  subfolder is created there).


FILE NAMING REQUIREMENTS
------------------------
Only PDF files (.pdf) are read. Everything else — and hidden files — is skipped.

Name files as:   DRAWING-NUMBER_REVISION DRAWING NAME.pdf

  - The drawing number comes first and must NOT contain an underscore.
  - An underscore ( _ ) separates the number from the revision.
  - The revision is 1 or 2 characters, numeric or alphabetical.
  - A single space separates the revision from the drawing name.

  Examples:
    A100_01 Site Plan.pdf        ->  A100  |  Site Plan          |  01
    A20_B Roof Plan.pdf          ->  A20   |  Roof Plan          |  B
    A9_1 Cover Sheet.pdf         ->  A9    |  Cover Sheet        |  1

NO REVISION:
If a file name has NO underscore, it is treated as having no revision. The
first word is the drawing number, the rest is the name, and Rev is left blank.

    A105 Level 3 Plan.pdf        ->  A105  |  Level 3 Plan       |  (blank)
    A400.pdf                     ->  A400  |  (blank)            |  (blank)

IF A NAME DOESN'T FIT THE PATTERN:
Nothing is dropped. If a file has an underscore but the part after it isn't a
clean 1-2 character revision (e.g. a 3-character revision), the whole name is
placed in the Drawing Title column with the number and revision left blank, and
it sorts to the bottom of its group so you can spot it and rename the file.


TROUBLESHOOTING
---------------
- Don't see it in the menu? Log out and back in, or check
  System Settings > Keyboard > Keyboard Shortcuts > Services > Files and Folders
  and make sure "Create Drawing Register" is ticked.
- Text looks wrong? Install the "KMR Waldenburg Halbschmal" font (see above).
- Wrong columns for a drawing? Check the file name against the rules above.

Made for spaceagency.
