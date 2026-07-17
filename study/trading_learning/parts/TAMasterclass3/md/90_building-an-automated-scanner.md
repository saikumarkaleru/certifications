# Building an Automated Scanner

A scanner is the single highest-leverage piece of infrastructure a discretionary or semi-systematic trader can build. The Indian equity universe alone is roughly 2,000 tradeable names on the NSE; add the F&O list (around 180-220 stocks plus indices), the MCX commodity contracts, and currency pairs, and no human can eyeball charts fast enough to find the handful that match a setup on any given day. A scanner does that work in seconds, every day, without fatigue, without recency bias, and without the emotional pull of yesterday's winner. This chapter is about turning a trading edge you already understand into a repeatable, automated filter that surfaces exactly the charts worth your attention — and nothing else.

We will build the concept up from what a scan actually is, cover the two India-realistic platforms most traders use (Chartink for no-code and a Python stack for full control), work a complete example end to end with real levels and rupee figures, and then be honest about the traps — survivorship, repainting, look-ahead bias, and the seductive lie of a scan that looks perfect on today's chart.

## What a scanner is and the logic behind it

A scanner is a **filter applied across a universe of instruments at a point in time**. It takes three things: a *universe* (which symbols), a *rule set* (boolean conditions built from price, volume, and derived indicators), and a *timeframe* (daily, weekly, 15-minute, etc.). It returns the subset of symbols where every condition is simultaneously true.

The mental model that matters: a scanner is not a strategy and it is not a prediction. It is a **funnel**. Your trading edge lives in the setup — say, "pullback to the 20-EMA in a stock making higher highs on rising volume." The scanner's only job is to convert that English sentence into machine-checkable conditions and hand you the 8 or 12 stocks out of 200 that qualify. You still apply judgment, position sizing, and risk management afterwards. A scanner that returns 150 results is useless (no funnel), and one that returns zero every day is either broken or too greedy. The sweet spot for a daily discretionary trader is roughly **5 to 25 candidates** — few enough to review each chart in a minute, many enough that you are not forcing trades on thin days.

The reason automation beats manual chart-flipping is not just speed. It is **consistency and honesty**. When you flip charts by hand, you unconsciously stop at names you already like and skip names you have a bias against. A coded rule applies the identical test to Reliance and to a small-cap you have never heard of. That neutrality is where a lot of hidden edge comes from — the scanner finds the stock you would never have looked at.

## Anatomy of a scan: the building blocks

Every scan, regardless of platform, is assembled from a small vocabulary:

| Block | Examples | Purpose |
|---|---|---|
| Price references | Close, Open, High, Low, prior-day Close | The raw series |
| Moving averages | SMA/EMA 20, 50, 100, 200; VWAP | Trend & mean-reference |
| Volume | Volume, 20-day avg volume, volume ratio | Confirmation / participation |
| Volatility | ATR(14), Bollinger width, NR7 | Regime & stop sizing |
| Momentum | RSI(14), MACD, rate-of-change, ADX | Strength & exhaustion |
| Structural | 52-week high/low, N-day breakout, gap % | Position in range |
| Relative | Stock return vs Nifty return | Relative strength |
| Cross-timeframe | Weekly trend + daily trigger | Multi-frame alignment |

A robust scan almost always combines blocks from **different families** so the conditions are not redundant. Three trend conditions that all say "price is above its moving averages" add nothing over one. A trend condition *plus* a volume condition *plus* a volatility contraction condition each carry independent information, and their intersection is meaningfully rarer and higher quality.

The core discipline is **the funnel order**: put the cheapest, most-eliminating filter first. Liquidity is almost always filter #1 — there is no point finding a beautiful setup in a stock that trades 4,000 shares a day, because you cannot get in or out and the chart itself is noise. A typical funnel for Indian equities:

1. **Liquidity gate** — 20-day average traded value above, say, ₹5 crore (or restrict to the F&O universe / Nifty 500 outright).
2. **Regime/trend filter** — the broad context (e.g., price above 200-DMA, or Nifty itself above its 50-DMA).
3. **Setup trigger** — the specific pattern you trade.
4. **Timing/quality refiners** — volume surge, RSI band, distance-from-MA sanity.

## Construction on Chartink (no-code, India-native)

