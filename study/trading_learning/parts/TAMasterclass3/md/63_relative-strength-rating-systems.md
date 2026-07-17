# Relative-Strength Rating Systems

Most traders confuse two very different ideas that share a name. The RSI — the Relative Strength *Index* invented by Welles Wilder — measures a single instrument against *its own past*. It has nothing to do with relative strength in the sense that this chapter uses the term. True **relative strength (RS)** is a *comparative* measure: how a stock is performing *against other stocks*, or against a benchmark like the Nifty 50. It is the engine behind momentum investing, sector rotation, and the entire IBD/CAN SLIM school of stock selection. In a market of 2,000-plus listed names, the single most useful filter you can build is one that ranks every stock by strength and lets you fish only in the top decile. This chapter builds that filter from scratch for Indian markets.

## What it is and the logic

The premise is empirical and stubborn: **strength persists**. Stocks that have outperformed the broad market over the last 6-12 months tend to keep outperforming over the next 1-3 months. This is the momentum anomaly, documented by Jegadeesh and Titman (1993) across decades and dozens of markets, including India (multiple NSE-based studies confirm a robust 6-1 and 12-1 momentum premium on Indian equities). It is one of the few edges in markets that has survived out-of-sample, survived publication, and survived transaction costs — though, as we will see, costs and turnover matter enormously.

The intuition is behavioural. Institutions cannot buy a full position in a day; when a fund decides HDFC Bank is a buy, it accumulates over weeks. That persistent buying pressure shows up as sustained outperformance. Analysts anchor and revise estimates slowly, so good news gets priced in gradually. Retail traders under-react to fresh trends and then over-react late. All of this creates a window where *the leaders keep leading*. Relative-strength rating systems are simply a disciplined way to find those leaders and avoid the laggards.

Contrast this with buying "cheap" stocks that have fallen. Bottom-fishing feels smart but statistically fights the momentum current. A stock making new relative lows against the Nifty is usually making them for a reason the market understands before you do. RS systems flip the question from "what is undervalued?" to "what is the market voting for with real money?"

## Construction, rules and settings

There are three broad ways to compute relative strength. Each has a place.

**1. The RS Ratio (line).** The simplest measure. Divide the stock's price by the benchmark's price:

```
RS Ratio = Stock Price / Benchmark Price
```

For an NSE stock you use the Nifty 50 (or a sector index) as the denominator. On TradingView you plot this directly: type `RELIANCE/NIFTY` in the symbol box and you get the RS line. When that line rises, Reliance is outperforming the Nifty regardless of whether Reliance itself is up or down in rupee terms. This is the crucial mental shift — **RS can rise in a falling market** if the stock falls less than the index. Defensive leadership in a bear phase shows up here first.

**2. The RS Rating (percentile rank).** This is the IBD-style number from 1 to 99. You compute each stock's price performance over a lookback, then rank it against the entire universe and express it as a percentile. An RS Rating of 90 means the stock outperformed 90% of all stocks. IBD's proprietary formula weights recent quarters more heavily:

```
Raw RS = 0.40 × (3-month return)
       + 0.20 × (next 3-month return)
       + 0.20 × (next 3-month return)
       + 0.20 × (final 3-month return)
```

That is a 12-month lookback with the most recent quarter double-weighted. You then percentile-rank the raw score across the universe. In India, Chartink and MarketSmith India publish exactly this kind of rating; you can also compute it yourself (code below).

**3. The Mansfield RS (zero-centred oscillator).** Stan Weinstein's version normalises the RS ratio against its own moving average so it oscillates around a zero line:

```
Mansfield RS = ((RS Ratio today / MA of RS Ratio) − 1) × 100
```

where the MA is typically a 52-week average of the RS ratio. Above zero = outperforming its recent norm; a cross above zero after a base is a classic Weinstein Stage-2 confirmation.

The table below summarises settings for an Indian swing-to-position workflow:

| Measure | Formula core | Lookback | Best use | Where to get it in India |
|---|---|---|---|---|
| RS Ratio line | Stock / Index | Live | Visual leadership, divergence | TradingView `SYM/NIFTY` |
| IBD RS Rating | Weighted 12m return, percentile | 12 months | Universe screening, top-decile filter | MarketSmith India, Chartink |
| Mansfield RS | RS ratio vs 52w MA | 52 weeks | Stage analysis, base breakouts | TradingView (Pine) |
| RRG (RS-Ratio + RS-Momentum) | Normalised RS + its momentum | ~14 weeks | Sector rotation quadrants | Optuma, StockEdge, custom |

