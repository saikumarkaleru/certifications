"""
Generate the FULL set of teaching diagrams for the illustrated handbook:
chart patterns, option payoffs, divergence, Dow cycle, indicators, etc.
Saves PNGs into ./img (alongside the 10 core images).
"""
import os
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

IMG = os.path.join(os.path.dirname(__file__), "img")
os.makedirs(IMG, exist_ok=True)
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.25})
GREEN, RED, BLUE, AMBER = "#1a9850", "#d73027", "#1f4e79", "#b8860b"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(IMG, name), dpi=130, bbox_inches="tight")
    plt.close(fig)
    print("  ->", name)


def box(ax, text, xy=(0.015, 0.04), fc="#eef5ff"):
    ax.text(xy[0], xy[1], text, transform=ax.transAxes, fontsize=9,
            bbox=dict(boxstyle="round", fc=fc), va="bottom")


# ===================== PART 1 =====================
def chart_types():
    df = load("^NSEI", "6mo")
    c = df["Close"]
    fig, axes = plt.subplots(1, 3, figsize=(13, 4))
    axes[0].plot(c.index, c.values, color=BLUE); axes[0].set_title("LINE chart\n(just closes — clean)")
    # bar (OHLC)
    ax = axes[1]
    sub = df.iloc[-30:]
    for i, (_, r) in enumerate(sub.iterrows()):
        col = GREEN if r.Close >= r.Open else RED
        ax.plot([i, i], [r.Low, r.High], color=col, lw=1)
        ax.plot([i - 0.3, i], [r.Open, r.Open], color=col, lw=1)
        ax.plot([i, i + 0.3], [r.Close, r.Close], color=col, lw=1)
    ax.set_title("BAR chart (OHLC)\nopen-high-low-close")
    # candle
    ax = axes[2]
    for i, (_, r) in enumerate(sub.iterrows()):
        col = GREEN if r.Close >= r.Open else RED
        ax.plot([i, i], [r.Low, r.High], color="black", lw=0.8)
        ax.add_patch(Rectangle((i - 0.3, min(r.Open, r.Close)), 0.6,
                     max(abs(r.Close - r.Open), 1), color=col))
    ax.set_title("CANDLESTICK\nthe global standard")
    fig.suptitle("Three ways to draw the same price", fontweight="bold", y=1.03)
    save(fig, "p1_charttypes.png")


def dow_cycle():
    x = np.linspace(0, 12, 400)
    y = (np.sin(x - 1.6) * 1.5 + x * 0.0 + 10
         + np.where(x < 6, x * 0.7, (12 - x) * 0.7))
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(x, y, color=BLUE, lw=2)
    phases = [(1.5, "ACCUMULATION\n(smart money buys quietly)", GREEN),
              (4.2, "MARK-UP\n(public joins, biggest rally)", GREEN),
              (7.5, "DISTRIBUTION\n(smart money sells)", RED),
              (10, "MARK-DOWN\n(decline)", RED)]
    for xpos, label, col in phases:
        ax.axvline(xpos, color=col, ls=":", alpha=0.5)
        ax.text(xpos, ax.get_ylim()[1] * 0.0 + 8.2, label, fontsize=8.5, ha="center",
                color=col, bbox=dict(boxstyle="round", fc="white", ec=col))
    ax.set_title("The Market Cycle (Dow / Wyckoff) — every trend has 4 phases",
                 fontweight="bold")
    ax.set_xticks([]); ax.set_ylabel("Price")
    save(fig, "p1_cycle.png")


def timeframes():
    df = load("^NSEI", "1y"); c = df["Close"]
    wk = c.resample("W-FRI").last()
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.3))
    axes[0].plot(wk.index, wk.values, color=BLUE, lw=1.6)
    axes[0].set_title("HIGHER timeframe (weekly)\n= the BIG trend / context", fontweight="bold")
    axes[1].plot(c.index[-60:], c.values[-60:], color=BLUE, lw=1.2)
    axes[1].set_title("LOWER timeframe (daily)\n= time your ENTRY", fontweight="bold")
    save(fig, "p1_timeframes.png")


