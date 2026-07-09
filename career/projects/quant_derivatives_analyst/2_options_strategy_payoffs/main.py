"""
main.py -- Options Strategy Payoffs & Risk Toolkit (orchestrator).

Run:
    python main.py

What it does (each step prints a clear console summary):
    1. Load a market snapshot (live yfinance -> cache -> synthetic fallback).
    2. Build ~16 classic option strategies from the Leg/Position abstraction and
       print legs, net debit/credit, max profit/loss, breakevens, net Greeks, POP.
    3. Show one strategy's P&L at expiry AND before expiry (time value demo).
    4. Print a spot x vol scenario grid for a representative strategy.
    5. Run the cross-strategy screener (ranked by risk/reward x POP).
    6. Write output/strategy_summary.xlsx (Summary, Screener, Scenario sheets).
    7. Save payoff charts to output/ (grid of payoffs, expiry-vs-before overlay,
       scenario heatmap).

Everything is per-share (1 contract = 1 share) to keep the maths transparent.
"""

from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Agg")  # headless backend -- we only save PNGs, never show a window
import matplotlib.pyplot as plt

# Make `src` importable no matter where python is invoked from.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from src.strategies import library, analytics  # noqa: E402
from src.strategies import market_data as md    # noqa: E402

OUTPUT_DIR = os.path.join(_HERE, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Global market parameters used for the before-expiry / Greeks / POP maths.
TICKER = os.environ.get("OPT_TICKER", "AAPL")
RISK_FREE = 0.045   # ~4.5% annualised risk-free rate


def hr(char="=", n=78):
    print(char * n)


# ---------------------------------------------------------------------------
# Step 1: market snapshot
# ---------------------------------------------------------------------------
def load_market():
    hr()
    print("STEP 1  |  MARKET SNAPSHOT")
    hr()
    # allow_live can be disabled via env for guaranteed-offline demos.
    allow_live = os.environ.get("OPT_OFFLINE", "0") != "1"
    snap = md.get_snapshot(TICKER, r=RISK_FREE, allow_live=allow_live)
    print(f"Underlying : {snap.ticker}")
    print(f"Data source: {snap.source.upper()}  "
          f"({'real chain' if snap.source!='synthetic' else 'BSM-priced ladder'})")
    print(f"Spot       : {snap.spot:.2f}")
    print(f"Impl. vol  : {snap.sigma*100:.1f}%   (annualised)")
    print(f"Risk-free  : {snap.r*100:.2f}%   Div yield: {snap.q*100:.2f}%")
    print(f"Expiry     : {snap.expiry}   (T = {snap.T*365:.0f} days = {snap.T:.3f}y)")
    print(f"Strikes    : {len(snap.strikes)} available "
          f"({min(snap.strikes):.1f} ... {max(snap.strikes):.1f})")
    return snap


# ---------------------------------------------------------------------------
# Step 2: build + summarise all strategies
# ---------------------------------------------------------------------------
def summarise_strategies(specs, snap):
    hr()
    print(f"STEP 2  |  {len(specs)} STRATEGIES  (per-share P&L)")
    hr()
    rows = []
    for spec in specs:
        pos = spec.position
        stats = pos.max_profit_loss(snap.spot)
        bes = pos.breakevens(snap.spot)
        g = pos.net_greeks(snap.spot, snap.T, snap.r, snap.sigma, snap.q)
        pop = analytics.probability_of_profit(spec, snap.spot, snap.T,
                                              snap.r, snap.sigma, snap.q)
        ncd = pos.net_debit_credit()

        mp = "unbounded" if stats["profit_unbounded"] else f"{stats['max_profit']:.2f}"
        ml = "unbounded" if stats["loss_unbounded"] else f"{stats['max_loss']:.2f}"
        be_str = ", ".join(f"{b:.2f}" for b in bes) if bes else "none"
        cd_word = "credit" if ncd > 0 else "debit"

        print(f"\n{spec.name}  [{spec.category}]")
        print(f"  view   : {spec.view}")
        print(f"  legs   : {pos.describe_legs()}")
        print(f"  net    : {abs(ncd):.2f} {cd_word}")
        print(f"  maxP/L : max profit {mp} | max loss {ml}")
        print(f"  b/e    : {be_str}")
        print(f"  greeks : delta {g.delta:+.3f}  gamma {g.gamma:+.4f}  "
              f"vega {g.vega:+.3f}/volpt  theta {g.theta:+.3f}/day")
        print(f"  POP    : {pop*100:.1f}%   (P&L>0 at expiry, risk-neutral lognormal)")

        rows.append({
            "Strategy": spec.name, "Category": spec.category,
            "Legs": pos.describe_legs(),
            "Net (>0 credit)": round(ncd, 2),
            "Max Profit": stats["max_profit"],
            "Max Loss": stats["max_loss"],
            "Profit Unbounded": stats["profit_unbounded"],
            "Loss Unbounded": stats["loss_unbounded"],
            "Breakevens": be_str,
            "Delta": round(g.delta, 4), "Gamma": round(g.gamma, 5),
            "Vega/volpt": round(g.vega, 4), "Theta/day": round(g.theta, 4),
            "POP %": round(pop * 100, 1),
        })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Step 3: expiry vs before-expiry P&L (time value demo)
# ---------------------------------------------------------------------------
def time_value_demo(specs, snap):
    hr()
    print("STEP 3  |  EXPIRY vs BEFORE-EXPIRY P&L  (time value)")
    hr()
    spec = next(s for s in specs if s.name == "Long Straddle")
    pos = spec.position
    T_half = snap.T / 2.0
    print(f"Strategy: {spec.name}   (showing P&L now-ish at T={T_half*365:.0f}d "
          f"vs at expiry)")
    sample = np.array([snap.spot * m for m in (0.85, 0.95, 1.0, 1.05, 1.15)])
    exp_pnl = pos.payoff_at_expiry(sample)
    now_pnl = pos.pnl_before_expiry(sample, T_half, snap.r, snap.sigma, snap.q)
    print(f"  {'Spot':>8} | {'Expiry P&L':>12} | {'Before-exp P&L':>14}")
    for s, e, n in zip(sample, exp_pnl, now_pnl):
        print(f"  {s:8.2f} | {e:12.2f} | {n:14.2f}")
    print("  -> Before expiry the curve is SMOOTH (still has time value); at "
          "expiry it is KINKED. The gap is the option's remaining time value.")
    return spec


# ---------------------------------------------------------------------------
# Step 4: scenario grid
# ---------------------------------------------------------------------------
def scenario_demo(specs, snap):
    hr()
    print("STEP 4  |  SCENARIO GRID  (before-expiry P&L: spot x vol)")
    hr()
    spec = next(s for s in specs if s.name == "Iron Condor")
    spots, vols, matrix = analytics.scenario_grid(
        spec, snap.spot, snap.T / 2.0, snap.r, snap.sigma, snap.q)
    print(f"Strategy: {spec.name}   (rows = vol, cols = spot move)")
    header = "  vol\\spot " + " ".join(f"{s:8.1f}" for s in spots)
    print(header)
    for i, v in enumerate(vols):
        line = " ".join(f"{matrix[i, j]:8.2f}" for j in range(len(spots)))
        print(f"  {v*100:6.1f}% | {line}")
    print("  -> Read across for spot risk, down for vega risk. A short-vol "
          "condor is hurt by rising vol (lower rows) and big spot moves (edges).")

    # Return a DataFrame for the Excel sheet.
    df = pd.DataFrame(matrix,
                      index=[f"{v*100:.1f}% vol" for v in vols],
                      columns=[f"{s:.1f}" for s in spots])
    return spec, spots, vols, matrix, df


# ---------------------------------------------------------------------------
# Step 5: screener
# ---------------------------------------------------------------------------
def run_screener(specs, snap):
    hr()
    print("STEP 5  |  SCREENER  (ranked by risk/reward x POP)")
    hr()
    rows = analytics.screen_strategies(specs, snap.spot, snap.T,
                                      snap.r, snap.sigma, snap.q)
    print(f"  {'#':>2} {'Strategy':<28} {'R/R':>7} {'POP%':>6} "
          f"{'MaxP':>9} {'MaxL':>9}  Note")
    screen_records = []
    for i, r in enumerate(rows, 1):
        rr = "n/a" if np.isnan(r.risk_reward) else f"{r.risk_reward:.2f}"
        mp = "unbnd" if r.note and "unbounded profit" in r.note else f"{r.max_profit:.2f}"
        ml = "unbnd" if r.note and "unbounded loss" in r.note else f"{r.max_loss:.2f}"
        print(f"  {i:>2} {r.name:<28} {rr:>7} {r.pop*100:>5.1f} "
              f"{mp:>9} {ml:>9}  {r.note}")
        screen_records.append({
            "Rank": i, "Strategy": r.name, "Category": r.category,
            "Risk/Reward": None if np.isnan(r.risk_reward) else round(r.risk_reward, 3),
            "POP %": round(r.pop * 100, 1),
            "Max Profit": round(r.max_profit, 2), "Max Loss": round(r.max_loss, 2),
            "Net (>0 credit)": round(r.net_cd, 2), "Note": r.note,
        })
    print("  -> Ranking rewards strategies with BOTH a good payoff ratio and a "
          "good probability of profit; unbounded-loss trades are penalised.")
    return pd.DataFrame(screen_records)


# ---------------------------------------------------------------------------
# Step 6: Excel workbook
# ---------------------------------------------------------------------------
def write_excel(summary_df, screen_df, scenario_df):
    hr()
    print("STEP 6  |  WRITE EXCEL")
    hr()
    path = os.path.join(OUTPUT_DIR, "strategy_summary.xlsx")
    with pd.ExcelWriter(path, engine="openpyxl") as xl:
        summary_df.to_excel(xl, sheet_name="Summary", index=False)
        screen_df.to_excel(xl, sheet_name="Screener", index=False)
        scenario_df.to_excel(xl, sheet_name="Scenario (IronCondor)")
    print(f"  wrote {path}")
    print("  sheets: Summary (all strategies + greeks + POP), Screener (ranked), "
          "Scenario (spot x vol grid)")
    return path


# ---------------------------------------------------------------------------
# Step 7: charts
# ---------------------------------------------------------------------------
def _plot_one(ax, spec, snap):
    """Draw one strategy's expiry payoff on ax with breakevens and zero line."""
    pos = spec.position
    S = np.linspace(snap.spot * 0.6, snap.spot * 1.4, 300)
    y = pos.payoff_at_expiry(S)
    ax.plot(S, y, lw=1.6)
    ax.axhline(0, color="black", lw=0.6)
    ax.axvline(snap.spot, color="grey", ls=":", lw=0.8)
    ax.fill_between(S, y, 0, where=(y >= 0), color="green", alpha=0.15)
    ax.fill_between(S, y, 0, where=(y < 0), color="red", alpha=0.15)
    ax.set_title(spec.name, fontsize=8)
    ax.tick_params(labelsize=6)


def draw_payoff_grid(specs, snap):
    n = len(specs)
    cols = 4
    rows = (n + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(15, 3 * rows))
    axes = np.array(axes).reshape(-1)
    for ax, spec in zip(axes, specs):
        _plot_one(ax, spec, snap)
    for ax in axes[n:]:
        ax.axis("off")
    fig.suptitle(f"Expiry payoff diagrams -- {snap.ticker} spot {snap.spot:.2f}",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.98])
    path = os.path.join(OUTPUT_DIR, "strategy_payoffs.png")
    fig.savefig(path, dpi=110)
    plt.close(fig)
    return path


