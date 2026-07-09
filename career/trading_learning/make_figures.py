"""
Figure generator for the Options Trading book.
Self-contained Black-Scholes pricer + Greeks + payoff engine -> clean matplotlib PNGs in figs/.
India-scale examples (Nifty ~ 24000). Run: python make_figures.py
"""
import os, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import log, sqrt, exp, erf, pi

FIGS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
os.makedirs(FIGS, exist_ok=True)

NAVY, GREEN, RED, BLUE, AMBER, PURPLE, GREY = "#16365c", "#16a34a", "#dc2626", "#2563eb", "#f59e0b", "#7c3aed", "#94a3b8"
plt.rcParams.update({"font.size": 9, "axes.edgecolor": "#cbd5e1", "figure.dpi": 120})


def style(ax, title, xl="Nifty at expiry", yl="Profit / Loss (points per unit)"):
    ax.set_title(title, color=NAVY, fontsize=11, weight="bold")
    ax.set_xlabel(xl, fontsize=9); ax.set_ylabel(yl, fontsize=9)
    ax.grid(alpha=0.25); ax.axhline(0, color="#334155", lw=0.8)
    ax.tick_params(labelsize=8)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIGS, name + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


# ---- Black-Scholes-Merton ----
def Nf(x): return 0.5 * (1 + erf(x / sqrt(2)))
def npdf(x): return exp(-x * x / 2) / sqrt(2 * pi)
def _d1(S, K, T, r, sig, q=0): return (log(S / K) + (r - q + 0.5 * sig * sig) * T) / (sig * sqrt(T))

def bs(S, K, T, r, sig, call=True, q=0):
    if T <= 0: return max(0.0, (S - K) if call else (K - S))
    D1 = _d1(S, K, T, r, sig, q); D2 = D1 - sig * sqrt(T)
    return (S * exp(-q * T) * Nf(D1) - K * exp(-r * T) * Nf(D2)) if call \
        else (K * exp(-r * T) * Nf(-D2) - S * exp(-q * T) * Nf(-D1))

def delta(S, K, T, r, sig, call=True, q=0):
    D1 = _d1(S, K, T, r, sig, q); return exp(-q * T) * (Nf(D1) if call else Nf(D1) - 1)
def gamma(S, K, T, r, sig, q=0):
    D1 = _d1(S, K, T, r, sig, q); return exp(-q * T) * npdf(D1) / (S * sig * sqrt(T))
def vega(S, K, T, r, sig, q=0):
    D1 = _d1(S, K, T, r, sig, q); return S * exp(-q * T) * npdf(D1) * sqrt(T) / 100
def theta(S, K, T, r, sig, call=True, q=0):
    D1 = _d1(S, K, T, r, sig, q); D2 = D1 - sig * sqrt(T)
    base = -S * exp(-q * T) * npdf(D1) * sig / (2 * sqrt(T))
    th = base - r * K * exp(-r * T) * Nf(D2) if call else base + r * K * exp(-r * T) * Nf(-D2)
    return th / 365
def rho(S, K, T, r, sig, call=True, q=0):
    D2 = _d1(S, K, T, r, sig, q) - sig * sqrt(T)
    return (K * T * exp(-r * T) * (Nf(D2) if call else -Nf(-D2))) / 100


# ---- payoff engine: legs = [(kind 'c'/'p'/'s', strike, qty(+long/-short), premium)] ----
def leg_pnl(S, kind, K, qty, prem):
    intr = np.maximum(S - K, 0) if kind == "c" else np.maximum(K - S, 0) if kind == "p" else (S - K)
    return qty * intr - qty * prem

def plot_payoff(name, title, legs, S0=24000, span=0.12, annotate=None):
    S = np.linspace(S0 * (1 - span), S0 * (1 + span), 500)
    pnl = sum(leg_pnl(S, *l) for l in legs)
    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.plot(S, pnl, color=NAVY, lw=2)
    ax.fill_between(S, pnl, 0, where=pnl >= 0, color=GREEN, alpha=0.16)
    ax.fill_between(S, pnl, 0, where=pnl < 0, color=RED, alpha=0.16)
    for l in legs:
        ax.axvline(l[1], color=GREY, ls=":", lw=0.7)
    if annotate:
        ax.text(0.02, 0.04, annotate, transform=ax.transAxes, fontsize=8, color="#334155",
                va="bottom", bbox=dict(boxstyle="round", fc="#f1f5f9", ec="#cbd5e1"))
    style(ax, title)
    save(fig, name)


