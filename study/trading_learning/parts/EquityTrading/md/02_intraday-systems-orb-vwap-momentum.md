# Intraday Systems: ORB, VWAP & Momentum

## Why this matters

You already know candlesticks and indicators. What separates a pro intraday trader from a chart-literate loser is having a **defined system** — a repeatable setup with entry, filter, stop, and target written *before* the market opens — instead of reacting to every wiggle. The retail gap here is discretion masquerading as skill: "it looked like it was breaking out." Pros trade three or four battle-tested Indian-market patterns — Opening-Range Breakout (ORB), VWAP trades, momentum/relative-strength, and gap-and-go — with mechanical rules. This chapter gives you those rules and the India-specific filters that keep them from firing on noise.

## The essentials

All times IST; session 09:15–15:30. Rules as of July 2026 — verify on NSE/broker.

**1. Opening-Range Breakout (ORB).** Define the range as the high/low of the first **N minutes** after 09:15 — commonly the 15-minute range (09:15–09:30). A break *and close* above the range high (with volume) = long; below the low = short. Best on **Bank Nifty** (high range, trends hard) and momentum stocks. The opening range on an index future or liquid stock reflects the overnight order imbalance; a genuine break of it is institutions repricing.

**2. VWAP (Volume-Weighted Average Price).** VWAP is the intraday "fair value" line institutions benchmark against. Two distinct plays:
- **VWAP trend / anchored VWAP:** In a trending session, price holds *one side* of VWAP. Buy pullbacks to VWAP in an uptrend, sell rallies to it in a downtrend. VWAP acts as dynamic support/resistance.
- **VWAP mean-reversion:** In a range-bound, choppy session (common mid-day), price stretched far from VWAP (e.g., >1 standard-deviation band) snaps back. Fade the extreme *only* when there's no trend.
The trap: using the same VWAP tactic in the wrong regime. Trend days punish mean-reversion; range days punish breakout-chasers.

**3. Momentum / Relative Strength (RS).** Rank stocks vs the index. On an up day, buy the stock *outperforming* Nifty (rising while Nifty is flat = leader); short the laggard on a down day. RS is measured simply: stock's % change vs Nifty's % change since open. Leaders keep leading intraday.

**4. Gap-and-Go.** A stock/index gapping up on news at 09:15, holding above the gap in the first 5–15 min, then breaking the opening-5-min high = continuation long. A gap that *fills* (fades back to prior close) fails the setup — don't chase.

**Filters that matter in India:**

| Filter | Why |
|---|---|
| Trade liquid names only (Nifty, Bank Nifty, F&O top-50) | spreads eat illiquid intraday edges |
| Volume confirmation on breakout | low-volume breaks are traps |
| Avoid 12:00–13:30 chop unless mean-reverting | mid-day thins out |
| Skip first 3–5 min raw print | opening auction noise |
| No new intraday entries after ~14:45 | not enough time to work; square-off pressure |
| Event days (RBI policy, Budget, expiry) | separate rules — expect whipsaws |

## Worked example: ORB on Bank Nifty futures

Date-stamped hypothetical, July 2026. Bank Nifty futures (lot size **15**, tick ₹0.05; **verify current lot on NSE** — F&O lot sizes revise). Say the future opens and the **09:15–09:30 range** forms:
- Range high: **52,180**
- Range low: **51,940**
- Range width: 240 points

At 09:34 the 5-min candle **closes at 52,205**, above the range high, on visibly rising volume, with Nifty also green (index confirmation). **Entry long at 52,210.**

- **Stop:** just below the range high that it broke, or below the breakout candle low — say **52,120** (90 points risk). Some use the range midpoint; tighter = more whipsaw.
- **Risk per lot:** 90 pts × 15 × ₹1 (Bank Nifty futures point = ₹1 per index point per unit; ₹1 × 15 = ₹15/point/lot) = 90 × 15 = **₹1,350 risk/lot.**
- **Target:** measured move = range width projected = 240 pts → target **52,450** (1st), or trail with VWAP. 240 pts × 15 = **₹3,600 reward/lot.** Reward:risk ≈ **2.7:1.**

Costs (futures, from 01-Apr-2026): STT ~0.05% on sell side. Sell value ≈ 52,450 × 15 = ₹7,86,750 → STT ≈ ₹393; plus brokerage (~₹40 both legs), exchange txn, SEBI, stamp, **18% GST on brokerage+txn**. All-in round-trip ≈ **₹500–600/lot.** On a ₹3,600 winner that's ~15% cost drag — meaningful, so the setup must have real edge, not a 1:1 target.

If instead the 09:34 candle closed at 52,150 (back inside the range) — **no trade.** The break must *close* outside with volume. Chasing the wick is the retail error.

## How pros do it / common mistakes

**Pros:**
- Pre-mark the opening range and VWAP before 09:30; know their setups by name and wait.
- Demand **confluence**: ORB + index confirmation + volume + RS all pointing the same way. One signal alone is a coin flip.
- Match tactic to **regime**: trend day → VWAP trend & ORB; range day → VWAP fade; never both.
- Size by rupee risk (fixed % of capital), not by "lots I feel like."

**Retail mistakes / red flags:**
- Trading ORB on a **gap-and-fill** morning — the range is meaningless.
- Fading VWAP on a strong trend day and averaging into a runaway loss.
- Chasing breakouts *after* the move (entering at 52,300, not 52,210) — worse R:R.
- Trading illiquid mid-caps where the 15-min range is 3 ticks wide.
- Ignoring expiry-day gamma whipsaws and RBI-day fake breaks.
- Over-trading the noon chop out of boredom.

## Checklist / drill

**Pre-market (before 09:15):** mark prior close, gap size, key levels; note event calendar (RBI/expiry/results).

**At 09:30:** draw the opening range; note VWAP; identify 2–3 RS leaders/laggards vs Nifty.

**Before any entry, tick all:**
- [ ] Which named system is this (ORB / VWAP-trend / VWAP-fade / momentum / gap-and-go)?
- [ ] Regime matches the tactic (trend vs range)?
- [ ] Volume confirms?
- [ ] Index agrees (Nifty direction)?
- [ ] Stop level and rupee risk written down (≤1–2% of capital)?
- [ ] Reward:risk ≥ 2:1 after costs?
- [ ] Time is before 14:45?

**Drill:** For 10 sessions, paper-trade *only* the 15-min ORB on Bank Nifty with the rules above — no other setups. Log break-close-above vs wick-only, and whether volume confirmed. You'll learn to feel the difference between a real break and a trap before risking a rupee.

*Rates, lot sizes, and rules as of July 2026 — verify on NSE/your broker/SEBI; they change.*
