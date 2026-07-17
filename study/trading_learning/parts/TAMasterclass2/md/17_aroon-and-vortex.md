# Aroon & Vortex Indicators

Most traders' toolkits stop at moving averages, RSI and MACD. That is fine — those three carry a lot of weight — but they share a blind spot. They tell you whether price is going up or down; they are slower to tell you whether price is *trending at all*. A stock can chop sideways for six weeks with a rising 20-EMA and a mid-range RSI, and you will keep taking losing breakout trades because nothing in your dashboard is screaming "there is no trend here yet." The Aroon and Vortex indicators are built precisely for that gap. Both are **trend-detection and trend-strength** tools rather than pure momentum oscillators, and both were designed to answer two questions that MACD answers badly: *Is a new trend starting?* and *Has the existing trend flipped?*

This chapter treats them together because Indian intraday and swing traders on Nifty, Bank Nifty and single stocks tend to use them as a pair — Aroon to spot the *birth* of a trend and confirm consolidations, Vortex to confirm and time *directional crossovers*. Neither is a holy grail. Used naively they whipsaw as badly as any indicator. Used with structure and, where relevant, option-chain confluence, they earn their place.

## Aroon: what it is and why it works

Aroon was created by Tushar Chande in 1995 (the same mind behind the Chande Momentum Oscillator). The name comes from a Sanskrit word meaning "dawn's early light" — the idea being that Aroon spots the *dawn of a new trend* before it is obvious on price.

The core insight is simple and, once you see it, obvious: **in a strong uptrend, new highs keep getting made recently; in a strong downtrend, new lows keep getting made recently.** So instead of measuring the *size* of price moves (which is what momentum indicators do), Aroon measures *how long it has been since the highest high and the lowest low* within a lookback window. Time, not price magnitude, is the input. That makes Aroon unusually good at one specific job — telling you when a market has *stopped* trending and gone to sleep, because in a range neither a fresh high nor a fresh low has happened recently.

There are two lines:

- **Aroon Up** = 100 × (period − bars since highest high) / period
- **Aroon Down** = 100 × (period − bars since lowest low) / period

The default period is **25**. Both lines oscillate between 0 and 100.

If the highest high in the last 25 bars occurred *today* (0 bars ago), Aroon Up = 100 × 25/25 = 100. If the highest high was 25 bars ago, Aroon Up = 0. Same logic mirrored for Aroon Down using lowest lows. So a fresh high pins Aroon Up at 100, and every bar that passes without a new high drags it down in steps of 4 (for period 25, each bar is 100/25 = 4 points).

### Reading the lines

- **Aroon Up above 70 and Aroon Down below 30** → healthy uptrend; fresh highs are recent, fresh lows are stale.
- **Aroon Down above 70 and Aroon Up below 30** → healthy downtrend.
- **Both lines below 50, tangled together** → no trend, consolidation. This is the reading no other popular indicator gives you as cleanly.
- **Crossovers** — Aroon Up crossing above Aroon Down signals a possible shift to bullish; the reverse for bearish.
- **Both lines high (both near 100)** happens briefly at inflection points where both a recent high and a recent low sit inside the window — usually a volatile, indecisive patch.

Some platforms also plot the **Aroon Oscillator** = Aroon Up − Aroon Down, a single line swinging between −100 and +100. Above zero = bullish bias, below zero = bearish, and the distance from zero is trend strength. On TradingView the two-line version is the default; Chartink screeners more often use the oscillator form.

## Aroon: settings for Indian timeframes

The default 25 is calibrated to daily charts and works well for Nifty and liquid large-caps on the daily. For other contexts:

- **Positional/daily swing (Nifty, Bank Nifty, large-caps):** 25 is the standard. Some traders shorten to 14 for faster signals on trending stocks, accepting more whipsaw.
- **Intraday 15-minute (Bank Nifty, Nifty futures):** 14 to 18 is common. On a 15-min chart, 25 bars is over six hours — nearly the whole session — so a shorter window keeps the indicator responsive within the day.
- **Intraday 5-minute (scalping index options):** 14, sometimes 9, for very fast reads, but expect noise; use only with strong structure.
- **Weekly (long-term stock investing overlay):** 25 weeks captures the primary trend well.

