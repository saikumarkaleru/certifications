# Weinstein Stage Analysis

Stan Weinstein published *Secrets for Profiting in Bull and Bear Markets* in 1988, and almost four decades later his framework remains one of the cleanest ways to answer the single most important question in trading: **should I even be looking to buy this stock right now, or is it garbage I should leave alone?** Most retail traders in India spend their energy hunting for the perfect entry candle. Weinstein flips the priority — get the *stage* right first, and a mediocre entry inside a good stage will still make money, while a perfect entry inside a bad stage will bleed you dry. This chapter treats Stage Analysis as a complete top-down trend-following *system*, not just a chart-labelling exercise, and adapts every rule to Nifty 50 stocks, the indices, and the realities of NSE liquidity and F&O.

## What it is & the logic

Weinstein's core insight is that every stock, index, commodity or currency moves through a repeating four-stage cycle relative to its own long-term moving average. The cycle is driven by the accumulation-and-distribution behaviour of large, informed money — the same auction logic Wyckoff described, but packaged into a decision tree a part-time trader can run in ten minutes a weekend.

The four stages are:

- **Stage 1 — Basing / Accumulation.** After a decline exhausts itself, the stock stops falling and drifts sideways in a range. The long-term moving average flattens out. Smart money quietly accumulates from discouraged holders. Nothing seems to be happening — which is exactly the point. You do **not** buy here; you build a watchlist.
- **Stage 2 — Advancing / Markup.** Price breaks *up and out* of the Stage 1 base on expanding volume and pulls the moving average up with it. This is the only stage where you should be aggressively long. The bulk of the entire move happens here.
- **Stage 3 — Topping / Distribution.** The advance loses momentum, price churns sideways in a volatile range near the highs, and the moving average rolls over from rising to flat. Smart money distributes to the euphoric crowd. You take profits and stop initiating longs.
- **Stage 4 — Declining / Markdown.** Price breaks *down and out* of the Stage 3 top below a falling moving average. This is where portfolios are destroyed. You must be out — and for F&O traders, this is where short setups live.

The genius is the discipline it imposes. Weinstein's rule is blunt: **buy only in Stage 2, hold through Stage 2, sell in early Stage 3 or on the break into Stage 4, and never, ever buy in Stage 4** no matter how "cheap" the stock looks or how good the story is. The number of Indian investors who bought Yes Bank, PC Jeweller, Vodafone Idea or Suzlon "for the long term" on the way down — deep in Stage 4 — is the entire argument for this method.

## Construction, rules & settings

### The moving average

Weinstein used a **30-week simple moving average** on weekly charts as his primary trend filter. Thirty weeks is roughly 150 trading days, so on a daily chart the equivalent is the **150-day SMA** (many practitioners round to the more familiar 200-DMA; both work, 150 is slightly more responsive). The slope of this average — rising, flat, or falling — is the single most important variable in the whole system.

| Element | Weinstein setting | Indian daily-chart equivalent |
|---|---|---|
| Primary trend MA | 30-week SMA | 150-day SMA (or 200-DMA) |
| Chart timeframe | Weekly (primary), daily (timing) | Weekly for stage; daily for entry |
| Volume confirmation | Weekly volume vs prior weeks | Daily volume vs 50-day average |
| Relative strength | Stock vs market index line | Stock ÷ Nifty 50 (Mansfield RS) |

### Mansfield Relative Strength

Weinstein's second pillar is **relative strength** — not the RSI oscillator, but a *ratio line* comparing the stock to the market. The Mansfield RS = (stock price ÷ index) normalised so the zero line is the moving average of that ratio. The rule: **only buy Stage 2 breakouts where RS is above zero and rising**, i.e. the stock is outperforming Nifty, not just going up because the whole market is going up. On TradingView you plot this with the "Relative Strength" comparison against NSE:NIFTY; on Chartink you can screen for it directly.

### The four-stage decision rules

