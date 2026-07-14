# Working Capital & the 13-Week Cash Forecast

## The ask

It's **Monday, 6 July 2026**. The term-loan sanction letter carries a covenant: **minimum cash balance of Rs 20 lakh** at all times, tested on the bank's month-end certificate. With the Q1 revenue miss (Rs 2.70 cr actual vs Rs 2.85 cr budget) and a big supplier payment and an advance-tax instalment both due this quarter, the CFO is nervous about a mid-quarter dip.

She asks for two things by **Wednesday**: (1) a clean read on **working capital and the cash conversion cycle** — how long NTSPL's cash is tied up — and (2) a **13-week direct cash-flow forecast** (a rolling treasury tool) showing every week's collections, payments, payroll, GST, TDS and loan EMI, with the **minimum-cash covenant check** flagged and a list of **levers to free cash** if a week breaches.

## What you're given

Working-capital assumptions and balances (FY2026-27):

| Item | Assumption | Balance |
|---|---|---|
| Debtors (DSO) | 60 days | Rs 2.00 cr |
| Inventory (DIO) | 40 days | Rs 0.90 cr |
| Creditors (DPO) | 45 days | Rs 1.05 cr |
| Term loan | Rs 1.20 cr @ 9.5% | — |
| Opening cash (Mon 6 Jul) | — | Rs 35 lakh |

Flow anchors (annualised): revenue Rs 12.00 cr (~Rs 1.00 cr/month, ~Rs 23 lakh/week), COGS Rs 8.40 cr, monthly payroll ~Rs 9 lakh (employee cost 1.08 cr/12). GST is broadly net ~Rs 3–4 lakh/month payable (output less input credit), TDS deposits ~Rs 1.5 lakh/month, advance tax Q1 instalment (15%) due 15 September but the Rs 15 lakh supplier catch-up lands in Week 4.

## Build it — step by step

**Step 1 — the cash conversion cycle (CCC).** This is how many days cash is locked in operations:

```
CCC = DSO + DIO - DPO
    = 60  + 40  - 45  = 55 days
```

NTSPL waits **55 days** between paying for goods/inventory and collecting the cash from customers. At ~Rs 12 cr revenue, each day of CCC ties up roughly `12cr/365 ≈ Rs 3.29 lakh`. So the 55-day cycle locks up about **Rs 1.81 cr** of operating cash — money funded by the term loan and cash reserves. Cutting CCC by 10 days frees ~Rs 33 lakh.

Cross-check via balances: Debtors 2.00 + Inventory 0.90 − Creditors 1.05 = **Net working capital Rs 1.85 cr** — consistent with the 55-day read.

**Step 2 — frame the 13-week grid.** In Excel, weeks as columns (W1 = w/c 6 Jul … W13 = w/c 28 Sep), rows as line items. The engine:

```
Closing cash (Wn) = Opening cash (Wn) + Collections - all Payments
Opening cash (Wn+1) = Closing cash (Wn)          [carry forward]
Covenant flag: =IF(Closing < 20L, "BREACH", "OK")
```

