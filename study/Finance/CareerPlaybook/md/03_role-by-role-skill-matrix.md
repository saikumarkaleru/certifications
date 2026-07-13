# Role-by-Role Skill & Tool Matrix

## What it is & where it's used

Every finance job posting is a *disguised skill list*. "Financial Analyst," "Accounts Executive," "Tax Associate" — the titles are vague, but the actual work is a fixed bundle of hard skills and named tools. This chapter is the decoder ring: for each common India-based finance/accounts/tax role, it names the **exact** hard skills, the **specific** tools (with version/module), and the **certifications** that move a resume from the reject pile to the shortlist.

Use this to *target*. Instead of "I'll learn finance," you decide: "I want to be an FP&A Analyst, so I need Excel modelling + Power BI + SQL, and I can skip TallyPrime and GST filing." A CA Inter + MBA candidate can credibly aim at six lanes — R2R accounting, Tax/GST, Audit, FP&A/Analyst, Treasury, and Analytics-leaning Finance — and each rewards a different tool stack.

## The gap: why companies want this (and college didn't teach it)

MBA and CA syllabi teach *concepts* (NPV, deferred tax, variance analysis) but not the *tool that executes the concept on Monday morning*. College never made you:

- Build a 3-statement model that ties (BS balances, CF reconciles) under a 45-minute clock.
- File a GSTR-3B on the actual portal or pass a reverse-charge journal in TallyPrime.
- Write `SELECT ... GROUP BY` to pull a revenue cut from a 2-million-row ledger export.
- Reconcile GSTR-2B to the purchase register when 40 invoices mismatch.

Employers pay for *execution under constraint*, not for knowing the definition. The gap this chapter closes: mapping each concept you already know to the **named artifact** an employer will hand you and say "do this."

## What "proficient" looks like

The concrete bar, by role — what a job-ready person does **unaided**:

| Role | Proficiency bar (does this without help) |
|---|---|
| Accounts Executive (R2R) | Passes month-end journals (accruals, prepaid, depreciation), reconciles bank & vendor ledgers, closes books in TallyPrime/SAP, produces trial balance |
| Tax/GST Associate | Files GSTR-1, 3B, does 2B reconciliation, computes TDS & advance tax, handles ITC eligibility calls |
| FP&A / Financial Analyst | Builds/updates 3-statement model, variance (budget vs actual) decks, forecasts, sensitivity tables; Power BI dashboard |
| Audit Associate | Vouching/verification, sampling, ratio analytics, drafts working papers, tests internal controls |
| Treasury/Banking Analyst | Cash-flow forecasting, working-capital metrics, forex/interest exposure, covenant tracking |
| Finance Data Analyst | SQL pulls, Python/pandas cleaning, DAX measures, automates a recurring MIS |

## Hands-on: how to actually do it

**The universal skill matrix** — the spine of the chapter. "★" = must-have, "○" = edge:

| Skill / Tool | R2R Acct | Tax/GST | FP&A | Audit | Treasury | Data Analyst |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| Excel (advanced: XLOOKUP, INDEX/MATCH, pivots) | ★ | ★ | ★ | ★ | ★ | ★ |
| Financial modelling (3-statement, DCF) | ○ | | ★ | ○ | ★ | ○ |
| TallyPrime | ★ | ★ | | ○ | ○ | |
| SAP FICO / Oracle / Zoho Books | ★ | ○ | ○ | ○ | ○ | |
| GST portal + Income-tax portal | ○ | ★ | | ○ | | |
| SQL | ○ | | ★ | ○ | ○ | ★ |
| Power BI / Tableau (DAX) | ○ | | ★ | ○ | ○ | ★ |
| Python (pandas) | | | ○ | ○ | | ★ |
| Ind AS / IFRS knowledge | ★ | ○ | ★ | ★ | ○ | |
| **Certification signal** | CA / CMA | CA + GST cert | CFA / FMVA | CA / ACCA | CFA / Treasury (ACT) | Any + BI cert |

**Excel — the formulas every role is tested on:**

