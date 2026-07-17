# Kagi Charts

## What it is and the logic

A Kagi chart is a Japanese charting method that strips price down to a single question: has the trend actually changed, or is this just noise? It does this by drawing a continuous vertical line that ignores time completely and reacts only to price movement of a meaningful size. When price keeps moving in the same direction the line simply extends. When price reverses by more than a defined amount — the *reversal threshold* — the line steps sideways a fraction and then draws a fresh vertical in the new direction. Nothing about the horizontal axis represents clock time. A quiet, ranging Friday afternoon in Nifty may produce two millimetres of chart; a violent gap-down Monday may produce a metre.

The word *kagi* refers to the old L-shaped key that the line's shape resembles. The method dates to the 1870s, when the Japanese rice market at Dojima was one of the most sophisticated futures markets on earth, and traders needed a way to track supply-demand pressure without being fooled by intraday chop. Steve Nison introduced it to Western audiences in *Beyond Candlesticks*, and it now sits inside TradingView, Chartink-adjacent tools, MetaStock and most professional platforms.

The genius of Kagi is its second layer: **line thickness**. The vertical is drawn thin (a *yin* line, weak) or thick (a *yang* line, strong) depending on whether price has broken the previous swing high or low. The line turns thick the moment price rises above the prior peak — the shoulder — and turns thin the moment price falls below the prior trough — the waist. So a single Kagi line silently encodes two independent pieces of information at once: current direction (up-leg or down-leg) and underlying strength (thick = buyers in control, thin = sellers in control). This is why old-school Japanese traders called Kagi the *"supply and demand chart"*. You are literally watching the balance of pressure change colour under your eyes.

Because Kagi filters by price size rather than by time, it does for trend what a good noise gate does for audio: small wiggles below the threshold vanish entirely, and what survives is structure. For a Nifty positional trader drowning in the intraday violence of 2026 — algo-driven, expiry-day gamma spikes, news whips — that filtering is the whole point.

## Construction, rules and settings

A Kagi chart needs exactly one input to be defined: the **reversal amount**. Everything else follows mechanically. There are two common ways to specify it.

**1. Percentage reversal (recommended for Indian equities).** The line reverses only when price moves against the current direction by at least X% of the current level. A 4% setting on Nifty at 24,000 means the line will not turn until price retraces roughly 960 points from the extreme of the current leg. Percentage scaling is self-adjusting: it stays sensible whether Nifty is at 18,000 or 30,000, and whether you apply it to a ₹80 PSU stock or a ₹3,500 large-cap.

**2. Fixed points / ATR reversal.** You specify an absolute number (say 150 points on Bank Nifty) or a multiple of Average True Range (say 2 × ATR). ATR-based reversals are excellent because they automatically widen in volatile regimes and tighten in calm ones.

Here is the exact algorithm the platform runs, tick by tick or candle-close by candle-close:

| Step | Rule |
|------|------|
| Start | Plant the first line at the opening price; direction unknown until first move exceeds the threshold. |
| Extending an up-line | If price makes a new high, extend the vertical line upward. No new line. |
| Extending a down-line | If price makes a new low, extend the vertical downward. |
| Reversal | If price moves against the current direction by ≥ reversal amount, draw a short horizontal "shoulder/waist" step, then start a new vertical in the opposite direction. |
| Thickness up-flip (yang) | When any up-line rises **above the previous high (shoulder)**, the line becomes thick from that point up. |
| Thickness down-flip (yin) | When any down-line falls **below the previous low (waist)**, the line becomes thin from that point down. |

Two vocabulary anchors you must know:

- **Shoulder** — a local high where the line turned down. Prior shoulders are horizontal resistance references.
- **Waist** — a local low where the line turned up. Prior waists are horizontal support references.

The classic mechanical signals are then trivially simple:

- **Buy** = the line turns from thin to thick (price closes above the prior shoulder).
- **Sell / exit** = the line turns from thick to thin (price closes below the prior waist).

That is the entire base system. Note something important about data source: Kagi is usually built on **closing prices** by default, which further suppresses intraday spikes, but most platforms let you switch to High/Low, which reacts faster and produces more, earlier — and noisier — flips. For Indian swing trading, close-based Kagi on the daily timeframe is the sober default.

Choosing the reversal amount is the single decision that matters. A rough guide for 2026 Indian instruments on daily data:

