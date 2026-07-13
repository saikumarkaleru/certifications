# Master Resource List & 12-Month Plan

## What it is & where it's used

This is the capstone chapter: a single, curated list of every course, book, channel, and dataset worth your time — mapped onto a **12-month calendar** that turns the whole Playbook into a schedule you can actually follow. No new tool here; the "skill" is **learning-project management**: sequencing skills so each one compounds into the next (Excel → SQL → Python → BI → domain), and producing *proof-of-work* (a GitHub repo, a dashboard, a reconciled book) that a hiring manager can click.

It's used by every early-career finance candidate — MBA + CA-Inter, B.Com + interviewing, or a working analyst trying to move from "MIS person" to "FP&A / data / tax specialist." Recruiters don't hire syllabi; they hire someone who can show a completed thing. This chapter is how you build a stack of completed things in a year while still clearing CA papers.

## The gap: why companies want this (and college didn't teach it)

College hands you 40 subjects and zero prioritisation. You graduate "knowing" accounting, stats, finance, and IT — none of it to a *job-ready depth*, and nothing integrated. Employers, by contrast, want a **T-shaped** person: broad awareness, one or two spikes deep enough to be trusted unaided on day one.

| What college optimises for | What employers pay for |
|---|---|
| Coverage (pass 40 subjects) | Depth (own 2 skills end-to-end) |
| Individual exams | A portfolio of shipped deliverables |
| Theory you can recite | A model/query/return you can *produce* |
| Fixed 3-year timeline | Self-directed 90-day skill sprints |

The missing meta-skill is **deliberate sequencing under a deadline** — exactly what a 12-month plan enforces. Do it and you arrive at interviews with a link, not a promise.

## What "proficient" looks like

A job-ready person, unaided, can:

- **Excel/FP&A:** build a 3-statement model with a working circular-reference switch; use `XLOOKUP`, `SUMIFS`, `INDEX/MATCH`, dynamic arrays; write a variance commentary.
- **Accounting/Tax:** pass any routine journal, close a trial balance, file GSTR-1 / GSTR-3B, reconcile GSTR-2B to books, compute TDS and advance tax.
- **SQL:** join 3+ tables, window functions, CTEs — pull a P&L from raw ledgers.
- **Python:** clean a messy CSV with `pandas`, automate a monthly report.
- **BI:** a Power BI dashboard with DAX measures (`Total Sales`, YoY%, running totals).
- **Meta:** a public GitHub with 3–4 mini-projects and a one-line README each.

The bar is **"can you do it live, on a timer, without Google for the basics."**

## Hands-on: how to actually do it

The engine of the year is a repeating **90-day skill sprint**. Each sprint: *Learn (weeks 1–4) → Build (5–10) → Ship + document (11–12).* Track it in one Excel sheet so the plan is itself a proof of your Excel.

Build a self-updating tracker. Columns: `Skill | Sprint | StartDate | TargetDate | Status | ProofURL`.

```
# % of the year elapsed, live:
=TEXT((TODAY()-DATE(2026,7,1))/365,"0.0%")

# Days left in the current sprint:
=[@TargetDate]-TODAY()

# RAG status flag:
=IF([@Status]="Done","🟢",IF([@TargetDate]-TODAY()<0,"🔴","🟡"))

# Count of shipped proofs:
=COUNTIF(Tracker[Status],"Done")

# Pull the next unfinished skill (dynamic array):
=FILTER(Tracker[Skill],Tracker[Status]<>"Done")
```

SQL to log study hours in a tiny SQLite/Postgres table and see weekly pace:

```sql
SELECT strftime('%Y-%W', log_date) AS week,
       skill,
       SUM(hours)                    AS hrs
FROM   study_log
GROUP  BY week, skill
HAVING SUM(hours) > 0
ORDER  BY week DESC;
```

Python to nag yourself — pulls the tracker and prints red items:

```python
import pandas as pd, datetime as dt
df = pd.read_excel("tracker.xlsx", sheet_name="Tracker")
today = pd.Timestamp(dt.date.today())
overdue = df[(df.Status != "Done") & (df.TargetDate < today)]
print(f"{len(overdue)} skill(s) slipping:")
print(overdue[["Skill", "TargetDate"]].to_string(index=False))
```

DAX measure for a "career progress" card in Power BI:

```
Skills Shipped % =
DIVIDE(
    CALCULATE(COUNTROWS(Tracker), Tracker[Status] = "Done"),
    COUNTROWS(Tracker)
)
```

## Worked example / mini-project

**Project: "One-Year Finance Skills Dashboard."** Realistic India-context plan for a CA-Inter candidate starting July 2026.

The 12-month map (study alongside CA, ~10 hrs/week on skills):

| Month | Sprint focus | Ship (proof-of-work) | Primary resource |
|---|---|---|---|
| Jul–Aug | Advanced Excel + FP&A | 3-statement model of a listed Indian FMCG (from annual report) | Wall Street Prep / CFI Excel |
| Sep | Accounting close + Tally | Closed a set of books; trial balance → P&L | TallyPrime + ICAI notes |
| Oct–Nov | GST + TDS practical | Filed a dummy GSTR-1/3B; GSTR-2B reco sheet | GST portal + ClearTax blog |
| Dec | SQL for finance | Query pack pulling P&L from raw sales table | Mode SQL Tutorial (free) |
| Jan–Feb | Python + pandas | Auto monthly MIS from 3 CSVs | Kaggle "Pandas" micro-course |
| Mar | Power BI + DAX | Sales & AR dashboard, 8 measures | Microsoft Learn (free) |
| Apr | Financial modelling / valuation | DCF + comps of the same FMCG | Aswath Damodaran (free) |
| May | Capstone + portfolio | GitHub README linking all six | — |
| Jun | Interview prep + polish | Mock tests, resume rewrite | This Playbook |

