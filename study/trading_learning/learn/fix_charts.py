"""Fix the charts that didn't depict their concept correctly:
iron condor (loss at wings), trendline (rising support under higher lows),
gaps (show a real gap), option-chain OI (calls above spot, puts below), and
tighten the support/resistance signal threshold."""
import os
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse
from scipy.signal import argrelextrema

IMG = os.path.join(os.path.dirname(__file__), "img")
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.25})
GREEN, RED, BLUE, PURP, AMBER = "#1a9850", "#d73027", "#1f4e79", "#6a3d9a", "#b8860b"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(IMG, name), dpi=130, bbox_inches="tight")
    plt.close(fig)
    print("  ->", name)


def mark_buy(ax, x, y, dy):
    ax.annotate("BUY", xy=(x, y), xytext=(x, y - dy), ha="center", fontsize=10.5,
                fontweight="bold", color="white", bbox=dict(boxstyle="round,pad=0.25", fc=GREEN, ec="none"),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2))


def mark_sell(ax, x, y, dy):
    ax.annotate("SELL", xy=(x, y), xytext=(x, y + dy), ha="center", fontsize=10.5,
                fontweight="bold", color="white", bbox=dict(boxstyle="round,pad=0.25", fc=RED, ec="none"),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2))


def hline(ax, y, color, label, xpos):
    ax.axhline(y, color=color, ls=":", lw=1.6)
    ax.text(xpos, y, f" {label}", color=color, va="bottom", fontsize=9.5, fontweight="bold")


def candle(ax, x, o, h, l, c, w=0.6):
    col = GREEN if c >= o else RED
    ax.plot([x, x], [l, h], color="black", lw=1.1, zorder=2)
    ax.add_patch(Rectangle((x - w / 2, min(o, c)), w, max(abs(c - o), 0.05), color=col, ec="black", lw=0.8, zorder=3))


def load(t="^NSEI", period="1y"):
    df = yf.download(t, period=period, progress=False, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df[["Open", "High", "Low", "Close"]].dropna()


# 1) IRON CONDOR — proper capped loss at the wings
def iron_condor():
    S = np.linspace(80, 120, 400)
    prem = 2
    put_spread = np.maximum(95 - S, 0) - np.maximum(90 - S, 0)   # 0 above 95, max 5 below 90
    call_spread = np.maximum(S - 105, 0) - np.maximum(S - 110, 0)  # 0 below 105, max 5 above 110
    pl = prem - put_spread - call_spread
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    ax.plot(S, pl, color=AMBER, lw=2.4)
    ax.axhline(0, color="#888", lw=1)
    ax.fill_between(S, pl, 0, where=(pl > 0), color=GREEN, alpha=0.13)
    ax.fill_between(S, pl, 0, where=(pl < 0), color=RED, alpha=0.13)
    ax.set_title("IRON CONDOR — profit if price stays in a RANGE; capped loss if it breaks out",
                 fontweight="bold")
    ax.set_xlabel("Price of stock at expiry"); ax.set_ylabel("Profit / Loss")
    ax.annotate("max profit\n(price stays 95–105)", xy=(100, 2), xytext=(100, 0.6),
                ha="center", fontsize=8.5, color=GREEN)
    ax.text(83, -3.4, "capped LOSS\nif it breaks out", ha="center", fontsize=8.5, color=RED)
    ax.text(117, -3.4, "capped LOSS\nif it breaks out", ha="center", fontsize=8.5, color=RED)
    save(fig, "p5_iron_condor.png")


# 2) TRENDLINE — rising line under the higher lows of an uptrend, with bounces
def trendline():
    np.random.seed(3)
    x = np.arange(130)
    support = 100 + x * 0.32                       # the rising trendline (support)
    price = support + 9 * np.abs(np.sin(x / 14)) + np.random.randn(130) * 0.7
    fig, ax = plt.subplots(figsize=(11, 5.2))
    ax.plot(x, price, color=BLUE, lw=1.4, label="Price")
    ax.plot(x, support, color=GREEN, ls="--", lw=1.8, label="Trendline (rising support)")
    # bounce points = where price comes closest to the support line (the higher lows)
    gap = price - support
    mins = argrelextrema(gap, np.less, order=8)[0]
    dy = (price.max() - price.min()) * 0.06
    for i in [m for m in mins if gap[m] < 2][:4]:
        ax.annotate("bounce", xy=(x[i], price[i]), xytext=(x[i], price[i] - dy),
                    ha="center", fontsize=9, color=GREEN, fontweight="bold",
                    arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.8))
    ax.set_title("TRENDLINE — connect the HIGHER LOWS of an uptrend; price bounces off it (support)",
                 fontweight="bold")
    ax.legend(loc="upper left", fontsize=9); ax.set_xticks([])
    save(fig, "p2_trendlines.png")


