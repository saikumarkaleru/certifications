# ITR Filing & Tax Audit

## What it is & where it's used

Income Tax Return (ITR) filing is the annual act of reporting a taxpayer's income, deductions, and tax paid to the Income Tax Department, and squaring off the balance (refund or demand). Tax audit under **Section 44AB** is the statutory examination of a business/profession's books by a Chartered Accountant, reported in **Form 3CA/3CB + 3CD**, that must be completed before the ITR of an audited assessee is filed.

Every finance function touches this:

| Role | What they do with ITR/tax audit |
|---|---|
| Accounts executive | Assembles the trial balance, ledgers, TDS/26AS reconciliation feeding the return |
| Tax associate (CA firm / Big 4) | Prepares 3CD annexures, drafts returns for clients, uploads on portal |
| Finance manager / controller | Signs off on tax provision, coordinates the statutory + tax audit close |
| Payroll / HR finance | Issues Form 16, ensures salary TDS matches employee ITRs |
| Founder / freelancer | Files own ITR-3/ITR-4, decides presumptive vs. audit |

If you are hired into any accounts or tax seat in India, July–September (the return + audit season) is the busiest, highest-visibility part of your year. Knowing the mechanics cold makes you immediately useful.

## The gap: why companies want this (and college didn't teach it)

An MBA teaches you what taxable income *is*. It does not teach you:

- **Which of the seven ITR forms** actually applies to a given fact pattern, and why using the wrong one gets the return treated as defective (Section 139(9)).
- How to **reconcile Form 26AS, AIS (Annual Information Statement), and TIS** against the books before you touch a return — the single most common real-world task.
- The **exact turnover thresholds** that trigger tax audit, and the trap in the 5% cash-transaction rule.
- How to fill **Clause 21 (disallowances), Clause 26 (Section 43B), Clause 34 (TDS compliance)** of Form 3CD — the clauses that consume 80% of audit time.
- The **portal click-path**: DSC registration, JSON utility, UDIN, CA-assignee acceptance workflow.

Colleges test theory in a vacuum. Employers pay for someone who can take a messy Tally backup and produce a filed, defensible return without supervision. That end-to-end capability is the gap.

## What "proficient" looks like

A job-ready person can, unaided:

1. Pick the **correct ITR form** for salary, capital gains, business, presumptive, or company income.
2. Download and **reconcile 26AS + AIS** to the books, flagging every mismatch with a reason.
3. Determine **tax-audit applicability** in under two minutes given turnover, profession, and cash ratios.
4. Populate **Form 3CD clause-by-clause** from a trial balance and supporting schedules.
5. Compute **total income, tax, interest under 234A/B/C**, and know whether it's a refund or payable.
6. Generate **UDIN**, get the audit report accepted by the assessee, and file the ITR before the due date.

## Hands-on: how to actually do it

### Step 1 — Pick the ITR form

| Form | Who files it |
|---|---|
| ITR-1 (Sahaj) | Resident individual, income ≤ ₹50L: salary, one house property, other sources |
| ITR-2 | Individual/HUF with capital gains, >1 house, foreign assets — **no business income** |
| ITR-3 | Individual/HUF with **business/professional income** (incl. F&O, intraday) |
| ITR-4 (Sugam) | Presumptive income u/s 44AD/44ADA/44AE, turnover ≤ ₹2 crore |
| ITR-5 | Firms, LLPs, AOP, BOI |
| ITR-6 | Companies (other than those claiming 11 exemption) |
| ITR-7 | Trusts, political parties, u/s 139(4A)–(4D) |

### Step 2 — Reconcile 26AS / AIS to books (the daily task)

Pull TDS from 26AS and match to your books. In Excel:

```
=XLOOKUP(A2, TDS_26AS[TAN], TDS_26AS[TaxDeducted], 0)          // TDS as per 26AS for each party
=B2 - C2                                                        // Books TDS minus 26AS TDS
=IF(ABS(D2)<1, "Match", IF(D2>0,"Short in 26AS","Excess in 26AS"))
```

Reconcile receipts against AIS SFT entries:

```python
import pandas as pd
books = pd.read_excel("sales_ledger.xlsx")          # party, invoice, amount
ais   = pd.read_excel("ais_export.xlsx")            # party, reported_amount

recon = books.merge(ais, on="party", how="outer", suffixes=("_books","_ais"))
recon["diff"] = recon["amount"].fillna(0) - recon["reported_amount"].fillna(0)
recon["flag"] = recon["diff"].apply(lambda d: "OK" if abs(d) < 1 else "INVESTIGATE")
recon.to_excel("ais_recon.xlsx", index=False)
```

