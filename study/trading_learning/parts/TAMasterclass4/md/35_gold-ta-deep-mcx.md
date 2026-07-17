# Gold TA (Deep, MCX)

Gold is the oldest asset on any Indian trader's screen and the most misunderstood. Retail treats it like a stock — draw a trendline, buy the breakout. But gold does not behave like Reliance or HDFC Bank. It is a global macro instrument wearing a rupee costume on the MCX. To trade gold well on the Multi Commodity Exchange you must hold two charts in your head at once: the international spot price in dollars per troy ounce, and the MCX contract in rupees per 10 grams. The gap between them — the USDINR exchange rate and the import-duty structure — is where most of the confusion and half the opportunity lives.

This chapter is a working playbook: what actually moves MCX gold, the levels and behaviour you must respect, the setups that repeat, a full worked trade, and the risk rules that keep a gold position from eating a month of gains in one US inflation print.

## The instrument's character and its real drivers

MCX Gold is quoted in rupees per 10 grams. The big contract (GOLD) is 1 kg — one rupee move in price is 100 rupees P&L, and a 1 kg lot represents roughly 75-80 lakh rupees of notional at 2026 prices near 75,000-95,000 per 10g. That is a large animal. Most retail traders should live in **GOLDM (GoldMini, 100 grams)** where one rupee of price move is 10 rupees, or **GOLDGUINEA (8 grams)** and the newer **GOLDPETAL (1 gram)** for the smallest accounts. Know your lot before you know your entry — a beginner sizing a full GOLD contract on a 500-point stop is risking 50,000 rupees on one idea, which is account-ending on a 2-3 lakh account.

The price you see on MCX is a **derived** price. The identity that governs it is approximately:

```
MCX Gold (per 10g)  ≈  Spot Gold ($/oz) × USDINR × (10 / 31.1035) × (1 + import duty + premium)
```

There are 31.1035 grams in a troy ounce. So three independent forces move your MCX chart:

1. **International gold in dollars** — driven by US real yields, the Fed, DXY (dollar index), inflation expectations, and safe-haven demand (war, banking stress, election uncertainty).
2. **USDINR** — a weakening rupee lifts MCX gold even when dollar gold is flat. This is why MCX gold can print fresh highs on a quiet global night.
3. **Duty and domestic premium/discount** — import duty changes (a Budget-day risk every February 1st) and festival/wedding-season physical demand.

The single most important relationship to internalise: **gold and US real interest rates are inversely correlated.** Gold pays no yield. When real yields (nominal yield minus inflation) rise, holding gold has a higher opportunity cost, and gold tends to fall. When real yields drop or go negative, gold shines. The DXY dollar index is the second lens — a strong dollar is usually a headwind for dollar gold, though in genuine crisis both can rise together as global cash hides in dollars and metal simultaneously.

## Key levels and behaviour you must respect

Gold trends powerfully and then goes to sleep for weeks. Its personality on the chart:

- **Round numbers matter more than in equities.** On MCX, levels like 70,000, 75,000, 80,000, 90,000, and 1,00,000 per 10g act as magnets and battle zones. Internationally the $2,000, $2,500, $3,000 marks do the same. Physical buyers and jewellers anchor to round rupee figures.
- **Gap behaviour on the daily.** MCX gold gaps at the 9:00 AM open because international gold traded all night while MCX was closed (MCX runs roughly 9:00 AM to 11:30/11:55 PM). The first hour on MCX is a *catch-up* to overnight COMEX and spot moves. Reading the overnight spot chart before the MCX open is not optional — it is the setup.
- **Two sessions of energy.** The Indian morning (catch-up + Asian flows) and the evening 5:00-8:00 PM window when Europe and then the US come online with data releases. US CPI, Non-Farm Payrolls (first Friday), FOMC decisions, and PCE all hit in the MCX evening/night. Gold's biggest daily ranges are made in that window.
- **Trends respect the 20 and 50 EMA on the daily and 4-hour.** In a clean uptrend, pullbacks to the 20 EMA get bought. A close below the 50 EMA on the daily is a genuine character change, not noise.
- **Volatility clusters.** ATR expands around Fed meetings and geopolitics, then contracts. Position size must breathe with ATR — the same rupee-stop is a tiny percentage move in a high-ATR week and a hair-trigger in a quiet one.

