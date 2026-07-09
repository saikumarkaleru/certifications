"""
Multi-Strategy Technical Backtesting Engine — Nifty & Bank Nifty
----------------------------------------------------------------
Backtests eight rules-based technical strategies on Nifty 50 and Bank Nifty over
~6 years and benchmarks them against buy-and-hold on a full set of performance
metrics (CAGR, Sharpe, Sortino, max drawdown, win-rate, profit factor). Produces
per-strategy trade logs, an equity-curve comparison chart per index, and a
polished PDF report.

Strategies (all long/flat, no leverage, no look-ahead — signals act next day):
  1. MA Crossover + RSI       : long when 20-SMA > 50-SMA and RSI(14) > 50
  2. RSI Mean-Reversion       : buy when RSI < 30, exit when RSI > 55
  3. MACD Trend               : long when MACD line > signal line
  4. Bollinger Breakout       : enter when close breaks above upper band, exit below 20-SMA
  5. Golden Cross 50/200      : long when 50-SMA > 200-SMA
  6. Bollinger Mean-Reversion : buy below the lower band, exit back at the 20-SMA
  7. Stochastic Reversal      : buy oversold (%K<20 crossing up %D), exit overbought (%K>80)
  8. Donchian Breakout        : long above the prior 20-day high, exit below the prior 10-day low

Indicators are computed by hand with pandas.

Run:  python backtester.py
"""
import os
import base64
import shutil
import subprocess
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "output")
INP = os.path.join(os.path.dirname(__file__), "input")   # the downloaded daily data lands here
os.makedirs(OUT, exist_ok=True)
os.makedirs(INP, exist_ok=True)

TICKERS = {"Nifty 50": "^NSEI", "Bank Nifty": "^NSEBANK"}
PERIOD = "7y"  # 7y of data; the 200-day SMA needs a long warmup, leaving ~6y to test on
TRADING_DAYS = 252


# ----------------------------- indicators -----------------------------
def add_indicators(df):
    c = df["Close"]  # daily closing prices — every indicator below is built from these
    # Simple Moving Averages: the average close over the last 20 and 50 days.
    # A rising/short SMA above a slow SMA is a classic "uptrend" signal.
    df["SMA20"] = c.rolling(20).mean()
    df["SMA50"] = c.rolling(50).mean()
    # RSI (Relative Strength Index), 14-day. Measures momentum on a 0-100 scale.
    d = c.diff()                                  # today's price change vs yesterday
    g = d.clip(lower=0).rolling(14).mean()        # avg of UP moves (gains); down days count as 0
    l = (-d.clip(upper=0)).rolling(14).mean()     # avg of DOWN moves (losses) as a positive number
    # RSI formula: 100 - 100/(1 + avgGain/avgLoss). High RSI = strong recent gains.
    # replace(0, NaN) avoids dividing by zero on a stretch with no losing days.
    df["RSI"] = 100 - 100 / (1 + g / l.replace(0, np.nan))
    # MACD = fast 12-day EMA minus slow 26-day EMA (EMA = exponentially weighted avg,
    # which reacts faster than an SMA). A positive MACD means short-term momentum is up.
    macd = c.ewm(span=12, adjust=False).mean() - c.ewm(span=26, adjust=False).mean()
    df["MACD"] = macd
    df["MACD_sig"] = macd.ewm(span=9, adjust=False).mean()  # 9-day EMA of MACD = the "signal" line
    # Bollinger Bands: SMA20 plus/minus 2 standard deviations of price (the band width
    # grows when the market is volatile). Price above the upper band = unusually strong move.
    std = c.rolling(20).std()
    df["BB_up"] = df["SMA20"] + 2 * std
    df["BB_dn"] = df["SMA20"] - 2 * std
    # SMA200: the 200-day average — the long-term trend line behind the "golden cross".
    df["SMA200"] = c.rolling(200).mean()
    # Stochastic Oscillator (14, 3): where today's close sits inside the recent 14-day
    # high-low range, on a 0-100 scale. %K is the raw line, %D a 3-day smoothing of it.
    # < 20 = oversold (near the bottom of the range), > 80 = overbought.
    low14, high14 = df["Low"].rolling(14).min(), df["High"].rolling(14).max()
    df["STO_K"] = 100 * (c - low14) / (high14 - low14).replace(0, np.nan)
    df["STO_D"] = df["STO_K"].rolling(3).mean()
    # Donchian Channel: the highest high of the PRIOR 20 days and lowest low of the PRIOR
    # 10 days (shift(1) = "prior", so today's bar can break out of yesterday's channel).
    df["DON_HI"] = df["High"].rolling(20).max().shift(1)
    df["DON_LO"] = df["Low"].rolling(10).min().shift(1)
    return df.dropna()  # drop early rows where the rolling windows had no full data yet


