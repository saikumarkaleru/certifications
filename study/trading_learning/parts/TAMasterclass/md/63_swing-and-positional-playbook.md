# The Swing & Positional TA Playbook

## What it is & why it works

A swing and positional playbook is the multi-day extension of technical trading: a written framework for holding an NSE position across days (swing: 2-15 sessions) to weeks or months (positional: several weeks to a few quarters), driven primarily by the daily and weekly charts. Where the intraday trader lives inside the auction of a single session, the swing/positional trader steps back to trade the *trend* — the larger, slower move that the daily candle records and the weekly candle confirms.

It works because of three structural realities of Indian equities:

1. **Trends persist on higher timeframes.** The daily and weekly charts filter out the intraday noise that makes the 5-minute chart a near-coin-flip. A stock that has broken out of a multi-month base on the weekly, with rising volume and improving relative strength, tends to keep going — because the same institutional accumulation, earnings re-rating, or sector rotation that started the move continues to play out over weeks. You are riding a fundamentally-driven move using a technical map.

2. **You harvest overnight and multi-day drift.** Much of the market's return arrives in gaps and multi-session runs that the intraday trader, flat by 15:20, never captures. Swing/positional trading is designed to *be there* for the gap-up after results, the follow-through day after a breakout, the trend leg after a sector catches a bid.

3. **Lower decision frequency reduces error and cost.** Fewer trades means fewer chances to break rules, lower brokerage/STT drag, and time for a thesis to work. The trade-off is overnight and weekend risk — gaps against you from global events, results, RBI policy, or news you cannot exit around. The playbook exists to size and structure around exactly that risk.

The core philosophy is *trade the trend, on the right timeframe, with a wide-enough stop that daily noise doesn't shake you out, sized so that a normal loss is small.* The enemy is not being wrong — it is being wrong *big*, or being shaken out of a right trade by a stop placed inside the noise.

## The mechanics

A swing/positional playbook has six modules: **universe & screening, trend/stage classification, setup selection, entry & stop construction, position sizing & pyramiding, and management/exit.**

### 1. Universe & screening

Trade liquid names with clean trends. A practical India universe: Nifty 50 and Nifty Next 50 constituents, liquid F&O stocks, and quality mid-caps with real delivery volume. Screen on Chartink/TradingView for:

| Filter | Typical criterion | Purpose |
|---|---|---|
| Trend | Price > 50-DMA > 200-DMA (rising) | Only trade uptrends (for longs) |
| Relative strength | Outperforming Nifty over 3-6 months | Leaders, not laggards |
| Base/structure | Consolidation, flag, or cup near highs | Low-risk entry point |
| Volume | Rising on up-moves, drying up in the base | Accumulation signature |
| Liquidity | Avg daily value > ₹20-50 cr | Clean fills, real stops |

### 2. Stage / trend classification (Weinstein)

- **Stage 1 — Basing:** sideways after a decline, 200-DMA flattening. Accumulate/watch.
- **Stage 2 — Advancing:** breakout above the base, price and 200-DMA rising. **This is where longs belong.**
- **Stage 3 — Topping:** choppy, 200-DMA flattening after a run. Tighten/exit.
- **Stage 4 — Declining:** downtrend, price < falling 200-DMA. Avoid longs; candidates for shorts (via futures).

### 3. Setup selection (a handful, no more)

| Setup | Trigger | Timeframe |
|---|---|---|
| Base/flag breakout | Close above a multi-week base on volume | Swing → positional |
| Pullback to rising 20/50-EMA | Reversal candle at MA support in an uptrend | Swing |
| Higher-low trendline bounce | Bounce off a rising trendline / prior breakout level (support flip) | Swing/positional |
| Weekly breakout | Weekly close above long consolidation | Positional |

### 4. Entry & stop

- **Entry:** on the breakout close, or on the lower-risk *retest* of the breakout level / MA. Daily-close confirmation avoids intraday fakeouts.
- **Stop:** below the base low, the pullback swing low, or a chosen multiple of ATR (e.g. 2-2.5× the 14-day ATR) so daily volatility doesn't stop you out. Weekly-close-based stops for positional trades.

### 5. Sizing & pyramiding

