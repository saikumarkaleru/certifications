"""
Technical Research Reports — Nifty, Bank Nifty & Commodities
-----------------------------------------------------------
Generates Daily, Weekly and Monthly technical research notes for Nifty 50,
Bank Nifty, Gold and Crude Oil. For each asset it computes support/resistance,
Fibonacci retracement, Bollinger Bands, RSI, MACD and ATR, then derives a
Buy / Sell / Hold view with entry, target and a volatility-sized stop-loss, plus
an annotated chart. Stops are 1.5x ATR; targets 2.5x ATR; extremely overbought/
oversold tapes are stepped aside to HOLD rather than chased.

Run:
  python generate_report.py            -> builds daily, weekly AND monthly
  python generate_report.py weekly     -> builds only that timeframe
"""
import os
import sys
import base64
import shutil
import subprocess
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = os.path.join(os.path.dirname(__file__), "output")
INP = os.path.join(os.path.dirname(__file__), "input")   # the downloaded daily/weekly/monthly data lands here
os.makedirs(OUT, exist_ok=True)
os.makedirs(INP, exist_ok=True)

ASSETS = {
    "Nifty 50": "^NSEI",
    "Bank Nifty": "^NSEBANK",
    "Gold (COMEX)": "GC=F",
    "Crude Oil (WTI)": "CL=F",
}

# per-timeframe configuration
TF = {
    "daily":   {"rule": None,    "period": "1y",  "swing": 60, "plot": 130, "cadence": "Daily"},
    "weekly":  {"rule": "W-FRI", "period": "5y",  "swing": 52, "plot": 120, "cadence": "Weekly"},
    "monthly": {"rule": "ME",    "period": "11y", "swing": 24, "plot": 96,  "cadence": "Monthly"},
}

# Weights for the confidence-weighted signal (sum to 1.0). Trend and momentum dominate; mean-reversion
# and market-structure are smaller, contrarian counter-weights. Each category votes in [-1, +1].
WEIGHTS = {"Trend": 0.40, "Momentum": 0.25, "Volatility": 0.15, "Mean-Reversion": 0.10, "Structure": 0.10}


def _clip(x):
    """Keep a sub-score within [-1, +1] (fully bearish .. fully bullish)."""
    return max(-1.0, min(1.0, x))


def rsi(series, n=14):
    # RSI (Relative Strength Index) measures momentum on a 0-100 scale.
    delta = series.diff()                             # day-over-day price change (+ up, - down)
    gain = delta.clip(lower=0).rolling(n).mean()      # average of UP moves over n bars (down days = 0)
    loss = (-delta.clip(upper=0)).rolling(n).mean()   # average of DOWN moves over n bars (up days = 0)
    rs = gain / loss.replace(0, np.nan)               # RS = avg gain / avg loss (avoid divide-by-zero)
    return 100 - (100 / (1 + rs))                     # squash RS into 0-100; >70 = overbought, <30 = oversold


def get_vix():
    """India VIX — the market's 'fear gauge'. Returns the current level + a plain-English read (None on failure)."""
    try:
        v = yf.download("^INDIAVIX", period="1mo", progress=False, auto_adjust=True)
        if isinstance(v.columns, pd.MultiIndex):
            v.columns = v.columns.get_level_values(0)
        last = float(v["Close"].dropna().iloc[-1])
        read = "low (complacent)" if last < 13 else "elevated (nervous)" if last > 20 else "moderate"
        return {"level": last, "read": read}
    except Exception:
        return None


