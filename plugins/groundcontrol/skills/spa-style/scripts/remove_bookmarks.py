#!/usr/bin/env python3
"""
remove_bookmarks.py — strip Word bookmarks from a document.

NATSPEC merged specs carry thousands of structural bookmarks (f-…/h-… anchors)
that are clutter and often have duplicate ids. This removes them across the
document body, headers and footers.

By default every bookmark goes. With --keep-toc, the Table-of-contents anchors
(names starting "_Toc") are preserved so the TOC's page numbers and links keep
working; their matching bookmarkEnd elements are kept by id.

Usage:
    python remove_bookmarks.py in.docx out.docx            # remove all
    python remove_bookmarks.py in.docx out.docx --keep-toc # keep _Toc anchors
"""
import sys, re, zipfile

START_RE = re.compile(r"<w:bookmarkStart\b[^>]*/>")
END_RE = re.compile(r"<w:bookmarkEnd\b[^>]*/>")

def strip(xml, keep_toc):
    keep_ids = set()
    if keep_toc:
        for m in START_RE.finditer(xml):
            name = re.search(r'w:name="([^"]*)"', m.group(0))
            wid = re.search(r'w:id="([^"]*)"', m.group(0))
            if name and name.group(1).startswith("_Toc") and wid:
                keep_ids.add(wid.group(1))

    def start_sub(m):
        if keep_toc:
            name = re.search(r'w:name="([^"]*)"', m.group(0))
            if name and name.group(1).startswith("_Toc"):
                return m.group(0)
        return ""

    def end_sub(m):
        if keep_toc:
            wid = re.search(r'w:id="([^"]*)"', m.group(0))
            if wid and wid.group(1) in keep_ids:
                return m.group(0)
        return ""

    xml = START_RE.sub(start_sub, xml)
    xml = END_RE.sub(end_sub, xml)
    return xml

def main():
    src, dst = sys.argv[1], sys.argv[2]
    keep_toc = "--keep-toc" in sys.argv
    with zipfile.ZipFile(src) as zin:
        names = zin.namelist()
        parts = {}
        removed = 0
        for n in names:
            if n == "word/document.xml" or re.match(r"word/(header|footer)\d+\.xml$", n):
                x = zin.read(n).decode("utf-8")
                before = len(START_RE.findall(x)) + len(END_RE.findall(x))
                nx = strip(x, keep_toc)
                after = len(START_RE.findall(nx)) + len(END_RE.findall(nx))
                removed += before - after
                parts[n] = nx
        with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
            for n in names:
                data = parts[n].encode("utf-8") if n in parts else zin.read(n)
                zout.writestr(n, data)
    kept = "kept _Toc anchors" if keep_toc else "removed all"
    print(f"Removed {removed} bookmark elements ({kept}) -> {dst}")

if __name__ == "__main__":
    main()
