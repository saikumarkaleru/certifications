# Project 3 — Multi-Asset Technical Coverage Watchlist

Screens **21 assets across 6 sectors** (indices, banking, IT, energy/materials, auto/FMCG, commodities)
on a **multi-timeframe** basis — daily + weekly trend confluence, MACD, RSI, a candlestick read and key
levels — and tags each **Buy / Sell / Hold** with a **★ strength** rating and an ATR stop. Output is a
sector-grouped morning coverage sheet for relationship managers.

This is an **Excel + Python** coverage workflow — an Excel scoring sheet, plus a Python screener that
scans all 21 names at once.

**Stack:** Python · pandas · numpy · yfinance · Excel

---

## What's in this folder
| File | What it is |
|------|------------|
| `watchlist.py` | The Python screener that scores all 21 assets. |
| `Coverage_Watchlist.xlsx` | The **Excel** coverage sheet — dropdowns, an auto **View** formula (daily & weekly agree), ★ strength, RSI heat-colouring and a BUY/SELL/HOLD `COUNTIF` summary. |
| `output/watchlist.pdf`, `output/watchlist.csv` | The generated coverage sheet. |

## How to run
```
pip install -r ../requirements.txt
python watchlist.py
```

## The data
Prices are pulled **fresh from Yahoo Finance** (`yfinance`) each run — **2 years of daily OHLC** for each of
the 21 names — so nothing is frozen. This is **current end-of-day data, refreshed each run — not a real-time
feed**. Each run also saves the exact data used to **`input/data_<asset>.csv`**
(one file per name) so the source is visible and auditable; the coverage sheet lands in `output/`.

---

## How it scores
- **Multi-timeframe confluence** — the daily trend and weekly trend (from 20/50-MA and price). The
  strongest setups are where **both timeframes agree**.
- **Composite score** across daily trend + weekly trend + MACD + price-vs-50MA + RSI extremes +
  candlestick read; the **★ strength** reflects how many factors align.
- Same oversold/overbought guardrail as the report; ATR stop on actionable calls; grouped by sector.

---

## Code walkthrough

The whole screener is plain pandas. Here are the five pieces that do the real work, each with the actual code and a plain-English read.

### Multi-timeframe trend (`trend_of`)
```python
def trend_of(close):
    sma20, sma50 = close.rolling(20).mean().iloc[-1], close.rolling(50).mean().iloc[-1]
    last = close.iloc[-1]
    if sma20 > sma50 and last > sma20:
        return "Up"
    if sma20 < sma50 and last < sma20:
        return "Down"
    return "Sideways"
```
A moving average is just the average closing price over the last N days, which smooths out the daily noise. We compute a fast 20-day and a slow 50-day average. It's an **uptrend** ("Up") only when the price sits above the 20-day average *and* the 20-day sits above the 50-day — short-term strength stacked over the long-term. "Down" is the exact mirror, and anything tangled in between is "Sideways".

### Weekly resample for confluence
```python
# weekly trend for multi-timeframe confluence
wk = df.resample("W-FRI").agg({"Open": "first", "High": "max",
                               "Low": "min", "Close": "last"}).dropna()
weekly_trend = trend_of(wk["Close"]) if len(wk) >= 50 else "n/a"
```
`resample("W-FRI")` rolls the daily bars up into **weekly candles** (each week ending Friday): the week's open is the first day's open, its high is the max, its low is the min, its close is the last day's close. We then run the same `trend_of` on that weekly series. When the daily and weekly trends *agree*, that's "confluence" — a higher-conviction setup than the daily chart alone.

### Candlestick detection (`candle_signal`)
```python
body, rng = abs(c - o), max(h - l, 1e-9)
lower_wick = min(o, c) - l
upper_wick = h - max(o, c)
if pc < po and c > o and o <= pc and c >= po:
    return "Bull engulf"
# ...
if body <= 0.3 * rng and lower_wick >= 2 * body:
    return "Hammer"
```
Each candle has a **body** (open-to-close) and **wicks** (the thin tails above and below). The rules just describe shapes: a *bullish engulfing* is yesterday's down-candle fully swallowed by today's up-candle (buyers took control); a *hammer* is a small body with a long lower wick (sellers pushed it down but buyers slammed it back up). The mirror shapes — bearish engulfing and shooting star — flag the opposite, and a near-zero body is a *doji* (indecision).

