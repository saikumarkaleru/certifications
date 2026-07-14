# TDS II: Filing 26Q & 24Q and Issuing Form 16/16A

## The situation

It's **10 July 2026** — the first quarter (Apr–Jun, **Q1 FY2026-27**) is closed and the return deadline is **31 July 2026**. This just landed on your desk: the finance manager forwards a calendar reminder — *"Q1 TDS returns due end of month. File 26Q and 24Q, and I need Form 16A for our landlord and Form 16 for staff ready right after. Also — TRACES flagged a short-deduction on last cycle; sort that out."*

You own the **TDS return filing**. Deducting and paying (Chapter 06) was only half the job; now you must **report every deductee** to the department so their tax credit appears in their AIS/26AS. Two returns:

- **26Q** — non-salary TDS (the 194C/J/H/I/Q from Chapter 06).
- **24Q** — salary TDS u/s 192 (the payroll from Chapter 05).

Then generate **Form 16A** (non-salary certificate) and **Form 16** (salary certificate) from TRACES, and clear the short-deduction default.

> Renumbering note: the 2025 Act calls these Sec 392 (salary)/393 (others), but the utilities, forms and TRACES still say 24Q/26Q and 194x. Familiar numbers used throughout.

## What you're given

The Q1 challan register (three months, but I show April's detail from Chapter 06; May and June mirror it):

| Challan (CIN) | Month | Section(s) | TDS (Rs) |
|---|---|---|---:|
| BSR 0510308 / 07-05-2026 / 00123 | Apr | 26Q: 94C+94J+94H+94I+94Q | 28,600 |
| BSR 0510308 / 07-05-2026 / 00124 | Apr | 24Q: 192 | 19,175 |
| (May challans) | May | 26Q + 24Q | 28,600 + 19,175 |
| (Jun challans) | Jun | 26Q + 24Q | 28,600 + 19,175 |

Deductee master for the April **26Q** annexure:

| Deductee | PAN | Section | Amount paid (Rs) | TDS (Rs) |
|---|---|---|---:|---:|
| CleanCo Agency | AAACC1111C | 194C | 80,000 | 1,600 |
| S. Iyer & Co | AAAFS2222F | 194J | 1,00,000 | 10,000 |
| Metro Sales Reps | AABFM3333M | 194H | 50,000 | 1,000 |
| Prime Estates | AAAAP4444P | 194I | 1,50,000 | 15,000 |
| Seller X | AAACS5555S | 194Q | 20,00,000 | 1,000 |

FY2026-27 due dates: **26Q/24Q — Q1 31-Jul, Q2 31-Oct, Q3 31-Jan, Q4 31-May.** Form 16A within 15 days of filing; **Form 16 by 15 June** after the FY.

## Do it — step by step

### Step 1 — prepare the return (RPU) and validate (FVU)

Download the **RPU** (Return Preparation Utility) and **FVU** (File Validation Utility) from the Protean/TIN site (or use TallyPrime's e-TDS export, or the income-tax portal's online 26Q flow).

In the RPU, fill three blocks:

1. **Deductor details:** TAN **HYDN01234A**, PAN **AABCN1234A**, name NTSPL, address Hyderabad, FY 2026-27, Form **26Q**, Quarter **Q1**.
2. **Challan details:** each CIN (BSR code + date + challan serial) and the amount — April's 26Q line = Rs 28,600.
3. **Deductee annexure:** one row per deductee, **mapped to the challan** that carried their tax.

A filled **26Q deductee row** (April, the CA):

| Field | Value |
|---|---|
| Deductee code | 02 (company) |
| PAN | AAAFS2222F |
| Name | S. Iyer & Co |
| Section | **194J** |
| Date of payment/credit | 30-04-2026 |
| Amount paid | 1,00,000 |
| TDS deducted | 10,000 |
| TDS deposited | 10,000 |
| Date of deduction | 30-04-2026 |
| Rate | 10% |
| Challan CIN mapped | BSR 0510308 / 07-05-2026 / 00123 |

Run **FVU validation** → it checks PAN format, that **sum of deductee TDS = challan amount**, and section codes. Output: a **.fvu file** + **Form 27A** (the one-page summary/control sheet).

### Step 2 — the 24Q difference (salary)

24Q has the same challan block, but the deductee annexure carries **each employee's monthly TDS**, and **Annexure II** (filed in **Q4 only**) carries the full-year salary breakup, deductions and tax computation per employee — that's what drives Form 16. For Q1, just the challan + per-employee deducted amounts (e.g. Arjun Rs 19,175/month; Priya nil).

### Step 3 — upload

Portal: **incometax.gov.in → e-File → Income Tax Forms → File TDS Return**, upload the **.fvu**, sign with **DSC** (or EVC). You get a **Token/Provisional Receipt Number (PRN)** — keep it; that's proof of filing.

### Step 4 — download certificates from TRACES

After the return is processed (a few days), log in to **TRACES** (deductor login, TAN HYDN01234A):

- **Form 16A** (non-salary): *Downloads → Form 16A → Q1 → 26Q*. TRACES generates a PDF per deductee with the **TRACES watermark and a unique certificate number**. Hand Form 16A to Prime Estates (rent, Rs 15,000 TDS), S. Iyer, etc. **Never** hand-type a 16A — only the TRACES-generated one is valid.
- **Form 16** (salary): Part A (TDS summary) from TRACES + **Part B** (salary computation) — issue to each employee **by 15 June** after year-end. Priya's Form 16 will show tax **nil** (87A); Arjun's will show Rs 2,30,100 deducted over the year.

### Step 5 — clear the short-deduction / late-fee default

TRACES shows a **Justification Report** flagging, say, a Rs 500 short-deduction (a bill where 1% was applied instead of 2% under 194C) plus **Sec 234E late fee** (Rs 200/day) because a prior return was one day late.

Fix:
1. Pay the shortfall + interest via a fresh challan (minor head **400 — TDS on regular assessment / demand**).
2. File a **correction (revised) return** in the RPU, adding the extra deduction and mapping the new challan.
3. Pay **234E fee** (Rs 200/day, capped at the TDS amount) — it **cannot be waived**.

```
Dr  TDS Short-deduction & Interest (Exp)   xxx
Dr  Late Filing Fee 234E (Exp, disallowed) xxx
      Cr  HDFC Bank
```

## The deliverable

**Q1 FY2026-27 26Q — reconciliation of annexure to challans (April slice):**

| Section | Deductees | TDS in annexure (Rs) |
|---|---|---:|
| 194C | CleanCo | 1,600 |
| 194J | S. Iyer & Co | 10,000 |
| 194H | Metro Sales | 1,000 |
| 194I | Prime Estates | 15,000 |
| 194Q | Seller X | 1,000 |
| **April total** | | **28,600** |
| **= April 26Q challan** | | **28,600** ✓ |

Filing outputs: **26Q .fvu + Form 27A + PRN**; **24Q .fvu + PRN**; **Form 16A** PDFs (5 vendors); **Form 16** ready for staff by 15 June 2027. Correction return filed; 234E fee paid.

## How it's checked

- **Challan-to-annexure tie:** sum of deductee TDS in each challan = challan amount (April Rs 28,600 = Rs 28,600). FVU won't validate otherwise.
- **CIN match:** the BSR/date/serial you keyed must match what the bank reported to OLTAS — a wrong BSR = **"challan mismatch"**, credit not passed.
- **PAN validity:** every deductee PAN must be valid and active; invalid PAN → deductee can't claim credit and you face 206AA exposure.
- **Cross-return consistency:** the TDS in Chapter 06's ledgers = 26Q; Chapter 05's 192 = 24Q. Books, challans and returns must all show the same numbers.
- **Form 16A source:** must be TRACES-generated (watermark + cert no.), not manual.
- **Deductee's AIS/26AS:** after processing, the vendor sees the credit — the ultimate proof it worked.

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---|---|---|
| Annexure total ≠ challan | FVU rejection | Map every deductee to a challan; reconcile |
| Wrong/invalid PAN | Credit denied; PAN-error default | Verify PANs before filing |
| Manual Form 16A | Invalid, not on 26AS | Download only from TRACES |
| Late return | **234E Rs 200/day** (non-waivable) + 271H penalty | File by 31 Jul / 31 Oct / 31 Jan / 31 May |
| Ignoring short-deduction notice | Interest compounds; demand outstanding | Pay + file correction return promptly |
| Annexure II skipped in Q4 | Form 16 Part B can't generate | File the salary detail annexure in Q4 24Q |

## On the job & in the interview

**The "why":** the challan proves tax was *paid*; the **return proves who it belongs to**. Only when the deductee's PAN is reported does their tax credit appear in their AIS/26AS so they can claim it. Form 16/16A is the deductee's certificate to file their own ITR. Miss the linkage and the vendor chases you because their credit is missing.

**Jargon:** *RPU/FVU* (prepare/validate), *Form 27A* (control sheet), *PRN/Token* (filing receipt), *TRACES* (the reporting/cert portal), *Justification Report* (the default listing), *234E* (late-fee), *271H* (penalty), *Annexure II* (Q4 salary breakup), *conso file* (consolidated file pulled from TRACES to prepare a correction).

**Interview Q&A:**

- *"What's the difference between 24Q and 26Q?"* → "24Q is salary TDS u/s 192 with an Annexure II salary computation in Q4 that feeds Form 16; 26Q is all non-salary TDS — 194C/J/H/I/Q — feeding Form 16A. Both are quarterly, both validated by FVU."
- *"A vendor says his TDS credit isn't showing in 26AS — how do you fix it?"* → "Check the deductee row in the filed 26Q: usually a wrong PAN or a challan-mismatch (BSR/serial). Pull the conso file from TRACES, file a correction return with the right PAN/CIN, and the credit flows to his AIS."
- *"The return is two days late — cost?"* → "Sec 234E late fee at Rs 200/day = Rs 400, capped at the TDS amount, and it can't be waived; plus possible 271H penalty. So we file 26Q/24Q by the quarterly due date every time."
