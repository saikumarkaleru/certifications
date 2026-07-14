# Blackline Account Reconciliation Workflow (End to End)

## What you'll be able to do

You'll be able to run the balance-sheet reconciliation process the way a modern GCC/shared-services R2R team runs it — in **BlackLine** — end to end: understand how SAP GL balances flow in, prepare a reconciliation with reconciling items, attach evidence, route it through **preparer → reviewer → approver**, apply **auto-certification** and **transaction matching**, raise a **journal** for a true-up, manage **tasks/SLA/aging**, and read the **variance/risk** dashboards. You'll do a worked bank-vs-GL recon with real reconciling items, and you'll be able to replicate the exact control in Excel for free.

## The drill — step by step

**What BlackLine is:** a cloud "financial close" platform that sits *on top of* the ERP. It doesn't replace SAP — it imports SAP GL balances and transactions, then governs the *certification* of every balance-sheet account. Core modules: **Account Reconciliations**, **Transaction Matching**, **Task Management**, **Journal Entry**, **Variance Analysis**. Trintech (Cadency/Adra) and Oracle ARCS are the main alternatives; the workflow concept is identical.

**1. Data in — the GL balance feed.** BlackLine imports two things from SAP: the **trial balance** (GL account balances per company code/period, e.g. via a scheduled flat-file or SAP connector) and, for matching, **transaction detail** (GL line items, bank statement lines). Each SAP GL account is mapped to a BlackLine **account** with an assigned **preparer, reviewer, risk rating, and template type**.

**2. Auto-certification rules.** Low-risk, low-value, or zero-balance accounts don't need a human every month. Rules such as *"balance = 0"*, *"balance unchanged from prior period"*, or *"balance < ₹50,000 threshold"* auto-certify the account and stamp it complete — the preparer only touches exceptions. This is the single biggest efficiency lever; know it cold.

**3. Choose the template & prepare.** For an account needing work (say **Bank GL 100000**), open the recon. Template types:
- **Account Analysis** — you list what makes up the balance.
- **Balance Comparison** — GL balance vs an external source (bank statement, sub-ledger).
- **Roll-forward** — opening + activity − closing (accruals, prepaids, fixed assets).
For the bank recon use **Balance Comparison**: on one side the **GL balance** (from SAP), on the other the **source balance** (bank statement). BlackLine computes the **difference**, which you must fully explain with **reconciling items**.

**4. Transaction Matching (auto-match).** Before manual work, the Matching module pairs GL bank lines to bank-statement lines on rules (amount + date + reference). Matched items drop out; only **unmatched** items remain as candidate reconciling items — the automated bank-rec engine.

**5. Enter reconciling items.** For each unexplained difference add an item: type (timing / error / in-transit), amount, description, GL date, aging start, and **supporting document** (upload the bank statement PDF, the SAP FB03 screenshot). Flag items needing a correction for a **journal**.

**6. Raise a journal if needed.** If the recon reveals a real GL error (e.g. bank charges never booked), create a BlackLine **Journal Entry** (Dr Bank Charges / Cr Bank) that, on approval, is exported back to SAP for posting (or posted directly via connector). The reconciling item then clears next period.

**7. Certify & route — the three-role flow.**
- **Preparer** completes the recon, ticks that reconciling items are supported and aged appropriately, and **submits**.
- **Reviewer** checks quality, evidence, and item validity → **approves** or **rejects with comment** (back to preparer).
- **Approver** (often a controller for high-risk accounts) gives final sign-off.
Every action is timestamped with the user — a full **audit trail** (who prepared, reviewed, approved, when, with what evidence).

**8. Task Management & SLA/aging.** The whole close (not just recons) runs as scheduled **tasks** with owners, due dates by working day, and dependencies — a digital close calendar. **SLA/aging**: reconciling items carry an age; items older than policy (e.g. >60 or >90 days) escalate and hit the **risk dashboard**. Overdue recons flag red for management.

**9. Variance / risk dashboards.** Variance Analysis auto-flags accounts whose balance moved beyond a threshold (absolute or %) vs prior period and demands an explanation. Management sees a heat-map: % of accounts certified, overdue, high-risk, aged items — the close scorecard.

## The output — worked Bank vs GL reconciliation (Bank GL 100000, April 2026)

