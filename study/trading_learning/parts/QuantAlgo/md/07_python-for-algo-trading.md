# Python for Algo Trading

## Why this matters

The gap between a retail "backtest" in TradingView's strategy tester and a professional research workflow is enormous, and it is mostly about *reproducibility and honesty*. TradingView hides your assumptions; a Python notebook forces you to state every one — data source, costs, slippage, lookahead — in code you can re-run and audit. Pros don't trust a strategy they can't reproduce from raw OHLC to equity curve on their own machine. Python is the lingua franca because pandas makes OHLC manipulation trivial, the ecosystem (yfinance, nsepy, broker SDKs, backtesting.py, vectorbt) is free, and vectorised code lets you test 20 years of Nifty in milliseconds. This chapter is about building a *minimal, reproducible* research loop: get data, compute a signal, backtest it with realistic Indian costs, and plot the equity curve — the skeleton every serious system starts from. (Live execution and SEBI's algo rules are the next chapter; this one stays in research.)

## The essentials

**Data sources (India).**

| Source | Gets you | Notes |
|---|---|---|
| `yfinance` | Free daily OHLC; `^NSEI` (Nifty), `^NSEBANK` (Bank Nifty), `RELIANCE.NS` | Great for research; adjust for splits; not tick data |
| `nsepy` / `jugaad-data` | NSE historical, indices, F&O | Community-maintained; NSE changes break them — pin versions |
| Broker historical API | Zerodha Kite, Upstox intraday/minute candles | Auth required; rate-limited; the real source for live systems |

**The stack.** `pandas` for the OHLC DataFrame (a DatetimeIndex plus Open/High/Low/Close/Volume). Compute indicators as vectorised column operations (`.rolling()`, `.ewm()`, `.pct_change()`) — no Python loops. Backtest with either `backtesting.py` (event-driven, readable, easy costs) or `vectorbt` (fully vectorised, blazing fast for parameter sweeps). Plot the equity curve with `matplotlib`.

**Costs must be modelled.** A backtest without Indian costs is a lie. Bake in STT (from 01-Apr-2026: equity intraday 0.025% on sell, futures ~0.05% on sell), brokerage (~₹20/order), exchange txn, 18% GST on brokerage+txn, stamp duty, plus **slippage** (assume you don't get the close). In `backtesting.py`, `commission=` covers a percentage; add a slippage buffer yourself.

**The cardinal sin: lookahead bias.** Compute a signal on bar *t*, act on bar *t+1*'s open. If you compute an indicator using today's close and also "buy at today's close," you've peeked. Shift signals by one bar.

*Library behaviour and NSE data endpoints as of July 2026 — pin package versions and re-verify; free data sources break often.*

## Worked example

A minimal, reproducible SMA-crossover backtest on Nifty daily, with costs. Run in a fresh venv: `pip install yfinance backtesting pandas matplotlib`.

```python
# nifty_sma_backtest.py  — reproducible research skeleton (July 2026)
import yfinance as yf
import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

# 1. DATA: Nifty 50 daily OHLC
data = yf.download("^NSEI", start="2015-01-01", end="2026-06-30",
                   auto_adjust=True, progress=False)
data = data[["Open", "High", "Low", "Close", "Volume"]].dropna()

# 2. INDICATOR helper (vectorised)
def SMA(series, n):
    return pd.Series(series).rolling(n).mean()

# 3. STRATEGY: long-only 50/200 SMA cross (trend-following)
class SmaCross(Strategy):
    n1, n2 = 50, 200
    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
    def next(self):
        # acts on NEXT bar's open -> no lookahead
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.position.close()

# 4. BACKTEST with realistic cost drag (commission ~ round-trip proxy incl. STT/GST/slippage)
bt = Backtest(data, SmaCross, cash=1_500_000,
              commission=0.0006, trade_on_close=False)
stats = bt.run()
print(stats[["Return [%]", "Sharpe Ratio", "Max. Drawdown [%]",
             "# Trades", "Win Rate [%]"]])

# 5. EQUITY CURVE
bt.plot(filename="nifty_sma_equity.html", open_browser=False)
```

What this teaches with real numbers: over ~11 years, a 50/200 cross on Nifty produces very *few* trades (roughly 10–20), so the 0.06% cost proxy barely dents it — a trend system's low turnover is its cost advantage (contrast a daily mean-reversion system trading 200×/year, where the same 0.06% compounds into a big drag). The printed Sharpe and Max Drawdown are your honest scorecard. Change `n1, n2` and re-run to feel how *sensitive* results are — if 50/200 works but 48/210 collapses, you've curve-fit. To sweep parameters fast, port the same signal to `vectorbt` and vectorise across a grid of (n1, n2) in one call.

For an intraday variant you'd pull minute candles from the Kite historical API instead of yfinance, and raise the cost/slippage assumption sharply (intraday STT + more fills).

## How pros do it / common mistakes

- **Pros separate research from execution.** The backtest above never touches a live order. Signal logic is reused; execution is a separate, tested layer (next chapter).
- **They pin versions and cache data** so a result is reproducible months later — `pip freeze > requirements.txt`, save the raw CSV.
- **They model costs *and* slippage pessimistically.** If the edge survives double the expected costs, it might be real.
- **They test out-of-sample.** Fit parameters on 2015–2021, validate untouched on 2022–2026. In-sample-only results are fiction.
- **Retail mistakes:** lookahead bias (buying at the close using the close); zero-cost backtests; over-fitting to one parameter set; ignoring survivorship bias (a stock universe that excludes delisted names flatters returns); trusting a stellar equity curve built on 4 trades.
- **Red flags:** Sharpe > 3 on daily data; an equity curve with no drawdowns; results that vanish when you shift signals by one bar (that *was* lookahead).

## Checklist / drill

1. Is my data source **pinned and cached**, so this is reproducible?
2. Do signals **act on t+1**, with no lookahead?
3. Are **STT (01-Apr-2026), GST, exchange, stamp AND slippage** all modelled?
4. Did I validate **out-of-sample**, not just in-sample?
5. Is the result **robust** to small parameter changes (not curve-fit)?

**Drill:** Run the script above. Then (a) set `commission=0` and note how much the reported return inflates — that gap is your cost reality; (b) change 50/200 to 48/210 and see if the edge holds; (c) deliberately introduce lookahead (`trade_on_close=True` with a close-based signal) and watch the Sharpe jump — that jump is exactly the bias pros hunt for and kill.
