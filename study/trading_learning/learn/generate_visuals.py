"""
Generate annotated, beginner-friendly chart images that VISUALLY explain every
core technical-analysis concept. Saves PNGs into ./img which are then compiled
into a visual learning PDF.
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

GREEN, RED = "#1a9850", "#d73027"


def save(fig, name):
    path = os.path.join(IMG, name)
    fig.tight_layout()
    fig.savefig(path, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print("  ->", name)


def candle(ax, x, o, h, l, c, w=0.55):
    color = GREEN if c >= o else RED
    ax.plot([x, x], [l, h], color="black", lw=1.4, zorder=1)
    ax.add_patch(Rectangle((x - w / 2, min(o, c)), w, max(abs(c - o), 0.01),
                           color=color, ec="black", lw=1.2, zorder=2))


# ---------- 1. Candle anatomy ----------
def fig_anatomy():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    candle(ax, 1, 20, 28, 18, 26)   # green
    candle(ax, 3, 26, 30, 16, 18)   # red
    ax.set_xlim(0, 5); ax.set_ylim(14, 33)
    ax.set_title("Anatomy of a Candlestick (one candle = one day)", fontweight="bold")
    # green labels
    ann = dict(arrowprops=dict(arrowstyle="->", color="black"), fontsize=10)
    ax.annotate("HIGH (highest price)", xy=(1, 28), xytext=(1.4, 31), **ann)
    ax.annotate("CLOSE (green = closed UP)", xy=(1.27, 26), xytext=(1.6, 27.5), **ann)
    ax.annotate("OPEN", xy=(1.27, 20), xytext=(1.6, 21.5), **ann)
    ax.annotate("LOW (lowest price)", xy=(1, 18), xytext=(1.4, 15.2), **ann)
    ax.annotate("upper wick\n(shadow)", xy=(1, 27), xytext=(0.05, 28.5), **ann)
    ax.annotate("BODY\n(open-to-close)", xy=(0.72, 23), xytext=(0.05, 22), **ann)
    ax.annotate("lower wick", xy=(1, 19), xytext=(0.05, 16.5), **ann)
    # red labels
    ax.annotate("RED = closed DOWN\n(close below open)", xy=(3, 17.5),
                xytext=(3.3, 14.8), **ann)
    ax.annotate("OPEN", xy=(3.27, 26), xytext=(3.6, 27.5), **ann)
    ax.annotate("CLOSE", xy=(3.27, 18), xytext=(3.6, 20), **ann)
    ax.set_xticks([1, 3]); ax.set_xticklabels(["Up day (bullish)", "Down day (bearish)"])
    save(fig, "01_anatomy.png")


# ---------- 2. Candlestick patterns ----------
def fig_patterns():
    fig, axes = plt.subplots(1, 4, figsize=(13, 4.2))
    # Doji
    ax = axes[0]
    candle(ax, 1, 20, 22, 13, 22); candle(ax, 2, 14, 15, 8, 14)
    candle(ax, 3, 11, 18, 4, 11.2)  # doji: open~close
    ax.set_title("DOJI\nindecision / reversal"); ax.set_xlim(0, 4); ax.set_ylim(2, 24)
    ax.annotate("tiny body\n(open≈close)", xy=(3, 11), xytext=(0.2, 19),
                arrowprops=dict(arrowstyle="->"), fontsize=9)
    # Hammer
    ax = axes[1]
    candle(ax, 1, 22, 23, 16, 17); candle(ax, 2, 17, 18, 11, 12)
    candle(ax, 3, 13, 14.5, 5, 14)  # hammer: small body top, long lower wick
    ax.set_title("HAMMER\nbullish reversal"); ax.set_xlim(0, 4); ax.set_ylim(3, 25)
    ax.annotate("long lower wick =\nbuyers rejected\nlower prices", xy=(3, 8),
                xytext=(0.1, 18), arrowprops=dict(arrowstyle="->"), fontsize=9)
    # Bullish engulfing
    ax = axes[2]
    candle(ax, 1, 20, 21, 15, 16); candle(ax, 2, 16, 17, 12, 13)
    candle(ax, 3, 12, 20, 11, 19)  # big green engulfs prior red
    ax.set_title("BULLISH ENGULFING\nstrong reversal up"); ax.set_xlim(0, 4); ax.set_ylim(9, 23)
    ax.annotate("big green candle\nswallows the\nprior red one", xy=(3, 15.5),
                xytext=(0.1, 20), arrowprops=dict(arrowstyle="->"), fontsize=9)
    # Shooting star
    ax = axes[3]
    candle(ax, 1, 10, 12, 9, 12); candle(ax, 2, 12, 16, 11, 16)
    candle(ax, 3, 17, 25, 16, 17.6)  # small body bottom, long upper wick
    ax.set_title("SHOOTING STAR\nbearish reversal"); ax.set_xlim(0, 4); ax.set_ylim(8, 27)
    ax.annotate("long upper wick =\nsellers rejected\nhigher prices", xy=(3, 23),
                xytext=(0.1, 12), arrowprops=dict(arrowstyle="->"), fontsize=9)
    fig.suptitle("Key Candlestick Patterns", fontweight="bold", y=1.04)
    save(fig, "p2_patterns.png")


# ---------- 3. Trend ----------
def fig_trend():
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.6))
    x = np.arange(20)
    up = np.array([10, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30])
    dn = up[::-1]
    axes[0].plot(x, up, color=GREEN, lw=2, marker="o", ms=3)
    axes[0].set_title("UPTREND = Higher Highs + Higher Lows", fontweight="bold", color=GREEN)
    axes[0].annotate("higher high", xy=(17, 28), xytext=(9, 29), fontsize=9,
                     arrowprops=dict(arrowstyle="->"))
    axes[0].annotate("higher low", xy=(16, 25), xytext=(9, 21), fontsize=9,
                     arrowprops=dict(arrowstyle="->"))
    axes[0].text(0.5, 27, '"Trade WITH the trend"\nLook to BUY dips', fontsize=10,
                 bbox=dict(boxstyle="round", fc="#eafaf0"))
    axes[1].plot(x, dn, color=RED, lw=2, marker="o", ms=3)
    axes[1].set_title("DOWNTREND = Lower Highs + Lower Lows", fontweight="bold", color=RED)
    axes[1].text(9, 27, "Look to SELL rallies\n(or stay out)", fontsize=10,
                 bbox=dict(boxstyle="round", fc="#fdecea"))
    save(fig, "03_trend.png")


# ---------- data for real-chart figures ----------
def load(t="^NSEI", period="1y"):
    df = yf.download(t, period=period, progress=False, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df[["Open", "High", "Low", "Close"]].dropna()


# ---------- 4. Support & Resistance ----------
def fig_sr(df):
    c = df["Close"]
    fig, ax = plt.subplots(figsize=(11, 5.2))
    ax.plot(c.index, c.values, color="#1f4e79", lw=1.3)
    res = c.quantile(0.92); sup = c.quantile(0.10)
    ax.axhline(res, color=RED, ls="--", lw=1.6)
    ax.axhline(sup, color=GREEN, ls="--", lw=1.6)
    ax.text(c.index[2], res, "  RESISTANCE  (ceiling — sellers step in)",
            color=RED, va="bottom", fontsize=10, fontweight="bold")
    ax.text(c.index[2], sup, "  SUPPORT  (floor — buyers step in)",
            color=GREEN, va="bottom", fontsize=10, fontweight="bold")
    ax.set_title("Support & Resistance (Nifty 50) — price bounces between a floor and a ceiling",
                 fontweight="bold")
    save(fig, "04_support_resistance.png")


# ---------- 5. Moving averages ----------
def fig_ma(df):
    c = df["Close"]
    ma20, ma50 = c.rolling(20).mean(), c.rolling(50).mean()
    fig, ax = plt.subplots(figsize=(11, 5.2))
    ax.plot(c.index, c.values, color="#999", lw=1, label="Price (daily close)")
    ax.plot(ma20.index, ma20, color="#1a9850", lw=1.8, label="20-day MA (fast)")
    ax.plot(ma50.index, ma50, color="#d73027", lw=1.8, label="50-day MA (slow)")
    ax.set_title("Moving Averages (Nifty 50) — smoothed trend lines",
                 fontweight="bold")
    ax.text(0.015, 0.05,
            "Price ABOVE the MAs = uptrend.\nWhen the fast MA crosses ABOVE the slow MA = bullish signal.",
            transform=ax.transAxes, fontsize=9.5,
            bbox=dict(boxstyle="round", fc="#eef5ff"))
    ax.legend(loc="upper left", fontsize=9)
    save(fig, "05_moving_averages.png")


# ---------- 6. RSI ----------
def fig_rsi(df):
    c = df["Close"]
    d = c.diff(); g = d.clip(lower=0).rolling(14).mean(); l = (-d.clip(upper=0)).rolling(14).mean()
    rsi = 100 - 100 / (1 + g / l.replace(0, np.nan))
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 6.4), sharex=True,
                                 gridspec_kw={"height_ratios": [2, 1]})
    a1.plot(c.index, c.values, color="#1f4e79", lw=1.3)
    a1.set_title("RSI — momentum: is the move overstretched?", fontweight="bold")
    a2.plot(rsi.index, rsi, color="#6a3d9a", lw=1.3)
    a2.axhline(70, color=RED, ls="--", lw=1); a2.axhline(30, color=GREEN, ls="--", lw=1)
    a2.axhspan(70, 100, color=RED, alpha=0.08); a2.axhspan(0, 30, color=GREEN, alpha=0.08)
    a2.set_ylim(0, 100); a2.set_ylabel("RSI")
    a2.text(rsi.index[2], 86, "ABOVE 70 = OVERBOUGHT (may fall)", color=RED, fontsize=9)
    a2.text(rsi.index[2], 16, "BELOW 30 = OVERSOLD (may bounce)", color=GREEN, fontsize=9)
    save(fig, "06_rsi.png")


# ---------- 7. MACD ----------
def fig_macd(df):
    c = df["Close"]
    macd = c.ewm(span=12, adjust=False).mean() - c.ewm(span=26, adjust=False).mean()
    sig = macd.ewm(span=9, adjust=False).mean(); hist = macd - sig
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 6.4), sharex=True,
                                 gridspec_kw={"height_ratios": [2, 1]})
    a1.plot(c.index, c.values, color="#1f4e79", lw=1.3)
    a1.set_title("MACD — trend & momentum together", fontweight="bold")
    a2.plot(macd.index, macd, color="#1a9850", lw=1.3, label="MACD line")
    a2.plot(sig.index, sig, color="#d73027", lw=1.3, label="Signal line")
    a2.bar(hist.index, hist, color=np.where(hist >= 0, "#9ad0a8", "#f2a8a0"), width=1.0)
    a2.axhline(0, color="#888", lw=0.8)
    a2.legend(loc="upper left", fontsize=8)
    a2.text(macd.index[2], a2.get_ylim()[1] * 0.6,
            "Green line crossing ABOVE red = bullish signal", fontsize=9)
    save(fig, "07_macd.png")


# ---------- 8. Bollinger Bands ----------
def fig_bb(df):
    c = df["Close"]; ma = c.rolling(20).mean(); sd = c.rolling(20).std()
    up, dn = ma + 2 * sd, ma - 2 * sd
    fig, ax = plt.subplots(figsize=(11, 5.2))
    ax.plot(c.index, c.values, color="#1f4e79", lw=1.3, label="Price")
    ax.plot(ma.index, ma, color="#888", lw=1, label="20-day MA (middle)")
    ax.plot(up.index, up, color=RED, lw=1, label="Upper band (+2σ)")
    ax.plot(dn.index, dn, color=GREEN, lw=1, label="Lower band (−2σ)")
    ax.fill_between(c.index, dn, up, color="#cfe0f5", alpha=0.35)
    ax.set_title("Bollinger Bands — volatility envelope around price", fontweight="bold")
    ax.text(0.015, 0.05,
            "Bands WIDE = volatile.  Bands NARROW ('squeeze') = calm before a big move.\n"
            "Near upper band = strong/overbought · near lower band = weak/oversold.",
            transform=ax.transAxes, fontsize=9, bbox=dict(boxstyle="round", fc="#eef5ff"))
    ax.legend(loc="upper left", fontsize=8)
    save(fig, "08_bollinger.png")


# ---------- 9. Fibonacci retracement ----------
def fig_fib(df):
    c = df["Close"]
    lo_idx = c.idxmin(); hi_idx = c.loc[lo_idx:].idxmax()
    lo, hi = c.loc[lo_idx], c.loc[hi_idx]
    diff = hi - lo
    levels = {"0% (high)": hi, "23.6%": hi - .236 * diff, "38.2%": hi - .382 * diff,
              "50%": hi - .5 * diff, "61.8%": hi - .618 * diff, "100% (low)": lo}
    fig, ax = plt.subplots(figsize=(11, 5.2))
    ax.plot(c.index, c.values, color="#1f4e79", lw=1.3)
    for name, lvl in levels.items():
        ax.axhline(lvl, color="#b8860b", ls="--", lw=0.9)
        ax.text(c.index[1], lvl, f"  {name}", color="#7a5c00", fontsize=9, va="bottom")
    ax.set_title("Fibonacci Retracement — where pullbacks often pause (38.2–61.8%)",
                 fontweight="bold")
    ax.text(0.015, 0.05, "After a big up-move, price often pulls back to one of these levels\n"
                          "before continuing. 61.8% is the most watched.",
            transform=ax.transAxes, fontsize=9, bbox=dict(boxstyle="round", fc="#fff7e6"))
    save(fig, "09_fibonacci.png")


# ---------- 10. Full buy setup ----------
def fig_setup(df):
    c = df["Close"].copy()
    ma20 = c.rolling(20).mean()
    fig, ax = plt.subplots(figsize=(11, 5.4))
    ax.plot(c.index, c.values, color="#1f4e79", lw=1.4, label="Price")
    ax.plot(ma20.index, ma20, color="#1a9850", lw=1.5, label="20-day MA (support in uptrend)")
    entry = c.iloc[-1]
    stop = entry * 0.97
    target = entry * 1.06
    ax.axhline(entry, color="#1f4e79", ls="-", lw=1)
    ax.axhline(stop, color=RED, ls="--", lw=1.2)
    ax.axhline(target, color=GREEN, ls="--", lw=1.2)
    ax.text(c.index[1], entry, "  ENTRY (buy here)", fontsize=9.5, va="bottom", color="#1f4e79")
    ax.text(c.index[1], stop, "  STOP-LOSS (exit if wrong)", fontsize=9.5, va="bottom", color=RED)
    ax.text(c.index[1], target, "  TARGET (book profit)", fontsize=9.5, va="bottom", color=GREEN)
    ax.set_title("Putting It Together — a BUY setup with Entry, Stop & Target",
                 fontweight="bold")
    ax.text(0.015, 0.04,
            "Checklist:  uptrend ✓   pullback to the 20-MA support ✓   then BUY,\n"
            "with a STOP just below and a TARGET above (reward bigger than risk).",
            transform=ax.transAxes, fontsize=9, bbox=dict(boxstyle="round", fc="#eafaf0"))
    ax.legend(loc="upper left", fontsize=8)
    save(fig, "10_setup.png")


def main():
    print("Building visuals...")
    fig_anatomy(); fig_patterns(); fig_trend()
    nifty = load("^NSEI", "1y")
    fig_sr(nifty); fig_ma(nifty); fig_rsi(nifty); fig_macd(nifty)
    fig_bb(nifty); fig_fib(nifty); fig_setup(nifty)
    print("Done. Images in ./img")


if __name__ == "__main__":
    main()
