# Chart Types: Line, Bar, Candles, Heikin-Ashi, Renko, P&F

## What it is & why it works

A chart is a *choice* about how to compress the firehose of trades into a picture a human can read. The same Nifty session can be drawn six different ways, and each drawing deliberately keeps some information and throws the rest away. That is not a flaw — it is the point. A line chart throws away everything but the close to reveal the clean skeleton of trend. A Renko chart throws away *time itself* to isolate pure price movement. A serious technician does not have a "favourite" chart type; they choose the representation whose *deliberate blindness* matches the question they are asking. Choosing the wrong chart is like using a microscope to read a road map.

Why does the choice matter so much? Because every trading decision is a signal-versus-noise problem, and each chart type sits at a different point on that trade-off. Candlesticks preserve maximum intrabar detail — open, high, low, close — which is rich signal *and* rich noise. Renko and Heikin-Ashi smooth aggressively — less noise, but at the cost of lag and hidden detail. Understanding *exactly what each chart discards* tells you precisely where it will lie to you. A trader who knows that a Heikin-Ashi candle's "close" is a fabricated average will never be fooled into thinking price actually traded there; a trader who does not will place a stop at a price the market never printed.

The unifying idea: charts are all built from the same four numbers per period — **Open, High, Low, Close (OHLC)** — plus, in some cases, the abandonment of time or the filtering of small moves. Master what each type keeps and discards, and you can pick the right lens instantly for the job: line for macro trend and clean levels, candles for entries and reversal patterns, Heikin-Ashi and Renko for riding and filtering trends, and Point & Figure for objective support/resistance and price targets stripped of all time-based noise.

## The mechanics

**Line chart.** Connects only the closing price of each period. Discards open, high, low, and all intrabar action. Its virtue is the close's significance — the close is the price at which the market *settled*, the value both sides agreed to hold overnight, and thus the least noisy single number. Best for: long-horizon trend, spotting the cleanest support/resistance, and comparing multiple instruments (a "spaghetti" of Nifty vs. Bank Nifty vs. Nifty IT closes).

**Bar chart (OHLC bar).** A vertical bar from low to high; a left tick marks the open, a right tick the close. Shows the full range and the open-to-close direction. Preferred by some Western technicians for its uncluttered look, but the body direction is harder to read at a glance than a candle.

**Candlestick.** The same OHLC as a bar, but the *body* (open-to-close) is filled/coloured and the *wicks* (shadows) show the high and low. A green/hollow body = close above open (bulls won the period); a red/filled body = close below open (bears won). Candles make the *battle* within each period visually instant — a long lower wick screams rejection of lower prices; a small body screams indecision. This visual richness is why candlesticks dominate pattern recognition (doji, engulfing, hammer, pin bar). Nothing is discarded relative to a bar; the information is simply *encoded more legibly.*

| Element | What it shows |
|---|---|
| Body | Open-to-close range and direction |
| Upper wick | Highest price rejected (sellers defended) |
| Lower wick | Lowest price rejected (buyers defended) |
| Body colour | Who won the period (green up / red down) |

**Heikin-Ashi ("average bar").** A *derived* candle. It replaces real OHLC with smoothed values:

- HA-Close = (Open + High + Low + Close) / 4  — the average of the real bar.
- HA-Open = (previous HA-Open + previous HA-Close) / 2  — the average of the prior HA candle.
- HA-High = max(High, HA-Open, HA-Close); HA-Low = min(Low, HA-Open, HA-Close).

The effect: consecutive candles are chained through the prior HA-Open, which *smooths noise* and produces long runs of same-colour candles in a trend — often with *no lower wicks* in a strong uptrend and *no upper wicks* in a strong downtrend. Crucially, the HA-Close and HA-Open are **fabricated averages — not prices the market ever traded.** HA is a trend-visualisation filter, not a source of real levels.

**Renko.** Abandons time entirely. A new "brick" is drawn only when price moves a fixed amount — the *box size* (e.g., 50 points on Bank Nifty, or an ATR-based size). Up-bricks and down-bricks are all identical in size; a *reversal* requires price to move (typically) two box sizes in the opposite direction before an opposite-colour brick prints. Because bricks form only on meaningful moves, Renko strips out sideways chop and time-based noise, leaving a starkly clean trend and very obvious support/resistance. The cost: it *lags* (a brick prints only after the full box move) and it *hides* how long a move took and any move smaller than the box.

**Point & Figure (P&F).** The oldest Western method, also time-independent. Columns of **X's** (rising prices) and **O's** (falling prices) are plotted on a grid defined by a *box size* and a *reversal amount* (classically 3 boxes). A new X is added each time price rises one box; the column switches to O's only when price reverses by the reversal amount (e.g., 3 boxes). P&F filters all minor noise, produces beautifully objective horizontal support/resistance and trendlines, and — uniquely — generates **price targets** via the vertical count (target = breakout price ± (column boxes × box size × reversal)) and horizontal count (width of a base projects the move).