Chartink is the de-facto free scanner for NSE traders because its data and universe are Indian by default and it needs no coding. Its query language is a compact English-like DSL. The structure is always `[timeframe] condition and [timeframe] condition ...`.

A worked liquidity + trend + pullback scan reads:

```
( {cash} (
  latest close > latest sma( close,50 ) and
  latest sma( close,50 ) > latest sma( close,200 ) and
  latest close < latest ema( close,20 ) * 1.02 and
  latest close > latest ema( close,20 ) * 0.98 and
  latest volume > latest sma( volume,20 ) and
  latest close * latest volume > 50000000
) )
```

Reading it line by line: price above the 50-DMA and 50 above 200 establishes an uptrend (the classic "stacked" structure); price hugging the 20-EMA within a ±2% band is the pullback trigger; volume above its 20-day average is participation; and `close * volume > 5,00,00,000` is the ₹5-crore turnover liquidity gate. On Chartink you can save this, run it after market close, set it to run intraday on 5- or 15-minute candles, and get email/Telegram alerts. The `{cash}` token scans the equity segment; you can swap in `{57960}` style group codes or use the built-in "Nifty 500" watchlist to constrain the universe — a cleaner way to guarantee liquidity than a turnover formula.

Chartink's strength is zero setup and correct Indian data. Its limits matter: **no true backtest of intraday entries with realistic fills, limited custom indicators, and a shared engine** that only sees standard fields. The moment you want ATR-based position sizing, walk-forward validation, or a custom composite score, you graduate to code.

## Construction in Python (full control)

The professional stack is Python with `pandas`, a data source, and a technical-indicator library. For Indian data, common sources are the NSE bhavcopy (free end-of-day), broker APIs (Zerodha Kite, Upstox, Angel One SmartAPI, Fyers) for live and historical candles, or paid vendors. Here is a compact but complete daily scanner skeleton that reproduces the pullback logic and adds an ATR-based risk column:

```python
import pandas as pd
import numpy as np

def ema(s, n):
    return s.ewm(span=n, adjust=False).mean()

def atr(df, n=14):
    h, l, c = df['high'], df['low'], df['close']
    tr = pd.concat([h - l,
                    (h - c.shift()).abs(),
                    (l - c.shift()).abs()], axis=1).max(axis=1)
    return tr.rolling(n).mean()

def scan_symbol(df):
    """df: daily OHLCV for one symbol, oldest->newest, >=200 rows."""
    df = df.copy()
    df['sma50']  = df['close'].rolling(50).mean()
    df['sma200'] = df['close'].rolling(200).mean()
    df['ema20']  = ema(df['close'], 20)
    df['vol20']  = df['volume'].rolling(20).mean()
    df['atr14']  = atr(df)

    r = df.iloc[-1]                      # today's completed candle
    turnover = r['close'] * r['volume']

    cond = (
        r['close']  > r['sma50']  and
        r['sma50']  > r['sma200'] and
        abs(r['close'] - r['ema20']) / r['ema20'] < 0.02 and
        r['volume'] > r['vol20']  and
        turnover    > 5e7
    )
    if not cond:
        return None

    stop   = r['close'] - 1.5 * r['atr14']
    risk_pct = (r['close'] - stop) / r['close'] * 100
    return {
        'close': round(r['close'], 2),
        'ema20': round(r['ema20'], 2),
        'atr14': round(r['atr14'], 2),
        'stop':  round(stop, 2),
        'risk_%': round(risk_pct, 2),
        'turnover_cr': round(turnover / 1e7, 1),
    }

# universe: dict of {symbol: dataframe}
results = {sym: scan_symbol(df) for sym, df in universe.items()}
hits = {s: r for s, r in results.items() if r}
out = pd.DataFrame(hits).T.sort_values('risk_%')
print(out.head(25))
```

The crucial line for correctness is `r = df.iloc[-1]` referencing the **completed** candle. If you are scanning live intraday, the current forming candle is not final — its close and volume change every tick — so a rule evaluated on it will flicker and "repaint." For end-of-day scans this is a non-issue; for intraday, always evaluate on the last *closed* bar (`df.iloc[-2]` if the live bar is still forming) unless you deliberately want a real-time trigger and can live with it re-firing.

Notice what the Python version buys you that Chartink cannot: the scan output already includes the **ATR-based stop, the percentage risk, and the position-size-relevant fields**, sorted so the tightest-risk setups float to the top. This is the difference between a list of tickers and a ranked, trade-ready shortlist.

