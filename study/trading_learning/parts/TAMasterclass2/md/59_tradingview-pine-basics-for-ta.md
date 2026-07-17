# TradingView Pine Script Basics for TA

## What it is & why it works

Pine Script is TradingView's built-in programming language for creating custom indicators, strategies, screeners and alerts. It is the bridge between "I have a trading idea" and "the chart automatically shows, tests and alerts me on that idea." For the technical trader it matters because it converts vague discretionary intuition into precise, testable, repeatable rules. The moment you can write "buy when the 20-EMA crosses above the 50-EMA on rising volume" in Pine, you can *see* it plotted on ten years of Nifty history, *backtest* whether it actually made money, and *get alerted* when it fires live — without watching the screen.

Why learn it rather than just using built-in indicators? Because your edge is usually a *combination* — a specific confluence no off-the-shelf indicator captures. Pine lets you encode exactly your setup: your EMA stack, your volume threshold, your RSI band, your session filter, your India-specific level logic. It removes emotion (the code fires the same way every time), removes manual errors, and lets you validate before risking capital. For an Indian trader on NSE/MCX, Pine works identically on Nifty, Bank Nifty, F&O stocks, USDINR and MCX contracts — one skill, the whole market.

This chapter is a working introduction: enough Pine (v5/v6 syntax) to write real indicators, a strategy you can backtest, and alerts you can trade from — grounded in Indian examples. It is not a substitute for the official reference, but it will get a technical trader productive.

## Mechanics — the anatomy of a Pine script

Open a TradingView chart, click **Pine Editor** at the bottom, and you get a blank script. Every indicator script has three parts.

**1. The version and declaration.**
```pine
//@version=6
indicator("My EMA Stack", overlay=true)
```
`//@version=6` pins the language version. `indicator()` declares this as a study; `overlay=true` plots it *on* the price chart (use `false` for a separate pane like RSI or MACD). For a backtestable system you write `strategy(...)` instead of `indicator(...)`.

**2. Inputs — your adjustable settings.**
```pine
fastLen = input.int(20, "Fast EMA")
slowLen = input.int(50, "Slow EMA")
volMult = input.float(1.5, "Volume multiple")
```
`input.*` creates the little gear-menu settings so you can tune the script without editing code. Always parameterise lengths and thresholds — it makes one script serve many instruments and timeframes.

**3. Calculation and plotting.**
```pine
fastEma = ta.ema(close, fastLen)
slowEma = ta.ema(close, slowLen)
plot(fastEma, "Fast", color.orange)
plot(slowEma, "Slow", color.blue)
```
`ta.ema()` is a built-in from the `ta` (technical analysis) namespace — Pine ships with `ta.ema`, `ta.sma`, `ta.rsi`, `ta.macd`, `ta.atr`, `ta.crossover`, `ta.crossunder`, `ta.highest`, `ta.lowest` and dozens more, so you rarely compute indicators by hand. `plot()` draws a line. `close`, `open`, `high`, `low`, `volume` are the built-in series for the current symbol.

**The execution model — this is the concept most beginners miss.** Pine runs your script once *per bar*, left to right across history and then on each new live bar. Variables like `close` mean "close of the bar currently being processed." To reference the previous bar you use the history-referencing operator: `close[1]` is the prior bar's close, `fastEma[1]` the prior bar's fast EMA. So a crossover is simply "fast is above slow now and was below or equal last bar" — which `ta.crossover(fastEma, slowEma)` handles for you, returning `true` on exactly the bar the cross happens.

## A complete, useful indicator (Indian example)

Here is a full script that marks EMA-crossover signals with a volume filter and colours the background — a real momentum tool you could run on Bank Nifty.

