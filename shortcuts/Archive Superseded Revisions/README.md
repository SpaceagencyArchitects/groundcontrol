ARCHIVE SUPERSEDED REVISIONS  —  Finder Quick Action for macOS
==============================================================

WHAT IT DOES
------------
Right-click a folder and choose "Archive Superseded Revisions". It looks
through the folder and all its subfolders and, wherever the same drawing exists
at more than one revision, keeps the highest revision in place and moves the
lower one(s) into an "_archive" folder in that same location.

It works IN PLACE on the folder you select — there is no copy and no prompt.
Missing "_archive" folders are created. Nothing is overwritten (a name clash is
renamed " (2)").

  - Folders whose name starts with "_" (including existing "_archive") are
    skipped, so already-archived files are left alone.
  - Each folder is compared on its own — drawings are grouped by drawing number
    within a folder, not across folders.

REVISION RANKING (which one is kept)
  A numbered revision (01, 02...) is treated as higher than a lettered revision
  (A, B...), which is higher than no revision at all. Within numbers the higher
  number wins; within letters the later letter wins.


INSTALL (once per Mac)
----------------------
1. Unzip this download.
2. Double-click "Archive Superseded Revisions.workflow".
   - If macOS blocks it, right-click the file, choose Open, then Install.
3. Click Install when prompted.


HOW TO USE
----------
1. Right-click the folder you want to tidy (e.g. ARCHITECT, or one series
   folder).
2. Quick Actions > Archive Superseded Revisions.
3. Done — the folder opens and a notification shows how many were archived.

FILE NAMING: drawings are read as  NUMBER_REVISION NAME.pdf
(e.g. A100_01 Ground Floor.pdf). A file with no underscore is treated as having
no revision.

Made for spaceagency.
