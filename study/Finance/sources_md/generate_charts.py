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

# ---------------------------------------------------------------------------
# 6. Equity & Capital Markets ch.18 -- efficient frontier + CML
# ---------------------------------------------------------------------------
np.random.seed(11)
n_assets, n_port = 6, 4000
asset_ret = np.random.uniform(0.06, 0.16, n_assets)
asset_vol = np.random.uniform(0.12, 0.30, n_assets)
corr = np.full((n_assets, n_assets), 0.35)
np.fill_diagonal(corr, 1.0)
cov = np.outer(asset_vol, asset_vol) * corr
weights = np.random.dirichlet(np.ones(n_assets), n_port)
port_ret = weights @ asset_ret
port_vol = np.sqrt(np.einsum('ij,jk,ik->i', weights, cov, weights))
rf = 0.06
sharpe = (port_ret - rf) / port_vol
best = np.argmax(sharpe)
fig, ax = plt.subplots(figsize=(6.6, 4.8))
sc = ax.scatter(port_vol * 100, port_ret * 100, c=sharpe, cmap="viridis", s=6, alpha=0.55)
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label("Sharpe ratio", fontsize=9)
ax.scatter(asset_vol * 100, asset_ret * 100, color=GOLD, s=55, edgecolors=NAVY, zorder=5,
           label="Individual assets")
ax.scatter([port_vol[best] * 100], [port_ret[best] * 100], color="#b23b3b", s=90, marker="*",
           zorder=6, label="Max-Sharpe (tangency) portfolio")
xmax = port_vol.max() * 100 * 1.08
ymax = port_ret.max() * 100 * 1.12
cml_x = np.linspace(0, xmax, 20)
cml_y = rf * 100 + sharpe[best] * cml_x
ax.plot(cml_x, cml_y, color="#b23b3b", ls="--", lw=1.4, label="Capital Market Line")
ax.set_xlim(0, xmax)
ax.set_ylim(port_ret.min() * 100 * 0.9, ymax)
ax.set_xlabel("Portfolio volatility, annualised (%)")
ax.set_ylabel("Expected return, annualised (%)")
ax.set_title("Simulated efficient frontier: 4,000 random portfolios of 6 assets")
ax.legend(loc="lower right", fontsize=8, frameon=False)
ax.grid(alpha=0.25)
savefig("efficient_frontier.png")

# ---------------------------------------------------------------------------
# 7. TRA -- candlestick chart with 50/200-day MA and RSI (multi-timeframe trend example)
# ---------------------------------------------------------------------------
np.random.seed(21)
n = 260
drift = np.concatenate([np.full(150, 0.0009), np.full(60, -0.0012), np.full(50, 0.0015)])
noise = np.random.normal(0, 0.013, n)
close = 100 * np.cumprod(1 + drift + noise)
open_ = close * (1 + np.random.normal(0, 0.004, n))
high = np.maximum(open_, close) * (1 + np.abs(np.random.normal(0, 0.006, n)))
low = np.minimum(open_, close) * (1 - np.abs(np.random.normal(0, 0.006, n)))
def trailing_ma(arr, window):
    """Proper trailing (backward-looking) moving average, NaN-padded at the
    front where a full window isn't yet available -- avoids the edge
    artifacts np.convolve(..., mode='same') produces at both ends."""
    valid = np.convolve(arr, np.ones(window) / window, mode="valid")
    return np.concatenate([np.full(window - 1, np.nan), valid])

ema50 = trailing_ma(close, 50)
ema200 = trailing_ma(close, 200)
delta = np.diff(close, prepend=close[0])
gain = np.where(delta > 0, delta, 0.0)
loss = np.where(delta < 0, -delta, 0.0)
avg_gain = trailing_ma(gain, 14)
avg_loss = trailing_ma(loss, 14)
rs = avg_gain / np.where((avg_loss == 0) | np.isnan(avg_loss), 1e-9, avg_loss)
rsi = 100 - 100 / (1 + rs)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 5.6), sharex=True, gridspec_kw={"height_ratios": [3, 1]})
width = 0.6
up = close >= open_
ax1.vlines(np.arange(n), low, high, color=np.where(up, "#2e8b57", "#b23b3b"), lw=0.6)
ax1.bar(np.arange(n)[up], (close-open_)[up], bottom=open_[up], width=width, color="#2e8b57")
ax1.bar(np.arange(n)[~up], (close-open_)[~up], bottom=close[~up], width=width, color="#b23b3b")
ax1.plot(ema50, color=BLUE, lw=1.3, label="50-day MA")
ax1.plot(ema200, color=GOLD, lw=1.6, label="200-day MA")
ax1.axvline(150, color=GRAY, ls=":", lw=1)
ax1.annotate("Trend weakens", xy=(150, close[150]), xytext=(160, close[150]*1.15),
             fontsize=8, color=GRAY, arrowprops=dict(arrowstyle="->", color=GRAY, lw=0.8))
