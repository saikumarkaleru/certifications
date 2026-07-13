"""
Render book.md -> Options_Trading_Zero_to_Professional.pdf

Pipeline (reuses the proven morning_report Chrome approach):
  1. markdown -> HTML (tables, fenced_code, sane_lists) + book CSS (A4, serif, cover,
     part dividers, figure framing, boxed sections).
  2. write temp HTML INSIDE options_book/ so figs/NAME.png resolve, then headless Chrome
     --print-to-pdf to an ABSOLUTE path, poll for completion.
  3. PyMuPDF stamps a running header + page numbers (cover skipped) and builds a
     clickable bookmark outline (parts + chapters + appendices).

RUN
  pip install markdown pymupdf
  python render_book.py
"""

import os
import re
import sys
import time
import tempfile
import subprocess

import markdown
import fitz  # PyMuPDF

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.abspath(__file__))
BOOK_MD = os.path.join(ROOT, "book.md")
TMP_HTML = os.path.join(ROOT, "_book_tmp.html")          # inside ROOT so figs/ resolve
RAW_PDF = os.path.join(ROOT, "_book_raw.pdf")
OUT_PDF = os.path.join(ROOT, "Options_Trading_Zero_to_Professional.pdf")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

TITLE = "Options Trading — Zero to Professional"

CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm; }
* { box-sizing: border-box; }
body {
  font-family: Georgia, 'Times New Roman', serif;
  color: #1b2330; font-size: 11pt; line-height: 1.5;
  text-align: justify; -webkit-hyphens: auto; hyphens: auto;
}