### Relative Rotation Graphs (RRG)

RRG deserves special mention because it is the most powerful *sector* tool for Indian rotation. It plots two axes: **JdK RS-Ratio** (x-axis, the level of relative strength) and **JdK RS-Momentum** (y-axis, the rate of change of that strength). Both are normalised around 100. This creates four quadrants that a sector or stock rotates through, usually clockwise:

- **Leading** (top-right): strong and still strengthening — hold longs.
- **Weakening** (bottom-right): still strong but momentum fading — trim, tighten stops.
- **Lagging** (bottom-left): weak and getting weaker — avoid or short.
- **Improving** (top-left): weak but momentum turning up — early accumulation candidates.

StockEdge and several Indian platforms now offer RRG on NSE sector indices (Nifty Bank, Nifty IT, Nifty Auto, Nifty FMCG, Nifty Metal, etc.). Watching sectors rotate clockwise through these quadrants is how you anticipate where leadership is *heading*, not just where it has been.

## Worked India example (levels and ₹)

Let us build a concrete RS screen as it might have looked on a real trading day. Suppose the Nifty 50 is at 24,000, roughly flat over three months (say it was 23,800 three months ago — a +0.8% index return). We compute the 3-month relative return for a handful of names:

| Stock | Price 3m ago | Price now | Stock return | Nifty return | RS (excess) |
|---|---|---|---|---|---|
| Trent | ₹5,400 | ₹6,750 | +25.0% | +0.8% | **+24.2%** |
| Dixon Tech | ₹9,800 | ₹12,100 | +23.5% | +0.8% | **+22.7%** |
| Bharti Airtel | ₹1,480 | ₹1,690 | +14.2% | +0.8% | +13.4% |
| HDFC Bank | ₹1,650 | ₹1,710 | +3.6% | +0.8% | +2.8% |
| Asian Paints | ₹2,900 | ₹2,480 | −14.5% | +0.8% | **−15.3%** |
| Hindustan Unilever | ₹2,650 | ₹2,380 | −10.2% | +0.8% | −11.0% |

Rank the whole Nifty 500 this way and Trent and Dixon land in the top few percentiles — RS Ratings near 95-99. Asian Paints and HUL sit near the bottom. The screen's message is blunt: money is flowing into retail/consumer-discretionary and EMS (electronics manufacturing) names and out of staples/paints. You would build your long watchlist from the top of the list *only*, and you would refuse to "average down" on Asian Paints no matter how attractive its valuation looks, because its RS is telling you the smart money is still leaving.

Now overlay the RS *line*. Plot `TRENT/NIFTY` on TradingView. If that line is making a series of higher highs and higher lows and has just broken to a new 52-week relative high while Trent's absolute price consolidates in a tight flag between ₹6,600 and ₹6,800 — that is the highest-conviction setup RS offers: **new relative-strength high preceding a price breakout.** The RS line leading price is the tell that institutions are accumulating into the consolidation.

## How to trade it (entry, stop, target, management)

RS is a *filter and a confirmation*, not a standalone trigger. The workflow:

1. **Screen weekly.** Every weekend, pull the universe (Nifty 500 or your liquid F&O list) and keep only RS Rating ≥ 80. This is your pond.
2. **Wait for a price setup within that pond.** A base breakout, a flag, a pullback to the 20/50-EMA that holds. RS gets you the *right stocks*; price structure gets you the *right moment*.
3. **Entry:** buy the breakout of the consolidation. In the Trent example, buy the break above ₹6,800 on volume.
4. **Stop:** below the base low or the last swing low. If Trent's flag low is ₹6,600, and you enter at ₹6,810, your stop at ₹6,580 is a ~3.4% risk. Position-size so that 3.4% equals no more than 0.75-1% of capital.
5. **Target:** momentum targets are trailed, not fixed. Ride with a moving-average trail (e.g. weekly close below 10-week EMA) or a chandelier stop. The whole point of momentum is to let winners run to fat right-tail outcomes; capping the target at 1:2 defeats the strategy's math.
6. **Management via RS itself:** exit or trim when the *RS line rolls over* — when the stock stops outperforming even if its price is still drifting up. On RRG, a move from Leading into Weakening is your early warning.

A cleaner rotational variant for a portfolio: hold the **top 10 RS-ranked F&O stocks**, rebalance monthly, drop any that fall out of the top 30, replace with the new top entrants. This is a mechanical momentum portfolio and it is exactly what many quant PMS products in India run under the hood.

