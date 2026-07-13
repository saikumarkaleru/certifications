# The interview-prep system

## What it is & where it's used

An interview-prep *system* is a repeatable, calendar-driven routine that turns "I hope they don't ask something hard" into "I have rehearsed this exact answer out loud." It has three tracks that every finance hiring loop tests, in some mix:

1. **Technical** — accounting, valuation, tax, FM concepts, GST/TDS mechanics, IFRS/Ind AS.
2. **Practical / assessment test** — a timed Excel model, a SQL screen, a "close these books" case, a live TallyPrime task, a GST return walk-through.
3. **Behavioral** — "walk me through a time you missed a deadline," fit, communication.

Where it's used: **every** role you're targeting — Big 4 audit/tax, FP&A/finance-analyst seats, controllership, treasury, equity research, KPO/GCC finance ops (Genpact, WNS, Deloitte USI), startup finance. The mix changes: audit leans technical + case; FP&A leans Excel test + behavioral; research leans modelling case + market view; KPO leans a timed assessment + versant English test.

## The gap: why companies want this (and college didn't teach it)

MBA and CA theory teaches you *what* a DCF is. The interview tests whether you can **build one in Excel in 25 minutes**, defend the WACC, and explain why FCFF ≠ PAT. College grades a written exam; employers grade a **live, timed, unaided performance** under a stranger's questions. Nobody in class made you say "I don't know, but here's how I'd find out" without panicking.

The specific gaps this chapter closes:

- **Recall → retrieval under pressure.** You know depreciation; can you post the entry when the interviewer stares at you?
- **Answers → structured answers.** Behavioral rounds reward STAR structure, not rambling.
- **One-size prep → role-specific prep.** Prepping the same 20 questions for audit and FP&A wastes both loops.
- **Cramming → cadence.** Mock tests spaced over weeks beat a panicked all-nighter.

## What "proficient" looks like

A job-ready candidate can, **unaided**:

| Track | The bar an interviewer is testing for |
|---|---|
| Technical | Answer a concept in 60–90 sec: definition → why → one number/example. Handle a 2-level follow-up ("and if rates rise?"). |
| Practical | Finish a timed Excel/SQL/Tally task correctly with keyboard, no mouse-hunting, no Googling formulas. |
| Behavioral | Deliver a STAR story in ~2 min with a real metric ("cut the close from 8 to 5 days"). |
| Meta | Say "I don't know" cleanly, then reason toward an answer. |

Concretely: build a 3-statement model skeleton in <30 min; write a `GROUP BY` join without help; compute GST liability with ITC set-off; explain deferred tax with an entry.

## Hands-on: how to actually do it

### 1. Build a question bank, then rehearse out loud

Maintain a tracker (Excel/Notion). Columns: `Question | Track | Role | My 90-sec answer | Confidence 1-5 | Last practiced`. Filter by confidence to know what to drill.

Quick Excel to surface weak spots:

```excel
=FILTER(A2:F200, (E2:E200<=3)*(C2:C200="FP&A"))
```

Sort by last-practiced so nothing goes stale:

```excel
=SORTBY(A2:F200, F2:F200, 1)
```

### 2. Technical drills — say the answer in a formula/entry, not prose

Rehearse *the artifact*, not a paragraph. Examples you should be able to produce instantly:

**Deferred tax on faster book vs tax depreciation** (India, timing difference):

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Deferred Tax Expense (P&L) | 25,000 | |
| To Deferred Tax Liability | | 25,000 |

**FCFF from PAT** — recite the bridge:

```
FCFF = PAT + Interest×(1−t) + Depreciation − Capex − ΔWorking Capital
```

**Valuation multiple sanity check in Excel:**

```excel
=EV / EBITDA      // e.g. =4500/600 -> 7.5x, then compare to peer median
```

### 3. Practical-test drills — timed, keyboard-only

**Excel screen (FP&A/analyst).** Practice these until they're muscle memory:

```excel
=XLOOKUP(A2, Master[Code], Master[Name], "Not found")
=SUMIFS(Amount, Region, "South", Month, ">="&DATE(2026,4,1))
=IFERROR(Rev/Prev-1, "n/a")            // MoM growth, guarded
=EOMONTH(TODAY(),-1)                    // last month-end for aging
```

**SQL screen (KPO/GCC/analytics).** Rehearse the classic "top vendors by spend":

```sql
SELECT v.vendor_name,
       SUM(i.amount)          AS total_spend,
       COUNT(*)               AS invoice_count
FROM   invoices i
JOIN   vendors  v ON v.vendor_id = i.vendor_id
WHERE  i.invoice_date >= '2026-04-01'
GROUP  BY v.vendor_name
HAVING SUM(i.amount) > 100000
ORDER  BY total_spend DESC
LIMIT  10;
```

**Python (data/analyst roles).** A 5-line profit-margin cut they can ask you to write:

```python
import pandas as pd
df = pd.read_csv("sales.csv")
df["margin"] = (df["revenue"] - df["cogs"]) / df["revenue"]
print(df.groupby("region")["margin"].mean().sort_values())
```

**DAX (Power BI dashboards):**

```dax
Total Revenue = SUM(Sales[Revenue])
YoY % = DIVIDE([Total Revenue] - CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('Date'[Date])), CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('Date'[Date])))
```

**TallyPrime / GST-portal (accounts/tax roles).** Be able to narrate the click-path:
- Tally sales entry: `Gateway of Tally → Vouchers → F8 (Sales) → party → item → GST auto-computes → Ctrl+A to save`.
- GSTR-3B: `gst.gov.in → login → Returns Dashboard → select period → GSTR-3B → Prepare Online → fill 3.1 outward + 4 ITC → Save → Proceed to Pay → File with DSC/EVC`.

### 4. Behavioral — STAR, timed to 2 minutes

Write 6–8 stories once, in this frame:

| S | Situation (1 line, context) |
| T | Task (what you owned) |
| A | Action (2–3 specific things *you* did) |
| R | Result (a **number**) |

Example: *"Month-end close ran 8 days (S). I owned the payables reconciliation (T). I built a SUMIFS-based auto-match sheet and a daily cut-off checklist (A). Close dropped to 5 days, and unmatched entries fell 70% (R)."*

## Worked example / mini-project: a 2-week prep sprint for one FP&A role

Target: **Finance Analyst, FMCG GCC, Bengaluru.** JD says: Excel modelling, variance analysis, SQL basics, stakeholder communication.

**Step 1 — decode the JD into a prep map:**

| JD phrase | Track | Drill |
|---|---|---|
| "budget vs actual variance" | Technical + Excel | Build a variance sheet with SUMIFS + % delta |
| "SQL to pull data" | Practical | 10 GROUP BY/JOIN queries |
| "partner with business" | Behavioral | 2 stakeholder STAR stories |

**Step 2 — build the reproducible variance model.** Data: budget ₹1.20 cr, actual ₹1.38 cr for a South region quarter.

```excel
Variance      =Actual - Budget            // =13800000-12000000 -> 1,800,000
Variance %    =(Actual-Budget)/Budget     // -> 15.0%
Flag          =IF(ABS(Variance%)>0.10,"Investigate","OK")
```

Then a one-line commentary you rehearse aloud: *"South is 15% over budget, ₹18 lakh, driven by trade-promo overspend; volume was on plan, so it's a price/mix issue — I'd pull the promo calendar next."*

**Step 3 — mock the SQL** using the vendor query above on sample data.

**Step 4 — run a full 45-min mock:** 15 min technical Q&A, 20 min Excel+SQL, 10 min behavioral. Score yourself, log gaps in the tracker, re-drill the ≤3 confidence items.

## How it's tested