| Stage | Price vs 30W MA | MA slope | Volume signature | Action |
|---|---|---|---|---|
| 1 Basing | Oscillating around a flat MA | Flat | Dull, contracting | Watchlist only |
| 2 Advancing | Above rising MA | Rising | Expands on up-weeks | **Buy / hold long** |
| 3 Topping | Whipsawing around flattening MA | Flattening | Erratic, spiky | Take profits, tighten stops |
| 4 Declining | Below falling MA | Falling | Expands on down-weeks | Out / short (F&O) |

### The Stage 2 breakout — precise entry rules

A valid Stage 2 entry requires **all** of the following:

1. Price closes decisively above the resistance ceiling of the Stage 1 base (a weekly close, not an intraday poke).
2. The 30-week MA has stopped falling and is flat-to-rising.
3. Volume on the breakout week is meaningfully above the recent average (Weinstein wanted at least double the average of the prior few weeks — in practice, a clear surge).
4. Mansfield RS is above zero.

Weinstein offered two entry tactics: the **aggressive** entry (buy the breakout as it happens) and the **conservative** entry (wait for the first pullback toward the breakout level, which often retests the old resistance as new support). In Indian markets, where breakouts frequently see a one-to-three-day "throwback," the pullback entry materially improves your risk-reward.

## Worked India example (levels & ₹)

Take a stylised but realistic example modelled on how a mid-cap capital-goods stock behaves in an up-cycle. Assume **Stock XYZ** on NSE.

**Stage 1 (basing):** For roughly seven months XYZ chops between ₹380 and ₹440. The 200-DMA, which had been falling through the prior decline, flattens out around ₹410. Weekly volumes are dull. RS versus Nifty is hovering near zero — XYZ is neither leading nor lagging. You add it to your watchlist and mark the ceiling: **₹440**.

**Stage 2 breakout:** In one week XYZ closes at ₹462 — a clean weekly close above ₹440 — on volume roughly 2.3x its 10-week average. The 200-DMA has turned up from ₹410 to ₹416. RS versus Nifty has crossed above zero and is rising. This is a textbook Stage 2 launch.

- **Aggressive entry:** buy at ₹462 on the breakout close.
- **Conservative entry:** three sessions later XYZ throws back to ₹445, holds the old ₹440 ceiling as support, and turns up. You buy at ₹448.

**Stop placement:** Weinstein places the initial stop below the breakout point / below the base. A logical stop sits under ₹438 (below the retested ceiling and below a swing low), say **₹436**. From the ₹448 entry that is a risk of ₹12 per share, about 2.7% — very tight for a position trade.

**Position sizing:** with a ₹5,00,000 account risking 1% (₹5,000) per trade, quantity = ₹5,000 ÷ ₹12 = **416 shares** (round to 400). Capital deployed ≈ ₹1,79,200.

**The advance:** over the next five months XYZ rides its rising 200-DMA from ₹448 to ₹690. Each pullback finds support at the rising average. You trail your stop up beneath successive swing lows.

**Stage 3 top:** near ₹690 the character changes — three weeks of wide, overlapping, high-volume churning between ₹650 and ₹700 with no net progress. The 200-DMA, now around ₹600, flattens. RS versus Nifty rolls over. You sell into strength around ₹678, or on the break below the ₹650 range floor. From ₹448 to ₹678 is **+₹230/share, roughly +51%**, or about ₹92,000 on 400 shares against ₹4,800 of initial risk — a realised reward-to-risk near 19:1 on a trade you sized to lose ₹5,000.

**Stage 4:** XYZ subsequently breaks ₹650, loses the 200-DMA at ₹600, and the average turns down. Had you "held for the long term," you'd have watched ₹678 become ₹430. Stage discipline is what banks the gain.

## How to trade it — entry, stop, target, management

**Entry.** Prefer the conservative pullback entry on liquid NSE names; use the aggressive breakout entry only on your highest-conviction leaders where you fear missing the move. Always demand the volume surge and positive RS — a breakout without volume in Indian mid-caps is frequently an operator-driven trap that reverses within a week.