A practical rule: **the shorter the period, the more often Aroon pins to 100 and 0**, which means more crossovers and more false starts. Longer periods give fewer, higher-quality signals but arrive late. For most Indian swing traders, daily-25 or 15min-14 are the two workhorses.

## Aroon: worked India example (₹ and levels)

Consider a reconstruction on **TATAMOTORS** on the daily chart. Suppose the stock spent several weeks ranging between roughly ₹920 and ₹960 — a tight consolidation. During this phase, both Aroon Up and Aroon Down sat below 50, criss-crossing each other around the 30–45 zone. That is the "market asleep" signature. A momentum trader looking at RSI hovering near 50 would get the same message but less crisply; Aroon's tangled sub-50 lines make the *absence of trend* visually unambiguous, which is the whole point.

Now suppose price pushes to a fresh 25-day high at ₹968. On that bar, Aroon Up jumps to 100 (new high today). Over the next three sessions price follows through to ₹985, ₹998, ₹1,012. Because each of those is a new high, Aroon Up stays pinned at or near 100, while Aroon Down — no new low for many bars — decays toward 8 or 4. Aroon Up above 70 with Aroon Down below 30 is now flashing a confirmed uptrend. The Aroon Oscillator has swung from near zero to about +90.

The trade logic: the *breakout bar* at ₹968 with Aroon Up hitting 100 while Aroon Down collapses is your trend-birth signal. Entry on a retest of the ₹960–968 breakout zone; stop below the consolidation low near ₹918; first target the measured move (range height ₹40 projected up → ₹1,000–1,008 area), trailing thereafter as long as Aroon Up holds above 70.

The exit signal that Aroon gives beautifully: when Aroon Up finally drops below 70 *and* Aroon Down climbs back above 30 — meaning fresh highs have stopped and a recent low has appeared — the trend is losing its grip. If on a later session price fails to make new highs for 7–8 bars and Aroon Down crosses above Aroon Up around ₹1,040, that crossover is your "trend is over, book or tighten" alert.

## Vortex Indicator: what it is and why it works

The Vortex Indicator (VI) was published by Etienne Botes and Douglas Siepman in *Technical Analysis of Stocks & Commodities* in 2010 — a relatively modern tool. Its inspiration is genuinely physical: the way water forms vortices, with upward and downward rotational motion. Botes and Siepman translated that into two oscillating lines that capture the tug-of-war between upward and downward price movement.

The construction rests on two measures of directional movement between consecutive bars:

- **VM+ (positive vortex movement)** = |Current High − Previous Low|. This captures the distance of the *upward* thrust — how far today's high is from yesterday's low.
- **VM− (negative vortex movement)** = |Current Low − Previous High|. This captures the *downward* thrust — how far today's low is from yesterday's high.

Both are summed over a lookback period (default **14**), then each is normalised by the sum of the **True Range** over the same period:

- **VI+ = (Σ VM+ over n) / (Σ True Range over n)**
- **VI− = (Σ VM− over n) / (Σ True Range over n)**

The two lines, VI+ and VI−, oscillate around 1.0 (or around 100 if scaled). When VI+ is above VI−, upward movement dominates — bullish. When VI− is above VI+, downward movement dominates — bearish. **The crossover of VI+ and VI− is the primary signal.**

Why does it work? Because it directly compares the range of up-moves against the range of down-moves, normalised by volatility. In a genuine uptrend, highs get made far above prior lows (big VM+), while down-thrusts are shallow (small VM−). VI+ pulls decisively above VI−. It is, in spirit, a cousin of Wilder's DMI/ADX (the +DI/−DI lines), but built differently and often quicker to cross at genuine turns. Many traders find the VI crossover cleaner and less laggy than the +DI/−DI cross for catching the *start* of a new leg.

