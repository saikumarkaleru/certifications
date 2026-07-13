"""
Strategy engine for the Options Strategy Encyclopedia.

Self-contained BSM pricer + a payoff evaluator that supports PER-LEG expiry (so
calendars/diagonals get the correct tent shape at front-month expiry). For every
strategy it:
  - prices each option leg at open (realistic, self-consistent premiums under a mild skew),
  - plots a payoff diagram (P&L at the evaluation horizon) -> figs/strategies/<slug>.png,
  - NUMERICALLY computes net debit/credit, max profit, max loss, breakevens and risk:reward
    from the payoff grid (no hand-typed numbers).
Outputs figs + strategies_metrics.json (consumed by the prose-writing agents).

Run:  python strat_engine.py
"""
import os, json, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import log, sqrt, exp, erf, pi

ROOT = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(ROOT, "figs", "strategies")
os.makedirs(FIGDIR, exist_ok=True)

NAVY, GREEN, RED, GREY = "#16365c", "#16a34a", "#dc2626", "#94a3b8"
plt.rcParams.update({"font.size": 9, "axes.edgecolor": "#cbd5e1", "figure.dpi": 120})

S0 = 24000.0     # Nifty ATM reference
R = 0.07         # risk-free
LOT = 75         # Nifty lot (for rupee scale, illustrative)


# ---------- Black-Scholes-Merton ----------
def Nf(x): return 0.5 * (1 + erf(x / sqrt(2)))
def _d1(S, K, T, r, sig): return (log(S / K) + (r + 0.5 * sig * sig) * T) / (sig * sqrt(T))

def bs(S, K, T, r, sig, call=True):
    if T <= 1e-9:
        return max(0.0, (S - K) if call else (K - S))
    if K <= 0:
        K = 1.0
    D1 = _d1(S, K, T, r, sig); D2 = D1 - sig * sqrt(T)
    return (S * Nf(D1) - K * exp(-r * T) * Nf(D2)) if call \
        else (K * exp(-r * T) * Nf(-D2) - S * Nf(-D1))


def leg_iv(strike):
    """Mild equity-index skew around ATM: OTM puts richer, OTM calls cheaper."""
    m = (strike - S0) / S0
    iv = 0.14 - 0.55 * m          # downside skew
    return float(min(0.40, max(0.085, iv)))


# ---------- per-leg pricing & payoff ----------
def price_leg(kind, strike, qty, dte):
    """Premium (per unit) paid/received at open. Stock leg returns its entry price."""
    if kind == "s":
        return S0
    T = max(dte, 1) / 365.0
    return bs(S0, strike, T, R, leg_iv(strike), call=(kind == "c"))


def leg_value_at(S, kind, strike, dte_open, horizon_dte):
    """Value of one leg (per unit) when spot=S at the evaluation horizon."""
    if kind == "s":
        return S                     # position VALUE; entry cost handled via net_cost
    rem = (dte_open - horizon_dte)    # days still to run after the horizon
    if rem <= 0.5:
        return np.maximum(S - strike, 0) if kind == "c" else np.maximum(strike - S, 0)
    T = rem / 365.0
    # vectorised BSM value of a still-alive leg at the horizon
    return np.array([bs(float(s), strike, T, R, leg_iv(strike), call=(kind == "c")) for s in S])


def build_legs(spec):
    """spec legs: (kind, offset_points, qty, dte). Returns concrete legs w/ strike, premium, dte."""
    out = []
    for kind, off, qty, dte in spec["legs"]:
        strike = S0 if kind == "s" else (S0 + off)
        prem = price_leg(kind, strike, qty, dte)
        out.append({"kind": kind, "strike": strike, "qty": qty, "dte": dte, "prem": prem})
    return out


def _pnl_on(S, legs, horizon, net_cost):
    pnl = np.zeros_like(S)
    for l in legs:
        pnl = pnl + l["qty"] * leg_value_at(S, l["kind"], l["strike"], l["dte"], horizon)
    return pnl - net_cost


def evaluate(spec):
    legs = build_legs(spec)
    horizon = min(l["dte"] for l in legs if l["kind"] != "s")  # front-month expiry
    net_cost = sum(l["qty"] * l["prem"] for l in legs)          # +debit / -credit (per unit)

    # Asymptotic slope as spot -> +infinity (only the upside can be truly unbounded;
    # the downside is always bounded because the index cannot fall below 0).
    slope_up = sum(l["qty"] for l in legs if l["kind"] in ("c", "s"))
    unlimited_up_profit = slope_up > 0.5
    unlimited_up_loss = slope_up < -0.5

    # ---- metrics on a WIDE grid (down to ~0, up to 3x) so bounded extrema are real ----
    W = np.linspace(1.0, S0 * 3.0, 3000)
    wp = _pnl_on(W, legs, horizon, net_cost)
    maxp = float(np.max(wp)); maxl = float(np.min(wp))
    bes = []
    sgn = np.sign(wp)
    for i in range(1, len(W)):
        if sgn[i - 1] != 0 and sgn[i] != 0 and sgn[i - 1] != sgn[i]:
            x0, x1, y0, y1 = W[i - 1], W[i], wp[i - 1], wp[i]
            bes.append(float(x0 - y0 * (x1 - x0) / (y1 - y0)))
    # keep only breakevens in a sane display band (avoids spurious deep-tail crossings,
    # e.g. the discounting kink of a deep LEAPS diagonal far above spot)
    bes = [b for b in bes if S0 * 0.75 < b < S0 * 1.25]

    # ---- scenario table: exact P&L at standard spot levels (at the horizon) ----
    scen_spots = [22800, 23400, 24000, 24600, 25200]   # -5%, -2.5%, flat, +2.5%, +5%
    sp = _pnl_on(np.array(scen_spots, dtype=float), legs, horizon, net_cost)
    scenarios = [{"spot": int(s), "pnl_pts": round(float(p), 0)} for s, p in zip(scen_spots, sp)]

    # ---- narrow grid for the actual plot ----
    span = spec.get("span", 0.14)
    S = np.linspace(S0 * (1 - span), S0 * (1 + span), 1200)
    pnl = _pnl_on(S, legs, horizon, net_cost)

    return {
        "legs": legs, "S": S, "pnl": pnl, "horizon": horizon, "net_cost": net_cost,
        "max_profit": maxp, "max_loss": maxl, "breakevens": bes, "scenarios": scenarios,
        "unlimited_up": bool(unlimited_up_profit), "unlimited_dn": bool(unlimited_up_loss),
    }