def narrative(a, cadence):
    """Rule-based (TEMPLATED) prose summary — built from the indicator values, NOT AI-generated.
    Turns the numbers into the kind of sentence a human analyst would write."""
    above20 = "above" if a["last"] > a["sma20"] else "below"
    above50 = "above" if a["last"] > a["sma50"] else "below"
    trend = ("a constructive uptrend" if a["last"] > a["sma20"] > a["sma50"]
             else "a developing downtrend" if a["last"] < a["sma20"] < a["sma50"]
             else "a mixed, range-bound structure")
    rstate = ("overbought territory" if a["rsi"] > 70 else "oversold territory" if a["rsi"] < 30
              else "neutral territory")
    macd = "positive" if a["macd_line"] > a["macd_sig"] else "negative"
    if a["view"] == "HOLD" and a["confidence"] >= 20:
        # a directional signal existed (confidence past the threshold) but the guardrail overrode it
        action = (f'A directional signal was present ({a["confidence"]}%), but the overbought/oversold '
                  f'guardrail holds the stance at HOLD; watch the {a["support"]:,.0f}–{a["resistance"]:,.0f} range.')
    elif a["view"] == "HOLD":
        action = (f'With no decisive edge ({a["confidence"]}% conviction), the stance is HOLD; watch the '
                  f'{a["support"]:,.0f}–{a["resistance"]:,.0f} range and act on a clear break either side.')
    else:
        action = (f'On balance this skews to a {a["view"]} ({a["confidence"]}% conviction): entry near '
                  f'{a["entry"]:,.0f}, target {a["target"]:,.0f}, stop {a["stop"]:,.0f}.')
    return (f'{a["name"]} is trading at {a["last"]:,.0f}, {above20} its 20-period MA and {above50} the '
            f'50-period MA, indicating {trend} on the {cadence.lower()} timeframe. RSI at {a["rsi"]:.0f} sits in '
            f'{rstate} while MACD momentum is {macd}. {action}')


def load(ticker, tf):
    cfg = TF[tf]
    df = yf.download(ticker, period=cfg["period"], progress=False, auto_adjust=True)  # pull price history
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)   # flatten yfinance's 2-level column headers
    df = df[["Open", "High", "Low", "Close"]].dropna()  # keep OHLC candles, drop missing rows
    if cfg["rule"]:
        # yfinance only gives DAILY candles. For weekly/monthly we "resample": group the daily bars
        # into buckets (W-FRI = week ending Friday, ME = month-end) and rebuild one bigger candle per
        # bucket -> Open = first day's open, High = highest high, Low = lowest low, Close = last day's close.
        df = df.resample(cfg["rule"]).agg(
            {"Open": "first", "High": "max", "Low": "min", "Close": "last"}).dropna()
    return df


