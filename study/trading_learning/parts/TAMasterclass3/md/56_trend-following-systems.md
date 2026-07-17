# Trend-Following Systems

## Origin & idea

Trend-following is the oldest, best-documented, most rigorously back-tested edge in all of technical analysis. Its lineage runs from the 1800s rice traders of Osaka, through Richard Donchian's channel breakouts in the 1950s, to the legendary **Turtle Traders** whom Richard Dennis and William Eckhardt recruited in 1983 to prove that trading could be taught as a mechanical system — and on to the modern managed-futures industry (AQR, Winton, Man AHL, Millburn) that runs tens of billions of dollars on essentially the same principle.

The idea is philosophically the *opposite* of the mean-reversion setups (OTE, Wyckoff Springs) in the preceding chapters. Trend-following makes no attempt to buy low or catch reversals. It asserts something humbler and statistically robust: **markets occasionally make large, sustained moves; nobody can predict when or which; so build a system that automatically climbs aboard every move early enough to profit, cuts every move that fails quickly and cheaply, and holds the winners for as long as the trend persists.** The edge is not in prediction — it is in an *asymmetric payoff distribution*: many small losses, a few enormous wins. The famous phrase is "cut your losses and let your profits run," and trend-following is that maxim made mechanical.

The defining statistics of a trend system are counter-intuitive and you must accept them to trade one:

- **Win rate is typically 30–45%** — you lose more often than you win.
- **The average win is 2–5× the average loss.** A handful of monster trends pay for a long tail of small stop-outs.
- **Profit is concentrated.** In most trend portfolios, the top ~10% of trades produce *more than 100%* of the net profit; the rest net to roughly zero or a small loss.
- **Drawdowns are long and psychologically brutal** — flat or bleeding for months while waiting for the next big trend. This is the *reason the edge survives*: most people can't stand it, so it doesn't get arbitraged away.

## Exact rules — building a complete system

A trend system needs five components, each fully specified. Below is a concrete, tradeable Indian-market design (call it the "Nifty-Verse Trend System") built from the classic Turtle/Donchian template, adapted for NSE and MCX.

### 1. Universe

Trend-following needs *many* uncorrelated instruments, because you never know which will trend. A diversified Indian basket:

| Bucket | Instruments |
|--------|-------------|
| Equity indices | Nifty 50 fut, Bank Nifty fut, Fin Nifty fut, Nifty Next 50 |
| Liquid F&O stocks | 15–20 names across sectors (Reliance, HDFC Bank, Infosys, Tata Motors, L&T, etc.) |
| Commodities (MCX) | Gold, Silver, Crude Oil, Natural Gas, Copper, Aluminium |
| Currency | USDINR, EURINR futures |

Diversification across *asset classes* is the free lunch: gold may trend while equities chop, crude may run while currencies sleep.

### 2. Entry

The core signal is a **Donchian channel breakout**. Two lengths, dual-system style:

| Rule | Specification |
|------|---------------|
| **System 1 (fast)** | Buy when price closes above the highest high of the last **20 days**; sell short when it closes below the lowest low of the last 20 days. |
| **System 2 (slow)** | Buy on a new **55-day** high; short on a new 55-day low. Catches the biggest trends and never misses one. |
| **Confirmation option** | Require the 50-day EMA above the 200-day EMA for longs (trend filter) to cut whipsaws. |

### 3. Position sizing — the heart of the system

The Turtles sized every position by **volatility (ATR)** so that each trade risked the same fraction of equity regardless of instrument. Define:

- **N = 20-day Average True Range** (the "unit of volatility") for the instrument.
- **Dollar/rupee volatility of 1 contract = N × point value.**
- **Unit size = (1% of account equity) ÷ (N × point value).**

So a volatile instrument (high N) gets a *smaller* position and a quiet one a *larger* position — every position risks ~1% of equity per N of adverse move. This single idea — **volatility parity** — is why the system can hold a dozen instruments without any one blowing up the account.

