# The Equity Playbook: 10 Concrete Setups

## Why this matters — the pro vs retail gap this closes

Retail traders collect *indicators*; professionals collect *setups*. An indicator tells you what happened; a setup is a complete, pre-defined package: entry trigger, stop location, target, the market regime it works in, and the position size. The difference is that a setup can be back-tested, journaled, and repeated — and a "feeling about RSI" cannot. Your TA guide taught you candlesticks and patterns; this chapter turns that vocabulary into **10 mechanical plays** you can run on NSE cash and index instruments. The honest truth first: most retail traders lose money net of costs, and the main reasons are (1) trading every setup in every regime, and (2) sizing by gut. A playbook fixes the first; risk-first sizing fixes the second. No setup here has an edge above ~55% hit rate — the edge lives in *selection, regime-matching, and R-multiples*, not in a magic entry.

## The essentials — the 10 setups

*(Costs referenced are current as of July 2026 — intraday equity STT 0.025% on sell, delivery 0.1% buy+sell, plus brokerage + exchange txn + 18% GST + stamp duty. Verify on your broker/NSE/SEBI; rules change.)*

Regime tags: **TREND** (index trending, India VIX rising or > 14), **RANGE** (VIX low < 12, choppy), **ANY** (works in most conditions with discipline).

| # | Setup | Regime | Entry trigger | Stop | Target | Notes / filter |
|---|---|---|---|---|---|---|
| 1 | **Opening Range Breakout (ORB)** | TREND | Break of the 9:15-9:30 15-min range high (long) / low (short) | Other side of the 15-min range | 1× to 2× the range width | Best on gap-and-go days; skip if range < 0.3% (no energy). Avoid on flat expiry mornings. |
| 2 | **VWAP reversion** | RANGE | Price stretches 1.5-2% from VWAP then prints a rejection candle back toward it | Beyond the stretch extreme | VWAP (the mean) | Only in low-VIX, no-news chop; deadly in trends. Use anchored VWAP from the open. |
| 3 | **Gap-fill** | ANY (fade) | Moderate gap (0.3-0.8%) *into* prior day's range that stalls in first 20 min | Above the gap high (for a short-to-fill) | Previous close (the gap origin) | Fade gaps *into* range; never fade a large gap into empty space (that continues). |
| 4 | **Breakout-retest** | TREND | Price breaks a level, pulls back, holds the level as support, then resumes | Just below the retested level | Measured move = pattern height | The highest-quality long. Waiting for the retest filters 60% of false breakouts. |
| 5 | **Trend pullback (MA)** | TREND | In an uptrend, price pulls to rising 20-EMA (or 50-EMA on daily) and prints a reversal candle | Below the pullback swing low | Prior swing high, then trail | Trade *with* the higher-timeframe trend only. Don't buy the first touch in a downtrend. |
| 6 | **52-week-high momentum** | TREND | Stock makes a new 52w high on above-average volume; buy the break or first pullback | Below breakout day's low / 8-10% swing (positional) | Trail; no fixed target on strong momentum | Volume must expand > 1.5× 20-day avg. Weak-volume new highs fail. |
| 7 | **Range-fade** | RANGE | Price tags a well-defined multi-day support/resistance and rejects | Just beyond the range boundary | Opposite side of the range | Needs ≥ 2 prior touches to define the range. First breakout of the range invalidates it. |
| 8 | **First red / first green day** | ANY | After an extended run, the first strong counter-day signals momentum exhaustion / reset | Beyond that day's extreme | 1-2 day mean-reversion move | A positional/swing timing tool, not a scalp. Confirm with volume and breadth. |
| 9 | **Inside bar** | ANY | A daily/hourly bar fully inside the prior bar's range; enter on break of the mother bar | Other end of the mother bar | 1× mother-bar height, then trail | Tight, defined risk. Best when it forms at a key level or after a trend pause. |
| 10 | **Sector-leader** | TREND | Trade the *strongest* stock in the day's leading sector (e.g. IT if Nifty IT leads) | Stock's structural swing low | Trail with the sector | Rank sectors by % change at 9:45; the leader's leader has the cleanest trend. |

