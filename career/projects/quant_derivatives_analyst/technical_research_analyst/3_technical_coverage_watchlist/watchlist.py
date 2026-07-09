"""
Multi-Asset Technical Coverage Watchlist — Equities & Commodities
----------------------------------------------------------------
Screens a sector-grouped universe of NSE large-caps plus commodities and the key
indices, and scores each on a MULTI-TIMEFRAME basis — daily trend + weekly trend
confluence, momentum (RSI, MACD), candlestick read and position vs key levels —
then tags a Buy / Sell / Hold signal with a strength rating (★) and an ATR-based
stop-loss. Outputs a sector-grouped CSV and a styled one-page watchlist (PDF) an
analyst can hand to relationship managers each morning.

Indicators (SMA, RSI, MACD, ATR) and candlestick rules are coded by hand.

Run:  python watchlist.py
"""
import os
import shutil
import subprocess
import numpy as np
import pandas as pd
import yfinance as yf

OUT = os.path.join(os.path.dirname(__file__), "output")
INP = os.path.join(os.path.dirname(__file__), "input")   # the downloaded daily data lands here
os.makedirs(OUT, exist_ok=True)
os.makedirs(INP, exist_ok=True)

# universe grouped by sector
UNIVERSE = {
    "Indices": {"Nifty 50": "^NSEI", "Bank Nifty": "^NSEBANK"},
    "Banking & Financials": {"HDFC Bank": "HDFCBANK.NS", "ICICI Bank": "ICICIBANK.NS",
                             "SBI": "SBIN.NS", "Axis Bank": "AXISBANK.NS",
                             "Kotak Bank": "KOTAKBANK.NS"},
    "IT": {"Infosys": "INFY.NS", "TCS": "TCS.NS", "HCL Tech": "HCLTECH.NS", "Wipro": "WIPRO.NS"},
    "Energy & Materials": {"Reliance": "RELIANCE.NS", "ONGC": "ONGC.NS",
                           "Tata Steel": "TATASTEEL.NS"},
    "Auto & FMCG": {"Maruti": "MARUTI.NS", "M&M": "M&M.NS", "ITC": "ITC.NS",
                    "Hind. Unilever": "HINDUNILVR.NS"},
    "Commodities": {"Gold (COMEX)": "GC=F", "Silver": "SI=F", "Crude Oil (WTI)": "CL=F"},
}


def rsi(s, n=14):
    # RSI measures momentum on a 0-100 scale. Steps:
    d = s.diff()                                  # day-over-day price change
    g = d.clip(lower=0).rolling(n).mean()         # average of UP moves over n days (losses set to 0)
    l = (-d.clip(upper=0)).rolling(n).mean()      # average of DOWN moves over n days (gains set to 0)
    # RS = avg gain / avg loss; RSI = 100 - 100/(1+RS). replace(0, NaN) avoids divide-by-zero.
    # Result is high (toward 100) when gains dominate, low (toward 0) when losses dominate.
    return 100 - 100 / (1 + g / l.replace(0, np.nan))


def trend_of(close):
    # Two moving averages: a fast 20-day and a slow 50-day average of closing price.
    sma20, sma50 = close.rolling(20).mean().iloc[-1], close.rolling(50).mean().iloc[-1]
    last = close.iloc[-1]
    # Up = price is above the 20-MA AND the 20-MA is above the 50-MA (short-term strength
    # stacked over the longer-term average -> healthy uptrend).
    if sma20 > sma50 and last > sma20:
        return "Up"
    # Down = the exact mirror: price below 20-MA and 20-MA below 50-MA -> downtrend.
    if sma20 < sma50 and last < sma20:
        return "Down"
    # Anything else (averages crossed/tangled) = no clear direction -> Sideways.
    return "Sideways"


def candle_signal(df):
    # Read the most recent candle's Open/High/Low/Close, plus the previous day's Open/Close.
    o, h, l, c = (df[x].iloc[-1] for x in ["Open", "High", "Low", "Close"])
    po, pc = df["Open"].iloc[-2], df["Close"].iloc[-2]
    body, rng = abs(c - o), max(h - l, 1e-9)  # body = open-to-close size; rng = full high-low range
    lower_wick = min(o, c) - l                # tail hanging below the body
    upper_wick = h - max(o, c)                # tail sticking above the body
    # Bullish engulfing: yesterday red (pc<po), today green (c>o) and today's body fully
    # swallows yesterday's -> buyers took over. Reversal-up signal.
    if pc < po and c > o and o <= pc and c >= po:
        return "Bull engulf"
    # Bearish engulfing: the mirror -> yesterday green, today red and engulfs it. Reversal-down.
    if pc > po and c < o and o >= pc and c <= po:
        return "Bear engulf"
    # Hammer: tiny body near the top with a long lower wick (>=2x body) -> sellers pushed down
    # but buyers rejected the low. Bullish.
    if body <= 0.3 * rng and lower_wick >= 2 * body:
        return "Hammer"
    # Shooting star: tiny body near the bottom with a long upper wick -> buyers pushed up but
    # got rejected. Bearish.
    if body <= 0.3 * rng and upper_wick >= 2 * body:
        return "Shooting star"
    # Doji: almost no body (open ~= close) -> indecision, neither side won.
    if body <= 0.1 * rng:
        return "Doji"
    return "-"


