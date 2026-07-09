"""Assemble all chapter/appendix markdown into one book.md with cover, TOC and part dividers."""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(ROOT, "chapters")
ENC = os.path.join(ROOT, "encyclopedia")
OUT = os.path.join(ROOT, "book.md")

# The Strategy Encyclopedia is spliced in right after Part VI (Strategies), i.e. after
# chapter 47 and before chapter 48 (Part VII). Files in reading order:
ENC_FILES = ["E00_intro.md"] + [f"E{i:02d}_" for i in range(1, 14)]
ENC_AFTER_CHAPTER = 47

# chapter-number -> (label, part title) marking where each part begins
PARTS = {
    1:  ("Part I", "Foundations"),
    10: ("Part II", "Payoffs & the Four Basic Positions"),
    16: ("Part III", "Pricing Options"),
    22: ("Part IV", "The Greeks"),
    30: ("Part V", "Volatility"),
    37: ("Part VI", "Options Strategies"),
    48: ("Part VII", "Trading & Risk Management"),
    57: ("Part VIII", "Advanced Topics"),
    62: ("Part IX", "Build Your Own Tools"),
    66: ("Part X", "Practice & Putting It Together"),
    68: ("Appendices", "Reference"),
}

files = sorted(glob.glob(os.path.join(CH, "[0-9]*.md")),
               key=lambda f: (int(os.path.basename(f)[:2]), os.path.basename(f)))

# read each file, capture its first '# ' heading as the TOC title
items = []   # (num, title, text)
for f in files:
    with open(f, encoding="utf-8") as fh:
        text = fh.read().strip()
    num = int(os.path.basename(f)[:2])
    m = re.search(r"^#\s+(.+)$", text, re.M)
    title = m.group(1).strip() if m else os.path.basename(f)
    items.append((num, title, text))

# ---- load the Strategy Encyclopedia (intro + 12 group-chapters) ----
def _enc_path(prefix):
    g = sorted(glob.glob(os.path.join(ENC, prefix + "*.md")))
    return g[0]

enc_items = []   # (title, text)
for pref in ENC_FILES:
    path = os.path.join(ENC, pref) if pref.endswith(".md") else _enc_path(pref)
    with open(path, encoding="utf-8") as fh:
        text = fh.read().strip()
    m = re.search(r"^#\s+(.+)$", text, re.M)
    title = m.group(1).strip() if m else os.path.basename(path)
    enc_items.append((title, text))

# ---- build TOC ----
toc = ["# Table of Contents\n"]
for num, title, _ in items:
    if num in PARTS:
        lbl, pt = PARTS[num]
        toc.append(f"\n**{lbl} — {pt}**\n")
    toc.append(f"- {title}")
    if num == ENC_AFTER_CHAPTER:                 # splice the encyclopedia into the TOC
        toc.append("\n**The Strategy Encyclopedia — 200 Strategies, When to Use Each**\n")
        for etitle, _ in enc_items:
            toc.append(f"- {etitle}")
toc.append("")

# ---- cover ----
_alltext = "\n".join(t for _, _, t in items) + "\n".join(t for _, t in enc_items)
nfig = len(set(re.findall(r"figs/[\w/]+\.png", _alltext)))
cover = f"""<div class="cover">
<div class="cover-kicker">A COMPLETE NSE F&O MASTERCLASS</div>
<div class="cover-title">Options Trading</div>
<div class="cover-sub2">Zero to Professional</div>
<div class="cover-line">From your first call &amp; put to professional-level pricing, the Greeks,
volatility and strategy &mdash; built for Indian markets (Nifty &amp; Bank Nifty).</div>
<div class="cover-meta">{len(items)} chapters &amp; appendices + a 200-strategy encyclopedia &bull; {nfig} figures &bull; worked &#8377; examples</div>
<div class="cover-foot">Saikumar Kaleru &bull; 2026</div>
</div>
<div class="pagebreak"></div>
"""

# ---- body with part dividers ----
body = []
for num, title, text in items:
    if num in PARTS:
        lbl, pt = PARTS[num]
        body.append(f'\n<div class="partpage"><div class="part-lbl">{lbl}</div>'
                    f'<div class="part-title">{pt}</div></div>\n')
    body.append("\n" + text + "\n")
    if num == ENC_AFTER_CHAPTER:                 # splice the encyclopedia into the body
        body.append('\n<div class="partpage"><div class="part-lbl">Strategy Encyclopedia</div>'
                    '<div class="part-title">200 Strategies, and When to Use Each</div></div>\n')
        for _, etext in enc_items:
            body.append("\n" + etext + "\n")

book = cover + "\n".join(toc) + "\n" + "".join(body)
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(book)

print("book.md written:", OUT)
print("chapters/appendices:", len(items))
print("words:", len(book.split()))
print("unique figures referenced:", nfig)
