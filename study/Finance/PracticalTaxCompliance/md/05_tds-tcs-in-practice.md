# TDS/TCS in practice

## What it is & where it's used

**TDS (Tax Deducted at Source)** means the *payer* withholds a slice of tax before paying a vendor, employee, landlord or contractor, and deposits it with the government against the payee's PAN. **TCS (Tax Collected at Source)** is the mirror image — the *seller* collects a small extra amount from the buyer on certain sales (scrap, motor vehicles > ₹10 lakh, some goods sales) and remits it.

It is the government's cash-flow engine and its biggest data-matching tool: every rupee deducted lands in the payee's **Form 26AS / AIS**, and if it doesn't match, someone gets a notice.

Roles that live and breathe this:

| Role | TDS/TCS work |
|---|---|
| Accounts Payable executive | deduct correct section/rate at invoice booking |
| Payroll executive | monthly TDS on salary (192), Form 16 in May |
| Tax/compliance associate | monthly challans, quarterly 24Q/26Q, corrections |
| Statutory auditor / articled clerk | vouch deductions, verify 26Q vs books, 40(a)(ia) disallowance |
| Vendor master / procurement | 206AB/206CCA PAN screening before onboarding |

If you touch a payment run in India, you touch TDS.

## The gap: why companies want this (and college didn't teach it)

An MBA teaches that "tax is deducted at source." It does **not** teach that you have to:

- pick the *right section* from a 40-row rate chart at the moment of booking,
- apply the **higher rate under 206AB** when a vendor hasn't filed returns,
- deposit by the **7th of next month** (30 April for March) or eat 1.5%/month interest,
- file **26Q** with the exact challan-deduction mapping or the return gets rejected,
- and know that a wrong deduction triggers a **30% expense disallowance** under section 40(a)(ia).

Colleges test *concepts*; employers test *whether the challan is right and filed on time*. A single missed deposit means interest, a ₹200/day late-filing fee under 234E, and a partner's phone call. That operational, deadline-driven, penalty-aware muscle is exactly what companies pay for and what no classroom simulates.

## What "proficient" looks like

A job-ready person can, unaided:

1. Read an invoice and say **"194J, 10%, ₹X"** or **"194C, 1%/2%, ₹Y"** in seconds.
2. Apply **threshold logic** (e.g. 194C single ₹30,000 / annual ₹1,00,000; 194J ₹30,000; 194Q ₹50 lakh) and **206AB** higher-rate override.
3. Pass the correct **journal entry** and reconcile the TDS payable ledger to the challan.
4. Generate a **challan (ITNS 281 / e-Pay Tax)**, download the CSI file, and validate the return in **RPU/TRACES**.
5. Explain the interplay of **194Q (buyer deducts) vs 206C(1H) (seller collects)** and who wins.
6. Produce **Form 16A** from TRACES and **Form 16** (Part A + Part B) for payroll.

## Hands-on: how to actually do it

### Key sections cheat-rates (FY 2025-26, resident, PAN available)

| Section | Nature of payment | Threshold | Rate |
|---|---|---|---|
| 192 | Salary | Basic exemption | Slab (avg) |
| 194C | Contractor / sub-contractor | ₹30,000 single / ₹1,00,000 p.a. | 1% (Ind/HUF), 2% (others) |
| 194J | Professional / technical fees | ₹30,000 | 10% (2% for technical/call-centre) |
| 194H | Commission / brokerage | ₹20,000 | 2% |
| 194I | Rent — plant/machinery / land-building | ₹2,40,000 p.a. | 2% / 10% |
| 194Q | Purchase of goods (buyer T/O > ₹10 cr) | ₹50,00,000 | 0.1% on excess |
| 206C(1H) | Sale of goods (seller T/O > ₹10 cr) | ₹50,00,000 | 0.1% on excess |
| 206C(1) | Scrap | — | 1% |
| **No PAN** | any | — | **20% (206AA)** |

### 206AB / 206CCA — the "non-filer" penalty

