# Advanced RSI: The Cardwell Method

Wilder gave the world RSI in 1978 with a simple message: above 70 is overbought, below 30 is oversold, and divergences warn of reversals. For a ranging market that is fine. But anyone who has shorted a trending Nifty because "RSI is overbought at 78" knows Wilder's rules can bankrupt you in a bull run. Andrew Cardwell — the man who arguably understood RSI more deeply than anyone after Wilder — flipped the interpretation on its head. His central discovery: **RSI behaves completely differently in bull markets versus bear markets, and its ranges themselves define the trend.** This chapter teaches the Cardwell method in full: RSI range rules, reversals (his replacement for divergence), positive/negative reversals, and how to trade all of it on NSE. If you learn one "advanced RSI" framework, learn this one — it is the genuine article, not repackaged basics.

## What it is and the deeper logic

RSI = 100 − 100/(1 + RS), where RS = average gain / average loss over N periods (Wilder used 14). It is a bounded 0–100 momentum oscillator. Wilder's original interpretation:
- \>70 overbought (sell), <30 oversold (buy).
- Divergence between price and RSI warns of reversal.
- Failure swings and centreline (50) crosses as confirmation.

Cardwell's insight, developed over decades of teaching, is that Wilder's overbought/oversold thresholds are *not fixed truths* — they are **symptoms of trend**. In a strong uptrend RSI reaching 70+ is not a sell signal; it is *confirmation of strength*. The correct question is not "is RSI overbought?" but "**which range is RSI trading in?**" Because RSI's operating range shifts with the trend, the range itself is a trend indicator.

## Pillar 1: RSI range rules (the foundation of Cardwell)

Cardwell observed that RSI confines itself to different bands depending on the market regime:

| Regime | RSI typically ranges | Interpretation |
|---|---|---|
| **Bull market** | 40–80 (support 40–50, resistance 80) | Pullbacks bottom at 40–50; RSI rarely breaks below 40 |
| **Bear market** | 20–60 (resistance 50–60, support 20) | Rallies top at 50–60; RSI rarely exceeds 60 |

The practical power: **the 40–50 zone is support in a bull market, and the 50–60 zone is resistance in a bear market.** So:

- If RSI keeps holding **above 40** on pullbacks, the trend is bullish — buy the dips into 40–50.
- If RSI keeps failing at **60** on rallies, the trend is bearish — sell the rips into 50–60.
- A **shift of the range** signals a trend change: when RSI in an uptrend finally breaks decisively below 40 and starts topping around 60 instead of 80, the market has flipped to a bear range. This is often earlier and cleaner than a price-based trend signal.

**Nifty example:** Through a sustained 2024-style uptrend, Nifty daily RSI repeatedly dipped to 43–47 and turned back up, never breaching 40, while peaking near 78–82. That is a textbook bull range. A Wilder trader shorting every "overbought 75+" reading was run over for months. A Cardwell trader instead *bought* every dip to the 40–50 RSI support. When RSI finally cracked below 40 and a subsequent rally stalled at 58, that range shift flagged the regime change to distribution — time to stand aside or flip bias.

## Pillar 2: Cardwell reversals — the real replacement for divergence

Here is Cardwell's most valuable and least-known contribution. He found that **positive and negative reversals** — not classic divergences — are the high-probability, trend-continuation signals. They are essentially *hidden divergence read through an RSI lens*, and they point in the direction of the trend, which is why they work when classic divergence fails.

**Positive reversal (bullish, appears in uptrends):**
- RSI makes a **lower low**, but price makes a **higher low**.
- Meaning: momentum dipped more than price — buyers defended a higher price on weaker-looking momentum. Strength. Continuation *up*.
- This is the opposite of what a Wilder trader expects; they would see "price higher low, RSI lower low" and call it bearish divergence. Cardwell says: in an uptrend, that is *bullish*.

**Negative reversal (bearish, appears in downtrends):**
- RSI makes a **higher high**, but price makes a **lower high**.
- Meaning: momentum popped more than price could — sellers capped price despite a momentum spike. Weakness. Continuation *down*.

| Signal | Price | RSI | Trend context | Implication |
|---|---|---|---|---|
| Positive reversal | Higher low | Lower low | Uptrend | Continuation UP |
| Negative reversal | Lower high | Higher high | Downtrend | Continuation DOWN |
| (Classic) bearish divergence | Higher high | Lower high | Often a trend — frequently *fails* | Weak reversal signal |
| (Classic) bullish divergence | Lower low | Higher low | Often a trend — frequently *fails* | Weak reversal signal |

Cardwell's teaching: in a healthy trend, **reversals dominate and classic divergences fail.** Classic divergences work mainly at genuine trend *ends* and in ranges. So the discipline is: identify the trend first (via range rules), then look for *reversals* in the trend direction — not divergences against it.

## Pillar 3: Price targets from reversals

Cardwell reversals are not just directional — they give **measured price targets.** From a positive reversal, measure the price distance from the RSI's higher-low pivot to the prior swing high, and project it upward from the reversal point. It is a momentum-based measured move: the "compression" between the two RSI/price lows resolves into an equivalent extension.

**Worked Bank Nifty example:** In an uptrend, price forms a higher low at 51,000 (RSI dips to a *lower* low of 44) versus a prior swing that ran from a 50,600 low to a 52,400 high. That is a positive reversal. Projected target ≈ reversal-low + prior swing range = 51,000 + (52,400 − 50,600) = 51,000 + 1,800 = **52,800**. Enter on confirmation above the pivot (say 51,300), stop below the higher low (50,900, ~400 pts), target 52,800. The RSI told you both *that* the trend would continue and *how far*.

