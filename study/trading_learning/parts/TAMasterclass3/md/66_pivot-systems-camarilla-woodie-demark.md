# Pivot Systems: Camarilla, Woodie & DeMark

Most Indian intraday traders know one flavour of pivots — the "classic" floor-trader pivot (PP, R1–R3, S1–S3) that TradingView plots by default and that half of Chartink scanners quietly reference. Volume I covered that. This chapter is about the three *specialised* pivot systems that professional intraday and swing desks actually argue about: **Camarilla** (a mean-reversion-vs-breakout machine built around the H3/H4 and L3/L4 lines), **Woodie's** pivots (a directional, CPR-cousin system that weights the current-session open), and **DeMark pivots** (the asymmetric, close-relative-to-open formula that Tom DeMark designed so the pivot *leans* in the direction of yesterday's momentum). Each computes a different set of numbers from the same OHLC, and — this is the part beginners miss — each is a different *philosophy* of what a level means. Camarilla says "price returns to value"; DeMark says "the pivot should predict the range, not sit in the middle of it"; Woodie says "the open tells you the day's bias before the first candle prints."

We will build each from its formula, plot a real Nifty and Bank Nifty example in rupees, give you exact entry/stop/target rules, and be honest about where these lines are genuinely edges versus where they are astrology with decimals.

## What pivot systems are and the logic

A pivot system is a set of **pre-computed horizontal levels for the coming session**, derived only from the *prior* period's High, Low, and Close (and sometimes Open). Because they use closed data, every level is fixed before the session starts — no repainting, no lag, no lookback ambiguity. That single property is why algorithmic desks love them: a pivot level is a hard number you can put in a limit order at 9:14 and forget. Classic pivots, Camarilla, Woodie, and DeMark all share this DNA; they differ only in the arithmetic and therefore in *what they claim the levels mean.*

The deeper logic: markets spend most of their time inside a value area and only occasionally trend out of it. Pivot levels are attempts to pre-mark (a) the **equilibrium** where price is "fairly valued" (the central pivot) and (b) the **edges** where the prior range's supply/demand should reappear. Whether you fade those edges (mean-reversion) or trade the break of them (momentum) depends on the system and the regime. Camarilla is explicitly dual-mode — it has inner lines to fade and outer lines to trade breakouts. DeMark is a single forward-looking projection. Woodie is directional and pairs with Camarilla on many trader screens.

For Indian markets, one practical note dominates everything: **which "prior period" do you use?** For index intraday (Nifty, Bank Nifty, Fin Nifty), you use the *prior day's regular-session* OHLC (09:15–15:30). You do **not** blend the pre-open or the NSE post-close session. For MCX Crude or Gold, the day session and evening session create a genuine choice — most MCX pivot traders use the full 09:00–23:30/23:55 range as one "day." For USDINR futures, use the 09:00–17:00 currency-segment day. Get the source range wrong and every level is wrong.

## Camarilla: construction, rules and settings

Camarilla pivots were popularised by Nick Scott in the late 1980s. The system generates **eight** levels — H1–H4 above and L1–L4 below a central reference — using multipliers of the prior range (R = High − Low). The famous constant is **1.1**, applied at descending powers.

| Level | Formula | Role |
|-------|---------|------|
| H4 | Close + R × 1.1/2 | Breakout trigger (long) |
| H3 | Close + R × 1.1/4 | **Short / fade the top** |
| H2 | Close + R × 1.1/6 | Minor resistance |
| H1 | Close + R × 1.1/12 | Minor resistance |
| L1 | Close − R × 1.1/12 | Minor support |
| L2 | Close − R × 1.1/6 | Minor support |
| L3 | Close − R × 1.1/4 | **Long / fade the bottom** |
| L4 | Close − R × 1.1/2 | Breakout trigger (short) |

Note two things. First, Camarilla is **Close-centred, not (H+L+C)/3-centred** — the whole ladder pivots around yesterday's close, which is why it hugs the settlement price where positions actually sit. Second, the *pairs matter*: H3/L3 form the inner "range" you fade, and H4/L4 form the outer "breakout" band. The distance from H3 to H4 (and L3 to L4) is R × 1.1 × (1/2 − 1/4) = R × 0.275 — a fixed, known width you can put a stop inside.

The core Camarilla playbook has two regimes:

