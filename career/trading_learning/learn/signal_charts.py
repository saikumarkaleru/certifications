"""
Redraw the key charts with VISUAL buy/sell signals.
INDICATOR charts (S/R, MA, RSI, MACD, Bollinger, Fibonacci, setup) use REAL Nifty
data so they look realistic, with signals detected from the data and marked with
green BUY / red SELL arrows, plus stop/target lines.
PATTERN charts (head & shoulders, double bottom, triangle, flag, hammer) stay as
clean schematic diagrams — that's the standard way to teach a pattern's shape.
Overwrites the matching images in ./img.
"""
import os
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
from scipy.signal import argrelextrema

IMG = os.path.join(os.path.dirname(__file__), "img")
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.25})
GREEN, RED, BLUE, PURP, AMBER = "#1a9850", "#d73027", "#1f4e79", "#6a3d9a", "#b8860b"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(IMG, name), dpi=130, bbox_inches="tight")
    plt.close(fig)
    print("  ->", name)


def load(t="^NSEI", period="1y"):
    df = yf.download(t, period=period, progress=False, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df[["Open", "High", "Low", "Close"]].dropna()


def mark_buy(ax, x, y, dy):
    ax.annotate("BUY", xy=(x, y), xytext=(x, y - dy), ha="center", fontsize=10.5,
                fontweight="bold", color="white",
                bbox=dict(boxstyle="round,pad=0.25", fc=GREEN, ec="none"),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2))


def mark_sell(ax, x, y, dy):
    ax.annotate("SELL", xy=(x, y), xytext=(x, y + dy), ha="center", fontsize=10.5,
                fontweight="bold", color="white",
                bbox=dict(boxstyle="round,pad=0.25", fc=RED, ec="none"),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2))


def hline(ax, y, color, label, xpos):
    ax.axhline(y, color=color, ls=":", lw=1.6)
    ax.text(xpos, y, f" {label}", color=color, va="bottom", fontsize=9.5, fontweight="bold")


def circle(ax, cx, cy, w, h, label=None):
    ax.add_patch(Ellipse((cx, cy), w, h, fill=False, edgecolor=PURP, lw=2.4, ls="--"))
    if label:
        ax.text(cx, cy + h / 2 + h * 0.08, label, ha="center", color=PURP,
                fontsize=9.5, fontweight="bold")


def candle(ax, x, o, h, l, c, w=0.6):
    col = GREEN if c >= o else RED
    ax.plot([x, x], [l, h], color="black", lw=1.1, zorder=2)
    ax.add_patch(Rectangle((x - w / 2, min(o, c)), w, max(abs(c - o), 0.05),
                           color=col, ec="black", lw=0.8, zorder=3))


# ============================ REAL-DATA INDICATOR CHARTS ============================
def sr():
    df = load(); c = df["Close"]
    n = len(c); dy = (c.max() - c.min()) * 0.07
    res = float(c.iloc[-n:].max()); sup = float(c.iloc[-n:].min())
    fig, ax = plt.subplots(figsize=(11, 5.4))
    ax.plot(c.index, c.values, color=BLUE, lw=1.4)
    hline(ax, res, RED, "RESISTANCE (sell zone)", c.index[2])
    hline(ax, sup, GREEN, "SUPPORT (buy zone)", c.index[2])
    mins = argrelextrema(c.values, np.less, order=6)[0]
    maxs = argrelextrema(c.values, np.greater, order=6)[0]
    rng = res - sup
    for i in [j for j in mins if c.iloc[j] <= sup + 0.18 * rng][:3]:
        mark_buy(ax, c.index[i], c.iloc[i], dy)
    for i in [j for j in maxs if c.iloc[j] >= res - 0.18 * rng][:3]:
        mark_sell(ax, c.index[i], c.iloc[i], dy)
    ax.set_title("SUPPORT & RESISTANCE (Nifty) — BUY near the floor, SELL near the ceiling",
                 fontweight="bold")
    save(fig, "04_support_resistance.png")


def ma():
    df = load(); c = df["Close"]
    ma20 = c.rolling(20).mean(); ma50 = c.rolling(50).mean()
    dy = (c.max() - c.min()) * 0.07
    fig, ax = plt.subplots(figsize=(11, 5.4))
    ax.plot(c.index, c.values, color="#9aa7b5", lw=1, label="Price")
    ax.plot(ma20.index, ma20, color=GREEN, lw=1.8, label="20-day MA")
    ax.plot(ma50.index, ma50, color=RED, lw=1.8, label="50-day MA")
    mins = argrelextrema(c.values, np.less, order=5)[0]
    # pullback-to-MA buys: a dip that touches the 20-MA while in an uptrend (20MA>50MA)
    buys = [i for i in mins if i > 50 and ma20.iloc[i] > ma50.iloc[i]
            and abs(c.iloc[i] - ma20.iloc[i]) < 0.012 * c.iloc[i]][:3]
    for i in buys:
        mark_buy(ax, c.index[i], c.iloc[i], dy)
    ax.set_title("MOVING AVERAGES (Nifty) — in an uptrend, BUY the pullback to the 20-day MA",
                 fontweight="bold")
    ax.legend(loc="upper left", fontsize=8.5)
    save(fig, "05_moving_averages.png")


