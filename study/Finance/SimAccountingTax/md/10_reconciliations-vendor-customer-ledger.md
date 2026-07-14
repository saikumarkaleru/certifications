# Reconciliations: Vendor, Customer, Inter-company and Ledger Scrutiny

## The situation

It's **6 May 2026**. April is closed and the audit-readiness checklist lands on your desk. Item one: *"Reconcile the top vendor and customer ledgers to their statements before we lock the month. I don't want surprises in September when the auditors confirm balances."*

A reconciliation answers one question: **does our ledger of a party agree with their ledger of us, and if not, why?** Every genuine difference must be explained by a **timing item** (in transit) or fixed by a **correcting entry** (a real error). Balance confirmations, TDS-in-their-books, unadjusted advances, and missed debit/credit notes are the usual suspects. Get this right and year-end audit confirmations (AABCN1234A's books vs third parties) tie out cleanly.

## What you're given

**A. Vendor: "Spark Components LLP" (a goods supplier).** Their **Statement of Account** to 30-Apr-2026 vs NTSPL's ledger (Gateway of Tally → Display → Account Books → Ledger → Spark Components LLP):

| Date | Particulars | Per Spark (their books) | Per NTSPL (our books) |
|---|---|---|---|
| Opening 01-Apr | | 3,20,000 Cr (we owe) | 3,20,000 Cr |
| 05-Apr | Invoice SP/441 goods | 5,90,000 Cr | 5,90,000 Cr |
| 12-Apr | Invoice SP/460 goods | 2,36,000 Cr | **not recorded** |
| 18-Apr | Our payment (NEFT) Rs 3,20,000 | **not recorded** | 3,20,000 Dr |
| 22-Apr | Credit note CN/12 (rate diff) Rs 18,000 | 18,000 Dr | **not recorded** |
| 28-Apr | TDS 194C by NTSPL on their labour bill | **not recorded** | 1,600 Dr |
| **Closing 30-Apr** | | **8,08,000 Cr** | **5,88,400 Cr** |

**B. Customer: "Deccan Industrial Pvt Ltd".** Their books show they owe us **Rs 4,10,000**; our ledger shows **Rs 4,72,000** receivable. Known items: a Rs 55,000 sales return (our credit note NT-CR/2627/03) they've booked but we posted to the wrong customer; and Rs 7,000 TDS **they** deducted u/s 194 on… (they wrongly treated our sale as a service and deducted — a dispute to resolve).

**C. Inter-company:** NTSPL has a sister concern "Nirvana Logistics"; NTSPL books **Rs 90,000 payable** for freight, sister books **Rs 90,000 receivable** — must match to the rupee on consolidation.

## Do it — step by step

**Step 1 — Fix the reference point.** Both parties should reconcile to the **same cut-off (30-Apr-2026)** and same currency of balance (we show them as a **creditor/Cr**; they show us as a **debtor**). A vendor's "you owe 8,08,000" should mirror our "we owe 8,08,000" once reconciled.

**Step 2 — Classify each difference** as *timing* (will self-clear) or *error* (needs a correcting entry):

| Reconciling item | Amount | Cause | Type | Action |
|---|---|---|---|---|
| Invoice SP/460 not in our books | 2,36,000 | Purchase not booked | **Error** | Book the purchase + ITC |
| Our 18-Apr payment not in their books | 3,20,000 | In transit at their end | Timing | They'll post; note only |
| Credit note CN/12 not in our books | 18,000 | Missed rate-diff credit | **Error** | Book the credit note |
| TDS 194C Rs 1,600 not in their books | 1,600 | They see it as a receivable from govt | Timing/normal | They reconcile via 26AS |

**Step 3 — Build the vendor reconciliation (bridge one balance to the other).** Start from **our** closing 5,88,400 Cr and bridge to **their** 8,08,000 Cr:

| | Amount (Cr +) |
|---|---|
| Balance per NTSPL books | 5,88,400 |
| Add: invoice SP/460 not yet booked by us | 2,36,000 |
| Less: credit note CN/12 not yet booked by us | (18,000) |
| Add back: TDS 1,600 we netted but they haven't (they'll claim via 26AS) | 1,600 |
| **Adjusted per our books** | **8,08,000** |
| Balance per Spark statement | **8,08,000** ✓ |

The Rs 3,20,000 payment is **in transit** at Spark's end — it's their reconciling item, not ours, so it doesn't feature in bridging *our* balance up to *theirs*.

**Step 4 — Post the correcting entries (TallyPrime → Accounting Vouchers → F9 Purchase / F7 Journal):**

```
Book missed purchase SP/460 (F9 Purchase voucher):
  Dr  Purchases – Goods            2,00,000
  Dr  Input CGST @9%                  18,000
  Dr  Input SGST @9%                  18,000
      Cr  Spark Components LLP        2,36,000

Book missed credit note CN/12 (rate difference) (F7/credit note):
  Dr  Spark Components LLP            18,000
      Cr  Purchases – Goods            15,254
      Cr  Input CGST @9%                1,373
      Cr  Input SGST @9%                1,373
```

