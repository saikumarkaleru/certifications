# ICT: Order Blocks & Fair Value Gaps

The "Inner Circle Trader" (ICT) methodology, developed and popularised by Michael J. Huddleston, is the most widely followed evolution of supply-and-demand thinking in the retail world of the 2020s. Strip away the sprawling jargon and cult-like community, and ICT is a precise, rules-based dialect of the same idea Chapters 50–51 established: institutions move price to fill orders, they leave footprints, and those footprints can be traded on the return. Where classical S&D draws loose rectangles around bases, ICT tightens the definitions into two flagship concepts — the **order block (OB)** and the **fair value gap (FVG)** — each with a mechanical identification rule. This chapter covers both, honestly separates the genuinely useful mechanics from the over-hyped mysticism, and shows how to apply them to Nifty, Bank Nifty and NSE stocks.

## What it is and the logic

ICT's central premise is that markets are engineered by large "smart money" participants who need liquidity to fill positions. To buy in size, they need sellers; the easiest sellers to find are the stop-losses of traders who are already short (resting sell-stops below a swing low) and the sell-stops of longs (below support). So price is often driven *down* to sweep those resting orders — a **liquidity grab** or **stop hunt** — before reversing sharply upward. The candle from which that reversal launches is the **order block**. The rapid move away frequently leaves a price **inefficiency** — a three-candle gap where price moved so fast that it traded almost one-directionally, called a **fair value gap**. Price, ICT argues, tends to return to "rebalance" these inefficiencies and to react at order blocks, because that is where unfilled institutional interest sits.

Two things are worth stating plainly at the outset. First, the *mechanical* observations — that price sweeps obvious liquidity pools before reversing, and that fast moves leaving imbalances often get partially retraced — are real, observable, and tradeable. Second, the surrounding narrative ("the algorithm is programmed to deliver price to X") is unfalsifiable storytelling. You do not need to believe a central algorithm exists to profit from the fact that stop clusters get run and imbalances get filled. Trade the mechanics; ignore the mysticism.

An order block is essentially the same object as an S&D base, but ICT defines it as a **single specific candle** — the last opposing candle before the impulsive move — rather than a consolidation range. A fair value gap has no real equivalent in classical S&D; it is ICT's genuine addition, a formal way to mark the *inefficiency* left inside the impulse leg itself.

## Construction: rules and settings

### The order block

A **bullish order block** is the *last down-close candle* before a strong up-move that breaks structure. A **bearish order block** is the *last up-close candle* before a strong down-move that breaks structure. The rules:

1. Identify an impulsive move that breaks a recent swing (a **break of structure**, BOS) or shifts the trend (**change of character**, CHoCH).
2. Walk back to the last candle whose body closed *against* the impulse direction. For a bullish OB, that is the last red (down-close) candle before the rally.
3. The order block zone runs from that candle's **open to its low** (bullish OB) or **open to its high** (bearish OB). Some traders use the full high-to-low of the candle including wicks; a tighter, common convention uses the body plus the "wick into the imbalance."
4. A **valid** OB should have caused, or coincided with, a liquidity sweep (it takes out a prior high/low) and should be followed by displacement (see below).

| Element | Bullish OB | Bearish OB |
|---|---|---|
| Candle | last down-close before up-impulse | last up-close before down-impulse |
| Zone top | candle open (or high) | candle high |
| Zone bottom | candle low | candle open (or low) |
| Entry edge (proximal) | top of block | bottom of block |
| Stop | below block low | above block high |

### Displacement and the fair value gap

**Displacement** is ICT's word for an explosive, one-directional move — the same "imbalance" from Chapter 50. The signature of displacement is the **fair value gap**, a three-candle pattern:

- Take any three consecutive candles.
- A **bullish FVG** exists when the **high of candle 1 is below the low of candle 3** — leaving an untraded gap between them, spanned by the large candle 2.
- A **bearish FVG** exists when the **low of candle 1 is above the high of candle 3**.

The gap (the space between candle 1's high and candle 3's low, for a bullish FVG) is the "fair value gap" — a price range that was skipped over in the rush. ICT theory says price is drawn back to fill (rebalance) at least part of this gap. The FVG is drawn as a rectangle spanning that empty range.

An FVG is strongest when it sits *inside* the displacement leg that created an order block and broke structure. The trifecta — **liquidity sweep → CHoCH/BOS with displacement → FVG left behind → order block at the origin** — is the core ICT long/short setup. In ICT shorthand this is often the "**OTE / order block + FVG entry after a liquidity raid**."

### Settings and timeframe pairing

ICT is inherently multi-timeframe. A common structure:

| Purpose | Timeframe (NSE-adapted) |
|---|---|
| Bias / draw on liquidity | Daily, 1-hour |
| Setup / structure | 15-min |
| Entry refinement (OB + FVG) | 5-min, 3-min, 1-min |

Because NSE trades ~09:15–15:30, ICT's "kill zone" concept (originally London/New York sessions for forex) adapts to: the **opening drive 09:15–10:00** (highest volatility, frequent liquidity sweeps of the previous day's high/low) and a **midday reversal window ~11:00–12:30**. The last hour (14:30–15:30) often trends into the close. These are the windows where OB+FVG setups fire cleanly; the dead 12:30–14:00 lunch lull produces low-quality signals.

## Worked India example (levels and ₹)

Take Nifty 50 on the 5-minute chart, an opening-drive scenario (representative 2025–26 levels). The previous day's low was 24,480 — an obvious liquidity pool, since shorts rest sell-stops above it and longs rest buy-stops below it.

- 09:15–09:35: Nifty opens at 24,520 and drifts down, breaking 24,480 to print a low of 24,462 — a **liquidity sweep** of the prior-day low. The last down-close candle before the reversal is a red candle with open 24,478, low 24,462.
- 09:40: a large green candle (candle 2) surges from 24,470 to 24,540 — **displacement**. Candle 1's high was 24,485; candle 3's low is 24,512. Since candle 1 high (24,485) < candle 3 low (24,512), a **bullish FVG** exists in the band **24,485–24,512**.
- This rally breaks the 09:15 opening swing high at 24,530 — a **change of character** confirming the up-shift.
- The **bullish order block** is the last down-close candle: zone **24,462–24,478** (low to open).

Now the setup. Price rallies to 24,560, then pulls back around 09:55. The high-probability entry zones are (a) the FVG at 24,485–24,512 and (b) the order block at 24,462–24,478 if price runs deeper. A patient trader places a buy limit at the top of the FVG (24,512) or splits: half at the FVG, half at the OB.

- Entry: **24,510** (FVG fill).
- Stop: below the order block low + buffer = **24,450** (60-point risk).
- T1: the morning high / prior-day high liquidity at 24,560 (50 points), then the next draw on liquidity — the prior-day high at, say, 24,690.

For one Nifty futures lot (lot size 75, representative): risk = 60 × 75 = **₹4,500**. If price runs to 24,690 (180 points), reward = 180 × 75 = **₹13,500**, a 3:1 trade. The FVG entry gave a tighter stop than a classical S&D base would have, improving R:R — this tightness is ICT's practical advantage.

**F&O expression.** With Nifty near 24,500 you would typically buy an ATM/ITM call or a bull call spread (buy 24,500 CE, sell 24,700 CE). As stressed in Chapter 51, map the 24,450 spot stop to a *premium* stop in advance, because a 60-point adverse move plus theta might cost ₹25–40 of ATM call premium per share. The FVG/OB combination gives you the precise spot invalidation you need to define that premium stop; do not enter the option without it.

**Bank Nifty note.** On Bank Nifty the same setup plays out with bigger numbers and more overshoot. A prior-day-low sweep might dip 80–120 points past the level before the OB forms, and the FVG might be 60–100 points wide. Widen buffers accordingly and prefer confirmation (a lower-timeframe CHoCH) over a blind limit, because Bank Nifty frequently runs *through* an FVG to a deeper order block before turning.

## How to trade it: entry, stop, target, management

**Entry.** Three graded approaches:

- **FVG limit entry:** buy limit at the proximal edge of the FVG (top for bullish). Best R:R, but price sometimes fills the FVG and keeps going to the OB.
- **Order block entry:** buy limit at the OB proximal edge. Deeper, safer fill, slightly worse R:R than the FVG if price only reaches the FVG.
- **Confirmation entry:** wait for price to enter the FVG/OB and print a lower-timeframe CHoCH (a 1-min higher-high after the pullback), then enter. Fewer failed trades, occasional missed moves.

The professional refinement is the **"FVG inside OB" confluence** — when the fair value gap overlaps the order block, that overlap is the highest-odds entry pocket, and you can place the limit there with a tight stop just beyond the OB.

**Stop.** Below the order block low (longs) or above the OB high (shorts), plus a buffer for the stop-hunt overshoot: ~15–25 points on Nifty, ~40–60 on Bank Nifty. Invalidation is a candle *close* through the far side of the order block — at that point the "unfilled orders" thesis is dead and the setup has failed.