# 3) GAPS — show a clear overnight gap
def gaps():
    fig, ax = plt.subplots(figsize=(11, 5.0))
    # rising candles, then a clear GAP UP, then continuation
    data = [(0, 100, 101, 99.3, 100.6), (1, 100.6, 101.6, 100.1, 101.1),
            (2, 101.1, 102.0, 100.6, 101.6), (3, 101.6, 102.6, 101.1, 102.1),
            (4, 102.1, 103.1, 101.6, 102.6), (5, 102.6, 103.6, 102.1, 103.1),
            (6, 103.1, 104.0, 102.7, 103.6),
            # --- GAP UP: opens at 109, far above the prior close 103.6 ---
            (7, 109.0, 110.2, 108.6, 109.8), (8, 109.8, 110.8, 109.2, 110.3),
            (9, 110.3, 111.3, 109.8, 110.9), (10, 110.9, 112.0, 110.4, 111.6)]
    for i, o, h, l, c in data:
        candle(ax, i, o, h, l, c)
    # highlight the empty gap zone between candle 6 (high 104) and candle 7 (low 108.6)
    ax.add_patch(Rectangle((6.5, 104.0), 1.0, 4.6, facecolor="#ffe8cc", edgecolor=AMBER, lw=1.5, ls="--", zorder=1))
    ax.annotate("GAP UP\n(price jumps overnight on big news;\ngaps often get 'filled' later)",
                xy=(7, 106.3), xytext=(2.2, 107.5), fontsize=9.5, color="#9a6b00", fontweight="bold",
                arrowprops=dict(arrowstyle="-|>", color=AMBER, lw=2))
    ax.set_title("GAP — the empty space where price jumps between sessions", fontweight="bold")
    ax.set_xticks([]); ax.set_ylim(98, 113); ax.set_xlim(-0.6, 10.6)
    save(fig, "p2_gaps.png")


# 4) OPTION CHAIN OI — call OI peaks ABOVE spot (resistance), put OI peaks BELOW spot (support)
def oi_chain():
    strikes = np.arange(23000, 25001, 200)            # 11 strikes
    spot = 24000
    put_oi = np.array([2, 4, 8, 15, 11, 7, 5, 3, 2, 2, 1])   # peak at 23600 (below spot)
    call_oi = np.array([1, 2, 3, 4, 6, 8, 11, 15, 10, 6, 3])  # peak at 24400 (above spot)
    res = strikes[int(call_oi.argmax())]
    sup = strikes[int(put_oi.argmax())]
    fig, ax = plt.subplots(figsize=(11, 5.0))
    w = 70
    ax.bar(strikes - w, call_oi, width=2 * w, color=RED, alpha=0.75, label="Call OI (resistance)")
    ax.bar(strikes + w, put_oi, width=2 * w, color=GREEN, alpha=0.75, label="Put OI (support)")
    ax.axvline(spot, color=BLUE, lw=2); ax.text(spot + 30, max(call_oi) * 0.95, "spot", color=BLUE, fontweight="bold")
    ax.axvline(res, color=RED, ls="--", lw=1.6); ax.text(res, max(call_oi) + 0.4, "highest CALL OI\n= resistance",
                                                         color=RED, fontsize=8.5, ha="center")
    ax.axvline(sup, color=GREEN, ls="--", lw=1.6); ax.text(sup, max(put_oi) + 0.4, "highest PUT OI\n= support",
                                                           color=GREEN, fontsize=8.5, ha="center")
    ax.set_title("OPTION CHAIN — highest Call OI (above spot) = resistance; highest Put OI (below) = support",
                 fontweight="bold")
    ax.set_xlabel("Strike price"); ax.set_ylabel("Open Interest (lakh)")
    ax.legend(loc="upper right", fontsize=9); ax.set_ylim(0, max(call_oi) + 3)
    save(fig, "p5_oi_chain.png")


# 5) SUPPORT/RESISTANCE — tighten so SELL only marks touches genuinely near resistance
def sr():
    df = load(); c = df["Close"]
    res = float(c.max()); sup = float(c.min()); rng = res - sup
    dy = rng * 0.07
    fig, ax = plt.subplots(figsize=(11, 5.4))
    ax.plot(c.index, c.values, color=BLUE, lw=1.4)
    hline(ax, res, RED, "RESISTANCE (sell zone)", c.index[2])
    hline(ax, sup, GREEN, "SUPPORT (buy zone)", c.index[2])
    mins = argrelextrema(c.values, np.less, order=6)[0]
    maxs = argrelextrema(c.values, np.greater, order=6)[0]
    for i in [j for j in mins if c.iloc[j] <= sup + 0.08 * rng][:3]:
        mark_buy(ax, c.index[i], c.iloc[i], dy)
    for i in [j for j in maxs if c.iloc[j] >= res - 0.08 * rng][:3]:
        mark_sell(ax, c.index[i], c.iloc[i], dy)
    ax.set_title("SUPPORT & RESISTANCE (Nifty) — BUY near the floor, SELL near the ceiling",
                 fontweight="bold")
    save(fig, "04_support_resistance.png")


def main():
    iron_condor(); trendline(); gaps(); oi_chain(); sr()
    print("Fixed 5 charts.")


if __name__ == "__main__":
    main()