def rsi_chart():
    df = load(); c = df["Close"]
    d = c.diff(); g = d.clip(lower=0).rolling(14).mean(); l = (-d.clip(upper=0)).rolling(14).mean()
    r = 100 - 100 / (1 + g / l.replace(0, np.nan))
    dy = (c.max() - c.min()) * 0.07
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 6.8), sharex=True,
                                 gridspec_kw={"height_ratios": [2, 1]})
    a1.plot(c.index, c.values, color=BLUE, lw=1.3)
    a1.set_title("RSI (Nifty) — BUY when RSI leaves OVERSOLD (<30), SELL when it leaves OVERBOUGHT (>70)",
                 fontweight="bold")
    rv = r.values
    buys = [i for i in range(15, len(rv)) if rv[i] > 30 and rv[i - 1] <= 30]
    sells = [i for i in range(15, len(rv)) if rv[i] < 70 and rv[i - 1] >= 70]
    for i in buys[-4:]:
        mark_buy(a1, c.index[i], c.iloc[i], dy)
    for i in sells[-4:]:
        mark_sell(a1, c.index[i], c.iloc[i], dy)
    a2.plot(r.index, r, color=PURP, lw=1.3)
    a2.axhline(70, color=RED, ls="--"); a2.axhline(30, color=GREEN, ls="--")
    a2.axhspan(70, 100, color=RED, alpha=0.08); a2.axhspan(0, 30, color=GREEN, alpha=0.08)
    a2.set_ylim(0, 100); a2.set_ylabel("RSI")
    a2.text(r.index[2], 86, "OVERBOUGHT", color=RED, fontsize=9)
    a2.text(r.index[2], 16, "OVERSOLD", color=GREEN, fontsize=9)
    save(fig, "06_rsi.png")


def macd_chart():
    df = load(); c = df["Close"]
    macd = c.ewm(span=12, adjust=False).mean() - c.ewm(span=26, adjust=False).mean()
    sig = macd.ewm(span=9, adjust=False).mean(); hist = macd - sig
    dy = (c.max() - c.min()) * 0.07
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 6.8), sharex=True,
                                 gridspec_kw={"height_ratios": [2, 1]})
    a1.plot(c.index, c.values, color=BLUE, lw=1.3)
    a1.set_title("MACD (Nifty) — BUY when the green line crosses ABOVE red, SELL when below",
                 fontweight="bold")
    m, s = macd.values, sig.values
    ups = [i for i in range(1, len(m)) if m[i] > s[i] and m[i - 1] <= s[i - 1]]
    dns = [i for i in range(1, len(m)) if m[i] < s[i] and m[i - 1] >= s[i - 1]]
    for i in ups[-4:]:
        mark_buy(a1, c.index[i], c.iloc[i], dy)
    for i in dns[-4:]:
        mark_sell(a1, c.index[i], c.iloc[i], dy)
    a2.plot(macd.index, macd, color=GREEN, lw=1.2, label="MACD line")
    a2.plot(sig.index, sig, color=RED, lw=1.2, label="Signal line")
    a2.bar(hist.index, hist, color=np.where(hist >= 0, "#9ad0a8", "#f2a8a0"), width=1)
    a2.axhline(0, color="#888", lw=0.8); a2.legend(fontsize=8, loc="upper left")
    save(fig, "07_macd.png")


def bb():
    df = load(); c = df["Close"]
    mid = c.rolling(20).mean(); sd = c.rolling(20).std()
    up, dn = mid + 2 * sd, mid - 2 * sd
    dy = (c.max() - c.min()) * 0.07
    fig, ax = plt.subplots(figsize=(11, 5.4))
    ax.plot(c.index, c.values, color=BLUE, lw=1.3, label="Price")
    ax.plot(mid.index, mid, color="#888", lw=1, label="20-day MA (middle)")
    ax.plot(up.index, up, color=RED, lw=1, label="Upper band")
    ax.plot(dn.index, dn, color=GREEN, lw=1, label="Lower band")
    ax.fill_between(c.index, dn, up, color="#cfe0f5", alpha=0.3)
    touch_dn = [i for i in range(20, len(c)) if c.iloc[i] <= dn.iloc[i]]
    touch_up = [i for i in range(20, len(c)) if c.iloc[i] >= up.iloc[i]]
    for i in touch_dn[-3:]:
        mark_buy(ax, c.index[i], c.iloc[i], dy)
    for i in touch_up[-3:]:
        mark_sell(ax, c.index[i], c.iloc[i], dy)
    ax.set_title("BOLLINGER BANDS (Nifty) — BUY at the lower band, SELL at the upper band",
                 fontweight="bold")
    ax.legend(loc="upper left", fontsize=8)
    save(fig, "08_bollinger.png")


