# KST, TRIX & Coppock Curve

Rate-of-change is the oldest idea in technical momentum: take today's price, compare it to price N bars ago, and you have a number that tells you how fast the market is accelerating or decelerating. The problem with a raw rate-of-change (ROC) line is that it is noisy — it jitters up and down with every wiggle, firing dozens of false crossovers a month. Three of the most respected momentum tools in technical analysis are all, at heart, attempts to *tame* rate-of-change into something smooth enough to trade: the **Coppock Curve** (Edwin Coppock, 1962), **TRIX** (Jack Hutson, early 1980s), and the **Know Sure Thing / KST** (Martin Pring, 1992). They sit on a spectrum from slow-and-strategic (Coppock, built for monthly charts and major bottoms) to medium (KST, a multi-timeframe swing tool) to fast-and-tactical (TRIX, usable intraday).

This chapter treats them as a family because they share a lineage and because an Indian trader can use them as a *timeframe ladder* — Coppock on the Nifty monthly to call generational buy zones, KST on the weekly/daily to time swing entries, TRIX on the daily/intraday for trigger timing. Each is smoothed ROC; the differences are in *how much* smoothing and over *how many* time horizons.

## Coppock Curve: what it is and why it works

Edwin Coppock was an economist, not a chartist, and he built his indicator to answer one narrow question posed to him by an Episcopal church that wanted to know when to invest their endowment: *when is the stock market a long-term buy?* His answer, published in Barron's in 1962, was inspired by an unusual source — he reportedly asked church officials how long it takes people to recover emotionally from bereavement, and was told 11 to 14 months. He reasoned that markets recover from the "bereavement" of a bear market on a similar emotional clock.

The formula reflects that:

**Coppock Curve = 10-period Weighted Moving Average of (14-period ROC + 11-period ROC)**

On its intended **monthly** timeframe: take the 14-month rate-of-change and the 11-month rate-of-change of the index, add them, and smooth the sum with a 10-month weighted moving average. The result is a slow, rolling line that oscillates around zero.

The classic signal is deliberately narrow: **a long-term BUY is generated when the Coppock Curve turns up from below the zero line.** That's it. Coppock explicitly did *not* offer a sell signal — his tool was designed only to identify major bottoms for long-term investors. When the curve is below zero (market has been falling) and it *stops falling and hooks upward*, the emotional recovery from the bear market is deemed to be underway.

Why it works: major market bottoms are momentum events. Price makes its low, but the *rate* of decline slows first — sellers exhaust before buyers dominate. A double-ROC smoothed over ten months captures that deceleration and turns up as the worst of the selling passes, historically flagging generational lows with impressive reliability while ignoring the noise that would shake out a faster indicator.

## Coppock: India example (Nifty monthly)

Reconstruct the Coppock Curve on the **Nifty 50 monthly** around major bottoms. After a deep decline — say the sharp 2020 crash or the 2008 collapse — the Nifty's Coppock Curve would have plunged well below zero as the 11- and 14-month ROCs went deeply negative. The buy signal does not come at the exact price low; it comes a few months *later*, when the curve stops declining and ticks upward from its trough while still below zero.

Concretely: imagine the Nifty bottoms near a monthly low, the Coppock reaches its most negative reading two or three months on, and then hooks up. That upturn — even if the Nifty has already rallied, say, 12–15% off the absolute low — is the signal. The Coppock trader accepts giving up the first leg in exchange for confirmation that the *rate* of the market has genuinely turned. Historically on the Nifty, monthly Coppock upturns from below zero have preceded multi-year bull phases with a strong hit rate. The trade-off is obvious and honest: on a monthly chart these signals appear only every few years, so Coppock is a *strategic asset-allocation* tool for long-term equity SIP top-ups or lump-sum deployment, not a trading indicator.

A practical Indian application: a long-term investor holding a Nifty index fund uses a monthly-Coppock upturn from below zero as a signal to deploy a lump sum or ramp up SIP contributions, and simply ignores the noise in between. Some practitioners also watch for the curve turning *down* from a high level above zero as a soft "reduce risk" hint, though Coppock himself never sanctioned a sell signal.

## TRIX: what it is and why it works

TRIX, developed by Jack Hutson for *Technical Analysis of Stocks & Commodities* in the early 1980s, sits at the opposite end of the family — it is fast enough for intraday use. The name comes from "**tri**ple exponential." The construction:

1. Take the closing price and compute a single EMA (default **15** periods).
2. Take an EMA *of that EMA*.
3. Take an EMA *of that* (triple-smoothed).
4. TRIX = the **1-period rate-of-change (percent) of the triple-smoothed EMA**, usually scaled (×10,000) so it reads in convenient numbers.

