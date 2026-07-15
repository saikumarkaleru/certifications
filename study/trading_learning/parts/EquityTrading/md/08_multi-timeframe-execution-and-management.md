# Multi-Timeframe Execution & Trade Management

## Why this matters — the pro vs retail gap this closes

Two traders take the same stock. One buys on a 5-minute breakout with no idea what the daily chart is doing, gets a good fill, and is stopped out an hour later because the daily trend was down and price mean-reverted straight into his stop. The other checks the *daily* for direction, drops to the *hourly* for structure, and enters on the *15-minute* — same stock, but the trade is aligned with the dominant force. Over a hundred trades, that alignment is the difference between a coin flip and an edge.

The gap this closes: retail trades a single timeframe and treats *entry* as the whole game. Pros treat entry as maybe 20% of it. The other 80% is **trade management** — where the stop is, when it moves to breakeven, when to book partial, and when to *do nothing* and let a winner run. Most retail P&L damage isn't bad entries; it's cutting winners at +1R and letting losers run to −3R. This chapter fixes the management, top-down.

## The essentials — top-down structure

**The three-timeframe stack (choose a ~1:4-6 ratio between them):**

| Role | Swing trader | Intraday trader |
|---|---|---|
| **Trend (context)** | Weekly / Daily | Daily / Hourly |
| **Setup (structure)** | Daily / 4-hour | Hourly / 15-min |
| **Trigger (entry)** | Hourly / 15-min | 5-min / 3-min |

**Rule:** the higher timeframe decides *direction and bias*; you only take lower-timeframe entries *in that direction*. If the daily is up, you buy 15-minute pullbacks/breakouts; you do NOT short 15-minute reversals against it. This one rule removes most low-quality trades.