| Chart type | Discards | Best used for |
|---|---|---|
| Line | O, H, L, intrabar | Macro trend, clean levels, comparisons |
| Bar / Candle | Nothing (full OHLC) | Entries, reversal patterns, precision |
| Heikin-Ashi | Real O & C (averaged) | Riding trends, filtering wobble |
| Renko | Time, sub-box moves | Pure trend, obvious S/R, filtering chop |
| P&F | Time, minor moves | Objective S/R, trendlines, price targets |

## Reading it — a worked India example

Take a single Bank Nifty swing — a trend up from **53,000 to 55,500** over two weeks, with a two-day shakeout in the middle — and read it through four lenses.

*On a daily candlestick chart:* you see everything. The rally shows green bodies with rising closes, but the mid-move shakeout prints two ugly red candles with long lower wicks — price stabbed down to 53,900 intraday but *closed* back near 54,600, leaving long lower shadows that reveal buyers aggressively defending. Those wicks are pure signal: they tell you the dip was rejected. A candle reader buys that rejection. But the two red bodies also create *visual anxiety* — the noise that shakes weak hands out.

*On a line chart (closes only):* the same two weeks look almost serene — a smooth rising line from 53,000 to 55,500 with a shallow dip to the 54,600 close. The shakeout's intraday terror vanishes because the closes never broke trend. This is the line chart's gift: it shows you the *settled* path and confirms the uptrend was never structurally threatened on a closing basis. Perfect for confirming the macro trend is intact and for drawing the clean rising support line through the closes.

*On a Heikin-Ashi chart:* the uptrend renders as a run of green candles with *no lower wicks* — the smoothing absorbs the shakeout into a couple of green candles with small bodies and tiny lower wicks rather than scary red bodies. The HA chart keeps you *in* the trade: the first red HA candle (with an upper wick) would be your visual "trend weakening" cue, and it never appeared during the shakeout. Warning: the HA-Close of ~54,900 during the dip is an *average*, not a traded price — Bank Nifty actually traded down to 53,900. Never set a stop off the HA candle.

*On a Renko chart (50-point boxes):* the two-day shakeout — because it was less than the ~2-box reversal — may print only one or two down-bricks before green bricks resume, or none at all. The chart shows an almost unbroken column of green bricks from 53,000 to 55,500, with the prior swing high at 54,800 clearly acting as support once broken. Renko makes the trend and the level unmistakable, but it *cannot tell you* the dip was scary or that it took two days — time and the intraday fear are gone.

*On a P&F chart (50-point box, 3-box reversal):* you see a long column of X's up to 55,500. The shakeout, being under 150 points (3 × 50), does *not* generate a new O-column — it is filtered out entirely. The prior consolidation base near 53,000 gives a vertical-count target: if the base was, say, 10 columns wide, the horizontal count projects a target well above 55,500, giving an objective, pre-defined price objective for the swing.

The lesson: the *same* move is terrifying on candles, serene on a line, smoothly bullish on HA, cleanly trending on Renko, and quantitatively targeted on P&F. Each answered a different question.

## Trading it

Match the chart to the job, and combine them.

**Line chart — trade the macro and the levels.** Use weekly/daily line charts to identify the primary trend and the *cleanest* horizontal support/resistance (closing-basis levels are the most respected). Entry decisions are *not* made here, but the line chart vetoes trades against the settled trend and marks the key levels to watch.

**Candlesticks — trade the entry.** This is your execution chart. Enter on candlestick triggers at a level the higher-timeframe chart identified: a bullish engulfing or hammer at the 54,600 support in the Bank Nifty example. *Stop* below the low of the signal candle (a real, traded price). *Target* the next resistance from the line/P&F chart. Candles give the precise entry, real stop levels, and reversal patterns.

**Heikin-Ashi — ride the trend.** Use HA to *stay in* a winning trend and avoid premature exits during noise. Entry: first strong green HA candle (flat or no lower wick) after a pullback. Hold: as long as candles stay green with small/no lower wicks. Exit signal: first red HA candle with an upper wick, or a doji-like HA candle (indecision). Because HA lags, use it for trend *following/management*, not for pinpoint entries, and **always set actual stops from the underlying candlestick or structure**, never from HA's fabricated prices.

**Renko — filter chop and trail.** In a whippy market, switch to Renko to see only meaningful moves. Entry: on a brick colour change confirmed by trend context. Trailing: move your stop under the last two bricks; exit on an opposite-colour brick. Box size is the key dial — too small and chop returns, too large and lag becomes painful. Use ATR-based box sizing to adapt.

**Point & Figure — objective levels and targets.** Use P&F to pre-commit to *objective* support/resistance, trendlines (drawn at 45°), and — its unique value — *price targets* via the vertical/horizontal count, so you enter a swing already knowing your measured objective and can size the trade by its reward-to-risk before you click.