# ===================== PART 2: chart patterns =====================
def head_shoulders():
    x = np.arange(11)
    y = np.array([10, 12, 11, 15, 12, 19, 12, 15, 11, 12, 8])
    fig, ax = plt.subplots(figsize=(8.5, 5))
    ax.plot(x, y, color=BLUE, lw=2, marker="o", ms=4)
    ax.axhline(11.6, color=RED, ls="--", lw=1.3)
    ax.text(0.2, 11.7, "NECKLINE", color=RED, fontsize=9)
    for xi, yi, t in [(3, 15, "Left\nShoulder"), (5, 19.4, "HEAD"), (7, 15, "Right\nShoulder")]:
        ax.annotate(t, xy=(xi, yi), xytext=(xi - 0.4, yi + 0.8), fontsize=9, ha="center")
    ax.annotate("break below neckline\n= SELL signal", xy=(9, 11), xytext=(8.4, 13.5),
                fontsize=9, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    ax.set_title("HEAD & SHOULDERS — a topping (reversal) pattern", fontweight="bold")
    ax.set_xticks([])
    save(fig, "p2_headshoulders.png")


def double_top():
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.3))
    x = np.arange(9)
    axes[0].plot(x, [8, 12, 16, 13, 16, 13, 11, 9, 7], color=BLUE, lw=2, marker="o", ms=4)
    axes[0].set_title("DOUBLE TOP (M) — reversal DOWN", fontweight="bold", color=RED)
    axes[0].annotate("two failed\nhighs", xy=(2, 16), xytext=(3.5, 15.5), fontsize=9)
    axes[1].plot(x, [16, 12, 8, 11, 8, 11, 13, 15, 17], color=BLUE, lw=2, marker="o", ms=4)
    axes[1].set_title("DOUBLE BOTTOM (W) — reversal UP", fontweight="bold", color=GREEN)
    axes[1].annotate("two held\nlows", xy=(2, 8), xytext=(3.2, 9), fontsize=9)
    for a in axes:
        a.set_xticks([])
    save(fig, "p2_doubletop.png")


def triangles():
    fig, axes = plt.subplots(1, 3, figsize=(13, 4))
    x = np.arange(10)
    # ascending
    hi = np.full(10, 16.0); lo = 8 + x * 0.7
    axes[0].plot(x, [8, 16, 9, 16, 11, 16, 12, 16, 13, 17], color=BLUE, lw=1.6, marker="o", ms=3)
    axes[0].plot(x, hi, "r--"); axes[0].plot(x, lo, "g--")
    axes[0].set_title("ASCENDING\n(bullish bias)", color=GREEN)
    # descending
    axes[1].plot(x, [16, 8, 15, 8, 13, 8, 12, 8, 11, 7], color=BLUE, lw=1.6, marker="o", ms=3)
    axes[1].plot(x, np.full(10, 8.0), "g--"); axes[1].plot(x, 16 - x * 0.7, "r--")
    axes[1].set_title("DESCENDING\n(bearish bias)", color=RED)
    # symmetrical
    axes[2].plot(x, [8, 16, 9, 15, 10, 14, 11, 13, 11.5, 15], color=BLUE, lw=1.6, marker="o", ms=3)
    axes[2].plot(x, 16 - x * 0.45, "r--"); axes[2].plot(x, 8 + x * 0.45, "g--")
    axes[2].set_title("SYMMETRICAL\n(breakout in trend dir.)", color=AMBER)
    for a in axes:
        a.set_xticks([])
    fig.suptitle("TRIANGLES — consolidation before a breakout", fontweight="bold", y=1.04)
    save(fig, "p2_triangles.png")


