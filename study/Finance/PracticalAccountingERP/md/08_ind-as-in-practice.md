# Ind AS in practice

## What it is & where it's used

Ind AS (Indian Accounting Standards) are India's IFRS-converged standards. They are **mandatory** for listed companies and large unlisted companies (net worth ≥ ₹250 crore), plus their holding/subsidiary/associate/JV entities. Everyone else runs on the older **AS** (Accounting Standards) or the simpler Ind AS-lite. So the first job skill is knowing *which* framework the entity is on.

Four standards do 80% of the real work on the job:

| Standard | Topic | Where it bites |
|---|---|---|
| **Ind AS 115** | Revenue from contracts with customers | Every sale, every SaaS subscription, every construction/AMC contract |
| **Ind AS 116** | Leases | Office rent, vehicles, equipment, plant land |
| **Ind AS 109** | Financial instruments | Receivables (ECL provisioning), investments, borrowings, derivatives |
| **Ind AS 16** | Property, plant & equipment | Capitalisation, componentisation, depreciation |

Roles that need this: **financial reporting / R2R analysts**, statutory-audit associates (CA articles/qualified), controllers, FP&A when building models off Ind AS numbers, and anyone preparing or auditing consolidated financials.

## The gap: why companies want this (and college didn't teach it)

MBA and even CA-Inter teaches *what* the standard says. The job is *applying* it to a messy contract nobody wrote with accounting in mind. College hands you "recognise revenue at fair value"; the employer hands you a ₹1.8 crore master service agreement with a discount, a free 3-month support add-on, and milestone billing, and asks: *how much revenue this quarter, and pass the entries.*

The specific gaps employers pay to close:
- **Unbundling contracts** into performance obligations and allocating price — pure judgement, no textbook number.
- **Building the Ind AS 116 ROU asset + lease liability amortisation schedule** in Excel from a rent agreement. This is a near-universal interview test.
- **ECL (Expected Credit Loss) provision matrices** under Ind AS 109 — replacing the old "provide when overdue 180 days" rule with a forward-looking model.
- Knowing the **AS → Ind AS journal differences** because most Indian firms carry both a tax book (AS/ICDS) and a reporting book (Ind AS).

## What "proficient" looks like

A job-ready person can, **unaided**:

1. Read a contract and split it into performance obligations, allocate the transaction price, and state the recognition pattern (point-in-time vs over-time).
2. Build a lease amortisation schedule in Excel that ties: opening liability × rate = interest, less payment = closing; and ROU depreciated straight-line.
3. Build an ECL provision matrix by ageing bucket and compute the loss allowance.
4. Pass the full set of Dr/Cr entries for each, including deferred tax where the book/tax base differs.
5. Explain *why* — e.g. why a security deposit gets discounted, why a lease liability uses the incremental borrowing rate.

## Hands-on: how to actually do it

### Ind AS 115 — the 5-step model

1. Identify the contract → 2. Identify performance obligations (POs) → 3. Determine transaction price → 4. Allocate price to POs (by standalone selling price, SSP) → 5. Recognise revenue as each PO is satisfied.

**Allocation in Excel** — software licence ₹10,00,000 + 1-yr support billed together for ₹11,00,000; SSPs are ₹10,00,000 and ₹2,00,000.

```
Total SSP           =10,00,000+2,00,000            → 12,00,000
Licence allocated   =1100000*(1000000/1200000)     → 9,16,667  (point-in-time)
Support allocated   =1100000*(200000/1200000)      → 1,83,333  (over 12 months)
Monthly support rev =183333/12                      → 15,278
```

Journal at contract start (support unearned):

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Bank / Trade receivable | 11,00,000 | |
| To Revenue – Licence | | 9,16,667 |
| To Contract liability (deferred support) | | 1,83,333 |

Each month: Dr Contract liability 15,278 / Cr Revenue – Support 15,278.

### Ind AS 116 — lease liability + ROU (lessee)

