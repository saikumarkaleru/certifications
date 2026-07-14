# TDS I: Identify, Compute, Deduct and Pay the Challan

## The situation

It's **30 April 2026**. This just landed on your desk: the payables clerk at **NTSPL** has queued five vendor bills for payment and pings you — *"Finance says don't release full amounts until you tell me the TDS to hold back. Also the challan has to be paid by 7th May or we get interest — can you compute and prepare it today?"*

You are the accounts executive who owns **TDS (tax deducted at source)**. NTSPL is a **deductor** because its turnover (> Rs 10 cr) crosses every threshold. Your job: for each bill, decide **is TDS attracted, under which section, at what rate**, then post the deduction entry (vendor gets paid **net**, the tax sits in a payable), and finally deposit one lot via challan by **7-May-2026** (for March bills the deadline shifts to 30 April).

> The Income-tax Act, 2025 renumbers non-salary TDS under **Sec 393**, but Tally, TRACES and the challan still use **194C/194J/194H/194I/194Q**. I use the familiar numbers.

## What you're given

The April 2026 vendor payment queue (all amounts exclusive of GST — **TDS is on the taxable value, not on GST**):

| # | Vendor | Nature | Amount (Rs) | Likely section |
|---|---|---|---:|---|
| 1 | CleanCo Agency | Housekeeping contract | 80,000 | 194C |
| 2 | S. Iyer & Co (CA) | Professional fee | 1,00,000 | 194J |
| 3 | Metro Sales Reps | Sales commission | 50,000 | 194H |
| 4 | Prime Estates | Office rent (monthly) | 1,50,000 | 194I |
| 5 | Seller X | Goods purchase (YTD > 50L) | 20,00,000 | 194Q |

FY2026-27 rate & threshold reference:

| Section | Nature | Rate | Threshold |
|---|---|---|---|
| 194C | Contractor | 1% indiv/HUF, **2% others** | Rs 30,000 single / Rs 1,00,000 p.a. |
| 194J | Professional | **10%** (2% technical/call-centre) | Rs 50,000 p.a. |
| 194H | Commission/brokerage | **2%** | Rs 20,000 p.a. |
| 194I | Rent (land/building) | **10%** | Rs 2,40,000 p.a. |
| 194Q | Purchase of goods | **0.1%** on value **over Rs 50 lakh**/seller | buyer turnover > Rs 10 cr |

## Do it — step by step

### Step 1 — threshold check (is TDS even attracted?)

| # | Section | Threshold test | Attracted? |
|---|---|---|---|
| 1 | 194C | Single bill Rs 80,000 > Rs 30,000 | Yes |
| 2 | 194J | Rs 1,00,000 > Rs 50,000 p.a. | Yes |
| 3 | 194H | Rs 50,000 > Rs 20,000 p.a. | Yes |
| 4 | 194I | Rs 1,50,000/mo → annualised Rs 18,00,000 > Rs 2,40,000 | Yes |
| 5 | 194Q | Buyer T/O > 10cr; this seller's YTD purchases now > Rs 50L | Yes, on excess |

### Step 2 — compute each TDS

**1. 194C — CleanCo (agency = "other", so 2%):** 2% × 80,000 = **Rs 1,600**. Net paid = 78,400.

**2. 194J — S. Iyer & Co (CA professional, 10%):** 10% × 1,00,000 = **Rs 10,000**. Net = 90,000.

**3. 194H — Metro Sales (commission, 2%):** 2% × 50,000 = **Rs 1,000**. Net = 49,000.

**4. 194I — Prime Estates (rent, 10%):** 10% × 1,50,000 = **Rs 15,000**. Net = 1,35,000.

**5. 194Q — Seller X (0.1% only on value over Rs 50 lakh):** Suppose YTD purchases from Seller X were Rs 40,00,000 before this Rs 20,00,000 bill, so cumulative = Rs 60,00,000. The **first Rs 50L is exempt**; TDS applies on the excess **Rs 10,00,000** → 0.1% × 10,00,000 = **Rs 1,000**. Net on this bill = 20,00,000 − 1,000 = 19,99,000.