# ------------------- position builders (strategies) -------------------
def _hold_between(entry, exit_):
    """Build a 0/1 position that turns on at `entry` and off at `exit_`."""
    # Some strategies (mean-reversion, breakout) need MEMORY: once you buy, you stay in
    # until a separate exit rule fires. A simple per-day condition can't do that, so we
    # walk day by day and carry a `holding` flag forward — this is a "stateful" position.
    pos = np.zeros(len(entry))
    holding = False                               # True while we are currently invested
    for i in range(len(entry)):
        if not holding and entry.iloc[i]:         # flat and an entry signal fires -> get in
            holding = True
        elif holding and exit_.iloc[i]:           # invested and an exit signal fires -> get out
            holding = False
        pos[i] = 1 if holding else 0              # record 1 (in market) or 0 (in cash) for the day
    return pd.Series(pos, index=entry.index)


# Trend-following: invested only while the fast SMA is above the slow SMA AND momentum
# is positive (RSI > 50). Both true each day -> 1 (in market), otherwise 0 (cash).
def strat_ma_cross(df):
    return ((df["SMA20"] > df["SMA50"]) & (df["RSI"] > 50)).astype(int)


# Mean-reversion: buy when oversold (RSI < 30) and hold until it recovers (RSI > 55).
# Needs the stateful helper because entry and exit use different thresholds.
def strat_rsi_revert(df):
    return _hold_between(df["RSI"] < 30, df["RSI"] > 55)


# Trend-following: invested whenever the MACD line is above its signal line.
def strat_macd(df):
    return (df["MACD"] > df["MACD_sig"]).astype(int)


# Breakout: enter when price closes above the upper Bollinger band (strong move) and
# hold until it falls back below the 20-day average.
def strat_bb_breakout(df):
    return _hold_between(df["Close"] > df["BB_up"], df["Close"] < df["SMA20"])


# Golden Cross: the classic long-term trend filter — invested whenever the 50-day SMA is
# above the 200-day SMA (a "golden cross"); flat once it crosses back below ("death cross").
def strat_golden_cross(df):
    return (df["SMA50"] > df["SMA200"]).astype(int)


# Bollinger Mean-Reversion: the mirror of the breakout — buy when price dips BELOW the lower
# band (stretched cheap) and hold until it reverts back up to the 20-day mean.
def strat_bb_revert(df):
    return _hold_between(df["Close"] < df["BB_dn"], df["Close"] >= df["SMA20"])


# Stochastic Reversal: buy when oversold (%K < 20) and %K turns up through %D, then hold
# until overbought (%K > 80). Catches short-term bounces off the bottom of the range.
def strat_stochastic(df):
    return _hold_between((df["STO_K"] < 20) & (df["STO_K"] > df["STO_D"]), df["STO_K"] > 80)


# Donchian Breakout (Turtle-style): go long when price closes above the prior 20-day high,
# and exit when it closes below the prior 10-day low. A pure trend-following breakout system.
def strat_donchian(df):
    return _hold_between(df["Close"] > df["DON_HI"], df["Close"] < df["DON_LO"])


STRATEGIES = {
    "MA Crossover + RSI": strat_ma_cross,
    "RSI Mean-Reversion": strat_rsi_revert,
    "MACD Trend": strat_macd,
    "Bollinger Breakout": strat_bb_breakout,
    "Golden Cross 50/200": strat_golden_cross,
    "Bollinger Mean-Reversion": strat_bb_revert,
    "Stochastic Reversal": strat_stochastic,
    "Donchian Breakout": strat_donchian,
}


# ----------------------------- metrics --------------------------------
def trades_from_position(position, close):
    """Return list of per-trade % returns from a 0/1 position series."""
    # The 0/1 series tells us WHEN we're invested; here we slice it into individual
    # round-trip trades so we can later compute win-rate and profit factor.
    rets, in_trade, entry = [], False, None
    for i in range(len(position)):
        if not in_trade and position.iloc[i] == 1:        # position flips 0 -> 1: a trade opens
            in_trade, entry = True, close.iloc[i]         # remember the entry price
        elif in_trade and position.iloc[i] == 0:          # position flips 1 -> 0: the trade closes
            rets.append(close.iloc[i] / entry - 1)        # record its % return (exit/entry - 1)
            in_trade = False
    if in_trade:                                          # still invested at the end of the data:
        rets.append(close.iloc[-1] / entry - 1)           # close the open trade at the last price
    return rets


