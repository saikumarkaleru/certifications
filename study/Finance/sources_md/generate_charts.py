"""
Generate real chart images (matplotlib) for worked examples in the Market
Research and Technical Research handbooks -- referenced via markdown image
syntax from MARKET_RESEARCH_COMPLETE_HANDBOOK.md / TRA_COMPLETE_HANDBOOK.md.

Run once after adding/changing a worked example that needs a new chart:
  python generate_charts.py
Then rebuild the relevant handbook PDF.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "charts")
os.makedirs(OUT, exist_ok=True)

NAVY = "#14365c"
BLUE = "#1f6098"
GOLD = "#d8a93a"
GRAY = "#6b7787"
COLORS = ["#1f6098", "#d8a93a", "#2e8b57", "#b23b3b"]

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 10,
    "axes.edgecolor": "#c9d2dc",
    "axes.labelcolor": NAVY,
    "text.color": "#1b2330",
    "xtick.color": "#33445a",
    "ytick.color": "#33445a",
    "axes.titlecolor": NAVY,
    "axes.titleweight": "bold",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})


def savefig(name):
    path = os.path.join(OUT, name)
    plt.tight_layout()
    plt.savefig(path, dpi=170, bbox_inches="tight")
    plt.close()
    print("wrote", path)


# ---------------------------------------------------------------------------
# 1. Market Research 6.10 -- segmentation scatter plot
# ---------------------------------------------------------------------------
np.random.seed(7)
segments = {
    "A: Convenience seekers (28%)": dict(n=224, ps=(2.1, 0.5), dc=(4.6, 0.4)),
    "B: Value-driven strivers (34%)": dict(n=272, ps=(4.4, 0.4), dc=(3.2, 0.6)),
    "C: Cautious traditionalists (22%)": dict(n=176, ps=(3.6, 0.5), dc=(1.8, 0.5)),
    "D: Affluent optimisers (16%)": dict(n=128, ps=(1.5, 0.4), dc=(4.8, 0.3)),
}
fig, ax = plt.subplots(figsize=(6.4, 4.6))
for (label, spec), color in zip(segments.items(), COLORS):
    ps = np.clip(np.random.normal(spec["ps"][0], spec["ps"][1], spec["n"]), 1, 5)
    dc = np.clip(np.random.normal(spec["dc"][0], spec["dc"][1], spec["n"]), 1, 5)
    ax.scatter(ps, dc, s=14, alpha=0.55, color=color, label=label, edgecolors="none")
ax.set_xlabel("Price sensitivity (1 = low, 5 = high)")
ax.set_ylabel("Digital comfort (1 = low, 5 = high)")
ax.set_title("K-means segmentation (k=4): price sensitivity vs digital comfort")
ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.5, 5.5)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=1, fontsize=8, frameon=False)
ax.grid(alpha=0.25)
savefig("segmentation_scatter.png")

# ---------------------------------------------------------------------------
# 2. Market Research 16.2 -- price elasticity of demand curve
# ---------------------------------------------------------------------------
price = np.linspace(80, 130, 100)
base_price, base_qty, elasticity = 100, 1000, -0.4
qty = base_qty * (price / base_price) ** elasticity
revenue = price * qty
fig, ax1 = plt.subplots(figsize=(6.4, 4.2))
ax1.plot(price, qty, color=BLUE, lw=2.2, label="Quantity demanded")
ax1.set_xlabel("Price (₹)")
ax1.set_ylabel("Quantity demanded", color=BLUE)
ax1.tick_params(axis="y", labelcolor=BLUE)
ax1.axvline(110, color=GRAY, ls="--", lw=1)
ax1.annotate("+10% price\n(worked example)", xy=(110, qty[np.argmin(np.abs(price-110))]),
             xytext=(112, 850), fontsize=8, color=GRAY)
ax2 = ax1.twinx()
ax2.plot(price, revenue, color=GOLD, lw=2.2, label="Total revenue")
ax2.set_ylabel("Total revenue (₹)", color="#a3781f")
ax2.tick_params(axis="y", labelcolor="#a3781f")
ax1.set_title("Inelastic demand (PED = -0.4): a price rise still grows revenue")
ax1.grid(alpha=0.25)
savefig("price_elasticity_curve.png")

# ---------------------------------------------------------------------------
# 3. Market Research 7.1 -- TAM/SAM/SOM funnel
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 4.6))
levels = [("TAM", 1.0, "#0d2440"), ("SAM", 0.62, "#16365c"), ("SOM", 0.30, "#1f6098")]
labels_extra = ["Total addressable market", "Serviceable addressable market", "Serviceable obtainable market"]
y = 0
for (name, width, color), extra in zip(levels, labels_extra):
    left = (1 - width) / 2
    ax.barh(y, width, left=left, height=0.6, color=color)
    ax.text(0.5, y, f"{name}\n{extra}", ha="center", va="center", color="white",
            fontsize=9, fontweight="bold")
    y -= 1
ax.set_xlim(0, 1)
ax.set_ylim(-2.6, 0.6)
ax.axis("off")
ax.set_title("TAM → SAM → SOM: narrowing to the realistically obtainable market")
savefig("tam_sam_som_funnel.png")

# ---------------------------------------------------------------------------
# 4. TRA 5.9 -- long straddle payoff diagram
# ---------------------------------------------------------------------------
spot = np.linspace(400, 600, 400)
strike, premium = 500, 34
call_payoff = np.maximum(spot - strike, 0) - 18
put_payoff = np.maximum(strike - spot, 0) - 16
straddle_pnl = call_payoff + put_payoff
fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.plot(spot, straddle_pnl, color=NAVY, lw=2.4, label="Long straddle P&L")
ax.axhline(0, color="#9aa5b1", lw=1)
ax.axvline(strike - premium, color=GOLD, ls="--", lw=1)
ax.axvline(strike + premium, color=GOLD, ls="--", lw=1)
ax.fill_between(spot, straddle_pnl, 0, where=(straddle_pnl >= 0), color="#2e8b57", alpha=0.15)
ax.fill_between(spot, straddle_pnl, 0, where=(straddle_pnl < 0), color="#b23b3b", alpha=0.12)
ax.annotate(f"Breakeven ₹{strike-premium}", xy=(strike-premium, 0), xytext=(strike-premium-55, 40),
            fontsize=8, color=GRAY, arrowprops=dict(arrowstyle="->", color=GRAY, lw=0.8))
ax.annotate(f"Breakeven ₹{strike+premium}", xy=(strike+premium, 0), xytext=(strike+premium+5, 40),
            fontsize=8, color=GRAY, arrowprops=dict(arrowstyle="->", color=GRAY, lw=0.8))
ax.set_xlabel("Stock price at expiry (₹)")
ax.set_ylabel("P&L per share (₹)")
ax.set_title("Long straddle payoff (500 CE + 500 PE, combined premium ₹34)")
ax.grid(alpha=0.25)
savefig("long_straddle_payoff.png")

# ---------------------------------------------------------------------------
# 5. TRA 10.5 -- backtest equity curve with drawdown
# ---------------------------------------------------------------------------
np.random.seed(3)
n_days = 750
daily_ret = np.random.normal(0.0008, 0.011, n_days)
equity = 5_00_000 * np.cumprod(1 + daily_ret)
running_max = np.maximum.accumulate(equity)
drawdown = (equity - running_max) / running_max * 100
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.6, 5.4), sharex=True,
                                 gridspec_kw={"height_ratios": [2.2, 1]})
ax1.plot(equity / 1e5, color=BLUE, lw=1.8)
ax1.set_ylabel("Equity (₹ lakh)")
ax1.set_title("Backtested strategy: equity curve and drawdown (3-year, illustrative)")
ax1.grid(alpha=0.25)
ax2.fill_between(np.arange(n_days), drawdown, 0, color="#b23b3b", alpha=0.35)
ax2.plot(drawdown, color="#8a2b2b", lw=1)
ax2.set_ylabel("Drawdown (%)")
ax2.set_xlabel("Trading day")
ax2.grid(alpha=0.25)
savefig("backtest_equity_drawdown.png")

print("\nAll charts generated in", OUT)