def fib():
    df = load("^NSEI", "1y"); c = df["Close"]
    lo_i = int(c.values.argmin())
    after = c.iloc[lo_i:]
    hi_i = lo_i + int(after.values.argmax())
    lo, hi = float(c.iloc[lo_i]), float(c.iloc[hi_i])
    diff = hi - lo
    levels = {"0% (high)": hi, "38.2%": hi - .382 * diff, "50%": hi - .5 * diff,
              "61.8%": hi - .618 * diff, "100% (low)": lo}
    dy = (c.max() - c.min()) * 0.07
    fig, ax = plt.subplots(figsize=(11, 5.4))
    ax.plot(c.index, c.values, color=BLUE, lw=1.3)
    for name, lvl in levels.items():
        ax.axhline(lvl, color=AMBER, ls="--", lw=0.9)
        ax.text(c.index[1], lvl, f" {name}", color="#7a5c00", fontsize=8.5, va="bottom")
    ax.axhspan(hi - .618 * diff, hi - .382 * diff, color="#fff3cd", alpha=0.5)
    # a BUY where price dips into the 38-62% zone after the high
    z_hi, z_lo = hi - .382 * diff, hi - .618 * diff
    dip = [i for i in range(hi_i + 1, len(c)) if z_lo <= c.iloc[i] <= z_hi]
    if dip:
        i = dip[0]
        mark_buy(ax, c.index[i], c.iloc[i], dy)
    ax.set_title("FIBONACCI (Nifty) — BUY the pullback into the 38–62% retracement zone",
                 fontweight="bold")
    save(fig, "09_fibonacci.png")


def setup():
    df = load(); c = df["Close"]
    ma20 = c.rolling(20).mean(); ma50 = c.rolling(50).mean()
    dy = (c.max() - c.min()) * 0.07
    mins = argrelextrema(c.values, np.less, order=5)[0]
    buys = [i for i in mins if i > 60 and ma20.iloc[i] > ma50.iloc[i]
            and abs(c.iloc[i] - ma20.iloc[i]) < 0.015 * c.iloc[i]]
    bi = buys[-1] if buys else int(len(c) * 0.6)
    entry = float(c.iloc[bi]); stop = entry * 0.975; target = entry + 2 * (entry - stop)
    fig, ax = plt.subplots(figsize=(11, 5.4))
    ax.plot(c.index, c.values, color=BLUE, lw=1.3, label="Price")
    ax.plot(ma20.index, ma20, color=AMBER, lw=1.6, label="20-day MA (support)")
    mark_buy(ax, c.index[bi], entry, dy)
    hline(ax, stop, RED, "STOP-LOSS", c.index[2])
    hline(ax, target, GREEN, "TARGET", c.index[2])
    ax.set_title("THE COMPLETE TRADE (Nifty) — uptrend + pullback to MA = BUY, with STOP & TARGET",
                 fontweight="bold")
    ax.legend(loc="upper left", fontsize=8.5)
    save(fig, "10_setup.png")


# ============================ SCHEMATIC PATTERN DIAGRAMS ============================
def hs():
    x = np.arange(11)
    y = np.array([10, 13, 11.5, 16, 11.6, 20, 11.6, 16, 11.5, 9, 7])
    fig, ax = plt.subplots(figsize=(9.5, 5.3))
    ax.plot(x, y, color=BLUE, lw=2, marker="o", ms=4)
    ax.axhline(11.55, color=AMBER, ls="--", lw=1.4); ax.text(0, 11.7, "neckline", color="#7a5c00", fontsize=9)
    circle(ax, 5, 20, 1.3, 3, "HEAD")
    ax.text(3, 16.6, "L. shoulder", fontsize=8.5, ha="center")
    ax.text(7, 16.6, "R. shoulder", fontsize=8.5, ha="center")
    mark_sell(ax, 9, 10.5, 2.5)
    hline(ax, 16.5, RED, "STOP (above shoulder)", 0)
    hline(ax, 6.5, GREEN, "TARGET", 0)
    ax.set_title("HEAD & SHOULDERS (schematic) — SELL when price breaks the neckline",
                 fontweight="bold")
    ax.set_xticks([]); ax.set_ylim(5, 23)
    save(fig, "p2_headshoulders.png")