def performance(position, mkt_ret, close):
    # *** THE KEY ANTI-CHEATING LINE ***
    # position.shift(1) moves every signal forward by one day, so today's return uses
    # YESTERDAY's position. Why: a signal is computed from today's CLOSE, which you only
    # know after the market shuts — you can't trade on it until the next day. Without this
    # shift you'd be "trading on a price you haven't seen yet" = look-ahead bias and fake
    # profits. fillna(0) makes the very first day flat (no prior signal to act on).
    r = position.shift(1).fillna(0) * mkt_ret
    equity = (1 + r).cumprod()                    # compound daily returns into a growth-of-1 curve
    years = len(r) / TRADING_DAYS                 # ~252 trading days per year
    # CAGR = the steady annual growth rate that turns 1 into the final equity over `years`.
    cagr = equity.iloc[-1] ** (1 / years) - 1 if years > 0 else np.nan
    # Sharpe = average daily return / its volatility, scaled to a year by sqrt(252).
    # Higher = more return per unit of total risk (assumes ~0% risk-free rate).
    sharpe = r.mean() / r.std() * np.sqrt(TRADING_DAYS) if r.std() else np.nan
    # Sortino is like Sharpe but only penalises DOWNSIDE volatility (std of losing days),
    # since investors don't mind upside swings.
    downside = r[r < 0].std()
    sortino = r.mean() / downside * np.sqrt(TRADING_DAYS) if downside else np.nan
    # Max drawdown = worst peak-to-trough drop. cummax() is the running all-time-high of
    # the equity curve; equity/peak - 1 is how far below the peak we are; .min() = the worst.
    max_dd = (equity / equity.cummax() - 1).min()
    trades = trades_from_position(position, close)  # list of individual trade returns
    wins = [t for t in trades if t > 0]             # profitable trades
    losses = [t for t in trades if t <= 0]          # break-even or losing trades
    gross_win = sum(wins)                           # total profit from winners
    gross_loss = abs(sum(losses))                   # total loss from losers (as a positive number)
    # Win % = winners / all trades; Profit Factor = gross_win / gross_loss (>1 means
    # winners outweigh losers). Both are computed in the return dict below.
    return {
        "Total Return %": (equity.iloc[-1] - 1) * 100,
        "CAGR %": cagr * 100,
        "Sharpe": sharpe,
        "Sortino": sortino,
        "Max DD %": max_dd * 100,
        "Trades": len(trades),
        "Win %": (len(wins) / len(trades) * 100) if trades else np.nan,
        "Profit Factor": (gross_win / gross_loss) if gross_loss else np.nan,
        "Exposure %": position.mean() * 100,
        "_equity": equity,
        "_trades": trades,
    }


# ----------------------------- data -----------------------------------
def load(ticker):
    df = yf.download(ticker, period=PERIOD, progress=False, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return add_indicators(df[["Open", "High", "Low", "Close"]].dropna())


# ----------------------------- charts ---------------------------------
def equity_chart(name, results, bh_equity):
    plt.figure(figsize=(11, 3.9))
    for strat, res in results.items():
        plt.plot(res["_equity"].index, res["_equity"], label=strat, linewidth=1.3)
    plt.plot(bh_equity.index, bh_equity, label="Buy & Hold", linewidth=1.6,
             color="black", linestyle="--", alpha=0.8)
    plt.title(f"{name} — strategy equity curves vs Buy & Hold (growth of 1)")
    plt.ylabel("Equity (x)")
    plt.legend(fontsize=8)
    plt.grid(alpha=0.3)
    path = os.path.join(OUT, f"{name.replace(' ', '_').lower()}_equity.png")
    plt.tight_layout()
    plt.savefig(path, dpi=130)
    plt.close()
    return path


# ----------------------------- report ---------------------------------
def _b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


METRIC_COLS = ["Total Return %", "CAGR %", "Sharpe", "Sortino", "Max DD %",
               "Trades", "Win %", "Profit Factor", "Exposure %"]


def fmt(v):
    return "-" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v:,.2f}"


def metrics_table(rows):
    head = "<tr><th>Strategy</th>" + "".join(f"<th>{c}</th>" for c in METRIC_COLS) + "</tr>"
    body = ""
    for strat, res in rows.items():
        cells = "".join(f"<td>{fmt(res[c])}</td>" for c in METRIC_COLS)
        body += f"<tr><td class='s'>{strat}</td>{cells}</tr>"
    return f"<table>{head}{body}</table>"