- **Risk per position:** 0.5-1% of capital, occasionally up to 1.5% for A+ weekly setups.
- **Size = Risk ÷ (entry − stop).** A wider swing stop means a *smaller* position — this is correct and protective.
- **Pyramid:** add on strength as the trade proves itself (e.g. after a +1R move and a new higher low), moving the aggregate stop to breakeven. Never add to a loser.
- **Portfolio heat:** cap total open risk (sum of all positions' risk) at ~4-6% so a correlated drawdown across, say, three banking names can't cripple the account.

### 6. Management & exit

Trail with a rising 20/50-EMA, a swing-low trendline, or a chandelier (ATR) stop. Scale out into strength; keep a runner for the trend. Exit on a decisive stage-3 topping structure, a break of the trailing structure on volume, or a fundamental thesis break.

## Reading it — a worked example: Reliance positional swing

Assume Reliance has spent four months in a base between ₹2,850 and ₹3,050 after a prior uptrend — a textbook **Stage 1 → Stage 2** transition setting up.

**Screen & context:** Reliance is above a flattening 200-DMA (~₹2,900) that is beginning to curl up. Relative strength vs Nifty has quietly improved over the last month. Volume in the base is drying up — the accumulation signature. The Nifty itself is in an uptrend, and energy/oil-to-telecom sentiment is constructive. This passes the universe, trend and structure filters.

**The setup (weekly breakout):** On a Wednesday, Reliance closes at ₹3,090 — a decisive daily close above the ₹3,050 base ceiling — on volume roughly 1.8× its 20-day average. The next day it holds ₹3,060 on a pullback (a clean retest of the breakout level, which has now flipped from resistance to support).

**Entry construction:**
- Entry on the retest hold: ₹3,070
- Stop: ₹2,975 — below the retest low and just under the 50-DMA, wide enough that normal daily swings (ATR ~₹55) won't shake me out. Risk = ₹95/share.
- On ₹5,00,000 capital at 1% risk (₹5,000), size ≈ 52 shares (₹5,000 ÷ ₹95). Notional ≈ ₹1.6 lakh.

**Measured move & targets:** the base height is roughly ₹200 (₹3,050 − ₹2,850). Projected from the breakout, that gives a first objective near ₹3,250. Prior swing structure and a round number reinforce ₹3,300 as a second target.

**How it plays out:**
- *Week 1-2:* price advances to ₹3,180. I move the stop up to breakeven (₹3,070) after it prints a higher low at ₹3,110. Risk is now zero.
- *Week 3:* it tags ₹3,255 (Target 1). I scale out one-third (~17 shares) for +₹185/share (~1.9R on that portion) and trail the rest below the rising 20-EMA (~₹3,150).
- *Week 4-6:* a clean Stage-2 advance carries it to ₹3,380 with a shallow pullback to the 20-EMA that holds. I add a small pyramid tranche on the higher low, aggregate stop trailed to ₹3,240.
- *Week 8:* the tape turns choppy near ₹3,420, volume on up-days fades, and a red weekly candle closes below the 20-EMA — early Stage-3 behaviour. The trailing stop at ₹3,300 takes me out of the remainder for roughly +₹230/share.

**Net:** a multi-week hold that captured the meat of a ~₹350 move on a ₹95 initial risk — a blended outcome of roughly 2.5-3R, with the account never exposed to more than 1% at entry and zero after the breakeven move. That is what the higher timeframe pays you for: patience and a wide, structural stop.

## Trading it — entries, stops, targets, scenarios

**Entries:** prefer the *retest* over the raw breakout for a tighter, lower-risk entry, accepting that the strongest movers occasionally run without looking back (you catch those on the breakout close or via a small starter position). Always require a daily *close* beyond the level; wicks lie.

**Stops:** the cardinal swing rule is *the stop lives outside the noise.* Use 2-2.5× ATR, or below the structural swing low / base low, whichever gives the position room. If the resulting position feels "too small", that is the volatility telling you the honest size — do not tighten the stop to justify a bigger position.

**Targets:** measured moves (base height, flag pole), prior swing highs, and round numbers give logical objectives. Scale out — book a third into the first target, trail the rest. The runner is where positional edge compounds.

**Scenarios:**
1. *Clean trend:* trail with the 20/50-EMA or rising swing lows; add on higher lows; let it run for weeks.
2. *Breakout fails (back inside base):* exit on the close back inside — a failed breakout is a distinct, respect-it signal, often a short setup.
3. *Overnight gap against you past the stop:* accept the gap loss; do not average down hoping to recover. This is the overnight-risk premium you knowingly sold when you chose to hold.
4. *Results/event mid-hold:* decide *in advance* — reduce size into results, or accept the binary. Never be surprised by a scheduled event.
5. *Sideways drift:* if the trade goes nowhere for weeks and ties up capital and risk, exit and redeploy — opportunity cost is real.

## Confluence — stacking the odds

- **Multi-timeframe alignment:** the daily setup should sit inside a weekly uptrend, which sits inside a rising index and a strong sector. A base breakout in an IT name is far stronger when the Nifty IT index and Nifty itself are both trending and IT is the leading sector on relative strength.
- **Relative strength & sector rotation:** buy the *leaders* of the leading sector. In 2024-25 India, rotation between banks, autos, capital-goods/PSU, pharma and IT has been the dominant swing driver — trade the sector catching the bid, not last quarter's winner.
- **Volume & delivery:** breakouts on rising volume and high delivery percentage signal real accumulation; low-volume breakouts are suspect.
- **Options/OI for index & F&O stocks:** for positional index or single-stock F&O trades, monthly OI walls mark durable support/resistance; a breakout that also clears a heavy Call OI strike has room to run. FII/DII flow data and futures OI build-up (long build-up = price up + OI up) corroborate the trend.
- **Fundamental tailwind:** the best positional technical setups coincide with an earnings re-rating, order-book visibility, or a macro tailwind. TA times the entry; fundamentals fuel the multi-month leg.
- **Market breadth:** advance-decline and % of stocks above their 200-DMA confirm whether a rising tide is broad (durable) or narrow (fragile).

The A+ positional trade is a Stage-2 breakout, in the leading sector, with rising volume, positive relative strength, a supportive index and a real fundamental story — five factors aligned. Those are rare; wait for them.

## Pitfalls & false signals

- **Stops too tight for the timeframe.** The commonest swing error: a 1% stop on a stock with 2-3% daily range. You get shaken out of the right trade repeatedly. Use ATR-based, structural stops and let size absorb the width.
- **Ignoring overnight/event risk.** Holding a full position into results, RBI policy, US CPI/FOMC, or an election result is selling a binary you didn't price. Reduce size or hedge.
- **Chasing extended breakouts.** Buying a stock already 15-20% above its base, far from any support, gives a terrible risk/reward — the stop is miles away. Buy near the base, the retest, or the MA pullback, not the vertical.
- **Overtrading a positional book.** Swing/positional edge comes from *holding*. Micromanaging daily, exiting on every red candle, destroys the very trend-capture you set out to do.
- **Portfolio correlation blindness.** Five "different" longs that are all PSU banks are one big bet. Cap correlated heat.
- **Fighting the stage.** Buying Stage-4 downtrends because they look "cheap" is how positional accounts bleed. Only long Stage 2.
- **Anchoring to a target and refusing to trail.** Rigid targets leave the fat tail of a big trend on the table; a mechanical trailing stop lets winners run.
- **Confusing a base breakout with a bull trap.** Filter with volume, index alignment, and a close (weekly close for positional). A breakout the whole market rejects the next session is a trap.

## Interview-ready summary

"Swing and positional trading is trading the trend on the daily and weekly charts — holding days to months to capture the multi-session move an intraday trader misses. I screen a liquid universe for Stage-2 uptrends: price above rising 50- and 200-DMAs, positive relative strength versus Nifty, and a tight base or MA pullback near highs on drying-up volume. I enter on a daily-close breakout or its retest, and — this is the key discipline — I place a wide, structural or ATR-based stop *outside* the daily noise, then size the position so that stop still risks only about 1% of capital. A wider stop means a smaller position, not a tighter stop. I trail with a rising 20/50-EMA or swing lows, scale out into measured-move targets, pyramid on higher lows, and cap total portfolio heat around 4-6% so correlated names can't sink me. Confluence — weekly trend, leading sector, rising volume, supportive index and a fundamental tailwind — separates the A+ trade from the average one. The overnight and event gap is the risk I'm paid to hold; I manage it by sizing and by never averaging a loser. The edge is patience: the trend does the work if my stop lets it."