## Pillar 4: The 40/50/60 centreline framework and momentum confirmation

Cardwell refined the centreline into a three-line map:
- **50** — momentum midline; bull markets hold above it on average, bears below.
- **40** — bull-market support / bear-market's upper boundary of oversold.
- **60** — bear-market resistance / bull-market's lower boundary of overbought territory.

A clean way to read regime at a glance: *Where does RSI find support and where does it find resistance?* Support at 40, resistance at 80 → bull. Support at 20, resistance at 60 → bear. Support at 45–50 with resistance at 65 → transitioning/uncertain, reduce size.

## India-adapted settings and application

- **Timeframe/length:** Wilder's 14 is fine on Nifty/Bank Nifty daily and weekly. For intraday Bank Nifty (5–15 min) some traders drop to RSI(9) for responsiveness — accept more noise.
- **Index vs stocks:** Range rules are cleanest on liquid, trending instruments — Nifty, Bank Nifty, large-cap F&O names. On choppy mid/small-caps, ranges are messier; demand more confirmation.
- **Chartink/TradingView:** you can scan for "RSI holding above 40 on pullback" or code positive/negative reversal conditions. A practical NSE scan: F&O stocks in an uptrend (price > 50-EMA) whose RSI just bounced from the 40–50 zone — a basket of Cardwell dip-buys.

## How to trade it — entry, stop, target, management

**Bull-market dip-buy (range + positive reversal):**
- *Context:* price above 50-EMA, RSI making higher lows above 40, resistance near 80.
- *Entry:* RSI pulls to 40–50 and turns up, ideally forming a positive reversal (RSI lower low vs price higher low) with a bullish candle. Enter on the turn.
- *Stop:* below the price higher-low pivot (structure-based), or where RSI would break below 40 decisively.
- *Target:* reversal measured move, and/or prior swing high; trail as RSI keeps holding 40+.
- *Management:* stay long while the bull range persists; exit or flip when RSI breaks the range (sustained close below 40 and rallies capping at 60).

**Bear-market rip-sell (mirror):** price below 50-EMA, RSI capping at 50–60; sell rallies into that zone on a negative reversal; stop above the price lower-high pivot; target the measured move down.

**F&O translation:** a bull range with a positive reversal favours **bull call spreads / short put spreads** with the short strike near the RSI-40 price support. A bear range with negative reversals favours **bear put spreads / short call spreads** capped at the RSI-60 resistance price. RSI range rules give you a *regime* read that tells you whether to be a net buyer of directional spreads (strong trend) or to fade extremes (range) — and where to place strikes.

## Confluence

- **Moving averages / ADX:** confirm the regime that validates which RSI range to expect. RSI range rules + rising ADX = high-conviction trend continuation.
- **Support/resistance & round numbers:** a positive reversal that bottoms exactly at a Nifty support/round number is premium.
- **Volume/OI:** a Cardwell dip-buy with fresh long build-up in futures OI is far stronger.
- **Ichimoku/MACD:** RSI range for regime, MACD histogram for timing, Ichimoku Kijun for the trailing stop — a complementary stack, each answering a different question.

## Pitfalls (honest)

- **Applying Wilder's fixed 70/30 in a trend** — the classic wealth-destroyer; shorting "overbought" Nifty in a bull run. Cardwell's whole point is that 70/30 are *not* trade signals in trends.
- **Trading classic divergence in strong trends** — it fails repeatedly; the market makes higher highs on weaker RSI for a long time before topping. Use reversals in the trend direction instead.
- **Mis-identifying the regime** — every Cardwell rule depends on first knowing bull vs bear range. Get the regime wrong and you will buy dips in a bear market. Always establish the range/trend first (higher-timeframe, 50-EMA, ADX).
- **Reversals without a trigger** — like divergence, a reversal is a *condition*; require a candle/structure trigger before entering.
- **Illiquid stocks** — range rules blur on choppy, gappy small-caps; stick to liquid instruments.
- **RSI(9) intraday noise** — shorter lengths whipsaw; confirm with structure.
- **Range-shift lag** — a genuine regime change (bull range → bear range) is only *confirmed* after the fact; early flips can be false. Size down during transitions rather than betting big on the first range break.

## Interview-ready summary

Andrew Cardwell reinterpreted Wilder's RSI for trending markets, and it is the most important "advanced RSI" framework. The core ideas: **RSI ranges define the trend** — a bull market holds roughly 40–80 with the **40–50 zone as support**, a bear market holds 20–60 with the **50–60 zone as resistance**; a shift of the range signals a regime change, often earlier than price. In trends, Cardwell's **positive and negative reversals** (a form of hidden divergence read through RSI) replace classic divergence: a positive reversal (RSI lower low, price higher low, in an uptrend) signals *continuation up* and even yields a measured price target, while classic divergences mostly fail in trends and only work at true reversals/ranges. Practically, identify the regime first, buy dips to RSI 40–50 in bull ranges (sell rips to 50–60 in bear ranges) on a reversal + trigger, place stops at the price pivot / range boundary, and translate into option spreads with strikes anchored to the RSI support/resistance price levels. The cardinal error the method fixes: never blindly short "overbought 70+" or buy "oversold 30−" in a trend — in Cardwell's world those readings *confirm* the trend rather than fade it.