**Targets — the "draw on liquidity."** ICT's genuinely useful targeting idea: price moves *from* one liquidity pool *to* another. Your target is the next obvious pool — the prior-day high, an old swing high, a round number (25,000 Nifty, 51,000 Bank Nifty), or an equal-highs cluster (a "liquidity magnet" where many stops rest). Ladder: T1 at the nearest pool (book half, move to break-even), runner toward the next major pool. This "buy at a discount OB, sell into the next liquidity" framing is cleaner than arbitrary Fibonacci targets.

**Management.** Move to break-even after T1. Trail runners below successive FVGs or order blocks formed on the way up (each new bullish FVG becomes a trailing support reference). If a fresh opposing order block forms against you mid-trade, tighten or exit.

## Confluence

ICT stacks best with:

- **Liquidity logic:** the setup is only A-grade if it followed a genuine sweep of an obvious pool (prior-day high/low, equal highs/lows, session high/low). No sweep, lower conviction — you are just buying a dip.
- **Premium/discount (the "dealing range"):** mark the swing high to swing low, split at 50% (the equilibrium). Buy order blocks only in the **discount** half (below 50%); sell only in the **premium** half. This is ICT's version of "buy low, sell high" and materially improves results.
- **Higher-timeframe alignment:** a 5-min bullish OB inside a fresh 1-hour bullish OB, both in a daily uptrend, is a conviction stack.
- **Classical S&D and Fibonacci:** an OB that coincides with a demand zone and the 62–79% "OTE" (optimal trade entry) retracement is quadruple confluence.
- **Indian F&O / OI:** an OB below price that sits at a strike with heavy Put open interest (put-writer support) is chart-plus-order-flow agreement; a bearish OB at a heavy Call-OI strike is reinforced resistance. This TA+OI overlay is the most valuable India-specific confluence.
- **Volume:** the displacement candle should carry a volume spike; a "displacement" on thin volume is suspect.

## Pitfalls

- **Curve-fitting the narrative.** ICT's biggest danger is that with enough OBs and FVGs on a chart, you can explain *any* move after the fact. Mark levels live, before price returns, or you are storytelling.
- **Every candle becomes an order block.** There are dozens of "last opposing candles" on any chart. Only OBs that produced a liquidity sweep *and* displacement *and* a break of structure qualify. Be ruthless.
- **FVGs everywhere.** Small three-candle gaps appear constantly; most get filled trivially and mean nothing. Trade only FVGs that sit inside a real displacement leg tied to structure.
- **Ignoring premium/discount.** Buying an order block in the premium half of the range (near the highs) is the most common ICT losing trade. Respect equilibrium.
- **Over-refining timeframes.** Dropping to the 15-second chart to find a "perfect" OB is analysis paralysis and drowns in noise. 5-min/1-min is enough for NSE intraday.
- **Options R:R illusion.** As with all S&D-family methods, a 3:1 *chart* trade is not a 3:1 *option* trade after theta and IV. Use futures or deep-ITM for linear payoff, and pre-map the spot stop to a premium stop.
- **Event and expiry blindness.** OB/FVG logic is noise on Bank Nifty expiry afternoons and around results/RBI/Fed. Sit out.
- **The subjectivity that is denied.** The ICT community often presents the method as mechanically precise; in practice, "which candle is the order block" and "is this displacement" involve genuine discretion. Standardise your own rules (body vs wick, what counts as displacement), journal them, and be consistent — do not pretend it is an algorithm.

## Interview-ready summary

ICT reframes supply-and-demand in a precise, liquidity-first dialect. An **order block** is the last opposing-close candle before an impulsive, structure-breaking move — a bullish OB is the last down-close before a rally, drawn from its open to its low; a bearish OB inverts. A **fair value gap** is a three-candle imbalance where candle 1's high sits below candle 3's low (bullish) — a price inefficiency the market tends to return to and rebalance. The flagship setup chains four events: a **liquidity sweep** of an obvious pool (prior-day high/low, equal highs), a **change of character / break of structure** on **displacement**, an **FVG** left in the impulse, and the **order block** at the origin — entered on the return via a limit at the FVG or OB (best when they overlap), stopped just beyond the order block, and targeted at the next **draw on liquidity**. Confluence with **premium/discount equilibrium** (buy discount OBs, sell premium OBs), higher-timeframe alignment, and Indian **Put/Call OI walls** raises conviction. The mechanics — stops get hunted, imbalances get filled — are real and tradeable; the surrounding "the algorithm delivers price" narrative is unfalsifiable and should be ignored. Traded with discipline (live marking, ruthless filtering, premium/discount respect, futures or spreads to preserve R:R, and events/expiry avoided), ICT is a legitimate precision-entry framework; treated as a mystical certainty, it becomes hindsight storytelling.