## Worked India example, end to end

Suppose it is a Thursday evening in 2026. Nifty closed at 24,850, itself comfortably above its 50-DMA — so the regime filter (bullish broad market) passes and we are happy running a long-pullback scan. We run the Python scanner over the Nifty 500 bhavcopy. It returns 11 hits. The top three by tightest risk:

| Symbol | Close (₹) | 20-EMA (₹) | ATR (₹) | Stop (₹) | Risk % | Turnover (₹ cr) |
|---|---|---|---|---|---|---|
| TITAN | 3,420 | 3,405 | 41 | 3,358 | 1.81 | 210 |
| CIPLA | 1,512 | 1,505 | 22 | 1,479 | 2.18 | 95 |
| TATASTEEL | 168 | 166.5 | 3.1 | 163.3 | 2.80 | 340 |

Take TITAN. The scan tells you: it is in a stacked uptrend (close 3,420 > 50-DMA > 200-DMA), it has pulled back to sit right on its 20-EMA (3,405, within 0.4%), volume today beat its 20-day average, and it trades ₹210 crore a day so fills are trivial. The ATR is ₹41, so a 1.5-ATR stop sits at ₹3,358 — a risk of ₹62 per share, or 1.81% of price.

Now the human judgment the scanner deliberately does *not* make: you pull the TITAN daily chart. You confirm the pullback is orderly (three small red candles, not one violent gap down on bad news). You check there is no earnings event in the next two sessions. Satisfied, you plan the trade:

- **Entry**: ₹3,425 on a break above today's high (buy-stop), confirming the pullback is resolving up.
- **Stop**: ₹3,358 (below the 20-EMA and 1.5 ATR away). Risk per share ≈ ₹67.
- **Target**: prior swing high at ₹3,560 (T1, ~2R) and a measured-move / trailing exit beyond.
- **Size**: risking ₹10,000 of a ₹10-lakh account (1%), position = 10,000 / 67 ≈ **149 shares**, a ₹5.1-lakh notional position. Because TITAN is in F&O, you might instead express this with a slightly OTM call debit spread to cap theta and define risk, but the cash-equity sizing is the honest baseline.

The scanner did in three seconds what would have taken an hour of chart-flipping, and it handed you the stop and the size, not just the name. That is the whole point.

## From scan to system: turning it into a daily process

A scanner only pays off if it is embedded in a **repeatable daily workflow**. The mature setup looks like this:

1. **Data refresh** — automated download of the day's bhavcopy or an API pull, run by a scheduler (`cron` on Linux/Mac, Task Scheduler on Windows) a few minutes after the 3:30 pm close, once NSE publishes final data.
2. **Run the scan(s)** — often several in parallel: a long-pullback scan, a short-breakdown scan, a breakout scan, a mean-reversion scan. Each writes its ranked output to a CSV or a Google Sheet.
3. **Alert delivery** — a Telegram bot or email pushes the shortlist to your phone so you review charts on the commute, not at 9:14 am in a panic.
4. **Manual review & journal** — you tag which candidates you will actually trade and why, feeding a journal that later tells you which *scan* is producing your winners.
5. **Pre-open plan** — by 9:00 am you have entries, stops, and sizes written down, and you place buy-stop / sell-stop orders (GTT on Zerodha, or bracket orders) rather than reacting live.

The last step matters more than the code. A scanner's job is to let you make decisions the *night before*, calmly, so the market open is pure execution. Traders who run a scan but still improvise at 9:15 have automated the easy part and left the hard part to their worst self.

## Confluence: making the scan smarter, not just longer

The temptation is to keep bolting on conditions until the scan returns only "perfect" charts. Resist it. Beyond four or five well-chosen, non-redundant conditions, each extra rule mostly removes *valid* setups while doing little to remove bad ones — you are curve-fitting the filter to the past. Better ways to add real quality:

- **Relative strength**, not more absolute conditions: require the stock's 3-month return to beat Nifty's. This single condition tends to improve long-scan hit rates more than any number of moving-average tweaks, because leaders keep leading.
- **Multi-timeframe alignment**: require the weekly trend up *and* the daily trigger. On Chartink, prefix conditions with `weekly` and `latest`. This is genuine independent information.
- **Ranking instead of filtering**: rather than a hard RSI cutoff, compute a composite score (e.g., relative strength percentile + volume-surge z-score + tightness of pullback) and sort. You keep all the candidates but review the best first — far more robust than a brittle threshold that a stock either clears or misses by 0.1.
- **Regime gating at the top**: only run the long scan when Nifty is above its 50-DMA and India VIX is below, say, 20; flip to the short/defensive scan otherwise. A scan that ignores regime will happily hand you long setups into a falling market.

## Backtesting the scan honestly

A scan can be backtested by asking: "If I had bought every hit on the close (or next open) with this stop and this target, over the last 3-5 years, what would the distribution of outcomes look like?" The metrics that matter are win rate, average R (reward-to-risk realized), expectancy per trade, maximum drawdown, and how many trades per month it produces. A scan with a 40% win rate and average 2.5R winners is excellent; a 70% win-rate scan with 0.5R winners and occasional 4R losers is a trap.

Two costs you must model or you will fool yourself:

- **Slippage and impact** — mid- and small-caps in India can slip 0.3-1% on a market order. On the pullback example, add ~0.1-0.3% to entry and exit. Ignoring this turns a marginal edge into a fictional one.
- **Brokerage, STT, and charges** — for equity delivery, STT is 0.1% each side plus exchange and stamp charges; for intraday and F&O the structure differs. A scan that trades often is far more sensitive to these. Always net-of-cost your backtest.

## Pitfalls: where scanners lie to you

**Survivorship bias.** If your backtest universe is "today's Nifty 500," you have quietly excluded every stock that got delisted, went bankrupt, or fell out of the index — precisely the losers. Your scan will look far better in backtest than it will live. The fix is a **point-in-time universe**: use the index constituents *as they were* on each historical date. This is the single most common way retail scanner backtests overstate edge.

**Look-ahead bias.** Using data that would not have been available at decision time — scanning on today's close but assuming you could have bought at today's close (you learn the close only *after* the market shuts). Be explicit: signal on close, execute on the *next* open or via next-day buy-stop, and backtest that way.

**Repainting / non-final bars.** Covered above — evaluating rules on a forming candle makes signals appear and vanish. Anything using the current live bar, or indicators that reference the future (some "no-repaint" claims are false), will look magical in hindsight and fail live.

**Over-optimization.** Twelve conditions and three magic constants tuned until the equity curve is beautiful is not a strategy; it is a memorized description of the past. Prefer few, economically-motivated conditions. Validate on **out-of-sample** data (build on 2019-2023, test untouched on 2024-2026) and via walk-forward. If the edge evaporates out of sample, it was never real.

**The liquidity illusion.** A scan run on the full cash universe will surface gorgeous charts in stocks that trade lakhs, not crores. The pattern is real; your ability to trade it is not. Keep the liquidity gate first and honest.

**Data quality.** Corporate actions (splits, bonuses, dividends) break unadjusted price series — a 1:1 bonus looks like a 50% crash to a naive scan. Use adjusted data, and sanity-check for missing days and bad ticks.

## Interview-ready summary

A scanner is a **funnel, not a strategy**: it converts a defined edge into machine-checkable conditions and returns the handful of symbols, out of thousands, that qualify — consistently and without bias. Build it in a funnel order — **liquidity gate first, then regime, then the setup trigger, then quality refiners** — combining conditions from *different* families (trend, volume, volatility, relative strength) so each carries independent information. For the Indian market, Chartink gives a zero-code, NSE-native engine ideal for quick daily and intraday scans, while a Python + pandas + broker-API stack gives full control: custom indicators, ATR-based stops and sizing baked into the output, and honest backtesting. Ranking by a composite score beats brittle hard thresholds; regime gating (Nifty above/below its 50-DMA, India VIX level) keeps you from running long scans into a bear market. The output must be **trade-ready** — symbol, entry, stop, size — so decisions are made calmly the night before and the open is pure execution. Be ruthless about the classic lies: survivorship bias (use point-in-time universes), look-ahead bias (signal on close, execute next bar), repainting (evaluate only completed candles), over-optimization (few economically-motivated rules, validated out-of-sample), and the liquidity illusion (a beautiful chart you cannot fill is worthless). A good scanner does not predict — it directs your limited attention to where your edge is most likely to be, faster and more honestly than you ever could by hand.
