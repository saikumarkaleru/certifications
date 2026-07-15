# Costs, Record-Keeping & P&L

## Why this matters — the pro vs retail gap this closes

Ask a retail trader "what did that Bank Nifty scalp actually cost you?" and you get a blank stare. They watch the gross P&L on Kite and assume that's the money. It isn't. The Indian charge stack — brokerage + STT + exchange txn + SEBI + GST + stamp duty — silently eats the edge, and for high-frequency options traders it is frequently the difference between a positive gross strategy and a negative net one. SEBI's FY24 data showed loss-making F&O traders paid **~28% of their net losses as transaction costs**; even profitable ones bled a big slice. The professional knows their cost-per-round-trip to the paisa, tracks **net** returns only, and keeps books clean enough to survive an audit. This chapter turns cost-blindness into cost-mastery.

*(Rate structure current as of 2026; STT figures reflect the 01-Apr-2026 Budget-2026 changes. Verify on your broker's charge sheet, NSE circulars, and SEBI — rules change.)*

## The essentials — the full charge stack

Every trade in India is hit by a stack of charges. As of **01-Apr-2026**:

| Charge | Equity delivery | Equity intraday | Futures | Options |
|---|---|---|---|---|
| **Brokerage** | ₹0 or flat (broker) | flat ₹20/order (typical) | flat ₹20/order | flat ₹20/order |
| **STT** | 0.1% buy + 0.1% sell | 0.025% on **sell** | ~0.05% on **sell** | ~0.15% on **premium (sell)** & on exercise |
| **Exchange txn charge** | ~0.00297% | ~0.00297% | ~0.00173% | ~0.03503% on premium |
| **SEBI charge** | ₹10 per crore | ₹10 per crore | ₹10 per crore | ₹10 per crore |
| **GST** | 18% on (brokerage + txn + SEBI) | same | same | same |
| **Stamp duty** | 0.015% buy | 0.003% buy | 0.002% buy | 0.003% buy |

(Commodities: add **CTT ~0.01% on sell** for non-agri futures. Rates are indicative — pull exact numbers from your broker.)

**Key truths:**
- STT and exchange txn on options are on **premium**, not notional — but options premium turnover is huge, so it adds up fast.
- GST applies to brokerage + txn + SEBI charges, not to STT/stamp.
- **Contract note** is the legal record: it lists every charge line-by-line per trade, is issued daily (T-day), and is what your CA/audit relies on. Reconcile it, don't trust screen P&L.

## Worked example — one Bank Nifty option round-trip

Bank Nifty lot size **35** (verify current lot with NSE — it changes). You buy 1 lot of a weekly call at premium **₹300** and sell at **₹340**. (Illustrative option txn/STT rates used; confirm live.)

**Gross:** (340 − 300) × 35 = **+₹1,400**.

Now the costs:
- **Brokerage:** ₹20 buy + ₹20 sell = **₹40**.
- **STT** (0.15% on sell premium): 0.0015 × (340 × 35) = 0.0015 × 11,900 = **₹17.85**.
- **Exchange txn** (~0.03503% on both legs' premium): 0.0003503 × (300×35 + 340×35) = 0.0003503 × (10,500 + 11,900) = 0.0003503 × 22,400 = **₹7.85**.
- **SEBI:** ₹10/crore × 22,400 turnover ≈ **₹0.02**.
- **GST** (18% on brokerage + txn + SEBI): 0.18 × (40 + 7.85 + 0.02) = **₹8.62**.
- **Stamp duty** (0.003% on buy premium): 0.00003 × 10,500 = **₹0.32**.

**Total charges ≈ ₹74.66.** **Net P&L = 1,400 − 74.66 = ₹1,325.34.**

That single trade lost **~5.3% of gross to costs**. Now imagine a scalper doing 20 round-trips a day: even at a ₹40-tick win each, costs compound, and on **losing** or break-even trades the charges are pure bleed. A trader who is right 55% of the time on ₹40 moves can still be **net negative** once the stack is applied. This is why costs, not signals, decide F&O survival.

## How pros do it / common mistakes

**How pros do it**
- They compute a **cost-per-round-trip** for each instrument and bake it into the strategy: a scalp must clear its cost by a comfortable margin before it's worth taking.
- They track **net (post-cost) returns** in their own sheet, reconciled against the broker's **tax-P&L and ledger** (Zerodha Console, Groww reports) — never eyeball P&L.
- They **read contract notes daily**, matching every charge line; discrepancies (wrong STT, extra brokerage) get raised immediately.
- They keep **digital books**: trade log, ledger, contract notes, bank statements, expense invoices — organised monthly so year-end audit/ITR-3 is a formality.
- They favour **fewer, higher-conviction trades** partly because each trade carries a fixed cost drag.

**Common mistakes**
- Judging a strategy on gross backtest P&L with **zero cost modelling** — the classic reason paper-profitable systems lose real money.
- Over-trading: 50 trades/day where the edge per trade is smaller than the round-trip cost.
- Never downloading contract notes; discovering at audit time the records are a mess.
- Confusing broker "brokerage" (small) with total charges (the stack) and underestimating STT on options.

**Red flags:** you don't know your per-trade cost; your win-rate looks fine but the account keeps shrinking (costs eating you); no organised records when the CA asks.

## Checklist / drill — record-keeping

**Monthly bookkeeping checklist**
- [ ] Download **all contract notes** (daily) and archive by month.
- [ ] Download broker **tax-P&L statement** and **funds ledger**.
- [ ] Update personal **trade log**: date, instrument, qty/lots, entry, exit, gross, charges, net.
- [ ] Reconcile trade-log net vs broker tax-P&L — investigate any mismatch.
- [ ] File **expense invoices** (data, internet, tools, CA) for deduction.
- [ ] Compute **net (post-cost) return %** for the month — the only number that counts.
- [ ] Note **total charges paid** this month as a % of gross P&L (your cost drag).

**Drill:** Take your last 20 trades. For each, compute the exact charge stack (use the table above) and subtract it. Now recompute your win-rate and average net-per-trade. Most traders find their real edge is **half** what the gross numbers suggested — and some discover they're net negative. Repeat monthly until cost-awareness is automatic. *Verify all rates on your broker's live charge list — 2026 rules change.*