def build_report(blocks, date_str):
    sections = ""
    for name, res, chart, bh in blocks:
        rows = dict(res)
        rows["Buy & Hold"] = bh
        sections += f"""
        <h2>{name}</h2>
        {metrics_table(rows)}
        <img class="chart" src="{_b64(chart)}"/>
        """
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
      @page {{ size: A4 landscape; margin: 12mm; }}
      * {{ box-sizing: border-box; }}
      body {{ font-family:"Calibri","Segoe UI",sans-serif; color:#1a1a1a; font-size:9.5pt; }}
      h1 {{ color:#16365c; font-size:16pt; border-bottom:2.4px solid #16365c; padding-bottom:4px; }}
      .meta {{ color:#555; font-size:9pt; margin:2px 0 10px; }}
      h2 {{ color:#16365c; font-size:12.5pt; margin:14px 0 4px; page-break-after:avoid; }}
      table {{ border-collapse:collapse; width:100%; font-size:9pt; margin-bottom:6px; }}
      th {{ background:#16365c; color:#fff; padding:4px 6px; text-align:right; }}
      th:first-child {{ text-align:left; }}
      td {{ padding:3px 6px; border-bottom:1px solid #e3e8ef; text-align:right; }}
      td.s {{ text-align:left; font-weight:600; }}
      tr:last-child td {{ background:#fff7e6; font-weight:600; }}
      .chart {{ width:82%; display:block; border:1px solid #eee; border-radius:4px; margin:2px auto 4px; page-break-inside:avoid; }}
      .note {{ color:#666; font-size:8.4pt; margin-top:8px; }}
    </style></head><body>
      <h1>Multi-Strategy Technical Backtest — Nifty &amp; Bank Nifty</h1>
      <div class="meta">Prepared by Saikumar Kaleru &nbsp;|&nbsp; {date_str} &nbsp;|&nbsp;
        {PERIOD} daily data &nbsp;|&nbsp; long/flat, no leverage, signals act next day.</div>
      {sections}
      <div class="note"><b>Metrics:</b> CAGR = annualised return; Sharpe = return per unit of total
        volatility; Sortino = return per unit of <i>downside</i> volatility; Max DD = worst peak-to-trough
        fall; Profit Factor = gross profit ÷ gross loss; Exposure = % of time invested. Highlighted row is
        passive Buy &amp; Hold. Educational use — past performance does not predict future results.</div>
    </body></html>"""
    hp = os.path.join(OUT, "backtest_report.html")
    pp = os.path.join(OUT, "backtest_report.pdf")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(html)
    chrome = next((p for p in [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        shutil.which("chrome") or "", shutil.which("msedge") or "",
    ] if p and os.path.exists(p)), None)
    if chrome:
        subprocess.run([chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pp}", "file:///" + hp.replace("\\", "/")],
                       check=False, stderr=subprocess.DEVNULL)
        return pp
    return None


# ----------------------------- main -----------------------------------
def main():
    blocks, metric_records = [], []
    for name, ticker in TICKERS.items():
        df = load(ticker)
        # Save the exact daily dataset used (OHLC + the hand-computed indicators) to the input/ folder
        # so the ~6 years of data behind the backtest is visible/auditable, not just downloaded in memory.
        df.to_csv(os.path.join(INP, f"data_{name.replace(' ', '_').lower()}.csv"))
        mkt_ret = df["Close"].pct_change().fillna(0)
        bh_equity = (1 + mkt_ret).cumprod()
        bh = performance(pd.Series(1, index=df.index), mkt_ret, df["Close"])

        print(f"\n=== {name} ===")
        results = {}
        for strat, fn in STRATEGIES.items():
            res = performance(fn(df), mkt_ret, df["Close"])
            results[strat] = res
            results[strat]["_trades_df"] = res.pop("_trades")
            print(f"  {strat:22s} CAGR={res['CAGR %']:6.2f}%  Sharpe={res['Sharpe']:.2f}  "
                  f"MaxDD={res['Max DD %']:6.1f}%  Win={res['Win %']:.0f}%  Trades={res['Trades']}")
            for c in METRIC_COLS:
                pass
            metric_records.append({"Index": name, "Strategy": strat,
                                   **{c: results[strat][c] for c in METRIC_COLS}})
            # trade log
            tl = pd.DataFrame({"trade_return_pct": [t * 100 for t in results[strat]["_trades_df"]]})
            tl.to_csv(os.path.join(OUT, f"trades_{name.replace(' ', '_').lower()}_"
                                        f"{strat.split()[0].lower()}.csv"), index=False)
        print(f"  {'Buy & Hold':22s} CAGR={bh['CAGR %']:6.2f}%  Sharpe={bh['Sharpe']:.2f}  "
              f"MaxDD={bh['Max DD %']:6.1f}%")
        metric_records.append({"Index": name, "Strategy": "Buy & Hold",
                               **{c: bh[c] for c in METRIC_COLS}})

        chart = equity_chart(name, results, bh_equity)
        blocks.append((name, results, chart, bh))

    pd.DataFrame(metric_records).to_csv(os.path.join(OUT, "backtest_results.csv"), index=False)
    date_str = pd.Timestamp.today().strftime("%d %b %Y")
    pdf = build_report(blocks, date_str)
    print(f"\nResults  -> {os.path.join(OUT, 'backtest_results.csv')}")
    print(f"Trade logs -> output/trades_*.csv")
    if pdf:
        print(f"PDF      -> {pdf}")


if __name__ == "__main__":
    main()