After these two, our ledger reads **8,08,000 Cr** — matched (the TDS Rs 1,600 was already correctly deducted and is a genuine timing item they clear via their Form 26AS).

**Step 5 — Customer reconciliation (Deccan).** Difference = 4,72,000 (ours) − 4,10,000 (theirs) = **Rs 62,000**, explained by: (a) **Rs 55,000** credit note we mis-posted to another customer — *our error*: reverse and re-post to Deccan (Dr Sales Return/Output GST, Cr Deccan); (b) **Rs 7,000** TDS they deducted — since our supply is **goods** (194Q is the buyer's duty, not a 194 deduction on us), their deduction is **wrong**; raise it with them to reverse, or reconcile once it shows in **our 26AS** as credit. After (a), our balance drops to 4,17,000; the residual 7,000 is the disputed TDS.

**Step 6 — Inter-company match.** Confirm NTSPL Rs 90,000 payable = Nirvana Logistics Rs 90,000 receivable, same period, same amount. If a debit/credit note or freight accrual sits on one side only, pass the mirror entry so consolidation eliminates cleanly (Dr Inter-co payable / Cr Inter-co receivable nets to zero).

**Step 7 — Ledger scrutiny (catch mispostings).** Gateway → Display → Account Books → Ledger → scan each control account for the odd entry: a purchase hitting "Repairs," a capital asset expensed, a personal expense in "Miscellaneous," a debit in a normally-credit vendor account. Fix via F7 Journal with a clear narration.

## The deliverable — vendor reconciliation statement

**Spark Components LLP — Reconciliation as at 30-Apr-2026**

| Particulars | Dr | Cr |
|---|---|---|
| Balance per NTSPL books (before fix) | | 5,88,400 |
| Add: Invoice SP/460 not booked | | 2,36,000 |
| Less: Credit note CN/12 not booked | 18,000 | |
| Adjust: TDS 194C (timing, at their end) | | 1,600 |
| **Balance per NTSPL (after correcting entries)** | | **8,08,000** |
| **Balance per Spark statement** | | **8,08,000** |
| **Difference** | | **NIL** ✓ |

**Reconciling items still open (timing, no entry needed by us):** payment Rs 3,20,000 in transit at Spark; TDS Rs 1,600 they clear via 26AS.

## How it's checked

- **Zero unexplained difference:** every rupee of gap is either a booked correction or a labelled timing item with an expected clearing date.
- **Balance confirmation:** at year-end, a signed confirmation from Spark stating **Rs 8,08,000** (or the then balance) must equal our ledger — the audit tie-out.
- **GST link:** the missed purchase (SP/460) ITC of Rs 3,600 flows into the **next** GSTR-2B recon — it must be in 2B before we claim.
- **TDS link:** amounts we deducted (Rs 1,600 194C) must appear in **our** 26Q and the vendor's 26AS; TDS others deducted on us must land in **our** 26AS.
- **Inter-company:** payable and receivable net to nil on consolidation.

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---|---|---|
| Netting TDS wrong — treating deductee TDS as a payment | Vendor balance won't tie; double-count | TDS deducted reduces payable but is a govt liability, not a payment to them |
| Ignoring in-transit items and force-posting | Fake entries, next-month reversal chaos | Label timing items; don't post them |
| Mis-posting a credit note to the wrong party | Two customers wrong, receivables misstated | Reverse and re-post; scrutinise CN allocations |
| Missing a supplier invoice at cut-off | Understated creditors + lost ITC | Book on reconciliation; check 2B follow-through |
| Never obtaining balance confirmations | Audit qualification; undetected fraud | Send confirmations for top parties quarterly |

## On the job & in the interview

Reconciliation is the accountant's lie-detector: it forces two independent records to agree, and every disagreement is either a timing truth or an error to fix. On the job you'll reconcile top vendors/customers monthly, banks daily-to-weekly, and inter-company before every consolidation. The discipline — *classify, bridge, correct, confirm* — is identical everywhere.

**Q: "Vendor statement shows Rs 8,08,000, your books show Rs 5,88,400. Walk me through it."**
A: I list every difference and tag it timing or error. Here two are our errors — an unbooked invoice (2,36,000) and a missed credit note (18,000) — which I post. The Rs 3,20,000 payment is in transit at their end (their reconciling item), and the Rs 1,600 TDS I deducted is a timing item they clear via 26AS. After my two entries, our balance is 8,08,000 — matched.

**Q: "A customer deducted TDS on a pure goods sale. Is that right?"**
A: No — TDS under 194 doesn't apply to a sale of goods; the buyer's obligation on goods is **194Q** (0.1% over Rs 50L), and that's a deduction *the buyer* self-reports, not something that reduces our invoice as a "TDS on us" in the normal way. I'd flag it, ask them to reconcile, and if they've genuinely deposited it, claim the credit once it appears in our Form 26AS. Meanwhile it's a reconciling item, not lost money.

**Q: "Why do auditors insist on external balance confirmations?"**
A: Internal ledgers can be manipulated or simply wrong; an independent confirmation from the counterparty is third-party evidence that the balance is real. It catches fictitious creditors, unrecorded liabilities, and disputed receivables — the things a reconciliation alone might miss if both sides share the same bad assumption.
