"""
Render a chapter-folder subject ("<Subject>/md/NN_chapter-name.md" files) -> a
styled PDF study guide. Companion to build_handbook_pdf.py (which handles a
single-file handbook instead of a folder of numbered chapters).

Replaces the old scratchpad/build_subject_pdf.py used to originally build
Finance/05_Equity_and_Capital_Markets.pdf, Finance/03_Valuation.pdf, etc.
(that script lived in a session scratchpad and no longer exists) so these
subjects can be deepened and rebuilt reproducibly going forward.

Pipeline: same as build_handbook_pdf.py — concatenate md/*.md chapters
(sorted by numeric filename prefix) -> one HTML doc with book CSS ->
headless Chrome --print-to-pdf -> PyMuPDF stamps header/page-numbers and
builds a clickable outline (chapter H1s level 1, ## sections level 2).

RUN
  python build_subject_pdf.py <subject_dir> "<Title>" <output.pdf>
  e.g. python build_subject_pdf.py ../EquityCapitalMarkets "Equity & Capital Markets" ../05_Equity_and_Capital_Markets.pdf
"""

import os
import re
import sys
import glob
import time
import tempfile
import subprocess

import markdown
import fitz  # PyMuPDF

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Same CSS as build_handbook_pdf.py, chapter h1s (not "page-break-before: always"
# by default in markdown->html, so each chapter file is wrapped with a pagebreak div).
CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm; }
* { box-sizing: border-box; }
body {
  font-family: Georgia, 'Times New Roman', serif;
  color: #1b2330; font-size: 11pt; line-height: 1.5;
  text-align: justify; -webkit-hyphens: auto; hyphens: auto;
}
.cover {
  height: 252mm; display: flex; flex-direction: column;
  justify-content: center; align-items: center; text-align: center;
  background: linear-gradient(160deg,#0d2440 0%,#16365c 55%,#1f4d7a 100%);
  color: #fff; margin: -20mm -18mm 0 -18mm; padding: 0 24mm;
}
.cover-kicker { text-transform: uppercase; letter-spacing: 4px; font-size: 11pt;
  color: #8fb4dd; font-family: 'Segoe UI',Arial,sans-serif; margin-bottom: 26px; }
.cover-title { font-size: 44pt; font-weight: 700; letter-spacing: 1px; line-height: 1.1;
  font-family: Georgia, serif; max-width: 165mm; }
.cover-line { font-size: 12.5pt; color: #cfe0f2; max-width: 150mm; margin: 34px auto 0;
  line-height: 1.6; font-family: 'Segoe UI',Arial,sans-serif; font-weight: 300; }
.cover-foot { position: relative; margin-top: 48px; font-size: 12pt; color: #eaf2fb;
  font-family: 'Segoe UI',Arial,sans-serif; letter-spacing: 1px; }
.pagebreak { page-break-after: always; }
.chapter { page-break-before: always; }
h1 { font-size: 21pt; color: #14365c; line-height: 1.15;
  margin: 0 0 4px; padding-bottom: 10px; border-bottom: 3px solid #14365c;
  text-align: left; font-family: 'Segoe UI Semibold','Segoe UI',Arial,sans-serif; }
h2 { font-size: 14pt; color: #1f6098; margin: 22px 0 8px;
  border-left: 4px solid #d8a93a; padding-left: 10px; text-align: left;
  font-family: 'Segoe UI Semibold','Segoe UI',Arial,sans-serif; page-break-after: avoid; }
h3 { font-size: 11.5pt; color: #234; margin: 14px 0 6px; text-align: left;
  font-family: 'Segoe UI Semibold','Segoe UI',Arial,sans-serif; page-break-after: avoid; }
p { margin: 7px 0; }
ul, ol { margin: 7px 0 7px 4px; padding-left: 22px; }
li { margin: 3px 0; }
code { font-family: 'Consolas','Courier New',monospace; background: #eef2f7;
  color: #143; padding: 1px 5px; border-radius: 4px; font-size: 9.6pt; }
pre { background: #0f2236; color: #e6edf5; padding: 12px 14px; border-radius: 7px;
  overflow-x: auto; page-break-inside: avoid; border-left: 4px solid #d8a93a; }
pre code { background: none; color: #e6edf5; padding: 0; font-size: 9.6pt; line-height: 1.45; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 9.8pt;
  font-family: 'Segoe UI',Arial,sans-serif; page-break-inside: avoid; }
th { background: #16365c; color: #fff; text-align: left; padding: 6px 9px;
  font-size: 9pt; text-transform: uppercase; letter-spacing: .3px; }
td { padding: 5px 9px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
tr:nth-child(even) td { background: #f5f8fc; }
blockquote { border-left: 4px solid #1f6098; background: #f3f7fb; margin: 12px 0;
  padding: 8px 14px; color: #33445a; font-size: 10.4pt; }
strong { color: #14365c; }
.mermaid { text-align: center; margin: 14px 0; page-break-inside: avoid; }
.mermaid svg { max-width: 100%; height: auto !important; }
img { max-width: 92%; display: block; margin: 14px auto; page-break-inside: avoid;
  border: 1px solid #e2e8f0; border-radius: 6px; }
"""

MERMAID_JS_PATH = os.path.join(ROOT, "vendor", "mermaid.min.js")

MERMAID_INIT_SCRIPT = """
<script>
document.querySelectorAll('pre > code.mermaid, pre > code.language-mermaid').forEach(function(code) {
  var pre = code.parentElement;
  var div = document.createElement('div');
  div.className = 'mermaid';
  div.textContent = code.textContent;
  pre.replaceWith(div);
});
mermaid.initialize({ startOnLoad: false, theme: 'default', themeVariables: { fontFamily: 'Segoe UI, Arial, sans-serif' } });
mermaid.run();
</script>
"""


def mermaid_script_tag():
    """Inline the local mermaid.min.js (no CDN dependency at render time)."""
    if not os.path.exists(MERMAID_JS_PATH):
        return ""
    with open(MERMAID_JS_PATH, encoding="utf-8") as f:
        js = f.read()
    return f"<script>{js}</script>{MERMAID_INIT_SCRIPT}"


def ensure_blank_line_before_tables(md_text):
    """python-markdown's `tables` extension only recognises a table if it's
    preceded by a blank line -- a huge fraction of this library's tables
    immediately follow a bold '**Label:**' line with no blank line, so they
    silently render as raw pipe-delimited text instead of an HTML table.
    Insert the missing blank line before any '|'-prefixed row whose
    preceding line is non-blank and isn't itself a table row."""
    lines = md_text.split("\n")
    out = []
    for i, line in enumerate(lines):
        if (line.lstrip().startswith("|") and out and out[-1].strip() != ""
                and not out[-1].lstrip().startswith("|")):
            out.append("")
        out.append(line)
    return "\n".join(out)


def md_to_html(md_text):
    md_text = ensure_blank_line_before_tables(md_text)
    return markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
        output_format="html5",
    )


def chapter_files(subject_dir):
    md_dir = os.path.join(subject_dir, "md")
    files = sorted(glob.glob(os.path.join(md_dir, "*.md")))
    if not files:
        raise SystemExit(f"No chapters found in {md_dir}")
    return files


def qa_file_for(subject_dir, chapter_fp):
    """Optional qa/<stem>_QA.md sibling for a md/<stem>.md chapter, if present."""
    stem = os.path.splitext(os.path.basename(chapter_fp))[0]
    qa_fp = os.path.join(subject_dir, "qa", f"{stem}_QA.md")
    return qa_fp if os.path.exists(qa_fp) else None


def build_html(subject_dir, title, tmp_html):
    files = chapter_files(subject_dir)
    chapters_html = []
    outline_files = []  # (md_path, is_qa) pairs, in render order, for TOC building
    for fp in files:
        with open(fp, encoding="utf-8") as f:
            md_text = f.read()
        chapters_html.append(f'<div class="chapter">{md_to_html(md_text)}</div>')
        outline_files.append((fp, False))
        qa_fp = qa_file_for(subject_dir, fp)
        if qa_fp:
            with open(qa_fp, encoding="utf-8") as f:
                qa_text = f.read()
            chapters_html.append(f'<div class="chapter">{md_to_html(qa_text)}</div>')
            outline_files.append((qa_fp, True))
    body = "\n".join(chapters_html)
    cover = f"""<div class="cover">
<div class="cover-kicker">Study Guide</div>
<div class="cover-title">{title}</div>
<div class="cover-line">A complete, concept-first reference &mdash; prepared for Saikumar Kaleru.</div>
<div class="cover-foot">certifications / study / Finance &bull; 2026</div>
</div><div class="pagebreak"></div>"""
    doc = (f"<!doctype html><html><head><meta charset='utf-8'>"
           f"<style>{CSS}</style></head><body>{cover}{body}{mermaid_script_tag()}</body></html>")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(doc)
    return tmp_html, outline_files


def chrome_pdf(html_path, pdf_path):
    pdf_path = os.path.abspath(pdf_path)
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
    profile = os.path.join(tempfile.gettempdir(), "chrome_pdf_profile_subject")
    url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-first-run",
                    f"--user-data-dir={profile}", "--no-pdf-header-footer",
                    "--virtual-time-budget=60000",
                    f"--print-to-pdf={pdf_path}", url],
                   check=False, stderr=subprocess.DEVNULL)
    for _ in range(90):
        if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
            time.sleep(1)
            break
        time.sleep(1)


def stamp_and_outline(raw_pdf, out_pdf, title, outline_files):
    doc = fitz.open(raw_pdf)
    n = len(doc)
    texts = [doc[i].get_text("text") for i in range(n)]

    gray = (0.42, 0.47, 0.54)
    rule = (0.80, 0.84, 0.89)
    folio = 0
    for i in range(n):
        page = doc[i]
        if i == 0:
            continue  # cover
        folio += 1
        r = page.rect
        page.insert_text((r.width / 2 - 110, 26), title,
                         fontname="helv", fontsize=8, color=gray)
        page.draw_line((50, 32), (r.width - 50, 32), color=rule, width=0.5)
        page.insert_text((r.width / 2 - 8, r.height - 22), str(folio),
                         fontname="helv", fontsize=9, color=gray)

    def find_page(needle, start=0):
        key = re.sub(r"\s+", "", needle)[:40].lower()
        for i in range(start, n):
            flat = re.sub(r"\s+", "", texts[i]).lower()
            if key and key in flat:
                return i
        return None

    merged = []
    cursor = 0
    for fp, is_qa in outline_files:
        with open(fp, encoding="utf-8") as f:
            md_text = f.read()
        m1 = re.search(r'^#\s+(.+)$', md_text, re.M)
        if not m1:
            continue
        t = m1.group(1).strip()
        pg = find_page(t, cursor)
        if pg is None:
            pg = find_page(t, 0)
        if pg is not None:
            cursor = pg
            level = 2 if is_qa else 1
            merged.append([level, t, pg + 1])
            if not is_qa:
                sub_cursor = pg
                for m2 in re.finditer(r'^##\s+(.+)$', md_text, re.M):
                    t2 = m2.group(1).strip()
                    pg2 = find_page(t2, sub_cursor)
                    if pg2 is not None:
                        sub_cursor = pg2
                        merged.append([2, t2, pg2 + 1])
    merged.sort(key=lambda x: (x[2], x[0]))
    if merged and merged[0][0] != 1:
        merged[0][0] = 1
    try:
        doc.set_toc(merged)
    except Exception as e:
        print("outline warning:", e)

    doc.save(out_pdf, deflate=True, garbage=4)
    doc.close()
    return n, folio


def main():
    if len(sys.argv) != 4:
        print('Usage: python build_subject_pdf.py <subject_dir> "<Title>" <output.pdf>')
        sys.exit(1)
    subject_dir, title, out_pdf = sys.argv[1], sys.argv[2], sys.argv[3]
    subject_dir = os.path.abspath(subject_dir)
    out_pdf = os.path.abspath(out_pdf)
    tmp_html = os.path.join(ROOT, "_subject_tmp.html")
    raw_pdf = os.path.join(ROOT, "_subject_raw.pdf")

    print("1/3  chapters -> HTML ...")
    _, outline_files = build_html(subject_dir, title, tmp_html)
    n_qa = sum(1 for _, is_qa in outline_files if is_qa)
    print(f"     {len(outline_files) - n_qa} chapters + {n_qa} qa files")

    print("2/3  HTML -> PDF (headless Chrome) ...")
    chrome_pdf(tmp_html, raw_pdf)
    if not (os.path.exists(raw_pdf) and os.path.getsize(raw_pdf) > 0):
        print("ERROR: Chrome did not produce a PDF.")
        sys.exit(1)

    print("3/3  stamping page numbers + outline (PyMuPDF) ...")
    total, numbered = stamp_and_outline(raw_pdf, out_pdf, title, outline_files)
    print(f"\nDONE  ->  {out_pdf}")
    print(f"      pages: {total}  (numbered: {numbered})")
    print(f"      size : {os.path.getsize(out_pdf)//1024} KB")

    for p in (tmp_html, raw_pdf):
        try:
            os.remove(p)
        except OSError:
            pass


if __name__ == "__main__":
    main()