The triple exponential smoothing is the clever part. Each EMA pass filters out cycles shorter than the EMA length. By the third pass, virtually all the minor noise, and the dominant lower-timeframe wiggles, are gone — TRIX responds *only* to the meaningful trend of prices. Then taking the rate-of-change of that ultra-smooth line gives you a momentum oscillator that is remarkably clean, crossing zero and forming divergences without the jitter of raw ROC or even MACD.

TRIX oscillates around a **zero line** and is typically paired with a **signal line** (a short EMA of TRIX itself, often 9-period).

### Reading TRIX

- **TRIX crosses above zero** → triple-smoothed trend momentum turned positive → bullish.
- **TRIX crosses below zero** → bearish.
- **TRIX crosses its signal line** → faster trigger, like MACD's signal-line cross.
- **Divergence** — price makes a new high but TRIX makes a lower high → momentum weakening, a common reversal warning. TRIX's smoothness makes its divergences especially trustworthy relative to noisier oscillators.

Default period is 15; shorten to 9 or 12 for faster intraday signals, lengthen to 20–30 for cleaner positional signals.

## TRIX: India example (₹ and levels)

Reconstruct TRIX(15) on **RELIANCE** daily. Suppose Reliance has been ranging around ₹2,850–2,950 and then begins a sustained advance. As the up-move develops, the triple-smoothed EMA line turns up and TRIX **crosses above zero** near ₹2,970 — a clean bullish momentum signal, uncluttered by the whipsaws that a raw ROC would have thrown during the range.

Entry on the zero-line cross (or, for a faster fill, the TRIX/signal-line cross a bar or two earlier) around ₹2,975; stop below the range low near ₹2,840; the position is held while TRIX stays above zero and above its signal line. As Reliance climbs to ₹3,150, watch for the exit tell: if price later grinds to a new high near ₹3,200 but TRIX prints a *lower* high (bearish divergence), momentum is fading beneath a rising price — tighten the stop or book. The actual sell trigger is TRIX crossing back below its signal line, then below zero.

For **intraday** use, TRIX(9) on a 15-minute Bank Nifty chart gives tradeable zero-line and signal-line crossovers; because it is so smooth, it lags a little, so it suits *trending* days and hurts on choppy ones — the same regime caveat that governs the whole momentum family.

## KST (Know Sure Thing): what it is and why it works

Martin Pring's KST, introduced in 1992, is the most sophisticated of the three. Pring's insight was that markets move in *multiple cycles simultaneously* — short, intermediate and long cycles all overlap — and that a good momentum indicator should blend all of them into one line. A single ROC captures only one cycle length; KST captures four and weights them.

Construction (the standard daily/weekly version):

1. Compute **four** different-length ROCs — commonly ROC(10), ROC(15), ROC(20) and ROC(30).
2. **Smooth each** ROC with its own moving average — commonly SMA(10), SMA(10), SMA(10) and SMA(15) respectively.
3. **Weight** them — the slower ROCs get *heavier* weights (typically 1, 2, 3, 4) so the longer cycle dominates while the faster ones add sensitivity.
4. **Sum** the four weighted, smoothed ROCs → that sum is the KST line.
5. A **signal line** (usually a 9-period SMA of KST) is plotted alongside.

The result is a smoothed momentum oscillator around zero that reflects short, intermediate *and* long cycles at once — hence Pring's semi-joking name, "Know Sure Thing." It behaves like a more robust MACD: fewer whipsaws because four cycles must broadly agree, yet responsive because the fast ROCs are in the mix.

### Reading KST

- **KST crosses above its signal line** → bullish trigger; **below** → bearish.
- **KST crosses the zero line** → confirmation of a momentum regime change.
- **Divergence** with price → early reversal warning.
- **Direction and level** — rising KST above zero is a strong uptrend; falling KST below zero a strong downtrend.

KST is genuinely **multi-timeframe**: Pring defined short-term, intermediate and long-term versions using different ROC/smoothing sets, so you can run a "long-term KST" on weekly data for the primary trend and a "short-term KST" on daily for entries — the same top-down discipline serious swing traders already apply, baked into one indicator family.

## KST: India example (₹ and levels)

Reconstruct KST on **INFY** daily. Suppose Infy has bottomed after a decline and is basing near ₹1,420. The four ROCs turn up at slightly different times; as they align, KST rises and **crosses above its signal line** below the zero line near ₹1,440 — an early bullish trigger. Confirmation follows when KST subsequently crosses *above zero* near ₹1,475, signalling the intermediate cycle has joined the short cycle.

The swing trade: enter on the KST/signal cross with confirmation from price structure at ₹1,445; stop below the base low near ₹1,405; hold while KST rises and stays above its signal line. Target the prior resistance shelf near ₹1,560. If Infy pushes to ₹1,580 later while KST rolls over and crosses *below* its signal line, that is the exit — the multi-cycle momentum has turned even though price is still near its high.

The advantage over a single oscillator: because KST needs several cycles to agree, it kept you out of the false rallies during the ₹1,420 base and only committed when the cycles aligned — far fewer whipsaws than a raw ROC or even a fast MACD would have given on the same chart.