/* ---------- cover ---------- */
.cover {
  height: 252mm; display: flex; flex-direction: column;
  justify-content: center; align-items: center; text-align: center;
  background: linear-gradient(160deg,#0d2440 0%,#16365c 55%,#1f4d7a 100%);
  color: #fff; margin: -20mm -18mm 0 -18mm; padding: 0 24mm;
}
.cover-kicker { text-transform: uppercase; letter-spacing: 4px; font-size: 11pt;
  color: #8fb4dd; font-family: 'Segoe UI',Arial,sans-serif; margin-bottom: 26px; }
.cover-title { font-size: 56pt; font-weight: 700; letter-spacing: 1px; line-height: 1.02;
  font-family: Georgia, serif; }
.cover-sub2 { font-size: 26pt; color: #d6e6f7; font-style: italic; margin-top: 6px; }
.cover-line { font-size: 12.5pt; color: #cfe0f2; max-width: 150mm; margin: 34px auto 0;
  line-height: 1.6; font-family: 'Segoe UI',Arial,sans-serif; font-weight: 300; }
.cover-meta { font-size: 10.5pt; color: #9fc0e2; margin-top: 40px;
  font-family: 'Segoe UI',Arial,sans-serif; border-top: 1px solid #45688f; padding-top: 16px; }
.cover-foot { position: relative; margin-top: 48px; font-size: 12pt; color: #eaf2fb;
  font-family: 'Segoe UI',Arial,sans-serif; letter-spacing: 1px; }
.pagebreak { page-break-after: always; }

/* ---------- part dividers ---------- */
.partpage {
  page-break-before: always; page-break-after: always;
  height: 245mm; display: flex; flex-direction: column;
  justify-content: center; align-items: center; text-align: center;
}
.part-lbl { font-family: 'Segoe UI',Arial,sans-serif; text-transform: uppercase;
  letter-spacing: 6px; font-size: 15pt; color: #1f6098; font-weight: 700; }
.part-title { font-size: 34pt; color: #16365c; margin-top: 18px; max-width: 150mm;
  line-height: 1.15; border-top: 3px solid #d8a93a; border-bottom: 3px solid #d8a93a;
  padding: 18px 10px; }

/* ---------- headings ---------- */
h1 { page-break-before: always; font-size: 23pt; color: #14365c; line-height: 1.15;
  margin: 0 0 4px; padding-bottom: 10px; border-bottom: 3px solid #14365c;
  text-align: left; font-family: 'Segoe UI Semibold','Segoe UI',Arial,sans-serif; }
/* the TOC h1 should not force an extra break beyond the cover's own */
h2 { font-size: 14.5pt; color: #1f6098; margin: 22px 0 8px;
  border-left: 4px solid #d8a93a; padding-left: 10px; text-align: left;
  font-family: 'Segoe UI Semibold','Segoe UI',Arial,sans-serif; page-break-after: avoid; }
h3 { font-size: 12pt; color: #234; margin: 16px 0 6px; text-align: left;
  font-family: 'Segoe UI Semibold','Segoe UI',Arial,sans-serif; page-break-after: avoid; }
p { margin: 7px 0; }

/* ---------- figures ---------- */
figure { margin: 16px auto; text-align: center; page-break-inside: avoid; }
figure img, p img { max-width: 92%; height: auto; border: 1px solid #cdd6e2;
  border-radius: 6px; padding: 4px; background: #fff; }
figcaption { font-family: 'Segoe UI',Arial,sans-serif; font-size: 9pt; color: #5a6b80;
  margin-top: 6px; font-style: italic; }

/* ---------- lists ---------- */
ul, ol { margin: 7px 0 7px 4px; padding-left: 22px; }
li { margin: 3px 0; }

/* ---------- code / formulas ---------- */
code { font-family: 'Consolas','Courier New',monospace; background: #eef2f7;
  color: #143; padding: 1px 5px; border-radius: 4px; font-size: 9.6pt; }
pre { background: #0f2236; color: #e6edf5; padding: 12px 14px; border-radius: 7px;
  overflow-x: auto; page-break-inside: avoid; border-left: 4px solid #d8a93a; }
pre code { background: none; color: #e6edf5; padding: 0; font-size: 9.6pt;
  line-height: 1.45; }

/* ---------- tables ---------- */
table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 9.8pt;
  font-family: 'Segoe UI',Arial,sans-serif; page-break-inside: avoid; }
th { background: #16365c; color: #fff; text-align: left; padding: 6px 9px;
  font-size: 9pt; text-transform: uppercase; letter-spacing: .3px; }
td { padding: 5px 9px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
tr:nth-child(even) td { background: #f5f8fc; }

/* ---------- blockquote ---------- */
blockquote { border-left: 4px solid #1f6098; background: #f3f7fb; margin: 12px 0;
  padding: 8px 14px; color: #33445a; font-size: 10.4pt; }

/* ---------- TOC ---------- */
.toc-block ul { list-style: none; padding-left: 4px; }
.toc-block li { margin: 2px 0; font-family: 'Segoe UI',Arial,sans-serif; font-size: 10.4pt; }
strong { color: #14365c; }
"""


def md_to_html(md_text):
    html = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
        output_format="html5",
    )
    # turn '<img alt="Figure: cap" src="figs/x.png">' into a captioned <figure>
    def figrepl(m):
        alt, src = m.group(1), m.group(2)
        cap = re.sub(r"^Figure:\s*", "", alt).strip()
        return (f'<figure><img src="{src}" alt="{alt}">'
                f'<figcaption>{cap}</figcaption></figure>')
    html = re.sub(r'<img alt="([^"]*)" src="([^"]+)"\s*/?>', figrepl, html)
    # a <p> that only wraps a figure: unwrap so it centres cleanly
    html = re.sub(r'<p>(<figure>.*?</figure>)</p>', r'\1', html, flags=re.S)
    return html


def build_html():
    with open(BOOK_MD, encoding="utf-8") as f:
        md_text = f.read()
    body = md_to_html(md_text)
    # tag the Table-of-Contents list for compact styling
    body = body.replace("<h1>Table of Contents</h1>",
                        '<h1 style="page-break-before:avoid">Table of Contents</h1>'
                        '<div class="toc-block">')
    # close the toc-block right before the first part divider
    body = body.replace('<div class="partpage">', '</div><div class="partpage">', 1)
    doc = (f"<!doctype html><html><head><meta charset='utf-8'>"
           f"<style>{CSS}</style></head><body>{body}</body></html>")
    with open(TMP_HTML, "w", encoding="utf-8") as f:
        f.write(doc)
    return TMP_HTML


def chrome_pdf(html_path, pdf_path):
    pdf_path = os.path.abspath(pdf_path)
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
    profile = os.path.join(tempfile.gettempdir(), "chrome_pdf_profile_book")
    url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-first-run",
                    f"--user-data-dir={profile}", "--no-pdf-header-footer",
                    "--virtual-time-budget=30000",
                    f"--print-to-pdf={pdf_path}", url],
                   check=False, stderr=subprocess.DEVNULL)
    for _ in range(60):
        if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
            time.sleep(1)  # let the write settle
            break
        time.sleep(1)


def stamp_and_outline(raw_pdf, out_pdf):
    doc = fitz.open(raw_pdf)
    n = len(doc)

    # --- read page text once (for header suppression + outline location) ---
    texts = [doc[i].get_text("text") for i in range(n)]

    def is_special(t):
        # cover or part-divider page: very little body text, large display words.
        # NB: CSS letter-spacing makes PDF text extract as "P A R T", so compare on a
        # whitespace-stripped, upper-cased copy.
        stripped = t.strip()
        if not stripped:
            return True
        if "A COMPLETE NSE F&O MASTERCLASS" in t:
            return True
        compact = re.sub(r"\s+", "", t).upper()
        if len(stripped) < 160 and (compact.startswith("PART")
                                    or compact.startswith("APPENDICES")
                                    or compact.startswith("STRATEGYENCYCLOPEDIA")):
            return True
        return False

    # --- header + page number stamp ---
    gray = (0.42, 0.47, 0.54)
    rule = (0.80, 0.84, 0.89)
    folio = 0
    for i in range(n):
        page = doc[i]
        if i == 0:
            continue  # cover: nothing
        if is_special(texts[i]):
            continue  # part dividers: keep clean
        folio += 1
        r = page.rect
        # running header
        page.insert_text((r.width / 2 - 110, 26), TITLE,
                         fontname="helv", fontsize=8, color=gray)
        page.draw_line((50, 32), (r.width - 50, 32), color=rule, width=0.5)
        # footer page number (centred)
        page.insert_text((r.width / 2 - 8, r.height - 22), str(folio),
                         fontname="helv", fontsize=9, color=gray)

    # --- build clickable outline from book.md structure ---
    # locate TOC pages to avoid matching titles there
    toc_pages = {i for i, t in enumerate(texts)
                 if (t.count("Chapter ") + t.count("Strategy Group")) >= 5}

    def find_page(needle, start=0):
        # strip ALL whitespace so a line-wrapped heading (e.g. "Quick-\nReference")
        # still matches the source title.
        key = re.sub(r"\s+", "", needle)[:40].lower()
        for i in range(start, n):
            if i in toc_pages:
                continue
            flat = re.sub(r"\s+", "", texts[i]).lower()
            if key and key in flat:
                return i
        return None

    # parse parts + chapter titles straight from book.md
    with open(BOOK_MD, encoding="utf-8") as f:
        md_text = f.read()
    toc = []
    # part dividers in md: <div class="partpage">..part-lbl..part-title..
    # chapters: lines like '# Chapter N: Title' and appendix '# Appendix X:'
    cursor = 0
    chap_re = r'^#\s+((?:Chapter|Appendix|Strategy Group|The Options Strategy Encyclopedia)\b.+)$'
    for m in re.finditer(chap_re, md_text, re.M):
        title = m.group(1).strip()
        pg = find_page(title, cursor)
        if pg is None:
            pg = find_page(title, 0)
        if pg is None:
            continue
        cursor = pg
        toc.append([1, title, pg + 1])

    # part dividers as level-1, chapters become level-2 under them
    parts = []
    for m in re.finditer(r'part-lbl">([^<]+)</div><div class="part-title">([^<]+)</div>',
                         md_text):
        parts.append(f"{m.group(1).strip()} — {m.group(2).strip()}")
    # locate each part page (special page whose text holds the part title)
    part_entries = []
    for lbl in parts:
        ttl = lbl.split("—", 1)[-1].strip()
        for i in range(n):
            t = re.sub(r"\s+", " ", texts[i]).strip()
            if len(t) < 120 and ttl.lower()[:24] in t.lower():
                part_entries.append([1, lbl, i + 1])
                break

    # merge: parts (lvl1) + their chapters (lvl2), in page order
    merged = []
    for lvl, title, pg in toc:
        merged.append([2, title, pg])
    for lvl, title, pg in part_entries:
        merged.append([1, title, pg])
    merged.sort(key=lambda x: (x[2], x[0]))
    # ensure first entry is level 1 (PyMuPDF requires a valid hierarchy)
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
    print("1/3  markdown -> HTML ...")
    html_path = build_html()
    print("     temp HTML:", html_path, f"({os.path.getsize(html_path)//1024} KB)")

    print("2/3  HTML -> PDF (headless Chrome) ...")
    chrome_pdf(html_path, RAW_PDF)
    if not (os.path.exists(RAW_PDF) and os.path.getsize(RAW_PDF) > 0):
        print("ERROR: Chrome did not produce a PDF.")
        return
    print("     raw PDF:", f"{os.path.getsize(RAW_PDF)//1024} KB")

    print("3/3  stamping page numbers + outline (PyMuPDF) ...")
    total, numbered = stamp_and_outline(RAW_PDF, OUT_PDF)
    print(f"\nDONE  ->  {OUT_PDF}")
    print(f"      pages: {total}  (numbered: {numbered})")
    print(f"      size : {os.path.getsize(OUT_PDF)//1024} KB")

    # cleanup intermediates (keep the final PDF + book.md + figs)
    for p in (TMP_HTML, RAW_PDF):
        try:
            os.remove(p)
        except OSError:
            pass


if __name__ == "__main__":
    main()