def flag_cup():
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.3))
    # bull flag
    x1 = np.arange(14)
    y1 = np.concatenate([np.linspace(8, 17, 6), np.linspace(17, 14, 5), np.linspace(14, 22, 3)])
    axes[0].plot(x1, y1, color=BLUE, lw=2)
    axes[0].annotate("flagpole\n(sharp move)", xy=(3, 13), xytext=(0.2, 18), fontsize=9)
    axes[0].annotate("flag\n(small pullback)", xy=(8, 15), xytext=(8.5, 11), fontsize=9)
    axes[0].annotate("breakout =\ncontinue up", xy=(13, 22), xytext=(10, 19), fontsize=9, color=GREEN)
    axes[0].set_title("BULL FLAG — continuation", fontweight="bold", color=GREEN)
    # cup & handle
    t = np.linspace(0, np.pi, 60)
    cup = 14 - 4 * np.sin(t)
    x2 = np.concatenate([np.arange(60), np.arange(60, 75)])
    y2 = np.concatenate([cup, np.linspace(14, 12.5, 8).tolist() + np.linspace(12.5, 18, 7).tolist()])
    axes[1].plot(x2, y2, color=BLUE, lw=2)
    axes[1].annotate("cup (rounded base)", xy=(30, 10.5), xytext=(20, 8.5), fontsize=9)
    axes[1].annotate("handle", xy=(66, 12.7), xytext=(58, 9.5), fontsize=9)
    axes[1].annotate("breakout up", xy=(74, 18), xytext=(62, 16.5), fontsize=9, color=GREEN)
    axes[1].set_title("CUP & HANDLE — bullish", fontweight="bold", color=GREEN)
    for a in axes:
        a.set_xticks([])
    save(fig, "p2_flag_cup.png")


def gaps():
    df = load("^NSEI", "3mo"); sub = df.iloc[-20:].reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(10, 4.6))
    for i, r in sub.iterrows():
        col = GREEN if r.Close >= r.Open else RED
        ax.plot([i, i], [r.Low, r.High], color="black", lw=0.8)
        ax.add_patch(Rectangle((i - 0.3, min(r.Open, r.Close)), 0.6,
                     max(abs(r.Close - r.Open), 1), color=col))
    ax.set_title("GAP — empty space where price jumps overnight", fontweight="bold")
    box(ax, "A gap = price opens far from yesterday's close (big news).\nGaps often get 'filled' later.",
        fc="#fff7e6")
    ax.set_xticks([])
    save(fig, "p2_gaps.png")


def trendlines():
    df = load("^NSEI", "1y"); c = df["Close"]
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(c.index, c.values, color=BLUE, lw=1.3)
    n = len(c)
    xi = np.arange(n)
    lows = c.values - 200
    ax.plot(c.index, np.linspace(lows.min(), lows.min() + 0.04 * (c.values[-1]), n) * 0 + np.poly1d(
        np.polyfit(xi, c.values, 1))(xi) - 600, color=GREEN, ls="--", lw=1.5)
    ax.set_title("TRENDLINE — connect the rising lows; it acts as support", fontweight="bold")
    box(ax, "Draw a line under the higher lows in an uptrend.\nPrice bouncing off it = trend intact; a break = warning.",
        fc="#eafaf0")
    save(fig, "p2_trendlines.png")


def star_patterns():
    def candle(ax, x, o, h, l, c, w=0.5):
        col = GREEN if c >= o else RED
        ax.plot([x, x], [l, h], color="black", lw=1.2)
        ax.add_patch(Rectangle((x - w / 2, min(o, c)), w, max(abs(c - o), 0.1), color=col, ec="black"))
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.3))
    ax = axes[0]
    candle(ax, 1, 20, 21, 14, 15); candle(ax, 2, 13, 14, 11, 12.5)
    candle(ax, 3, 13, 21, 12, 20)
    ax.set_xlim(0, 4); ax.set_ylim(10, 23)
    ax.set_title("MORNING STAR — bullish bottom (3 candles)", fontweight="bold", color=GREEN)
    ax.annotate("down → small pause → strong up", xy=(2, 12), xytext=(0.1, 21), fontsize=9)
    ax = axes[1]
    candle(ax, 1, 12, 18, 11, 17); candle(ax, 2, 18.5, 20, 18, 19)
    candle(ax, 3, 18, 19, 11, 12)
    ax.set_xlim(0, 4); ax.set_ylim(10, 21)
    ax.set_title("EVENING STAR — bearish top (3 candles)", fontweight="bold", color=RED)
    ax.annotate("up → small pause → strong down", xy=(2, 19), xytext=(0.1, 11.5), fontsize=9)
    save(fig, "p2_star.png")


