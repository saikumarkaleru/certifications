# GST — Payment of Tax

> Secs 49, 49A, 49B, 50, 51, 52 + Rules 85–88B, PMT forms. Verify TDS threshold (₹2.5L), rates (2%/1%), Rule 86B trigger (₹50L), interest rates (18%/24%) against ICAI material.

## Snapshot
Self-assessment regime → three electronic ledgers. **Liability Register (PMT-01)** = what you owe; **Cash Ledger (PMT-05)** = money deposited (pays **anything**); **Credit Ledger (PMT-02)** = ITC (pays **output tax only**, never RCM/interest/penalty/fee). Utilisation follows fixed order; discharge follows oldest-first; TDS (Sec 51)/TCS (Sec 52) inject prepaid money into supplier's **cash** ledger; Rules 86A/86B are anti-abuse gates.

## Core concepts
- Cash = real revenue; credit = bookkeeping offset — kept separate (keeps refunds honest, Centre-State settlement closed).
- "Output tax" (Sec 2(82)) **excludes RCM tax** → RCM must be paid in **cash**.
- IGST credit = universal solvent; CGST and SGST credit **never cross**.
- TDS/TCS credit lands in **cash** ledger (prepaid money, not ITC).

## Key provisions / rules

### Three ledgers
| Ledger | Form | Sec | Pays |
|---|---|---|---|
| Cash | PMT-05 | 49(1),(3) | **Anything** — tax, interest, penalty, fee, other |
| Credit | PMT-02 | 49(2),(4) | **Output tax ONLY** |
| Liability | PMT-01 | 49(7) | (register of dues) |

- Challan **PMT-06** (valid **15 days**; OTC ≤ **₹10,000**/challan/tax period). CIN on payment. Cash ledger = 4 major heads × 5 minor heads grid.
- **PMT-09** (Sec 49(10)/(11)): transfer within cash ledger between heads — NOT a refund, stays within cash. PMT-03 (re-credit rejected refund to credit ledger), PMT-04 (discrepancy), PMT-07 (debited but no CIN).

### Utilisation order (Sec 49(5), 49A, 49B, Rule 88A)
1. IGST credit → IGST liability fully.
2. Balance IGST credit → CGST and/or SGST in **any order and proportion** (Rule 88A).
3. Only after IGST credit = 0: CGST credit → CGST then IGST (never SGST).
4. Only after IGST credit = 0: SGST credit → SGST then IGST (never CGST).

| Credit ↓ / Tax → | IGST | CGST | SGST |
|---|---|---|---|
| IGST | 1st | after IGST | after IGST |
| CGST | after IGST gone | 1st | **NEVER** |
| SGST | after IGST gone | **NEVER** | 1st |

- **Rule 86A** (block): Commissioner/officer ≥ Assistant Commissioner may disallow use of suspect fraudulent/ineligible credit; temporary (lapses **1 year**); restraint not levy, doesn't extinguish credit.
- **Rule 86B** (1% cash floor): if taxable supply (excl. exempt/zero-rated) in a **month > ₹50 lakh** → discharge **≥1% of output tax liability in CASH** (credit ≤ 99%). Exceptions: proprietor/MD/partner paid income tax >₹1L in each of last 2 FYs; received refund >₹1L (zero-rated/inverted duty) preceding FY; already paid >1% cumulative cash in current FY; govt dept/PSU/local authority/statutory body.

### Order of discharge (Sec 49(8))
(1) Self-assessed tax + dues of **PREVIOUS** periods → (2) current period → (3) other amounts / Sec 73/74 demand. Within each level, credit clears only **tax**; interest/penalty/fee = cash.

### Interest (Sec 50, Rule 88B)
| Situation | Sec | Rate | Base |
|---|---|---|---|
| Delayed tax (return filed late) | 50(1) proviso | **18%** | **Net cash liability only** (Rule 88B(1)), due date → payment |
| Short/not paid (proceedings / after 73-74) | 50(1) | **18%** | **Gross** tax (Rule 88B(2)) |
| ITC wrongly **availed AND utilised** | 50(3) | **24%** | Wrongly-utilised ITC, utilisation → reversal (Rule 88B(3)) |

