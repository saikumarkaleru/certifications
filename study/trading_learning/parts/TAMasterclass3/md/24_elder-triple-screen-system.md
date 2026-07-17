# Elder Triple-Screen Trading System

Dr. Alexander Elder, a psychiatrist-turned-trader, published the Triple-Screen system in *Trading for a Living* (1993) and refined it in *The New Trading for a Living* (2014). It is not an indicator — it is a **method of combining timeframes and indicator types so their weaknesses cancel out.** That framing alone makes it worth a full chapter, because most Indian retail traders die from the exact disease Triple-Screen was engineered to cure: taking a trade signal on a single chart, on a single timeframe, with a single indicator, and then wondering why the "perfect" MACD crossover on the 5-minute chart failed inside twenty minutes.

This chapter treats Triple-Screen as a **named system** — origin, exact rules, an India worked example on Nifty and Bank Nifty, edge and cost notes, F&O adaptations, and the pitfalls that quietly break it.

## Origin & the core idea

Elder's insight is that every indicator lies in a specific way. **Trend-following indicators** (moving averages, MACD, Directional System) are right in trends and whipsaw brutally in ranges. **Oscillators** (Stochastic, Force Index, Williams %R, RSI) are right in ranges and give premature, repeated sell signals in a strong uptrend — the "overbought" reading that stays overbought for three weeks while price doubles. Use either one alone and half the market environment is your enemy.

Elder's fix borrows from the wave structure of markets across scales. He argued you should always look at **at least three timeframes**, each larger than the last by a factor of roughly **five**. If you like to trade off the hourly chart, your "middle" screen is the hourly, your "long" screen is the daily (roughly 5–7x), and your "short" screen is the 10-minute (roughly 5–6x). The genius is the division of labour:

- **Screen 1 (the tide) — the longer timeframe** decides the **direction** you are allowed to trade. Trend-following tool only. You never fight this.
- **Screen 2 (the wave) — the intermediate timeframe** uses an **oscillator** to find a counter-trend pullback *against* the tide. In an uptrend you wait for the oscillator to dip and give you a discount.
- **Screen 3 (the ripple) — the shorter timeframe** is the **trigger** for precise entry, typically a trailing buy-stop above the previous bar's high (in an uptrend) so price has to prove itself before you commit.

The metaphor Elder uses is the ocean: you find which way the tide is running, you wait for a wave moving against the tide to recede, and you enter on the ripple as the tide reasserts. You are buying pullbacks in uptrends and selling rallies in downtrends — but only pullbacks that occur *within* a confirmed larger trend. That is the whole system in one sentence.

## Exact rules

Elder deliberately left the specific indicators flexible, but he prescribed defaults. Here is a clean, tradable specification.

### Timeframe map

| Role | Screen | Purpose | Tool type | Elder default |
|---|---|---|---|---|
| Tide | Long (5x middle) | Direction filter | Trend-following | Weekly MACD-Histogram slope, or 13/26 EMA |
| Wave | Middle (your chart) | Timing the pullback | Oscillator | Force Index (2-period) or Stochastic |
| Ripple | Short (1/5 middle) | Entry trigger | Breakout stop | Buy-stop above prior bar high |

The "middle" screen is whatever your natural trading horizon is. A swing trader's middle screen is the **daily**; tide is **weekly**; ripple is the **hourly**. An intraday Bank Nifty trader's middle screen is the **15-minute**; tide is the **75-minute or hourly**; ripple is the **3- or 5-minute**.

### Screen 1 — the tide (direction)

Elder's original tool is the **Weekly MACD-Histogram**. The tradeable signal is not the absolute value but the **slope**: the histogram ticking *up* from one bar to the next = bullish tide (longs only); ticking *down* = bearish tide (shorts only). Slope, not zero-line, because slope turns earlier and keeps you aligned with momentum.

| Screen-1 reading | Permission |
|---|---|
| Weekly MACD-Histogram rising | Long trades only this week |
| Weekly MACD-Histogram falling | Short trades only this week |
| Flat / ambiguous | Stand aside |

Many traders substitute a simpler filter: price above a rising **26-week EMA** = uptrend. Both work; the MACD-Histogram slope is more sensitive and gives earlier turns at the cost of more flip-flops near ranges.

### Screen 2 — the wave (pullback)

On the middle timeframe, apply an oscillator and **look for the oscillator to move against the tide.** Elder's favourite is the **2-period Force Index** (Force Index = volume × (close − prior close), smoothed with a short EMA). Rules:

- Tide up → **buy when the middle-screen oscillator turns negative** (Force Index below zero, or Stochastic below 30, or 2-day EMA of Force Index dips). You are buying the dip *inside* the uptrend.
- Tide down → **sell when the oscillator turns positive** (Force Index above zero, or Stochastic above 70). You are shorting the bounce *inside* the downtrend.

