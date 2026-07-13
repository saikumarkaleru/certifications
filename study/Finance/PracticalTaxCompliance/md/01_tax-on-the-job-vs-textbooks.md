# Tax on the job vs textbooks

## What it is & where it's used

A tax/compliance role is not "knowing the Income-tax Act." It is running a **recurring machine** that takes raw business transactions, classifies them correctly, computes the right tax, files the right return before a legal deadline, pays the money, and keeps proof — every single month, forever. The Act is the rulebook; the job is operating the assembly line.

Where this sits in real org charts:

| Role | What tax/compliance work looks like day-to-day |
|---|---|
| Accounts Executive (SME / startup) | Files GSTR-1 and GSTR-3B, deposits TDS, reconciles GSTR-2B vs purchase register in Excel |
| Tax Analyst (mid/large corp) | Owns a compliance calendar, prepares TDS returns (26Q/24Q), advance-tax workings, litigation trackers |
| Big-4 / consulting associate | Same mechanics but across many clients; automates recons in Excel/Power Query |
| AP/AR & Controller-track | Ensures every vendor invoice has correct GST + TDS *before* payment, so books close clean |
| Global finance (US/EU/APAC) | Sales-tax/VAT filings, withholding, statutory reporting — different rates, identical *rhythm* |

The common thread across geographies: **deadlines are the product.** A brilliant computation filed one day late is a failure; a mediocre computation filed on time and later revised is normal.

## The gap: why companies want this (and college didn't teach it)

Your MBA and CA-Inter taught you **how tax is computed** — slab rates, Section 40(a)(ia) disallowance, input tax credit eligibility, the theory of "supply." That knowledge is necessary and assumed. Nobody pays you for it, because it's in every textbook and now in every LLM.

What college did **not** teach, and what the company is actually buying:

- **The calendar mindset.** Textbooks are organized by *concept* (chapter on TDS, chapter on GST). Work is organized by *date* (7th = TDS deposit, 11th = GSTR-1, 20th = GSTR-3B). The unit of work is a deadline, not a topic.
- **Reconciliation, not computation.** 80% of the job is matching two lists that should agree but don't — books vs GST portal, TDS deducted vs Form 26AS, vendor invoice vs GSTR-2B. Textbooks never show two lists.
- **Documentation & audit trail.** The answer isn't "₹1,80,000 TDS." It's "₹1,80,000, here is the challan CIN, here is the working, here is who approved it."
- **Tooling.** Real tax runs on Excel, TallyPrime/SAP, the GST and TRACES portals, and increasingly Power Query/SQL — none of which appear in a syllabus.

Employers see thousands of candidates who can quote a section and zero who can hand back a clean reconciliation by 5 PM. That scarcity is your paycheck.

## What "proficient" looks like

The concrete bar. A job-ready person can, **unaided**:

1. Take a month's sales and purchase data in Excel and produce a GSTR-3B summary (output tax, eligible ITC, net payable) with formulas, not by hand.
2. Reconcile the purchase register against GSTR-2B and produce a list of mismatched invoices with the *reason* (missing, wrong GSTIN, wrong amount, wrong period).
3. Compute TDS on a batch of vendor invoices, pick the correct section (194C vs 194J vs 194Q), and generate the deposit figure per section.
4. Read a compliance calendar and, on any given day, say what is due and whether it's done.
5. Pass a payment for release only after confirming GST is claimable and TDS is deducted — i.e., protect the company from disallowance.

If you can do these five, you clear the practical test for almost any India accounts/tax role.

## Hands-on: how to actually do it

### 1. Build the compliance calendar (the core artifact)

This is the single most job-defining table. Memorize its shape.

| Due date | Compliance | Form | Period | Applies to |
|---|---|---|---|---|
| 7th | TDS/TCS deposit | Challan ITNS-281 | Prev. month | All deductors (7th, but 30 Apr for March) |
| 11th | GST outward supplies | GSTR-1 | Prev. month | Monthly filers |
| 13th | GST outward (QRMP) | IFF | Prev. month | Quarterly filers |
| 20th | GST summary + payment | GSTR-3B | Prev. month | Monthly filers |
| 25th | GST payment (QRMP) | PMT-06 | Prev. month | Quarterly filers |
| 15th (Jun/Sep/Dec/Mar) | Advance tax | Challan 280 | Quarter | Companies & taxpayers |
| 31 Jul (Q1)/31 Oct/31 Jan/31 May | TDS return | 24Q/26Q | Quarter | Deductors |