def score_asset(name, ticker):
    df = yf.download(ticker, period="2y", progress=False, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df[["Open", "High", "Low", "Close"]].dropna()
    if len(df) < 120:
        return None
    # save the exact daily data used for this name so the source is visible/auditable
    df.to_csv(os.path.join(INP, f"data_{name.replace(' ', '_').lower()}.csv"))

    c = df["Close"]
    last = c.iloc[-1]
    daily_trend = trend_of(c)

    # (a) WEEKLY resample for multi-timeframe confluence: roll the daily bars up into
    # weekly candles (week ends Friday) so we can also read the bigger-picture weekly trend.
    # A daily AND weekly trend that agree is a higher-conviction setup than daily alone.
    wk = df.resample("W-FRI").agg({"Open": "first", "High": "max",
                                   "Low": "min", "Close": "last"}).dropna()
    weekly_trend = trend_of(wk["Close"]) if len(wk) >= 50 else "n/a"

    r = rsi(c).iloc[-1]
    # MACD = difference of a fast (12) and slow (26) exponential moving average; the signal
    # line is a 9-period EMA of MACD. MACD above signal = bullish momentum, below = bearish.
    macd = c.ewm(span=12, adjust=False).mean() - c.ewm(span=26, adjust=False).mean()
    macd_line, macd_sig = macd.iloc[-1], macd.ewm(span=9, adjust=False).mean().iloc[-1]
    # (b) ATR (Average True Range) = average daily price travel, used to size the stop.
    # True Range = the largest of: today's high-low, |high - prev close|, |low - prev close|,
    # so it accounts for overnight gaps. ATR is the 14-day average of that.
    tr = pd.concat([df["High"] - df["Low"], (df["High"] - c.shift()).abs(),
                    (df["Low"] - c.shift()).abs()], axis=1).max(axis=1)
    atr = tr.rolling(14).mean().iloc[-1]
    pattern = candle_signal(df)

    # (c) COMPOSITE SCORE: start at 0 and let each factor vote +1 (bullish) or -1 (bearish).
    # Range is -6..+6. Six factors: daily trend, weekly trend, MACD cross, price vs 50-MA,
    # RSI extremes, candlestick read.
    score = 0
    score += {"Up": 1, "Sideways": 0, "Down": -1}[daily_trend]            # daily trend vote
    score += {"Up": 1, "Sideways": 0, "Down": -1, "n/a": 0}[weekly_trend]  # weekly trend vote
    score += 1 if macd_line > macd_sig else -1                            # MACD momentum vote
    score += 1 if last > c.rolling(50).mean().iloc[-1] else -1            # price above/below 50-MA
    if r > 70:        # RSI overbought -> a bearish vote
        score -= 1
    elif r < 30:      # RSI oversold -> a bullish vote
        score += 1
    if pattern in ("Bull engulf", "Hammer"):        # bullish candle -> +1
        score += 1
    elif pattern in ("Bear engulf", "Shooting star"):  # bearish candle -> -1
        score -= 1

    # Thresholds: clearly net-bullish (>=2) -> BUY, clearly net-bearish (<=-2) -> SELL,
    # anything in between (mixed signals, no edge) -> HOLD.
    signal = "BUY" if score >= 2 else "SELL" if score <= -2 else "HOLD"
    # (d) GUARDRAIL: don't SELL something already deeply oversold (RSI<25, likely to bounce),
    # and don't chase a BUY that's already very overbought (RSI>80, likely to pull back).
    if signal == "SELL" and r < 25:
        signal = "HOLD"
    elif signal == "BUY" and r > 80:
        signal = "HOLD"

    # (e) ★ STRENGTH: how strongly the factors align. Bigger |score| = more filled stars
    # (capped at 3); the rest show as hollow ☆.
    stars = "★" * min(3, abs(score)) + "☆" * (3 - min(3, abs(score)))
    # (f) ATR-BASED STOP: place the stop 1.5x ATR away from price -- below for a BUY, above for
    # a SELL -- so the stop is sized to the asset's own volatility. HOLDs get no stop (NaN).
    stop = (last - 1.5 * atr if signal == "BUY"
            else last + 1.5 * atr if signal == "SELL" else np.nan)

    return {
        "Asset": name, "Last": round(last, 1), "Daily": daily_trend, "Weekly": weekly_trend,
        "RSI": int(round(r)), "MACD": "Bull" if macd_line > macd_sig else "Bear",
        "Candle": pattern, "Signal": signal, "Strength": stars,
        "Stop-loss": round(stop, 1) if not np.isnan(stop) else "-", "_score": score,
    }


def to_pdf(by_sector, counts):
    colour = {"BUY": "#1a7f37", "SELL": "#c0392b", "HOLD": "#b8860b"}
    cols = ["Asset", "Last", "Daily", "Weekly", "RSI", "MACD", "Candle", "Strength"]
    sections = ""
    for sector, rows in by_sector.items():
        body = ""
        for x in rows:
            badge = (f"<span style='color:#fff;background:{colour[x['Signal']]};padding:1px 7px;"
                     f"border-radius:3px;font-weight:700'>{x['Signal']}</span>")
            cells = "".join(f"<td>{x[k]}</td>" for k in cols)
            body += f"<tr>{cells}<td>{badge}</td><td>{x['Stop-loss']}</td></tr>"
        sections += f"""<tr class="sec"><td colspan="10">{sector}</td></tr>{body}"""

    summary = (f"<b style='color:#1a7f37'>{counts['BUY']} Buy</b> &nbsp; "
               f"<b style='color:#c0392b'>{counts['SELL']} Sell</b> &nbsp; "
               f"<b style='color:#b8860b'>{counts['HOLD']} Hold</b>")
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
      @page {{ size: A4; margin: 12mm 13mm; }}
      body {{ font-family:"Calibri","Segoe UI",sans-serif; color:#1a1a1a; }}
      h1 {{ color:#16365c; font-size:15pt; margin-bottom:2px; }}
      .meta {{ color:#555; font-size:9pt; margin-bottom:4px; }}
      .summary {{ font-size:10pt; margin-bottom:10px; }}
      table {{ border-collapse:collapse; width:100%; font-size:9pt; }}
      th {{ background:#16365c; color:#fff; text-align:left; padding:5px 7px; }}
      td {{ padding:4px 7px; border-bottom:1px solid #e7ebf1; }}
      tr.sec td {{ background:#e8eef6; color:#16365c; font-weight:700; font-size:9.2pt;
                   text-transform:uppercase; letter-spacing:0.5px; padding:5px 7px; }}
      .note {{ color:#666; font-size:8.3pt; margin-top:10px; }}
    </style></head><body>
      <h1>Technical Coverage Watchlist — Equities &amp; Commodities</h1>
      <div class="meta">Prepared by Saikumar Kaleru &nbsp;|&nbsp; {pd.Timestamp.today():%d %b %Y}
        &nbsp;|&nbsp; multi-timeframe (daily + weekly) &nbsp;|&nbsp; for study/educational use — not investment advice.</div>
      <div class="summary">Coverage: {summary}</div>
      <table>
        <tr><th>Asset</th><th>Last</th><th>Daily</th><th>Weekly</th><th>RSI</th><th>MACD</th>
            <th>Candle</th><th>Strength</th><th>Signal</th><th>Stop-loss</th></tr>
        {sections}
      </table>
      <div class="note"><b>Signal logic:</b> a composite score across daily trend, weekly trend
        (multi-timeframe confluence), MACD cross, price-vs-50MA, RSI extremes and candlestick read.
        Strength ★ reflects how many factors align. Stops sized to 1.5x ATR. Deeply overbought/oversold
        names are held rather than chased. Sorted by conviction within each sector.</div>
    </body></html>"""
    hp, pp = os.path.join(OUT, "watchlist.html"), os.path.join(OUT, "watchlist.pdf")
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


def main():
    by_sector, all_rows = {}, []
    for sector, names in UNIVERSE.items():
        rows = []
        for name, ticker in names.items():
            try:
                r = score_asset(name, ticker)
            except Exception:
                r = None
            if r:
                rows.append(r)
                print(f"  {sector[:12]:12s} {name:16s} {r['Signal']:4s} "
                      f"D:{r['Daily']:8s} W:{r['Weekly']:8s} RSI={r['RSI']:>3} {r['Candle']}")
        rows.sort(key=lambda x: -x["_score"])
        by_sector[sector] = rows
        all_rows += rows

    counts = {s: sum(1 for r in all_rows if r["Signal"] == s) for s in ["BUY", "SELL", "HOLD"]}
    pd.DataFrame([{k: v for k, v in r.items() if k != "_score"} for r in all_rows]).to_csv(
        os.path.join(OUT, "watchlist.csv"), index=False)
    pdf = to_pdf(by_sector, counts)
    print(f"\n  {counts['BUY']} Buy / {counts['SELL']} Sell / {counts['HOLD']} Hold")
    print(f"CSV -> {os.path.join(OUT, 'watchlist.csv')}")
    if pdf:
        print(f"PDF -> {pdf}")


if __name__ == "__main__":
    main()
