#!/usr/bin/env python3
"""
apply_font.py — set the practice's in-house font across the whole document.

Replaces every font reference (paragraph/character styles, document defaults,
direct run formatting, theme major/minor fonts, headers & footers) with the
target family, so nothing falls back to Arial/Calibri when published.

The spaceagency in-house font is "KMR Waldenburg" (this is the family name Word
shows for KMR-Waldenburg-BuchHalbschmal.ttf; the full family "KMR Waldenburg
Buch Halbschmal" is an alias). Install the .ttf first (copy to ~/.fonts and run
`fc-cache -f`) or the PDF will substitute a lookalike.

House style: the font is a single weight, so faux-bold looks wrong — use
--no-bold to strip all bold. Headings are set in all caps with --caps-headings.

Usage:
    python apply_font.py in.docx out.docx                          # default font only
    python apply_font.py in.docx out.docx --no-bold --caps-headings
    python apply_font.py in.docx out.docx "KMR Waldenburg" --no-bold --caps-headings
"""
DEFAULT_FONT = "KMR Waldenburg"
HEADING_STYLES = ("Heading1", "Heading2", "Heading3", "Heading4")
import sys, re
from docxlib import list_parts, read_part, write_parts

def strip_bold(xml):
    # remove every bold toggle (b / bCs); with none present the doc is non-bold
    return re.sub(r"<w:bCs\b[^>]*/>", "", re.sub(r"<w:b\b[^>]*/>", "", xml))

def caps_headings(styles_xml):
    # inject <w:caps/> into each heading style's run properties
    def repl(m):
        block = m.group(0)
        sid = re.search(r'w:styleId="([^"]+)"', block)
        if sid and sid.group(1) in HEADING_STYLES and "<w:caps" not in block:
            if "<w:rPr>" in block:
                block = block.replace("<w:rPr>", "<w:rPr><w:caps/>", 1)
            else:
                block = re.sub(r"(</w:name>)", r"\1<w:rPr><w:caps/></w:rPr>", block, 1)
        return block
    return re.sub(r"<w:style\b.*?</w:style>", repl, styles_xml, flags=re.S)

def set_rfonts(xml, font):
    # every <w:rFonts .../> — rewrite ascii/hAnsi/cs/eastAsia attributes
    def repl(m):
        tag = m.group(0)
        for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia",
                     "w:asciiTheme", "w:hAnsiTheme", "w:cstheme"):
            tag = re.sub(attr + r'="[^"]*"', "", tag)
        tag = re.sub(r"\s+", " ", tag).replace("<w:rFonts ", "").replace("<w:rFonts", "").rstrip("/>").strip()
        return (f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>')
    return re.sub(r"<w:rFonts\b[^>]*/>", repl, xml)

def ensure_docdefaults(styles_xml, font):
    # Guarantee a docDefaults rPrDefault rFonts pointing at the target font.
    if "<w:rFonts" in styles_xml.split("</w:docDefaults>")[0]:
        return set_rfonts(styles_xml, font)
    inject = (f'<w:docDefaults><w:rPrDefault><w:rPr>'
              f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>'
              f'</w:rPr></w:rPrDefault></w:docDefaults>')
    return re.sub(r"(<w:styles\b[^>]*>)", r"\1" + inject, styles_xml, count=1)

def set_theme_fonts(theme_xml, font):
    # major + minor latin typefaces
    return re.sub(r'(<a:latin\b[^>]*\btypeface=")[^"]*(")',
                  lambda m: m.group(1) + font + m.group(2), theme_xml)

def main():
    args = [a for a in sys.argv[1:]]
    no_bold = "--no-bold" in args;      args = [a for a in args if a != "--no-bold"]
    caps = "--caps-headings" in args;   args = [a for a in args if a != "--caps-headings"]
    src, dst = args[0], args[1]
    font = args[2] if len(args) > 2 else DEFAULT_FONT
    parts = list_parts(src)
    repl = {}
    for name in parts:
        if name == "word/styles.xml":
            x = ensure_docdefaults(set_rfonts(read_part(src, name), font), font)
            if no_bold: x = strip_bold(x)
            if caps: x = caps_headings(x)
            repl[name] = x
        elif name in ("word/document.xml", "word/fontTable.xml") \
                or re.match(r"word/(header|footer)\d+\.xml$", name) \
                or name.startswith("word/glossary/") and name.endswith((".xml",)) and ("styles" in name or "document" in name or "fontTable" in name):
            x = set_rfonts(read_part(src, name), font)
            if no_bold: x = strip_bold(x)
            repl[name] = x
        elif re.match(r"word/theme/theme\d+\.xml$", name):
            repl[name] = set_theme_fonts(read_part(src, name), font)
    write_parts(src, dst, repl)
    extras = (" +no-bold" if no_bold else "") + (" +caps-headings" if caps else "")
    print(f"Applied font '{font}'{extras} across {len(repl)} parts -> {dst}")

if __name__ == "__main__":
    main()