```
=XLOOKUP(A2, Ledger[VendorCode], Ledger[Balance], "Not found")
=SUMIFS(Amount, Date, ">="&DATE(2026,4,1), Date, "<="&DATE(2026,6,30), GL, "5*")
=INDEX(Data, MATCH(1,(Data[Acct]=H2)*(Data[Period]=I2),0),3)   ' Ctrl+Shift+Enter (legacy)
=IFERROR(Sales/LAGyear-1, "n/a")                                ' growth %
```

**SQL — a revenue cut an analyst writes daily:**

```sql
SELECT  region,
        DATE_TRUNC('month', invoice_date) AS mth,
        SUM(taxable_value)                AS net_rev,
        SUM(taxable_value * 0.18)         AS gst_est
FROM    sales_invoices
WHERE   invoice_date >= '2026-04-01'
  AND   status = 'POSTED'
GROUP BY region, DATE_TRUNC('month', invoice_date)
HAVING  SUM(taxable_value) > 100000
ORDER BY net_rev DESC;
```

**Python — GSTR-2B vs purchase-register reconciliation (the classic tax test):**

```python
import pandas as pd
books = pd.read_excel("purchase_register.xlsx")
gstr2b = pd.read_excel("gstr2b.xlsx")
recon = books.merge(gstr2b, on="invoice_no", how="outer",
                    suffixes=("_books", "_2b"), indicator=True)
recon["itc_diff"] = recon["igst_books"].fillna(0) - recon["igst_2b"].fillna(0)
mismatch = recon[(recon["_merge"] != "both") | (recon["itc_diff"].abs() > 1)]
mismatch.to_excel("itc_mismatch.xlsx", index=False)
```

**DAX — Power BI measures an FP&A dashboard needs:**

```
Net Revenue = SUM(Sales[TaxableValue])
YoY % = DIVIDE([Net Revenue] - CALCULATE([Net Revenue], SAMEPERIODLASTYEAR('Date'[Date])),
              CALCULATE([Net Revenue], SAMEPERIODLASTYEAR('Date'[Date])))
Budget Variance = [Net Revenue] - [Budget]
```

**TallyPrime click-path (month-end accrual):**
Gateway of Tally → Vouchers → F7 (Journal) → Dr *Rent Expense* ₹50,000 → Cr *Rent Payable* ₹50,000 → narration → Ctrl+A to save.

**GST portal path (file GSTR-3B):** gst.gov.in → Login → Returns Dashboard → select period → GSTR-3B "Prepare Online" → fill 3.1 (outward), 4 (ITC from 2B) → Save → Proceed to Pay → Offset liability → File with DSC/EVC.

## Worked example / mini-project

**Target role: FP&A Analyst. Deliverable: a Q1 FY27 budget-vs-actual pack.** Reproduce with these numbers:

| Line (₹ lakh) | Budget | Actual | Variance | Var % |
|---|--:|--:|--:|--:|
| Revenue | 1,200 | 1,140 | (60) | -5.0% |
| COGS | 720 | 700 | 20 | +2.8% (fav) |
| Gross Profit | 480 | 440 | (40) | -8.3% |
| Employee cost | 180 | 195 | (15) | -8.3% |
| Other opex | 120 | 118 | 2 | +1.7% |
| **EBITDA** | **180** | **127** | **(53)** | **-29.4%** |

Steps: (1) Import both columns into Excel, `Variance = Actual − Budget`, `Var% = Variance/Budget`. (2) Flag any line where `ABS(Var%) > 10%` with `=IF(ABS(E2)>0.1,"⚠ Investigate","")`. (3) Root-cause: EBITDA missed by ₹53L driven by a ₹60L revenue shortfall + ₹15L staff overrun. (4) Load into Power BI, add the `YoY %` and `Budget Variance` DAX measures above, build a waterfall visual. (5) One-slide narrative: "Revenue miss (volume, not price) is the EBITDA driver; hiring ran ahead of plan." That five-step artifact is *exactly* what an FP&A screen asks you to produce.

## How it's tested

