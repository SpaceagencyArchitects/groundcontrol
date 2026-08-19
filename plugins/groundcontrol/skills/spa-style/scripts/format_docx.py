#!/usr/bin/env python3
"""
format_docx.py — apply the spaceagency house style to ANY .docx in one pass,
driven by spa-style.json. Works on letters, reports, schedules — any Word
document, not just NATSPEC specs.

It runs the portable formatters in order: font + no-bold + caps headings →
heading spacing + remove header rule → clean bookmarks + add heading bookmarks →
collapse blank paragraphs + strip soft breaks → place the logo (at the {{logo}}
token and/or in the header) → fill the {{company}} token.

Everything is parameterised in spa-style.json, so changing the font, spacing
or logo is a one-line edit there.

Usage:
    python format_docx.py in.docx out.docx
    python format_docx.py in.docx out.docx --config /path/spa-style.json
"""
import sys, os, json, subprocess, tempfile, shutil, zipfile, re

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)

def run(script, *args):
    subprocess.run([sys.executable, os.path.join(HERE, script), *map(str, args)], check=True)

def asset(path):
    return path if os.path.isabs(path) else os.path.join(SKILL, path)

def replace_token(docx, token, text):
    """Replace a plain-text token in the body with `text` (single line)."""
    with zipfile.ZipFile(docx) as z:
        names = z.namelist(); data = {n: z.read(n) for n in names}
    doc = data["word/document.xml"].decode()
    if token not in doc:
        return False
    esc = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    data["word/document.xml"] = doc.replace(token, esc).encode()
    with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as zo:
        for n in names:
            zo.writestr(n, data[n])
    return True

def main():
    a = sys.argv
    src, dst = a[1], a[2]
    cfg_path = a[a.index("--config") + 1] if "--config" in a else os.path.join(SKILL, "spa-style.json")
    cfg = json.load(open(cfg_path))

    tmp = tempfile.mkdtemp()
    step = [0]
    cur = os.path.join(tmp, "s0.docx"); shutil.copy(src, cur)
    def nxt():
        step[0] += 1
        return cur, os.path.join(tmp, f"s{step[0]}.docx")

    # 1. font + house style
    font = cfg.get("font", "KMR Waldenburg")
    i, o = nxt(); args = [i, o, font]
    if cfg.get("no_bold"): args.append("--no-bold")
    if cfg.get("caps_headings"): args.append("--caps-headings")
    run("apply_font.py", *args); cur = o

    # 2. style tweaks: header rule + heading spacing
    i, o = nxt(); args = [i, o]
    if cfg.get("remove_header_line"): args.append("--remove-header-line")
    for sid, (bef, aft) in cfg.get("heading_spacing", {}).items():
        args += ["--heading", f"{sid}:{bef}:{aft}"]
    if len(args) > 2:
        run("style_tweaks.py", *args); cur = o

    # 3. bookmarks
    if cfg.get("clean_bookmarks", True):
        i, o = nxt(); run("remove_bookmarks.py", i, o, "--keep-toc"); cur = o
    if cfg.get("bookmark_headings", True):
        i, o = nxt(); run("bookmark_headings.py", i, o); cur = o

    # 4. tidy blanks
    if cfg.get("collapse_blanks", True):
        i, o = nxt(); args = [i, o]
        if cfg.get("strip_soft_breaks"): args.append("--strip-soft-breaks")
        run("collapse_blanks.py", *args); cur = o

    # 5. logo
    logo = cfg.get("logo") or {}
    if logo.get("file") and os.path.exists(asset(logo["file"])):
        i, o = nxt(); args = [i, o, "--logo", asset(logo["file"]),
                              "--width-cm", logo.get("width_cm", 3),
                              "--token", logo.get("token", "{{logo}}")]
        if logo.get("in_header"): args.append("--header")
        run("place_logo.py", *args); cur = o

    # 6. company token
    comp = cfg.get("company") or {}
    if comp.get("token"):
        line = " · ".join(x for x in [comp.get("name"), comp.get("address"),
                                      comp.get("phone"), comp.get("email")] if x)
        replace_token(cur, comp["token"], line)

    shutil.copy(cur, dst)
    print(f"House style applied -> {dst}")

if __name__ == "__main__":
    main()