Lease liability = **PV of future lease payments** at the incremental borrowing rate (IBR).

```excel
=PV(rate_per_period, n_periods, -payment, 0, type)
=-PV(0.10, 5, 300000, 0, 0)          'annual ₹3,00,000 rent, 5 yrs, 10% IBR, arrears
```

ROU asset = lease liability + initial direct costs + restoration provision − incentives.

Initial entry:

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Right-of-use asset | 11,37,236 | |
| To Lease liability | | 11,37,236 |

Then each period split payment into interest and principal (see worked example).

### Ind AS 109 — ECL simplified approach for receivables

Provision matrix: apply a historical loss rate (adjusted for forward-looking factors) to each ageing bucket.

```excel
ECL_bucket = Gross_exposure * loss_rate
Total_ECL  = SUMPRODUCT(exposure_range, loss_rate_range)
```

Impairment entry: Dr Impairment loss (P&L) / Cr Allowance for ECL.

**Security deposit (interest-free) under Ind AS 109** — a ₹5,00,000 deposit refundable in 3 years, discounted at 10%:

```excel
=5,00,000/(1.10)^3   → 3,75,657   'financial asset at amortised cost
Difference 1,24,343  → prepaid rent (ROU/expense), unwound as interest income
```

### Ind AS 16 — componentisation & depreciation

Capitalise cost + directly attributable costs (freight, install, testing) − trade discounts; borrowing costs if a qualifying asset (Ind AS 23). Depreciate each significant **component** with a different useful life separately.

```excel
Depreciation p.a. = (Cost - Residual) / Useful_life           'SLM
=SLN(cost, salvage, life)
=DB(cost, salvage, life, period)                              'WDV / declining balance
```

## Worked example / mini-project

**Build a 5-year Ind AS 116 lease schedule.** Office rent ₹3,00,000/year in arrears, 5 years, IBR 10%.

Liability at inception `=-PV(0.10,5,300000)` = **₹11,37,236**. ROU = same.

| Yr | Opening liab | Interest @10% | Payment | Closing liab | ROU dep (SLM) |
|---|---|---|---|---|---|
| 1 | 11,37,236 | 1,13,724 | 3,00,000 | 9,50,960 | 2,27,447 |
| 2 | 9,50,960 | 95,096 | 3,00,000 | 7,46,056 | 2,27,447 |
| 3 | 7,46,056 | 74,606 | 3,00,000 | 5,20,661 | 2,27,447 |
| 4 | 5,20,661 | 52,066 | 3,00,000 | 2,72,727 | 2,27,447 |
| 5 | 2,72,727 | 27,273 | 3,00,000 | ~0 | 2,27,447 |

Year-1 entries:

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Interest expense (finance cost) | 1,13,724 | |
| Lease liability | 1,86,276 | |
| To Bank | | 3,00,000 |
| Depreciation – ROU asset | 2,27,447 | |
| To Accumulated depreciation – ROU | | 2,27,447 |

**Compare to old AS 19 operating lease:** total P&L would be a flat ₹3,00,000 rent. Under Ind AS 116, Year-1 charge = 1,13,724 + 2,27,447 = **₹3,41,171** — front-loaded. That front-loading is the single most-asked interview point. Reproduce this in Excel; the closing balance hitting ~0 in year 5 is your check.

**Reproduce the ECL piece** with this matrix:

| Ageing | Exposure (₹) | Loss rate | ECL (₹) |
|---|---|---|---|
| Not due | 20,00,000 | 0.5% | 10,000 |
| 1–90 days | 8,00,000 | 2% | 16,000 |
| 91–180 | 3,00,000 | 10% | 30,000 |
| >180 | 1,00,000 | 50% | 50,000 |
| **Total** | **32,00,000** | | **1,06,000** |

`=SUMPRODUCT(B2:B5, C2:C5)` → 1,06,000. Entry: Dr Impairment loss 1,06,000 / Cr Allowance for ECL 1,06,000.

## How it's tested