```pine
//@version=6
indicator("EMA Cross + Volume (BankNifty)", overlay=true)

fastLen = input.int(20, "Fast EMA")
slowLen = input.int(50, "Slow EMA")
volLen  = input.int(20, "Volume avg length")
volMult = input.float(1.5, "Volume multiple")

fastEma = ta.ema(close, fastLen)
slowEma = ta.ema(close, slowLen)
avgVol  = ta.sma(volume, volLen)

bullCross = ta.crossover(fastEma, slowEma)
bearCross = ta.crossunder(fastEma, slowEma)
volOk     = volume > volMult * avgVol

longSig  = bullCross and volOk
shortSig = bearCross and volOk

plot(fastEma, "Fast EMA", color.orange, 2)
plot(slowEma, "Slow EMA", color.blue, 2)

plotshape(longSig,  title="Long",  style=shape.triangleup,
          location=location.belowbar, color=color.green, size=size.small)
plotshape(shortSig, title="Short", style=shape.triangledown,
          location=location.abovebar, color=color.red, size=size.small)

bgcolor(longSig ? color.new(color.green, 85) :
        shortSig ? color.new(color.red, 85) : na)

alertcondition(longSig,  "Long signal",  "EMA bull cross + volume")
alertcondition(shortSig, "Short signal", "EMA bear cross + volume")
```

Everything a technical trader wants is here: parameterised inputs, `ta.*` calculations, a compound condition (`crossover AND volume`), visible triangle markers, a shaded background, and `alertcondition()` hooks so TradingView can ping your phone. Load it on a Bank Nifty 15-minute chart and it will mark every volume-confirmed EMA cross in history and alert on new ones live.

## Turning it into a backtestable strategy

Change `indicator` to `strategy` and add order calls, and TradingView's Strategy Tester will report the P&L, win rate, drawdown and profit factor across history.

```pine
//@version=6
strategy("EMA Cross Strategy", overlay=true,
         initial_capital=1000000, default_qty_type=strategy.percent_of_equity,
         default_qty_value=10, commission_type=strategy.commission.percent,
         commission_value=0.03)

fastLen = input.int(20, "Fast EMA")
slowLen = input.int(50, "Slow EMA")
atrLen  = input.int(14, "ATR length")
atrMult = input.float(2.0, "ATR stop multiple")

fastEma = ta.ema(close, fastLen)
slowEma = ta.ema(close, slowLen)
atr     = ta.atr(atrLen)

if ta.crossover(fastEma, slowEma)
    strategy.entry("Long", strategy.long)

if ta.crossunder(fastEma, slowEma)
    strategy.close("Long")

// ATR trailing stop
strategy.exit("Stop", "Long", stop = close - atrMult * atr)
```

Note the realistic touches for Indian conditions: `initial_capital=1000000` (₹10 lakh), `commission_value=0.03` percent to approximate brokerage plus a slice of STT/charges, `default_qty_type=strategy.percent_of_equity` so position size scales with the account, and an ATR-based exit so the stop adapts to Bank Nifty's volatility rather than a fixed point value. Run it, open the Strategy Tester tab, and read net profit, max drawdown, win rate and profit factor. Change the inputs, re-run, compare. This loop — hypothesise, code, backtest, refine — is the entire point of Pine for a serious technician.

## Worked India example (levels & ₹)

Load the strategy on daily Nifty over the last five years. Suppose (reconstruction — verify on your own chart and data) it shows: 42 trades, 48% win rate, profit factor 1.6, max drawdown 12%, net profit roughly 90% on ₹10 lakh. The equity curve is choppy in 2022's range and strong through 2023–24's trend — immediately telling you this is a *trend-following* system that pays in trends and bleeds small in ranges, exactly as EMA crosses should behave.

Now you experiment. Add a regime filter — only take longs when price is above the 200-day SMA:
```pine
trendUp = close > ta.sma(close, 200)
if ta.crossover(fastEma, slowEma) and trendUp
    strategy.entry("Long", strategy.long)
```
Re-run. Fewer trades (say 28), higher win rate (55%), shallower drawdown (8%). The 200-SMA filter removed the counter-trend crosses that were losing money in downtrends. This is Pine's real gift: you *measured* an intuition instead of guessing. You can see, in rupees and drawdown, that the trend filter improved the system — and you can now trade it with justified confidence.

## How to trade it (from script to execution)

1. **Prototype the idea** as an `indicator` with `plotshape` markers so you can eyeball whether the signals land where you'd expect on Nifty/Bank Nifty history.
2. **Convert to `strategy`** and backtest with realistic capital, commissions and an ATR stop. Read profit factor and drawdown, not just net profit.
3. **Refine with filters** (trend regime, session time, volume) and re-measure — keep changes that improve robustness, not just curve-fit the past.
4. **Deploy as alerts.** Right-click the chart → Add Alert → choose your `alertcondition` (or "Any alert() function call"), set it to notify your phone/webhook. Now the script watches the market and you execute manually on the ping — the sane middle ground between fully manual and fully automated.
5. **Forward-test on paper** for a few weeks before committing real capital; backtests are optimistic and Indian intraday data has quirks (gaps, expiry-day behaviour).