- **Range day (fade):** If price opens *between L3 and H3*, you expect mean reversion. Sell near H3 targeting the pivot/L-levels; buy near L3 targeting the pivot/H-levels. Stop just beyond H4/L4.
- **Trend day (breakout):** If price *breaks and holds* above H4 (or below L4), the range-fade thesis is dead and you flip to momentum — go long on the H4 break, targeting H5 (an extension = H4 + (H4−H3)) or a measured move.

A refinement many use is the **open-relative rule**: if today opens *above H3* already, the sequence is considered "gap-strong" and you favour longs on any pullback to H3 rather than shorting it.

## Camarilla worked example — Bank Nifty

Suppose Bank Nifty's prior regular session closed as: **High 52,180, Low 51,540, Close 51,720.**

Range R = 52,180 − 51,540 = **640**.

- H4 = 51,720 + 640 × 0.55 = 51,720 + 352 = **52,072**
- H3 = 51,720 + 640 × 0.275 = 51,720 + 176 = **51,896**
- H2 ≈ 51,720 + 117.3 = **51,837**
- H1 ≈ 51,720 + 58.7 = **51,779**
- L1 ≈ **51,661**
- L2 ≈ **51,603**
- L3 = 51,720 − 176 = **51,544**
- L4 = 51,720 − 352 = **51,368**

Now the session opens at **51,760** — inside L3–H3, so the base case is a **range/fade day**. Price rallies in the first hour to **51,890**, kissing H3 (51,896). This is the textbook Camarilla short: you sell 51,890–51,900, place the stop at **52,085** (just above H4, ~₹190 risk per share-equivalent), and target the central zone / L1 around **51,660** (reward ~₹230). If instead price had *ripped through 52,072 (H4) and held two 5-minute closes above it*, you abandon the short thesis entirely and buy the H4 breakout, stop back under H4, target H5 = 52,072 + (52,072−51,896) = **52,248**.

On one lot of Bank Nifty futures (lot size 15 in 2026), the fade trade's ~176-point move to target is 176 × 15 = **₹2,640** gross per lot, against ~195-point risk = ₹2,925 — a roughly 0.9:1 raw payoff that only works because the *hit rate* on H3 fades in a range regime is high (often 60–65% in genuinely rangebound sessions). That asymmetry is the whole game: Camarilla fades win often and small; the discipline is refusing to fade on trend days.

## Woodie's pivots: construction and rules

Woodie's pivots (from Ken Wood's trading community) look like classic pivots but change **one input**: the central pivot weights the **current session's open** by doubling it and — crucially — Woodie computes the pivot from the *prior* High/Low but the *current* Open, so the level updates the moment today opens.

| Level | Formula |
|-------|---------|
| PP (Woodie) | (High + Low + 2 × Open) / 4 |
| R1 | 2 × PP − Low |
| R2 | PP + (High − Low) |
| S1 | 2 × PP − High |
| S2 | PP − (High − Low) |

Here "Open" = today's open, "High/Low" = *yesterday's* high and low. Because today's open is double-weighted, a gap-up drags the whole Woodie ladder up relative to a classic pivot, encoding the gap's bias directly into the levels. This is why Woodie traders describe the system as **directional**: the pivot tells you the day's lean before you've seen a single bar of today's action.

Woodie's community also layers proprietary tools (the "CCI" trend/zero-line rules, the "Tugboat" and "GB100" setups), but the pivot levels themselves are used simply: price above Woodie PP = bullish bias, trade R1→R2 as upside targets and S1 as support; price below PP = bearish bias, mirror it. The R2/S2 (= PP ± prior range) act as full-range extension targets.

## Woodie worked example — Nifty 50

Prior Nifty session: **High 24,410, Low 24,150, Close 24,300.** Today **opens at 24,380** (a gap up).

Woodie PP = (24,410 + 24,150 + 2 × 24,380) / 4 = (24,410 + 24,150 + 48,760) / 4 = 97,320 / 4 = **24,330**.

Compare: the *classic* pivot = (24,410 + 24,150 + 24,300)/3 = **24,286.7**. The gap-up open has pulled Woodie's PP ~43 points higher — it "believes" the gap.

- R1 = 2 × 24,330 − 24,150 = **24,510**
- R2 = 24,330 + (24,410 − 24,150) = 24,330 + 260 = **24,590**
- S1 = 2 × 24,330 − 24,410 = **24,250**
- S2 = 24,330 − 260 = **24,070**

