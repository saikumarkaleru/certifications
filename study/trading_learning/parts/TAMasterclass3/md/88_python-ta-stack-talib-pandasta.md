# Python TA Stack: TA-Lib & pandas-ta

## The concept

Once a chart idea survives eyeballing on TradingView, the next honest step is to compute it over *years* of Nifty and Bank Nifty data, on hundreds of NSE stocks, reproducibly, with numbers you can inspect. That is the job of the Python technical-analysis stack. The two workhorse libraries are **TA-Lib** (a C library with a Python wrapper, fast and battle-tested, ~150 functions) and **pandas-ta** (pure Python built on pandas/NumPy, ~130+ indicators, DataFrame-native and easy to install). They compute the same *kinds* of things — moving averages, RSI, MACD, ATR, Bollinger Bands, ADX, Supertrend — but they differ in speed, install pain, default parameters, and how they hand you results.

The mental model you must internalise: an indicator library takes a **price DataFrame** — typically OHLCV indexed by timestamp — and returns **derived series** aligned to that same index. Nothing more. It does not know about position sizing, costs, expiry, or lot sizes. It does not backtest. It transforms price into features. Keeping that boundary clean (data → features here; features → decisions and P&L in a separate backtest layer) is what separates a maintainable research workflow from a tangle of look-ahead bugs.

Why two libraries? TA-Lib is the reference implementation — when a fund quotes "RSI(14)," they almost certainly mean TA-Lib's Wilder-smoothed version. It is fast enough to run over the entire NSE universe. But it needs the underlying C library installed, which historically caused grief on Windows. pandas-ta installs with a plain `pip`, returns tidy pandas objects, supports method-chaining via a `.ta` accessor, and covers newer indicators (Supertrend, HMA, many others) that TA-Lib lacks. Many Indian retail quants use pandas-ta for exploration and TA-Lib when they need reference-exact values or speed. In practice you often keep both and cross-check.

## The method and the maths (precise)

### Getting clean OHLCV

Everything starts with a correct DataFrame. A realistic Indian setup pulls Nifty/Bank Nifty and NSE stocks. Common sources: `yfinance` (append `.NS` for NSE cash, e.g. `RELIANCE.NS`, `^NSEI` for Nifty 50, `^NSEBANK` for Bank Nifty), broker APIs (Kite Connect, Angel SmartAPI, Dhan), or paid vendors. The non-negotiable hygiene steps:

1. Ensure a proper `DatetimeIndex` in `Asia/Kolkata`.
2. Columns named exactly `open, high, low, close, volume` (pandas-ta is case-insensitive but be consistent).
3. Drop or forward-handle NSE holidays and half-days; never interpolate prices across gaps.
4. Adjust for splits/bonuses if using cash equities — an unadjusted Reliance chart will show a fake crash on a bonus date.
5. Sort ascending by time. Out-of-order rows silently corrupt every rolling calculation.

### The indicator maths that actually matters

Most libraries hide the smoothing convention, and the convention changes the number. Two examples every serious user should know cold.

**Wilder's RSI(14).** RSI = 100 − 100/(1 + RS), where RS = average gain / average loss. The subtlety is the *averaging*: Wilder uses a smoothed (running) average, not a simple mean:

```
AvgGain_t = (AvgGain_{t-1} * 13 + Gain_t) / 14
```

TA-Lib's `RSI` uses this Wilder smoothing. Some naive implementations use a simple rolling mean and produce slightly different, non-standard values — which is why your Python RSI may not match TradingView unless both use Wilder's method. pandas-ta's `rsi` also uses Wilder by default.

**ATR(14).** True Range = max(high−low, |high−prevClose|, |low−prevClose|). ATR is then Wilder-smoothed TR. This is the backbone of volatility-scaled stops (the ₹ math from the Pine chapter). Because it uses the previous close, ATR needs one bar of warm-up and is undefined on the first row — a source of `NaN` you must handle.

### TA-Lib usage

TA-Lib takes NumPy arrays, returns NumPy arrays, and prepends `NaN` for the warm-up period:

