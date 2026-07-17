# Three-Line-Break Charts

## What it is and the logic

A Three-Line-Break chart (TLB, also called *sanju ashi* or "three-step new price line" in its native Japanese) is a price-driven, time-independent charting method built entirely from small coloured bricks, or *lines*. Each brick is drawn only when price achieves something meaningful: it either extends the current trend by making a new high (or low) beyond the previous brick, or it reverses the trend — but reversing requires overcoming *three* prior bricks, not just one. That single asymmetry — trends extend cheaply, reversals must earn it — is the whole philosophy. It builds a natural lag into reversals so that you are not shaken out of a good trend by the first pullback, while letting genuine trend continuation add bricks freely.

Like Kagi and Renko, TLB throws away the horizontal time axis. A brick appears when price does the required work and at no other time; a two-week consolidation inside the range produces *zero* bricks, while a sharp trending session might print several. What survives on the chart is only price movement that mattered, colour-coded by direction — white/green for up-bricks, black/red for down-bricks in the classic scheme.

The "three" in Three-Line-Break is a parameter, not a law. You can build a One-Line-Break (hyper-sensitive, flips on any new-direction close), a Two-Line-Break, a Five-Line-Break (very slow, for long-horizon investors) and so on. Three is the traditional default because, empirically in the old Japanese rice and later stock markets, requiring price to exceed the extreme of the last three bricks filtered ordinary noise while still catching real turns reasonably early. Steve Nison popularised it in the West alongside Kagi and Renko as the three "non-time" chart families.

The mental model that makes TLB click: imagine the trend has been climbing and has printed a run of white bricks. A reversal brick (black) is only allowed to appear if price closes below the *low of the last three white bricks*. So the market must not merely dip — it must undo three bricks' worth of progress before TLB will admit the trend has turned. That is a deliberately high bar, and it is why TLB reversals, when they finally come, tend to be trustworthy.

## Construction, rules and settings

TLB is built on **closing prices** (this is standard and important — it is what gives TLB its noise immunity). The algorithm, run at each close:

| Situation | Rule |
|-----------|------|
| First brick | Compare first two closes; draw a white up-brick or black down-brick accordingly. |
| Continuation (up) | If today's close > the **top** of the last up-brick, draw a new white up-brick to the new close. |
| Continuation (down) | If today's close < the **bottom** of the last down-brick, draw a new black down-brick. |
| Reversal from up to down | If today's close < the **low of the last three up-bricks**, draw a black down-brick (the reversal brick). |
| Reversal from down to up | If today's close > the **high of the last three down-bricks**, draw a white up-brick. |
| Nothing qualifies | No brick is drawn. Time passes on the real calendar; the chart does not move. |

The "last three" is the *line-break* number. Two clarifications that trip people up:

