#!/usr/bin/env python3
"""
bookmark_headings.py — add a named bookmark to each section heading so the
document is easy to navigate (Word's Insert ▸ Bookmark list, the Bookmarks pane,
and hyperlink targets).

By default it bookmarks every worksection heading (heading level 1). Use
--levels to include more, e.g. --levels 1,2 to also bookmark the
GENERAL/PRODUCTS/EXECUTION subsections. Headings are found by their *outline
level*, not a fixed style name, so it works whether the style is called
"Heading1" (fresh NATSPEC download) or "Heading"/"Heading 2" (after a Pages/Word
round-trip renames the styles). Bookmark names come from the heading text (e.g.
"0131 Preliminaries" -> "WS_0131_Preliminaries") and never start with an
underscore, so they show as normal (not hidden) bookmarks.

Usage:
    python bookmark_headings.py in.docx out.docx
    python bookmark_headings.py in.docx out.docx --levels 1,2
"""
import sys, re
from docxlib import (read_document_xml, read_part, write_parts,
                         iter_paragraphs, para_style, para_text)

def styles_for_levels(styles_xml, levels_1based):
    """Return the set of styleIds whose outline level matches the requested
    heading levels (1-based → outlineLvl 0-based)."""
    want = {l - 1 for l in levels_1based}
    out = set()
    for m in re.finditer(r'<w:style\b[^>]*w:styleId="([^"]+)"[^>]*>(.*?)</w:style>',
                         styles_xml, re.S):
        sid, body = m.group(1), m.group(2)
        ol = re.search(r'<w:outlineLvl w:val="(\d+)"', body)
        if ol and int(ol.group(1)) in want:
            out.add(sid.replace("&amp;", "&"))
    return out

def sanitize(text):
    base = re.sub(r"[^0-9A-Za-z]+", "_", text).strip("_")
    if not base:
        base = "Section"
    if base[0].isdigit():
        base = "WS_" + base
    return base[:40]

def main():
    src, dst = sys.argv[1], sys.argv[2]
    levels_1based = {1}
    if "--levels" in sys.argv:
        levels_1based = {int(x.strip()) for x in sys.argv[sys.argv.index("--levels") + 1].split(",")}
    levels = styles_for_levels(read_part(src, "word/styles.xml"), levels_1based)
    if not levels:
        sys.exit("No heading styles found for the requested outline levels.")

    doc = read_document_xml(src)
    existing = [int(x) for x in re.findall(r'<w:bookmark(?:Start|End)\b[^>]*w:id="(\d+)"', doc)]
    nid = max(existing + [899999]) + 1   # high ids, clear of any survivors

    edits, used, count = [], set(), 0
    for s, e, p in iter_paragraphs(doc):
        if para_style(p) in levels and para_text(p).strip():
            name = sanitize(para_text(p))
            orig, k = name, 1
            while name in used:
                name = f"{orig}_{k}"[:40]; k += 1
            used.add(name)
            m = re.search(r"</w:pPr>", p)
            spos = s + (m.end() if m else p.index(">") + 1)
            epos = e - len("</w:p>")
            bid = nid; nid += 1
            edits.append((spos, f'<w:bookmarkStart w:id="{bid}" w:name="{name}"/>'))
            edits.append((epos, f'<w:bookmarkEnd w:id="{bid}"/>'))
            count += 1

    for pos, text in sorted(edits, key=lambda x: x[0], reverse=True):
        doc = doc[:pos] + text + doc[pos:]
    write_parts(src, dst, {"word/document.xml": doc})
    print(f"Added bookmarks to {count} headings ({', '.join(sorted(levels))}) -> {dst}")

if __name__ == "__main__":
    main()