def double_bottom():
    x = np.arange(9)
    y = np.array([18, 13, 9, 12.5, 9, 12.5, 15, 17, 19])
    fig, ax = plt.subplots(figsize=(9.5, 5.3))
    ax.plot(x, y, color=BLUE, lw=2, marker="o", ms=4)
    ax.axhline(12.7, color=AMBER, ls="--", lw=1.4); ax.text(0, 12.9, "neckline", color="#7a5c00", fontsize=9)
    circle(ax, 2, 9, 1.1, 2.2); circle(ax, 4, 9, 1.1, 2.2, "two equal bottoms")
    mark_buy(ax, 6, 15, 2.6)
    hline(ax, 8.3, RED, "STOP (below bottoms)", 0)
    hline(ax, 18.5, GREEN, "TARGET", 0)
    ax.set_title("DOUBLE BOTTOM (schematic) — BUY when price breaks the neckline",
                 fontweight="bold")
    ax.set_xticks([]); ax.set_ylim(6, 21)
    save(fig, "p2_doubletop.png")


def triangle():
    x = np.arange(12)
    y = np.array([8, 16, 9, 16, 11, 16, 12.5, 16, 13.5, 16, 14.5, 19])
    fig, ax = plt.subplots(figsize=(9.8, 5.3))
    ax.plot(x, y, color=BLUE, lw=1.8, marker="o", ms=3)
    ax.plot(x, np.full(12, 16.2), color=RED, ls="--", lw=1.2)
    ax.plot(x, 8 + x * 0.62, color=GREEN, ls="--", lw=1.2)
    mark_buy(ax, 11, 19, 3)
    hline(ax, 13.5, RED, "STOP (inside)", 0)
    hline(ax, 23, GREEN, "TARGET (= height)", 0)
    ax.set_title("ASCENDING TRIANGLE (schematic) — BUY the breakout above the flat top",
                 fontweight="bold")
    ax.set_xticks([]); ax.set_ylim(6, 26)
    save(fig, "p2_triangles.png")


def flag():
    x = np.arange(16)
    y = np.concatenate([np.linspace(8, 18, 7), np.linspace(17.5, 15, 5), np.linspace(15.5, 25, 4)])
    fig, ax = plt.subplots(figsize=(9.8, 5.3))
    ax.plot(x, y, color=BLUE, lw=2)
    circle(ax, 9, 16.2, 3.2, 3.2, "flag (pause)")
    ax.annotate("flagpole", xy=(3, 13), xytext=(0.2, 18), fontsize=9,
                arrowprops=dict(arrowstyle="->"))
    mark_buy(ax, 13, 21, 3.2)
    hline(ax, 14.5, RED, "STOP (below flag)", 0)
    hline(ax, 25.5, GREEN, "TARGET (= flagpole)", 0)
    ax.set_title("BULL FLAG (schematic) — BUY the breakout from the flag", fontweight="bold")
    ax.set_xticks([]); ax.set_ylim(6, 28)
    save(fig, "p2_flag_cup.png")


def hammer_buy():
    fig, ax = plt.subplots(figsize=(11, 5.3))
    data = [(0, 30, 18, 28, 19), (1, 28, 19, 26, 20), (2, 26, 17, 24, 18),
            (3, 24, 15, 22, 16), (4, 22, 13, 20, 14), (5, 17, 13.5, 12, 16.5),
            (6, 17, 21, 16, 20.5), (7, 20.5, 25, 20, 24), (8, 24, 28, 23, 27.5)]
    for i, o, h, l, c in data:
        candle(ax, i, o, h, l, c)
    hline(ax, 12, GREEN, "SUPPORT", 0)
    circle(ax, 5, 14.5, 0.9, 6, "HAMMER at support")
    mark_buy(ax, 6, 17, 5)
    hline(ax, 11, RED, "STOP (below hammer)", 0)
    hline(ax, 28, GREEN, "TARGET", 0)
    ax.set_title("CANDLE REVERSAL (schematic) — BUY after a hammer confirms at support",
                 fontweight="bold")
    ax.set_xticks([]); ax.set_ylim(9, 33); ax.set_xlim(-0.5, 9)
    save(fig, "02_patterns.png")


def main():
    print("Real-data indicator charts...")
    sr(); ma(); rsi_chart(); macd_chart(); bb(); fib(); setup()
    print("Schematic pattern diagrams...")
    hs(); double_bottom(); triangle(); flag(); hammer_buy()
    print("Done.")


if __name__ == "__main__":
    main()