## Confluence (including OI)

Pine can pull *other* symbols with `request.security()`, which lets you build India-specific confluence directly into a script. Examples: overlay the India VIX on a Nifty chart and suppress long signals when VIX is spiking; pull the Bank Nifty/Nifty ratio to confirm financial leadership; or bring in a sector index to only trade stocks whose sector is trending. While TradingView does not natively serve NSE option-chain OI inside Pine, you can encode *volatility-regime* confluence (VIX via `request.security(\"NSE:INDIAVIX\", timeframe.period, close)`) and multi-timeframe confluence (compute the daily EMA trend and only take 15-minute longs that agree) — both hugely improve signal quality. A cross-checked script that requires the higher-timeframe trend *and* a supportive VIX regime before firing is dramatically cleaner than the raw crossover.

```pine
htfTrend = request.security(syminfo.tickerid, "D",
             ta.ema(close,50) > ta.ema(close,200))
vix = request.security("NSE:INDIAVIX", "D", close)
goodRegime = htfTrend and vix < 20
longSig := longSig and goodRegime
```

## Pitfalls

**Repainting.** The most notorious Pine trap. If you use `request.security()` on a higher timeframe without care, or reference the current (unclosed) bar, signals can *repaint* — appear and disappear as the bar forms, making backtests look far better than live reality. Rule: for reliable signals, act on *bar close* (`barstate.isconfirmed`) and use `request.security(..., lookahead=barmerge.lookahead_off)`. If a strategy's backtest looks too good, suspect repainting or lookahead bias first.

**Lookahead / future data.** Never write logic that peeks at future bars. Pine's `[1]` looks back, which is safe; certain constructions can accidentally use future information and produce fantasy backtests.

**Over-optimisation (curve-fitting).** Tuning inputs until the backtest is perfect produces a script that fits the past and fails the future. Prefer robust parameters that work across many settings and instruments over a single magic combination. Test on out-of-sample data.

**Ignoring costs.** A backtest without commissions and slippage will show profits that vanish live, especially for intraday systems with many trades. Always set `commission_value` and mentally add slippage — on Bank Nifty options and fast movers, slippage can exceed brokerage.

**Confusing indicator vs. strategy.** `indicator` scripts cannot place backtest orders; `strategy` scripts can. Beginners try to read P&L off an indicator — it isn't there. Use `strategy` when you want the Strategy Tester.

**Series vs. simple type errors.** Pine is typed; some built-ins need a `simple int` length, not a `series`. Beginners hit confusing errors here — read the error, and usually the fix is making the input a plain `input.int` rather than a computed series.

## Interview-ready summary

Pine Script is TradingView's language for turning a trading idea into a plotted, backtestable, alertable rule that runs identically across NSE, MCX and FX. Its value to a technician is precision and validation: you encode your exact confluence (EMA stack, volume threshold, RSI band, session filter) once, see it on years of Nifty history, measure whether it actually made money, and get alerted when it fires — removing selection bias and emotion. Every script has a version tag, an `indicator()` or `strategy()` declaration, `input.*` settings, `ta.*` calculations (`ta.ema`, `ta.rsi`, `ta.atr`, `ta.crossover`), and `plot`/`plotshape`/`alertcondition` outputs. The core mental model is that Pine runs once per bar left-to-right, with `close` meaning the current bar and `close[1]` the previous — so a crossover is just "above now, below last bar." To validate an idea you switch `indicator` to `strategy`, add realistic Indian settings (₹10 lakh capital, ~0.03% commission, ATR-based stops), and read profit factor and drawdown in the Strategy Tester — then improve it with measured filters like a 200-SMA trend regime or an India VIX cross-check via `request.security()`, keeping only changes that improve robustness rather than curve-fit the past. The deployment sweet spot is manual execution on `alertcondition` pings. The killer pitfalls are repainting and lookahead bias (act on confirmed bar close, `lookahead_off`), over-optimisation, and ignoring commissions and slippage — any of which makes a backtest lie. Learn Pine and you stop guessing whether your edge works; you measure it.