### Step 3 — Test tax-audit applicability (Section 44AB)

```python
def tax_audit_required(turnover, cash_receipts_pct, cash_payments_pct,
                       is_profession, gross_receipts_prof,
                       opted_presumptive=False, declared_below_presumptive=False):
    if is_profession:
        if gross_receipts_prof > 50_00_000:          # 44AB(b): ₹50 lakh
            return "Audit required (profession)"
    else:
        # Business: ₹1 cr default; ₹10 cr if cash <=5% both ways
        if cash_receipts_pct <= 5 and cash_payments_pct <= 5:
            limit = 10_00_00_000
        else:
            limit = 1_00_00_000
        if turnover > limit:
            return f"Audit required (business, limit ₹{limit:,})"
    if declared_below_presumptive and turnover > 0:  # 44AB(e)
        return "Audit required (declared below presumptive)"
    return "No audit required"

print(tax_audit_required(9_50_00_000, 3, 4, False, 0))   # -> No audit (₹10cr limit)
print(tax_audit_required(1_20_00_000, 40, 30, False, 0)) # -> Audit required (₹1cr)
```

### Step 4 — Choose the audit report form

- **Form 3CA** — accounts already audited under another law (Companies Act, LLP Act). CA just annexes 3CD.
- **Form 3CB** — accounts NOT audited under any other law (proprietor, most partnerships). CA gives an opinion + annexes 3CD.
- **Form 3CD** — the 44-clause statement of particulars, annexed to *both* 3CA and 3CB.

### Step 5 — Key Form 3CD clauses (where time goes)

| Clause | What it captures |
|---|---|
| 12 | Presumptive income (44AD/44ADA etc.) |
| 16 | Amounts not credited to P&L |
| 21(a) | Personal/capital/penalty expenses disallowed |
| 21(b) | Disallowance u/s 40(a) — TDS not deducted/paid |
| 26 | Section 43B — statutory dues paid vs. outstanding |
| 27 | CENVAT/GST credit, prior-period items |
| 31 | Loans/deposits u/s 269SS/269T (cash > ₹20,000) |
| 34 | TDS/TCS compliance — deducted, deposited, return filed |

### Step 6 — Journal for the tax provision

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Income Tax Expense (P&L) | 3,60,000 | |
| &nbsp;&nbsp;To Provision for Tax | | 3,60,000 |
| *(Being provision for current tax created)* | | |
| Advance Tax Paid A/c | 2,80,000 | |
| TDS Receivable A/c | 60,000 | |
| &nbsp;&nbsp;To Bank | | 2,80,000 |
| Provision for Tax | 3,60,000 | |
| &nbsp;&nbsp;To Advance Tax Paid | | 2,80,000 |
| &nbsp;&nbsp;To TDS Receivable | | 60,000 |
| &nbsp;&nbsp;To Provision — Balance Payable | | 20,000 |

## Worked example / mini-project

**Client:** Sharma Traders (proprietor, wholesale). FY 2025-26.

| Item | Amount (₹) |
|---|---|
| Turnover (all digital) | 3,40,00,000 |
| Cash receipts | 4,20,000 (1.2%) |
| Cash payments | 6,80,000 (2.0%) |
| Net profit as per books | 24,50,000 |
| Depreciation (books) | 3,10,000 |
| Depreciation (Income Tax Act) | 3,85,000 |
| Interest to bank paid before due date | 1,20,000 |
| GST payable outstanding on 30 Sep (43B) | 90,000 |

**1. Audit applicability:** cash both ≤ 5% → limit is ₹10 cr. Turnover ₹3.4 cr < ₹10 cr → **no 44AB audit** unless declaring below 44AD's 6%/8% presumptive. Profit ₹24.5L is 7.2% of turnover, above 6% → **no audit**. Suppose the client instead declares only ₹18L (5.3%) → **audit triggered under 44AB(e)**.

**2. Assume audit applies. Compute business income:**

```
Net profit per books                    24,50,000
Add: Book depreciation                  +3,10,000
Less: Tax depreciation                  -3,85,000
Add: GST unpaid u/s 43B (Clause 26)      +90,000
------------------------------------------------
Business income                         24,65,000
```

**3. Tax (individual, new regime, FY25-26 slabs):**

```
Income                 24,65,000
Tax:
  0–4L    : 0
  4–8L    : 5% x 4L      = 20,000
  8–12L   : 10% x 4L     = 40,000
  12–16L  : 15% x 4L     = 60,000
  16–20L  : 20% x 4L     = 80,000
  20–24.65L:25% x 4.65L  = 1,16,250
  Total tax             = 3,16,250
  +4% cess              = 12,650
  Total liability       = 3,28,900
```