If the payee is a **"specified person"** (didn't file ITR for the relevant previous year *and* aggregate TDS/TCS ≥ ₹50,000 in that year), deduct at the **higher of**: twice the normal rate, or 5%. Check status on the **Reporting Portal → Compliance Check for 206AB** (bulk PAN upload). Never onboard a big vendor without this screen.

### Excel: pick section, apply threshold, compute TDS

```excel
' Rate lookup from a RateTable (Section | Rate)
=XLOOKUP([@Section], RateTable[Section], RateTable[Rate])

' Apply annual threshold: only deduct once cumulative crosses limit
=IF([@CumInvoiceValue]>[@Threshold], [@InvoiceValue]*[@Rate], 0)

' 194Q — 0.1% only on purchases ABOVE 50 lakh (cumulative from same seller)
=MAX(0, MIN([@CumPurchase],[@CurrPurchase]) - MAX(5000000,[@CumPurchase]-[@CurrPurchase]))*0.001

' 206AB override: higher of 2x rate or 5%
=IF([@IsSpecifiedPerson]="Y", MAX([@Rate]*2, 5%), [@Rate])
```

### Journal entries

Booking a ₹1,00,000 professional-fee invoice (194J @10%):

| Account | Dr | Cr |
|---|---|---|
| Professional Fees (expense) | 1,00,000 | |
| To Vendor A/c | | 90,000 |
| To TDS Payable – 194J | | 10,000 |

On deposit (7th of next month):

| Account | Dr | Cr |
|---|---|---|
| TDS Payable – 194J | 10,000 | |
| To Bank | | 10,000 |

### TallyPrime click-path
`Gateway of Tally → Vouchers → F9 Purchase` → select TDS nature of payment on the ledger → Tally auto-computes → `Alt+G → TDS Reports → Challan Reconciliation` → `Ctrl+P` for ITNS 281.

### Deposit & return calendar

| Task | Due date |
|---|---|
| Deposit TDS (Apr–Feb) | **7th** of next month |
| Deposit TDS (March) | **30 April** |
| **26Q/27Q** (non-salary) | Q1 31-Jul, Q2 31-Oct, Q3 31-Jan, Q4 **31-May** |
| **24Q** (salary) | same quarterly dates |
| **Form 16A** (from TRACES) | 15 days after return due date |
| **Form 16** (salary) | **15 June** |

Deposit via **income tax portal → e-Pay Tax → Proceed (TDS/TCS) → ITNS 281**. Download the **CSI file** from the portal — the RPU validation needs it.

## Worked example / mini-project

**Vermilion Analytics Pvt Ltd**, June 2025 payments:

| Vendor | Service | Section | Amount (₹) | Note |
|---|---|---|---|---|
| CA Rao & Co | Audit fee | 194J | 2,00,000 | PAN valid |
| BuildRight (partnership) | Office renovation | 194C | 5,00,000 | contractor |
| Mehta (proprietor) | Freelance design | 194J | 40,000 | **non-filer (206AB)** |
| Landlord (building) | Office rent | 194I(b) | 3,00,000 | annual |

**Computation**

```
194J  Rao & Co : 2,00,000 × 10%           = 20,000
194C  BuildRight (firm, 2%) : 5,00,000 × 2% = 10,000
194J  Mehta, 206AB → max(10%×2, 5%)=20% :
      40,000 × 20%                          =  8,000
194I  Rent (building 10%) : 3,00,000 × 10% = 30,000
------------------------------------------------
Total TDS for June                          = 68,000
```

Deposit **₹68,000 by 7 July 2025** (four challans or one, split by section in the return). If deposited on 20 July instead:
`Interest u/s 201 = 68,000 × 1.5% × 2 months (deducted June, paid July → part-months) = ₹2,040`.

**Return (26Q, Q1) mapping** — each deductee row links to the challan by BSR code + date + serial. Validate in **RPU** → generate `.fvu` → upload on TRACES/income-tax portal → download **Form 16A** for each vendor two weeks later.

Reproduce it: build the four-row table in Excel, add the `206AB` override formula, sum column, and you have the exact number a compliance associate files.

## How it's tested

**Interview questions**
- "Vendor raises a ₹28,000 194C invoice, then a ₹15,000 one — do you deduct? On what?" (Yes, on ₹43,000 total, since annual ₹1,00,000 not crossed but single-bill ₹30,000 crossed on second? — trap: 194C single limit ₹30,000, aggregate ₹1,00,000; neither crossed individually but aggregate matters — expected answer: deduct once ₹1,00,000 aggregate crosses.)
- "194Q vs 206C(1H) — same transaction, both above ₹50L, who acts?" (194Q buyer prevails; seller stops collecting.)
- "What is section 40(a)(ia)?" (30% disallowance of expense if TDS not deducted/paid.)
- "Client didn't deduct 206AB higher rate — consequences?" (short deduction, interest, disallowance.)

**Practical test** companies give:
- A timed sheet of 10 invoices → identify section, rate, TDS amount, and total challan (30 min in Excel).
- "Here's a 26Q .fvu error log — fix the challan-deduction mismatch."
- Payroll case: compute annual salary TDS, spread over 12 months, produce Form 16 Part B.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Deducting on **GST component** of invoice | Deduct on **taxable value only** (excl. GST), if GST shown separately |
| Wrong Ind/HUF vs firm rate in 194C (1% vs 2%) | Check payee constitution in vendor master |
| Missing **206AB** higher rate | Run bulk Compliance Check every quarter; flag in vendor master |
| Depositing March TDS by 7 April | March deadline is **30 April** — don't overpay interest, don't miss |
| Challan section ≠ return section | Reconcile TDS payable ledger to challan before filing |
| Quoting no PAN → 20% forgotten | Block payment until PAN captured |
| Late return | ₹200/day fee u/s **234E** (capped at TDS amount) — file even if late |

Pros keep a **TDS control sheet**: section-wise payable ledger reconciled to challans each month, and a vendor master with PAN + 206AB status refreshed quarterly.

## Learn-it roadmap & resources

**Time to proficiency:** 3–4 weeks of hands-on, if you already know accounting basics.

| Week | Focus |
|---|---|
| 1 | Section/rate chart, thresholds, journal entries |
| 2 | e-Pay Tax challan, CSI file, TallyPrime TDS |
| 3 | RPU + TRACES: file a dummy 26Q, generate Form 16A |
| 4 | 24Q + Form 16, 206AB compliance check, corrections |

**Resources (free):** Income Tax India e-filing portal (practice login), TRACES "e-Tutorials", NSDL/Protean **RPU & FVU** utilities (download free), CBDT rate chart PDF. **Paid:** ICAI BoS TDS module, ClearTDS / Winman TDS software (free trials), any "TDS return filing" Udemy course (₹500).
**Certification:** none required, but ICAI Intermediate (Taxation) and a "GST & TDS Practitioner" course strengthen the CV.

## Quick-reference

```
DEPOSIT: 7th next month | MARCH: 30 April
RETURNS: 26Q/24Q — 31 Jul / 31 Oct / 31 Jan / 31 May
FORM 16: 15 June | FORM 16A: 15 days after return

RATES (PAN available, FY25-26):
 192  salary        slab
 194C contractor    1% ind/huf, 2% others   (30k/1L)
 194J prof fees     10% (2% technical)       (30k)
 194H commission    2%                        (20k)
 194I rent          2% P&M / 10% land-bldg    (2.4L)
 194Q buy goods     0.1% >50L (buyer T/O>10cr)
 206C(1H) sell gds  0.1% >50L (seller side)
 206C(1) scrap      1%
 NO PAN (206AA)     20%
 206AB non-filer    higher of 2×rate or 5%

INTEREST 201: 1%/mo (not deducted) or 1.5%/mo (not paid)
LATE FEE 234E: ₹200/day (max = TDS)
DISALLOWANCE 40(a)(ia): 30% of expense
```

**Key formula:** `TDS = Taxable value (excl. GST) × applicable rate`, applied once the cumulative payment crosses the section threshold, with a 206AB override for non-filers.