This is the counter-intuitive heart of the system: **when the tide is up, oscillator weakness is a buy signal, not a sell signal.** The oscillator's job here is only to measure how far price has pulled back, giving you a better entry price and a tighter stop.

### Screen 3 — the ripple (trigger)

Do not enter at market when Screen 2 lights up. Instead place a **trailing buy-stop** (uptrend) one tick above the high of the current bar, trailed down each bar as long as the pullback continues. When price rallies and takes out a prior high, you are filled automatically — and if price keeps falling, you are never filled and you lose nothing. In a downtrend, mirror it: a **trailing sell-stop** one tick below the current bar's low.

The ripple screen enforces a rule most systems lack: **the market must move in your direction before you are allowed in.** You never catch the exact bottom, and you never need to.

### Stops and targets

| Element | Rule |
|---|---|
| Initial stop | Below the low of the pullback (long) / above the high of the bounce (short); Elder favours a stop below the most recent minor low |
| Trailing stop | Move to breakeven quickly; then trail under swing lows or a short EMA |
| Target | Often the prior swing high (long); or exit when Screen-2 oscillator reaches the opposite extreme |
| Position size | The **2% rule** — never risk more than 2% of account equity per trade; plus the **6% rule** — stop opening new trades for the month once total drawdown hits 6% |

Elder's money-management "iron rules" (2% and 6%) are not optional add-ons — he treats them as inseparable from the entry logic.

## Worked India example — swing long on Nifty 50

Assume it is a Tuesday in early 2026. Nifty 50 is trading around **24,000**. We are swing trading, so: **tide = weekly, wave = daily, ripple = 60-minute.**

**Screen 1 (weekly).** On the weekly Nifty chart the MACD-Histogram (12,26,9) printed a lower low three weeks ago and has now ticked *up* two weeks running. Price is holding above a rising 26-week EMA near 23,200. Tide reading: **up → longs only.** Good — we ignore every short setup this week.

**Screen 2 (daily).** Over the last four sessions Nifty slipped from 24,350 to 23,950 — a normal pullback. The daily 2-period Force Index has dropped **below zero** and the daily Stochastic %K is at **24**, below the 30 line. Both confirm the wave has receded against the tide. This is our buy zone. We are now hunting an entry, not a reason to be bearish about the four red daily candles.

**Screen 3 (60-minute).** Yesterday's most recent 60-minute bar had a high of **24,015**. We place a **buy-stop at 24,020**. We do not chase. If Nifty keeps sliding to 23,850, our stop is never triggered and we simply re-trail it lower next hour. This morning the index firms and at 11:15 trades through 24,020 — **we are filled long at 24,020.**

**Risk.** The pullback low was 23,940; the last minor swing low sits at 23,880. We place the stop at **23,860** (just under the swing low). Risk per unit = 24,020 − 23,860 = **160 points.**

**Sizing (2% rule).** Account = ₹10,00,000. Max risk = 2% = **₹20,000.** Nifty futures lot is 25. Risk per lot = 160 × 25 = **₹4,000.** Max lots = 20,000 / 4,000 = **5 lots.** We take 4 lots to keep a buffer and stay under the 6% monthly cap.

**Target/management.** The prior swing high is 24,350. As price clears 24,150 we trail the stop to breakeven (24,020). Nifty runs to **24,340** over the next two sessions where the daily Stochastic tags 82 (opposite extreme = Screen-2 exit). We close 4 lots near 24,320.

**P&L.** Gain ≈ 300 points × 25 × 4 lots = **₹30,000** gross, against ₹20,000 of defined risk — a reward:risk of roughly 1.9:1 on a trade where every screen agreed. Brokerage, STT on the sell side, exchange fees and GST on a 4-lot futures round-trip run roughly ₹800–1,200; slippage on the stop entry maybe 2–4 points. Net stays comfortably above ₹28,000.

Notice what the system *stopped* us from doing: it forbade the tempting short after four red daily candles, because the weekly tide was up. That single filter is where most of the edge lives.

## Intraday adaptation — Bank Nifty on the 15-minute

Bank Nifty is India's most-traded index for intraday and options. Map: **tide = 75-minute (or hourly), wave = 15-minute, ripple = 3-minute.**

- **75-min tide:** 13/26 EMA stack rising and MACD-Histogram slope up → longs only for the session.
- **15-min wave:** wait for a pullback where the 15-minute Stochastic dips under 30 or Force Index goes negative, ideally into a prior support or the rising 20-EMA around, say, **52,400.**
- **3-min ripple:** buy-stop above the last 3-minute swing high, e.g. **52,460**, stop under the pullback low **52,340** (120-point risk). Bank Nifty futures lot is 35, so risk/lot = 120 × 35 = ₹4,200; the 2% rule on a ₹5,00,000 intraday book (₹10,000) allows ~2 lots.

