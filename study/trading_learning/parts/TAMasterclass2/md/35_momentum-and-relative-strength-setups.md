# Setups: Momentum & Relative Strength (5 setups)

Momentum and relative strength (RS) are the closest thing technical analysis has to a genuine market anomaly that survives out-of-sample testing across decades and geographies. The core empirical fact is simple and stubborn: instruments that have been strong tend to keep being strong for the next few weeks to months, and instruments that have been weak tend to keep being weak. Academic finance calls this "cross-sectional momentum" and it works on Indian equities too — a portfolio of the top-decile 6-month performers on the NSE has historically outrun the bottom decile by a wide margin, before costs. For a discretionary technical trader this abstract edge becomes concrete in a handful of repeatable setups. This chapter builds five of them, each with exact rules and an India-first worked example. The unifying idea across all five: **do not fight strength, and do not buy weakness hoping it is cheap.** Buy what the market is already voting for, time your entry with price structure, and let relative strength tell you which horse to back.

Two definitions before we begin, because traders confuse them. **Absolute momentum** (also "time-series momentum") asks: is this instrument itself going up? You measure it against its own past — price above the 200-DMA, a rising rate-of-change, a fresh 52-week high. **Relative momentum / relative strength** asks: is this instrument going up *more than* its peers or its benchmark? You measure it as a ratio — stock price divided by Nifty, or a sector index divided by Nifty. The best setups stack both: an absolute uptrend that is *also* outperforming its benchmark. That combination — strong and strongest — is where the fat tails of return live.

## Why momentum & relative strength work

There are three durable engines. First, **information diffuses slowly.** When Persistent Systems or Dixon Technologies posts a genuinely transformational quarter, the full re-rating does not happen in one candle; institutions accumulate over weeks, analyst upgrades trickle in, and the stock trends. Second, **herding and career risk** — a fund manager who is underweight the year's strongest sector faces client questions, so flows chase strength, extending it. Third, **the disposition effect**: retail sells winners too early and holds losers too long, which paradoxically *creates* under-reaction to good news (winners stay cheap relative to fundamentals for a while) and over-supply in losers. All three mean price has memory. Relative strength simply ranks that memory across the universe so you deploy capital where the collective bid is strongest.

The honest caveats: momentum works until it violently doesn't. Its worst enemy is the sharp mean-reversion "momentum crash" that follows a panic bottom — think the V-shaped recovery of April–June 2020, or the March 2023 Adani-driven washout reversing, where the previous laggards (PSU banks, capital goods) suddenly led and the crowded momentum names (high-multiple tech) lagged. So every setup below carries a regime filter and a hard stop. Momentum is a high-win-rate-in-trends, ugly-drawdown-in-reversals strategy. You manage it with position sizing and exits, never with conviction alone.

## The relative-strength toolkit (settings you'll reuse)

- **RS line (price ratio):** On TradingView, plot the symbol `NSE:STOCK/NSE:NIFTY` (or divide by the sector index). A rising RS line = outperformance; you want RS making new highs *before or with* price. Mansfield RS, a normalised version, oscillates around zero.
- **Rate of Change (ROC):** `ROC = (Close − Close_n periods ago) / Close_n × 100`. Use 20-period for swing, 125-period (~6 months) for the classic momentum lookback.
- **RS Rating percentile:** Chartink and marketsmithindia publish an IBD-style RS Rating (1–99). Above 80 is the institutional-grade zone; below 40 is avoid-for-longs.
- **Distance from 52-week high:** Momentum leaders sit within ~15% of their 52wk high; laggards languish 30–50% below.
- **ADX(14):** Above 25 confirms a trend worth riding; below 20 warns momentum setups will chop.

Now the five setups.

## Setup 1 — Relative Strength Leader Breakout