**Stop.** Initial stop just below the base/breakout level. This is non-negotiable and defines your position size, never the other way around. Weinstein was emphatic: the stop protects you from the times your stage read is simply wrong.

**Targets & trailing.** Stage Analysis is a *trend-following* method, so you don't set a fixed profit target — you let Stage 2 run and exit when the stock tells you it's entering Stage 3. Practical trailing tools: (a) trail beneath the rising 30-week / 200-day MA; (b) trail beneath successive higher swing lows; (c) exit a portion on the first weekly close back below the MA. Weinstein's own preference was to hold as long as price stayed above a rising average and RS stayed positive.

**Management with F&O.** For a Nifty or Bank Nifty *index* Stage read, you can express Stage 2 with long futures or bull call spreads and, crucially, use Stage 4 to justify bearish positions (long puts, bear put spreads) — the framework gives you *directional permission* that keeps you out of the classic mistake of shorting a raging Stage 2 or bottom-fishing a Stage 4.

## Confluence

Stage Analysis becomes far more powerful stacked with:

- **Market stage first.** Run the four-stage read on Nifty 50 itself. Weinstein insisted you fight the tape less when the *market* is in Stage 2. In a market Stage 4 (a genuine bear phase like 2008 or Mar 2020), even good stocks fail — reduce size or stand aside.
- **Sector stage second.** Check the sector index (Nifty Bank, Nifty IT, Nifty Auto). A Stage 2 stock inside a Stage 2 sector inside a Stage 2 market is the highest-probability long you can find.
- **Relative strength ranking.** Among Stage 2 candidates, prefer the ones with the strongest, longest-rising RS line — the market leaders.
- **Volume / Wyckoff.** A Stage 1 base showing a Wyckoff spring or a clear absorption of supply before breakout raises conviction.
- **Point-and-figure or horizontal volume.** Confirms the width of the base — wider bases (longer Stage 1) tend to fuel longer Stage 2 advances.

## Pitfalls

- **Anticipating Stage 2.** Buying inside Stage 1 "before it breaks out" because you're impatient. Bases can drag for months; capital tied up in a stock going nowhere is capital not compounding elsewhere. Wait for the breakout.
- **Mistaking a bounce for Stage 2.** A sharp rally inside Stage 4, below a falling MA, is a *bear-market rally*, not a new uptrend. If the MA is still falling and RS is negative, it is not Stage 2 — full stop. This is the single most expensive error, and it's how averaging-down victims get trapped.
- **Ignoring volume.** A breakout on dull volume in an Indian small/mid-cap is often manipulation. No volume, no trade.
- **Whipsaw in choppy markets.** In a broad, rangebound market the MA slope keeps flattening and stocks fake breakouts. Use the market-stage filter to reduce activity in these phases.
- **Over-labelling.** Real charts are messier than textbook diagrams. Don't force a stage label on ambiguous price action — if you can't tell whether it's late Stage 1 or early Stage 2, it's a watchlist item, not a trade.
- **Survivorship in backtests.** Testing the method only on today's index constituents flatters it; the delisted Stage 4 disasters (which the method would have kept you *out* of) are exactly its value, so include the failures.

## Interview-ready summary

Weinstein Stage Analysis classifies any instrument into one of four repeating phases relative to its **30-week (≈150/200-day) moving average**: Stage 1 basing (flat MA, accumulate — watchlist only), Stage 2 advancing (price above a rising MA on expanding volume — the only buy zone), Stage 3 topping (flattening MA, volatile churn — take profits), and Stage 4 declining (price below a falling MA — be out, or short via F&O). Confirmation requires a **volume surge** on the Stage 2 breakout and **positive, rising Mansfield relative strength** versus Nifty. It is a top-down trend-following system: read the market's stage, then the sector's, then the stock's, and only stack longs when all three align. The stop sits just below the base and defines position size; you trail the rising average rather than setting a fixed target. Its greatest practical value in Indian markets is negative — it is the discipline that stops you from averaging down into Stage 4 wealth-destroyers like the market repeatedly produces.
