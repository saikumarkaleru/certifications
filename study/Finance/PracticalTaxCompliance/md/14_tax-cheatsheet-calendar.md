# Cheat-sheet: due-dates, rates & forms

## What it is & where it's used

Every finance/accounts/tax job in India runs on a compliance calendar. Miss a GST return by a day and interest plus late fees start ticking; miss a TDS deposit and you lose the expense deduction. The person who *knows the dates cold* — the 7th, 11th, 15th, 20th of every month — is the one the manager trusts with the filings.

This chapter is the reference sheet you keep pinned. It's used by:

- **Accounts executives / AP-AR** — TDS deduction, GST input reconciliation.
- **Tax associates (Big 4, boutique CA firms)** — return filing, advance tax, TDS returns.
- **Finance analysts / controllers** — cash-flow planning around statutory outflows.
- **Founders / SME accountants** — the one-person compliance team.

Interviewers *love* this because it can't be bluffed. You either know that TDS is deposited by the **7th** and the GSTR-3B is by the **20th**, or you don't.

> Rates below reflect **FY 2025-26 / AY 2026-27**. Always re-verify against the latest Finance Act — rates change every Budget.

## The gap: why companies want this (and college didn't teach it)

An MBA teaches you *what* TDS is (a mechanism to collect tax at source). It never teaches you that Section 194J (professional fees) is 10%, 194C (contractor) is 1%/2%, 194Q (goods purchase) is 0.1%, or that all of them get deposited by the 7th of the next month via **Challan ITNS-281**. College gives you the concept; the employer pays for the **execution under a deadline**.

The gap is precisely this: colleges teach *principles*, jobs run on *dates, forms, sections and thresholds*. A fresher who says "I'll deduct TDS on this consultant bill at 10% under 194J, deposit by the 7th, and file 26Q for the quarter" is instantly worth more than one who defines TDS beautifully but can't file it.

## What "proficient" looks like

A job-ready person can, *without Googling*:

1. Look at a purchase/expense invoice and state the correct **TDS section, rate, and threshold**.
2. Name the **due date** for TDS deposit, TDS return, GSTR-1, GSTR-3B, advance tax, and ROC filings.
3. Compute **interest and late fee** for a delayed filing.
4. Pick the **right form** (26Q vs 24Q vs 27Q; GSTR-1 vs 3B vs 9; ITR-1 vs 3 vs 6).
5. Read a GST portal / TRACES dashboard and know what's pending.

The bar isn't memorising all of the Income-tax Act — it's the **20 high-frequency dates, rates and forms** that recur every single month.

## Hands-on: how to actually do it

### 1. The monthly compliance rhythm (burn this into memory)

| Date | Obligation | Form / Challan |
|------|-----------|----------------|
| **7th** | Deposit TDS/TCS for previous month | Challan ITNS-281 |
| **11th** | File GSTR-1 (outward supplies, monthly filers) | GSTR-1 |
| **13th** | GSTR-1 (QRMP quarterly) / IFF (optional) | GSTR-1 / IFF |
| **15th** | PF & ESI deposit; Advance tax (quarterly) | ECR / Challan 280 |
| **20th** | File & pay GSTR-3B (monthly filers) | GSTR-3B |
| **22nd/24th** | GSTR-3B (QRMP, state-wise) | GSTR-3B |
| **30th/31st** | TDS return (quarterly), ROC filings | 26Q/24Q, MGT-7/AOC-4 |

### 2. TDS rate & section quick lookup (most-used)

| Section | Nature of payment | Rate | Threshold (FY25-26) |
|---------|-------------------|------|---------------------|
| 192 | Salary | Slab | Basic exemption |
| 194A | Interest (non-bank) | 10% | ₹5,000 |
| 194C | Contractor (individual/HUF) | 1% | ₹30,000 single / ₹1,00,000 aggregate |
| 194C | Contractor (others) | 2% | same |
| 194H | Commission / brokerage | 2% | ₹20,000 |
| 194I | Rent — plant & machinery | 2% | ₹2,40,000 |
| 194I | Rent — land/building | 10% | ₹2,40,000 |
| 194J | Professional / technical fees | 10% / 2% | ₹30,000 |
| 194Q | Purchase of goods | 0.1% | ₹50,00,000 |
| 206C(1H) | TCS on sale of goods | 0.1% | ₹50,00,000 |

