MAKE A DOCUMENT REGISTER — BUILD NOTES
======================================

Files here:
  register.py            The Python engine. Near the top it has a line:
                             TEMPLATE_B64 = "<base64...>"
                         That long string is the letterhead .docx encoded as
                         base64, so the shortcut is fully self-contained.
  SPAA_Letterhead_v0.docx  The source letterhead the base64 was made from.
  Make a Document Register - shell script.txt
                         The full shell body used by the Quick Action / Shortcut.
                         It wraps register.py in a heredoc.

To change the register logic:
  - Edit register.py (leave the TEMPLATE_B64 line alone unless changing the
    letterhead).

To change the letterhead:
  1. Replace SPAA_Letterhead_v0.docx with the new one (keep the KMR Waldenburg
     Halbschmal styles / header / footer).
  2. Regenerate the base64 and paste it back as TEMPLATE_B64:
        base64 -i "SPAA_Letterhead_v0.docx" | tr -d '\n'
     (or in python: base64.b64encode(open(f,'rb').read()).decode())

To rebuild the shortcut after editing register.py:
  - Re-embed register.py into the shell script (replace the text between
    <<'PYEOF' and PYEOF in the .txt), then paste that into the Run Shell Script
    action, OR ask Claude to repackage the .workflow.