def fmt_legs(legs):
    parts = []
    for l in legs:
        if l["kind"] == "s":
            parts.append(f"{'Long' if l['qty']>0 else 'Short'} {abs(l['qty'])}x underlying @ {l['strike']:.0f}")
            continue
        side = "Buy" if l["qty"] > 0 else "Sell"
        opt = "CE" if l["kind"] == "c" else "PE"
        q = abs(l["qty"])
        qx = f"{q}x " if q != 1 else ""
        parts.append(f"{side} {qx}{l['strike']:.0f} {opt} @ {l['prem']:.0f}")
    return " | ".join(parts)


def plot(spec, ev):
    S, pnl, legs = ev["S"], ev["pnl"], ev["legs"]
    fig, ax = plt.subplots(figsize=(7.0, 3.0))
    ax.plot(S, pnl, color=NAVY, lw=2)
    ax.fill_between(S, pnl, 0, where=pnl >= 0, color=GREEN, alpha=0.16)
    ax.fill_between(S, pnl, 0, where=pnl < 0, color=RED, alpha=0.16)
    for l in legs:
        if l["kind"] != "s":
            ax.axvline(l["strike"], color=GREY, ls=":", lw=0.6)
    ax.axhline(0, color="#334155", lw=0.8)
    ax.set_title(spec["name"], color=NAVY, fontsize=10.5, weight="bold")
    ax.set_xlabel("Nifty at horizon", fontsize=8.5)
    ax.set_ylabel("P&L (points/unit)", fontsize=8.5)
    ax.grid(alpha=0.22); ax.tick_params(labelsize=8)
    # annotation box with computed metrics
    mp = "unlimited" if ev["unlimited_up"] else f"{ev['max_profit']:.0f}"
    ml = "unlimited" if ev["unlimited_dn"] else f"{ev['max_loss']:.0f}"
    be = ", ".join(f"{b:.0f}" for b in ev["breakevens"]) or "—"
    txt = f"Max P {mp} | Max L {ml}\nBE: {be}"
    ax.text(0.02, 0.04, txt, transform=ax.transAxes, fontsize=7.5, color="#334155",
            va="bottom", bbox=dict(boxstyle="round", fc="#f1f5f9", ec="#cbd5e1"))
    fig.tight_layout()
    path = os.path.join(FIGDIR, spec["slug"] + ".png")
    fig.savefig(path, dpi=120, facecolor="white")
    plt.close(fig)
    return path


def risk_reward(ev):
    """Defined-risk R:R as |reward|:|risk|, else None."""
    if ev["unlimited_up"] or ev["unlimited_dn"]:
        return None
    risk = abs(ev["max_loss"]); reward = abs(ev["max_profit"])
    if risk < 1e-6:
        return None
    return round(reward / risk, 2)


def run(strategies):
    out = []
    for i, spec in enumerate(strategies, 1):
        ev = evaluate(spec)
        plot(spec, ev)
        rr = risk_reward(ev)
        out.append({
            "n": i, "slug": spec["slug"], "name": spec["name"], "category": spec["category"],
            "view": spec.get("view", ""), "vol": spec.get("vol", ""),
            "legs_text": fmt_legs(ev["legs"]),
            "net_cost": round(ev["net_cost"], 1),
            "debit_credit": "debit" if ev["net_cost"] > 0 else "credit",
            "max_profit": None if ev["unlimited_up"] else round(ev["max_profit"], 0),
            "max_loss": None if ev["unlimited_dn"] else round(ev["max_loss"], 0),
            "max_profit_unlimited": ev["unlimited_up"],
            "max_loss_unlimited": ev["unlimited_dn"],
            "breakevens": [round(b, 0) for b in ev["breakevens"]],
            "risk_reward": rr,
            "scenarios": [{"spot": s["spot"], "pnl_pts": s["pnl_pts"],
                           "pnl_rupees": round(s["pnl_pts"] * LOT)} for s in ev["scenarios"]],
            "lot": LOT,
            "fig": f"figs/strategies/{spec['slug']}.png",
            "tagline": spec.get("note", ""),
        })
    with open(os.path.join(ROOT, "strategies_metrics.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    return out


if __name__ == "__main__":
    import strategies_data as sd
    res = run(sd.STRATEGIES)
    print(f"strategies processed: {len(res)}")
    print(f"figures in: {FIGDIR}")
    cats = {}
    for r in res:
        cats[r["category"]] = cats.get(r["category"], 0) + 1
    for c, n in cats.items():
        print(f"  {n:>3}  {c}")