## Confluence

RS is most trustworthy when it stacks with:

- **Volume / accumulation:** an Accumulation-Distribution or OBV line confirming the RS line. Rising RS on rising volume is institutional; rising RS on dead volume is suspect.
- **Fundamental momentum:** IBD's full CAN SLIM pairs RS with earnings acceleration (the "C" and "A"). In India, cross-check that the RS leader also has improving quarterly EPS and rising sales — Trent, Dixon and similar leaders of recent years all had genuine earnings acceleration underneath the RS.
- **Sector RS:** a top-RS stock inside a top-RS sector (Leading quadrant on RRG) is far stronger than a lone leader in a lagging sector. Rank sectors first, then stocks within the winning sectors.
- **Stage analysis:** Weinstein Stage 2 (price above a rising 30-week MA) *plus* Mansfield RS above zero is the textbook high-probability long.

## Pitfalls

**Momentum crashes.** The ugly secret of momentum is its left tail. After sharp market bottoms (March 2009, March 2020, the post-COVID snapback), the *prior losers* violently outperform and the crowded momentum leaders get crushed. A pure RS-long book can suffer double-digit drawdowns in days during these reversals. Manage with a market-regime filter: only run full momentum exposure when the Nifty is above its 200-DMA; cut exposure hard when it is below.

**Turnover and cost.** Chasing the freshest RS leaders means high turnover. In India, factor in STT, brokerage, exchange fees, GST and stamp duty — round-tripping a position can cost 0.10-0.30% depending on segment. Monthly rebalancing a 10-stock book is manageable; weekly churn often eats the edge alive. Backtest *net* of these costs, always.

**Extended entries.** The commonest beginner error: an RS Rating of 99 tells you the stock has *already* run. Buying it 40% above its base, far from any support, is buying strength at the worst price. RS qualifies the stock; you still must wait for a *low-risk entry point* — a base, flag, or pullback — not chase vertical extension.

**Illiquidity distortion.** In small-caps, a thin stock can post a huge RS from a few buy orders. Restrict serious RS screening to liquid names (F&O universe or Nifty 500 with a minimum turnover filter, say ₹25 crore average daily value) so the ranking reflects real institutional flow.

**Benchmark choice matters.** RS against the Nifty 50 flatters large-caps in a large-cap-led market and vice versa. For a mid-cap name, also check RS against the Nifty Midcap 150 so you know whether it is leading its *own* peer group or just riding a mid-cap wave.

### A minimal Python RS-rating computation

```python
import pandas as pd

# prices: DataFrame, columns = tickers, index = daily dates
def ibd_rs_rating(prices, asof):
    q = 63  # ~one trading quarter
    p = prices.loc[:asof]
    r1 = p.iloc[-1] / p.iloc[-q]   - 1
    r2 = p.iloc[-q] / p.iloc[-2*q] - 1
    r3 = p.iloc[-2*q] / p.iloc[-3*q] - 1
    r4 = p.iloc[-3*q] / p.iloc[-4*q] - 1
    raw = 0.4*r1 + 0.2*r2 + 0.2*r3 + 0.2*r4
    rating = raw.rank(pct=True) * 99      # 1..99 percentile
    return rating.round(0).sort_values(ascending=False)

# top20 = ibd_rs_rating(prices, '2026-07-16').head(20)
```

Feed it end-of-day bhavcopy data from the NSE (free) or any data vendor, and you have your own MarketSmith-style rating engine that costs nothing.

## Interview-ready summary

Relative strength measures a stock *against the market*, not against itself (that is RSI, a different animal). It exploits the well-documented momentum anomaly: 6-12 month leaders tend to keep leading over the next 1-3 months. Compute it three ways — the RS ratio line (stock/Nifty), the IBD percentile rating (1-99, recent-quarter-weighted), and Mansfield/RRG for stage and rotation. Use it as a *filter*: screen weekly for RS ≥ 80, then wait for a proper base or flag breakout inside that pond, stop under the base, and trail winners to capture the momentum right-tail. Confirm with volume, earnings acceleration, and sector RS (RRG Leading quadrant). Respect the two killers — momentum crashes at market bottoms (gate exposure with the 200-DMA) and cost/turnover in the STT-heavy Indian market (rebalance monthly, not daily; trade liquid names only). RS does not tell you *when* to buy; it tells you *what* is worth watching. Price structure supplies the trigger.
