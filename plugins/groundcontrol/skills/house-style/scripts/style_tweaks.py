#!/usr/bin/env python3
"""
style_tweaks.py — small targeted edits to paragraph styles.

  --remove-header-line     drop the bottom border on the "Header" style
                           (the horizontal rule across the top of every page)
  --blank-header           empty every header part (removes the running
                           STYLEREF worksection title — use once the title is in
                           the footer, so it isn't duplicated / broken in Pages)
  --heading STYLE:BEF:AFT  set a style's paragraph spacing, in points, e.g.
                           --heading Heading3:12:6  --heading Heading4:6:6
                           (points are converted to twentieths internally)

Usage:
    python style_tweaks.py in.docx out.docx --remove-header-line --blank-header \
        --heading Heading3:12:6 --heading Heading4:6:6
"""
import sys, re
from docxlib import read_part, list_parts, write_parts

def blank_header(xml):
    # keep the <w:hdr ...> wrapper; replace its contents with one empty paragraph
    return re.sub(r"(<w:hdr\b[^>]*>).*(</w:hdr>)",
                  r'\1<w:p><w:pPr><w:pStyle w:val="Header"/></w:pPr></w:p>\2',
                  xml, flags=re.S)

def edit_style_block(styles, style_id, fn):
    pat = re.compile(r'(<w:style\b[^>]*w:styleId="' + re.escape(style_id) + r'".*?</w:style>)', re.S)
    return pat.sub(lambda m: fn(m.group(1)), styles, count=1)

def set_spacing(block, before_tw, after_tw):
    spacing = f'<w:spacing w:before="{before_tw}" w:after="{after_tw}"/>'
    if "<w:spacing" in block:
        return re.sub(r"<w:spacing\b[^>]*/>", spacing, block, count=1)
    # insert spacing into pPr (create pPr if absent)
    if "<w:pPr>" in block:
        return block.replace("<w:pPr>", "<w:pPr>" + spacing, 1)
    return re.sub(r"(</w:name>)", r"\1<w:pPr>" + spacing + "</w:pPr>", block, 1)

def remove_pbdr(block):
    return re.sub(r"<w:pBdr>.*?</w:pBdr>", "", block, flags=re.S)

def main():
    src, dst = sys.argv[1], sys.argv[2]
    styles = read_part(src, "word/styles.xml")
    parts = {}
    done = []
    if "--remove-header-line" in sys.argv:
        styles = edit_style_block(styles, "Header", remove_pbdr)
        done.append("removed Header border")
    if "--blank-header" in sys.argv:
        n = 0
        for name in list_parts(src):
            if re.match(r"word/header\d+\.xml$", name):
                parts[name] = blank_header(read_part(src, name)); n += 1
        done.append(f"blanked {n} headers")
    # collect all --heading specs (support repeats)
    for idx, a in enumerate(sys.argv):
        if a == "--heading":
            sid, bef, aft = sys.argv[idx + 1].split(":")
            b, af = int(round(float(bef) * 20)), int(round(float(aft) * 20))
            styles = edit_style_block(styles, sid, lambda blk, b=b, af=af: set_spacing(blk, b, af))
            done.append(f"{sid} spacing {bef}/{aft}pt")
    parts["word/styles.xml"] = styles
    write_parts(src, dst, parts)
    print("Style tweaks: " + "; ".join(done) + f" -> {dst}")

if __name__ == "__main__":
    main()