**What it is.** Buy a stock that is (a) in an absolute uptrend, (b) outperforming Nifty on the RS line, and (c) breaking out of a tight base to a fresh 20-day or 52-week high. This is the workhorse — the O'Neil "pivot buy" adapted with an explicit RS filter for the Indian market.

**Why it works.** You are combining the two edges: absolute momentum (fresh high) plus relative momentum (RS at new highs). The tight base before breakout means supply has been absorbed; the breakout on volume signals demand overwhelming that supply. Because the stock already leads the tape, market-wide up-days act as a tailwind.

| Element | Rule |
|---|---|
| Universe | F&O or liquid cash stocks, RS Rating ≥ 80, price > 200-DMA and > 50-DMA |
| Trigger | Break above a 4–8 week base high (or 52wk high) with volume ≥ 1.5× 20-day avg; RS line at/near new high |
| Entry | On close above pivot, or intraday break with the pivot holding into close |
| Stop | Below the base / below the breakout-day low, typically 4–7% |
| Target | Measured move (base depth projected up) or trail on 21-EMA; book partial at 2R |
| Timeframe | Daily chart, swing hold 2–8 weeks |
| Regime | Nifty > 50-DMA, market breadth positive; avoid in index downtrends |

**Worked India example (approximate reconstruction — verify on your charts).** Take Dixon Technologies through a strong 2024 stretch. Suppose the stock had run from ~₹6,000 to a high near ₹9,500 and then built a five-week flag between ₹8,900 and ₹9,500 while Nifty chopped sideways — the RS line kept grinding up because Dixon held its gains while the index went nowhere. The pivot is ₹9,500. The setup triggers when price closes at ₹9,560 on volume ~1.8× average. Entry ₹9,560, stop below the flag at ₹8,850 (a ~7.4% risk), first target the measured move: base depth ₹600 projected gives ₹10,100, second target trailing the 21-EMA. If the stock ran to ₹11,200 over the next six weeks, that is roughly 3R+ on the trade with the trailing stop doing the work. The tell that made it worth taking was the RS line printing new highs *during* the base — the stock was being accumulated even while the index rested.

**Confluence (incl. OI).** Check the option chain on breakout day: rising futures OI *with* rising price = fresh longs (bullish confirmation); rising OI with falling price would be a warning of shorts building. A stock breaking out while its ATM/OTM call OI builds and IV stays contained is the cleanest version. Also confirm the *sector* is a leader (see Setup 4) — a leader in a leading sector is the highest-probability variant.

**Pitfalls.** Chasing extended stocks already 20%+ above the 50-DMA; buying a "breakout" on thin volume that fails back into the base (the classic bull trap); ignoring a weak market — even leaders get dragged down when Nifty breaks its 50-DMA. Never widen the stop to "give it room"; a failed RS-leader breakout should be cut fast.

## Setup 2 — Sector Rotation / Top-Down RS

**What it is.** A two-stage top-down process: first rank the sectoral indices by relative strength versus Nifty, then buy the strongest stock inside the strongest sector. This is how you avoid the amateur error of buying a decent stock in a dying sector.

**Why it works.** In India, sector moves are enormous and persistent — PSU banks and defence/railways PSUs in 2023–24, IT in 2020–21, metals in 2021. A rising tide inside a hot sector lifts even mediocre names, and the leader captures the most. RS ranking tells you where institutional flows are concentrating *now*, not where they were last year.

| Element | Rule |
|---|---|
| Step 1 | Rank NSE sector indices (Bank, IT, Auto, Pharma, Metal, FMCG, PSU Bank, Realty, etc.) by 3-month RS vs Nifty; shortlist top 2–3 rising |
| Step 2 | Inside each leading sector, find the stock with highest RS Rating in an uptrend |
| Trigger | Pullback to rising 20/50-EMA that holds, or a fresh breakout, in the leader |
| Stop | Below the pullback swing low (~5–8%) |
| Target | Ride while the *sector* RS line rises; exit when sector loses leadership |
| Timeframe | Daily/weekly; hold weeks to a couple of months |
| Regime | Any — even in a flat Nifty, one sector usually leads |