# ===================== PART 3: more indicators =====================
def load(t="^NSEI", period="1y"):
    df = yf.download(t, period=period, progress=False, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df[["Open", "High", "Low", "Close"]].dropna()


def adx():
    df = load("^NSEI", "1y"); c = df["Close"]
    # simple ADX proxy via rolling directional movement
    up = df["High"].diff(); dn = -df["Low"].diff()
    plus = ((up > dn) & (up > 0)) * up
    minus = ((dn > up) & (dn > 0)) * dn
    tr = (df["High"] - df["Low"]).rolling(14).mean()
    pdi = 100 * plus.rolling(14).mean() / tr
    mdi = 100 * minus.rolling(14).mean() / tr
    adxv = (abs(pdi - mdi) / (pdi + mdi) * 100).rolling(14).mean()
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 6), sharex=True,
                                 gridspec_kw={"height_ratios": [2, 1]})
    a1.plot(c.index, c.values, color=BLUE)
    a1.set_title("ADX — trend STRENGTH, with +DI (green) and -DI (red) showing DIRECTION",
                 fontweight="bold")
    a2.plot(pdi.index, pdi, color=GREEN, lw=1.1, label="+DI (bullish strength)")
    a2.plot(mdi.index, mdi, color=RED, lw=1.1, label="-DI (bearish strength)")
    a2.plot(adxv.index, adxv, color="#6a3d9a", lw=1.8, label="ADX (trend strength)")
    a2.axhline(25, color=AMBER, ls="--")
    a2.text(adxv.index[2], 27, "ABOVE 25 = strong trend", fontsize=8.5, color=AMBER)
    a2.legend(fontsize=8, loc="upper left", ncol=3)
    a2.set_ylabel("ADX / DI"); a2.set_ylim(0, 60)
    save(fig, "p3_adx.png")


def stochastic():
    df = load("^NSEI", "6mo")
    low14 = df["Low"].rolling(14).min(); high14 = df["High"].rolling(14).max()
    k = 100 * (df["Close"] - low14) / (high14 - low14)
    d = k.rolling(3).mean()
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 6), sharex=True,
                                 gridspec_kw={"height_ratios": [2, 1]})
    a1.plot(df.index, df["Close"], color=BLUE); a1.set_title("STOCHASTIC — momentum for ranging markets",
                                                             fontweight="bold")
    a2.plot(k.index, k, color=GREEN, lw=1, label="%K"); a2.plot(d.index, d, color=RED, lw=1, label="%D")
    a2.axhline(80, color=RED, ls="--"); a2.axhline(20, color=GREEN, ls="--")
    a2.axhspan(80, 100, color=RED, alpha=0.08); a2.axhspan(0, 20, color=GREEN, alpha=0.08)
    a2.legend(fontsize=8, loc="upper left"); a2.set_ylim(0, 100)
    a2.text(k.index[2], 86, ">80 overbought", color=RED, fontsize=8)
    a2.text(k.index[2], 8, "<20 oversold", color=GREEN, fontsize=8)
    save(fig, "p3_stochastic.png")


def volume():
    df = load("^NSEI", "3mo")
    vol = yf.download("^NSEI", period="3mo", progress=False)["Volume"]
    if isinstance(vol, pd.DataFrame):
        vol = vol.iloc[:, 0]
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 6), sharex=True,
                                 gridspec_kw={"height_ratios": [2, 1]})
    a1.plot(df.index, df["Close"], color=BLUE); a1.set_title("VOLUME — the fuel behind a move",
                                                             fontweight="bold")
    cols = [GREEN if df["Close"].iloc[i] >= df["Open"].iloc[i] else RED for i in range(len(df))]
    a2.bar(vol.index, vol.values, color=cols[:len(vol)])
    a2.set_ylabel("Volume")
    box(a2, "Big move + high volume = trustworthy. Move on low volume = suspect.", xy=(0.015, 0.7))
    save(fig, "p3_volume.png")


def pivots():
    df = load("^NSEI", "2mo"); c = df["Close"]
    h, l, cl = df["High"].iloc[-2], df["Low"].iloc[-2], df["Close"].iloc[-2]
    P = (h + l + cl) / 3
    r1, s1 = 2 * P - l, 2 * P - h
    r2, s2 = P + (h - l), P - (h - l)
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(c.index, c.values, color=BLUE, lw=1.3)
    for lvl, name, col in [(r2, "R2", RED), (r1, "R1", RED), (P, "PIVOT", "#333"),
                           (s1, "S1", GREEN), (s2, "S2", GREEN)]:
        ax.axhline(lvl, color=col, ls="--", lw=1)
        ax.text(c.index[1], lvl, f"  {name}", color=col, fontsize=9, va="bottom")
    ax.set_title("PIVOT POINTS — auto support/resistance for the day (intraday favourite)",
                 fontweight="bold")
    save(fig, "p3_pivots.png")