*Worked sizing.* Account = ₹20,00,000; risk per unit = 1% = ₹20,000. Suppose Nifty futures N (20-day ATR) = 220 points and the point value is ₹50/point per lot (25 qty × ... use current lot economics; here assume ₹50/pt for illustration). Rupee volatility per lot = 220 × 50 = ₹11,000. Unit size = ₹20,000 ÷ ₹11,000 ≈ **1.8 → round to 2 lots**. If Nifty ATR spikes to 330 in a volatile phase, unit size falls to ₹20,000 ÷ (330×50) = 1.2 → 1 lot. The position *automatically shrinks* as volatility rises.

### 4. Stops & pyramiding

| Rule | Specification |
|------|---------------|
| **Initial stop** | 2N below entry for longs (2× ATR). At N-per-1%, a 2N stop risks ~2% per unit. |
| **Pyramiding** | Add one more unit every time price moves **½N** in your favour, up to a max of 4 units, raising the stop 2N below the *latest* add. |
| **Portfolio caps** | Max 4 units per instrument; max ~6 units in one closely-correlated group (e.g., all equity indices); max ~12 units total long or short. |

### 5. Exit

| Rule | Specification |
|------|---------------|
| **System 1 exit** | Exit longs on a **10-day** low (a shorter Donchian in the opposite direction). |
| **System 2 exit** | Exit longs on a **20-day** low. |
| **Catastrophic stop** | The 2N initial stop always applies until the trailing channel exit tightens past it. |

Note the asymmetry: you enter on a 20/55-day extreme but exit on a *shorter* 10/20-day reversal, so winners are given room while losers are cut relatively fast.

## Worked India example

Take **MCX Crude Oil** in a hypothetical 2026 rally. Crude has been ranging around ₹6,200–6,600/bbl (per barrel, MCX quotes; lot = 100 barrels, so ₹1 move = ₹100/lot). The 55-day high sits at **₹6,650**. On a geopolitical supply shock, crude closes at **₹6,710** — a System-2 55-day breakout. Entry triggered.

- **N (20-day ATR)** = ₹180. Point value = ₹100/₹1 move per lot. Rupee volatility per lot = 180 × 100 = ₹18,000.
- Account ₹20,00,000, 1% = ₹20,000 → **unit ≈ 1 lot**.
- **Entry:** long 1 lot at ₹6,710. **Initial stop:** 2N below = 6,710 − 360 = **₹6,350** (risk ≈ ₹36,000 ≈ 1.8%).
- **Pyramid:** every +½N (₹90) add a lot. Crude runs to 6,800 → add lot 2, raise stop to 2N below latest = 6,440. To 6,890 → add lot 3. To 6,980 → add lot 4 (max). Now long 4 lots, average ~₹6,845, trailing stop 2N below the last add.
- Crude trends to **₹7,600** over six weeks. Then it makes a **20-day low** at ₹7,380 → System-2 exit, all 4 lots out around 7,380.
- **P&L:** roughly (7,380 − 6,845 avg) × 4 lots × 100 = **535 × 400 = ₹2,14,000** gross, against an initial risk of ~₹36,000 — about **6R** on the campaign. That single trade can carry a quarter of small losers.

Now the *other* reality: in the same period, the system might have taken 20-day breakouts on Bank Nifty (whipsawed, −1.5%), USDINR (whipsawed, −1%), silver (small win, +0.8%), and Infosys (stopped out, −2%). The crude winner dwarfs them all — that is trend-following working exactly as designed.

## Backtest / edge notes & realistic costs

Trend-following is unusually honest because it back-tests cleanly (fully mechanical, no discretion) and has *out-of-sample* live evidence spanning 40+ years and hundreds of markets. Documented characteristics:

- **Long-run Sharpe ~0.5–0.8** for a diversified single-system trend portfolio — modest, but with *positive skew* and low correlation to equities (it often profits in equity bear markets — "crisis alpha," e.g., 2008).
- **Sensitivity to parameters is low** — 20 vs 25 vs 30-day breakouts all work, which is a sign of a *real* edge, not a curve-fit. Beware any trend system that only works at one magic lookback.
- **Costs matter enormously.** For Indian retail, subtract: brokerage, STT/CTT (STT on equity futures sell-side, CTT on commodity futures), exchange & SEBI fees, stamp duty, and — the big one — **slippage on breakouts**. You are, by definition, buying strength and selling weakness, so you get filled at worse prices than the signal. Realistic all-in cost of 0.05–0.15% per round turn on liquid futures can convert a paper edge into break-even on the fast (20-day) system. The slower (55-day) system trades less and survives costs better.
- **Rollover.** Indian index and commodity futures expire monthly; a trend system must **roll** positions to the next contract, incurring extra cost and basis noise. Build rollover into the backtest or it will overstate returns.
- **Capacity/liquidity.** Confine the universe to liquid F&O names and active MCX contracts; illiquid stock futures produce untradeable slippage on breakouts.