- Proviso (retrospective 1.7.2017): interest only on cash portion because ITC was already in exchequer's hands. Gross if return filed after 73/74 begins.
- Sec 50(3): interest only if wrong credit **availed AND utilised**; "utilised" = ledger balance falls **below** wrongly-availed amount. Reversed before dip = no interest. Interest can apply to a **part** only.

### TDS — Sec 51 (Rule 66)
- Deductors: Central/State govt dept, local authority, govt agencies, notified persons (bodies with ≥51% govt participation, govt societies, PSUs).
- **2%** (1% CGST + 1% SGST / 2% IGST) where taxable value under a **contract exceeds ₹2,50,000** (excl. GST).
- No TDS: supplier & place of supply in State/UT **different** from recipient's registration State; on tax component; exempt/non-taxable supply; contract value ≤ ₹2,50,000.
- Deposit by **10th** next month; **GSTR-7**; certificate **GSTR-7A**. Lands in supplier's **cash ledger**. Late deposit 18% interest.

### TCS — Sec 52 (Rule 67)
- Electronic Commerce Operator collecting consideration for sellers. **Not** where ECO liable under **Sec 9(5)**.
- **Up to 1%** (0.5% CGST + 0.5% SGST / 1% IGST) on **net value of taxable supplies** = aggregate taxable supplies (excl. Sec 9(5)) − supplies **returned**.
- Deposit by **10th**; **GSTR-8** + annual statement. Lands in supplier's **cash ledger**. Matching mechanism reconciles. Suppliers via ECO compulsorily registrable.

## Worked mini-example
Rule 88A optimisation: Output CGST 1,00,000, SGST 1,00,000, IGST nil. ITC: IGST 1,00,000, CGST 20,000, SGST 90,000.
- **Optimal** — route IGST credit to weaker own-credit head (CGST): CGST = 20,000 own + 80,000 IGST → paid; SGST = 90,000 own + 10,000 IGST → paid. **Cash = ₹0**, ₹10,000 IGST c/f.
- **Suboptimal** (all IGST to CGST): CGST fully paid but ₹20,000 CGST credit stranded; SGST needs ₹10,000 cash. Costs ₹10,000 cash. Always route IGST balance to head with short own-credit.

## Exam traps & must-remember
1. Credit ledger pays **output tax only** — interest/penalty/late fee/RCM = **CASH** (output tax excludes RCM).
2. Interest (late return) on **net cash**, not gross — but gross if after Sec 73/74.
3. Sec 50(3) 24% only if availed **AND utilised**; "utilised" = balance falls below wrong amount; part-only possible.
4. IGST credit exhausted first (Sec 49A); within it Rule 88A gives any order/proportion.
5. CGST ⇄ SGST **never** cross.
6. TDS threshold **per contract**, excl. GST, **exceeds** ₹2.5L (exactly ₹2.5L = no TDS); no TDS on State mismatch.
7. TCS on **net** value at ~1% (not 2%); not for Sec 9(5).
8. Order of discharge mandatory — can't pay current while previous open.
9. Rule 86B = 1% of **output tax liability**, triggered by taxable turnover >₹50L/**month** (not 1% of turnover).
10. PMT-09 = transfer within cash ledger; not a refund, not credit-ledger.
11. OTC cap ₹10,000/challan; PMT-06 valid 15 days.
12. Rule 86A = temporary restraint (≤1 yr), not a rate; ≠ Rule 86B.
13. TDS/TCS credit → **cash** ledger, not credit ledger.

## One-line recall
- Cash pays anything; credit pays output tax only (never RCM/interest/penalty).
- Utilise IGST credit first fully; then CGST/SGST any order; CGST↔SGST never cross.
- Discharge: previous dues → current → demands; credit clears tax only.
- Interest 18% net cash (late return) / gross (proceedings); 24% wrong ITC availed+utilised.
- TDS 2% >₹2.5L contract (GSTR-7); TCS ~1% net value (GSTR-8) — both → supplier cash ledger, by 10th.
- Rule 86B: >₹50L/month → ≥1% output tax in cash; Rule 86A blocks suspect credit ≤1 yr.
