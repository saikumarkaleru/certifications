# Brokers, Margins & the Full Cost Stack

## Why this matters

The retail trader picks a broker on brokerage alone — "₹20 flat, cheapest" — and never models the *full* cost stack that actually decides whether a strategy is viable. Brokerage is often the *smallest* line. STT, exchange transaction charges, SEBI fees, GST on brokerage-plus-charges, and stamp duty stack on top, and for intraday and options they can dwarf the ₹20. Pros know their exact round-turn cost per instrument and their **breakeven in ticks/points** before they place a trade — because a scalping edge of 3 points on Nifty futures is pure fantasy once you subtract 1.5–2 points of frictional cost per round-turn. This chapter turns "cheap broker" into a precise per-trade breakeven number.

## The essentials

**Discount vs full-service.** *Discount* brokers (Zerodha, Groww, Upstox, Dhan, Angel) charge flat/zero brokerage, no advice, do-it-yourself platforms (Kite, etc.). *Full-service* (ICICI Direct, HDFC Securities, Kotak) bundle research, RMs, and 3-in-1 accounts but charge percentage brokerage — often 0.3–0.5% on delivery, which is 15–25× a discount broker. For a self-directed trader the discount model wins on cost; full-service suits those who want bundled banking/advice.

**The accounts.** You need a **trading account** (with the broker, to place orders) and a **demat account** (with a Depository Participant, holding shares in electronic form at NSDL or CDSL). Discount brokers bundle both. Delivery shares sit in demat; F&O and intraday don't touch demat (no delivery).

**Margins (F&O).** SEBI mandates **upfront margin = SPAN + Exposure**. SPAN is the exchange's risk-based margin for the worst-case move in your position; Exposure is an additional buffer. **Peak-margin** rules are fully enforced (as of 2026): the clearing corporation snapshots your margin at random intra-day points, and short-margin attracts penalty. There is **no more excessive intraday leverage** — brokers cannot give you 20× on options selling; you post full SPAN+Exposure upfront. **MTF (Margin Trading Facility)** lets you buy *delivery* equity with part payment, broker funds the rest at interest (~12–18% p.a.).

**The charge stack (per trade).** Every trade carries:
1. **Brokerage** — flat (e.g. ₹20 or 0.03%, whichever lower) intraday/F&O; often ₹0 delivery on discount brokers.
2. **STT (Securities Transaction Tax)** — segment-specific (below).
3. **Exchange transaction charge** — NSE/BSE per-segment, small %.
4. **SEBI turnover fee** — ₹10 per crore.
5. **GST — 18%** on (brokerage + exchange txn + SEBI).
6. **Stamp duty** — on buy side, state-set, small.

**STT from 01-Apr-2026 (Budget 2026 — verify on NSE/broker/SEBI, rules change):**

| Segment | STT |
|---|---|
| Equity **delivery** | 0.1% on buy **and** sell |
| Equity **intraday** | 0.025% on **sell** only |
| **Futures** (equity/index) | ~0.05% on **sell** |
| **Options** | ~0.15% on **premium (sell)** and on exercise |
| Commodity non-agri futures (CTT) | ~0.01% on sell |

*(Figures as of July 2026; STT/CTT and exchange rates are revised in Budgets — always reconfirm.)*

## Worked example — breakeven for intraday & F&O

**A) Nifty Futures intraday, 1 lot (lot size 25 — verify current lot).** Nifty at 24,600 → contract value = 24,600 × 25 = **₹6,15,000**. Buy and sell same value roughly.
- Brokerage: ₹20 buy + ₹20 sell = ₹40
- STT (futures sell 0.05%): 0.0005 × 6,15,000 = ₹307.50
- Exchange txn (~0.0019% NSE futures, verify): ~₹23 round-turn
- SEBI (₹10/cr): ~₹1.2
- GST 18% on (₹40 + ₹23 + ₹1.2): ~₹11.5
- Stamp (~0.002% buy): ~₹12

**Total ≈ ₹395** round-turn. On lot size 25, that's **₹395 / 25 ≈ 15.8 points** you must earn on Nifty *just to break even*. A "5-point scalp" is a guaranteed loser here. The dominant cost is STT, not brokerage.

**B) Bank Nifty option buy, 5 lots (lot 15 — verify).** Buy 52000 CE at ₹210, sell at ₹230.
- Premium turnover sell = 230 × 15 × 5 = ₹17,250
- Brokerage: ₹20 + ₹20 = ₹40
- STT (options 0.15% on sell premium): 0.0015 × 17,250 = ₹25.9
- Exchange txn (~0.05% on premium, NSE options — verify): buy 15,750×0.0005≈₹7.9 + sell 17,250×0.0005≈₹8.6 = ₹16.5
- SEBI + GST + stamp: ~₹12
**Total ≈ ₹95.** Small in rupees, but on a cheap OTM strike bought at ₹5 with a wide spread, the *spread* (previous chapter) plus these charges can be 15–25% of premium — the real killer is spread, not this stack.

## How pros do it / common mistakes

**Pros:**
- Compute **round-turn cost in points/ticks** per instrument and demand an edge several times larger.
- Prefer **index futures/near-ATM index options** where cost-per-rupee-exposure is lowest.
- Track **peak-margin** headroom so they never take a penalty.
- Use a broker's **charges calculator** (Zerodha's brokerage calculator, etc.) and reconcile against the **contract note** monthly.

**Retail mistakes:**
- Choosing a broker on brokerage while ignoring the **STT/GST stack**.
- **Over-trading** intraday — 30 round-turns/day × ₹395 = ₹11,850/day of pure cost on Nifty futures.
- Scalping tiny edges that don't clear the **frictional breakeven**.
- Getting **peak-margin penalties** from carrying under-margined positions.
- Confusing MTF interest for "free leverage" — it compounds daily at 12–18%.

## Checklist / drill

- [ ] I know my **round-turn cost in ₹ and in points/ticks** for this instrument.
- [ ] My expected edge is **≥ 3× the frictional breakeven**.
- [ ] I have **SPAN + Exposure** upfront and peak-margin headroom.
- [ ] Delivery vs intraday vs F&O **STT rate** confirmed (2026 slabs).
- [ ] Monthly: reconcile **contract notes** vs a brokerage calculator.

**Drill:** Rebuild the two worked examples above with *today's* live lot sizes and NSE charge rates, then compute your personal breakeven in points for (i) Nifty fut, (ii) Bank Nifty ATM option. Pin that number to your screen. If a setup's target is below it, you don't take the trade.