Honest bottom line: the edge is real and durable, but for a retail account the two enemies are **costs** (favouring slower systems and liquid instruments) and **psychology** (the low win-rate and long drawdowns).

## Adaptations for NSE / F&O

- **Trade futures, not cash**, for leverage efficiency and short-selling ability; size by ATR against SPAN margin, and never let total margin utilisation exceed ~50% so pyramiding and volatility spikes don't trigger margin calls.
- **Options as a defined-risk expression.** Instead of a stopped future, express a trend breakout with slightly ITM or ATM options 2–3 months out, or debit spreads — capping loss to premium. Trade-off: theta decay punishes slow trends and you lose the clean ATR-stop mechanics. Best reserved for high-conviction 55-day breakouts.
- **Expiry & gap risk.** Weekly-expiry gamma and overnight gaps can jump a future past its stop. Size for gap risk (this is another reason for the conservative 1% unit) and avoid initiating fresh breakouts into major event nights (RBI policy, US FOMC/CPI, Budget).
- **Sector & index correlation caps** are essential on NSE, where Bank Nifty, Fin Nifty and financial stocks move together — treat them as *one* risk bucket, not five independent bets.
- **Long-only variant for equities.** Because Indian equity indices have a strong upward drift and short-selling stock futures against a rising market bleeds, many retail trend-followers run *long-only* on equities and *long/short* only on commodities and currencies.

## Pitfalls

- **The choppy-market death by a thousand cuts.** In range-bound years (a sideways Nifty), breakout systems whipsaw relentlessly. Adding a trend filter (50/200 EMA, or ADX > 20) reduces false breakouts — at the cost of missing some early entries.
- **Abandoning the system in the drawdown.** The single biggest cause of failure is discretionary interference — skipping the signal that turns out to be the year's big winner, or overriding a stop. The system's edge *only exists if you take every signal.*
- **Over-optimisation / curve-fitting.** Tuning lookbacks to the past decade's best backtest produces a fragile system. Prefer round-number, parameter-insensitive settings and validate out-of-sample and across many markets.
- **Under-diversification.** A trend system on just Nifty and Bank Nifty is *not* trend-following — it's two correlated bets that will be flat-to-losing during any prolonged equity range. Breadth of instruments is the risk control.
- **Ignoring costs and slippage** in the backtest — the most common way a "profitable" trend system turns out to be a break-even one live.
- **Position-sizing neglect.** Skipping ATR-based sizing and using fixed lots means one volatile instrument dominates your risk and a single bad gap can be catastrophic. Volatility parity is not optional.

## Summary

Trend-following is the mechanical embodiment of "cut losses, let profits run": enter in the direction of established strength (a **Donchian 20- or 55-day breakout**), size every position by **volatility (ATR)** so each risks ~1% of equity, stop out cheaply at **2N**, **pyramid** into winners, and exit on a **shorter opposite-direction channel**. It wins only **30–45%** of the time but earns because a few outsized trends pay for a long tail of small losses — a positively-skewed payoff that has survived out-of-sample for four decades across hundreds of markets, precisely *because* its long, painful drawdowns deter most traders from sticking with it. For Indian markets, run it across a **diversified basket** (Nifty/Bank Nifty/Fin Nifty futures, liquid F&O stocks, MCX gold/silver/crude, USDINR), respect correlation caps, favour the slower system to survive **costs, STT/CTT, slippage and rollover**, and consider defined-risk option expressions only for high-conviction breakouts. The honest edge is not prediction — it is **discipline plus diversification plus asymmetric payoffs**; the strategy fails not when it is wrong (it is wrong most of the time) but when the trader lacks the fortitude to take every signal through the drawdowns.