def analyse(name, df, tf):
    cfg = TF[tf]
    close = df["Close"]
    last = close.iloc[-1]              # most recent close = the price we judge everything against

    # --- (a) indicators measured on the LAST bar (.iloc[-1] = newest value) ---
    sma20 = close.rolling(20).mean().iloc[-1]   # 20-period simple moving average (short trend)
    sma50 = close.rolling(50).mean().iloc[-1]   # 50-period simple moving average (longer trend)
    std20 = close.rolling(20).std().iloc[-1]    # 20-period volatility (standard deviation)
    # Bollinger Bands = the 20-MA +/- 2 standard deviations (a "normal" price envelope)
    bb_upper, bb_lower = sma20 + 2 * std20, sma20 - 2 * std20

    r = rsi(close).iloc[-1]                      # latest RSI momentum reading
    # MACD = difference between a fast (12) and slow (26) exponential moving average;
    # the "signal" line is a 9-period EMA of MACD. MACD above signal = bullish momentum.
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    macd_line = (ema12 - ema26).iloc[-1]
    macd_sig = (ema12 - ema26).ewm(span=9, adjust=False).mean().iloc[-1]

    # --- (b) swing high/low over the last N bars -> support, resistance, Fibonacci ---
    win = close.iloc[-cfg["swing"]:]            # window of the most recent N closes
    swing_high, swing_low = win.max(), win.min()  # highest/lowest price in that window
    diff = swing_high - swing_low               # the full size of the swing
    # Fibonacci retracements: common levels (23.6/38.2/50/61.8%) inside the swing where price often
    # pauses or reverses. Measured DOWN from the swing high, so 0.236 sits near the top, 0.618 near the bottom.
    fib = {
        "0.236": swing_high - 0.236 * diff,
        "0.382": swing_high - 0.382 * diff,
        "0.5": swing_high - 0.5 * diff,
        "0.618": swing_high - 0.618 * diff,
    }
    support, resistance = swing_low, swing_high  # floor = swing low, ceiling = swing high

    # --- (c) Average True Range (14): typical bar size = how volatile the asset is ---
    # True Range per bar = the largest of: (high-low), |high-prev close|, |low-prev close|.
    # The .shift() pulls the PREVIOUS close so gaps between bars are counted too.
    tr = pd.concat([
        df["High"] - df["Low"],
        (df["High"] - df["Close"].shift()).abs(),
        (df["Low"] - df["Close"].shift()).abs(),
    ], axis=1).max(axis=1)
    atr = tr.rolling(14).mean().iloc[-1]        # ATR = 14-bar average of those true ranges

    # --- (d) CONFIDENCE-WEIGHTED SCORE: five categories each vote in [-1, +1] (bearish .. bullish),
    #         combined by WEIGHTS into a net signal (-1..+1) and a 0-100% confidence. ---
    rng = resistance - support
    cats = {
        # Trend: price vs the 20-MA, and the 20-MA vs the 50-MA
        "Trend": _clip(((1 if last > sma20 else -1) + (1 if sma20 > sma50 else -1)) / 2),
        # Momentum: the MACD cross, plus how far RSI is above/below the 50 mid-line
        "Momentum": _clip(((1 if macd_line > macd_sig else -1) + _clip((r - 50) / 20)) / 2),
        # Volatility/position: where price sits inside the Bollinger band envelope (breakout direction)
        "Volatility": _clip((last - sma20) / (2 * std20)) if std20 else 0.0,
        # Mean-reversion (contrarian): oversold leans bullish, overbought leans bearish
        "Mean-Reversion": _clip((50 - r) / 30),
        # Market structure: near support = bullish (room to rise), near resistance = bearish
        "Structure": _clip(1 - 2 * (last - support) / rng) if rng else 0.0,
    }
    net = sum(WEIGHTS[k] * cats[k] for k in WEIGHTS)   # weighted net signal in [-1, +1]
    confidence = round(abs(net) * 100)                 # 0-100% conviction in the call
    view = "BUY" if net >= 0.20 else "SELL" if net <= -0.20 else "HOLD"
    # --- (e) guardrail: don't short a deeply oversold tape, don't chase an extremely overbought one ---
    if view == "SELL" and r < 25:
        view = "HOLD"                           # too oversold to safely short -> step aside
    elif view == "BUY" and r > 80:
        view = "HOLD"                           # too overbought to safely chase -> step aside

    # --- (f) risk levels sized to volatility: stop = 1.5x ATR away, target = 2.5x ATR away ---
    if view == "BUY":
        stop, target = last - 1.5 * atr, last + 2.5 * atr  # buy: stop below, target above
    elif view == "SELL":
        stop, target = last + 1.5 * atr, last - 2.5 * atr  # sell: stop above, target below
    else:
        stop, target = None, None   # HOLD = no active trade, so no stop/target; show the watch-range instead

    chart = plot(name, df, support, resistance, fib, tf)
    a = {
        "name": name, "last": last, "sma20": sma20, "sma50": sma50,
        "bb_upper": bb_upper, "bb_lower": bb_lower, "rsi": r,
        "macd_line": macd_line, "macd_sig": macd_sig,
        "support": support, "resistance": resistance, "fib": fib,
        "atr": atr, "view": view, "confidence": confidence, "cats": cats,
        "entry": last, "target": target, "stop": stop, "chart": chart,
    }
    a["narrative"] = narrative(a, cfg["cadence"])   # rule-based prose summary built from the above
    return a


def plot(name, df, support, resistance, fib, tf):
    """Render a clean candlestick chart: candles + 20/50-MA + shaded support/resistance + Fibonacci."""
    cfg = TF[tf]
    d = df.iloc[-cfg["plot"]:]
    o, h, l, c = d["Open"], d["High"], d["Low"], d["Close"]
    sma20 = df["Close"].rolling(20).mean().iloc[-cfg["plot"]:]
    sma50 = df["Close"].rolling(50).mean().iloc[-cfg["plot"]:]
    x = np.arange(len(d))
    span = max(h.max() - l.min(), 1e-6)

    fig, ax = plt.subplots(figsize=(10, 4.3))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("#fbfcfe")
    # candle wicks + bodies (green up, red down)
    ax.vlines(x, l, h, color="#8a96a5", linewidth=0.6, zorder=1)
    for i in range(len(d)):
        oi, ci = o.iloc[i], c.iloc[i]
        col = "#1a9850" if ci >= oi else "#d73027"
        ax.add_patch(Rectangle((x[i] - 0.32, min(oi, ci)), 0.64,
                               max(abs(ci - oi), span * 0.001), color=col, ec=col, lw=0.3, zorder=2))
    # moving averages
    ax.plot(x, sma20.values, color="#1f4e79", lw=1.2, label="20-MA", zorder=3)
    ax.plot(x, sma50.values, color="#e08214", lw=1.2, label="50-MA", zorder=3)
    # shaded support / resistance zones
    band = span * 0.012
    ax.axhspan(support - band, support + band, color="#1a9850", alpha=0.12, zorder=0)
    ax.axhspan(resistance - band, resistance + band, color="#d73027", alpha=0.12, zorder=0)
    ax.axhline(support, color="#1a9850", ls="--", lw=1.1, zorder=3)
    ax.axhline(resistance, color="#d73027", ls="--", lw=1.1, zorder=3)
    ax.text(0.3, resistance, f" Resistance {resistance:,.0f}", color="#a5170f", fontsize=8,
            va="bottom", fontweight="bold")
    ax.text(0.3, support, f" Support {support:,.0f}", color="#0d6b2e", fontsize=8,
            va="bottom", fontweight="bold")
    # Fibonacci retracements (subtle)
    for k, v in fib.items():
        ax.axhline(v, color="#c2c8d2", ls=":", lw=0.6, zorder=0)
        ax.text(len(d) - 0.5, v, f"{k}", color="#9aa3b0", fontsize=6.5, va="center", ha="right")
    ax.set_title(f"{name} — {cfg['cadence']} candles with 20/50-MA, support/resistance & Fibonacci",
                 fontsize=10.5, fontweight="bold", color="#16365c", loc="left")
    ax.legend(loc="upper left", fontsize=7.5, framealpha=0.9, ncol=2)
    ax.grid(axis="y", alpha=0.16); ax.set_xticks([]); ax.margins(x=0.01)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color("#d6dce5")
    ax.tick_params(labelsize=8, colors="#555")
    path = os.path.join(OUT, f"{name.replace(' ', '_').lower()}_{tf}_chart.png")
    plt.tight_layout()
    plt.savefig(path, dpi=135)
    plt.close()
    return path


