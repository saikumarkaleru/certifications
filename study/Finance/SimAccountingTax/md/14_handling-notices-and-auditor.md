# Handling a GST / Income-tax Notice and Working with the Auditor

## The situation

It's Monday, **17 August 2026**, 9:40 a.m. Three things landed on your desk before you'd finished your coffee:

1. An email from the **GST portal** — *"Notice for intimating discrepancies in the return after scrutiny — FORM GST ASMT-10"* for **NTSPL, GSTIN 36AABCN1234A1Z5**, tax period **April 2026**. The officer says the ITC claimed in GSTR-3B (Rs 12,78,000) exceeds the ITC auto-populated in GSTR-2B by **Rs 9,000**, and wants an explanation within 30 days, failing which proceedings under **Sec 73** (DRC-01) will follow.
2. A **CPC Bengaluru intimation u/s 143(1)** for **AY 2027-28** (you'd filed early) showing a **tax mismatch of Rs 46,000** — the return claimed TDS credit that the system says isn't fully reflected in Form 26AS.
3. Your director forwarding the **statutory auditor's engagement letter and PBC (prepared-by-client) request list** — the FY2026-27 audit fieldwork starts **1 September 2026**.

You're the Accounts/Tax Associate. All three are yours to run. A notice is not an accusation — it's a **question with a deadline**. Miss the deadline and the question becomes a demand.

## What you're given

**(a) The GST ASMT-10 discrepancy (April 2026):**

| Item | GSTR-3B (books) | GSTR-2B (portal) | Difference |
|---|---|---|---|
| ITC — CGST | 5,31,000 | 5,26,500 | 4,500 |
| ITC — SGST | 5,31,000 | 5,26,500 | 4,500 |
| ITC — IGST | 2,16,000 | 2,16,000 | 0 |
| **Total ITC** | **12,78,000** | **12,69,000** | **9,000** |

The Rs 9,000 gap is exactly the **book bill of Rs 40,000 + GST 7,200** you booked but which had **not yet appeared in 2B** — wait, check the math: 7,200 vs 9,000. Reconcile carefully below. (This is the trap: the officer nets two opposite errors.)

Two reconciling items from the April month-end:
- **Item A** — supplier bill Rs 50,000 + GST **Rs 9,000** is **in 2B but NOT in books** (you never claimed it — correctly excluded).
- **Item B** — book bill Rs 40,000 + GST **Rs 7,200** is **in books but NOT in 2B** (you claimed it early — should have deferred).

**(b) The 143(1) intimation (AY 2027-28):**

| Line | As filed (ITR) | As computed (CPC) | Diff |
|---|---|---|---|
| Total income | 1,50,60,000 | 1,50,60,000 | 0 |
| Tax + cess | 39,15,600 | 39,15,600 | 0 |
| TDS credit claimed | 4,50,000 | 4,04,000 | **46,000** |
| Net payable/(refund) | (35,000) refund | 11,000 payable | 46,000 |

**(c) The auditor's PBC list (extract):**

```
STATUTORY AUDIT FY2026-27 — PREPARED-BY-CLIENT LIST
1.  Signed trial balance 31-Mar-2027 (from TallyPrime)
2.  Bank statements + BRS for all accounts (HDFC xxxx4567)
3.  Fixed asset register + depreciation working (Rs 14,40,000)
4.  GST returns GSTR-1/3B/2B + annual reconciliation (turnover)
5.  TDS returns 24Q/26Q + Form 26AS + challans
6.  Payroll register, PF/ESI/PT challans
7.  Closing stock statement 31-Mar-2027 + valuation basis
8.  Confirmations: debtors, creditors, bank, loans
9.  Provisions schedule (audit fee, electricity, depreciation)
10. Related-party transactions + board minutes
```

## Do it — step by step

### (a) Reply to the GST ASMT-10

**Step 1 — Reconcile 3B to 2B line by line (don't argue, prove).** Build the bridge:

| Reconciling item | CGST | SGST | IGST |
|---|---|---|---|
| ITC per GSTR-3B (books) | 5,31,000 | 5,31,000 | 2,16,000 |
| Less: Item B claimed early, not in 2B (Rs 7,200, intra-state) | (3,600) | (3,600) | – |
| ITC that SHOULD equal 2B | 5,27,400 | 5,27,400 | 2,16,000 |
| ITC per 2B (portal) | 5,26,500 | 5,26,500 | 2,16,000 |
| Residual gap | 900 | 900 | 0 |

The residual **Rs 1,800** is Item A logic in reverse — a portal timing float. **Conclusion for the reply:** you over-claimed **Rs 7,200** (Item B — supplier hadn't filed his GSTR-1, so it wasn't in your 2B; Rule 36(4) requires ITC only to the extent reflected in 2B). You will **reverse Rs 7,200 with interest** and reclaim it in the month the supplier files. Item A (Rs 9,000 in 2B, not in books) you **never claimed** — no action, but you note it so the officer sees you're conservative.

**Step 2 — Reverse the excess ITC.** Pay via **DRC-03** (voluntary payment) or reverse in the next GSTR-3B Table 4(B). Interest u/s 50: 24% p.a. on wrongly availed & utilised ITC. Rs 7,200 × 24% × ~4 months (Apr claim → Aug reversal ≈ 120 days) = **Rs 7,200 × 24% × 120/365 = Rs 568**.

**Tally entry for the reversal (Accounting Voucher → F7 Journal):**

```
Dr  Input CGST reversal (ITC ineligible)   3,600
Dr  Input SGST reversal (ITC ineligible)   3,600
Dr  Interest on GST (indirect exp)           568
    Cr  Input CGST                                 3,600
    Cr  Input SGST                                 3,600
    Cr  Bank / Electronic cash ledger (DRC-03)       568
```

**Step 3 — Draft the ASMT-11 reply** on the portal (Services → User Services → View Additional Notices/Orders → Reply). Attach: (i) the reconciliation table above, (ii) the DRC-03 challan, (iii) a covering letter. Keep the tone factual: *"The difference of Rs 7,200 arose because supplier [X]'s invoice was booked in April 2026 but not reflected in GSTR-2B of that period as the supplier filed GSTR-1 late. Per Rule 36(4) NTSPL has reversed the ITC vide DRC-03 dated 17-Aug-2026 with interest u/s 50, and will re-avail on reflection in 2B. All other ITC ties to 2B."*

### (b) Fix the 143(1) TDS mismatch

The Rs 46,000 is TDS a customer **deducted on NTSPL's AMC receipts but hasn't deposited/filed** — so it's not in 26AS/AIS. **Do not blindly pay.** Steps:

1. Open the income-tax portal → e-Proceedings → the 143(1); check **Form 26AS + AIS** for the missing entry.
2. If the deductor simply filed late, wait for 26AS to update, then file a **rectification u/s 154** ("Reprocess the return") — the credit flows and the demand vanishes.
3. If the deductor won't file, chase them for the TDS certificate (Form 16A); you can only claim what's in 26AS. Meanwhile, either pay the Rs 11,000 under protest or file 154 with proof.
4. Respond on the portal within **30 days** — "Disagree with demand," attach 26AS extract and the deductor's Form 16A.

### (c) Run the statutory audit

**Get books audit-ready before Day 1.** Freeze the TallyPrime books, run **Display → Trial Balance**, and tie every schedule to it. The auditor's tests are predictable — anticipate them:

| Auditor test | What must tie |
|---|---|
| Revenue Rs 12,00,00,000 | GSTR-1 annual + Tally sales ledger + 26AS receipts |
| Purchases Rs 8,40,00,000 (COGS) | GSTR-2B + purchase ledger + stock movement |
| Closing stock Rs 45,00,000 (Apr) → year-end statement | Physical count + valuation (lower of cost/NRV) |
| Depreciation Rs 14,40,000 | Fixed asset register (Cos Act Sch II) |
| Provisions | Audit fee 25,000, electricity 40,000 accruals traced to invoices |
| TDS Rs 51,600/month | 26Q/24Q + challans + 26AS |

**Common auditor queries you pre-empt:** (i) *"Show the BRS."* — reconcile HDFC xxxx4567 to the book balance, list uncleared cheques. (ii) *"Provision for audit fee — is TDS u/s 194J provided?"* Yes, 10% on the year-end provision. (iii) *"Closing stock valuation basis?"* Lower of cost or NRV, FIFO. (iv) *"Related-party?"* Director's rent/loans disclosed per AS 18 / Sec 188.

## The deliverable

**1. ASMT-11 reply summary (filed 17-Aug-2026):**

| Field | Value |
|---|---|
| Notice ref (ASMT-10) | Tax period Apr-2026 |
| ITC discrepancy alleged | Rs 9,000 |
| Explained (Item A, never claimed) | Rs 9,000 — no demand |
| Accepted & reversed (Item B) | Rs 7,200 ITC + Rs 568 interest |
| Mode of payment | DRC-03 dated 17-Aug-2026 |
| Status | Discrepancy resolved; re-avail on 2B reflection |

**2. 143(1) response:** "Disagree with demand" filed; rectification u/s 154 lodged once 26AS updates → net **refund Rs 35,000** restored.

**3. Audit close:** clean TB, all PBC items delivered, queries closed. Auditor signs **3CB-3CD (tax audit, due 30-Sep-2026)** and the **Sec 143 statutory audit report**; company ITR-6 filed by **31-Oct-2027**.

## How it's checked

- **GST:** the range officer verifies your reversed ITC appears in Table 4(B) of the next GSTR-3B / DRC-03 challan; interest computed at 24% (utilised) not 18%. If the reconciliation ties, the ASMT proceeding is **dropped (no DRC-01)**.
- **Income-tax:** CPC reprocesses the 154; the demand is nil once 26AS shows the Rs 46,000. Your 26AS TDS credit must equal what you claimed in the ITR — **to the rupee**.
- **Audit:** the auditor ties **turnover (books) = GSTR-9 = 26AS**, purchases = 2B, TDS deducted = 26Q, and depreciation = FAR. Any un-reconciled difference becomes an **audit observation** or a **3CD qualification**.

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---|---|---|
| Paying the ASMT demand blindly without reconciling | Lose ITC you were entitled to (Item A) | Always build the 3B↔2B bridge first |
| Reversing at 18% interest instead of 24% | Officer raises differential; short payment | ITC **availed & utilised** wrongly = 24% u/s 50(3) |
| Ignoring the 30-day ASMT window | Escalates to DRC-01 / Sec 73 demand + penalty | Reply in ASMT-11 even if only partial |
| Paying the 143(1) demand instead of filing 154 | Lose a genuine refund | Check 26AS; rectify, don't pay |
| Handing the auditor an unfrozen Tally | Figures move mid-audit; re-work | Freeze books, take a signed TB, back up the company |
| No creditor/debtor confirmations | Audit qualification | Send balance confirmations early |

## On the job & in the interview

The **"why"**: a notice is a system flag, not a verdict. GST scrutiny is now algorithmic — the portal auto-compares 3B vs 2B and 1 vs 3B and throws ASMT-10s in bulk. Your job is to convert the flag into a **paper trail the officer can tick**. Same with 143(1): CPC is a matching engine, so 90% of intimations are TDS/26AS timing, fixed by rectification, not payment.

**Jargon to own:** ASMT-10 (scrutiny notice), ASMT-11 (reply), DRC-01 (show-cause/demand), DRC-03 (voluntary payment), Sec 73 (non-fraud demand), Rule 36(4) (2B-linked ITC), 143(1) (intimation), Sec 154 (rectification), PBC list, 3CB-3CD (tax audit report).

**Interview Q&A:**

*Q1: "You get an ASMT-10 saying your ITC exceeds 2B by Rs 9,000. Walk me through it."*
"I'd never pay first. I reconcile 3B to 2B line by line. Here the Rs 9,000 was actually two items netting — a Rs 9,000 bill in 2B I correctly didn't claim, and a Rs 7,200 bill I claimed early before it hit 2B. I reverse the Rs 7,200 via DRC-03 with 24% interest under Rule 36(4), re-avail when the supplier files, and file ASMT-11 with the reconciliation. That closes the proceeding without a DRC-01."

*Q2: "A 143(1) shows a demand because TDS credit was disallowed. Do you pay?"*
"No — first check 26AS and AIS. It's almost always the deductor filing late, so the credit isn't reflected yet. I file a rectification under Sec 154 to reprocess once 26AS updates, and respond 'disagree with demand' on the portal within 30 days with the Form 16A. Paying would mean forfeiting a genuine refund."

*Q3: "What's the first thing you do when the auditor arrives?"*
"Hand them a **frozen, signed trial balance** and the PBC pack — BRS, FAR, GST and TDS reconciliations, stock statement, confirmations. Everything must tie: turnover to GSTR-9 and 26AS, purchases to 2B, TDS to 26Q, depreciation to the fixed asset register. If it ties, the audit is queries, not qualifications."