For structure, gold responds beautifully to **weekly and daily support/resistance drawn from swing highs/lows**, to **Fibonacci retracements of the last major leg** (the 61.8% of a big rally is a classic re-accumulation zone), and to **horizontal supply/demand shelves** where price previously spent days building a base.

## The best setups on MCX gold

**Setup 1 — Overnight-gap fade or follow (morning).** Before 9:00 AM, check where international spot/COMEX gold settled versus MCX's previous close. If spot rallied 1% overnight, MCX will gap up to catch up. Two plays: if the gap merely aligns MCX to spot (fair gap), you *follow* the trend after the first 15-minute candle confirms direction. If MCX gaps *beyond* what spot justifies (over-reaction, often thin pre-market), you *fade* back toward fair value. The discipline: compute the fair MCX price using the identity above with live USDINR, and compare.

**Setup 2 — Event-driven breakout (evening).** Around US CPI (usually 6:00 PM IST) or FOMC (11:30 PM-12:30 AM IST), gold coils into the release. The professional play is not to guess the number but to trade the *reaction*: let the first violent candle print, wait for the retest of the breakout level, and enter on confirmation with a stop beyond the spike. Never hold a naked position *into* a Fed decision unless you have accepted a wide, gap-sized stop.

**Setup 3 — Trend pullback to 20 EMA (swing).** On the daily, in an established uptrend (price above rising 20 and 50 EMA, higher highs and higher lows), buy pullbacks into the 20 EMA / prior breakout shelf, stop below the recent swing low, target the prior high and then trail. This is the bread-and-butter positional trade and it fits gold's tendency to trend for weeks once macro turns.

**Setup 4 — Range rotation.** When macro is balanced, gold rotates in a multi-week rupee range (say 74,000-77,000). Sell the top edge, buy the bottom edge, with tight stops beyond the range boundary and a rule to flip to breakout mode the moment a daily *closes* outside the range on expanding volume.

## A worked India example

Assume it is a Wednesday in 2026. Setup: US CPI due at 6:00 PM IST. MCX GOLDM (100g) has been consolidating between 76,200 and 77,000 for six sessions. Daily trend is up (price above rising 20/50 EMA), so bias is *long into strength*.