**Interview questions you'll actually get:**
- Technical: "Walk me through the three statements and how they link." / "What's deferred tax?" / "FCFF vs FCFE?" / "How does ITC set-off work under GST?"
- Behavioral: "Tell me about a deadline you missed." / "A time you disagreed with a manager."

**Practical/assessment tests companies actually give:**

| Role | The real test |
|---|---|
| FP&A / analyst | Timed 30–45 min Excel: build variance/forecast from raw data, no internet |
| KPO / GCC ops | Online assessment: Excel + a SQL screen + Versant/English test |
| Equity research | "Model this company" case, 60–90 min, plus a stock pitch |
| Audit (Big 4) | Case study: risks in a scenario; sometimes a sampling/ratio exercise |
| Accounts / tax | "Post these entries" or a live Tally task; GST return walk-through |

Expect a **take-home** for some (build a model overnight) and a **live-share** for others (screen-share while you type). Practice both — narrating while typing is a separate skill.

## Common mistakes & how pros avoid them

| Mistake | Pro move |
|---|---|
| Only reading notes, never speaking answers | Rehearse **out loud**, timed, ideally recorded |
| Prepping generic questions for every role | Decode each JD into a prep map first |
| Mouse-hunting in Excel tests | Learn keyboard: `Alt+=` autosum, `F4` absolute ref, `Ctrl+Shift+↓` select |
| Rambling behavioral answers | STAR, 2 min max, end on a metric |
| Cramming the night before | Space mocks over 2–4 weeks (cadence below) |
| Bluffing when stuck | "I don't know — here's how I'd reason it out" |
| Ignoring the "any questions for us?" close | Prepare 3 sharp questions about the team/metrics |

## Learn-it roadmap & resources

**Time to interview-ready:** 3–4 weeks of ~1 hr/day if your fundamentals are solid; 6–8 weeks if you're also relearning Excel/SQL.

**Mock-test cadence (the backbone):**

| Week | Cadence |
|---|---|
| 1 | Build question bank; 2 self-mocks (technical only) |
| 2 | 3 mocks: add timed Excel/SQL; log gaps daily |
| 3 | 3 mocks with a peer/mentor as interviewer; full loop |
| 4 | 2 dress-rehearsal mocks; taper, review tracker only |

Rule: **one full timed mock every 2–3 days**, never fewer than two before a real interview. Re-drill only ≤3-confidence items — don't re-practice what you've mastered.

**Resources (free unless noted):**
- Technical: *Breaking Into Wall Street* / *Wall Street Prep* (paid) for modelling; *Corporate Finance Institute* free articles; ICAI study material for Ind AS/tax.
- Excel/SQL/Python: Microsoft Excel functions docs, Mode SQL tutorial (free), Kaggle Python micro-courses (free).
- Behavioral: Google "STAR method finance"; write your 8 stories in a doc.
- Practice sets: Glassdoor + AmbitionBox (India) for company-specific asked questions.
- Certifications that double as prep: **NISM** (research analyst), **CFA L1** (technical depth), **Microsoft Excel (MO-201)**.

## Quick-reference

**The 3 tracks:** Technical (concept in 90 sec) · Practical (timed, keyboard-only) · Behavioral (STAR, 2 min, end on a number).

**Excel test essentials:** `XLOOKUP`, `SUMIFS`, `IFERROR`, `EOMONTH`; keys `Alt+=`, `F4`, `Ctrl+Shift+Arrow`, `Ctrl+A` (save in Tally).

**SQL screen essentials:** `JOIN … ON`, `GROUP BY`, `HAVING`, `ORDER BY … DESC`, `LIMIT`.

**FCFF bridge:** `PAT + Int×(1−t) + Dep − Capex − ΔWC`.

**GST filing path:** `gst.gov.in → Returns Dashboard → GSTR-3B → fill 3.1 & 4 → Save → Pay → File`.

**Cadence:** 1 full timed mock every 2–3 days; ≥2 before any real interview; re-drill only confidence ≤3.

**When stuck:** "I don't know — here's how I'd find out," then reason aloud.