**Worked India example (approximate).** Suppose in a 2024 window the Nifty PSU Bank index is the top-ranked sector, RS line rising for two months while Nifty is flat. Within it, a name like Canara Bank shows the highest RS and a clean uptrend. Rather than chase, you wait for a pullback into the rising 50-EMA near, say, ₹100, which holds with a bullish reversal candle. Entry ₹102, stop ₹95 (below the swing low, ~7%), and you hold as long as the PSU Bank RS line keeps rising. If the sector led for another two months and Canara ran to ₹125, you exit not on a price target but on the *sector* rolling over — RS line flattening and the index losing its 50-DMA. The discipline is: your thesis is "this sector leads," so your exit is "this sector stops leading."

**Confluence (incl. OI).** Bank Nifty and PSU-heavy names have deep option chains — watch sector-index OI and PCR. A leading sector with a rising index and constructive (not overstretched) PCR supports continuation. Rotation is confirmed when money visibly *leaves* the prior leader (its RS line rolls over) and enters the new one.

**Pitfalls.** Buying the sector after it has already run 40% and everyone is talking about it — RS is high but the easy money is gone; prefer sectors *turning up* in rank, not those parabolic. Also beware single-stock news (a bank-specific NPA shock) overriding the sector tailwind; diversify across two leaders in the sector.

## Setup 3 — Momentum Pullback (Buy the Dip in a Strong Trend)

**What it is.** In a confirmed strong uptrend with high RS, buy the *first or second* shallow pullback to a moving average (20-EMA on daily, or the rising trendline) rather than chasing the breakout. This gives a tighter stop and better R:R than Setup 1.

**Why it works.** Strong trends do not go straight up; they breathe. Buyers who missed the initial move wait to add on dips, so shallow pullbacks in high-RS names get bought quickly. The moving average acts as dynamic support because the whole market watches it. You are buying strength *at a discount* with the trend as your tailwind.

| Element | Rule |
|---|---|
| Universe | RS Rating ≥ 80, ADX(14) > 25, price making higher highs & higher lows |
| Trigger | Pullback of 3–8% to the rising 20-EMA (or 50-EMA for slower trends) that holds; entry on a bullish reversal candle or reclaim of prior day's high |
| Stop | Below the pullback low or below the MA, ~3–5% (tighter than a breakout) |
| Target | Prior swing high first, then trail; add on next base breakout |
| Timeframe | Daily swing, hold days to weeks |
| Regime | Only in stocks whose trend and RS are intact; abandon if RS line breaks down |

**Worked India example (approximate).** Consider Trent through a strong retail-led run. Say the stock is trending from ₹4,000 toward ₹7,000, RS line at new highs, ADX around 30. After a push to ₹6,800 it pulls back over three sessions to the rising 20-EMA near ₹6,350 and prints a hammer that reclaims the prior day's high. Entry ₹6,420, stop ₹6,180 below the pullback low (~3.7%), first target the prior high ₹6,800 (nearly 2R), then trail the 20-EMA. Because the risk was small and the trend strong, a run back to new highs at ₹7,300 yields ~4R. The key filter: the pullback was *shallow and orderly* on declining volume — distribution would show heavy-volume down days, which you avoid.

**Confluence (incl. OI).** On the pullback, futures OI often *drops* (weak-hand longs shaken out) then rises again as price reclaims — a healthy reset. If during the dip put-writers step in at the support strike (put OI building below), that's a floor forming. Avoid dips where call OI is being aggressively unwound — that signals the up-move is over.

**Pitfalls.** The line between a healthy pullback and a trend break is the whole game — a break of the 50-EMA on rising volume, or the RS line making a lower low, means the trend is failing; do not "average down." Also avoid catching the *third or fourth* pullback of an aged trend, where each dip gets deeper — that is the trend maturing.

