#!/usr/bin/env python3
"""
scan_issues.py — reconstruct a drawing issue register from a spaceagency project folder.
Stdlib only (runs anywhere, incl. on the device via device_bash).

Usage:
  python3 scan_issues.py "<PROJECT_ROOT>" [--discipline ARCHITECT] [--out data.json]

Folder convention (per GROUNDCONTROL):
  <PROJECT_ROOT>/
    __CURRENT DOCUMENTS/<DISCIPLINE>/<series>/   current PDFs + _archive/ (superseded)
    <YYMMDD>_<desc>/                             one dated folder per issue
  Filenames:  <DrawingNo>_<Rev> <Name>.pdf   (Rev = 1-3 char alphanumeric)
"""
import os, re, sys, json, argparse

def parse(fn):
    if not fn.lower().endswith(".pdf"): return None
    stem = fn[:-4]
    m = re.match(r'^([A-Za-z]\d[\w.]*)_(\S+)\s+(.*)$', stem)      # No_Rev Name
    if m: return {"no": m.group(1).upper(), "rev": m.group(2), "name": m.group(3).strip(), "missing_rev": False}
    m = re.match(r'^([A-Za-z]\d[\w.]*)\s+(.*)$', stem)            # No Name  (rev missing = user error)
    if m: return {"no": m.group(1).upper(), "rev": "", "name": m.group(2).strip(), "missing_rev": True}
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--discipline", default="ARCHITECT")
    ap.add_argument("--out", default="-")
    a = ap.parse_args()
    root = a.root.rstrip("/")

    # project number + title from "(NNNN) TITLE"
    base = os.path.basename(root)
    pm = re.match(r'^\(?(\w+)\)?\s+(.*)$', base)
    project_no = pm.group(1) if pm else ""
    project_title = (pm.group(2) if pm else base).strip()

    # locate __CURRENT DOCUMENTS/<DISCIPLINE>
    cur_root = None
    for d in os.listdir(root):
        if "CURRENT DOCUMENTS" in d.upper() and os.path.isdir(os.path.join(root, d)):
            cand = os.path.join(root, d, a.discipline)
            if os.path.isdir(cand): cur_root = cand; break
    if not cur_root:
        sys.exit(f"Could not find __CURRENT DOCUMENTS/{a.discipline} under {root}")

    disc_letter = a.discipline[0].upper()  # A for ARCHITECT
    current, missing = {}, []
    for series in sorted(os.listdir(cur_root)):
        sp = os.path.join(cur_root, series)
        if not os.path.isdir(sp) or series.startswith("_"): continue
        for fn in os.listdir(sp):
            p = parse(fn)
            if not p: continue
            if p["missing_rev"]: missing.append(f"{series}/{fn}")
            current.setdefault(p["no"], {"rev": p["rev"], "name": p["name"], "series": series})

    issues = []
    for d in sorted(os.listdir(root)):
        dp = os.path.join(root, d)
        if not os.path.isdir(dp): continue
        md = re.match(r'^(\d{2})(\d{2})(\d{2})[_ ](.*)$', d)
        if not md: continue
        drw = {}
        for fn in os.listdir(dp):
            if "TRANSMITTAL" in fn.upper(): continue
            p = parse(fn)
            if not p: continue
            if not p["no"].startswith(disc_letter) or not re.match(rf'^{disc_letter}\d', p["no"]): continue
            if p["missing_rev"]: missing.append(f"{d}/{fn}")
            drw[p["no"]] = p["rev"]
        if drw:
            issues.append({"folder": d, "date": f"20{md.group(1)}-{md.group(2)}-{md.group(3)}",
                           "desc": md.group(4), "count": len(drw), "drawings": drw})
    issues.sort(key=lambda x: x["date"])

    data = {"project_title": project_title, "project_no": project_no, "discipline": a.discipline,
            "current": current, "issues": issues, "missing_rev": sorted(set(missing))}
    js = json.dumps(data, indent=1)
    if a.out == "-": print(js)
    else: open(a.out, "w").write(js); print(f"wrote {a.out}: {len(current)} drawings, {len(issues)} issues, {len(data['missing_rev'])} missing-rev")

if __name__ == "__main__":
    main()