**4. Interest 234B/C** applies if advance tax < 90% paid — compute and add. **5. Reconcile TDS credit from 26AS, adjust, arrive at payable/refund. 6.** CA generates **UDIN**, uploads 3CB-3CD, client accepts, then ITR-3 is filed.

Reproduce this in a spreadsheet: one tab for book-to-tax adjustments, one for the slab calc using nested `IF`/`SUMPRODUCT`, one for the 3CD Clause 26 schedule.

## How it's tested

**Interview questions:**
- "Turnover is ₹8 crore, 100% digital — is tax audit required?" (No, ₹10 cr limit.)
- "Client is a doctor with ₹55L receipts — which form, is audit needed?" (ITR-3; audit yes, > ₹50L.)
- "Difference between 3CA and 3CB?"
- "What is Clause 34 and why does it matter?" (TDS compliance; drives 40(a)(ia) disallowance.)
- "What is UDIN and when is it generated?"

**Practical assessment:** Firms hand you a **Tally backup + 26AS PDF** and a laptop, and ask you to (a) prepare the tax-audit computation, (b) fill a blank 3CD in the utility, and (c) tell them the tax payable — timed, 60–90 minutes. Big 4 tax teams also give a **book-to-tax reconciliation case** in Excel. Expect a short "spot the disallowance" test on a sample P&L.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Wrong ITR form (ITR-1 with capital gains) → defective u/s 139(9) | Map income sources to the form table first |
| Ignoring AIS/TIS, filing only on books | Always download AIS; reconcile before filing |
| Filing ITR before uploading & accepting the audit report | Sequence: 3CB-3CD → UDIN → assessee acceptance → then ITR |
| Missing UDIN within 60 days | Generate UDIN at report signing, not later |
| Treating the ₹10 cr limit as automatic | It needs BOTH cash receipts and payments ≤ 5% |
| Forgetting 43B add-back for unpaid statutory dues | Reconcile GST/PF/ESI paid vs. outstanding at year-end |
| Not reporting 40(a)(ia) TDS defaults in Clause 34/21(b) | Cross-check TDS returns to expense ledgers |

## Learn-it roadmap & resources

**Time to job-ready: 8–12 weeks** of focused practice alongside CA Inter tax study.

- **Weeks 1–2:** ITR form selection, heads of income, new vs. old regime slabs.
- **Weeks 3–4:** 26AS/AIS reconciliation in Excel; file 3–4 dummy ITR-1/ITR-2 on the portal's offline JSON utility.
- **Weeks 5–8:** Section 44AB applicability drills; fill 3CD clause-by-clause on sample data.
- **Weeks 9–12:** Full mock — Tally backup to filed ITR-3 with 3CB-3CD.

**Resources (free):** Income Tax portal (incometax.gov.in) — offline utilities, FAQs; ICAI *Guidance Note on Tax Audit u/s 44AB*; department's YouTube how-to-file videos; ClearTax and Tax Guru blogs for worked examples. **Paid:** any CA-firm articleship (the real training ground), Udemy "Income Tax Return Filing" practical courses. **Certification:** the **CA qualification** itself authorizes signing tax audits; CA Inter + articleship experience is what employers screen for.

## Quick-reference

| Trigger | Threshold |
|---|---|
| Business tax audit (default) | Turnover > ₹1 crore |
| Business tax audit (cash ≤ 5% both ways) | Turnover > ₹10 crore |
| Profession tax audit | Gross receipts > ₹50 lakh |
| Presumptive business (44AD) | Turnover ≤ ₹2 crore, deem 6% (digital)/8% (cash) |
| Presumptive profession (44ADA) | Receipts ≤ ₹75 lakh, deem 50% |
| 269SS/269T cash loan limit | ₹20,000 |

**Form map:** 3CA = accounts audited elsewhere · 3CB = not audited elsewhere · 3CD = 44-clause annexure (always).

**Filing sequence:** Books close → 26AS/AIS reconcile → 3CB-3CD prepared → **UDIN** → CA uploads → assessee accepts → **ITR filed**.

**Key clauses:** 21(b) = TDS disallowance · 26 = 43B dues · 31 = cash loans · 34 = TDS compliance.

**Due dates (typical):** Non-audit ITR — 31 Jul · Tax audit report — 30 Sep · Audited ITR — 31 Oct.

**Interest:** 234A (late filing) · 234B (< 90% advance tax) · 234C (deferment of instalments) — all @ 1% p.m.