Collections come from the debtor book (60-day DSO means this quarter I'm largely collecting on prior-quarter sales), so I lag them: `=SUMIFS(Invoices, DueWeek, Wn)`. I use ~Rs 23 lakh/week baseline collections, dipping in the weeks reflecting the Q1 volume miss.

**Step 3 — load the lumpy outflows.** The killers in a direct forecast are the non-smooth items: supplier catch-up Rs 15 L (W4), quarterly-ish GST clusters, monthly payroll (last working week of each month), TDS (by the 7th → W1, W5, W10), loan EMI, and advance tax.

Loan EMI on Rs 1.20 cr @ 9.5% — interest alone is `1.20cr × 9.5% / 12 ≈ Rs 95,000/month`; with principal the EMI is ~Rs 2.6 lakh/month (assume ~5-yr amortisation). I place it in the first week of each month.

## The deliverable

**13-Week Direct Cash-Flow Forecast — NTSPL (Rs lakh), w/c 6 Jul → 28 Sep 2026**

| Week | Open | Collect | Supplier pay | Payroll | GST/TDS | EMI | Capex/Tax | Close | Covenant |
|---|---|---|---|---|---|---|---|---|---|
| W1 | 35.0 | 23 | −16 | 0 | −1.5 | −2.6 | 0 | 37.9 | OK |
| W2 | 37.9 | 22 | −17 | 0 | 0 | 0 | 0 | 42.9 | OK |
| W3 | 42.9 | 21 | −16 | 0 | −4 (GST) | 0 | 0 | 43.9 | OK |
| W4 | 43.9 | 22 | −16 | −9 | 0 | 0 | −15 (supplier catch-up) | 25.9 | OK |
| W5 | 25.9 | 23 | −17 | 0 | −1.5 | −2.6 | 0 | 27.8 | OK |
| W6 | 27.8 | 20 | −15 | 0 | 0 | 0 | 0 | 32.8 | OK |
| W7 | 32.8 | 21 | −16 | 0 | −4 (GST) | 0 | 0 | 33.8 | OK |
| W8 | 33.8 | 22 | −16 | −9 | 0 | 0 | 0 | 30.8 | OK |
| W9 | 30.8 | 23 | −17 | 0 | −1.5 | −2.6 | 0 | 32.7 | OK |
| W10 | 32.7 | 22 | −16 | 0 | −1.5 (TDS) | 0 | 0 | 37.2 | OK |
| W11 | 37.2 | 21 | −16 | 0 | −4 (GST) | 0 | 0 | 38.2 | OK |
| W12 | 38.2 | 22 | −16 | −9 | 0 | 0 | −20 (adv tax) | 15.2 | **BREACH** |
| W13 | 15.2 | 24 | −16 | 0 | 0 | −2.6 | 0 | 20.6 | OK (thin) |

**Analyst commentary:** *Cash holds above the Rs 20 lakh covenant through most of the quarter, with the first squeeze in W4 (supplier catch-up drops us to Rs 25.9 L) and a **covenant breach in W12** at Rs 15.2 L — the collision of month-end payroll and the 15-Sep advance-tax instalment. W13 recovers to Rs 20.6 L only because collections tick up. This is a timing problem, not a solvency problem — NWC is healthy at Rs 1.85 cr — but the bank tests the balance, so we must act before W12.*

**Levers to free cash (ranked, with the W12 fix):**

| Lever | Mechanism | Cash impact | Fixes W12? |
|---|---|---|---|
| Accelerate collections (DSO 60→50) | Dunning top 10 debtors, early-pay 1% discount | ~Rs 33 L freed | Yes — pull ~Rs 10–15 L into W11–12 |
| Stagger advance tax / phase supplier | Move Rs 15 L supplier catch-up W4→W6; pay adv tax in two tranches | Smooths the two dips | Yes |
| Extend DPO 45→55 with key vendors | Negotiate net-55 terms | ~Rs 33 L freed | Partial |
| Trim inventory (DIO 40→32) | Order in smaller lots on slow SKUs | ~Rs 26 L freed | Partial |
| Draw the CC/OD limit | Bank overdraft as a buffer week | Bridges W12 | Yes (last resort) |

**Recommendation:** pull collections forward on the top 10 debtors and split the advance-tax payment — that alone lifts W12 back above Rs 20 L without touching the OD line.

## How it's reviewed

The CFO/controller checks: (1) **roll-forward integrity** — each week's opening = prior week's closing, no gaps (a single broken link corrupts every downstream week). (2) **Covenant flag actually fires** — the `IF < 20L` must catch W12; a forecast that hides a breach is worse than useless. (3) **Lumpy items present** — payroll, EMI, GST, TDS, advance tax all placed on the *right* week, not smoothed away. (4) **CCC ties to balances** — 55 days ≈ Rs 1.85 cr NWC. (5) **Direct, not indirect** — this is actual receipts/payments (treasury view), not a P&L-derived accrual cash flow. (6) **Collections lag DSO** — you're collecting old sales, so the Q1 miss hits *these* weeks with a ~60-day delay.

## Common mistakes & red flags

- **Recognising cash when revenue is booked** — with 60-day DSO, a sale today is cash ~8 weeks out. Putting revenue into the collection week overstates near-term cash badly.
- **Smoothing lumpy outflows** — averaging payroll/GST/tax across weeks hides the exact week you breach. The whole point of 13-week is the *timing*.
- **Sign errors / broken carry-forward** — one wrong link and the covenant check lies.
- **Confusing the CCC sign on DPO** — DPO is *subtracted*; a longer DPO shortens the cycle (good for cash).
- **Treating an overdraft draw as "found cash"** — it's a financing plug and carries interest; it's a last-resort lever, not a fix.
- **Ignoring GST input credit** — forecasting gross output GST without netting input credit overstates the outflow.

## On the job & in the interview

The 13-week (a "flash" or "rolling") cash forecast is the treasury heartbeat of an FP&A team — it answers "will we make payroll and stay onside the covenant?" while the annual budget answers "will we hit PAT?" The **cash conversion cycle** is the structural story behind it: DSO + DIO − DPO. Improving CCC is often the cheapest financing available — freeing Rs 33 lakh by collecting 10 days faster beats drawing a loan at 9.5%.

**Q: "Walk me through the cash conversion cycle and what a 55-day cycle costs us."**
*A: CCC = DSO 60 + DIO 40 − DPO 45 = 55 days — the gap between paying suppliers and collecting from customers. At Rs 12 cr revenue, ~Rs 3.3 lakh is tied up per day of cycle, so 55 days locks ~Rs 1.8 cr of operating cash, matching our Rs 1.85 cr net working capital. Every 10 days we shave frees ~Rs 33 lakh — real, interest-free financing.*

**Q: "Your W12 breaches the Rs 20 lakh covenant. What do you do — and don't say 'draw the overdraft'?"**
*A: It's a timing collision of month-end payroll and the 15-Sep advance-tax instalment, not insolvency. First lever is collections: dunning the top 10 debtors and a small early-pay discount pulls Rs 10–15 lakh into W11–12. Second, I'd split the advance-tax payment and shift the W4 supplier catch-up to W6 to de-cluster the outflows. That restores the buffer without financing cost. The OD line is the last resort because it carries 9.5%+ interest and signals stress to the bank.*

**Q: "Why a direct 13-week forecast and not just the indirect cash flow from the model?"**
*A: The indirect statement starts from PAT and adjusts for non-cash and working-capital movements — great for the annual view, but it's accrual-based and monthly. Treasury needs actual receipts and payments by week to manage the covenant and payroll. The direct method lists real cash in and out, so it catches the exact week we dip — which a monthly accrual view would completely miss.*
