# Study Guide — Fund Ops: NAV, Reconciliation & KYC/AML

Everything you need to defend this project line-by-line in an interview.

---

## 30-second pitch

> "I built a fund-operations tool in Python that does the three things a fund
> accountant / ops analyst does daily: it strikes the fund's NAV, it reconciles
> trades and cash between our internal book and the custodian and classifies the
> breaks onto an aged exception queue, and it runs a KYC/AML control that
> risk-rates customers into CDD/EDD tiers and monitors transactions for
> large-value, structuring and layering patterns. It's a small `src/` package
> with unit tests, and it outputs a formatted Excel workbook and charts. It runs
> fully offline on synthetic data seeded with real-world break types."

---

## Guided walkthrough (how it runs)

1. **`data.py`** loads the CSVs from `input/` — positions, today's and prior-day
   prices, book vs custodian trades and cash, customers, transactions, and the
   fund static parameters.
2. **`pricing.py`** values each holding and tags the price source
   (GOOD / STALE / FALLBACK_PRIOR / MISSING). Total holdings MV feeds the NAV.
3. **`nav.py`** builds the waterfall: GAV = holdings + cash + accrued income;
   subtract the daily-accrued management fee (TER) and other expenses to get NAV;
   divide by units for NAV per unit; compare to the prior day and flag a ≥2% move.
4. **`reconciliation.py`** matches book vs custodian on a key, compares quantity
   and amount, and classifies each break; ages it and puts it on the queue.
5. **`kyc.py`** scores customers (geography/product/profile) into tiers with
   mandatory-EDD overrides, then runs four AML rules to raise alerts.
6. **`reporting.py`** writes the six-sheet Excel workbook and three PNG charts.
7. **`main.py`** orchestrates all of it and prints a desk-style summary.

---

## Core concepts (know these cold)

### Fund accounting
- **NAV (Net Asset Value)** = total assets − total liabilities. For a fund:
  `NAV = market value of investments + cash + accrued income − accrued expenses`.
- **NAV per unit / per share** = NAV ÷ units outstanding. This is the price at
  which investors subscribe and redeem. Getting it wrong is a **NAV error**,
  which can require investor compensation.
- **GAV (Gross Asset Value)** = assets *before* deducting liabilities/fees.
- **TER (Total Expense Ratio)** = annual running cost of the fund (management
  fee + admin + audit + custody) as a % of assets. The management fee **accrues
  daily** so the NAV each day already reflects a slice of the annual fee —
  otherwise the day the fee is paid the NAV would jump.
- **Accrued income** = income earned but not yet received (e.g. dividend declared
  but not paid, bond coupon accruing between payment dates). Accruing it keeps
  the NAV fair to investors who subscribe/redeem between payment dates.
- **Valuation point / cut-off** = the fixed daily time the NAV is struck.
- **Pricing/valuation policy** = documented rules for stale, missing or
  hard-to-value prices. A **fair-value adjustment** replaces a stale market price
  with an estimated fair price.

### Trade lifecycle & settlement
- **Trade lifecycle**: order → execution → **trade capture / booking** →
  **confirmation/affirmation** (agree economics with the counterparty) →
  **clearing** → **settlement** (exchange of cash and securities) → position &
  cash update → reconciliation.
- **T+1 settlement**: cash and securities settle **one business day** after trade
  date (US equities moved T+2 → T+1 in May 2024). **Trade date** is when you
  deal; **settlement date** is when it actually settles. Between them you carry a
  **receivable/payable**.
- **DVP (Delivery versus Payment)**: securities delivered only against
  simultaneous payment — removes principal risk.
- **Custodian**: the bank that safekeeps the fund's assets and provides the
  independent record we reconcile against. **Fund accountant / administrator**:
  strikes the NAV. **Front / middle / back office**: dealing / risk & trade
  support / settlements & reconciliation.

### Reconciliation & break types
- **Reconciliation** = matching two independent records (our book vs the
  custodian) so the NAV is struck on verified positions and cash.
- **Break / exception** = a difference that needs investigation:
  - **Quantity mismatch** — same trade, different quantity booked.
  - **Price / amount mismatch** — different price or settlement amount.
  - **Missing trade (unmatched book)** — we booked it, custodian didn't show it.
  - **Orphan (unmatched custodian)** — custodian shows it, we didn't book it.
  - **Duplicate** — same trade booked twice on one side.
- **Aging** = how long a break has been open; older breaks are higher risk and
  escalated. Breaks feed an **exception queue** worked worst-first.

### KYC / AML
- **KYC (Know Your Customer)** = verify identity and understand the customer at
  onboarding and periodically after.
- **CDD (Customer Due Diligence)** = standard checks. **EDD (Enhanced Due
  Diligence)** = deeper checks for higher-risk customers (source of wealth,
  senior sign-off, ongoing monitoring). **SDD** = simplified for low risk.
- **Risk-based approach**: rate customers by **geography, product/service, and
  profile (PEP, adverse media, entity type)** and apply diligence proportional
  to risk.
- **PEP (Politically Exposed Person)** = higher corruption/bribery risk → EDD.
- **FATF** = global AML standard-setter; publishes high-risk ("black/grey list")
  jurisdictions. Sanctioned countries (e.g. Iran, North Korea) are highest risk.
- **Transaction monitoring** patterns:
  - **Structuring / smurfing** — splitting a large amount into several deposits
    just under a reporting threshold to avoid detection.
  - **Layering** — rapid in-and-out movement to obscure the money trail (the
    second stage of money laundering: placement → layering → integration).