## Setups and how to trade the family

| Setup | Indicator | Trigger | Stop | Target | Timeframe | Regime |
|---|---|---|---|---|---|---|
| Generational buy | Coppock | Curve turns up from below zero | N/A (investment) | Multi-year hold | Monthly | Post-bear-market bottom |
| TRIX zero-cross long | TRIX(15) | TRIX crosses above zero | Below range/swing low | Prior resistance | Daily | Trending |
| TRIX signal trigger | TRIX(9) | TRIX crosses above its signal line | Below trigger bar | Intraday resistance/VWAP | 15-min | Trending day |
| KST swing long | KST | KST crosses above signal below zero, then confirms above zero | Below base low | Prior resistance shelf | Daily/weekly | Basing → uptrend |
| Momentum divergence exit | Any of the three | Price new high, indicator lower high | — | Book / tighten | Any | Maturing trend |

**Workflow as a ladder:** Coppock (monthly) tells you the *strategic* backdrop is a bull market → you look only for longs. KST (weekly/daily) times the *swing* — enter when it crosses its signal in the trend direction. TRIX (daily/intraday) fine-tunes the *trigger bar*. Each lower rung confirms rather than contradicts the one above.

## Confluence — including option-chain

- **Coppock + market breadth:** A monthly Coppock upturn confirmed by improving advance-decline and % of Nifty 500 stocks above their 200-DMA is a powerful all-clear for equity deployment.
- **KST/TRIX + moving averages:** A KST or TRIX bullish cross above a rising 50-DMA, with price above the 200-DMA, stacks trend and momentum.
- **Divergence + support/resistance:** A TRIX or KST bearish divergence *at* a known resistance level is far more actionable than divergence in open space.
- **Option-chain (index/F&O):** For a KST or TRIX bullish swing signal on Nifty or Bank Nifty, check the chain — if put writers are adding OI at support (building a floor) and PCR is turning up as momentum turns, positioning agrees with the technicals; if a heavy call-OI wall sits just overhead, expect the momentum signal to stall there and plan the target accordingly. A TRIX zero-cross that coincides with call-writer unwinding at resistance is a higher-conviction directional-option trade.
- **Volume:** Momentum crossovers on rising volume are more trustworthy than those on declining volume.

## Pitfalls

1. **Coppock is a bottom-caller, not a trading tool.** It fires rarely (every few years on monthly Nifty), gives no official sell signal, and using it on daily charts destroys its logic. Do not day-trade Coppock.
2. **All three lag — that is the price of smoothness.** TRIX's triple smoothing and KST's multi-ROC blend and Coppock's 10-month WMA all delay the signal. You will never buy the exact low or sell the exact high; these tools trade *confirmed* momentum, not turns.
3. **Whipsaws still happen in ranges.** Smoother than raw ROC, yes — immune, no. In prolonged sideways markets, even KST and TRIX flip around zero. Combine with a trend filter (ADX, moving-average slope) and stand aside when the market is directionless.
4. **Divergences can persist.** A TRIX or KST bearish divergence can run for weeks while price grinds higher. Divergence is a *warning*, not a timing trigger — wait for the actual cross.
5. **Parameter fiddling / overfitting.** It is tempting to optimise the ROC lengths and weights to a specific stock's history. That curve-fits to the past. Prefer the standard settings (Coppock 14/11/10; TRIX 15; KST 10/15/20/30 with 1-2-3-4 weights) unless you have a robust, walk-forward reason to change them.
6. **Coppock's upturn can occasionally fail** in a secondary decline (a "double dip"). No single indicator is infallible; confirm with breadth and price structure.

## Interview-ready summary

All three are *smoothed rate-of-change* momentum tools on a slow-to-fast spectrum. **Coppock Curve** (1962) = 10-month WMA of (14-month ROC + 11-month ROC), designed for *monthly* charts; its only signal is an upturn from below zero, historically a reliable caller of major long-term bottoms — a strategic deployment tool, not a trading indicator, with no sell signal. **TRIX** (early 1980s) = the 1-period ROC of a *triple-smoothed* EMA (default 15); its triple smoothing strips noise so its zero-line crosses, signal-line crosses and divergences are unusually clean, and it is fast enough for intraday use. **KST / Know Sure Thing** (Pring, 1992) = a weighted sum of *four* smoothed ROCs (10/15/20/30, weights 1-2-3-4) that blends short, intermediate and long cycles into one line with a signal line — a more robust, multi-timeframe MACD. Use them as a timeframe ladder: Coppock (monthly) for the strategic backdrop, KST (weekly/daily) for swing timing, TRIX (daily/intraday) for the trigger. Every one lags in exchange for smoothness, whipsaws in ranges, and works best filtered by trend and, for index trades, confirmed by breadth and agreeing option-chain OI/PCR.
