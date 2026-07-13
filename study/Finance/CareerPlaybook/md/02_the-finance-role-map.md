# The Finance Role Map

## What it is & where it's used

"Finance" on a job portal is a dozen different jobs wearing one label. A tax analyst and an M&A banker share almost no daily tools. Before you can build skills (the rest of this book), you need a map: who does what, what it pays, and how you get in. This chapter is that map.

The core split is **buy-side vs sell-side vs corporate vs assurance**:

- **Corporate finance** (inside a company): Accounting, Tax, FP&A, Treasury, Product Control. You keep the company's own books, forecasts, and cash.
- **Sell-side** (advises/intermediates): Investment Banking (IB), Equity Research (ER). You sell deals, advice, and coverage.
- **Buy-side** (invests capital): PE/VC, asset management, hedge funds. You deploy money to earn returns.
- **Assurance & control**: External Audit, Internal Audit, Credit, Risk. You verify, lend against, and constrain.

Every role below hires in India (Mumbai, Bengaluru, Gurugram, Hyderabad GCCs) and globally. Your MBA + CA-Inter combination is a strong fit for Accounting, Tax, FP&A, Credit, Audit, and Product Control immediately, and a stepping stone into IB/ER.

## The gap: why companies want this (and college didn't teach it)

College teaches you to *describe* a balance sheet. Employers pay you to *build, defend, and act on one under a deadline*. The specific gaps:

| College taught | Job actually needs |
|---|---|
| Ratio definitions | A working 3-statement model that ties out |
| "Depreciation reduces profit" | The actual Dr/Cr entry in Tally, GST implications |
| Portfolio theory | Pulling 2M transaction rows in SQL and reconciling |
| "Tax is 30%" | Filing GSTR-3B, computing MAT, TDS mismatch in 26AS |
| One right answer | Judgement under ambiguity, defended in an interview |

The role map closes the *orientation* gap: MBAs routinely apply to the wrong role, quote the wrong pay band, and fail interviews because they can't name what the desk does hour-to-hour. Knowing the map is itself a screening filter recruiters use.

## What "proficient" looks like

A job-ready candidate can, unaided:

1. **Name any role's core deliverable** — "ER analysts publish an initiation report with a target price and a DCF; FP&A owns the monthly variance deck."
2. **Quote a realistic pay band** for their city and level (not a glassdoor fantasy).
3. **Map their own skills to 2-3 target roles** and articulate the entry path.
4. **Pass the role-specific technical screen** — a modelling test for IB, a books-close case for accounting, a SQL screen for product control.

The bar is *specificity*. "I like markets" fails. "I want equity research covering Indian banks because I can already read an RBI-reported NIM and build a provisioning model" passes.

## Hands-on: how to actually do it

Below is each major role with its core deliverable, entry path, and a concrete artifact you'd produce.

**Accounting** — records transactions, closes books, files financials.
```
' Example journal: sale of ₹1,00,000 goods + 18% GST
Dr Debtors (Trade Receivables)      1,18,000
   Cr Sales                                  1,00,000
   Cr Output CGST                                9,000
   Cr Output SGST                                9,000
```
Entry path: B.Com/CA-Inter → Accounts Executive → Assistant Manager.

**Tax** — direct (income tax, TDS, MAT) + indirect (GST). Deliverable: filed GSTR-3B/1, Form 26AS reconciliation.
```
-- reconcile GST purchase register to GSTR-2B
SELECT p.gstin, SUM(p.itc) AS book_itc, SUM(b.itc) AS portal_itc,
       SUM(p.itc) - SUM(b.itc) AS mismatch
FROM purchase_register p
LEFT JOIN gstr2b b ON p.invoice_no = b.invoice_no
GROUP BY p.gstin
HAVING ABS(SUM(p.itc) - SUM(b.itc)) > 1;
```

**FP&A** (Financial Planning & Analysis) — budgets, forecasts, variance. Deliverable: monthly board deck.
```excel
=XLOOKUP(A2, Actuals[Cost Centre], Actuals[Amount]) - Budget[Amount]   ' variance
=(ThisMonth-LastMonth)/LastMonth                                        ' MoM %
```
DAX for a rolling forecast:
```dax
Rolling3M Rev = 
CALCULATE( SUM(Sales[Revenue]),
    DATESINPERIOD(Calendar[Date], MAX(Calendar[Date]), -3, MONTH) )
```