| | Amount (₹) |
|---|---|
| **GL balance (SAP, 30.04.2026)** | 11,80,000 |
| **Bank statement balance** | 12,10,000 |
| **Difference to explain** | (30,000) |

Reconciling items:

| # | Item | Type | Amount (₹) | Evidence | Age (days) |
|---|---|---|---|---|---|
| 1 | Cheque issued to vendor, not yet cleared bank | Timing (o/s cheque) | −50,000 | FB03 doc 127 | 8 |
| 2 | Customer NEFT received, not yet in GL | Timing (deposit in transit) | +18,000 | Bank stmt line | 3 |
| 3 | Bank charges on statement, not booked | Error → journal | +2,000 | Bank stmt | 2 |
| | **Net reconciling items** | | **−30,000** | | |

**Tie-out:** GL 11,80,000 − 50,000 + 18,000 + 2,000 = **12,10,000** = bank balance. Difference fully explained → recon certifiable. Item 3 spawns Journal `Dr 404000 Bank Charges 2,000 / Cr 100000 Bank 2,000` exported to SAP; items 1 & 2 self-clear when the cheque clears and the NEFT posts.

Certification trail: *Prepared — A.Rao 02-May 10:14; Reviewed — S.Iyer 03-May 09:40; Approved — Controller 03-May 16:20.*

## Checks & gotchas

- **The recon isn't done when the difference is small — it's done when every rupee of difference is explained by a supported reconciling item.** An unexplained residual, even ₹100, fails review.
- **Aged reconciling items** are the real risk: a "timing" item still open after 90 days usually isn't timing — it's an error or a missed write-off. Auditors go straight to the aging report.
- **Auto-certification thresholds** set too loose let real movements slip through uncertified — the balance/threshold rules must be defensible to audit.
- **BlackLine journals must actually post in SAP** — a journal approved in BlackLine but not exported/posted leaves BlackLine and SAP out of sync; confirm the SAP document number.
- **Segregation of duties**: preparer ≠ reviewer ≠ approver. Same person on two roles breaks the control and is an audit finding.
- Balance comparison uses the **period-end** GL and bank balances at the **same date** — mixing a 30-Apr GL with a 2-May bank balance manufactures fake reconciling items.

## Interview drill

**Q1. How does BlackLine tie to SAP?**
"BlackLine imports the SAP trial balance and transaction detail each period; each GL account maps to a BlackLine reconciliation with an owner and risk rating. We certify the SAP balance is correct and supported; corrections are raised as BlackLine journals exported back to SAP. It governs the close on top of SAP — it doesn't replace the ledger."

**Q2. What is auto-certification and why is it safe?**
"Rule-based sign-off for low-risk accounts — zero balances, unchanged balances, or balances under a threshold certify automatically so humans focus on exceptions. It's safe when thresholds are risk-calibrated and documented, and high-risk or materially-moved accounts are always excluded from auto-cert and force manual review."

**Q3. A reconciling item is 120 days old — what do you do?**
"Investigate root cause — an aged 'timing' item usually isn't timing. If it's an error, raise a correcting journal; if it's unrecoverable, write it off with approval; then fix the process so it doesn't recur. I'd never let it keep rolling — it's a control and audit red flag on the aging dashboard."

## Practise free

BlackLine has no free tier, but the **control is fully replicable in Excel** — and doing so proves you understand it better than clicking buttons:
- **Recon workbook:** one tab per account. Columns: GL balance, source balance, difference, then a reconciling-items table (type, amount, evidence link, aging-start date, `=TODAY()-start` for age). A cell check `=GL - source - SUM(items)` must equal **0** to certify.
- **Auto-cert logic:** `=IF(OR(bal=0, bal=priorbal, ABS(bal)<50000), "Auto-Certified", "Manual")`.
- **Workflow columns:** Preparer / Reviewer / Approver names + date stamps, with conditional formatting red when overdue vs a due-date column — mimics task management and SLA.
- **Aging dashboard:** a pivot of reconciling items bucketed 0–30 / 31–60 / 61–90 / 90+ with a red flag on the last bucket.
- **Transaction matching:** two lists (GL lines, bank lines), match on amount+date with `XLOOKUP`/Power Query merge; the unmatched rows are your reconciling items — exactly BlackLine's engine.
Do this once against the April bank recon above and you can speak to every BlackLine screen from real experience. BlackLine and Trintech both publish free product demos and webinars (blackline.com, trintech.com) — watch two to learn the exact button names.