Excel formula to flag what's due and overdue against today's date:

```excel
=IF([@Done]="Yes","✔ Done",
   IF([@DueDate]<TODAY(),"⚠ OVERDUE",
     IF([@DueDate]<=TODAY()+3,"DUE SOON","")))
```

Days remaining, with weekend awareness:

```excel
=NETWORKDAYS(TODAY(),[@DueDate])-1
```

### 2. TDS section picker (stop guessing)

```excel
=XLOOKUP([@Nature], Sections[Nature], Sections[Section], "REVIEW")
```

TDS amount with threshold logic (194J professional, threshold ₹30,000, rate 10%):

```excel
=IF([@YTDPayment]+[@Invoice] > 30000, ROUND([@Invoice]*10%, 0), 0)
```

### 3. GST output tax and net payable

```excel
Output tax   =SUMIFS(Sales[TaxAmt], Sales[Type],"Taxable")
Eligible ITC =SUMIFS(Purch[TaxAmt], Purch[ITCEligible],"Yes")
Net payable  =MAX(OutputTax-EligibleITC, 0)
```

### 4. GSTR-2B reconciliation (the interview favourite) — Power Query merge

Load `PurchaseRegister` and `GSTR2B` as tables, then in Power Query:

```
= Table.NestedJoin(PurchaseRegister, {"GSTIN","InvNo"},
                   GSTR2B, {"GSTIN","InvNo"},
                   "Match", JoinKind.LeftOuter)
```

Expand, then classify:

```excel
=IF([@Match]="","Not in 2B - hold ITC",
   IF(ROUND([@BookTax],0)<>ROUND([@2BTax],0),"Value mismatch","Matched"))
```

### 5. The journal entries you'll actually pass

Vendor bill with GST input and TDS deducted (professional fee ₹1,00,000 + 18% GST, TDS @10%):

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Professional Fees (expense) | 1,00,000 | |
| Input CGST | 9,000 | |
| Input SGST | 9,000 | |
| To Vendor A/c | | 1,08,000 |
| To TDS Payable (194J) | | 10,000 |

On depositing TDS:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| TDS Payable (194J) | 10,000 | |
| To Bank | | 10,000 |

### 6. TallyPrime / portal click-paths

- **Record GST purchase:** Gateway of Tally → Vouchers → F9 (Purchase) → select party → item → GST ledgers auto-populate if configured.
- **File GSTR-1:** Gateway → Display More Reports → GST Reports → GSTR-1 → export JSON → gst.gov.in → Returns Dashboard → select period → GSTR-1 → upload JSON → Submit → File with DSC/EVC.
- **Deposit TDS:** incometax.gov.in → e-Pay Tax → select 281 → Company/Non-company, section code → pay → save challan CIN.

## Worked example / mini-project

**Scenario:** You run compliance for *Nova Traders Pvt Ltd*, June 2026.

Sales (all intra-state, 18%):

| Invoice | Taxable (₹) | GST (₹) |
|---|---|---|
| S-101 | 5,00,000 | 90,000 |
| S-102 | 3,00,000 | 54,000 |
| **Total** | **8,00,000** | **1,44,000** |

Purchases:

| Invoice | Taxable (₹) | GST (₹) | In GSTR-2B? |
|---|---|---|---|
| P-201 (goods) | 4,00,000 | 72,000 | Yes |
| P-202 (services) | 1,00,000 | 18,000 | No |

**Step 1 — ITC:** Only invoices reflected in GSTR-2B are claimable (Rule 36(4)/Sec 16). P-202 is not in 2B → hold ₹18,000. Eligible ITC = **₹72,000**.

**Step 2 — GSTR-3B net GST:** Output 1,44,000 − ITC 72,000 = **₹72,000 payable** by 20 Jul via GSTR-3B; pay via PMT-06/cash ledger.

**Step 3 — TDS:** P-202 is a professional service, ₹1,00,000 > ₹30,000 threshold → 194J @10% = **₹10,000 TDS** to deposit by 7 Jul (Challan 281). Vendor is paid ₹1,08,000 − ₹10,000 = ₹98,000.

**Step 4 — Calendar check on 5 Jul:**

| Due | Task | Status |
|---|---|---|
| 7 Jul | Deposit TDS ₹10,000 | DUE SOON |
| 11 Jul | File GSTR-1 (₹8,00,000 sales) | Pending |
| 20 Jul | GSTR-3B, pay ₹72,000 | Pending |