def _img_b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


def html_section(a):
    colour = {"BUY": "#1a7f37", "SELL": "#c0392b", "HOLD": "#b8860b"}[a["view"]]
    fib_rows = "".join(
        f"<tr><td>Fib {k}</td><td>{v:,.0f}</td></tr>" for k, v in a["fib"].items())
    rsi_state = "overbought" if a["rsi"] > 70 else "oversold" if a["rsi"] < 30 else "neutral"
    macd_state = "bullish" if a["macd_line"] > a["macd_sig"] else "bearish"
    cat_bars = " &nbsp;·&nbsp; ".join(
        f"{k} {'+' if v >= 0 else ''}{v:.2f}" for k, v in a["cats"].items())
    if a["view"] == "HOLD":
        call = (f'No active trade &mdash; watch range <b>{a["support"]:,.0f}</b> to '
                f'<b>{a["resistance"]:,.0f}</b>; act on a clear break either side.')
    else:
        rr = abs(a["target"] - a["entry"]) / abs(a["entry"] - a["stop"])
        call = (f'Entry <b>{a["entry"]:,.0f}</b> &nbsp;|&nbsp; Target <b>{a["target"]:,.0f}</b> '
                f'&nbsp;|&nbsp; Stop-loss <b>{a["stop"]:,.0f}</b> &nbsp;|&nbsp; R:R <b>{rr:.1f}:1</b>')
    return f"""
    <div class="card" style="border-left:5px solid {colour}">
      <div class="card-head">
        <h2>{a['name']}</h2>
        <span class="badge" style="background:{colour}">{a['view']}</span>
      </div>
      <div class="call">{call}</div>
      <div class="confwrap"><span class="conflabel">Confidence</span><span class="confbar"><span class="conffill" style="width:{a['confidence']}%;background:{colour}"></span></span><span class="confpct">{a['confidence']}%</span> &nbsp;<span class="cats">{cat_bars}</span></div>
      <div class="narr"><b>Summary</b> <span class="tag">auto-generated &middot; rule-based</span> &mdash; {a['narrative']}</div>
      <div class="grid">
        <table>
          <tr><td>Last price</td><td>{a['last']:,.0f}</td></tr>
          <tr><td>20-period MA</td><td>{a['sma20']:,.0f}</td></tr>
          <tr><td>50-period MA</td><td>{a['sma50']:,.0f}</td></tr>
          <tr><td>RSI(14)</td><td>{a['rsi']:.1f} ({rsi_state})</td></tr>
          <tr><td>MACD</td><td>{macd_state}</td></tr>
          <tr><td>ATR(14)</td><td>{a['atr']:,.1f}</td></tr>
        </table>
        <table>
          <tr><td>Resistance</td><td>{a['resistance']:,.0f}</td></tr>
          <tr><td>Support</td><td>{a['support']:,.0f}</td></tr>
          <tr><td>Bollinger upper</td><td>{a['bb_upper']:,.0f}</td></tr>
          <tr><td>Bollinger lower</td><td>{a['bb_lower']:,.0f}</td></tr>
          {fib_rows}
        </table>
      </div>
      <img class="chart" src="{_img_b64(a['chart'])}"/>
    </div>"""