**Scenario stack (Bank Nifty up-swing):** line chart confirms the primary uptrend and marks 54,600 support → P&F gives a 56,000+ vertical-count target → candlestick prints a hammer at 54,600 → you enter on the hammer's close, stop below its 53,900 low, target 56,000 → you switch to Heikin-Ashi/Renko to *manage* the trade, holding while HA stays green and trailing under Renko bricks, exiting on the first red HA candle with an upper wick.

## Confluence

Chart types are not rivals — they are a *layered workflow*, and combining them with other tools multiplies edge:

- **Multi-chart-type stacking:** line for the macro trend and cleanest levels, candles for the entry trigger, HA/Renko for management. This top-down flow is itself a confluence engine.
- **Candles + structure/patterns:** candlesticks are the substrate for every reversal pattern (engulfing, pin bar, doji) and for reading BOS/CHoCH swing points — only candles show the wicks that mark true rejection at a level.
- **Renko/P&F + support-resistance & trendlines:** by stripping time, both produce *cleaner, more objective* horizontal levels and trendlines than a candle chart, where noise clutters the picture. A Renko brick base or a P&F double-top breakout is a high-conviction level.
- **P&F count + Fibonacci/measured moves:** cross-check a P&F vertical-count target against a Fibonacci extension or a chart-pattern measured move; when two independent methods point to the same price, the target is far more credible.
- **Line-chart divergence with option-chain/OI:** when the *closing-basis* line chart makes a new high but option-chain data shows heavy call writing at the strike above spot and futures long-unwinding, the clean line-chart breakout is suspect — the settled price says up, positioning says exhaustion.
- **Heikin-Ashi + momentum:** confirm HA colour with an oscillator (RSI/MACD) so you are not held in a fading trend by HA's lag alone.

The professional habit is to *default* to candlesticks for analysis and entries, and deliberately switch lenses — line to see trend clearly, HA/Renko to filter and manage, P&F to target — when the specific question demands it.

## Pitfalls & false signals

**Heikin-Ashi's fabricated prices — the most dangerous trap.** HA-Open and HA-Close are *averages*, not traded prices. Placing a stop or a limit at an HA level means placing it at a price the market never printed — you will be filled at a different real price, or your "level" will be meaningless. HA also *lags*: it shows the trend has turned only after real price has already moved, so it gives late entries and late exits. Use HA for *visual trend context and holding*, never for precise price decisions.

**Renko's lag and hidden information.** A Renko brick prints only after the full box move completes, so signals arrive late; and Renko hides *time* and every move smaller than the box — a two-day agonising consolidation looks identical to a five-minute one. A too-small box reintroduces the chop you switched to Renko to escape; a too-large box makes you dangerously late. Renko is also repaint-prone across platforms depending on whether it uses close-based or traditional bricks — know your platform's convention.

**Line charts hide intrabar risk.** The serene line that never broke trend can conceal a violent intraday stab (Bank Nifty's 700-point wick to 53,900) that would have blown a tight stop. Never size or place stops off a line chart; it shows the *settled* path, not the *risk* path.

**P&F and Renko discard time — bad for options.** Because both ignore time, they are ill-suited to any decision where *time decay* matters (options), where the *rate* of a move, not just its extent, is the whole game. Use time-based candles for options timing.

**Over-smoothing = false confidence.** HA and Renko *look* cleaner and more certain than reality is. The smoothness is a design choice, not a promise; a beautiful run of green HA candles can reverse violently on the next real bar. Do not let a tidy chart lull you into oversized positions or missing stops.

**Mismatching chart to task.** Using candlesticks to find the macro trend (too noisy), or a line chart to time an entry (no stop reference), or Renko for an options scalp (no time) — the errors all stem from ignoring what each type *discards*. The discipline is: name your question first, then pick the lens whose blindness is acceptable for that question.

## Interview-ready summary

Every chart is built from the same four numbers — open, high, low, close — and each type is a deliberate choice about what to keep and what to discard. A **line** chart plots only closes, discarding all intrabar detail to reveal the cleanest macro trend and the most-respected settled levels — great for the big picture, useless for stops because it hides intraday risk. **Bar and candlestick** charts keep the full OHLC; candlesticks encode it most legibly, with bodies showing who won the period and wicks showing rejected prices, which is why they are the substrate for entries and every reversal pattern. **Heikin-Ashi** replaces real OHLC with smoothed averages so trends render as long runs of same-colour, often wickless candles — excellent for *staying in* and filtering wobble, but its open and close are fabricated averages the market never traded, so I never set stops off it and I accept its lag. **Renko** abandons time, printing fixed-size bricks only on meaningful moves to strip out chop and produce obvious support/resistance — at the cost of lag and hidden detail, and it is poor for options because time and rate-of-move vanish. **Point & Figure** also ignores time, plotting X and O columns on a box grid to give the most objective support/resistance and trendlines, plus unique measured price targets via the vertical and horizontal counts. My workflow stacks them: line for trend and levels, P&F for objective targets, candlesticks for the entry trigger and real stops, and Heikin-Ashi or Renko to ride and trail — choosing each lens by naming the question first and knowing exactly what that lens is blind to.