**Treasury** — cash, FX, debt, liquidity. Deliverable: daily cash position, hedge book.
```python
# simple FX exposure netting
import pandas as pd
exp = pd.DataFrame({'ccy':['USD','USD','EUR'],'amt':[500000,-200000,300000]})
net = exp.groupby('ccy')['amt'].sum()   # net position to hedge
```

**Investment Banking (IB)** — raises capital, advises M&A. Deliverable: pitch deck, DCF, LBO model.
```excel
=NPV(WACC, FCF_range) + TerminalValue/(1+WACC)^n    ' enterprise value
```

**Equity Research (ER)** — covers listed stocks, issues target prices. Deliverable: initiation note.

**Credit** — assesses borrower repayment ability. Deliverable: credit appraisal memo, rating.
```excel
=EBITDA/Interest            ' interest coverage
=(Total Debt)/EBITDA        ' leverage — banks cap ~3.0-3.5x
```

**Risk** — market/credit/operational risk limits. Deliverable: VaR report, limit monitoring.
```python
import numpy as np
returns = np.random.normal(0, 0.02, 1000)
VaR_95 = np.percentile(returns, 5)   # 1-day 95% Value at Risk
```

**Audit** — external (statutory) or internal. Deliverable: audit opinion / control findings.

**PE/VC** — buys companies (PE) or funds startups (VC). Deliverable: investment committee memo, LBO/cap-table.

**Product Control** (bank markets desk) — validates trader P&L daily. Deliverable: signed-off daily P&L, P&L explain.
```sql
SELECT desk, trade_date,
       SUM(mtm_today) - SUM(mtm_yesterday) AS daily_pnl
FROM positions GROUP BY desk, trade_date;
```

## Worked example / mini-project

**Build your own role-fit scorecard.** Reproduce this in Excel with your real numbers.

| Role | Core deliverable | Entry path (India) | Fit for you (1-5) | Notes |
|---|---|---|---|---|
| Accounting | Books close, financials | CA/B.Com → Accts Exec | 5 | CA-Inter direct fit |
| Tax | GSTR/ITR filed | CA/CA-Inter → Tax Assoc | 5 | Strong |
| FP&A | Variance deck | MBA → FP&A Analyst | 5 | MBA + Excel |
| Treasury | Cash/FX position | MBA/CA → Treasury Analyst | 4 | Learn FX |
| Credit | Appraisal memo | MBA → Credit Analyst | 4 | Bank/NBFC |
| IB | DCF, pitch | Top MBA/CA → Analyst | 3 | Pedigree-gated |
| ER | Initiation note | CFA/MBA → Associate | 3 | Add CFA |
| Product Control | Daily P&L sign-off | CA/MBA → Analyst | 4 | GCC hiring |

Then compute a weighted score:
```excel
=SUMPRODUCT(Fit_range, Weight_range)/SUM(Weight_range)
```
Weight by your priorities (pay 40%, growth 30%, fit 30%). The top 2-3 rows become your application targets. This forces the *specificity* recruiters screen for.

**Pay bands** (approximate, 2026; India in ₹ LPA total; Global in USD base + bonus). GCC = Global Capability Centre in India.

| Role | India entry (₹ LPA) | India 5-8 yr (₹ LPA) | Global entry (USD) |
|---|---|---|---|
| Accounting | 4-7 | 12-20 | 55-75k |
| Tax | 5-8 | 15-25 | 60-85k |
| FP&A | 7-12 | 20-40 | 70-95k |
| Treasury | 7-12 | 20-38 | 70-100k |
| Credit | 6-11 | 18-35 | 65-90k |
| Risk | 8-14 | 22-45 | 75-110k |
| Audit (Big 4) | 8-12 | 20-40 | 60-85k |
| Product Control | 9-15 | 25-50 | 75-110k |
| Equity Research | 10-18 | 30-70 | 90-140k |
| IB | 15-30 | 50-1.2cr | 110-175k + |
| PE/VC | 18-35 | 60-1.5cr+ | 130-200k + |

Note: IB/PE bonuses can equal or exceed base; back-office/control roles have tighter, steadier bands.

## How it's tested