> 194Q vs 206C(1H): if the seller was already collecting **TCS** on the same sale, 194Q (buyer's deduction) **prevails** and the seller stops TCS. Only one applies.

**Total TDS deducted, April 2026 (non-salary):**

| Section | Amount (Rs) |
|---|---:|
| 194C | 1,600 |
| 194J | 10,000 |
| 194H | 1,000 |
| 194I | 15,000 |
| 194Q | 1,000 |
| **Total 26Q TDS** | **28,600** |

### Step 3 — the deduction entries in TallyPrime

Path: **Gateway of Tally → Vouchers → F5 Payment** (or F7 Journal to book the bill, then payment). Booking the CA bill (194J) as a journal:

```
Dr  Professional Fees (Indirect Exp)     1,00,000
      Cr  S. Iyer & Co (Sundry Creditor)     90,000
      Cr  TDS Payable - 194J                  10,000
```

Rent (194I):

```
Dr  Rent (Indirect Exp)                  1,50,000
      Cr  Prime Estates                     1,35,000
      Cr  TDS Payable - 194I                  15,000
```

194Q on the goods purchase (TDS reduces the payable, not the purchase cost):

```
Dr  Purchases (Goods)                   20,00,000
      Cr  Seller X                        19,99,000
      Cr  TDS Payable - 194Q                  1,000
```

Same pattern for 194C (Cr TDS 1,600) and 194H (Cr TDS 1,000). Every entry: **Dr the full expense/purchase, Cr the vendor net, Cr the TDS payable.**

### Step 4 — lower / no-deduction cases

Before deducting, check whether the vendor gave you a certificate:

- **Form 15G/15H:** self-declaration by a resident (15H = senior citizen) that total income is below the taxable limit — mainly for interest (194A), **not** applicable to 194C/J/H/I/Q here, but you must still collect and report any that arrive.
- **Sec 197 certificate:** the vendor obtains a TDS certificate from their AO authorising a **lower or nil rate**. If Prime Estates hands you a 197 cert at 2%, you deduct 2% (Rs 3,000), not 10% — and you must quote the **certificate number** in the return.
- **No PAN → Sec 206AA:** deduct at the **higher of the specified rate or 20%**. If Metro Sales has no PAN, 194H becomes 20% = Rs 10,000, not Rs 1,000.

### Step 5 — pay the challan (by 7-May-2026)

Portal: **incometax.gov.in → e-Pay Tax** (the old **Challan ITNS 281** is now the online e-pay-tax flow). Fill:

| Field | Value |
|---|---|
| TAN | **HYDN01234A** |
| Assessment Year | **2027-28** (AY for FY2026-27) |
| Type of payment | **(200) TDS payable by taxpayer** (not 400 = demand) |
| Nature / section | 94C / 94J / 94H / 94I / 94Q as applicable |
| Tax | 28,600 |
| Interest / Penalty | 0 |
| Total | **28,600** |
| Mode | Net-banking, HDFC xxxx4567 |

On success you get a **CIN** (Challan Identification Number: BSR code + date + challan serial). Post it:

```
Dr  TDS Payable (194C/J/H/I/Q)   28,600
      Cr  HDFC Bank               28,600
```

## The deliverable

**April 2026 TDS working (non-salary) — ready for the 26Q return:**

| Section | Base (Rs) | Rate | TDS (Rs) | Net paid (Rs) |
|---|---:|---|---:|---:|
| 194C CleanCo | 80,000 | 2% | 1,600 | 78,400 |
| 194J S. Iyer & Co | 1,00,000 | 10% | 10,000 | 90,000 |
| 194H Metro Sales | 50,000 | 2% | 1,000 | 49,000 |
| 194I Prime Estates | 1,50,000 | 10% | 15,000 | 1,35,000 |
| 194Q Seller X | 10,00,000* | 0.1% | 1,000 | 19,99,000 |
| **Total** | | | **28,600** | |

*194Q base = amount over the Rs 50L cumulative threshold. **Challan deposited 07-May-2026, CIN recorded.**

## How it's checked

- **Section & rate** match the nature of payment (agency = 194C @ 2%, CA = 194J @ 10%).
- **Base excludes GST** where the GST is shown separately on the invoice.
- **194Q** is on the **excess over Rs 50L**, not the whole bill — Rs 1,000, not Rs 2,000.
- **PAN present** on every deductee, else 206AA 20% kicks in.
- **Challan:** TAN, AY 2027-28, minor head 200, section codes correct; total Rs 28,600 = sum of TDS Payable ledgers cleared.
- **Deposit date ≤ 7th** of next month — the CIN date proves timeliness.

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---|---|---|
| TDS on gross incl. GST | Over-deduction, vendor dispute | Deduct on taxable value only |
| 194Q on full Rs 20L | Rs 2,000 instead of Rs 1,000 | Only the excess over Rs 50L |
| Using 1% for agency 194C | Short deduction | Non-individual = 2% |
| No PAN, still at normal rate | 206AA short deduction, notice | Deduct 20% when PAN absent |
| AY quoted as 2026-27 | Challan mis-tagged, mismatch in 26Q | FY2026-27 → **AY 2027-28** |
| Minor head 400 instead of 200 | Challan treated as demand payment | Use 200 for regular TDS |
| Late deposit (after 7th) | **Interest 1.5%/month** u/s 201 | Pay by the 7th |

## On the job & in the interview

**The "why":** TDS collects tax at the point income is paid, so the government gets revenue early and the transaction is reported — the deductee then claims the TDS as a credit in their own return (visible in their 26AS/AIS). NTSPL is the **collection agent**: deduct on paying, deposit by the 7th, report quarterly.

**Jargon:** *deductor/deductee*, *TAN* (deductor's tax account number — different from PAN), *CIN* (challan proof), *minor head 200 vs 400*, *206AA* (no-PAN higher rate), *Sec 201* (interest for late deduction/deposit).

**Interview Q&A:**

- *"Vendor bills Rs 20 lakh of goods, you've already bought Rs 40 lakh from him this year — what's the 194Q TDS?"* → "Cumulative Rs 60L, first Rs 50L is outside 194Q, so 0.1% on the Rs 10L excess = Rs 1,000. And 194Q overrides the seller's 206C(1H) TCS."
- *"A contractor has no PAN — what rate?"* → "Section 206AA forces the higher of the specified rate or 20%. So a 194C agency payment goes from 2% to 20%."
- *"By when must April TDS reach the government, and what if it's late?"* → "By 7 May 2026 via e-pay-tax under TAN HYDN01234A. Late deposit attracts interest at 1.5% per month under Sec 201, and the expense can be disallowed."