- **CTR (Currency Transaction Report)** = mandatory report of large cash
  transactions (US: > $10,000). **SAR / STR (Suspicious Activity / Transaction
  Report)** = filed when activity looks suspicious regardless of amount.

---

## Interview Q&A (15–20)

**1. What is NAV and why does it matter?**
Net Asset Value = assets − liabilities; per unit it's the dealing price for
subscriptions/redemptions. An incorrect NAV means investors transact at the
wrong price, so accuracy and controls are critical.

**2. Walk me through your NAV calculation.**
GAV = holdings market value + cash + accrued income. Subtract the daily-accrued
management fee (GAV × annual TER × days/365) and other accrued expenses to get
NAV. NAV ÷ units outstanding = NAV per unit. See `nav.compute_nav`.

**3. Why accrue the management fee daily instead of on payment date?**
So the NAV reflects the true cost each day and doesn't jump when the fee is
actually paid. Daily accrual is fair to investors dealing on any given day.

**4. What is the TER and what's in it?**
Total Expense Ratio — the fund's annual running cost as a % of assets:
management fee plus admin, custody, audit and other operating costs. My model
accrues the management-fee component daily.

**5. What is accrued income and why accrue it?**
Income earned but not yet received (dividends declared not paid, bond coupon
accruing). Accruing keeps the NAV fair between income payment dates.

**6. How do you handle a stale or missing price?**
Documented policy: a price older than 3 days is STALE (used as last-known-good
but flagged); no price today falls back to the prior-day close (FALLBACK, flagged);
no price anywhere is MISSING → valued at 0 and raised as a hard exception. A real
desk would suspend the NAV or apply a fair-value adjustment rather than publish.

**7. You flag a ≥2% day-over-day NAV move — why?**
A large move is either a real market event or an error (bad price, missed
corporate action, booking error). Flagging it triggers a four-eyes check before
the NAV is published — a standard NAV-oversight tolerance control.

**8. What is T+1 settlement? Trade date vs settlement date?**
Trade date is when the deal is struck; settlement date is when cash and
securities actually change hands — one business day later for US equities since
2024. Between the two you carry a receivable/payable.

**9. Walk me through the trade lifecycle.**
Order → execution → booking → confirmation/affirmation → clearing → settlement →
position & cash update → reconciliation. Ops mostly lives in the post-execution
"middle/back office" stages.

**10. What is reconciliation and why two sources?**
Matching our internal book against the custodian's independent record. Two
independent sources catch booking errors, missed trades and fails before they
corrupt the NAV.

**11. What break types does your engine detect?**
Quantity mismatch, price/amount mismatch, missing-at-custodian (unmatched book),
orphan-at-custodian (unmatched custodian), and duplicate. Matched records drop
off the queue. Each is aged and given a severity.

**12. Custodian shows a trade you didn't book — what is it and what do you do?**
An orphan / unmatched-custodian break. Investigate: is it a trade we executed but
failed to capture, a custodian error, or booked to the wrong account? Book it,
amend, or dispute with the custodian; escalate if it ages.

**13. How do you prioritise breaks?**
By severity and age. Amount mismatches and missing/orphan trades are High;
quantity mismatches and duplicates Medium. Older breaks escalate. The queue is
sorted worst-first with aging buckets (0–2d … 10d+).

**14. How is one engine reused for trades and cash?**
`reconcile()` is generic: you pass the match key, the columns to compare, and the
date column for aging. Trades key on `trade_id` and compare quantity + amount;
cash keys on `type+reference` and compares amount.

**15. Explain your KYC risk-scoring model.**
Weighted composite: geography 35%, product 35%, profile 30%, each 0–100. Below 35
is Low (CDD), 35–65 Medium (CDD+), 65+ High (EDD). PEP, sanctioned/high-risk
geography, or correspondent banking force EDD regardless of score.

**16. CDD vs EDD — when does each apply?**
CDD is standard due diligence for normal-risk customers. EDD adds source-of-wealth
checks, senior sign-off and closer ongoing monitoring for higher-risk customers
(high-risk geography, PEPs, complex/opaque structures).

**17. Why do PEPs and certain countries force EDD?**
Higher inherent bribery/corruption and sanctions risk. A risk-based approach
requires enhanced measures regardless of the numeric score — a hard override.

**18. What is structuring and how do you catch it?**
Splitting a large sum into several deposits just under a reporting threshold to
avoid a CTR. I flag ≥3 inbound deposits in the $8,000–$9,999 band for one
customer.

**19. CTR vs SAR/STR?**
A CTR is a mandatory report of large cash transactions (US > $10k) — objective,
threshold-based. A SAR/STR is filed for *suspicious* activity regardless of
amount and is judgement-based. My LARGE_VALUE rule is CTR-style; STRUCTURING and
RAPID_MOVEMENT are the kind of patterns that feed a SAR.

**20. What are the three stages of money laundering and which does RAPID_MOVEMENT target?**
Placement → layering → integration. Rapid in-and-out movement (in then a
near-equal outflow within a few days) is classic **layering** — moving funds
quickly to obscure their origin.

**21. What would you improve with more time?**
Multi-currency FX for the NAV, position-level bond accrued-interest (day-count),
corporate-action processing, fuzzy trade matching (near-key/economic matching),
a persistent break history for true aging, and calibrated AML thresholds.

---

## Quick numbers to remember (sample run)
- Holdings MV ≈ **$15.46M**, GAV ≈ **$16.76M**, NAV ≈ **$16.73M**,
  NAV/unit ≈ **3.3465** (prior 3.2600 → **+2.65%, flagged**).
- **5 trade breaks + 3 cash breaks**; **8 customers → 4 High (EDD)**;
  **14 AML alerts**.
