# Chapter 11 — AS 11: The Effects of Changes in Foreign Exchange Rates

## Snapshot
- Covers (a) accounting for **foreign-currency transactions** and (b) **translating financial statements of foreign operations** (branches, subsidiaries, associates, JVs), plus **forward exchange contracts**.
- Core: a foreign-currency amount must be translated into ₹ using an exchange rate; the **right rate** depends on whether the item is **monetary** (live money claim — re-translate) or **non-monetary** (settled historical cost — freeze).
- Reporting currency = ₹ (Indian company). Excludes hedge accounting beyond forwards, inflation restatement, and (directly) foreign borrowing costs (AS 16 interacts).

## Core concepts
- **Monetary items ("water")** — money held + assets/liabilities to be **received/paid in fixed or determinable amounts of money** → re-translate at **closing rate**; differences to P&L.
- **Non-monetary items ("ice")** — everything else (physical assets, ownership, rights to goods) → keep at **historical (transaction-date) rate**; no exchange difference (unless carried at fair value → rate on date fair value determined).
- **The test is FORM OF SETTLEMENT, not asset type:** settled in a fixed sum of money = monetary; settled in goods/services/ownership = non-monetary. So an **advance for goods** is non-monetary but a **loan** is monetary.
- **Exchange difference** = same foreign amount reported at different rates.

### Monetary vs non-monetary
| Monetary (re-translate) | Non-monetary (freeze) |
|---|---|
| Cash, bank, debtors, creditors | Inventory, PPE, intangibles, goodwill |
| Loans given/taken, deposits | Equity investments (shares held) |
| Redeemable pref shares/debentures held | Prepaid expenses |
| Cash-settled provisions | Advances for goods (paid OR received) |
| **Refundable** advance (money back) | Warranty-by-repair provisions |
| Doubtful debtor (gross claim still money) | Share capital, securities premium |

## Key provisions / rules

### Three moments of a foreign-currency transaction
1. **Initial recognition** — transaction-date spot rate (avg for a week/month allowed if stable). Transaction date = date it qualifies for recognition (risk/reward pass), not invoice/payment date.
2. **Each balance sheet date** — monetary → **closing rate** (difference = exchange difference); non-monetary at cost → **keep historical**; non-monetary at fair value → rate when FV determined.
3. **Settlement** — settlement-date rate.
- **Re-baselining:** in a later year, measure the difference against the **previously reported** amount, not the origination amount. Safe habit: compute closing ₹ freshly (foreign amount × rate) and take difference from what the item is currently sitting at.

### Where the difference goes
- **General rule:** exchange differences on monetary items (on settlement OR on reporting) → **Profit & Loss** in the period they arise — both unrealised (year-end) and realised (settlement); symmetric (no prudence-based deferral of gains).
- **AS 11 does NOT capitalise exchange differences into asset cost** (default → P&L).
- **Para 46/46A relief (optional, time-bound):** a company MAY (i) add exchange differences on **long-term** foreign-currency monetary items funding a **depreciable capital asset** to that asset's cost (depreciate over life), and (ii) accumulate other long-term differences in **FCMITDA**, amortised over item life (not beyond 31 Mar 2020). "Long-term" = **12 months or more** at origination; option applied **consistently to ALL** such items. **Verify current applicability/cut-off in ICAI material.**
- Revenue/purchases (income-statement lines) stay **frozen at transaction rate** — only monetary *balances* move.
- **Average rate** allowed for many similar transactions — **NOT** if rates fluctuate significantly.

### Forward exchange contracts
- **(a) Hedge of an existing recognised asset/liability (not speculative/firm-commitment):**
  - **Premium/discount** = (forward rate − spot at inception) × amount → **amortise over contract life** (time-apportioned, straddling year-ends).
  - **Exchange difference** = change in **spot** × amount → **P&L**.
  - Cancellation/renewal profit/loss → P&L.
- **(b) Speculative, OR hedge of firm commitment/forecast transaction:**
  - **No premium/discount amortisation.**
  - **Mark to market:** gain/loss = amount × (forward rate now quoted for remaining maturity − contract rate) → **P&L**. Compare against **current forward rate for the remaining maturity, NOT spot.**