## Worked example — ORB on Infosys (real numbers)

**Setup #1, TREND day.** Nifty gaps up +0.5%, IT leads. Infosys (INFY) opens 1,590.

- **9:15-9:30 range:** high 1,598, low 1,584 → range width **₹14**. That's ~0.9% — enough energy.
- **Entry:** 1,598.50 on the 15-min high break, on rising volume.
- **Stop:** below the range low, **1,583** → risk = **₹15.50/share**.
- **Target 1:** 1× range = 1,598 + 14 = **1,612**; **Target 2:** 2× = **1,626**.
- **Sizing:** ₹5,00,000 capital, per-trade risk 0.4% = **₹2,000**. Shares = 2,000 ÷ 15.5 ≈ **129 shares** (round to 125). Position value ≈ ₹2,00,000 (needs MTF or delivery cash; verify intraday margin with your broker).
- **Outcome:** exits half at 1,612 (+₹1.75k on 62 shares = ~₹875), trails the rest, second half stops at breakeven-plus. **R-multiple ≈ +1.0R to +1.3R.**
- **Costs check (intraday, both legs ≈ ₹4L turnover):** STT 0.025% on ~₹2L sell ≈ ₹50; brokerage (₹20 flat/leg typical discount broker) ₹40; exchange txn ≈ ₹12; GST 18% on (brokerage+txn) ≈ ₹9; stamp ≈ ₹6 → total ≈ **₹120**. A +₹875 gross trade nets ~₹755. On a 129-share loser (−₹2,000), costs still apply — **your edge must clear costs on every scalp**, which is why sub-1R scalping rarely survives.

## How pros do it / common mistakes

**How pros do it:** They run **2-3 setups they've mastered**, not all ten. Each setup is tagged to a regime and they *sit out* when the regime doesn't match — a range-fader does nothing on a strong trend day, and that discipline *is* the edge. They journal every trade by setup name, so after 100 trades they know which setup pays them and cut the rest. They take partial profits and trail, converting hit-rate into R-multiples. They accept a 45-55% win rate and win because winners run 1.5-2R while losers are capped at 1R.

**Classic retail errors & red flags:**
- Running all 10 setups simultaneously → forcing trades in the wrong regime (fading a runaway trend, chasing breakouts in chop).
- No range/volume filter on ORB → trading a 0.15% opening range that's pure noise.
- Fading large gaps into empty space (setup #3 misused) — the single most expensive beginner mistake.
- Moving the stop "to give it room" — the fastest path to a −4R loss.
- Ignoring the cost stack and over-trading: 20 scalps/day at ₹120 each = ₹2,400 of guaranteed friction before any P&L.
- No position sizing — same quantity on a ₹15 stop and a ₹60 stop, so one loser wipes four winners.

## Checklist / drill

**Per-trade checklist (before every entry):**

1. [ ] Which named setup is this? (If you can't name it, don't take it.)
2. [ ] Does today's regime (VIX, trend/range) match the setup's tag?
3. [ ] Exact entry trigger, stop level, and first target written *before* entry.
4. [ ] R:R ≥ 1.5? If not, skip.
5. [ ] Shares = (per-trade risk ₹) ÷ (entry − stop). Never override this.
6. [ ] Does expected profit clear the cost stack comfortably?
7. [ ] Am I within my daily max loss? (If two stops already hit, stop trading.)

**Drill (30 sessions):** Pick **one** setup (e.g. Breakout-retest #4). Paper- or micro-trade *only that setup* for 30 sessions. Log entry, stop, target, regime, R-multiple, and cost. At the end, compute win rate, average R, and expectancy = (win% × avg-win-R) − (loss% × avg-loss-R). If expectancy > 0 after costs, size up; if not, the setup — or your execution of it — has no edge, and no amount of new indicators will fix that.