**Interview questions:**
- Walk me through the 5-step revenue model with an example. When is revenue *over time* vs *point in time*?
- What's the day-1 entry for a lease? Why does an operating lease now sit on the balance sheet?
- Difference between ECL and the old incurred-loss model? What's the "simplified approach"?
- Which costs get capitalised into PPE? Is training cost capitalised? (No.)
- AS vs Ind AS revenue difference — what changed for a bundled software sale?

**Practical tests companies give:**
- **Timed Excel (30–45 min):** "Here's a rent agreement — build the ROU + lease liability schedule and the year-1 journals." Extremely common for reporting/audit roles.
- **Case:** a contract with two deliverables and a discount — allocate the price and give quarterly revenue.
- **Provision matrix:** ageing given, compute ECL with SUMPRODUCT.
- Big-4 audit assessments give an accounting-treatment memo: "conclude with reference to the standard paragraph."

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Recognising bundled revenue upfront | Split into POs, defer service portion as contract liability |
| Using the wrong lease discount rate | Use IBR (or rate implicit if determinable); document the source |
| Straight-lining lease expense under Ind AS 116 | Only AS 19 straight-lines; Ind AS 116 splits interest + depreciation |
| Forgetting short-term/low-value lease exemption | ≤12 months or low-value → expense straight-line, no ROU |
| Provisioning ECL only when overdue | ECL is forward-looking; even *not-due* balances carry a small rate |
| Capitalising training/admin/launch costs in PPE | Only directly attributable costs to bring asset to working condition |
| Ignoring the deferred tax on Ind AS adjustments | Book base ≠ tax base → create DTA/DTL (Ind AS 12) |
| Discounting the security deposit but forgetting to unwind | Recognise interest income each year; amortise the prepaid rent |

## Learn-it roadmap & resources

**Time to proficiency:** 6–8 weeks part-time to handle these four standards confidently in Excel and journals.

- **Weeks 1–2:** Ind AS 115 + 116 — the two highest-yield. Build one lease schedule and one revenue-allocation sheet from scratch.
- **Weeks 3–4:** Ind AS 109 (ECL, amortised cost, security deposits) + Ind AS 16.
- **Weeks 5–6:** Deferred tax linkage (Ind AS 12), consolidation basics, first-time adoption (Ind AS 101).
- **Weeks 7–8:** Real annual reports — read the "significant accounting policies" note of a listed company and rebuild one disclosure.

**Resources:**
- **ICAI** free Ind AS study material + the bare standards (mca.gov.in) — authoritative and free.
- **EY / KPMG / Deloitte / PwC** "Ind AS pocket guides" and illustrative disclosures — free PDFs, industry-grade.
- Company annual reports (Infosys, Reliance) — free, best worked examples of real disclosures.
- **Certification:** ICAI's Certificate Course on Ind AS; **Dip IFR (ACCA)** is the globally-portable equivalent — highly regarded and transferable to IFRS roles abroad.

## Quick-reference

| Item | Formula / rule |
|---|---|
| Revenue (5 steps) | Contract → POs → Price → Allocate (by SSP) → Recognise |
| Price allocation | `=Total*(SSP_item/Total_SSP)` |
| Lease liability | `=-PV(IBR, n, payment, 0, type)` |
| ROU asset | Liability + IDC + restoration − incentives |
| Lease interest | Opening liability × IBR |
| ECL | `=SUMPRODUCT(exposure, loss_rate)` |
| Deposit at amortised cost | `=Deposit/(1+r)^n` |
| PPE depreciation | `=SLN(cost,salvage,life)` or `=DB(...)` for WDV |
| Lease exemption | ≤12 months OR low-value → straight-line expense |
| Applicability | Listed OR net worth ≥ ₹250 cr (+ group entities) |

**Golden rule:** Ind AS front-loads and puts things *on* the balance sheet (leases, ECL, discounted deposits). If your answer looks like flat AS-19 rent or "provide only when overdue," you're on the wrong standard.