**Position management building blocks:**
- **Initial stop** placed on the *setup* timeframe (below the structure that would invalidate the trade), not an arbitrary %.
- **1R** = your initial risk per share (entry − stop). All management is measured in R.
- **Scale in:** enter partial on the trigger, add on confirmation (a higher timeframe close, or a retest that holds).
- **Move to breakeven:** once price reaches ~+1R, trail the stop to entry — the trade can no longer lose money. (Don't do this too early or normal noise stops you flat.)
- **Partial booking:** sell a portion (e.g., one-third to half) at a defined target (+1.5R to +2R, or a resistance/prior high) to reduce risk and lock cash.
- **Let the runner run:** trail the remainder on the *setup* or *trend* timeframe (swing low, MA, or ATR chandelier) so the last piece can catch an outsized move.

**India-specific execution notes (2026 — verify on your broker/NSE):**
- Timings 9:15-15:30; the first 15-30 min and last 30 min are the most liquid/volatile. Avoid resting wide stops through the volatile open.
- Use **limit orders** near support to control slippage; **SL-L (stop-loss limit)** for stops, aware that a fast gap can jump a limit stop — for hard protection consider SL-M where offered.
- Costs stack on every scale-in/out: brokerage + STT (delivery 0.1% buy+sell; intraday 0.025% on sell — from 01-Apr-2026) + exchange txn + SEBI + 18% GST on (brokerage+txn) + stamp duty. Over-scaling a small position gets eaten by charges — scale in *meaningful* chunks.
- **SEBI retail algo framework (mandatory 01-Apr-2026):** if you automate any of this scaling/trailing, every algo order needs an exchange Algo-ID via your *registered broker's* API; open/unregistered APIs are banned. Manual discretionary management needs none of this. *Verify current rules on SEBI/NSE.*

## Worked example — an MTF equity swing trade

**Stock:** liquid F&O-universe name, cash/delivery. Capital ₹5,00,000, risk 1% (₹5,000) per trade.

**Top-down read:**
- **Weekly:** uptrend, above rising 20-week EMA → longs only.
- **Daily:** pulling back into a rising 50-DMA at ~₹800, holding support.
- **Hourly (setup):** builds a small base ₹800-₹815; a break of ₹815 triggers.
- **15-min (trigger):** breaks ₹815 on a volume push.

**Entry & sizing:**
- Setup-timeframe (hourly) invalidation: a close below ₹792. Entry ₹816, stop ₹792 → **1R = ₹24/share.**
- Shares = ₹5,000 ÷ ₹24 = **208.** Scale-in plan: buy 140 now, keep 68 for an add.
- Buy 1: **140 @ ₹816 = ₹1,14,240.**

**Add (confirmation):** price closes the hour at ₹828 above the breakout and holds a retest of ₹818. Add the remaining **68 @ ₹826 = ₹56,168.** Blended entry ≈ ₹819, total 208 shares, invested ≈ **₹1,70,400.** Raise stop to **₹805** (below the retest low) — open risk now ≈ 208 × ₹14 = ₹2,912, well under budget.

**Management as it works:**
- Price reaches **₹843** (≈ +1R from blended entry). **Move stop to breakeven ₹819.** The trade is now risk-free.
- Price tags a prior swing high / +2R at **₹867.** **Book partial:** sell 100 @ ₹867 = ₹86,700 (locks ≈ ₹4,800 gross on that half). Remaining: **108 shares.**
- **Let the runner run:** trail the 108 on the daily 20-EMA / swing lows. Over three weeks price grinds to **₹930**, then closes a day below the 20-EMA at **₹918.**
- **Exit runner:** sell 108 @ ₹918 = ₹99,144.

**Result:** proceeds ₹86,700 + ₹99,144 = ₹1,85,844 on ₹1,70,400 invested → **≈ ₹15,400 gross** (minus a few hundred rupees of STT/charges across the scales). Risk taken was ₹5,000; realised ≈ +3R, because the *management* (breakeven move, partial, trailing runner) captured a move far bigger than the initial +2R target — while never risking more than 1%.

## How pros do it / common mistakes

**Pros:**
- **Direction from the top, timing from the bottom** — always aligned.
- **Manage in R, not rupees or emotions.** Breakeven at ~+1R, partial at a planned level, runner trailed on the higher timeframe.
- **Do less to the winner.** Once it's working and stop is at breakeven, they mostly *sit* and let the trail do the exiting.
- **Pre-write the whole plan** — entry, stop, add level, breakeven trigger, partial target, trail rule — *before* entering.

**Retail errors / red flags:**
- Entering on a 5-min signal against the daily trend ("counter-trend martyrdom").
- Moving the stop to breakeven at +0.2R and getting shaken out of every trade by noise.
- Booking the *whole* position at +1R, then watching a +5R move without you.
- Moving a stop *further away* when the trade goes against them (the account-killer).
- Over-scaling a tiny position into 6 tranches and donating the edge to STT/brokerage.
- Managing a swing trade on the 3-minute chart and panic-exiting on intraday noise.

## Checklist / drill

**Per-trade management checklist:**
- [ ] Higher-timeframe trend identified; trade is *with* it.
- [ ] Setup-timeframe structure + invalidation level chosen → defines the stop.
- [ ] 1R (entry − stop) computed; shares = risk-budget ÷ 1R.
- [ ] Scale-in plan: first tranche + add trigger written.
- [ ] Breakeven rule set (move stop to entry at ~+1R).
- [ ] Partial-booking level set (+1.5-2R or a resistance/prior high).
- [ ] Runner trail rule set (swing low / 20-EMA / ATR chandelier) on the setup or trend timeframe.
- [ ] Managing on the *setup* timeframe, not the trigger timeframe — no panic exits on noise.

**Drill:** Take 10 past trades on your charts. For each, mark: higher-TF trend, entry, initial stop (1R), the +1R breakeven point, a +2R partial, and where a 20-EMA trail would have exited the runner. Compare the disciplined-management result to what you actually did. Almost everyone finds the same lesson — their entries were fine; their management gave the edge back. Fixing that, not finding a better indicator, is the leap to professional.

*STT, GST, settlement, and the SEBI retail-algo rules cited are as of 2026 (Budget 2026 / effective 01-Apr-2026). Verify current charges, order types, and algo requirements on NSE, your broker, and SEBI — rules change.*
