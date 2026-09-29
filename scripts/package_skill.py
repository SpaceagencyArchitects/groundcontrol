#!/usr/bin/env python3
"""Package the GROUNDCONTROL codex as an uploadable Claude skill zip.

Claude's skill upload rejects zip paths with special characters (✱, commas,
parentheses, spaces). The repo keeps readable names for Obsidian and Docsify;
this script builds the zip with safe, slugged paths and rewrites every path
reference in SKILL.md and every markdown link in the codex pages to match.

Output: dist/groundcontrol.zip
"""
import os, re, shutil, sys, tempfile, unicodedata, urllib.parse, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "groundcontrol"
OUT = ROOT / "dist" / "groundcontrol.zip"
SKIP_DIRS = {".obsidian"}
SKIP_FILES = {".DS_Store"}

def slug_part(name: str, is_file: bool = True) -> str:
    stem, ext = os.path.splitext(name) if is_file else (name, "")
    if name in ("SKILL.md", "_sidebar.md"):
        return name
    s = unicodedata.normalize("NFKD", stem).encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower() or "index"
    return s + ext.lower()

def slug_path(rel: str) -> str:
    parts = rel.split("/")
    return "/".join(slug_part(p, i == len(parts) - 1) for i, p in enumerate(parts))

# 1. map every file
mapping = {}
for dirpath, dirnames, filenames in os.walk(SKILL):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for f in filenames:
        if f in SKIP_FILES or f.startswith("._"):
            continue
        rel = os.path.relpath(os.path.join(dirpath, f), SKILL).replace(os.sep, "/")
        mapping[rel] = slug_path(rel)
clash = len(set(mapping.values())) != len(mapping)
if clash:
    sys.exit("Slug collision — two files map to the same safe name.")
dir_mapping = {}
for rel, new in mapping.items():
    parts, nparts = rel.split("/")[:-1], new.split("/")[:-1]
    for i in range(1, len(parts) + 1):
        dir_mapping["/".join(parts[:i]) + "/"] = "/".join(nparts[:i]) + "/"

def map_ref(ref: str) -> str:
    if ref in mapping:
        return mapping[ref]
    if ref in dir_mapping:
        return dir_mapping[ref]
    return ref

# 2. rewrite SKILL.md backtick paths
def fix_skill(text: str) -> str:
    def repl(m):
        ref = m.group(1)
        base = re.sub(r" \(.*$", "", ref)
        return "`" + map_ref(base) + ref[len(base):] + "`"
    text = re.sub(r"`(references/[^`]+?)`", repl, text)
    text = text.replace("`references/A<NN> - <Title>.md`", "`references/a<nn>-<title>.md` (see the file map below)")
    rows = "\n".join(f"| {Path(r).stem} | `{mapping[r]}` |" for r in sorted(mapping)
                     if r.startswith("references/") and r.endswith(".md") and not r.endswith("_sidebar.md"))
    text += ("\n\n## File map (packaged names)\n\n"
             "In this package, file names are slugged for upload. Codex notes link to each other "
             "by the original titles below.\n\n| Title | File |\n|---|---|\n" + rows + "\n")
    return text

# 3. rewrite relative markdown links inside pages
LINK = re.compile(r"(\]\()([^)\s]+)(\))")
def fix_page(rel: str, text: str) -> str:
    here = os.path.dirname(rel)
    def repl(m):
        target = m.group(2)
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            return m.group(0)
        path, _, frag = target.partition("#")
        dec = urllib.parse.unquote(path)
        full = os.path.normpath(os.path.join(here, dec)).replace(os.sep, "/")
        if full not in mapping:
            return m.group(0)
        newrel = os.path.relpath(mapping[full], os.path.dirname(mapping[rel]) or ".").replace(os.sep, "/")
        return m.group(1) + newrel + ("#" + frag if frag else "") + m.group(3)
    return LINK.sub(repl, text)

# 4. build
tmp = Path(tempfile.mkdtemp())
dest = tmp / "groundcontrol"
for rel, new in mapping.items():
    src, dst = SKILL / rel, dest / new
    dst.parent.mkdir(parents=True, exist_ok=True)
    if rel == "SKILL.md":
        dst.write_text(fix_skill(src.read_text(encoding="utf-8")), encoding="utf-8")
    elif rel.endswith(".md"):
        dst.write_text(fix_page(rel, src.read_text(encoding="utf-8")), encoding="utf-8")
    else:
        shutil.copy2(src, dst)

# 5. verify frontmatter and SKILL.md paths
fm = re.search(r"^description: (.*)$", skill_text := (dest / "SKILL.md").read_text(encoding="utf-8"), re.M)
if not fm or len(fm.group(1)) > 1024:
    sys.exit(f"SKILL.md description must be 1–1024 characters (is {len(fm.group(1)) if fm else 0}).")
missing = [r for r in set(re.findall(r"`(references/[^`<]+?)`", skill_text))
           if not (dest / re.sub(r" \(.*$", "", r)).exists()]
if missing:
    sys.exit(f"SKILL.md names paths missing from the package: {missing}")
bad = [n for n in mapping.values() if re.search(r"[^A-Za-z0-9._/\-]", n)]
if bad:
    sys.exit(f"Unsafe paths remain: {bad}")

OUT.parent.mkdir(exist_ok=True)
if OUT.exists():
    OUT.unlink()
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(dest.rglob("*")):
        if p.is_file():
            z.write(p, p.relative_to(tmp).as_posix())
shutil.rmtree(tmp)
print(f"Built {OUT.relative_to(ROOT)} — {len(mapping)} files, {OUT.stat().st_size/1e6:.1f} MB")
