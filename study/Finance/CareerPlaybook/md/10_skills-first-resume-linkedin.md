# Skills-first resume & LinkedIn

## What it is & where it's used

A **skills-first resume** flips the old script. Instead of leading with "Responsible for handling accounts payable," you lead with a demonstrable, measurable output built on a named tool: *"Automated a 400-line vendor reconciliation in Excel (XLOOKUP + Power Query), cutting month-end close from 3 days to 4 hours."* The verb is an action, the tool is explicit, and the result is a number.

This matters for **every** finance/accounts/tax role you'll target in India or abroad:

| Role | What recruiters scan for |
|---|---|
| Accounts Executive / R2R | Tally, GST returns, BRS, journal entries, Excel |
| FP&A / Financial Analyst | Excel modeling, variance analysis, Power BI, SQL |
| Audit / Assurance | SA/Ind AS references, sampling, working papers, CaseWare |
| Tax (Direct/Indirect) | GST portal, TDS, Form 26AS, ITR filing, reconciliations |
| Data-facing finance | SQL, Python (pandas), DAX, dashboarding |

The resume and LinkedIn profile are two front-ends to the **same skills database**. An ATS (Applicant Tracking System) and a human recruiter both do keyword matching first, judgement second. Your job is to pass the keyword pass, then survive the human read.

## The gap: why companies want this (and college didn't teach it)

An MBA teaches you *frameworks* (Porter, WACC theory, capital structure). CA Inter teaches you *standards* (Ind AS 115, SA 700, GST Sec 16). Neither produces the artifact an employer actually pays for: **a working file that saves someone time or catches an error.**

The gap is specific:

- College graded you on **answers**; the job grades you on **repeatable process** (a model someone else can open and trust).
- Your CV likely lists **courses and marks**; a recruiter can't hire a mark — they hire a person who can build a cost sheet in TallyPrime and file a GSTR-3B without supervision.
- ATS software rejects ~60-70% of resumes before a human sees them, almost always for **missing keywords** — the exact tool names and standard references you assumed were "obvious."

Closing this gap costs nothing but rewriting. You already *did* the Excel model in a group project — you just described it as "prepared financial analysis" instead of "built a 3-statement model with a circular-reference interest toggle."

## What "proficient" looks like

A job-ready skills-first profile clears this bar **unaided**:

1. Every bullet has the shape **[Action verb] + [tool/skill] + [quantified result]**. No result-free bullets.
2. The **top third** of page one (the "above the fold" zone recruiters read in 6 seconds) contains a Skills/Tools summary and 2-3 headline achievements — not your address and objective statement.
3. The exact tool nouns appear verbatim: `TallyPrime`, `GSTR-1`, `Excel (XLOOKUP, SUMIFS, Power Query)`, `SQL`, `Power BI (DAX)`, `Ind AS`, `TDS`, `26AS`, `BRS`.
4. LinkedIn headline is a **positioning statement**, not a job title: *"Accounts & GST | Tally + Advanced Excel | CA Inter | Automating month-end close"*.
5. One line is verifiable: a GitHub link, a public dashboard, a Google Sheet, or a specific number a reference could confirm.

## Hands-on: how to actually do it

### Rewrite a weak bullet — the mechanics

Take a bullet and pass it through three filters: **Tool named? Number attached? Verb strong?**

| Weak (college voice) | Strong (skills-first) |
|---|---|
| Handled monthly reconciliation | Reconciled 12 bank accounts monthly in Excel using SUMIFS + conditional flags, surfacing ₹2.1L of duplicate vendor payments |
| Assisted in GST filing | Filed GSTR-1 and GSTR-3B for a 40-invoice/month firm; matched ITC against GSTR-2B, reducing mismatches to zero |
| Made financial models | Built a 3-statement model in Excel with a debt-schedule circularity toggle; used it to test 3 capex scenarios |
| Worked on data analysis | Wrote SQL to pull 18 months of sales and built a Power BI dashboard tracking 6 KPIs, refreshed weekly |