> No PAN → TDS at **20%** (or twice the rate, whichever is higher).

### 3. Interest & late-fee formulas (put these in Excel)

```excel
' TDS interest — late DEDUCTION: 1% per month (or part) from due-to-deduct to actual deduction
=TDS_Amount * 1% * Months_Delay

' TDS interest — late DEPOSIT: 1.5% per month (or part) from deduction to deposit
=TDS_Amount * 1.5% * ROUNDUP((Deposit_Date - Deduction_Date)/30, 0)

' GST late fee (3B/1): Rs 50/day (Rs 20/day nil), capped
=MIN(Days_Late * 50, Cap)

' GST interest on late tax payment: 18% p.a. on net tax
=Net_Tax * 18% * Days_Late / 365
```

### 4. Which form? (decision cheat-sheet)

```
TDS returns:   Salary → 24Q   |  Resident non-salary → 26Q  |  Non-resident → 27Q  |  TCS → 27EQ
GST returns:   Sales → GSTR-1 |  Summary+pay → GSTR-3B       |  Annual → GSTR-9 (>Rs 2 cr) + 9C (>Rs 5 cr)
Income Tax:    Individual (no biz) → ITR-1/2 | Individual+biz → ITR-3 | Firm/LLP → ITR-5 | Company → ITR-6
ROC (company): Annual return → MGT-7 | Financials → AOC-4 | Director KYC → DIR-3 KYC
```

### 5. Income-tax slabs — New Regime (default, AY 2026-27)

| Income slab | Rate |
|-------------|------|
| Up to ₹4,00,000 | Nil |
| ₹4,00,001 – ₹8,00,000 | 5% |
| ₹8,00,001 – ₹12,00,000 | 10% |
| ₹12,00,001 – ₹16,00,000 | 15% |
| ₹16,00,001 – ₹20,00,000 | 20% |
| ₹20,00,001 – ₹24,00,000 | 25% |
| Above ₹24,00,000 | 30% |

Rebate u/s 87A: nil tax up to ₹12,00,000 taxable income. Standard deduction ₹75,000 (salary). Verify against the current Finance Act each year.

## Worked example / mini-project

**Scenario:** Acme Traders Pvt Ltd, June 2026. Build the month's compliance sheet.

Transactions:
- Paid consultant ₹80,000 for audit support (194J).
- Paid contractor (company) ₹1,50,000 for fit-out (194C).
- Office rent to landlord ₹60,000/month (194I building).
- June sales ₹18,00,000 + GST 18%; input GST available ₹1,40,000.

**Step 1 — TDS:**

| Payment | Section | Rate | TDS |
|---------|---------|------|-----|
| Consultant ₹80,000 | 194J | 10% | ₹8,000 |
| Contractor ₹1,50,000 | 194C | 2% | ₹3,000 |
| Rent ₹60,000 | 194I(b) | 10% | ₹6,000 |
| **Total TDS** | | | **₹17,000** |

Deposit ₹17,000 via ITNS-281 by **7 July 2026**. File 26Q by **31 July 2026** (Q1).

**Step 2 — GST:**
- Output GST = 18,00,000 × 18% = ₹3,24,000
- Input credit = ₹1,40,000
- Net GST payable = **₹1,84,000**
- File GSTR-1 by **11 July**, GSTR-3B + pay ₹1,84,000 by **20 July 2026**.

**Step 3 — What if 3B is filed on 5 August (15 days late)?**
- Late fee = 15 × ₹50 = ₹750
- Interest = 1,84,000 × 18% × 15/365 = **₹1,361**
- Total avoidable cost = **₹2,111** — the entire point of knowing the calendar.

**Journal entry for the consultant bill + TDS:**

| Particulars | Dr | Cr |
|-------------|-----|-----|
| Professional Fees A/c | 80,000 | |
| To TDS Payable (194J) | | 8,000 |
| To Consultant (Bank/Payable) | | 72,000 |

## How it's tested

