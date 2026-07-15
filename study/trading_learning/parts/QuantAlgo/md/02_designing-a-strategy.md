# Designing a Trading Strategy

## Why this matters — the pro vs retail gap this closes

Retail traders collect *setups*; pros build *systems*. A setup is "buy when RSI is oversold." A system specifies the universe, the exact entry and exit, the filters, the timeframe, the position size, and the costs — every decision pre-made so that execution is mechanical. The difference matters because a vague setup cannot be tested, cannot be sized, and cannot be improved. This chapter turns a trading *idea* (a hypothesis) into a complete, objective, testable **strategy specification**. Getting this right also inoculates you against the single biggest killer of retail quant efforts — curve-fitting — which starts not in the backtest but here, at design time.

## The essentials — from hypothesis to rules

A strategy is a falsifiable hypothesis plus six mechanical components. Start with the hypothesis in plain English, because it forces you to have an *economic reason* the edge exists.

**1. Hypothesis (the "why").** Example: *"Nifty tends to continue an intraday trend after a strong, wide-range first hour, because institutional order flow persists through the session."* If you can't state why an edge should exist, you're just data-mining noise.

**2. Universe (what you trade).** Be specific: Nifty 50 index futures? Bank Nifty weekly options? The Nifty 100 cash stocks with average daily turnover > Rs 50 crore? A liquid universe controls slippage. Illiquid mid-caps will destroy a backtested edge in real fills.

**3. Timeframe.** Intraday 5-min? Daily close? This determines your data, your costs (intraday STT is 0.025% on sell for equity; F&O differs), and your tax head — **intraday equity is speculative business income, F&O is non-speculative, delivery is STCG/LTCG (FY2026-27)** — *verify with a CA; rules change.*

**4. Entry rule (objective trigger).** No adjectives. Not "when it looks strong." Instead: *"Enter long at the next candle open when the 20-EMA > 50-EMA AND price closes above the previous day's high."*

**5. Exit rule(s).** Stop-loss, target, and/or time-based exit. E.g. *"Stop = entry − 1× ATR(14); target = entry + 2× ATR; force-exit any open position at 15:15 IST."* Exits matter more than entries for most systems.

**6. Filters.** Conditions that switch the system off: no trades on RBI policy / Union Budget days; skip if India VIX > 25; only trade 09:30–14:30 to avoid the noisy open and the close. Each filter must earn its place — see curve-fitting below.

**7. Position sizing.** The rule that maps signal to quantity. The professional default is **fixed-fractional risk**: risk a fixed % of equity per trade (commonly 0.5–1%). Position size = `(Equity × Risk%) / (Stop distance × per-point value)`, then round *down* to whole lots.

**Objective vs subjective — the acid test:** could two strangers, given your rules and the same chart data, place the identical trade? If yes, it's objective and testable. If no, rewrite it.

## Worked example — a full strategy spec

**Hypothesis:** Bank Nifty exhibits opening-range momentum; a decisive break of the first 30-min range in the trend direction tends to run.

| Component | Rule (fully specified) |
|---|---|
| Universe | Bank Nifty index future, current-month, lot size 35 (*verify NSE; lot sizes revise*) |
| Timeframe | 5-min candles, intraday only, T+1 settlement irrelevant (no delivery) |
| Entry | Long: 5-min close above the 09:15–09:45 range high, only if that range width ≤ 250 pts. Short: mirror below range low |
| Stop | Opposite end of the opening range |
| Target | 1.5× the range width from entry |
| Filters | Skip Budget/RBI/monthly-expiry days; skip if India VIX > 22; no new entries after 13:30; one trade per side per day |
| Position size | Risk 1% of Rs 5,00,000 = Rs 5,000/trade; size = Rs 5,000 / (range width × Rs 35) |

**Numeric instance.** Opening range 51,900–52,120 (width 220 pts, within the 250 cap). Long entry on a 5-min close at 52,140. Stop 51,900 (risk 240 pts), target = 52,140 + 1.5×220 = **52,470**.

- Risk per lot = 240 × 35 = Rs 8,400. Position size = Rs 5,000 / Rs 8,400 = 0.59 lots → **round down to 0 lots.** The trade is *too big for 1% risk* on a Rs 5L account. This is the design telling you the truth: either accept ~1.7% risk to trade 1 lot, or you're undercapitalised for Bank Nifty and should be on Nifty (smaller per-point rupee value) or index options with defined risk.
- If you accept 1 lot: risk Rs 8,400, reward if target hit = (52,470 − 52,140) × 35 = 330 × 35 = **Rs 11,550**, before ~Rs 1,300 all-in 2026 costs (STT on futures ~0.05% sell + brokerage + 18% GST stack). Net reward ~Rs 10,250 vs net risk ~Rs 9,700 → real payoff ~1.06R, not the 1.5R the target implied. **Costs shrank your edge — that's why they go in the spec, not the appendix.**

## How pros do it / common mistakes

**How pros do it:**
- **Economic rationale first.** Every rule traces back to *why* the edge should exist (order-flow persistence, mean-reversion after overreaction, risk-premium harvesting). Rules with no story are prime suspects for overfitting.
- **Fewer parameters, wider zones.** A robust system has 2–4 parameters, and it should work across a *range* of each (a target of 1.4× or 1.6× shouldn't flip it from great to terrible). Fragility is the fingerprint of curve-fitting.
- **Design the exit and the sizing before the entry.** Amateurs obsess over entries; survival lives in exits and sizing.
- **Specify costs and taxes at design time.** Bake in 2026 STT/charges; know your tax head.

**Common mistakes / red flags:**
- **Curve-fitting from the start:** adding a filter "because 2019 would've been better with it," using oddly specific numbers (RSI < 27.5, EMA of 43), or a rule that only makes sense for one historical event. If a parameter has a suspiciously precise value, you fit it to the past.
- **Subjective words** ("strong," "clearly," "confirmation") that can't be coded.
- **Too many filters** — each one you add is another degree of freedom to overfit and fewer trades to test on.
- **Sizing by conviction** instead of fixed risk.
- **Ignoring liquidity** — a beautiful spec on illiquid stocks dies on slippage.

## Checklist / drill

**Strategy-spec checklist (all must be YES before backtesting):**
- [ ] One-line economic hypothesis for *why* the edge exists.
- [ ] Universe named with a liquidity floor.
- [ ] Timeframe fixed; tax head and cost model noted (2026 STT/charges).
- [ ] Entry, stop, target, time-exit all objective — two strangers get the same trade.
- [ ] ≤ 4 parameters, each with no suspiciously precise value.
- [ ] Position sizing = fixed-fractional risk, rounded down to whole lots.
- [ ] Every filter has a written justification.

**Drill:** Take one idea and fill the seven-row table above with zero adjectives. Then delete your two "nice-to-have" filters and check the idea still makes economic sense. If removing a filter destroys the logic, the logic was the filter — i.e., you were fitting. Rebuild until the core survives on 3 parameters or fewer.
