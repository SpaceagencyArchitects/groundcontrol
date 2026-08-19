#!/usr/bin/env python3
"""
collapse_blanks.py — tidy the runs of empty paragraphs NATSPEC uses for spacing.

NATSPEC brackets its guidance with blank paragraphs (often three in a row). Once
the guidance is stripped or moved to comments, those blanks stack up and show as
paragraph breaks throughout. This collapses any run of consecutive blank
paragraphs down to a single blank (default) — or removes them entirely with
--remove-all.

A paragraph is only treated as a removable blank when it has no text AND carries
nothing structural: no section break, bookmark, comment marker, drawing/image,
field, or manual break. So sections, footers, the TOC anchors, heading
bookmarks and comment anchors are all preserved.

--strip-soft-breaks additionally removes soft line breaks (<w:br/> and
w:type="textWrapping") that a Pages/Word round-trip often injects at the end of
headings and prompts, showing as an empty row under each. Page and column breaks
are kept.

Usage:
    python collapse_blanks.py in.docx out.docx                    # collapse to one
    python collapse_blanks.py in.docx out.docx --remove-all       # remove every blank
    python collapse_blanks.py in.docx out.docx --strip-soft-breaks
"""
import sys, re
from docxlib import read_document_xml, write_parts, iter_paragraphs, para_text

def strip_soft_breaks(doc):
    # drop runs that contain only a soft (textWrapping / untyped) line break
    doc = re.sub(r'<w:r\b[^>]*>(?:<w:rPr>(?:(?!</w:r>).)*?</w:rPr>)?'
                 r'<w:br(?:\s+w:type="textWrapping")?\s*/>\s*</w:r>', "", doc, flags=re.S)
    # and any remaining bare soft-break elements
    doc = re.sub(r'<w:br(?:\s+w:type="textWrapping")?\s*/>', "", doc)
    return doc

KEEP_IF = ("bookmarkStart", "bookmarkEnd", "commentRangeStart", "commentRangeEnd",
           "commentReference", "<w:sectPr", "<w:drawing", "<pic:", "<w:pict",
           "fldChar", "instrText", "<w:br", "<w:object", "<w:tbl")

def is_removable_blank(p_xml):
    if para_text(p_xml).strip():
        return False
    return not any(tok in p_xml for tok in KEEP_IF)

def main():
    src, dst = sys.argv[1], sys.argv[2]
    remove_all = "--remove-all" in sys.argv
    doc = read_document_xml(src)

    n_breaks = 0
    if "--strip-soft-breaks" in sys.argv:
        n_breaks = len(re.findall(r'<w:br(?:\s+w:type="textWrapping")?\s*/>', doc))
        doc = strip_soft_breaks(doc)

    paras = list(iter_paragraphs(doc))
    del_spans = []
    prev_blank = False
    last_end = None
    for s, e, p in paras:
        if last_end is not None and "<w:tbl" in doc[last_end:s]:
            prev_blank = False            # a table breaks the run
        blank = is_removable_blank(p)
        if blank and (remove_all or prev_blank):
            del_spans.append((s, e))      # drop this extra blank
        else:
            prev_blank = blank
        last_end = e

    for s, e in sorted(del_spans, reverse=True):
        doc = doc[:s] + doc[e:]
    write_parts(src, dst, {"word/document.xml": doc})
    mode = "removed all" if remove_all else "collapsed to one"
    extra = f"; stripped {n_breaks} soft breaks" if n_breaks else ""
    print(f"Removed {len(del_spans)} blank paragraphs ({mode}){extra} -> {dst}")

if __name__ == "__main__":
    main()