### Prove the Excel claim (so it's not a bluff)

The bullet says XLOOKUP + SUMIFS. Be ready to show the actual formulas:

```excel
=XLOOKUP(A2, Vendors[VendorID], Vendors[GSTIN], "NOT FOUND")
=SUMIFS(Ledger[Amount], Ledger[Party], A2, Ledger[Month], "Mar-26")
=IFERROR(XLOOKUP(...), "Check master")     'never leave #N/A in a client file
```

### Prove the SQL claim

```sql
SELECT vendor_id,
       COUNT(*)          AS invoices,
       SUM(taxable_val)  AS taxable,
       SUM(igst+cgst+sgst) AS total_tax
FROM   purchases
WHERE  invoice_date BETWEEN '2025-04-01' AND '2026-03-31'
GROUP  BY vendor_id
HAVING SUM(taxable_val) > 500000
ORDER  BY total_tax DESC;
```

### Prove the Python claim

```python
import pandas as pd
gstr2b = pd.read_excel("GSTR2B.xlsx")
books  = pd.read_excel("PurchaseRegister.xlsx")
recon = books.merge(gstr2b, on="invoice_no", how="outer",
                    indicator=True, suffixes=("_books","_2b"))
mismatch = recon[recon["_merge"] != "both"]     # ITC not matching
mismatch.to_excel("ITC_mismatch.xlsx", index=False)
```

### Prove the DAX claim (Power BI)

```dax
Total Tax = SUM(Purchases[TotalTax])
ITC Matched % =
DIVIDE(
    CALCULATE([Total Tax], Purchases[MatchStatus] = "Matched"),
    [Total Tax], 0)
```

### The ATS keyword pass

Copy the job description into a doc. Highlight every noun that is a tool, standard, or task (`Tally`, `Ind AS 116`, `variance analysis`, `TDS`, `SQL`). If your resume doesn't contain that exact string, and you can honestly claim it, add it. ATS does literal matching — "MS Excel" and "Excel" are fine, but "spreadsheets" won't match a search for "Excel."

## Worked example / mini-project

**Goal:** turn one real thing you did into a portfolio bullet + LinkedIn line + interview story.

You built a GST input-tax-credit reconciliation for a friend's trading firm. Realistic numbers:

| Metric | Value |
|---|---|
| Purchase invoices / month | 320 |
| ITC as per books | ₹4,80,000 |
| ITC as per GSTR-2B | ₹4,52,000 |
| Mismatch found | ₹28,000 (11 invoices) |
| Time before automation | ~6 hours manual |
| Time after (Power Query) | 25 minutes |

**The journal entry you'd pass** for the ₹28,000 blocked/deferred ITC:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| ITC Receivable – Under Reconciliation A/c | 28,000 | |
| Input CGST A/c | | 14,000 |
| Input SGST A/c | | 14,000 |

**Resume bullet:**
> Built a Power Query + Python ITC reconciliation matching a 320-invoice/month purchase register against GSTR-2B; identified ₹28,000 of unmatched credit and cut the monthly recon from 6 hours to 25 minutes.

**LinkedIn "Featured" post (2 lines):**
> Automated a GST ITC reconciliation this week — Power Query pulls the register, Python matches it to GSTR-2B, mismatches export in one click. 6 hours → 25 minutes. Steps + sample file in comments. #GST #Excel #Finance

**Interview story (STAR):** *Situation:* manual recon, credit leaking. *Task:* find the gap fast. *Action:* built the merge (showed the `indicator=True` pandas code above). *Result:* ₹28k recovered, 93% time saved, now runs monthly.

That single project feeds three assets. Do this for 3-4 projects and your profile is done.

## How it's tested

Employers rarely take the resume at face value. Expect:

- **Timed Excel test (30-45 min):** given a raw dataset, "build a summary with SUMIFS/XLOOKUP, add a pivot, flag duplicates, and 3 charts." Speed and keyboard shortcuts are watched.
- **"Close these books" case:** a trial balance with 8-10 pending adjustments (depreciation, prepaid, accruals, a wrong GST posting). You pass entries and produce a P&L + Balance Sheet.
- **SQL screen:** 2-3 queries — a `GROUP BY` aggregate, a `JOIN`, and a `HAVING` filter. Very common for FP&A/analyst roles.
- **GST/tax practical:** "Here are 20 invoices — compute output tax, ITC, and net GST payable; which ITC is blocked under Sec 17(5)?"
- **Resume defense questions:** *"Walk me through the XLOOKUP you used"*, *"Why XLOOKUP over VLOOKUP?"* (answer: works left-to-right agnostic, returns arrays, native `if_not_found`). If you can't defend a bullet, **delete it.**

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Objective statement ("seeking a challenging role…") | Delete it. Replace with a 2-line skills summary. |
| Result-free bullets ("handled," "assisted," "worked on") | Every bullet gets a number or a named output. |
| Listing "MS Office" as a skill | Name the *functions*: XLOOKUP, SUMIFS, Power Query, pivot tables. |
| Skills you can't demo | If you can't pass a 10-min test on it, don't list it. |
| Photo-heavy, multi-column resume that ATS can't parse | Single column, standard headings, `.docx` or text-based PDF. |
| Same resume for every job | Re-order skills to mirror each job description's keywords. |
| LinkedIn headline = "Student at XYZ" | Make it a positioning line with tools + target role. |
| Empty LinkedIn "Featured" and "Projects" | Pin 2-3 project artifacts; recruiters click these. |

Pros also keep a **master resume** (everything) and cut a **tailored 1-pager** per application in 10 minutes.

## Learn-it roadmap & resources

**Time to a job-ready profile: 2-3 weekends** (the skills you're describing you should already have; this is packaging).

| Week | Do this |
|---|---|
| 1 | List 4 real projects. Write each as Action+Tool+Number. Pass every bullet through the 3 filters. |
| 1 | Rebuild resume as single-column `.docx`; add a "Tools" line. Run it through Jobscan/free ATS checker. |
| 2 | Rewrite LinkedIn: headline, About (3 short paras), Skills section (pin top 3), one Featured project post. |
| 2 | Ask 2 people for a specific-skill recommendation; endorse to seed reciprocity. |

**Resources (mostly free):**
- Harvard/most-college resume guides (PDF) — for the single-column skeleton.
- Jobscan / Resume Worded — free ATS keyword match score.
- LinkedIn's own "Skills" and SSI (Social Selling Index) page.
- Excel: ExcelJet (formula reference), Chandoo (India-context).
- SQL: SQLBolt, Mode SQL Tutorial (free, browser-based).
- Certifications that read well on a finance CV: **Microsoft Excel Expert (MO-201)**, **Google Data Analytics (Coursera)**, **Microsoft PL-300 (Power BI)**, plus your **CA Inter** progress stated plainly.

## Quick-reference

**Bullet formula:** `[Strong verb] + [named tool] + [quantified result]`

**Strong verbs:** Built, Automated, Reconciled, Modeled, Reduced, Filed, Analyzed, Forecasted, Audited, Streamlined.

**Must-name tool keywords (India finance):**
```
TallyPrime · Excel (XLOOKUP, SUMIFS, Power Query, pivots) · SQL ·
Power BI (DAX) · Python (pandas) · GSTR-1 · GSTR-3B · GSTR-2B ·
TDS · Form 26AS · BRS · Ind AS · SA 700 · variance analysis
```

**Resume structure (top → bottom):** Name + contact → 2-line summary → Tools/Skills line → Achievements/Projects → Experience → Education (CA Inter, MBA) → Certifications.

**LinkedIn headline template:**
`[Function] | [Tool 1] + [Tool 2] | [Credential] | [1-line value]`
e.g. `Accounts & Tax | TallyPrime + Advanced Excel | CA Inter | Cutting month-end close times`

**6-second test:** cover everything below the top third of page one — can a stranger tell what you do and prove it? If not, fix the top third first.