Because Bank Nifty is fast, the ripple trigger is doing heavy lifting: it keeps you out of the "falling knife" pullback that never turns.

## Backtest / edge notes & realistic costs

Triple-Screen has no single canonical backtest because the middle-screen oscillator and the exit are discretionary. But the structural edge is well-documented and intuitive:

- **The tide filter is the biggest contributor.** Studies of "trade only in the direction of the higher-timeframe trend" filters on Indian indices consistently improve win rate by roughly 8–15 percentage points versus taking every oscillator signal, mainly by deleting counter-trend losers.
- **The ripple stop-entry removes a chunk of failed pullbacks** at the cost of slightly worse entry prices — a favourable trade in liquid instruments, a poor one in illiquid mid-caps where the stop gaps.
- **Realistic frictions matter more than the signal.** On Nifty/Bank Nifty futures, per-round-trip cost (brokerage + STT + exchange + GST + stamp) plus 2–5 points of slippage is small relative to a 150–300 point swing, so the system survives costs. On stock options — especially weekly OTM Bank Nifty options — bid/ask spread and theta can eat the entire edge; there Triple-Screen must be applied to the *underlying* and expressed through appropriately-chosen strikes, not traded on the option's own chart.
- **Expectancy, not win rate, is the scorecard.** With a ~50–55% win rate and reward:risk near 1.7:1, expectancy is positive; the 2%/6% money rules are what convert positive expectancy into survivable equity curves through inevitable losing clusters.

Honest caveat: because two of the three screens involve judgement (which oscillator, how deep a pullback, when to exit), two disciplined traders will produce different results from "the same" system. Triple-Screen is a **framework that constrains discretion**, not a mechanical black box. Backtest results should therefore be treated as indicative of the *approach*, and each trader must forward-test their own concrete parameterisation on a demo/paper book before sizing up.

## F&O adaptations for NSE

- **Express the swing through options, size with the tide.** When the weekly tide is up and the daily wave gives a buy, buying a slightly ITM call or a bull call spread on Nifty/Bank Nifty captures the move with defined risk. Keep the 2% rule on the *premium at risk.*
- **Use OI as a fourth, confirming lens, never a screen.** If Screen-1 tide is up and the daily setup fires near a strike with heavy put writing (support), the confluence is stronger. But do not let OI override the tide.
- **Avoid Triple-Screen on the option chart itself.** Oscillators on an option's price are distorted by theta decay and IV shifts; always run all three screens on the underlying index/stock.
- **Respect event risk.** Suspend fresh entries into RBI policy, Union Budget, major results, and monthly F&O expiry — the tide can invert in one candle and the ripple trigger will fill you straight into a gap.

## Pitfalls

1. **Screen creep.** Adding a fourth and fifth indicator to each screen until nothing ever agrees. Elder's power is *one tool per screen.* More is worse.
2. **Fighting the tide because the oscillator "looks overbought."** In a strong uptrend the middle-screen oscillator will read overbought repeatedly; that is not a short signal, it is the tide doing its job. Shorts are forbidden while the tide is up. Full stop.
3. **Entering at market instead of on the ripple stop.** Skipping the trigger reintroduces the falling-knife risk the system was built to remove.
4. **Wrong timeframe ratio.** Using 5-min / 15-min / 30-min (ratios of only 2–3x) makes all three screens basically the same chart, so they always agree and the "confirmation" is illusory. Keep the ~5x spacing.
5. **Ignoring the 2% and 6% rules.** The entry logic can be perfect and you can still be wiped out by oversizing one trade or revenge-trading through a 6% monthly hole. The money rules are load-bearing.
6. **Applying it to illiquid stocks.** Stop-entries and swing-low stops assume you can get filled near your price; in thin NSE mid/small-caps, gaps make both meaningless.

## Interview-ready summary

Triple-Screen is Alexander Elder's multi-timeframe method that assigns each of three timeframes (spaced ~5x apart) a distinct job: the **long timeframe sets the tradeable direction** using a trend-following tool (weekly MACD-Histogram slope), the **middle timeframe times a pullback** against that trend using an oscillator, and the **short timeframe triggers entry** via a trailing stop so the market must move your way before you commit. You only ever buy dips in uptrends and sell rallies in downtrends — never against the tide. Risk is capped by the 2%-per-trade and 6%-per-month rules. On Nifty, that means: weekly up → wait for a daily Stochastic/Force-Index dip → buy-stop above the prior hourly high, stop under the swing low, target the prior swing high or the opposite oscillator extreme. Its edge comes overwhelmingly from the direction filter deleting counter-trend losers; its main failure modes are fighting the tide on "overbought" readings, collapsing the timeframe spacing, and abandoning the money-management rules.