## Vortex: settings and behaviour

The default period is **14**. As with Aroon:

- **Daily swing:** 14 is standard; some lengthen to 21 for fewer whipsaws on choppy stocks.
- **Intraday index/futures (15-min):** 14 works; 10–13 for faster crossovers when scalping Bank Nifty.
- **The wider the gap between VI+ and VI−, the stronger the trend.** Lines converging toward 1.0 and tangling = weakening trend or range — the same "no-trend" warning Aroon gives, expressed differently.

A useful nuance: VI+ spiking sharply above 1.10–1.15 while VI− drops below 0.85 often marks a *powerful* impulse leg (think a gap-up trending day on Bank Nifty). Extreme readings can precede exhaustion, so treat very wide separations as "strong but watch for a mean-reversion pause," not "add blindly."

## Vortex: worked India example (₹ and levels)

Take a reconstruction on **BANKNIFTY futures**, 15-minute chart, on a trending session. Suppose the index opens soft and drifts, with VI− above VI+ through the first hour — bearish control, price sliding from 48,500 toward 48,200. Around 10:45, buyers step in on a hammer near 48,180. Over the next two 15-min candles, highs push well above the prior lows (large VM+), True Range stays moderate, and **VI+ crosses above VI− around 48,260**.

That crossover is the entry trigger for a long. Entry ~48,270; stop below the 48,180 swing low (about 90 points — on Bank Nifty futures, sizeable, so options or reduced lots are wiser); target the prior day's VWAP/resistance cluster near 48,550. As the up-leg develops, VI+ widens to ~1.12 while VI− sinks to ~0.86, confirming trend strength; you trail the stop under successive 15-min swing lows. When price stalls near 48,540 and VI+ and VI− begin converging back toward 1.0, the impulse is fading — time to book or tighten hard. A later VI− cross back above VI+ near 48,500 would be the "trend over" flag.

For an **options overlay** on the same move: the VI+ crossover coinciding with a bullish trend is when you would prefer buying an ATM/slightly-ITM call or selling a put spread — directional exposure justified because the indicator says a real up-leg (not chop) is underway. If instead VI+ and VI− were tangled around 1.0, you would *avoid* directional option buying (theta bleed in a range) and prefer non-directional structures.

## How to trade them: combining Aroon and Vortex

The two tools are complementary rather than redundant:

- **Aroon** is superior at flagging *consolidation and the birth of a trend* (its time-based logic pins to extremes at fresh highs/lows).
- **Vortex** is superior at *timing the directional crossover* and confirming which side has control.

A robust workflow:

1. **Filter with Aroon.** Only look for directional trades when Aroon confirms a trend exists — Aroon Up > 70 with Aroon Down < 30 for longs (or the mirror for shorts). If both lines are tangled below 50, stand aside; the market is ranging and both indicators will whipsaw.
2. **Time with Vortex.** Within an Aroon-confirmed trend, use a VI+ / VI− crossover in the trend's direction as the entry trigger, ideally on a pullback rather than at a stretched extreme.
3. **Confirm with structure.** Both fire best at a broken level, a trendline retest, or a support/resistance flip — never in a vacuum.

### Setup table

| Setup | Trigger | Stop | Target | Timeframe | Best regime |
|---|---|---|---|---|---|
| Aroon trend-birth long | Aroon Up hits 100 on a fresh-high breakout bar; Aroon Down < 30 | Below consolidation low | Measured move (range height) | Daily / 15-min | End of a clean range |
| Vortex crossover long | VI+ crosses above VI− with prior Aroon uptrend confirmation | Below trigger-bar / recent swing low | Prior resistance / VWAP cluster | 15-min intraday | Trending session |
| Aroon+Vortex combo long | Aroon Up>70, Aroon Down<30, AND VI+>VI− on a pullback | Below pullback swing low | Trail under swing lows until Aroon Up<70 | Daily swing | Established uptrend |
| Range-avoidance filter | Both Aroon lines <50 tangled OR VI+/VI− pinned at 1.0 | — (no trade) | — | Any | Choppy/sideways — SIT OUT |
| Aroon trend-death exit | Aroon Up drops <70 and Aroon Down climbs >30 (or VI− crosses VI+) | — | Book / tighten | Any | Trend maturing |