ax1.set_ylabel("Price (₹)")
ax1.set_title("Candlestick chart with 50/200-day MA and RSI(14)")
ax1.legend(loc="upper left", fontsize=8, frameon=False)
ax1.grid(alpha=0.2)
ax2.plot(rsi, color=NAVY, lw=1.2)
ax2.axhline(70, color="#b23b3b", ls="--", lw=0.9)
ax2.axhline(30, color="#2e8b57", ls="--", lw=0.9)
ax2.fill_between(np.arange(n), 70, 100, color="#b23b3b", alpha=0.08)
ax2.fill_between(np.arange(n), 0, 30, color="#2e8b57", alpha=0.08)
ax2.set_ylim(0, 100)
ax2.set_ylabel("RSI(14)")
ax2.set_xlabel("Trading day")
ax2.grid(alpha=0.2)
savefig("candlestick_ma_rsi.png")

# ---------------------------------------------------------------------------
# 8. Market Research -- awareness-to-purchase brand funnel
# ---------------------------------------------------------------------------
stages = ["Unaided\nawareness", "Aided\nawareness", "Consideration", "Trial", "Repeat\npurchase", "Loyal\n(NPS promoter)"]
values = [22, 61, 38, 24, 15, 9]
fig, ax = plt.subplots(figsize=(6.6, 4.4))
colors_funnel = plt.cm.Blues(np.linspace(0.9, 0.35, len(stages)))
bars = ax.bar(stages, values, color=colors_funnel, edgecolor=NAVY, linewidth=0.6)
for b, v in zip(bars, values):
    ax.text(b.get_x() + b.get_width()/2, v + 1.5, f"{v}%", ha="center", fontsize=9, color=NAVY, fontweight="bold")
ax.set_ylabel("% of target population")
ax.set_title("Brand funnel: unaided awareness through to loyal/promoter")
ax.set_ylim(0, 70)
ax.grid(axis="y", alpha=0.25)
plt.xticks(fontsize=8.5)
savefig("brand_funnel.png")

# ---------------------------------------------------------------------------
# 9. Market Research 6.7 -- regression driver analysis (standardised betas)
# ---------------------------------------------------------------------------
drivers = ["Trust in\nsecurity", "Ease of\nnavigation", "App\nspeed", "Support\nresponsiveness", "Feature\ncompleteness"]
betas = [0.34, 0.28, 0.19, 0.11, 0.04]
sig = [True, True, True, True, False]
fig, ax = plt.subplots(figsize=(6.4, 4.2))
colors_bar = ["#1f6098" if s else "#c9d2dc" for s in sig]
bars = ax.barh(drivers[::-1], betas[::-1], color=colors_bar[::-1], edgecolor=NAVY, linewidth=0.5)
for b, v, s in zip(bars, betas[::-1], sig[::-1]):
    label = f"{v:.2f}" + ("" if s else "  (not significant)")
    ax.text(v + 0.01, b.get_y() + b.get_height()/2, label, va="center", fontsize=9, color=NAVY)
ax.set_xlabel("Standardised beta (driver of NPS)")
ax.set_title("NPS driver analysis: which app attributes actually move NPS")
ax.set_xlim(0, 0.45)
ax.grid(axis="x", alpha=0.25)
savefig("nps_driver_analysis.png")

# ---------------------------------------------------------------------------
# 10. Market Research 6.8 -- conjoint attribute importance
# ---------------------------------------------------------------------------
attrs = ["Interest rate", "Approval speed", "Credit limit"]
importance = [45, 30, 20]
other = 100 - sum(importance)
if other > 0:
    attrs.append("Brand/other")
    importance.append(other)
fig, ax = plt.subplots(figsize=(6, 4.2))
colors_pie = ["#16365c", "#1f6098", "#5b8fc7", "#d8a93a"][:len(attrs)]
wedges, texts, autotexts = ax.pie(importance, labels=attrs, autopct="%1.0f%%", startangle=90,
                                    colors=colors_pie, textprops={"fontsize": 9.5, "color": NAVY},
                                    wedgeprops={"edgecolor": "white", "linewidth": 1.5})
for at in autotexts:
    at.set_color("white")
    at.set_fontweight("bold")
ax.set_title("Conjoint-derived attribute importance: UPI lending feature")
savefig("conjoint_attribute_importance.png")