### Composite score → Buy / Sell / Hold + guardrail
```python
score = 0
score += {"Up": 1, "Sideways": 0, "Down": -1}[daily_trend]
score += {"Up": 1, "Sideways": 0, "Down": -1, "n/a": 0}[weekly_trend]
score += 1 if macd_line > macd_sig else -1
score += 1 if last > c.rolling(50).mean().iloc[-1] else -1
if r > 70:   score -= 1
elif r < 30: score += 1
# ... candlestick adds +1 / -1 ...
signal = "BUY" if score >= 2 else "SELL" if score <= -2 else "HOLD"
if signal == "SELL" and r < 25:  signal = "HOLD"
elif signal == "BUY" and r > 80: signal = "HOLD"
```
Six factors each cast a single vote: +1 if bullish, −1 if bearish. Add them up (the total runs −6 to +6). A clearly positive total (**≥ 2**) is a BUY, a clearly negative one (**≤ −2**) is a SELL, and anything in the muddy middle is a HOLD. The **guardrail** then overrides the extremes: it refuses to SELL something already deeply oversold (RSI < 25, likely to bounce) or chase a BUY that's already very overbought (RSI > 80, likely to pull back).

### ★ strength and ATR stop
```python
stars = "★" * min(3, abs(score)) + "☆" * (3 - min(3, abs(score)))
stop = (last - 1.5 * atr if signal == "BUY"
        else last + 1.5 * atr if signal == "SELL" else np.nan)
```
The **★ strength** is just how far the score is from zero (capped at 3): the more factors that agree, the more filled stars. ATR (Average True Range) is the asset's typical daily price travel, so a **1.5 × ATR** stop sits one-and-a-half "normal days" away from the entry — below price for a BUY, above for a SELL. HOLDs get no stop. Sizing the stop to each asset's own volatility means a calm large-cap and a jumpy commodity each get a sensible distance.

---

## Results — sample run

> Regenerates each run; this reflects a run on **Jun 2026** data. **Summary: 4 BUY · 7 SELL · 10 HOLD.**

| Sector | Asset | Daily | Weekly | RSI | View | ★ | Stop |
|--------|-------|-------|--------|----:|------|---|-----:|
| Indices | Bank Nifty | Up | Sideways | 78 | **BUY** | ★★★ | 56,996 |
| Indices | Nifty 50 | Sideways | Sideways | 64 | **BUY** | ★★☆ | — |
| Banking | HDFC Bank | Sideways | Sideways | 71 | **BUY** | ★★☆ | — |
| Banking | Kotak Bank | Up | Sideways | 74 | **BUY** | ★★☆ | — |
| Banking | Axis Bank | Up | Up | 87 | HOLD | — | — |
| IT | Infosys | Down | Down | 29 | **SELL** | ★★★ | 1,092 |
| IT | TCS | Down | Down | 34 | **SELL** | ★★★ | 2,174 |
| IT | HCL Tech | Down | Down | 35 | **SELL** | ★★★ | 1,146 |
| Energy/Mat. | Tata Steel | Down | Sideways | 26 | **SELL** | ★★☆ | 195 |
| Auto/FMCG | Maruti | Down | Down | 55 | **SELL** | ★★☆ | — |
| Auto/FMCG | ITC | Sideways | Down | 73 | **SELL** | ★★★ | 296 |
| Commodities | Gold (COMEX) | Down | Sideways | 31 | **SELL** | ★★★ | 4,225 |

*(HOLD names not shown — mixed/contradictory signals, no edge.)*

### What the results say
- **IT was the weakest sector** — Infosys, TCS and HCL Tech all SELL with daily+weekly agreement (the
  highest-conviction ★★★ setups).
- **Indices & banks led the long side** — Bank Nifty, Nifty, HDFC Bank and Kotak Bank flagged BUY.
- **Axis Bank sat on HOLD** despite an "Up" daily+weekly, because RSI was extremely overbought (87) —
  the guardrail keeps the model from chasing a stretched move.

---

## Limitations
Mechanical scoring (a human adds context) · the Python composite View is richer than the simple
"both-timeframes-agree" rule in the Excel sheet — both are defensible, but they can differ on borderline
names · commodity data uses global benchmarks as MCX proxies.