## Setup 4 — Dual-Momentum Rotation (Systematic)

**What it is.** A rules-based portfolio setup combining absolute and relative momentum. Rank a defined universe (Nifty 50, or a basket of sector ETFs / index proxies) by 6-month return; hold the top N; but only if each also passes an *absolute* filter (positive 6-month return and price > 200-DMA). Otherwise sit in cash/liquid. Rebalance monthly.

**Why it works.** This is Gary Antonacci's dual momentum applied to India. Relative momentum picks the winners; absolute momentum (the "is it up at all?" filter) is the crash guard that pulls you to cash in bear markets, sidestepping the momentum-crash drawdowns. It mechanises Setups 1–2 and removes discretion, which for many traders is the edge that actually survives.

| Element | Rule |
|---|---|
| Universe | Sector indices/ETFs, or top-30 liquid F&O stocks |
| Rank | 6-month (125-day) ROC, high to low |
| Hold | Top 3–5 names, equal weight |
| Absolute filter | Only hold a name if its own 6-month ROC > 0 AND price > 200-DMA; else that slot → cash |
| Rebalance | Monthly (or on last Thursday, aligning with expiry) |
| Stop | Portfolio-level; individual names exit at rebalance if they fall out of rank/filter |
| Regime | Built-in: the absolute filter forces cash in downtrends |

**Worked India example (approximate).** Imagine a month-end ranking of sector proxies where PSU Bank (+38% over 6m), Realty (+31%), and Auto (+22%) top the list, all above their 200-DMAs, while IT (−4%) and FMCG (+1%) lag. The system holds PSU Bank, Realty, Auto, equal weight. Next month, if Realty's 6-month ROC turns negative and it slips below its 200-DMA, that slot rotates to the next qualifying leader — or to cash if fewer than three names pass the absolute filter. During a broad market decline where *no* sector shows positive 6-month momentum, the whole book sits in liquid funds — that is the setup doing its most valuable job, keeping you out. Backtested on Indian sectors, this style captures the big multi-month rotations while capping the worst drawdowns via the cash switch.

**Confluence.** Because this is systematic, the "confluence" is really robustness testing — check that results aren't dependent on one lookback (blend 3m and 6m ranks), and account for realistic costs and slippage on monthly rebalances. Overlay a simple breadth check (percent of Nifty stocks above 200-DMA) as a sanity gauge on the absolute filter.

**Pitfalls.** Whipsaw at market turns — the monthly rebalance can buy just before a reversal (the momentum crash). Mitigate with the absolute filter and by not over-concentrating. Turnover and STT/brokerage eat returns if you rebalance too often; monthly is a reasonable India cadence. And never override the system mid-month on a hunch — that reintroduces the discretion the setup was designed to remove.

## Setup 5 — 52-Week High Momentum Thrust (with RS confirmation)

**What it is.** Buy stocks making *fresh 52-week highs* — but only those where the RS line is *also* at a new high and volume expands. The 52-week high is the purest momentum signal in the public eye; filtering it through relative strength removes the weak, low-quality new highs that fail.

**Why it works.** The 52-week high is a psychological watershed — above it, *no one is holding a loss*, so there is no overhead supply from trapped bulls waiting to break even. George-Hwang-Tetlock research found new-high stocks under-react and continue. Adding RS ensures the new high is backed by genuine outperformance, not just a low-float pop.

| Element | Rule |
|---|---|
| Trigger | Close at a new 52-week high, volume ≥ 1.5× 20-day avg, RS line at new high |
| Confirm | Price > 50-DMA > 200-DMA (proper stack), broad market not in downtrend |
| Entry | On the new-high close, or on first shallow pullback that holds above the breakout level |
| Stop | Below the last consolidation / prior resistance now support, ~5–8% |
| Target | Trail with 21-EMA or a 3-week trailing low (Darvas-style box) |
| Timeframe | Daily/weekly, position-trade for months |
| Regime | Strongest in bull markets; reduce frequency when new-highs list shrinks |