1. Early in a new trend there may be fewer than three same-colour bricks. If only one or two bricks exist since the last reversal, the reversal rule uses however many exist (you cannot break three bricks that aren't there). So very early reversals are actually *easier*, which is why fresh trends can whip once or twice before settling.
2. Continuation only needs price to beat the *single* most recent brick's extreme, not three. Extension is cheap; reversal is expensive. Remember the asymmetry.

The core mechanical signals:

- **Buy** = the appearance of a white reversal brick (trend flips from down to up).
- **Sell / go short / exit long** = the appearance of a black reversal brick (trend flips from up to down).

There is essentially nothing else to the base system — it is even simpler than Kagi because there is no thickness dimension; direction *is* the signal.

**Settings.** The one meaningful parameter is the line-break number. There is a secondary implicit parameter — the **timeframe of the closes** you feed it (daily, weekly, hourly), which matters enormously because TLB has no internal size gate the way Renko does. TLB bricks are as big as price movements happen to be; feeding it 5-minute closes on Bank Nifty produces a very different, far busier chart than daily closes.

| Line-break setting | Behaviour | Suits |
|--------------------|-----------|-------|
| 1-line-break | Flips on any new-direction close | Scalpers, very active; noisy |
| 2-line-break | Moderately sensitive | Short-term swing |
| **3-line-break** | Classic balance | Positional swing trading (default) |
| 4/5-line-break | Slow, high-conviction reversals only | Long-term investors, weekly charts |

For Indian markets in 2026 the sober defaults are: **3-line-break on daily closes** for swing trading Nifty/Bank Nifty/liquid stocks, and **3-line-break on weekly closes** for positional investing. Intraday TLB (3-line on 15-min) is usable on index futures but expect more whipsaw.

## Worked India example (levels and ₹)

Take **HDFC Bank** on the daily chart, 3-line-break on closes, through a realistic 2026 sequence. Assume a prior downtrend has printed black bricks and the last few down-bricks sit at closes of **₹1,655, ₹1,642 and ₹1,628** (three consecutive down-bricks). The reversal-up rule now requires a close **above the high of the last three down-bricks = ₹1,655**.

- Price closes **₹1,648** — inside the range, below ₹1,655, and not below ₹1,628 either. **No brick.** The chart is silent even though a day passed.
- Next close **₹1,662** — above ₹1,655, the three-brick high. A **white reversal brick is drawn.** *Buy signal.* Long entered near ₹1,662. The top of this new up-brick is ₹1,662.
- Close **₹1,689** — above ₹1,662, so a second white up-brick prints to ₹1,689. Trend confirming.
- Close **₹1,681** — below ₹1,689 (no continuation) but above the three-up-brick low, which is now ₹1,628 (bricks at 1662, 1689, plus we still count back). No reversal, **no brick.** The pullback is absorbed silently.
- Close **₹1,712** — new high beyond ₹1,689, third white brick to ₹1,712.
- Trend extends: closes of **₹1,748, ₹1,795, ₹1,840** each print fresh white bricks. Now the last three up-bricks top out at 1748/1795/1840, and their **low is ₹1,748**.
- Price rolls over. Close **₹1,762** — above ₹1,748, no reversal, no brick. Close **₹1,731** — below the three-up-brick low of ₹1,748. A **black reversal brick prints.** *Exit long / sell signal.* Position closed near ₹1,731.

Trade result: long ~₹1,662, exit ~₹1,731 → **+₹69 (~4.2%)** captured on a ~₹190 up-move from base to peak (₹1,628→₹1,840). As with every reversal-threshold method, TLB surrendered the final ₹109 (1,840→1,731) — the structural cost of demanding three bricks be broken before admitting the turn. In exchange, it never once flinched during the two intraday-scale pullbacks that on a candlestick chart would have looked like potential tops.

For **Nifty futures**, a 3-line-break on weekly closes across a trending year would typically print a long, uninterrupted run of white bricks, keeping a positional trader in the entire move and flipping black only when weekly closes finally broke three bricks down — usually within a few percent of the actual top. That is exactly the trade-off positional traders want: give up the last few percent in return for never being shaken out of the middle 80%.

## How to trade it: entry, stop, target, management

**Entry.** Take the reversal-brick signal on the close that produces it, or the next open. A white reversal brick after a downtrend is your long; a black reversal brick after an uptrend is your short (or long exit). Never front-run the brick — a close that *almost* breaks three bricks has broken nothing.

**Stop.** TLB gives a clean structural stop: the **extreme of the reversal brick's opposing swing**. For the HDFC long entered on the white reversal brick at ₹1,662, the natural invalidation is a black reversal brick — which would require a close below the last three up-bricks' low. Early in the trade that low is near ₹1,628, so initial risk ≈ ₹34 (2%). You can either wait for the full black reversal brick (structural stop) or place a hard stop just below ₹1,628 to cap gap risk.

**Target.** TLB is a pure trend follower; the honest default is *no target — ride to the opposite reversal brick*. If a rulebook needs targets, project measured moves from the reversal-brick base or take partial profits at prior swing highs and trail the balance. Because bricks cluster at real swing points, Fibonacci extensions and prior-swing resistance overlay naturally.

**Management.** Professional refinements:

1. **Colour-run filter.** Require at least *two* same-colour bricks after a reversal before deploying full size — a lone reversal brick that immediately reverses again is the classic TLB whipsaw, most common in ranges and around Nifty expiry.
2. **Multi-timeframe stack.** Weekly TLB sets the regime (white = longs only); daily TLB times entries. Only take daily white reversal bricks while the weekly chart is white.
3. **Pyramiding on continuation.** Add a unit on each fresh continuation brick, trailing the stop up to the low of the last three bricks as the trend matures.
4. **Watch brick *size*.** Because TLB has no fixed brick size, a suddenly enormous brick (a gap or news candle) is information — often a climax. Large late-trend bricks warn of exhaustion; tighten stops.

## Confluence

TLB carries only direction, so pair it with orthogonal signals:

- **Volume / delivery %.** A white reversal brick on strong NSE delivery volume is far more reliable than one on thin turnover.
- **Option chain / OI.** On index instruments, a black reversal brick coinciding with fresh put-writer capitulation (put OI unwinding below spot) strongly corroborates a top. TLB says structure turned; OI says the option sellers agree.
- **Higher-timeframe TLB.** The weekly-white + daily-reversal-brick stack is the core confluence.
- **Trendlines and moving averages.** A reversal brick that coincides with a break of a well-respected trendline or the 50-DMA is higher conviction than a naked brick.
- **Round numbers.** A reversal brick forming at Nifty 24,000 or Bank Nifty 50,000 marries structure to psychology.

As with all price-derived tools, do *not* stack multiple momentum oscillators on TLB — they read the same closes and merely echo the chart. Confluence must come from something TLB cannot see: volume, open interest, breadth.

## Pitfalls

**1. Whipsaws in ranges.** TLB's entire edge is trend capture; in a sideways market it prints a lone reversal brick, you enter, it flips back, and you lose the spread plus costs — repeatedly. Because early trends have fewer than three bricks to break, reversals near a range are *easier* and thus more prone to false flips. Use a regime filter; stand aside in confirmed ranges.

**2. No time axis — same trap as Kagi.** Distance along the chart is not elapsed time. A flat stretch can hide a month of consolidation. Do not read brick count as duration.

**3. Timeframe sensitivity.** Because TLB has no internal size gate, the choice of close-timeframe *is* the volatility setting. The same 3-line-break looks utterly different on 5-min vs daily closes. Pick the timeframe deliberately to match your holding period and keep it fixed between backtest and live trading.

**4. Gap risk on single stocks.** An overnight results gap can leap past three bricks in one close, producing a reversal brick far from your intended stop. Size for gaps on stocks; index futures are milder but not immune.

**5. Surrendered final leg.** By design, TLB always gives back the last portion of a move (the three bricks it needed to see broken). Traders who expect it to nail tops and bottoms will be perpetually disappointed and tempted to front-run the brick — which destroys the method. Accept the give-back as the price of reliability.

**6. Line-break number over-fitting.** Sliding the line-break number until last year looks perfect produces a setting that fails next year. Choose from the small standard menu (2/3/4) based on your horizon, not from an optimiser.

**7. Costs on frequent flips.** On shorter timeframes TLB flips often; brokerage, STT, exchange charges and slippage on Indian instruments quietly erode the edge. Always backtest with realistic all-in costs; a system that looks great gross can be negative net.

## Interview-ready summary

A Three-Line-Break chart is a time-independent, close-based Japanese charting method built from coloured bricks. Continuation is cheap — a single new closing high/low beyond the last brick adds a same-colour brick — but reversal is expensive: price must close beyond the extreme of the **last three bricks** before an opposite-colour reversal brick appears. This deliberate asymmetry filters noise and keeps you in trends, at the cost of entering late and surrendering the final leg. The core signals are the **white reversal brick (buy)** and **black reversal brick (sell/exit)**, with a natural structural stop at the opposing three-brick extreme. It suits positional and swing trading on Nifty, Bank Nifty and liquid NSE stocks — 3-line-break on daily closes for swings, on weekly closes for investing — and it demands a regime filter to survive ranges, plus honest transaction costs. Confluence should come from volume and option-chain OI, not from more oscillators. The one-line essence: *trends earn bricks easily, but a reversal must break three bricks to prove itself — so when TLB finally changes colour, it usually means something.*