def draw_time_value(spec, snap):
    pos = spec.position
    S = np.linspace(snap.spot * 0.7, snap.spot * 1.3, 300)
    exp = pos.payoff_at_expiry(S)
    now = pos.pnl_before_expiry(S, snap.T / 2.0, snap.r, snap.sigma, snap.q)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(S, exp, label="At expiry (kinked)", lw=1.8)
    ax.plot(S, now, label=f"Before expiry T={snap.T/2*365:.0f}d (smooth)", lw=1.8, ls="--")
    ax.axhline(0, color="black", lw=0.6)
    ax.axvline(snap.spot, color="grey", ls=":", lw=0.8, label="spot")
    ax.set_title(f"{spec.name}: expiry vs before-expiry P&L (time value)")
    ax.set_xlabel("Underlying price at valuation")
    ax.set_ylabel("P&L per share")
    ax.legend(fontsize=8)
    fig.tight_layout()
    path = os.path.join(OUTPUT_DIR, "time_value_overlay.png")
    fig.savefig(path, dpi=120)
    plt.close(fig)
    return path


def draw_scenario_heatmap(spec, spots, vols, matrix):
    fig, ax = plt.subplots(figsize=(9, 4))
    im = ax.imshow(matrix, aspect="auto", cmap="RdYlGn", origin="lower")
    ax.set_xticks(range(len(spots)))
    ax.set_xticklabels([f"{s:.0f}" for s in spots], fontsize=8)
    ax.set_yticks(range(len(vols)))
    ax.set_yticklabels([f"{v*100:.0f}%" for v in vols], fontsize=8)
    ax.set_xlabel("Spot")
    ax.set_ylabel("Implied vol")
    ax.set_title(f"{spec.name}: before-expiry P&L (spot x vol)")
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, f"{matrix[i, j]:.1f}", ha="center", va="center",
                    fontsize=6, color="black")
    fig.colorbar(im, ax=ax, label="P&L per share")
    fig.tight_layout()
    path = os.path.join(OUTPUT_DIR, "scenario_heatmap.png")
    fig.savefig(path, dpi=120)
    plt.close(fig)
    return path


def draw_charts(specs, snap, tv_spec, scen):
    hr()
    print("STEP 7  |  SAVE CHARTS")
    hr()
    scen_spec, spots, vols, matrix, _ = scen
    p1 = draw_payoff_grid(specs, snap)
    p2 = draw_time_value(tv_spec, snap)
    p3 = draw_scenario_heatmap(scen_spec, spots, vols, matrix)
    for p in (p1, p2, p3):
        print(f"  wrote {p}")
    return [p1, p2, p3]


# ---------------------------------------------------------------------------
def main():
    snap = load_market()
    specs = library.build_all(snap)
    summary_df = summarise_strategies(specs, snap)
    tv_spec = time_value_demo(specs, snap)
    scen = scenario_demo(specs, snap)
    screen_df = run_screener(specs, snap)
    write_excel(summary_df, screen_df, scen[4])
    draw_charts(specs, snap, tv_spec, scen)

    hr()
    print("DONE. All steps completed successfully.")
    hr()


if __name__ == "__main__":
    main()