**Worked India example (approximate).** Suppose a defence/PSU name like Bharat Electronics (BEL) clears a long base and closes at an all-time high after a multi-quarter order-book story. Say the base top was ₹190, and BEL closes at ₹196 on volume ~2× average, RS line simultaneously at a fresh high versus Nifty. Entry ₹196, stop below the base at ₹181 (~7.7%). You then trail using a 3-week Darvas box — as new boxes form higher, you raise the stop to just under each box floor. If BEL trended for months toward ₹280 with the RS line leading the whole way, the trailing box exits you only when the trend genuinely breaks, capturing the bulk of a multi-bagger leg. The RS filter is what kept you in BEL rather than a lower-quality new-high name that fizzled.

**Confluence (incl. OI).** New all-time highs have no overhead resistance, so watch OI for confirmation of fresh longs (OI up, price up). In F&O names, an expanding OI base at higher strikes as price makes new highs shows positioning following the move. A new high on *falling* OI (short-covering only) is lower quality — prefer fresh-long-driven highs.

**Pitfalls.** Not every 52-week high continues — the ones that fail usually lacked RS confirmation or made the high on a news gap that immediately faded (buy the gap, get trapped). Avoid new highs in a deteriorating market where the total count of new highs is collapsing (a breadth divergence — see Volume I). And respect that all-time-high investing feels psychologically wrong ("it's too expensive") — that discomfort is precisely why the edge persists.

## Putting the five together

These setups are a family, not five unrelated tricks. Setup 4 is the systematic skeleton; Setups 1, 3, and 5 are discretionary ways to time entries into names that a dual-momentum ranking would already favour; Setup 2 supplies the top-down context so you fish in the right pond. A practical workflow: each weekend, rank sectors (Setup 2) and screen Chartink for RS Rating ≥ 80 stocks at or near 52-week highs (Setup 5) in tight bases (Setup 1); during the week, take entries on shallow pullbacks (Setup 3); and hold the whole thing accountable to the absolute-momentum crash filter (Setup 4's price-above-200-DMA rule and Nifty regime check).

Position sizing ties it together. Because momentum's tail risk is the sharp reversal, risk a fixed fraction — 0.5–1% of capital — per trade, and reduce gross exposure when the Nifty loses its 50-DMA and market breadth deteriorates. Momentum rewards you for being aggressive in trends and humble at turns; the setups give you the entries, but sizing and the regime filter give you the survival.

## Interview-ready summary

- **Momentum** = an instrument rising vs its own past (absolute); **relative strength** = rising vs a benchmark/peers (relative). Best setups stack both: strong *and* strongest.
- Three engines: slow information diffusion, herding/flows, and the disposition effect — all give price memory. Edge is real and survives out-of-sample, including on NSE.
- **Five setups:** (1) RS Leader Breakout from a tight base; (2) Sector-Rotation top-down RS — strongest stock in strongest sector; (3) Momentum Pullback to the rising 20/50-EMA; (4) Dual-Momentum systematic rotation with an absolute-momentum crash filter to cash; (5) 52-week-High Thrust with RS confirmation and Darvas-box trailing.
- **RS toolkit:** price ratio line (STOCK/NIFTY), ROC (20-day swing, 125-day momentum), RS Rating percentile (≥80 institutional), distance from 52wk high, ADX>25 for trend.
- **OI confluence:** rising OI + rising price = fresh longs (confirm); breakouts on falling OI (short-covering) are lower quality; put-writing at support builds floors.
- **The honest risk:** momentum crashes at V-bottoms when laggards suddenly lead. Manage with a hard stop per trade, 0.5–1% risk sizing, an absolute-momentum/regime filter, and reduced exposure when Nifty breaks its 50-DMA. High win-rate in trends, ugly drawdowns at reversals — you survive on exits and sizing, not conviction.
