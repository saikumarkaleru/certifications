"""
Generate SEPARATE single-concept charts (one idea per image), so each gets its own
card and its own explanation in the guide — no two different things side by side.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

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
                fontweight="bold", color="white",
                bbox=dict(boxstyle="round,pad=0.25", fc=GREEN, ec="none"),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2))


def mark_sell(ax, x, y, dy):
    ax.annotate("SELL", xy=(x, y), xytext=(x, y + dy), ha="center", fontsize=10.5,
                fontweight="bold", color="white",
                bbox=dict(boxstyle="round,pad=0.25", fc=RED, ec="none"),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2))


def hline(ax, y, color, label, xpos=0):
    ax.axhline(y, color=color, ls=":", lw=1.6)
    ax.text(xpos, y, f" {label}", color=color, va="bottom", fontsize=9.5, fontweight="bold")


def circle(ax, cx, cy, w, h, label=None):
    ax.add_patch(Ellipse((cx, cy), w, h, fill=False, edgecolor=PURP, lw=2.4, ls="--"))
    if label:
        ax.text(cx, cy + h / 2 + h * 0.08, label, ha="center", color=PURP,
                fontsize=9.5, fontweight="bold")


# ----------------------- TRIANGLES (3 separate) -----------------------
def tri_ascending():
    x = np.arange(10)
    y = np.array([8, 16, 9.5, 16, 11, 16, 12.5, 16, 14, 18.5])
    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    ax.plot(x, y, color=BLUE, lw=1.8, marker="o", ms=3)
    ax.plot(x, np.full(10, 16.2), color=RED, ls="--", lw=1.3)
    ax.text(0, 16.4, "flat resistance", color=RED, fontsize=9)
    ax.plot(x, 8 + x * 0.72, color=GREEN, ls="--", lw=1.3)
    ax.text(0.2, 8.2, "rising support", color=GREEN, fontsize=9)
    mark_buy(ax, 9, 18.5, 3)
    hline(ax, 13.5, RED, "STOP (inside)")
    hline(ax, 23, GREEN, "TARGET (= triangle height)")
    ax.set_title("ASCENDING TRIANGLE — usually breaks UP (bullish)", fontweight="bold", color=GREEN)
    ax.set_xticks([]); ax.set_ylim(6, 26)
    save(fig, "p2_tri_ascending.png")


def tri_descending():
    x = np.arange(10)
    y = np.array([16, 8, 15, 8, 13.5, 8, 12, 8, 10.5, 6])
    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    ax.plot(x, y, color=BLUE, lw=1.8, marker="o", ms=3)
    ax.plot(x, np.full(10, 7.8), color=GREEN, ls="--", lw=1.3)
    ax.text(0, 8.0, "flat support", color=GREEN, fontsize=9)
    ax.plot(x, 16 - x * 0.72, color=RED, ls="--", lw=1.3)
    ax.text(0.2, 15.4, "falling resistance", color=RED, fontsize=9)
    mark_sell(ax, 9, 6, 3)
    hline(ax, 10.5, GREEN, "STOP (inside)")
    hline(ax, 1.5, RED, "TARGET (= triangle height)")
    ax.set_title("DESCENDING TRIANGLE — usually breaks DOWN (bearish)", fontweight="bold", color=RED)
    ax.set_xticks([]); ax.set_ylim(0, 18)
    save(fig, "p2_tri_descending.png")


def tri_symmetric():
    x = np.arange(10)
    y = np.array([8, 16, 9.5, 15, 11, 14, 12, 13, 12.4, 17])
    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    ax.plot(x, y, color=BLUE, lw=1.8, marker="o", ms=3)
    ax.plot(x, 16.5 - x * 0.5, color=RED, ls="--", lw=1.3)
    ax.plot(x, 7.5 + x * 0.5, color=GREEN, ls="--", lw=1.3)
    ax.text(0.2, 7.6, "both lines converging", color="#555", fontsize=9)
    mark_buy(ax, 9, 17, 3)
    hline(ax, 11.5, RED, "STOP (other side)")
    hline(ax, 21, GREEN, "TARGET")
    ax.set_title("SYMMETRICAL TRIANGLE — breaks in the EXISTING trend's direction",
                 fontweight="bold", color=AMBER)
    ax.set_xticks([]); ax.set_ylim(5, 24)
    save(fig, "p2_tri_symmetric.png")


# ----------------------- FLAG and CUP (separate) -----------------------
def bull_flag():
    x = np.arange(16)
    y = np.concatenate([np.linspace(8, 18, 7), np.linspace(17.5, 15, 5), np.linspace(15.5, 25, 4)])
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    ax.plot(x, y, color=BLUE, lw=2)
    circle(ax, 9, 16.2, 3.2, 3.2, "flag (pause)")
    ax.annotate("flagpole\n(sharp rally)", xy=(3, 13), xytext=(0.2, 19), fontsize=9,
                arrowprops=dict(arrowstyle="->"))
    mark_buy(ax, 13, 21, 3.2)
    hline(ax, 14.5, RED, "STOP (below flag)")
    hline(ax, 25.5, GREEN, "TARGET (= flagpole height)")
    ax.set_title("BULL FLAG — a brief pause, then the trend continues UP", fontweight="bold", color=GREEN)
    ax.set_xticks([]); ax.set_ylim(6, 28)
    save(fig, "p2_flag.png")


def cup_handle():
    t = np.linspace(0, np.pi, 60)
    cup = 14 - 4 * np.sin(t)
    x = np.concatenate([np.arange(60), np.arange(60, 75)])
    handle = np.concatenate([np.linspace(14, 12.5, 8), np.linspace(12.5, 18, 7)])
    y = np.concatenate([cup, handle])
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    ax.plot(x, y, color=BLUE, lw=2)
    ax.annotate("cup (rounded base)", xy=(30, 10.4), xytext=(18, 8.4), fontsize=9,
                arrowprops=dict(arrowstyle="->"))
    circle(ax, 66, 13.2, 10, 3, "handle")
    mark_buy(ax, 72, 17, 3)
    hline(ax, 12, RED, "STOP (below handle)")
    hline(ax, 19.5, GREEN, "TARGET (= cup depth)")
    ax.set_title("CUP & HANDLE — rounded base + small dip, then breaks UP", fontweight="bold", color=GREEN)
    ax.set_xticks([]); ax.set_ylim(7, 21)
    save(fig, "p2_cup.png")


# ----------------------- DOUBLE bottom / top (separate) -----------------------
def double_bottom():
    x = np.arange(9)
    y = np.array([18, 13, 9, 12.5, 9, 12.5, 15, 17, 19])
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    ax.plot(x, y, color=BLUE, lw=2, marker="o", ms=4)
    ax.axhline(12.7, color=AMBER, ls="--", lw=1.4); ax.text(0, 12.9, "neckline", color="#7a5c00", fontsize=9)
    circle(ax, 2, 9, 1.0, 2.2); circle(ax, 4, 9, 1.0, 2.2, "two equal bottoms")
    mark_buy(ax, 6, 15, 2.6)
    hline(ax, 8.3, RED, "STOP (below bottoms)")
    hline(ax, 18.5, GREEN, "TARGET (= pattern height)")
    ax.set_title("DOUBLE BOTTOM (W) — reversal UP, BUY the neckline break", fontweight="bold", color=GREEN)
    ax.set_xticks([]); ax.set_ylim(6, 21)
    save(fig, "p2_double_bottom.png")


def double_top():
    x = np.arange(9)
    y = np.array([8, 13, 17, 13.5, 17, 13.5, 11, 9, 7])
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    ax.plot(x, y, color=BLUE, lw=2, marker="o", ms=4)
    ax.axhline(13.3, color=AMBER, ls="--", lw=1.4); ax.text(0, 13.5, "neckline", color="#7a5c00", fontsize=9)
    circle(ax, 2, 17, 1.0, 2.2); circle(ax, 4, 17, 1.0, 2.2, "two equal tops")
    mark_sell(ax, 6, 11, 2.4)
    hline(ax, 17.7, RED, "STOP (above tops)")
    hline(ax, 7.5, GREEN, "TARGET (= pattern height)")
    ax.set_title("DOUBLE TOP (M) — reversal DOWN, SELL the neckline break", fontweight="bold", color=RED)
    ax.set_xticks([]); ax.set_ylim(5, 20)
    save(fig, "p2_double_top.png")


# ----------------------- OPTION PAYOFFS (separate) -----------------------
def payoff(ax, S, pl, title, col):
    ax.plot(S, pl, color=col, lw=2.4)
    ax.axhline(0, color="#888", lw=1)
    ax.fill_between(S, pl, 0, where=(pl > 0), color=GREEN, alpha=0.13)
    ax.fill_between(S, pl, 0, where=(pl < 0), color=RED, alpha=0.13)
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel("Price of stock at expiry"); ax.set_ylabel("Profit / Loss")


def long_call():
    S = np.linspace(80, 120, 200); K, p = 100, 4
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    payoff(ax, S, np.maximum(S - K, 0) - p, "LONG CALL (bullish) — buy if you expect price to RISE", GREEN)
    ax.axvline(104, color="#888", ls=":"); ax.text(104.3, -3, "breakeven\n(strike+premium)", fontsize=8)
    save(fig, "p5_call.png")


def long_put():
    S = np.linspace(80, 120, 200); K, p = 100, 4
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    payoff(ax, S, np.maximum(K - S, 0) - p, "LONG PUT (bearish) — buy if you expect price to FALL", RED)
    ax.axvline(96, color="#888", ls=":"); ax.text(86, -3, "breakeven\n(strike-premium)", fontsize=8)
    save(fig, "p5_put.png")


def covered_call():
    S = np.linspace(80, 120, 200); K, p = 100, 4
    pl = (S - 100) + p - np.maximum(S - K, 0)
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    payoff(ax, S, pl, "COVERED CALL — own the stock + sell a call for income (upside capped)", AMBER)
    save(fig, "p5_covered_call.png")


def straddle():
    S = np.linspace(80, 120, 200); K = 100
    pl = np.maximum(S - K, 0) + np.maximum(K - S, 0) - 8
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    payoff(ax, S, pl, "LONG STRADDLE — buy call + put; profit from a BIG move EITHER way", BLUE)
    ax.text(100, -7, "loses if price\nstays flat", fontsize=8.5, ha="center", color=RED)
    save(fig, "p5_straddle.png")


def bull_spread():
    S = np.linspace(80, 120, 200)
    pl = (np.maximum(S - 100, 0) - 3) - (np.maximum(S - 108, 0) - 1)
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    payoff(ax, S, pl, "BULL CALL SPREAD — buy a call, sell a higher one; capped risk AND reward", GREEN)
    save(fig, "p5_bull_spread.png")


def iron_condor():
    S = np.linspace(80, 120, 200)
    pl = (3 - np.maximum(92 - S, 0)) + (3 - np.maximum(S - 108, 0)) \
         - (1 - np.maximum(88 - S, 0)) - (1 - np.maximum(S - 112, 0))
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    payoff(ax, S, pl, "IRON CONDOR — profit when price stays RANGE-BOUND (income strategy)", AMBER)
    save(fig, "p5_iron_condor.png")


def main():
    print("Triangles...")
    tri_ascending(); tri_descending(); tri_symmetric()
    print("Flag & cup...")
    bull_flag(); cup_handle()
    print("Double bottom/top...")
    double_bottom(); double_top()
    print("Option payoffs...")
    long_call(); long_put(); covered_call(); straddle(); bull_spread(); iron_condor()
    print("Done.")


if __name__ == "__main__":
    main()