| Role | Interview questions | Practical test |
|---|---|---|
| Accounting | "Pass the entry for a prepaid expense." "What's a deferred tax asset?" | Timed: close a trial balance, spot 3 errors |
| Tax | "Explain reverse charge under GST." "MAT credit mechanism?" | File a mock GSTR-3B; reconcile 26AS |
| FP&A | "Walk me through your budget vs actual process." | Timed Excel: build a variance bridge, a rolling forecast |
| Treasury | "How do you hedge a USD payable?" | Cash-flow forecast case |
| Credit | "Rank these ratios for a lending decision." | Spread a borrower's financials, write a 1-page memo |
| IB | "Walk me through a DCF." "Why does depreciation flow through 3 statements?" | 3-hour LBO/3-statement modelling test |
| ER | "Pitch me a stock." | Build a model + short thesis on a given company |
| Product Control | "What's P&L explain?" "T+1 vs T+0?" | SQL screen + a P&L reconciliation case |

The single most common practical test across corporate finance is a **timed Excel test** (no internet, 30-90 min). The IB/ER world tests **full modelling from a blank sheet**. Control/product roles increasingly add a **SQL screen**.

## Common mistakes & how pros avoid them

- **Applying to "finance" generically.** Pros apply to a *named desk* with a matching artifact in hand (a model, a filed return).
- **Quoting Western pay in India (or vice versa).** Know your city's band; overshoot by 2x and you're filtered out, undershoot and you're underpaid for years.
- **Confusing prestige with fit.** IB pays most but is pedigree- and hours-gated. A CA-Inter holder often has a faster, richer path via Audit → Product Control → FP&A than a doomed IB cold-apply.
- **Ignoring the GCC boom.** Bengaluru/Hyderabad/Gurugram GCCs now run real product control, FP&A, and risk for global banks — global-quality work, India base. Underrated entry point.
- **No numbers in interviews.** "I improved reporting" loses. "I cut close from 8 to 5 days by automating a 12-tab reconciliation" wins.
- **Treating audit as a dead end.** Big 4 audit is the single most reliable launchpad in India — it opens Product Control, FP&A, Risk, and internal audit at 2-3x pay within 5 years.

## Learn-it roadmap & resources

**Time to role-clarity: 1 week. Time to first role: 3-12 months** depending on the technical gap.

| Phase | Time | Do this |
|---|---|---|
| Map | Week 1 | Build the role-fit scorecard above; pick 2-3 targets |
| Skill | Months 1-3 | Learn the target's core tool (Excel modelling / SQL / Tally+GST) — later chapters |
| Proof | Months 2-4 | Build 1 portfolio artifact per target role |
| Apply | Months 3-6 | Apply to named desks; use referrals (LinkedIn alumni) |

Resources:
- **Free**: Corporate Finance Institute intro courses; Aswath Damodaran's valuation lectures (YouTube, free); Mergers & Inquisitions (IB career site); ICAI study material (tax/audit).
- **Paid**: WallStreetPrep / Breaking Into Wall Street (IB modelling); CFA (ER/buy-side signal); FRM (risk); CA final (audit/tax — you're already on this).
- **Certifications by role**: CA → Audit/Tax/Accounting; CFA → ER/PE/AM; FRM → Risk; NISM → distribution/compliance; MBA → FP&A/Credit/general.

## Quick-reference

| Role | One-line | Top cert | India entry ₹LPA |
|---|---|---|---|
| Accounting | Keeps the books | CA | 4-7 |
| Tax | Files & optimizes tax | CA | 5-8 |
| FP&A | Budgets & forecasts | MBA/CFA | 7-12 |
| Treasury | Manages cash & FX | MBA/CA | 7-12 |
| Credit | Assesses borrowers | MBA/CFA | 6-11 |
| Risk | Sets & monitors limits | FRM | 8-14 |
| Audit | Verifies statements | CA | 8-12 |
| Product Control | Signs off daily P&L | CA | 9-15 |
| ER | Covers stocks, target price | CFA | 10-18 |
| IB | Raises capital, M&A | MBA/CA | 15-30 |
| PE/VC | Invests capital | CFA/MBA | 18-35 |

**Rules of thumb**: Buy-side pays > sell-side > corporate > assurance, but volatility and hours scale the same way. Big 4 Audit is India's best launchpad. GCCs give global work at India base. Always apply to a *named desk* with a matching *artifact*.