```python
import numpy as np, pandas as pd, talib

df = pd.read_parquet("banknifty_15m.parquet")  # tz-aware, sorted, clean
close = df["close"].to_numpy(dtype=float)
high  = df["high"].to_numpy(dtype=float)
low   = df["low"].to_numpy(dtype=float)

df["rsi14"]   = talib.RSI(close, timeperiod=14)
df["atr14"]   = talib.ATR(high, low, close, timeperiod=14)
macd, sig, hist = talib.MACD(close, 12, 26, 9)
df["macd"], df["macd_sig"], df["macd_hist"] = macd, sig, hist
upper, mid, lower = talib.BBANDS(close, 20, 2, 2)
df["bb_up"], df["bb_mid"], df["bb_lo"] = upper, mid, lower
```

TA-Lib also has an *abstract* API (`talib.abstract`) that accepts a DataFrame-like dict, handy for programmatic pipelines. Note that TA-Lib returns arrays aligned by position, so you must assign back to the DataFrame you sliced from — never mix rows.

### pandas-ta usage

pandas-ta attaches a `.ta` accessor to any DataFrame and can append results in place:

```python
import pandas as pd
import pandas_ta as ta

df.ta.rsi(length=14, append=True)          # -> column RSI_14
df.ta.atr(length=14, append=True)          # -> column ATRr_14
df.ta.macd(fast=12, slow=26, signal=9, append=True)
df.ta.bbands(length=20, std=2, append=True)
df.ta.supertrend(length=10, multiplier=3, append=True)  # not in TA-Lib
```

The **Strategy** object batches many indicators in one call, which is convenient for building a feature matrix:

```python
mystrat = ta.Strategy(
    name="india_features",
    ta=[
        {"kind": "ema", "length": 20},
        {"kind": "ema", "length": 50},
        {"kind": "rsi", "length": 14},
        {"kind": "atr", "length": 14},
        {"kind": "adx", "length": 14},
        {"kind": "supertrend", "length": 10, "multiplier": 3},
    ],
)
df.ta.strategy(mystrat)   # can run multi-threaded across indicators
```

One gotcha: pandas-ta and TA-Lib sometimes name/round things differently and occasionally use a different default (e.g. ATR "RMA" vs SMA smoothing in older versions). pandas-ta can even *delegate* to TA-Lib if installed (`talib=True`), giving reference-exact values while keeping the tidy API — a good default when both are available.

## A worked example with data (levels and rupees)

Goal: build a small, honest feature set on **Nifty 50 daily** and generate a simple long-only trend signal, then sanity-check it before ever calling it a strategy. Assume Nifty around 26,500 (a realistic 2026 level).

```python
import yfinance as yf, pandas as pd, pandas_ta as ta

nifty = yf.download("^NSEI", start="2015-01-01",
                    interval="1d", auto_adjust=False)
nifty.columns = [c.lower() for c in nifty.columns]
nifty = nifty.dropna().sort_index()

nifty.ta.ema(length=50, append=True)
nifty.ta.ema(length=200, append=True)
nifty.ta.atr(length=14, append=True)
nifty.ta.rsi(length=14, append=True)

# Signal: golden-cross regime, RSI not overbought
nifty["long"] = (
    (nifty["EMA_50"] > nifty["EMA_200"]) &
    (nifty["RSI_14"] < 70)
).astype(int)

# CRITICAL: shift signal by 1 bar to trade next-day open
nifty["pos"] = nifty["long"].shift(1).fillna(0)
nifty["ret"] = nifty["close"].pct_change()
nifty["strat_ret"] = nifty["pos"] * nifty["ret"]
```

The **`.shift(1)`** line is the most important in the whole example. If you compute a signal from today's close and then apply it to today's return, you are trading on information you did not have until the close — pure look-ahead. Shifting by one bar enforces "decide on today's close, act on tomorrow." Getting this wrong is the number-one reason a Python backtest looks brilliant and then loses money live.

Now the ₹ sanity check. Suppose over the sample the strategy is invested ~60% of days and produces a compound return that turns ₹10,00,000 into, say, ₹34,00,000 while buy-and-hold reaches ₹31,00,000 — a modest edge with meaningfully lower time-in-market and drawdown. Before believing any of it:

- **Costs**: this toy applies zero costs. A daily-rebalanced index strategy has few trades (regime flips are rare), so costs are small here — but the moment you move to intraday Bank Nifty with dozens of trades, STT + brokerage + slippage can erase the entire edge. Compute turnover and multiply by realistic per-trade cost.
- **Look-ahead**: verified via `.shift(1)`.
- **Warm-up NaNs**: the first 200 rows have no EMA_200; `pos` is 0 there, which is correct, but confirm you are not silently dropping them mid-series.
- **Survivorship**: `^NSEI` is fine (index), but if you ran this over "the 50 current Nifty stocks," you would be testing only today's winners over history — a classic bias.

## How to use it in a real TA workflow

The stack fits into a disciplined pipeline:

1. **Ingest & clean** OHLCV once, store as Parquet partitioned by symbol/timeframe. Clean data is reused; never re-clean ad hoc.
2. **Feature layer** — use TA-Lib/pandas-ta to compute a *wide* feature matrix (indicators at several lengths). Keep this pure: input DataFrame → output DataFrame, no decisions.
3. **Signal layer** — combine features into ent/exit booleans. Always `.shift()` before applying to returns.
4. **Backtest layer** — hand signals to vectorbt or backtesting.py (next chapter) for realistic fills, costs, and metrics. Do *not* compute P&L by hand in the feature notebook; it invites subtle bugs.
5. **Validation** — walk-forward / out-of-sample, then paper-trade via alerts before real size.

For scale (the whole NSE F&O or cash universe), TA-Lib's speed wins: loop symbols, compute arrays, concatenate. pandas-ta's multi-threaded `strategy()` helps but is slower per symbol. A common pattern: pandas-ta for interactive research, a TA-Lib batch job for nightly feature generation across the universe.

A practical India-specific tip: keep a small reconciliation test that compares your Python RSI(14)/ATR(14) on Nifty against TradingView's values on the same candles. If they diverge by more than rounding, you have a smoothing-convention or data-alignment bug — fix it before building anything on top.

## Honest limitations

- **Libraries compute; they do not think.** An indicator is a lossy transform of price. Stacking twelve of them does not create edge — it creates correlated features that overfit fast.
- **Convention mismatches are silent.** RSI/ATR/EMA can differ across libraries and versions (Wilder vs SMA smoothing, adjust=True/False on EMA). Always know which convention you are using and reconcile against a reference.
- **NaN and alignment bugs.** Warm-up NaNs, unsorted indices, and mixing positional NumPy output with a re-sliced DataFrame cause errors that do not throw — they just quietly shift your numbers. Assert index alignment.
- **No costs, no reality.** The feature layer knows nothing about STT, brokerage, slippage, impact, or lot sizes. Those live downstream and routinely flip a "profitable" indicator strategy negative on Indian intraday timeframes.
- **Look-ahead is the default failure mode.** Any research where the signal is not shifted relative to the return it earns is contaminated. Treat `.shift()` discipline as sacred.
- **Data quality dominates.** Split/bonus adjustment, holiday handling, and continuous-futures stitching for F&O affect results more than the choice of indicator. Garbage OHLCV makes the fanciest indicator worthless.

## Interview-ready summary

The Python TA stack turns price into features: **TA-Lib** (fast C core, ~150 functions, reference-exact Wilder RSI/ATR, needs the C lib) and **pandas-ta** (pure Python, DataFrame-native `.ta` accessor, batchable `Strategy`, includes Supertrend and can delegate to TA-Lib). Both take clean OHLCV and return aligned series — nothing about costs or sizing. The maths to know: Wilder-smoothed RSI and ATR, because the smoothing convention is why your numbers may not match TradingView. The workflow is layered — ingest/clean → features (pure) → signals (always `.shift()` to kill look-ahead) → a real backtester for costs and metrics → walk-forward validation. The recurring failure modes are look-ahead, convention mismatches, warm-up NaNs, survivorship, and pretending costs are zero. Reconcile against a reference, keep the boundaries clean, and never confuse "computed an indicator" with "found an edge."