Trade logic: price opened at 24,380, comfortably **above PP 24,330 → bullish bias.** You wait for a pullback toward PP. If Nifty dips to **24,335–24,340** and holds (a higher low on the 5-min), you go long, stop below S1 at **24,240** (~95-point risk), first target R1 **24,510** (~170 points), runner to R2 **24,590**. On Nifty futures (lot 75 in 2026) the R1 target ≈ 170 × 75 = **₹12,750** gross per lot against ~₹7,125 risk — a clean ~1.8:1 that the Woodie bias framing set up *before the open.* If price instead loses PP and closes a 5-min bar below 24,320, the bullish thesis is void and you stand aside (or flip short toward S1).

## DeMark pivots: the asymmetric formula

Tom DeMark's pivot is the cleverest of the three because it is **conditional on the relationship between the prior Close and prior Open.** The idea: a market that closed *above* where it opened has upward momentum and its true pivot should sit *higher*; one that closed below should pivot lower. So DeMark computes a value **X** three different ways:

| Condition | X |
|-----------|---|
| Close < Open | X = High + 2 × Low + Close |
| Close > Open | X = 2 × High + Low + Close |
| Close = Open | X = High + Low + 2 × Close |

Then:
- **Pivot (DeMark) = X / 4**
- **Resistance = X / 2 − Low**
- **Support = X / 2 − High**

DeMark deliberately produces **only one resistance and one support**, not a ladder. The philosophy is anti-clutter: the system gives you a single projected high-and-low band for tomorrow, and the *asymmetry* means the band is skewed in the direction yesterday's body pointed. On a strong up-close day, resistance sits further away (room to run) and support sits closer (shallow pullbacks) — encoding momentum into geometry.

## DeMark worked example — Reliance / Nifty stock

Take a liquid NSE stock, **Reliance**, prior day: **Open 2,910, High 2,958, Low 2,896, Close 2,948.** Close (2,948) > Open (2,910), so momentum is up → use the second row.

X = 2 × High + Low + Close = 2 × 2,958 + 2,896 + 2,948 = 5,916 + 2,896 + 2,948 = **11,760**.

- Pivot = 11,760 / 4 = **2,940**
- Resistance = 11,760 / 2 − Low = 5,880 − 2,896 = **2,984**
- Support = 11,760 / 2 − High = 5,880 − 2,958 = **2,922**

Read it: the projected band is **2,922 support ↔ 2,984 resistance, pivoting at 2,940.** Because it was an up-close, resistance (2,984, +36 from close) sits further than support (2,922, −26). The trade: if Reliance opens near 2,945 and holds above the 2,940 pivot, you're long-biased; buy dips to **2,924–2,926** near DeMark support (which often coincides with the prior low 2,896–2,922 demand zone), stop under **2,912** (below Open, ~₹14 risk), target the **2,984** DeMark resistance (~₹58–₹60 reward). At Reliance's F&O lot of 500, that's roughly ₹29,000 gross target vs ₹7,000 risk — a ~4:1 that DeMark's asymmetric geometry handed you *because* it read yesterday's up-close correctly. The honest caveat: had the close been *below* open, the whole band flips skew and you would have run the mirror trade.

## How to trade all three — entry, stop, target, management

Across the three systems, the disciplined workflow is identical even though the numbers differ:

**1. Classify the day first.** Where did price open relative to the key line? Camarilla: inside L3–H3 (fade) or outside H4/L4 (breakout)? Woodie: above or below PP (directional bias)? DeMark: above or below the single pivot? *No level triggers a trade until the regime is set.*

**2. Enter at the level, not into space.** Pivot levels work as *limit* zones, not chase signals. Place resting orders (or wait for a rejection candle) at H3/L3, at Woodie PP, at DeMark support/resistance. Entering mid-range guarantees a bad stop.

**3. Stop is defined by the next structural level.** Camarilla fade stops go just beyond H4/L4 — never a random number of points. Woodie longs stop below S1; DeMark longs stop below the pivot (or below prior Open). The system *gives* you the stop; use it.

**4. Targets are the opposing/next levels.** Camarilla fade → central zone → opposite inner line. Woodie → R1 then R2. DeMark → the single opposite line. Trail a runner only after the first target pays for the risk.

