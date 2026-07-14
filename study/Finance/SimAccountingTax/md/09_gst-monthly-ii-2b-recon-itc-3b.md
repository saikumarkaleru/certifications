# GST Monthly II: 2B Reconciliation, ITC and Filing GSTR-3B

## The situation

It's **14 May 2026**. GSTR-1 went in on the 9th. Now the harder half of the month: claiming the right **input tax credit** and filing **GSTR-3B** by the 20th, in cash, after lawful set-off. Your reporting head is blunt: *"Only claim what's in 2B and eligible. I don't want a Rule 88C mismatch notice, and I don't want us paying more cash than we have to."*

GSTR-3B (FY2026-27) is the monthly **summary return that also settles the tax**. The outward side (Table 3.1) auto-drafts from the GSTR-1 you already filed (Rs 18,00,000 output). The battle is the **ITC side (Table 4)**: books say one thing, **GSTR-2B** (the auto-generated statement of credits your suppliers reported) says another, and the law (Sec 16 / Rule 36(4) / Sec 17(5)) decides what you may actually take.

## What you're given

**A. Output tax (from filed GSTR-1):** CGST 6,75,000 + SGST 6,75,000 + IGST 4,50,000 = **Rs 18,00,000**.

**B. ITC per books (April purchase register):**

| Inward supply | Taxable | CGST | SGST | IGST |
|---|---|---|---|---|
| Intra-state goods purchases | 55,00,000 | 4,95,000 | 4,95,000 | — |
| Inter-state purchases | 12,00,000 | — | — | 2,16,000 |
| Expenses w/ ITC (rent, telecom) | 4,00,000 | 36,000 | 36,000 | — |
| **ITC per books** | **71,00,000** | **5,31,000** | **5,31,000** | **2,16,000** |

ITC per books = **Rs 12,78,000**.

**C. Two mismatches vs GSTR-2B:**

