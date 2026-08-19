"""
docxlib.py — light-weight, regex-based helpers for reading and rewriting the
XML parts of a .docx without a heavy DOM. Shared by the house-style scripts.
"""
import re, zipfile


# --- zip io -----------------------------------------------------------------
def read_document_xml(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        return z.read("word/document.xml").decode("utf-8")

def read_part(docx_path, name):
    with zipfile.ZipFile(docx_path) as z:
        return z.read(name).decode("utf-8")

def list_parts(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        return z.namelist()

def write_parts(src_docx, dst_docx, replacements):
    """Copy src_docx to dst_docx, overwriting the parts named in the
    `replacements` dict {partname: new_text}."""
    with zipfile.ZipFile(src_docx) as zin:
        names = zin.namelist()
        with zipfile.ZipFile(dst_docx, "w", zipfile.ZIP_DEFLATED) as zout:
            for n in names:
                data = zin.read(n)
                if n in replacements:
                    data = replacements[n].encode("utf-8")
                zout.writestr(n, data)
            for n, text in replacements.items():
                if n not in names:
                    zout.writestr(n, text.encode("utf-8"))

# --- paragraph parsing ------------------------------------------------------
_P_RE = re.compile(r"<w:p(?: [^>]*)?>.*?</w:p>|<w:p(?: [^>]*)?/>", re.S)
_PSTYLE_RE = re.compile(r'<w:pStyle w:val="([^"]+)"')
_TEXT_RE = re.compile(r"<w:t[^>]*>(.*?)</w:t>", re.S)

def iter_paragraphs(doc_xml):
    """Yield (start, end, xml) for each <w:p> in document order."""
    for m in _P_RE.finditer(doc_xml):
        yield m.start(), m.end(), m.group(0)

def para_style(p_xml):
    m = _PSTYLE_RE.search(p_xml)
    return m.group(1) if m else None

def para_text(p_xml):
    return "".join(_TEXT_RE.findall(p_xml)).replace("‑", "-").strip()

def unescape(s):
    return (s.replace("&amp;", "&").replace("&lt;", "<")
             .replace("&gt;", ">").replace("&quot;", '"').replace("&#8217;", "'"))
