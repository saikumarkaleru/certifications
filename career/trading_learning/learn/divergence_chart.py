"""Make a clear RSI-divergence teaching chart: mark the two price highs and the two RSI highs,
show that price makes a Higher High while RSI makes a Lower High = bearish divergence."""
import os
import numpy as np
import matplotlib.pyplot as plt

IMG = os.path.join(os.path.dirname(__file__), "img")
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.25})
GREEN, RED, BLUE, PURP = "#1a9850", "#d73027", "#1f4e79", "#6a3d9a"

x = np.arange(80)
# price: two peaks, the SECOND one HIGHER (higher high)
price = (115 + 6 * np.sin(x / 7)
         + np.where(x < 40, x * 0.0, 0)
         )
price[16:24] += 4      # first peak
price[52:60] += 10     # second, clearly HIGHER peak
p1 = 10 + int(np.argmax(price[10:30]))    # snap markers to the actual peaks
p2 = 45 + int(np.argmax(price[45:65]))

# RSI: two peaks, the SECOND one clearly LOWER (lower high)
rsi = 52 + 18 * np.sin(x / 7)
rsi[16:24] += 14       # first RSI peak (high)
rsi[52:60] -= 4        # second RSI peak pushed lower
r1 = 10 + int(np.argmax(rsi[10:30]))
r2 = 45 + int(np.argmax(rsi[45:65]))

fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True,
                             gridspec_kw={"height_ratios": [1.3, 1]})

# ---- price panel ----
a1.plot(x, price, color=BLUE, lw=1.7)
a1.plot([p1, p2], [price[p1], price[p2]], color=RED, ls="--", lw=2)
for xi, lab in [(p1, "High 1"), (p2, "High 2\n(HIGHER high)")]:
    a1.plot(xi, price[xi], "o", color=RED, ms=9)
    a1.annotate(lab, xy=(xi, price[xi]), xytext=(xi - 4, price[xi] + 3),
                fontsize=9.5, fontweight="bold", color=RED)
a1.set_title("RSI DIVERGENCE — price makes a HIGHER high, RSI makes a LOWER high",
             fontweight="bold")
a1.set_ylabel("Price")

# ---- RSI panel ----
a2.plot(x, rsi, color=PURP, lw=1.7)
a2.axhline(70, color=RED, ls="--", lw=1); a2.axhline(30, color=GREEN, ls="--", lw=1)
a2.axhspan(70, 100, color=RED, alpha=0.07); a2.axhspan(0, 30, color=GREEN, alpha=0.07)
a2.plot([r1, r2], [rsi[r1], rsi[r2]], color=RED, ls="--", lw=2)
for xi, lab in [(r1, "High 1"), (r2, "High 2\n(LOWER high)")]:
    a2.plot(xi, rsi[xi], "o", color=RED, ms=9)
    a2.annotate(lab, xy=(xi, rsi[xi]), xytext=(xi - 4, rsi[xi] - 12),
                fontsize=9.5, fontweight="bold", color=RED)
a2.set_ylim(0, 100); a2.set_ylabel("RSI")
a2.text(1, 86, "OVERBOUGHT", color=RED, fontsize=8.5)
a2.text(1, 16, "OVERSOLD", color=GREEN, fontsize=8.5)
a2.text(40, 6, "Price UP but RSI DOWN  =  BEARISH DIVERGENCE  =  momentum fading, expect a fall",
        fontsize=9.5, fontweight="bold", color=RED, ha="center",
        bbox=dict(boxstyle="round", fc="#fdecea", ec=RED))

fig.tight_layout()
fig.savefig(os.path.join(IMG, "06b_rsi_divergence.png"), dpi=130, bbox_inches="tight")
print("-> 06b_rsi_divergence.png")