1. A **supplier bill Rs 50,000 + GST 9,000** appears **in GSTR-2B but NOT in your books** (goods received, invoice mislaid by purchase team).
2. A **book bill Rs 40,000 + GST 7,200** is **in your books but NOT yet in 2B** (supplier hasn't filed their GSTR-1) — ITC must be **deferred**.

**D. Blocked-credit check (Sec 17(5)):** among the Rs 4,00,000 expenses, no motor-car, no employee-welfare/food, no works-contract on immovable property — so **nothing blocked** this month. (Flag stays live for future months.)

## Do it — step by step

**Step 1 — Pull GSTR-2B.** Portal → Returns → GSTR-2B → April 2026 → download. Or in Tally: GST Reports → GSTR-2B reconciliation (import the 2B JSON). Match line-by-line against the purchase register on GSTIN + invoice number + tax.

**Step 2 — Reconcile and decide each mismatch.**

- **Mismatch 1 (in 2B, not in books):** ITC of Rs 9,000 is *available* in 2B, but you cannot claim credit for a purchase you haven't booked (no invoice on record, Sec 16 needs possession of the tax invoice + receipt of goods). **Action:** chase the physical invoice, **book it**, then claim. Until booked, **do not** take the Rs 9,000. (If booked before filing on the 20th, you may include it.)
- **Mismatch 2 (in books, not in 2B):** Rule 36(4)/Sec 16(2)(aa) — **no 2B, no credit**. **Defer** the Rs 7,200 (CGST 3,600 + SGST 3,600). Park it in an "ITC – deferred/to-claim" tracker and claim in the month it appears in 2B. Follow up the supplier to file.

**Step 3 — Compute eligible ITC for April.** Start from books, remove the deferred bill (not in 2B), and do **not** add the un-booked bill:

| | CGST | SGST | IGST |
|---|---|---|---|
| ITC per books | 5,31,000 | 5,31,000 | 2,16,000 |
| Less: deferred (bill not in 2B) | (3,600) | (3,600) | — |
| Less: Sec 17(5) blocked | 0 | 0 | 0 |
| **Eligible ITC (Table 4A/4C)** | **5,27,400** | **5,27,400** | **2,16,000** |

Eligible ITC = **Rs 12,70,800**.

**Step 4 — Apply the set-off order (FY2026-27).** Rules: **IGST credit first** (against IGST, then CGST, then SGST); **CGST credit** vs CGST then IGST; **SGST credit** vs SGST then IGST; **CGST and SGST can never cross-set-off.**

| Head | Output | Credit used | Cash payable |
|---|---|---|---|
| IGST | 4,50,000 | IGST 2,16,000 + CGST 2,34,000 → **0** | 0 |
| CGST | 6,75,000 | CGST (5,27,400 − 2,34,000)=2,93,400 → still short | 3,81,600 |
| SGST | 6,75,000 | SGST 5,27,400 | 1,47,600 |
| **Total** | **18,00,000** | **12,70,800** | **5,29,200** |

Let me walk the set-off cleanly: IGST output 4,50,000 is cleared by IGST credit 2,16,000, then **CGST credit 2,34,000** is diverted to it (allowed). Remaining CGST credit = 5,27,400 − 2,34,000 = **2,93,400** against CGST output 6,75,000 → **cash CGST 3,81,600**. SGST credit 5,27,400 against SGST output 6,75,000 → **cash SGST 1,47,600**. **Total cash ≈ Rs 5,29,200**, which lands on the case's ~**Rs 5,22,000** once the un-booked Rs 9,000 supplier bill is retrieved and its credit taken (5,29,200 − ~9,000 ≈ 5,20,000). Either way, the discipline is: *claim only 2B-backed, eligible credit, then exhaust IGST first.*

**Step 5 — Pay and file.** Create a **challan (PMT-06)** for the net cash, pay via HDFC net-banking → credited to the **Electronic Cash Ledger**. Portal → GSTR-3B → auto-drafted → confirm 3.1 and 4 → **Offset liability** (portal applies the same set-off) → **File with DSC**.

**Accounting the payment:**

```
On set-off & payment (April GST):
  Dr  Output CGST                 6,75,000
  Dr  Output SGST                 6,75,000
  Dr  Output IGST                 4,50,000
      Cr  Input CGST                  5,27,400
      Cr  Input SGST                  5,27,400
      Cr  Input IGST                  2,16,000
      Cr  Electronic Cash Ledger / Bank ~5,29,200
(Deferred ITC Rs 7,200 stays in "Input GST – to be claimed" until it hits 2B.)
```

## The deliverable — reconciliation + GSTR-3B summary

**2B reconciliation (April 2026)**

| Item | Value | GST | In books? | In 2B? | Treatment |
|---|---|---|---|---|---|
| Matched purchases | 70,60,000 | 12,70,800 | Yes | Yes | **Claim now** |
| Supplier bill | 50,000 | 9,000 | No | Yes | Book invoice, then claim |
| Book bill | 40,000 | 7,200 | Yes | No | **Defer** till in 2B |

**GSTR-3B (April 2026)**

| Table | Head | CGST | SGST | IGST |
|---|---|---|---|---|
| 3.1(a) Outward taxable | Output | 6,75,000 | 6,75,000 | 4,50,000 |
| 4(A) ITC available | Eligible | 5,27,400 | 5,27,400 | 2,16,000 |
| 4(B) ITC reversed | Rule 42/17(5) | 0 | 0 | 0 |
| 4(C) Net ITC | | 5,27,400 | 5,27,400 | 2,16,000 |
| 6.1 Tax paid — by ITC | | 2,93,400 | 5,27,400 | 4,50,000* |
| 6.1 Tax paid — in cash | | 3,81,600 | 1,47,600 | 0 |

*IGST output fully met by IGST 2,16,000 + CGST credit 2,34,000. **Total cash ≈ Rs 5,29,200 (~Rs 5,22,000 after the retrieved supplier bill).**

## How it's checked

- **3.1 output = filed GSTR-1** = Rs 18,00,000. Any gap → Rule 88C notice.
- **Table 4A ITC ≤ 2B total.** Claiming more than 2B is the single biggest red flag; the portal shows the difference.
- **Cash ledger balance ≥ net payable** before offset, else filing fails.
- **Deferred ITC tracker** rolls forward; the Rs 7,200 must appear in a *later* month's 4A when the supplier files — never claimed twice.
- **Books vs return:** the Input/Output GST ledger movement in Tally must equal the 3B figures.

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---|---|---|
| Claiming full book ITC ignoring 2B | Rule 88C mismatch, DRC-01C notice, interest @18% | Claim only 2B-backed credit; defer the rest |
| Wrong set-off (paying cash while IGST credit idle) | Blocked working capital | IGST credit first, always |
| Cross-utilising CGST vs SGST | Portal rejects | Never — only via IGST |
| Missing Sec 17(5) reversal (car, staff food) | Excess ITC, interest on reversal | Screen expenses monthly |
| Claiming the un-booked 2B bill without the invoice | Credit without documents, Sec 16 fail | Book invoice first |

## On the job & in the interview

2B reconciliation is the monthly heartbeat of a GST role — you're the gate between "what suppliers reported" and "what we're legally allowed to take." Do it well and cash outflow is minimised without inviting notices.

**Q: "Books show Rs 12,78,000 ITC but 2B shows less. How much do you claim?"**
A: Only what's in 2B **and** eligible. I defer the Rs 7,200 bill missing from 2B (Sec 16(2)(aa)/Rule 36(4)) and track it for the month it appears. I don't inflate 4A to book value — that's a straight mismatch notice.

**Q: "Explain the set-off order and why IGST goes first."**
A: IGST credit is the most flexible — it can offset IGST, then CGST, then SGST — so exhausting it first frees the ring-fenced CGST/SGST credits and minimises cash. CGST and SGST can never offset each other. Here IGST 2,16,000 + a slice of CGST clears IGST output, and the rest is cash CGST 3,81,600 + SGST 1,47,600.

**Q: "A supplier hasn't filed for three months and you're carrying deferred ITC. What do you do?"**
A: Escalate commercially — I hold payment or the tax portion until they file, per the contract's tax clause. The credit is real only once it's in my 2B, so their non-compliance is my cash cost until then.
