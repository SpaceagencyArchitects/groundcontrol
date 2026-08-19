#!/usr/bin/env python3
"""
place_logo.py — drop the practice logo into a document.

A general Word document has no NATSPEC "Your logo" placeholder, so this uses a
convention instead:
  * --token "{{logo}}"  (default): replaces that text wherever you typed it in
    the body with the logo image at --width-cm.
  * --header            : also/instead places the logo in the page header
    (top-left of every page).

Usage:
    python place_logo.py in.docx out.docx --logo assets/logo.png --width-cm 3
    python place_logo.py in.docx out.docx --logo assets/logo.png --header
"""
import sys, os, re, zipfile

def emu(cm): return round(cm * 360000)

def drawing(rid, cx, cy, name="Logo", did=2001):
    return (f'<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
        f'<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
        f'<wp:docPr id="{did}" name="{name}"/>'
        f'<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
        f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
        f'<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        f'<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        f'<pic:nvPicPr><pic:cNvPr id="{did}" name="{name}"/><pic:cNvPicPr/></pic:nvPicPr>'
        f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
        f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
        f'</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r>')

REL = ('<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/'
       'officeDocument/2006/relationships/image" Target="{tgt}"/>')

def add_rel(rels_text, rid, target):
    if f'Id="{rid}"' in rels_text:
        return rels_text
    return rels_text.replace("</Relationships>", REL.format(rid=rid, tgt=target) + "</Relationships>")

def ensure_ct(ct, ext):
    mime = "jpeg" if ext in ("jpg", "jpeg") else ext
    if f'Extension="{ext}"' in ct:
        return ct
    return ct.replace('<Default Extension="xml" ContentType="application/xml"/>',
        f'<Default Extension="xml" ContentType="application/xml"/>'
        f'<Default Extension="{ext}" ContentType="image/{mime}"/>')

def main():
    a = sys.argv
    src, dst = a[1], a[2]
    logo = a[a.index("--logo") + 1]
    width = float(a[a.index("--width-cm") + 1]) if "--width-cm" in a else 3.0
    token = a[a.index("--token") + 1] if "--token" in a else "{{logo}}"
    do_header = "--header" in a

    from PIL import Image
    w, h = Image.open(logo).size
    cx = emu(width); cy = round(cx * h / w)
    ext = os.path.splitext(logo)[1].lstrip(".").lower()

    with zipfile.ZipFile(src) as z:
        names = z.namelist()
        parts = {n: z.read(n) for n in names}

    media = f"word/media/houselogo.{ext}"
    parts[media] = open(logo, "rb").read()
    parts["[Content_Types].xml"] = ensure_ct(parts["[Content_Types].xml"].decode(), ext).encode()

    placed = []
    # body token replacement
    doc = parts["word/document.xml"].decode()
    if token and token in doc:
        rid = "rIdHouseLogo"
        parts["word/_rels/document.xml.rels"] = add_rel(
            parts["word/_rels/document.xml.rels"].decode(), rid, f"media/houselogo.{ext}").encode()
        # replace the whole run that contains the token
        run_re = re.compile(r"<w:r\b[^>]*>(?:(?!</w:r>).)*?" + re.escape(token) + r"(?:(?!</w:r>).)*?</w:r>", re.S)
        doc, n = run_re.subn(drawing(rid, cx, cy), doc, count=1)
        if n == 0:  # token not isolated in a run; replace the raw text
            doc = doc.replace(token, "", 1)
        parts["word/document.xml"] = doc.encode()
        placed.append(f"body token '{token}'")

    # header placement
    if do_header:
        hdrs = [n for n in names if re.match(r"word/header\d+\.xml$", n)]
        for i, hn in enumerate(hdrs):
            rid = f"rIdHouseLogoH{i}"
            rels_name = f"word/_rels/{os.path.basename(hn)}.rels"
            rels = parts.get(rels_name, b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   b'<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"></Relationships>').decode()
            parts[rels_name] = add_rel(rels, rid, f"media/houselogo.{ext}").encode()
            hx = parts[hn].decode()
            # insert the drawing into the first paragraph's first run slot (after pPr)
            hx = re.sub(r"(<w:p\b[^>]*>(?:<w:pPr>.*?</w:pPr>)?)",
                        r"\1" + drawing(rid, cx, cy, name="LogoH", did=2100 + i), hx, count=1, flags=re.S)
            parts[hn] = hx.encode()
        if hdrs:
            placed.append(f"{len(hdrs)} header(s)")

    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for n in list(dict.fromkeys(names + list(parts.keys()))):
            zout.writestr(n, parts[n])
    print(f"Placed logo ({', '.join(placed) if placed else 'nowhere — token not found'}) -> {dst}")

if __name__ == "__main__":
    main()