**5. Time-of-day management (India-specific).** The first 45 minutes (09:15–10:00) on Nifty/Bank Nifty is where pivot fades fail most — volatility and news gaps overwhelm the levels. Many pivot traders take fade signals only *after* 10:00 and take breakout signals *only if the break holds past 09:45*. The 15:00–15:30 close hour is for exiting, not initiating, fades.

## Confluence: making pivots reliable

A pivot level in isolation is a coin-flip nudged slightly by regime. The edge sharpens dramatically at **confluence**:

- **Pivot + prior-day level.** A Camarilla L3 that sits ₹5 from yesterday's low, or a DeMark support that overlaps the prior close, is a far stronger fade than a lonely line.
- **Pivot + CPR.** Woodie pivots pair naturally with the **Central Pivot Range** (already in Volume II): a narrow CPR + price rejecting Woodie R1 is a high-conviction short.
- **Pivot + round number.** Bank Nifty 52,000, Nifty 24,500, USDINR 84.00 — a Camarilla H4 that lands on a round strike (where option OI clusters) magnifies the reaction.
- **Pivot + option OI wall.** On Nifty/Bank Nifty, overlay the max-OI call/put strikes. When Camarilla H3 ≈ the highest-OI call strike, market-makers' gamma hedging reinforces the fade — this is the single best confluence available in Indian index intraday.
- **Pivot + VWAP.** Price reclaiming Woodie PP *and* VWAP together is a much cleaner long than either alone.

The rule of thumb: **two confluent factors roughly double your comfort; three make it a core trade.** One factor alone is a scalp at best.

## Pitfalls

- **Wrong source range.** Using the wrong prior session (including pre-open, mixing MCX day+evening incorrectly, or using calendar-day OHLC for a stock that had a special session) corrupts every level silently. Verify your charting source's pivot session setting.
- **Fading a trend day.** The number-one Camarilla account-killer: mechanically shorting H3 on a day that has already broken H4. If H4/L4 breaks and holds, the fade regime is *dead* — flip or stand aside. Do not average into a runaway.
- **Treating DeMark like a ladder.** DeMark gives one support and one resistance by design. Traders who "add levels" to it are inventing numbers with no basis.
- **Ignoring gaps in Woodie.** Woodie's whole value is that it weights the open — but a huge gap (results, budget day, global shock) can place PP in dead air where price never trades. On >1% gaps, pivots are unreliable until the first hour builds real structure.
- **Over-tight stops inside the range.** The H3–H4 band is ~0.275R wide for a reason; stopping at 0.1R gets you shaken out by noise before the fade works. Respect the system's own geometry.
- **Backtest without costs.** These are intraday, high-frequency-of-signals systems. At NSE F&O costs (STT on sell side, exchange + SEBI charges, GST on brokerage, ~₹20 flat brokerage on discount brokers), a strategy that looks like +8 points/trade in a backtest can be break-even net. Always model round-trip costs of roughly ₹40–₹120 per lot depending on segment.
- **Curve-fitting the multiplier.** Some traders "optimise" Camarilla's 1.1 constant. Don't — the levels' value is that they are *standard and widely watched*; changing the constant removes the self-fulfilling crowd effect that makes them work.

## Interview-ready summary

Pivot systems pre-compute fixed horizontal levels from prior-period OHLC, so they never repaint. The three advanced systems differ in philosophy: **Camarilla** centres on the prior *close* and gives an eight-line ladder whose H3/L3 inner band you *fade* and whose H4/L4 outer band you trade as *breakouts* — a dual-mode range-vs-trend machine (key constant 1.1, inner band at 1.1/4, outer at 1.1/2). **Woodie's** pivot double-weights *today's open* — (H+L+2×Open)/4 — making it *directional*: above PP is bullish bias, R1/R2 are upside targets, and a gap drags the whole ladder in the gap's direction. **DeMark** is *asymmetric and conditional*: the formula branches on whether the prior Close was above or below the Open, projecting a single skewed support-resistance band that leans in yesterday's direction. Trade all three the same disciplined way — classify the regime from the open, enter *at* the level with a resting/rejection order, take the stop the system defines (beyond H4/L4, below S1, below the pivot), target the opposing level, and only size up at confluence with prior-day levels, CPR, VWAP, round numbers, or option OI walls. The honest limits: pivots are edges *only* when regime-matched (fading a trend day is the classic blow-up), gaps break Woodie, DeMark must stay a single band, and at real NSE F&O costs the thin per-trade edge demands high discipline and a correct prior-session source range to survive.