| Instrument | Typical level (2026) | Sensible % reversal | Character |
|------------|----------------------|---------------------|-----------|
| Nifty 50 | ~24,000 | 3–4% | Positional swings, few flips |
| Bank Nifty | ~52,000 | 4–5% | Higher vol, needs wider gate |
| Reliance | ~₹2,900 | 4% | Clean large-cap trends |
| Mid-cap stock | ₹400–1,200 | 5–6% | Wider to survive gaps |
| USDINR | ~83.5 | 1–1.5% | Low vol, tighten the gate |
| MCX Gold | ~₹72,000/10g | 2.5–3% | Trends well, moderate gate |

Smaller reversal = more lines, earlier turns, more whipsaws. Larger reversal = fewer, later, cleaner signals. There is no free lunch; you are choosing where to sit on the responsiveness-vs-reliability curve.

## Worked India example (levels and ₹)

Take **Reliance Industries** on the daily chart across a hypothetical but realistic 2026 up-move, using a **4% percentage reversal on closing prices**.

Reliance is basing near **₹2,780**. The Kagi line is drawing downward and is **thin** — sellers still nominally in charge, price below the last waist. Over two weeks it grinds to a low close of **₹2,742**, then buyers step in.

- Price closes at **₹2,853**. From the ₹2,742 low that is +₹111, which is 4.05% — just over the reversal threshold. The line draws a short shoulder-step and begins a fresh **up-line**. But it is still **thin**: price has not yet exceeded the prior shoulder at ₹2,890.
- Reliance pushes to close **₹2,905**. This clears the prior shoulder of ₹2,890. The Kagi line **flips from thin to thick right at ₹2,890.** *This is the buy signal.* Entry taken near ₹2,905.
- The stock trends. The line extends thick all the way to a close of **₹3,180**, ignoring three separate 1–2% intraday pullbacks along the way because none exceeded the 4% (~₹127) gate. On a candlestick chart those pullbacks would have looked scary; on Kagi they do not exist.
- Eventually price closes **₹3,050**, a retracement of ₹130 from the ₹3,180 high — that is 4.09%, past the gate. The line steps sideways and draws a new **down-line**. It stays **thick** for now because it hasn't yet broken the last waist at ₹3,010.
- Price closes **₹2,995**, below the ₹3,010 waist. The line **flips thick to thin at ₹3,010.** *This is the exit signal.* Position closed near ₹2,995.

Trade result: bought ~₹2,905, exited ~₹2,995, a clean **+₹90 (~3.1%)** capture on a single ₹275 up-swing, having sat through the entire trend without being shaken out by intraday noise — because the noise never rose to the level of a Kagi event. Note the honest part: Kagi gave back the last ₹185 (from ₹3,180 high to ₹2,995 exit). Reversal-threshold methods always surrender the final leg; that is the structural cost of only reacting to confirmed reversals.

For **Bank Nifty futures**, the same logic at a 5% reversal (~₹2,600 at 52,000) would ignore almost all the daily whipsaw that shreds tighter systems, at the cost of entering meaningfully after the turn. Position-sized correctly — say 1% account risk with the stop placed at the last waist — that lag is survivable.

## How to trade it: entry, stop, target, management

**Entry.** The purest Kagi entry is the thin→thick flip (long) or thick→thin flip (short). Take it on the close of the candle that produces the flip, or on the next open. Do not anticipate; the flip either happens or it doesn't.