**Interview questions:**
- "By when do you deposit TDS deducted in June?" → 7 July.
- "TDS rate and section on a ₹1 lakh consultancy bill?" → 194J, 10%, ₹10,000.
- "Difference between GSTR-1 and GSTR-3B?" → 1 = outward supply detail; 3B = summary + tax payment.
- "Company files which ITR?" → ITR-6.
- "Interest for depositing TDS one month late?" → 1.5% per month.

**Practical assessments companies give:**
1. **Timed compliance-calendar test** — a table of transactions; you fill section, rate, TDS, due date under 20 minutes.
2. **Excel late-fee model** — build interest/late-fee formulas for a set of delayed filings.
3. **"File this in Tally"** — pass TDS entries, generate 26Q, reconcile GSTR-2B vs purchase register.
4. **GST recon case** — spot the invoices in books but missing from GSTR-2B and quantify blocked ITC.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---------|-----|
| Deducting TDS at wrong rate/section | Keep the section table taped to your monitor; verify threshold *and* rate |
| Missing the "part of a month" rule | Interest is per month **or part** — 31 days = 2 months, always ROUNDUP |
| Forgetting the aggregate threshold (194C ₹1 L/yr) | Track year-to-date payments per vendor, not just single bills |
| Filing 3B without reconciling 2B | Reconcile ITC monthly; claim only what appears in GSTR-2B |
| No-PAN vendor deducted at normal rate | 20% flat when PAN absent — always collect PAN first |
| Depositing TDS but not filing the return | Deposit ≠ return; 26Q/24Q are separate quarterly obligations |
| Using old FY rates | Re-check every rate after the Union Budget |

Pros run a **shared calendar with reminders 2 days before each due date**, keep a vendor master with PAN + default TDS section, and reconcile GST every month — never at year-end.

## Learn-it roadmap & resources

**Time to proficiency:** 3–4 weeks of hands-on filing to internalise the calendar; ~2 months to be trusted end-to-end.

- **Week 1** — Memorise the monthly rhythm (7/11/15/20) and top-10 TDS sections.
- **Week 2** — Practice GSTR-1 & 3B on the GST portal sandbox; do 2B reconciliation.
- **Week 3** — File a mock 26Q on TRACES; build the interest/late-fee Excel model.
- **Week 4** — Do a full month's close for a dummy company (like the example above).

**Resources:**
- **Free:** income-tax portal (incometax.gov.in), GST portal (gst.gov.in), CBIC & CBDT circulars, ClearTax/TaxGuru blogs, ICAI study material (Taxation).
- **Paid:** ClearTax / Zoho Books hands-on, Udemy "GST & TDS Practical", any local CA-firm articleship (best learning).
- **Certification:** CA Intermediate (Taxation paper), ICAI GST certificate course, GST Practitioner exam.

## Quick-reference

```
MONTHLY:  7th TDS deposit | 11th GSTR-1 | 15th PF/ESI/adv tax | 20th GSTR-3B
QUARTERLY: TDS return by end of month after quarter (Q4 salary 24Q → 31 May)
ADV TAX:  15 Jun 15% | 15 Sep 45% | 15 Dec 75% | 15 Mar 100%
ANNUAL:   ITR (non-audit) 31 Jul | audit 31 Oct | GSTR-9 31 Dec | AOC-4/MGT-7 within 30/60 days of AGM
```

| Quick TDS | Sec | Rate |
|-----------|-----|------|
| Salary | 192 | Slab |
| Contractor | 194C | 1%/2% |
| Commission | 194H | 2% |
| Rent (building) | 194I | 10% |
| Professional | 194J | 10% |
| Goods purchase | 194Q | 0.1% |

| Interest/Fee | Rate |
|--------------|------|
| TDS late deduction | 1% / month |
| TDS late deposit | 1.5% / month |
| GST late tax | 18% p.a. |
| GST late fee | ₹50/day (₹20 nil), capped |
| Income-tax 234B/C | 1% / month |

**Forms:** 24Q (salary TDS) · 26Q (non-salary) · 27Q (NR) · 27EQ (TCS) · GSTR-1/3B/9/9C · ITR-1/3/5/6 · ITNS-281 (TDS challan) · Challan 280 (income tax).