# ---------------------------------------------------------------------------
# 11. TRA 5.4 -- option Greeks across strikes (Delta, Gamma, Theta)
# ---------------------------------------------------------------------------
from scipy.stats import norm
S0, r, sigma, T = 24500, 0.065, 0.13, 14/365
strikes = np.linspace(23500, 25500, 200)
d1 = (np.log(S0/strikes) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
d2 = d1 - sigma*np.sqrt(T)
call_delta = norm.cdf(d1)
gamma = norm.pdf(d1) / (S0*sigma*np.sqrt(T))
theta = (-(S0*norm.pdf(d1)*sigma)/(2*np.sqrt(T)) - r*strikes*np.exp(-r*T)*norm.cdf(d2)) / 365

fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.4))
for ax, (data, label, color) in zip(axes, [
        (call_delta, "Delta", BLUE), (gamma, "Gamma", GOLD), (theta, "Theta (₹/day)", "#b23b3b")]):
    ax.plot(strikes, data, color=color, lw=2)
    ax.axvline(S0, color=GRAY, ls=":", lw=1)
    ax.set_title(label, fontsize=10, color=NAVY, fontweight="bold")
    ax.set_xlabel("Strike price", fontsize=8.5)
    ax.grid(alpha=0.25)
    ax.tick_params(labelsize=8)
axes[0].annotate("ATM\n(spot)", xy=(S0, 0.5), fontsize=7.5, color=GRAY, ha="center")
fig.suptitle("Call option Greeks across strikes (Nifty-style example, 14 DTE)", fontsize=11.5,
             color=NAVY, fontweight="bold", y=1.03)
savefig("greeks_across_strikes.png")

# ---------------------------------------------------------------------------
# 12. Market Research 20.4 -- MMM saturation curves (TV vs Digital diminishing returns)
# ---------------------------------------------------------------------------
spend = np.linspace(0, 60, 200)
def saturation(x, scale, k):
    return scale * (1 - np.exp(-x / k))
tv_response = saturation(spend, 18, 12)
digital_response = saturation(spend, 22, 30)
fig, ax = plt.subplots(figsize=(6.6, 4.4))
ax.plot(spend, tv_response, color=BLUE, lw=2.2, label="TV response curve")
ax.plot(spend, digital_response, color=GOLD, lw=2.2, label="Digital response curve")
ax.scatter([40], [saturation(40, 18, 12)], color=BLUE, s=70, zorder=5, edgecolors=NAVY)
ax.scatter([15], [saturation(15, 22, 30)], color=GOLD, s=70, zorder=5, edgecolors=NAVY)
ax.annotate("TV: ₹40cr spend\n(deep in saturation\n-- low marginal ROI)", xy=(40, saturation(40,18,12)),
            xytext=(42, saturation(40,18,12)-6), fontsize=8, color=GRAY)
ax.annotate("Digital: ₹15cr spend\n(still steep --\nhigh marginal ROI)", xy=(15, saturation(15,22,30)),
            xytext=(17, saturation(15,22,30)-5), fontsize=8, color=GRAY)
ax.set_xlabel("Annual channel spend (₹ cr)")
ax.set_ylabel("Sales contribution (indexed)")
ax.set_title("MMM saturation curves: why marginal ROI differs from average ROI")
ax.legend(loc="lower right", fontsize=8.5, frameon=False)
ax.grid(alpha=0.25)
savefig("mmm_saturation_curves.png")

# ---------------------------------------------------------------------------
# 13. Market Research 21.4 -- CLV sensitivity to churn rate
# ---------------------------------------------------------------------------
churn = np.linspace(0.05, 0.40, 100)
arpu, margin = 2400, 0.65
clv = (arpu * margin) / churn
fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.plot(churn * 100, clv, color=NAVY, lw=2.4)
for cr, label_color in [(0.20, "#b23b3b"), (0.15, "#2e8b57")]:
    val = (arpu * margin) / cr
    ax.scatter([cr*100], [val], color=label_color, s=70, zorder=5, edgecolors=NAVY)
    ax.annotate(f"{int(cr*100)}% churn\nCLV = Rs.{val:,.0f}", xy=(cr*100, val),
                xytext=(cr*100+2, val+400), fontsize=8.5, color=label_color, fontweight="bold")
ax.set_xlabel("Annual churn rate (%)")
ax.set_ylabel("Customer Lifetime Value (₹)")
ax.set_title("CLV is highly non-linear in churn rate: small churn cuts, large CLV gains")
ax.grid(alpha=0.25)
savefig("clv_vs_churn.png")

print("\nAll charts generated in", OUT)