def plot_greek(name, title, fn, K=24000, yl="value", color=BLUE, S0=24000, span=0.10):
    S = np.linspace(S0 * (1 - span), S0 * (1 + span), 400)
    y = [fn(s) for s in S]
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.plot(S, y, color=color, lw=2)
    ax.axvline(K, color=GREY, ls=":", lw=0.8)
    style(ax, title, "Nifty spot", yl)
    save(fig, name)


def main():
    S0, r = 24000, 0.07
    T, sig = 30 / 365, 0.15

    # ---- Part II: the four basic payoffs (premiums illustrative, points/unit) ----
    plot_payoff("long_call", "Long Call (buy 24000 CE @ 250)", [("c", 24000, 1, 250)],
                annotate="Max loss = 250 (premium)\nBreakeven = 24250\nUpside unlimited")
    plot_payoff("long_put", "Long Put (buy 24000 PE @ 240)", [("p", 24000, 1, 240)],
                annotate="Max loss = 240 (premium)\nBreakeven = 23760\nProfit as Nifty falls")
    plot_payoff("short_call", "Short Call (sell 24000 CE @ 250)", [("c", 24000, -1, 250)],
                annotate="Max profit = 250\nLoss unlimited above 24250")
    plot_payoff("short_put", "Short Put (sell 24000 PE @ 240)", [("p", 24000, -1, 240)],
                annotate="Max profit = 240\nLarge loss as Nifty falls")

    # ---- Part III: intrinsic vs time value, BSM price vs spot ----
    S = np.linspace(0.9 * S0, 1.1 * S0, 400)
    intr = np.maximum(S - S0, 0)
    val = np.array([bs(s, S0, T, r, sig, True) for s in S])
    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.plot(S, val, color=BLUE, lw=2, label="Option value (now)")
    ax.plot(S, intr, color=NAVY, lw=1.5, ls="--", label="Intrinsic value (at expiry)")
    ax.fill_between(S, val, intr, color=AMBER, alpha=0.25, label="Time value")
    ax.axvline(S0, color=GREY, ls=":", lw=0.8)
    style(ax, "Intrinsic vs Time Value (24000 Call)", "Nifty spot", "Option price (points)")
    ax.legend(fontsize=8); save(fig, "time_value")

    for days, col in [(3, RED), (15, AMBER), (45, GREEN)]:
        pass
    fig, ax = plt.subplots(figsize=(7, 3.2))
    for days, col, lbl in [(45, GREEN, "45d"), (15, AMBER, "15d"), (3, RED, "3d"), (0.0001, NAVY, "expiry")]:
        y = [bs(s, S0, days / 365, r, sig, True) for s in S]
        ax.plot(S, y, color=col, lw=1.8, label=lbl)
    ax.axvline(S0, color=GREY, ls=":", lw=0.8)
    style(ax, "Time decay: call value as expiry approaches", "Nifty spot", "Call price (points)")
    ax.legend(fontsize=8, title="Days left"); save(fig, "time_decay")

    # ---- Part IV: Greeks vs spot ----
    plot_greek("delta_call", "Call Delta vs Spot (30d, IV 15%)",
               lambda s: delta(s, 24000, T, r, sig, True), yl="Delta", color=BLUE)
    plot_greek("delta_put", "Put Delta vs Spot",
               lambda s: delta(s, 24000, T, r, sig, False), yl="Delta", color=BLUE)
    plot_greek("gamma", "Gamma vs Spot (peaks at-the-money)",
               lambda s: gamma(s, 24000, T, r, sig), yl="Gamma", color=PURPLE)
    plot_greek("vega", "Vega vs Spot (per 1% IV)",
               lambda s: vega(s, 24000, T, r, sig), yl="Vega (pts per 1% IV)", color=GREEN)
    plot_greek("theta", "Theta vs Spot (per day, long call)",
               lambda s: theta(s, 24000, T, r, sig, True), yl="Theta (pts/day)", color=RED)
    plot_greek("rho", "Rho vs Spot (per 1% rate, call)",
               lambda s: rho(s, 24000, T, r, sig, True), yl="Rho", color=AMBER)

    # gamma & theta vs days to expiry (ATM)
    days = np.linspace(60, 1, 200)
    g = [gamma(S0, S0, d / 365, r, sig) for d in days]
    th = [theta(S0, S0, d / 365, r, sig, True) for d in days]
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.plot(days, g, color=PURPLE, lw=2)
    ax.invert_xaxis(); style(ax, "ATM Gamma explodes near expiry", "Days to expiry", "Gamma")
    save(fig, "gamma_vs_time")
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.plot(days, th, color=RED, lw=2)
    ax.invert_xaxis(); style(ax, "ATM Theta (decay) accelerates near expiry", "Days to expiry", "Theta (pts/day)")
    save(fig, "theta_vs_time")

    # ---- Part V: volatility smile / skew / term structure ----
    K = np.linspace(0.85 * S0, 1.15 * S0, 200)
    smile = 0.15 + 0.0000000045 * (K - S0) ** 2
    skew = 0.20 - 0.0000028 * (K - S0)
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.plot(K, smile * 100, color=BLUE, lw=2)
    ax.axvline(S0, color=GREY, ls=":", lw=0.8)
    style(ax, "Volatility Smile (symmetric)", "Strike", "Implied volatility (%)")
    save(fig, "vol_smile")
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.plot(K, skew * 100, color=RED, lw=2)
    ax.axvline(S0, color=GREY, ls=":", lw=0.8)
    style(ax, "Equity-index Skew (puts bid, Nifty-style)", "Strike", "Implied volatility (%)")
    save(fig, "vol_skew")
    dte = np.array([7, 14, 30, 60, 90, 180])
    tsiv = np.array([12.5, 13.2, 14.0, 14.8, 15.3, 15.9])
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.plot(dte, tsiv, "o-", color=GREEN, lw=2)
    style(ax, "IV Term Structure (calm market, upward)", "Days to expiry", "ATM implied vol (%)")
    save(fig, "term_structure")

    # ---- Part VI: strategy payoffs (Nifty-scale, illustrative premiums) ----
    plot_payoff("bull_call_spread", "Bull Call Spread (+24000C 250 / -24300C 120)",
                [("c", 24000, 1, 250), ("c", 24300, -1, 120)],
                annotate="Net debit 130 | Max profit 170 | Max loss 130\nBreakeven 24130")
    plot_payoff("bear_put_spread", "Bear Put Spread (+24000P 240 / -23700P 110)",
                [("p", 24000, 1, 240), ("p", 23700, -1, 110)],
                annotate="Net debit 130 | Max profit 170 | Max loss 130")
    plot_payoff("bull_put_spread", "Bull Put Spread (-24000P 240 / +23700P 110)",
                [("p", 24000, -1, 240), ("p", 23700, 1, 110)],
                annotate="Net credit 130 | Max profit 130 | Max loss 170")
    plot_payoff("bear_call_spread", "Bear Call Spread (-24000C 250 / +24300C 120)",
                [("c", 24000, -1, 250), ("c", 24300, 1, 120)],
                annotate="Net credit 130 | Max profit 130 | Max loss 170")
    plot_payoff("long_straddle", "Long Straddle (+24000C 250 / +24000P 240)",
                [("c", 24000, 1, 250), ("p", 24000, 1, 240)],
                annotate="Cost 490 | BE 23510 & 24490\nProfits on a big move either way")
    plot_payoff("short_straddle", "Short Straddle (-24000C 250 / -24000P 240)",
                [("c", 24000, -1, 250), ("p", 24000, -1, 240)],
                annotate="Credit 490 | profits if Nifty stays near 24000\nLarge risk on a big move")
    plot_payoff("long_strangle", "Long Strangle (+24300C 120 / +23700P 110)",
                [("c", 24300, 1, 120), ("p", 23700, 1, 110)],
                annotate="Cost 230 | cheaper than straddle\nneeds a bigger move")
    plot_payoff("short_strangle", "Short Strangle (-24300C 120 / -23700P 110)",
                [("c", 24300, -1, 120), ("p", 23700, -1, 110)],
                annotate="Credit 230 | wide profit zone | big tail risk")
    plot_payoff("long_butterfly", "Long Call Butterfly (24000 body)",
                [("c", 23700, 1, 360), ("c", 24000, -2, 200), ("c", 24300, 1, 95)],
                annotate="Cheap, defined risk | max profit if Nifty pins 24000")
    plot_payoff("iron_butterfly", "Iron Butterfly (24000 body)",
                [("c", 24000, -1, 250), ("p", 24000, -1, 240), ("c", 24300, 1, 120), ("p", 23700, 1, 110)],
                annotate="Credit 260 | max profit if Nifty pins 24000")
    plot_payoff("iron_condor", "Iron Condor (-24300C/-23700P, wings 24600/23400)",
                [("c", 24300, -1, 120), ("c", 24600, 1, 45), ("p", 23700, -1, 110), ("p", 23400, 1, 40)],
                annotate="Credit 145 | wide profit zone 23555-24445\nDefined risk", span=0.10)
    plot_payoff("covered_call", "Covered Call (long Nifty @ 24000, -24300C @ 120)",
                [("s", 24000, 1, 24000), ("c", 24300, -1, 120)],
                annotate="Income 120 | caps upside at 24300\nstill exposed below")
    plot_payoff("protective_put", "Protective Put (long Nifty @ 24000, +23700P @ 110)",
                [("s", 24000, 1, 24000), ("p", 23700, 1, 110)],
                annotate="Insurance | downside floored near 23700\ncosts 110")
    plot_payoff("collar", "Collar (long Nifty, +23700P 110, -24300C 120)",
                [("s", 24000, 1, 24000), ("p", 23700, 1, 110), ("c", 24300, -1, 120)],
                annotate="Near-zero cost hedge | range-bound payoff")
    plot_payoff("ratio_spread", "Call Ratio Spread (+24000C / -2x 24300C)",
                [("c", 24000, 1, 250), ("c", 24300, -2, 120)],
                annotate="Cheap/credit | risk if Nifty rallies hard")
    plot_payoff("call_backspread", "Call Backspread (-24000C / +2x 24300C)",
                [("c", 24000, -1, 250), ("c", 24300, 2, 120)],
                annotate="Profits on a strong rally | small risk in middle")
    plot_payoff("synthetic_long", "Synthetic Long (+24000C 250 / -24000P 240)",
                [("c", 24000, 1, 250), ("p", 24000, -1, 240)],
                annotate="Mimics long futures | net debit 10")

    # long call before vs at expiry
    S = np.linspace(0.9 * S0, 1.1 * S0, 400)
    fig, ax = plt.subplots(figsize=(7, 3.2))
    atexp = np.maximum(S - 24000, 0) - 250
    now = np.array([bs(s, 24000, T, r, sig, True) for s in S]) - 250
    ax.plot(S, atexp, color=NAVY, lw=2, label="At expiry")
    ax.plot(S, now, color=BLUE, lw=2, ls="--", label="Today (30d left)")
    ax.fill_between(S, atexp, 0, where=atexp >= 0, color=GREEN, alpha=0.12)
    ax.fill_between(S, atexp, 0, where=atexp < 0, color=RED, alpha=0.12)
    style(ax, "Long Call: P&L now vs at expiry"); ax.legend(fontsize=8)
    save(fig, "long_call_time")

    # probability of profit (lognormal terminal) for a long straddle
    mu = log(S0) + (r - 0.5 * sig * sig) * T
    sd = sig * sqrt(T)
    x = np.linspace(0.82 * S0, 1.18 * S0, 500)
    pdf = (1 / (x * sd * sqrt(2 * pi))) * np.exp(-(np.log(x) - mu) ** 2 / (2 * sd * sd))
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.plot(x, pdf, color=NAVY, lw=2)
    for be in (23510, 24490):
        ax.axvline(be, color=RED, ls="--", lw=1)
    ax.fill_between(x, pdf, 0, where=(x < 23510) | (x > 24490), color=GREEN, alpha=0.2)
    style(ax, "Where Nifty might expire (lognormal) + straddle breakevens", "Nifty at expiry", "Probability density")
    save(fig, "pop_distribution")

    # binomial one-step tree diagram
    fig, ax = plt.subplots(figsize=(7, 3.4))
    ax.plot([0, 1], [0, 1], color=NAVY, lw=1.5); ax.plot([0, 1], [0, -1], color=NAVY, lw=1.5)
    ax.plot([1, 2], [1, 2], color=NAVY, lw=1.5); ax.plot([1, 2], [1, 0], color=NAVY, lw=1.5)
    ax.plot([1, 2], [-1, 0], color=NAVY, lw=1.5); ax.plot([1, 2], [-1, -2], color=NAVY, lw=1.5)
    pts = {(0, 0): "S=24000", (1, 1): "24600 (u)", (1, -1): "23400 (d)",
           (2, 2): "25200", (2, 0): "24000", (2, -2): "22800"}
    for (xx, yy), t in pts.items():
        ax.scatter([xx], [yy], s=420, color="#dbeafe", edgecolor=NAVY, zorder=3)
        ax.text(xx, yy, t, ha="center", va="center", fontsize=7.5, color=NAVY, zorder=4)
    ax.set_title("Two-step binomial tree (Nifty up/down)", color=NAVY, fontsize=11, weight="bold")
    ax.axis("off"); save(fig, "binomial_tree")

    print("figures written:", len([f for f in os.listdir(FIGS) if f.endswith(".png")]))


if __name__ == "__main__":
    main()