Reproduce this in one Excel sheet: a Sales tab, a Purchase tab with an "In2B" column, and a Calendar tab using the flag formula above. That workbook *is* a portfolio piece.

## How it's tested

**Interview questions (verbal):**
- "Walk me through the GST monthly compliance cycle and every due date."
- "A vendor invoice is in your books but not in GSTR-2B. What do you do?"
- "Difference between 194C, 194J and 194Q — and which rate?"
- "What happens if you deduct TDS but pay the vendor without depositing it?" (Answer: 30% expense disallowance u/s 40(a)(ia) until deposited.)

**Practical/assessment tests (what actually decides it):**
- **Timed Excel test (30–45 min):** Given a raw sales+purchase dump, produce GSTR-3B output tax, eligible ITC, and net payable using formulas. They watch whether you use `SUMIFS`/`XLOOKUP` or manually add — manual = reject.
- **The reconciliation case:** Two files (purchase register + GSTR-2B) that don't tie. Deliver a mismatch list with reasons. This is the single most common practical screen.
- **"Close the month" case:** A trial balance and a stack of pending items; book the TDS/GST provisions and hand back a clean set.

## Common mistakes & how pros avoid them

| Mistake | How pros avoid it |
|---|---|
| Claiming ITC not in GSTR-2B | Reconcile 2B **before** filing 3B; hold unmatched ITC, don't claim on faith |
| Paying vendor before deducting TDS | Gate: no payment released until TDS field is filled — protects against 40(a)(ia) |
| Treating tax as a computation, not a calendar | Maintain a live calendar; the deadline is the deliverable |
| No documentation | Save every challan CIN, ARN, and working; "trust me" fails an audit |
| Hard-coding rates in cells | Keep a rate/section master table and `XLOOKUP` into it — one place to update |
| Manual copy-paste recon | Use Power Query merge; it's repeatable and leaves an audit trail |
| Missing the March exception | TDS for March is due **30 April**, not 7 April |

## Learn-it roadmap & resources

**Realistic time-to-proficiency: 8–12 weeks** of deliberate practice alongside study.

- **Weeks 1–2:** Build the compliance calendar from scratch in Excel. Learn `SUMIFS`, `XLOOKUP`, `NETWORKDAYS`, `IF`.
- **Weeks 3–4:** GST mechanics hands-on — free-play in the [GST portal sandbox](https://www.gst.gov.in), file dummy GSTR-1/3B. Read CBIC's GST flyers.
- **Weeks 5–6:** TDS — sections, thresholds, TRACES portal, Form 26AS reading. Deposit a test challan on the income-tax portal.
- **Weeks 7–8:** Power Query reconciliation; automate the 2B match.
- **Weeks 9–12:** Do the mini-project monthly with fresh numbers; add TallyPrime.

**Resources:**
- Free: CBIC GST portal help, income-tax e-filing portal guides, ClearTax/TaxGuru blogs, ICAI study material (you already have it).
- Paid/high-ROI: TallyPrime with GST certificate; ClearTax or Zoho Books trial for hands-on filing; Microsoft Excel/Power Query courses.
- Certifications that signal job-readiness: **TallyPrime GST**, ICAI's practical GST/TDS courses, and your CA-Inter itself.

## Quick-reference

**Due dates (monthly filer):** TDS deposit 7th · GSTR-1 11th · GSTR-3B 20th · TDS return end of month after quarter · Advance tax 15 Jun/Sep/Dec/Mar.

**Key TDS sections:**

| Section | Nature | Rate | Threshold (₹) |
|---|---|---|---|
| 194C | Contractor | 1% (ind/HUF) / 2% | 30,000 single / 1,00,000 aggregate |
| 194J | Professional/technical | 10% (2% technical) | 30,000 |
| 194Q | Purchase of goods | 0.1% | 50,00,000 |
| 194H | Commission/brokerage | 5% | 15,000 |

**Core formulas:**
```excel
=XLOOKUP(nature, Sections[Nature], Sections[Section], "REVIEW")
=SUMIFS(Sales[Tax], Sales[Type],"Taxable")
=MAX(OutputTax-EligibleITC,0)
=IF([@Done]="Yes","✔",IF([@Due]<TODAY(),"OVERDUE",""))
```

**Golden rules:** ITC only if in GSTR-2B · Deduct TDS before paying vendor · The deadline is the deliverable · Keep the challan/ARN as proof.