def render_pdf(analyses, tf, date_str, vix=None):
    cfg = TF[tf]
    cards = "".join(html_section(a) for a in analyses)
    vix_html = (f" &nbsp;|&nbsp; India VIX <b>{vix['level']:.2f}</b> ({vix['read']})" if vix else "")
    pill = {"BUY": "#1a7f37", "SELL": "#c0392b", "HOLD": "#b8860b"}
    summary_rows = "".join(
        f"<tr><td class='nm'>{a['name']}</td>"
        f"<td><span class='pill' style='background:{pill[a['view']]}'>{a['view']}</span></td>"
        f"<td>{a['confidence']}%</td><td>{a['last']:,.0f}</td>"
        f"<td>{a['support']:,.0f}</td><td>{a['resistance']:,.0f}</td></tr>" for a in analyses)
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
      @page {{ size: A4; margin: 11mm 13mm; }}
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{ font-family: "Calibri","Segoe UI",sans-serif; color: #1a1a1a; font-size: 10pt; }}
      .topbar {{ background: #16365c; color: #fff; padding: 11px 16px; border-radius: 6px; margin-bottom: 12px; }}
      .topbar .brand {{ font-size: 8.5pt; letter-spacing: 2.5px; color: #aebfd6; font-weight: 700; }}
      .topbar h1 {{ font-size: 16pt; margin: 1px 0 3px; font-weight: 700; }}
      .topbar .meta {{ color: #d6deeb; font-size: 8.8pt; }}
      .snap-h {{ color: #16365c; font-size: 11pt; font-weight: 700; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.5px; }}
      .snaptbl {{ width: 100%; border-collapse: collapse; font-size: 9.3pt; margin-bottom: 12px; }}
      .snaptbl th {{ background: #16365c; color: #fff; text-align: right; padding: 4px 9px; font-weight: 600; }}
      .snaptbl th:first-child {{ text-align: left; }}
      .snaptbl td {{ padding: 4px 9px; border-bottom: 1px solid #e6eaf0; text-align: right; }}
      .snaptbl td.nm {{ text-align: left; font-weight: 600; color: #16365c; }}
      .pill {{ color: #fff; font-weight: 700; font-size: 8.4pt; padding: 1px 9px; border-radius: 9px; }}
      .disclaimer {{ font-style: italic; color: #888; font-size: 8.2pt; margin-bottom: 12px; }}
      .card {{ border: 1px solid #dde3ec; border-radius: 6px; padding: 11px 13px; margin-bottom: 13px;
               page-break-inside: avoid; box-shadow: 0 1px 2px rgba(20,48,92,0.06); }}
      .card-head {{ display: flex; justify-content: space-between; align-items: center; }}
      .card-head h2 {{ color: #16365c; font-size: 13pt; }}
      .badge {{ color: #fff; font-weight: 700; font-size: 11pt; padding: 2px 14px; border-radius: 4px; letter-spacing: 1px; }}
      .call {{ margin: 6px 0 5px; font-size: 10.5pt; }}
      .confwrap {{ display: flex; align-items: center; gap: 6px; font-size: 8.6pt; color: #555; margin-bottom: 6px; }}
      .conflabel {{ color: #16365c; font-weight: 600; }}
      .confbar {{ display: inline-block; width: 120px; height: 8px; background: #e7ebf1; border-radius: 5px; overflow: hidden; }}
      .conffill {{ display: block; height: 100%; border-radius: 5px; }}
      .confpct {{ font-weight: 700; color: #333; }}
      .confwrap .cats {{ color: #9aa3b0; font-size: 8pt; }}
      .narr {{ font-size: 9.2pt; color: #2a2a2a; background: #f4f7fb; border-left: 3px solid #16365c;
               padding: 6px 10px; margin: 4px 0 9px; border-radius: 0 3px 3px 0; }}
      .narr .tag {{ font-size: 7.4pt; color: #fff; background: #8a93a3; padding: 0 5px; border-radius: 3px;
                    text-transform: uppercase; letter-spacing: 0.4px; vertical-align: middle; }}
      .grid {{ display: flex; gap: 26px; margin-bottom: 8px; }}
      table {{ border-collapse: collapse; font-size: 9.2pt; }}
      td {{ padding: 1.5px 10px 1.5px 0; }}
      .grid td:first-child {{ color: #555; }}
      .grid td:last-child {{ font-weight: 600; text-align: right; }}
      .chart {{ width: 100%; border: 1px solid #e8ecf2; border-radius: 4px; margin-top: 4px; }}
      .method {{ font-size: 8.4pt; color: #666; border-top: 1px solid #ddd; padding-top: 6px; }}
    </style></head><body>
      <div class="topbar">
        <div class="brand">{cfg['cadence'].upper()} &middot; TECHNICAL RESEARCH</div>
        <h1>Nifty 50 &middot; Bank Nifty &middot; Gold &middot; Crude Oil</h1>
        <div class="meta">Prepared by Saikumar Kaleru &nbsp;|&nbsp; {date_str} &nbsp;|&nbsp; {cfg['cadence']} timeframe{vix_html}</div>
      </div>
      <div class="snap-h">Market Snapshot</div>
      <table class="snaptbl">
        <tr><th>Instrument</th><th>View</th><th>Confidence</th><th>Last</th><th>Support</th><th>Resistance</th></tr>
        {summary_rows}
      </table>
      <div class="disclaimer">Technical view from price action, moving averages, RSI, MACD, Bollinger Bands,
        ATR and Fibonacci retracement. For study/educational use &mdash; not investment advice.</div>
      {cards}
      <div class="method"><b>Method:</b> The Buy/Sell/Hold view is a <b>confidence-weighted score</b> across
        five categories &mdash; Trend (40%), Momentum (25%), Volatility (15%), Mean-Reversion (10%) and
        Structure (10%) &mdash; each voting in [&minus;1,+1]; the weighted net gives the direction and the %
        confidence. Stops/targets are sized to volatility (1.5x / 2.5x ATR); extremely overbought/oversold
        tapes are stepped aside to HOLD. The per-asset <b>Summary is auto-generated from the indicators by a
        rule-based template</b> (not AI).</div>
    </body></html>"""

    html_path = os.path.join(OUT, f"research_report_{tf}.html")
    pdf_path = os.path.join(OUT, f"research_report_{tf}.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    chrome = next((p for p in [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        shutil.which("chrome") or "", shutil.which("msedge") or "",
    ] if p and os.path.exists(p)), None)
    if not chrome:
        print("  (Chrome not found - open the HTML and Print to PDF manually)")
        return None
    subprocess.run([chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf_path}", "file:///" + html_path.replace("\\", "/")],
                   check=False, stderr=subprocess.DEVNULL)
    return pdf_path


def run(tf):
    date_str = pd.Timestamp.today().strftime("%d %b %Y")
    vix = get_vix()                       # India VIX (fear gauge) — shown in the report header
    analyses = []
    for name, ticker in ASSETS.items():
        df = load(ticker, tf)
        # save the exact data used for this asset/timeframe so the source is visible/auditable
        df.to_csv(os.path.join(INP, f"data_{name.replace(' ', '_').lower()}_{tf}.csv"))
        analyses.append(analyse(name, df, tf))
    pdf = render_pdf(analyses, tf, date_str, vix)
    print(f"\n=== {TF[tf]['cadence']} Technical Research Report ===")
    if vix:
        print(f"  India VIX: {vix['level']:.2f} ({vix['read']})")
    for a in analyses:
        if a["view"] == "HOLD":
            print(f"  {a['name']:16s}: HOLD ({a['confidence']:>2}%)  last={a['last']:,.0f}  RSI={a['rsi']:.0f}  "
                  f"(no trade; range {a['support']:,.0f}-{a['resistance']:,.0f})")
        else:
            print(f"  {a['name']:16s}: {a['view']:4s} ({a['confidence']:>2}%)  last={a['last']:,.0f}  "
                  f"RSI={a['rsi']:.0f}  target={a['target']:,.0f}  stop={a['stop']:,.0f}")
    if pdf:
        print(f"  PDF -> {pdf}")


def main():
    timeframes = [sys.argv[1]] if len(sys.argv) > 1 else ["daily", "weekly", "monthly"]
    for tf in timeframes:
        if tf not in TF:
            print(f"Unknown timeframe '{tf}'. Use daily | weekly | monthly.")
            continue
        run(tf)


if __name__ == "__main__":
    main()