| Role | Interview questions | Practical / assessment test |
|---|---|---|
| R2R Acct | "Journal for prepaid insurance?" "Bank reco steps?" | Timed: close a mini trial balance in Tally / pass 10 adjusting entries |
| Tax/GST | "ITC blocked u/s 17(5)?" "RCM on which services?" | Reconcile a GSTR-2B vs register file; compute a 3B liability |
| FP&A | "Walk me through linking the 3 statements." "How does ₹100 depreciation flow?" | 45-min timed model build; budget-variance case |
| Audit | "Assertions you test for revenue?" "Sampling method?" | Vouch a sample set; spot the misstatement in given ledgers |
| Data Analyst | "Difference between WHERE and HAVING?" | Live SQL screen (HackerRank); build a dashboard from a CSV |

The "₹100 depreciation" question is the FP&A gatekeeper: *Income statement −100 → net income −100×(1−tax); Cash flow add back +100; Balance sheet PP&E −100, cash +tax shield, retained earnings −net income — and it must balance.* Know it cold.

## Common mistakes & how pros avoid them

- **Hardcoding numbers inside formulas.** Pros keep all assumptions in a separate blue-font input cell; formulas reference cells only.
- **A model that doesn't tie.** Amateurs "plug" the balance sheet. Pros build a `Balance check = Assets − (Liab + Equity)` row that must read 0; if not, the CF is wrong.
- **Confusing ITC eligibility.** Blocked credits (u/s 17(5): motor vehicles, personal-use, works contract) get claimed by mistake. Pros reconcile to 2B first, never to the invoice alone.
- **SQL without `GROUP BY` discipline** — selecting non-aggregated columns; pros put every non-aggregate in `GROUP BY`.
- **Listing tools you can't demo.** Never write "SAP" if you can only spell it. Interviewers ask module-level questions (FICO vs MM).
- **Ignoring Ind AS in accounting roles** — e.g., recognising revenue on invoice date instead of per Ind AS 115 performance obligation.

## Learn-it roadmap & resources

| Skill | Time to job-ready | Resource (free → paid) |
|---|---|---|
| Advanced Excel | 3–4 weeks | ExcelJet cheat-sheet (free) → Chandoo; Microsoft Learn |
| Financial modelling | 6–8 weeks | Aswath Damodaran (free, NYU) → CFI **FMVA** (paid) |
| TallyPrime | 2–3 weeks | Tally Education free videos → Tally certification |
| GST/tax practice | 4 weeks | GSTN free tutorials + ICAI GST module; use the portal sandbox |
| SQL | 3–4 weeks | SQLBolt / Mode SQL tutorial (free) → HackerRank SQL badge |
| Power BI (DAX) | 3–4 weeks | Microsoft Learn (free) → PL-300 certification |
| Python/pandas | 6 weeks | Kaggle "pandas" (free) → DataCamp |

Certifications that actually signal, by lane: **CA / CMA** (accounting-tax), **CFA / FMVA** (analyst-FP&A), **ACCA** (global audit), **PL-300** (BI), **ACT** (treasury). Your CA Inter + MBA already covers the accounting-concept base — spend money only on the *tool* certs (FMVA, PL-300) that your degrees don't prove.

## Quick-reference

```
Excel:  =XLOOKUP(lookup, arr, return, "NA")  |  =SUMIFS(sum, crit_rng, crit)
        Balance check row must = 0
SQL:    SELECT col, AGG(x) FROM t WHERE ... GROUP BY col HAVING AGG(x)>n
DAX:    YoY% = DIVIDE([M]-CALCULATE([M],SAMEPERIODLASTYEAR(Date[Date])), prior)
Tally:  F7 journal | F5 payment | Alt+G quick-nav | Ctrl+A save
GST:    3B = 3.1 outward + 4 ITC → offset → file (DSC/EVC); reconcile 2B first
Depn ₹100 flow: IS -100→NI -100(1-t); CF +100; BS PP&E-100, cash+shield, RE-NI
Cert by lane: R2R→CA/CMA | FP&A→CFA/FMVA | Audit→ACCA | BI→PL-300 | Treasury→ACT
```

**Targeting rule:** pick ONE column of the matrix, master its ★ rows, get its one tool-cert, and build one reproducible artifact (a model, a reco, a dashboard). That column — not "finance" in general — is what you apply for.