def atr():
    df = load("^NSEI", "1y"); c = df["Close"]
    tr = pd.concat([df.High - df.Low, (df.High - c.shift()).abs(), (df.Low - c.shift()).abs()],
                   axis=1).max(axis=1)
    a = tr.rolling(14).mean()
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 6), sharex=True,
                                 gridspec_kw={"height_ratios": [2, 1]})
    a1.plot(c.index, c.values, color=BLUE); a1.set_title("ATR — how much price moves in a day (volatility)",
                                                          fontweight="bold")
    a2.plot(a.index, a, color="#6a3d9a"); a2.set_ylabel("ATR")
    box(a2, "Use ATR to size your stop-loss: a wider ATR needs a wider stop\nso normal noise doesn't kick you out.",
        xy=(0.015, 0.62))
    save(fig, "p3_atr.png")


# ===================== PART 4 =====================
def divergence():
    n = 60
    x = np.arange(n)
    price = 20 + x * 0.15 + np.sin(x / 4) * 1.5
    price[-15:] = price[-15] + np.linspace(0, 3, 15)  # higher high
    rsi = 55 + np.sin(x / 4) * 12
    rsi[-15:] = rsi[-15] - np.linspace(0, 10, 15)      # lower high
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 6.4), sharex=True,
                                 gridspec_kw={"height_ratios": [1, 1]})
    a1.plot(x, price, color=BLUE); a1.set_title("BEARISH DIVERGENCE — the hidden warning",
                                                fontweight="bold", color=RED)
    a1.set_ylim(price.min() - 1, price.max() + 3)
    a1.annotate("price: HIGHER high", xy=(n - 1, price[-1]), xytext=(n - 33, price[-1] - 4),
                fontsize=9, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    a2.plot(x, rsi, color="#6a3d9a"); a2.set_ylabel("RSI")
    a2.annotate("RSI: LOWER high", xy=(n - 1, rsi[-1]), xytext=(n - 28, rsi[-1] - 6),
                fontsize=9, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    box(a2, "Price makes a new high but RSI does NOT = momentum fading = possible reversal.",
        xy=(0.015, 0.05), fc="#fdecea")
    save(fig, "p4_divergence.png")


def elliott():
    pts = [(0, 10), (2, 14), (3, 12), (5, 18), (6, 16), (8, 22),
           (9, 18), (10, 20), (11, 16)]
    x, y = zip(*pts)
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(x, y, color=BLUE, lw=2, marker="o", ms=4)
    for i, lab in enumerate(["", "1", "2", "3", "4", "5", "A", "B", "C"]):
        ax.annotate(lab, (x[i], y[i]), textcoords="offset points", xytext=(0, 8),
                    fontsize=11, fontweight="bold",
                    color=GREEN if lab in "135" else RED if lab in "ABC" else "#333")
    ax.set_title("ELLIOTT WAVE — trends move in 5 waves up, then 3 waves (A-B-C) down",
                 fontweight="bold")
    ax.set_xticks([])
    save(fig, "p4_elliott.png")


# ===================== PART 5: options & futures =====================
def payoff(ax, S, pl, title, col=GREEN):
    ax.plot(S, pl, color=col, lw=2.2)
    ax.axhline(0, color="#888", lw=1)
    ax.fill_between(S, pl, 0, where=(pl > 0), color=GREEN, alpha=0.12)
    ax.fill_between(S, pl, 0, where=(pl < 0), color=RED, alpha=0.12)
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel("Price of stock at expiry"); ax.set_ylabel("Profit / Loss")


def options_basic():
    S = np.linspace(80, 120, 200); K, prem = 100, 4
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
    payoff(axes[0], S, np.maximum(S - K, 0) - prem, "LONG CALL (bullish)\nrisk = premium, upside = unlimited")
    axes[0].annotate("breakeven", xy=(104, 0), xytext=(106, 5), fontsize=8)
    payoff(axes[1], S, np.maximum(K - S, 0) - prem, "LONG PUT (bearish)\nrisk = premium, profit if price falls", RED)
    save(fig, "p5_call_put.png")


def options_income():
    S = np.linspace(80, 120, 200); K, prem = 100, 4
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
    cc = (S - 100) + prem - np.maximum(S - K, 0)
    payoff(axes[0], S, cc, "COVERED CALL (own stock + sell call)\nincome, but upside capped", AMBER)
    strad = np.maximum(S - K, 0) + np.maximum(K - S, 0) - 8
    payoff(axes[1], S, strad, "LONG STRADDLE (buy call + put)\nprofit from a BIG move either way", BLUE)
    save(fig, "p5_income_straddle.png")


def options_spreads():
    S = np.linspace(80, 120, 200)
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
    bull = np.maximum(S - 100, 0) - 3 - (np.maximum(S - 108, 0) - 1)
    payoff(axes[0], S, bull, "BULL CALL SPREAD\ncapped risk AND capped reward", GREEN)
    ic = (3 - np.maximum(92 - S, 0)) + (3 - np.maximum(S - 108, 0)) \
         - (1 - np.maximum(88 - S, 0)) - (1 - np.maximum(S - 112, 0))
    payoff(axes[1], S, ic, "IRON CONDOR\nprofit when price stays RANGE-BOUND", AMBER)
    save(fig, "p5_spreads.png")


def futures_curve():
    months = np.arange(1, 8)
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.plot(months, 100 + months * 1.2, color=RED, lw=2, marker="o", label="CONTANGO (futures > spot — normal)")
    ax.plot(months, 100 - months * 1.2, color=GREEN, lw=2, marker="o", label="BACKWARDATION (futures < spot — tight supply)")
    ax.axhline(100, color="#888", ls=":"); ax.text(1, 100.4, "spot price", fontsize=9)
    ax.set_title("FUTURES CURVE — contango vs backwardation", fontweight="bold")
    ax.set_xlabel("Months to expiry"); ax.legend(fontsize=9)
    save(fig, "p5_futures_curve.png")


def oi_chain():
    strikes = np.arange(23000, 25100, 200)
    call_oi = np.array([2, 3, 4, 6, 9, 14, 11, 7, 5, 3, 2])[:len(strikes)]
    put_oi = np.array([2, 4, 6, 9, 13, 10, 7, 5, 3, 2, 1])[:len(strikes)]
    fig, ax = plt.subplots(figsize=(11, 5))
    w = 80
    ax.bar(strikes - w, call_oi, width=2 * w, color=RED, alpha=0.7, label="Call OI (resistance)")
    ax.bar(strikes + w, put_oi, width=2 * w, color=GREEN, alpha=0.7, label="Put OI (support)")
    ax.axvline(24000, color=BLUE, lw=2); ax.text(24050, max(call_oi) * 0.9, "spot", color=BLUE)
    ax.set_title("OPTION CHAIN — Open Interest shows support & resistance", fontweight="bold")
    ax.set_xlabel("Strike price"); ax.set_ylabel("Open Interest (lakh)")
    ax.legend(fontsize=9)
    box(ax, "Highest CALL OI strike = resistance.  Highest PUT OI strike = support.", xy=(0.015, 0.78), fc="#fff7e6")
    save(fig, "p5_oi_chain.png")


def iv_skew():
    strikes = np.linspace(22000, 26000, 50)
    iv = 14 + ((strikes - 24000) / 1000) ** 2 * 1.1 - (strikes - 24000) / 1000 * 1.5
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.plot(strikes, iv, color="#6a3d9a", lw=2.2)
    ax.axvline(24000, color=BLUE, ls=":"); ax.text(24050, iv.min(), "spot (ATM)", color=BLUE, fontsize=9)
    ax.set_title("VOLATILITY SKEW — option IV differs by strike (puts pricier = crash fear)",
                 fontweight="bold")
    ax.set_xlabel("Strike price"); ax.set_ylabel("Implied Volatility %")
    save(fig, "p5_iv_skew.png")


# ===================== PART 6,7,8 =====================
def gold_dollar():
    g = load("GC=F", "2y")["Close"]; d = load("DX-Y.NYB", "2y")["Close"]
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(g.index, g.values, color=AMBER, lw=1.6, label="Gold")
    ax2 = ax.twinx(); ax2.plot(d.index, d.values, color=GREEN, lw=1.3, label="US Dollar Index")
    ax.set_title("GOLD vs the US DOLLAR — they usually move OPPOSITE", fontweight="bold")
    ax.set_ylabel("Gold", color=AMBER); ax2.set_ylabel("Dollar Index", color=GREEN)
    box(ax, "Strong dollar → weaker gold (and vice-versa). Gold is a safe-haven / inflation hedge.",
        xy=(0.015, 0.05), fc="#fff7e6")
    save(fig, "p6_gold_dollar.png")


def vix():
    try:
        v = load("^INDIAVIX", "1y")["Close"]
    except Exception:
        v = load("^VIX", "1y")["Close"]
    nf = load("^NSEI", "1y")["Close"]
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(nf.index, nf.values, color=BLUE, lw=1.3, label="Nifty")
    ax2 = ax.twinx(); ax2.plot(v.index, v.values, color=RED, lw=1.1, label="VIX (fear)")
    ax.set_title("INDIA VIX — the 'fear gauge' spikes when markets fall", fontweight="bold")
    ax.set_ylabel("Nifty", color=BLUE); ax2.set_ylabel("VIX", color=RED)
    box(ax, "High VIX = fear/big moves (often near bottoms). Low VIX = calm/complacent.",
        xy=(0.015, 0.05), fc="#fdecea")
    save(fig, "p7_vix.png")


def riskreward():
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.axhspan(100, 112, color=GREEN, alpha=0.12)
    ax.axhspan(96, 100, color=RED, alpha=0.12)
    for y, t, col in [(100, "ENTRY (buy)", BLUE), (112, "TARGET  (+12 reward)", GREEN),
                      (96, "STOP-LOSS  (−4 risk)", RED)]:
        ax.axhline(y, color=col, lw=2); ax.text(0.02, y + 0.2, t, color=col, fontsize=11, fontweight="bold")
    ax.annotate("", xy=(0.7, 112), xytext=(0.7, 100), arrowprops=dict(arrowstyle="<->", color=GREEN))
    ax.annotate("", xy=(0.85, 100), xytext=(0.85, 96), arrowprops=dict(arrowstyle="<->", color=RED))
    ax.text(0.72, 106, "REWARD", color=GREEN, fontsize=10)
    ax.text(0.87, 98, "RISK", color=RED, fontsize=10)
    ax.set_title("RISK : REWARD — here it's 3:1 (risk 4 to make 12)", fontweight="bold")
    ax.set_xlim(0, 1); ax.set_ylim(93, 115); ax.set_xticks([]); ax.set_ylabel("Price")
    box(ax, "Rule: only take trades where reward is at least 2x the risk.\nThen you can be wrong often and still profit.",
        xy=(0.3, 0.05), fc="#eafaf0")
    save(fig, "p8_riskreward.png")


def drawdown():
    np.random.seed(1)
    eq = pd.Series(100 + np.cumsum(np.random.randn(250) * 1.2 + 0.25))
    peak = eq.cummax(); dd = (eq - peak) / peak * 100
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 6), sharex=True,
                                 gridspec_kw={"height_ratios": [2, 1]})
    a1.plot(eq.index, eq, color=BLUE); a1.plot(peak.index, peak, color=GREEN, ls="--", lw=1)
    a1.set_title("DRAWDOWN — the worst fall from a peak (the 'pain' of a strategy)", fontweight="bold")
    a2.fill_between(dd.index, dd, 0, color=RED, alpha=0.3)
    a2.set_ylabel("Drawdown %")
    box(a2, "Max drawdown = the biggest drop you'd have had to sit through. Lower is safer.",
        xy=(0.015, 0.08))
    save(fig, "p8_drawdown.png")


def main():
    print("Building full diagram set...")
    chart_types(); dow_cycle(); timeframes()
    head_shoulders(); double_top(); triangles(); flag_cup(); gaps(); trendlines(); star_patterns()
    adx(); stochastic(); volume(); pivots(); atr()
    divergence(); elliott()
    options_basic(); options_income(); options_spreads(); futures_curve(); oi_chain(); iv_skew()
    gold_dollar(); vix(); riskreward(); drawdown()
    print("Done.")


if __name__ == "__main__":
    main()