- **Pre-event read.** International spot is at $2,940, USDINR at 87.20. Fair MCX ≈ 2940 × 87.20 × (10/31.1035) × (1 + duty/premium ~0.09) ≈ compute: 2940 × 87.20 = 2,56,368; ÷ 31.1035 = 8,242 per gram-ounce factor; × 10 = 82,420; but that is per 10g before adjusting the ounce/gram — let me keep the trader's shortcut: **watch the spread**, don't recompute to the rupee every tick. MCX is trading 76,600, i.e. tracking spot with the current duty regime; the spread to your reference is stable, so no dislocation edge here. The edge is the *event*, not mispricing.
- **The event.** 6:00 PM: CPI prints *softer* than expected (disinflation). Dollar (DXY) drops, US real yields drop, gold spikes. GOLDM rips from 76,600 through 77,000 (range top) to 77,450 on a huge 5-minute candle.
- **The professional entry.** You do *not* chase the spike. You mark 77,000 (old resistance, now support) as your retest line. Over the next 20 minutes price pulls back to 77,080 and holds above the broken range. You go long GOLDM at 77,120, stop at 76,850 (below the breakout candle's midpoint and back inside the range — a range re-entry would invalidate the breakout). Risk = 270 points × 10 rupees = 2,700 rupees on one GOLDM lot.
- **Management.** Initial target the measured move: range height was ~800 points (76,200-77,000), projected from breakout ≈ 77,800. Price grinds to 77,900 into the US evening. You book half at 77,800 (2R+), trail the rest under the rising 15-minute swing lows. It closes the MCX session at 78,050 near the night high. Second half exits next morning on the first 5-minute lower low at 78,150.
- **Result.** Roughly +680 and +1,030 points on the two halves — call it ~8,500 rupees profit on 2,700 risk, about 3.1R. Clean because you traded the *reaction and retest*, not the guess.

Now the counter-example that teaches the lesson: had CPI printed *hot*, gold would have spiked the other way, blown through 76,200, and a naked pre-event long would have been stopped with a gap-widened slip. That is precisely why the plan was "trade the retest after the candle," not "buy before the number."

## How to use gold for bias and timing across your whole book

Even if you never trade gold, its chart is a macro dashboard. Rising gold with a falling dollar and falling real yields signals a *risk-friendly, easing-expectation* environment that also tends to support equities and hurt the case for holding cash. Gold spiking *with* a rising dollar and falling equities is a *fear* signal — safe-haven bid — and warns you to reduce risk in your Nifty/Bank Nifty longs. Watching gold, USDINR, and Nifty together gives an intermarket read no single chart provides.

For timing, gold's own signals are cleaner than most equities because participation is global and deep, so its trends have fewer fakeouts once confirmed on the daily. Use gold's daily 20/50 EMA relationship as a regime filter: above and rising = trend-follow longs; whipsawing around the EMAs = range tactics only.

## Pitfalls and risk notes specific to gold

- **The USDINR trap.** You can be right on dollar gold and wrong on MCX because the rupee moved against you, or vice versa. If you have a strong *dollar-gold* view, be aware you are also implicitly long or short the rupee move. Serious traders track both.
- **Budget-day duty risk (Feb 1).** A cut or hike in gold import duty can reprice MCX overnight by a full percent or more, independent of world gold. Do not carry a large, tightly-stopped MCX position into the Union Budget without accounting for a policy gap.
- **Overnight gap risk is structural, not occasional.** MCX is closed while the world trades. Every position held overnight carries gap risk from US-session data. Size for the gap, not for the intraday range. A stop that is "safe" intraday can be leapfrogged at the 9:00 AM open.
- **Round-number fakeouts.** Big round levels (80,000, 1,00,000) attract stop-runs. Expect a poke through and reversal; wait for a *close* beyond, not a wick.
- **Thin pre-market and late-night liquidity.** Spreads widen after ~11:00 PM and in the first minutes at 9:00 AM. Market orders in thin books slip badly on a 1 kg lot. Use limits.
- **Contango and rollover.** MCX gold contracts expire (5th of the expiry month cycle). Near expiry, roll to the next series; don't get caught in low-liquidity delivery-logic on the last days.
- **Correlation is not a law.** Gold usually falls when real yields rise — usually. In a full-blown crisis both gold and the dollar rise as everything else is sold. Respect regime, don't marry the textbook correlation.

## Interview-ready summary

MCX Gold is a rupee-denominated derivative of a dollar-denominated global asset. Its price is a product of international spot gold, the USDINR exchange rate, and India's import-duty/premium structure — so three forces, not one, move your chart. Dollar gold is driven primarily by US real interest rates (inverse relationship) and the dollar index, with safe-haven demand as an overlay. On the chart, gold trends hard then rests, respects round rupee numbers and the daily 20/50 EMA, and makes its biggest ranges in the MCX evening/night around US data (CPI, NFP, FOMC). The highest-quality setups are the overnight-gap follow/fade at the morning open, the event breakout-and-retest in the evening, and the trend-pullback-to-20-EMA swing. The defining risks are overnight gap exposure (MCX is closed while the world trades), USDINR moving against a correct dollar-gold view, and Budget-day duty shocks. Trade the reaction and the retest — never the guess before the number — size to the gap rather than the intraday range, and use the smaller GOLDM/GOLDGUINEA contracts until your edge and account can carry the 1 kg animal.