**Concrete numbers to reproduce the Excel piece:** take Hindustan Unilever-style figures — Revenue ₹62,000 cr, EBITDA margin 24%, tax rate 25.17%, capex ₹1,200 cr, WC days 15. Build the model, then flex revenue growth 6%/8%/10% and watch FCF. The *deliverable* is one `.xlsx` with a scenario dropdown, pushed to GitHub — that single file beats "MBA Finance" on a resume.

A sample journal from the Sept close sprint, to prove the accounting spike:

| Date | Particulars | Dr (₹) | Cr (₹) |
|---|---|---|---|
| 30-Sep | Depreciation A/c ..... Dr | 50,000 | |
| | To Accumulated Depreciation A/c | | 50,000 |
| 30-Sep | Salaries A/c ..... Dr | 2,00,000 | |
| | To Salaries Payable A/c | | 2,00,000 |
| 30-Sep | Profit & Loss A/c ..... Dr | 2,50,000 | |
| | To Depreciation A/c | | 50,000 |
| | To Salaries A/c | | 2,00,000 |

## How it's tested

Hiring for these roles almost always includes a **practical**, not just a chat:

- **FP&A / analyst:** a *timed 45-min Excel case* — "here's a raw sales dump, build a summary P&L with `SUMIFS` and a pivot, comment on the biggest variance." No formulas from memory = fail.
- **Data-leaning finance:** a *SQL screen* on HackerRank / DataLemur — 2–3 questions, usually a window function and a self-join.
- **Accounts / audit:** a *"close these books"* case — you're handed a trial balance with errors to find, or asked to pass adjusting entries live.
- **Tax:** compute TDS on a set of invoices, or reconcile GSTR-2B mismatches and state the ITC allowed.
- **Interview questions:** "Walk me through your 3-statement model." / "How did you build that dashboard — what's the DAX?" / "Show me your GitHub." The follow-ups probe whether *you* did it.

The tell that separates you: you can screen-share and *do the thing*, because you shipped six of them this year.

## Common mistakes & how pros avoid them

- **Tutorial hell.** Watching 40 hours, building nothing. Pros cap learning at ~30% of sprint time; the rest is building.
- **Breadth with no spike.** "A little Python, a little BI, a little SQL" impresses no one. Go deep on one per sprint.
- **No proof.** If it's not on GitHub or a shareable file, it didn't happen to a recruiter.
- **Buying every course.** 90% of what you need is free (below). Pros pay only for structured modelling (WSP/CFI) or a domain cert.
- **Ignoring the CA overlap.** Your CA tax/audit/costing papers *are* domain depth — reuse them as portfolio topics, don't treat them as separate.
- **Perfectionism.** A shipped B-grade dashboard beats an unfinished A-grade one. Timebox, then ship.

## Learn-it roadmap & resources

**Time-to-proficiency:** ~10 hrs/week for 12 months gets you interview-ready in 2–3 skills. Each 90-day sprint = one credible spike.

**The master list (free unless noted):**

| Skill | Best resource | Cost |
|---|---|---|
| Excel/FP&A | CFI FMVA (paid), Wall Street Prep, ExcelIsFun (YouTube) | Free–₹30k |
| Modelling/Valuation | Aswath Damodaran (NYU, free lectures + spreadsheets) | Free |
| Accounting/Tax | ICAI study material, ClearTax & TaxGuru blogs, CA Rachana Ranade (YT) | Free |
| Tally/GST | TallyPrime learning portal, GST portal (practice with dummy GSTIN) | Free |
| SQL | Mode SQL Tutorial, DataLemur, SQLBolt | Free |
| Python | Kaggle micro-courses, "Automate the Boring Stuff" (free book) | Free |
| Power BI/DAX | Microsoft Learn, SQLBI (Marco Russo), Guy in a Cube (YT) | Free |
| Books | *Financial Modeling* (Benninga), *Storytelling with Data* (Knaflic), *Naked Statistics* (Wheelan) | Paid |
| Portfolio | GitHub + a one-page Notion/PDF case study each | Free |

**Certifications worth it (India-relevant):** CFA/FRM if going capital-markets/risk; NISM for securities roles; Microsoft PL-300 for Power BI; your CA itself is the strongest single credential — finish it. Skip generic "Udemy certificates" — they signal nothing.

## Quick-reference

| Item | Value |
|---|---|
| Sprint length | 90 days: Learn (4w) → Build (6w) → Ship (2w) |
| Weekly commitment | ~10 hrs skills, on top of CA study |
| Learn:Build ratio | 30 : 70 |
| Sprints in the year | 4 major + 2 short = 6 shipped proofs |
| Progress formula | `=(TODAY()-DATE(2026,7,1))/365` |
| Overdue flag | `=IF([@TargetDate]-TODAY()<0,"🔴","🟢")` |
| Shipped count | `=COUNTIF(Tracker[Status],"Done")` |
| SQL pace check | `GROUP BY strftime('%Y-%W', log_date)` |
| DAX progress | `DIVIDE(done_rows, total_rows)` |
| Non-negotiable | Every sprint ends with a public, clickable deliverable |
| Free stack | Mode (SQL) · Kaggle (Python) · MS Learn (BI) · Damodaran (valuation) |
| Paid, if any | CFI/WSP (Excel modelling); PL-300 (BI); finish CA |

**The one rule that makes the year work:** never finish a sprint without a link you can paste into a resume. Six links in twelve months closes the MBA-to-employer gap for good.