### Foreign operations — integral vs non-integral
- **Non-integral indicators (autonomy):** transacts mostly in own local currency; day-to-day autonomy; local financing/sales/costs; parent's cash flows insulated (only dividends/net investment); local pricing; active local market.
- **Integral** = extension/conduit of parent (foreign sales depot reselling parent's goods; overseas purchasing office).

| Item | INTEGRAL | NON-INTEGRAL |
|---|---|---|
| Monetary A & L | Closing rate | Closing rate |
| Non-monetary A & L | Historical (transaction) rate | **Closing rate** (all A & L) |
| Income & expenses | Transaction/average rate | Transaction/average rate |
| Exchange difference | **P&L** | **FCTR (equity)** |

- Non-integral: net difference → **Foreign Currency Translation Reserve (FCTR)** in equity, **recycled to P&L only on disposal**. Goodwill & fair-value adjustments on acquisition = assets of that operation → **closing rate**.
- Integral: depreciation at the **same historical rate as the asset**; COGS at the rate of the related inventory (not blanket average).
- **Change in classification** = prospective from date of change.
- A **long-term intra-group monetary item** whose settlement is neither planned nor likely = part of **net investment**; its differences go to **FCTR in consolidated** statements (but to P&L in separate statements).

## Journal entries
```
Purchases/Asset A/c   Dr   To Creditor (foreign) A/c        (initial: foreign amt × spot)
Forex Loss A/c        Dr   To Creditor (foreign) A/c        (year-end: closing − recorded)
Creditor A/c  Dr / Forex Loss A/c Dr   To Bank A/c          (settlement)
Debtor (foreign) A/c  Dr   To Forex Gain A/c                (receivable, favourable move)
Premium on Forward A/c Dr  To Bank/Forward Payable; then P&L Dr To Premium (amortise)
FCTR A/c              Dr/Cr (balancing figure, non-integral translation)
FCTR A/c              Dr   To Profit on Disposal/P&L        (recycle on disposal)
Fixed Asset A/c       Dr   To Foreign Currency Loan A/c     (para 46A: loss added to asset cost)
```

## Worked mini-example (monetary item across two years)
Import steel €100,000 on 1 Jan; spot ₹90 → record steel & creditor at ₹90,00,000.
- 31 Mar year-end, closing ₹93: creditor = €100,000 × 93 = ₹93,00,000 → **exchange loss ₹3,00,000 to P&L (Yr 1)**. Steel stays ₹90,00,000.
- Settle 5 Apr at ₹94: pay ₹94,00,000 vs creditor ₹93,00,000 → **exchange loss ₹1,00,000 to P&L (Yr 2)**.
- Total ₹4,00,000 loss, split ₹3,00,000 + ₹1,00,000. Steel (non-monetary) never re-translated.
- **Advance twist:** a non-refundable advance for a machine is **non-monetary** — NOT re-translated at year-end; machine cost blends advance-date and balance-date rates. If **refundable in cash**, it becomes monetary → re-translate at closing.

## Disclosures
1. Amount of **exchange differences in net profit/loss** for the period.
2. Net exchange differences in **FCTR** (separate equity component) + **reconciliation** opening→closing.
3. If reporting currency ≠ domicile currency: the **reason**, and reason for any change.
4. Change in classification of a significant foreign operation (integral ↔ non-integral): nature, reason, impact on shareholders' funds, and on net profit/loss for each prior period as if changed at start.
5. (If para 46/46A used) the fact of the option and amounts capitalised/in FCMITDA/amortised.
6. **Encouraged:** foreign-currency risk management policy.

## Exam traps & must-remember
- **Never re-translate non-monetary items** (inventory, PPE, advances, prepaid) — classify first.
- Advance paid/received for goods = non-monetary; the word "refundable" flips it to monetary.
- Book the year-end difference on monetary items — don't wait for settlement.
- Year 2 baseline = prior year-end rate, not origination rate.
- Never restate revenue/purchases to closing rate — only monetary balances move.
- Non-integral differences → FCTR (equity), not P&L; integral → P&L, no reserve.
- Forward: premium = (forward − spot at inception) amortised over life; exchange difference = spot movement to P&L. Don't amortise a speculative forward's premium.
- Time-apportion premium across a straddling year-end.
- Speculative forward marked against current **forward** rate for remaining maturity, not spot.
- Fair-valued non-monetary item → rate on date FV determined.
- Integral vs non-integral misclassification changes every number.
- On disposal of non-integral operation, recycle FCTR to P&L (else understate gain/loss).
- Post-balance-sheet rate change = non-adjusting event (AS 4) — don't use it; use closing rate as at B/S date.
- Average rate not permitted if rates fluctuated sharply.
- Para 46A: optional, long-term (12m+), consistent to all, time-bound — verify cut-off.

## One-line recall
- Monetary = water → closing rate; non-monetary = ice → historical rate.
- Test = settled in money (monetary) vs goods/ownership (non-monetary); advance = non-monetary, loan = monetary.
- Monetary differences → P&L now (both unrealised & realised); revenue/purchases frozen.
- Re-baseline to last reported amount, never to origination in later years.
- Forward (hedge): amortise premium + spot difference to P&L; speculative = mark to market vs forward rate.
- Integral → P&L; non-integral → all at closing rate, difference to FCTR, recycled on disposal.