## Confluence — including option-chain

- **With ADX/DMI:** Aroon and Vortex both answer "is there a trend," as does ADX. If ADX is rising above 25 *and* Aroon confirms *and* VI+ leads VI−, you have three independent votes for a real trend — a high-conviction directional setup.
- **With moving averages:** A VI+ crossover above a rising 20-EMA, with Aroon Up>70, is far stronger than the crossover alone.
- **With volume:** A fresh-high Aroon breakout on above-average volume (say 1.5× the 20-day average) is the difference between a real breakout and a fake-out.
- **With option-chain / OI (index & F&O stocks):** When Aroon/Vortex flip bullish and, simultaneously, the option chain shows **call writers being squeezed** — call OI at the nearest resistance strike *unwinding* while puts add OI at lower strikes (support building) — the technical and positioning signals agree, and continuation odds improve. Conversely, if VI+ crosses up but heavy call OI is *still stacking* just overhead (a wall of resistance), the breakout may stall; demand extra confirmation. **PCR turning up** alongside a Vortex bullish crossover is a supportive confluence for index longs.
- **With VWAP intraday:** A VI+ crossover *above* VWAP on Bank Nifty is a much cleaner long than a crossover below VWAP (where you are fighting the day's mean).

## Pitfalls

1. **Whipsaws in ranges — the number-one killer.** Both indicators generate frequent, false crossovers when price is sideways. This is not a flaw to be fixed but a regime to be avoided: use the Aroon-tangle / VI-convergence reading as a *do-not-trade* signal, not as a reason to keep flipping positions.
2. **Aroon pinning at 100 is not "buy now."** Aroon Up hitting 100 just means a fresh high happened; in a choppy stock it hits 100 repeatedly at range tops right before reversals. Require the *pairing* — Up high AND Down low — plus structure.
3. **Lag at reversals.** Because Aroon uses a lookback of past highs/lows, at a sharp V-reversal it can stay bullish for several bars after price has topped. Vortex crosses faster but then generates more false crosses. Neither is a leading oracle.
4. **Extreme Vortex separation ≠ add forever.** Very wide VI+/VI− gaps mark strong but often *late-stage* moves; chasing there invites buying the top of an impulse leg.
5. **Wrong period for the timeframe.** Running default-25 Aroon on a 5-min chart makes it glacially slow (25 bars ≈ two hours); running period-9 on a daily makes it hyperactive. Match the period to the horizon.
6. **Treating them as standalone systems.** Backtests of raw Aroon or raw Vortex crossovers on Nifty stocks typically show mediocre edge alone; the edge appears when they are used as *filters and timers* inside a structure-based plan.

## Interview-ready summary

**Aroon** (Chande, 1995; default 25) measures *how recently* the highest high and lowest low occurred within a lookback, giving two lines (Aroon Up, Aroon Down) from 0–100. Fresh highs pin Aroon Up to 100; its unique strength is cleanly flagging *consolidation* (both lines tangled below 50) and the *birth of a new trend* (one line to 100, the other collapsing). **Vortex** (Botes & Siepman, 2010; default 14) compares the range of upward thrusts (VM+ = |High − prior Low|) against downward thrusts (VM− = |Low − prior High|), each normalised by True Range, producing VI+ and VI− lines whose crossover signals directional shifts — a faster-turning cousin of DMI. Use Aroon to confirm a trend *exists*, Vortex to *time* the entry crossover, and always demand structural confluence (broken levels, volume, and for index/F&O trades, agreeing OI/PCR). Both are trend/strength tools, not momentum oscillators; their fatal weakness is whipsaw in ranges, which is precisely the regime their own "tangled lines" reading tells you to sit out. Honest edge comes from using them as filters and timers within a plan, not as standalone buy/sell machines.