**Stop.** Kagi hands you a natural, non-arbitrary stop: the **opposing swing**. For a long entered on a thin→thick flip, your invalidation is a thick→thin flip — i.e. a close below the most recent waist. You can place a hard stop just below that waist rather than waiting for the full flip, which caps the loss but risks being clipped on a marginal poke. In the Reliance example, the long at ₹2,905 had its waist at roughly ₹2,853 (the leg's origin); risk was about ₹52, or 1.8%.

**Target.** Kagi is a trend-following tool, so the honest default is *no fixed target* — ride until the opposite flip. If you need targets for a rules book, use prior shoulders (for longs) as reference resistance and take partial profits there, trailing the rest to the flip. Measured-move projections and Fibonacci extensions overlay cleanly because Kagi shoulders and waists are themselves clean swing points.

**Management.** The three professional refinements:

1. **Double-window (tweezer) confirmation.** Wait for the line to make *two* consecutive thick sections above successive shoulders before committing full size — this filters the single-flip fakeout common around Nifty expiry.
2. **Multi-timeframe stacking.** Run a wide-reversal weekly Kagi for the regime (thick = only take longs) and a tighter daily Kagi for entries. Only take daily thin→thick flips while the weekly line is thick.
3. **Scale with thickness persistence.** Add to the position each time the line clears a *new* shoulder (a fresh thick extension), pyramiding into strength, with the stop trailed up to the newest waist.

Position sizing follows directly from the waist-based stop: risk-per-unit = entry − waist; units = (account × risk%) ÷ risk-per-unit. Because Kagi stops are structural rather than arbitrary percentages, the sizing math is unusually clean.

## Confluence

Kagi is a *structure* tool; it pairs best with orthogonal information.

- **Volume.** A thin→thick flip on above-average delivery volume (check NSE delivery %) is far more trustworthy than one on thin volume. Volume confirms that the shoulder break has real participation.
- **Option chain / OI.** On Nifty and Bank Nifty, a Kagi thick-flip that coincides with call-writer capitulation (call OI unwinding at the strike just above) is a high-conviction long. The Kagi tells you structure turned; the OI tells you why.
- **Higher-timeframe trend.** As above — weekly-thick + daily-flip is the bread-and-butter confluence.
- **Support/resistance and round numbers.** A waist forming exactly at a psychological round number (Nifty 24,000, Bank Nifty 50,000) that then produces a thin→thick flip is a textbook long — structure and psychology agreeing.
- **RSI / momentum divergence.** A fresh Kagi shoulder that is *higher* in price but comes with *lower* RSI is an early warning that the next thick extension may fail; tighten stops.

The anti-confluence discipline matters just as much: do not layer three momentum oscillators on top of Kagi. They are all reading the same price and will merely amplify each other. Pair Kagi with something it cannot see — volume, OI, breadth — not with a repackaged version of itself.

## Pitfalls

**1. Choosing the reversal amount by curve-fitting.** It is trivially easy to slide the reversal % until the past year looks perfect. That optimised setting will not survive the next regime. Anchor the setting to volatility (ATR-based) so it adapts, and pick from a small, sensible menu rather than optimising to two decimal places.

**2. Forgetting there is no time axis.** A Kagi line that has barely moved horizontally in a week can lull you into thinking "nothing happened", when in fact price simply stayed inside the gate. Conversely a huge horizontal run can compress a single frantic day. Never read distance-along-the-chart as elapsed time — a mistake that wrecks anyone trying to eyeball "how long" a trend lasted.

**3. Gap risk on Indian stocks.** Overnight gaps — common on results, block deals, regulatory news — can leap straight past a waist, so your "structural stop below the waist" fills far worse than planned. On single stocks, size for gap risk; on index futures this is milder but expiry and global-cue gaps still bite.

**4. Late entries in fast, mean-reverting markets.** In a choppy, rangebound Nifty (say a pre-budget drift), Kagi's whole edge — filtering noise — becomes a liability: every flip is late and the range chops you with buy-high-sell-low flips. Kagi is a *trend* instrument; in a confirmed range, stand aside or switch tools.

**5. Close vs High/Low confusion.** Traders test on close-based Kagi, then trade a High/Low feed that flips earlier and more often, and wonder why live results diverge from the backtest. Fix the data basis before you do anything else, and keep it fixed.

**6. Over-trusting the mechanical signal.** Kagi flips are clean but not magic. In backtests across Indian equities the naive thin/thick flip system is profitable in trending years and mediocre-to-negative in choppy years — like every trend follower. It needs a regime filter and honest costs (brokerage, STT, slippage, which on frequent flips add up) to be viable.

## Interview-ready summary

A Kagi chart is a time-independent Japanese charting method that plots a continuous line reacting only to price moves larger than a defined reversal threshold (percentage, points, or ATR-based). Its defining feature is line thickness: the line turns **thick (yang)** when price breaks above the previous shoulder — buyers in control — and **thin (yin)** when price breaks below the previous waist — sellers in control. The core signals are the **thin→thick flip (buy)** and **thick→thin flip (sell/exit)**, with natural structural stops at the opposing swing. Its strength is superb noise filtering, which makes it ideal for positional trend-following on Nifty, Bank Nifty and liquid NSE stocks (typical daily reversals 3–5%); its cost is late entries and surrendered final legs, plus vulnerability in ranges and to overnight gaps. Trade it with volume and option-chain confluence, a higher-timeframe regime filter, and honest transaction costs. Remember the one-line essence: *Kagi turns the messy war of price into a single line whose direction shows who is winning and whose thickness shows by how much.*
