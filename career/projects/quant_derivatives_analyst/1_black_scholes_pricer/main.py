"""
main.py  --  Black-Scholes / Binomial / Monte-Carlo options analytics (orchestrator)
====================================================================================

WHAT THIS SCRIPT DEMONSTRATES, top to bottom (each step prints a summary):

  1. Price a sample ATM option: call/put price, ALL first- and second-order
     Greeks, and the put-call parity check.
  2. Cross-check the price three ways: closed-form BSM vs CRR binomial tree vs
     Monte-Carlo -- they must agree within tolerance.
  3. Show the American early-exercise premium (American put > European put).
  4. Implied-vol round-trip: price with a known sigma, recover it from the price.
  5. Validate analytic Greeks against finite differences (bump-and-reprice).
  6. Pull a REAL option chain (yfinance, with offline fallback), solve each
     contract's implied vol from its mid price, report pricing accuracy, and
     build the implied-vol SMILE (IV vs strike).
  7. Write output/black_scholes_summary.xlsx (sheets: Prices, Greeks, Validation, Smile).
  8. Save charts to output/: payoff, Greeks-vs-spot, IV smile, tree convergence.

DEPENDENCIES: numpy, pandas, matplotlib (Agg), openpyxl, yfinance. Normal CDF is
built from math.erf, so no scipy and no mandatory network (offline fallback).

Run:  python main.py
"""

import os
import sys
import math
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")                 # non-interactive: just write PNGs, never open a window
import matplotlib.pyplot as plt

# --- Absolute-path-safe wiring so the script runs from anywhere -------------
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)
OUTDIR = os.path.join(HERE, "output")
os.makedirs(OUTDIR, exist_ok=True)

from pricer import (bs_price, put_call_parity_gap, all_greeks, greeks,
                    crr_price, mc_price, implied_vol, validate_greeks,
                    get_option_chain)


def hr(title):
    """Print a titled horizontal rule -- keeps the console output readable."""
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


def main():
    # =====================================================================
    # STEP 1 -- Sample ATM option: price, Greeks, put-call parity
    # =====================================================================
    S, K, T, r, q, sigma = 100.0, 100.0, 1.0, 0.05, 0.0, 0.20
    hr("STEP 1  Sample option: price + Greeks + put-call parity")
    print(f"Inputs: S={S}  K={K}  T={T}yr  r={r:.0%}  q={q:.0%}  sigma={sigma:.0%}")

    call_px = bs_price(S, K, T, r, sigma, "call", q)
    put_px = bs_price(S, K, T, r, sigma, "put", q)
    print(f"  Call price: {call_px:10.4f}")
    print(f"  Put  price: {put_px:10.4f}")

    lhs = call_px - put_px
    rhs = put_call_parity_gap(S, K, T, r, q)
    print(f"  Put-call parity:  C - P = {lhs:.6f}   vs   "
          f"S e^(-qT) - K e^(-rT) = {rhs:.6f}   (diff {abs(lhs-rhs):.2e})")

    cg = all_greeks(S, K, T, r, sigma, "call", q)
    pg = all_greeks(S, K, T, r, sigma, "put", q)
    print("\n  Greek        Call         Put     (scaling)")
    scaling = {"Delta": "per $1", "Gamma": "per $1^2", "Vega": "per 1% vol",
               "Theta": "per day", "Rho": "per 1% rate", "Vanna": "per 1% vol",
               "Volga": "per 1% vol", "Charm": "per day"}
    greeks_rows = []
    for g in ["Delta", "Gamma", "Vega", "Theta", "Rho", "Vanna", "Volga", "Charm"]:
        print(f"  {g:6s} {cg[g]:11.6f} {pg[g]:11.6f}    ({scaling[g]})")
        greeks_rows.append({"Greek": g, "Call": cg[g], "Put": pg[g],
                            "Scaling": scaling[g]})
    greeks_df = pd.DataFrame(greeks_rows)

    # =====================================================================
    # STEP 2 -- Three pricers must agree: BSM vs CRR tree vs Monte-Carlo
    # =====================================================================
    hr("STEP 2  Cross-check: BSM vs CRR tree vs Monte-Carlo")
    tree_call = crr_price(S, K, T, r, sigma, "call", q, N=1000, american=False)
    mc_call, mc_se = mc_price(S, K, T, r, sigma, "call", q, n_paths=400_000, seed=7)
    print(f"  BSM  (closed form) : {call_px:10.4f}")
    print(f"  CRR  (1000 steps)  : {tree_call:10.4f}   (diff vs BSM {abs(tree_call-call_px):.2e})")
    print(f"  MC   (400k paths)  : {mc_call:10.4f}   +/- {mc_se:.4f} (1 s.e.)")
    within = abs(mc_call - call_px) < 4 * mc_se
    print(f"  BSM within MC confidence band? {'YES' if within else 'NO'}")

    prices_df = pd.DataFrame([
        {"Method": "Black-Scholes (closed form)", "Call": call_px, "Put": put_px},
        {"Method": "CRR binomial tree (N=1000)", "Call": tree_call,
         "Put": crr_price(S, K, T, r, sigma, "put", q, N=1000)},
        {"Method": "Monte-Carlo (400k, antithetic)", "Call": mc_call,
         "Put": mc_price(S, K, T, r, sigma, "put", q, n_paths=400_000, seed=7)[0]},
    ])

    # =====================================================================
    # STEP 3 -- American early-exercise premium (American put > European put)
    # =====================================================================
    hr("STEP 3  American early-exercise premium (ITM put)")
    # Use an in-the-money put on a higher-rate name so early exercise clearly pays.
    Sa, Ka, Ta, ra, qa, siga = 100.0, 110.0, 1.0, 0.08, 0.0, 0.30
    eu_put = crr_price(Sa, Ka, Ta, ra, siga, "put", qa, N=1000, american=False)
    am_put = crr_price(Sa, Ka, Ta, ra, siga, "put", qa, N=1000, american=True)
    print(f"  Inputs: S={Sa} K={Ka} T={Ta} r={ra:.0%} sigma={siga:.0%}")
    print(f"  European put : {eu_put:10.4f}")
    print(f"  American put : {am_put:10.4f}")
    print(f"  Early-exercise premium : {am_put - eu_put:10.4f}  (>= 0 always)")

    # =====================================================================
    # STEP 4 -- Implied-vol round-trip
    # =====================================================================
    hr("STEP 4  Implied-vol round-trip (recover a known sigma)")
    true_sigma = 0.2734
    px = bs_price(S, K, T, r, true_sigma, "call", q)
    rec = implied_vol(px, S, K, T, r, "call", q)
    print(f"  Priced a call at sigma = {true_sigma:.4f}  ->  price {px:.6f}")
    print(f"  Solver recovered sigma = {rec:.6f}   (error {abs(rec-true_sigma):.2e})")

    # =====================================================================
    # STEP 5 -- Greeks validation vs finite differences
    # =====================================================================
    hr("STEP 5  Analytic Greeks vs finite differences (call)")
    val_df = validate_greeks(S, K, T, r, sigma, "call", q)
    print(val_df.to_string(index=False,
          formatters={"Analytic": "{:.6f}".format,
                      "Numeric": "{:.6f}".format,
                      "AbsError": "{:.2e}".format}))
    print(f"  Max abs error across Greeks: {val_df['AbsError'].max():.2e}")

    # =====================================================================
    # STEP 6 -- Real option chain: IV per contract + pricing accuracy + SMILE
    # =====================================================================
    hr("STEP 6  Real option chain -> implied vols -> smile")
    chain = get_option_chain(ticker="AAPL", expiry=None)
    print(f"  Source: {chain['source'].iloc[0]}   contracts: {len(chain)}")
    spot = float(chain["spot"].iloc[0])
    Tc = float(chain["T"].iloc[0])
    rc = float(chain["r"].iloc[0])
    qc = float(chain["q"].iloc[0])
    print(f"  Spot={spot:.2f}  T={Tc:.4f}yr  r={rc:.0%}  q={qc:.0%}")

    smile_rows = []
    for _, row in chain.iterrows():
        Kc = float(row["strike"])
        mid = float(row["mid"])
        iv = implied_vol(mid, spot, Kc, Tc, rc, "call", qc)   # market IV
        if not math.isfinite(iv):
            continue                                          # skip un-invertible quotes
        model_px = bs_price(spot, Kc, Tc, rc, iv, "call", qc)  # re-price with that IV
        smile_rows.append({
            "Strike": Kc,
            "Moneyness": Kc / spot,
            "MarketMid": mid,
            "ImpliedVol": iv,
            "ModelPrice": model_px,
            "AbsErr": abs(model_px - mid),
        })
    smile_df = pd.DataFrame(smile_rows).sort_values("Strike").reset_index(drop=True)
    print(f"  Solved IVs for {len(smile_df)} contracts.")
    print(f"  Re-pricing accuracy: mean abs err {smile_df['AbsErr'].mean():.2e}, "
          f"max {smile_df['AbsErr'].max():.2e}")
    print("\n  Strike   Moneyness   MarketMid   ImpliedVol")
    for _, rrow in smile_df.iterrows():
        print(f"  {rrow['Strike']:7.2f}   {rrow['Moneyness']:8.3f}   "
              f"{rrow['MarketMid']:9.4f}   {rrow['ImpliedVol']:9.4f}")

    # =====================================================================
    # STEP 7 -- Excel workbook (Prices, Greeks, Validation, Smile)
    # =====================================================================
    hr("STEP 7  Writing Excel workbook")
    xlsx = os.path.join(OUTDIR, "black_scholes_summary.xlsx")
    with pd.ExcelWriter(xlsx, engine="openpyxl") as w:
        prices_df.to_excel(w, sheet_name="Prices", index=False)
        greeks_df.to_excel(w, sheet_name="Greeks", index=False)
        val_df.to_excel(w, sheet_name="Validation", index=False)
        smile_df.to_excel(w, sheet_name="Smile", index=False)
    print(f"  Wrote {xlsx}")

    # =====================================================================
    # STEP 8 -- Charts
    # =====================================================================
    hr("STEP 8  Saving charts")
    spots = np.linspace(50, 150, 200)

    # (a) Payoff at expiry vs value today (call): the gap is time value.
    call_curve = [bs_price(s, K, T, r, sigma, "call", q) for s in spots]
    payoff = np.maximum(spots - K, 0.0)
    plt.figure(figsize=(8, 5))
    plt.plot(spots, payoff, label="Payoff at expiry  max(S-K,0)")
    plt.plot(spots, call_curve, label="Value today (incl. time value)")
    plt.axvline(K, color="grey", ls="--", alpha=0.6, label="Strike")
    plt.title("Call: Payoff at Expiry vs Value Today")
    plt.xlabel("Spot S"); plt.ylabel("Value"); plt.legend(); plt.grid(alpha=0.3)
    plt.savefig(os.path.join(OUTDIR, "payoff_diagram.png"), dpi=120, bbox_inches="tight")
    plt.close()

    # (b) Greeks vs spot: delta / gamma / vega on one figure (shared x).
    deltas = [greeks(s, K, T, r, sigma, "call", q)["Delta"] for s in spots]
    gammas = [greeks(s, K, T, r, sigma, "call", q)["Gamma"] for s in spots]
    vegas = [greeks(s, K, T, r, sigma, "call", q)["Vega"] for s in spots]
    fig, ax = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
    ax[0].plot(spots, deltas, color="C0"); ax[0].set_ylabel("Delta")
    ax[0].axvline(K, color="grey", ls="--", alpha=0.5); ax[0].grid(alpha=0.3)
    ax[0].set_title("Call Greeks vs Spot")
    ax[1].plot(spots, gammas, color="C1"); ax[1].set_ylabel("Gamma")
    ax[1].axvline(K, color="grey", ls="--", alpha=0.5); ax[1].grid(alpha=0.3)
    ax[2].plot(spots, vegas, color="C2"); ax[2].set_ylabel("Vega (per 1%)")
    ax[2].axvline(K, color="grey", ls="--", alpha=0.5); ax[2].grid(alpha=0.3)
    ax[2].set_xlabel("Spot S")
    plt.savefig(os.path.join(OUTDIR, "greeks_vs_spot.png"), dpi=120, bbox_inches="tight")
    plt.close()

    # (c) Implied-vol smile: IV vs strike from the real/synthetic chain.
    plt.figure(figsize=(8, 5))
    plt.plot(smile_df["Strike"], smile_df["ImpliedVol"], "o-", color="C3")
    plt.axvline(spot, color="grey", ls="--", alpha=0.6, label=f"Spot {spot:.1f}")
    plt.title("Implied Volatility Smile")
    plt.xlabel("Strike K"); plt.ylabel("Implied vol"); plt.legend(); plt.grid(alpha=0.3)
    plt.savefig(os.path.join(OUTDIR, "iv_smile.png"), dpi=120, bbox_inches="tight")
    plt.close()

    # (d) Tree convergence: CRR price vs N steps, approaching the BSM line.
    Ns = [5, 10, 20, 40, 80, 160, 320, 640]
    tree_prices = [crr_price(S, K, T, r, sigma, "call", q, N=n) for n in Ns]
    plt.figure(figsize=(8, 5))
    plt.plot(Ns, tree_prices, "o-", label="CRR tree price")
    plt.axhline(call_px, color="red", ls="--", label=f"BSM = {call_px:.4f}")
    plt.title("CRR Binomial Convergence to Black-Scholes")
    plt.xlabel("Number of steps N"); plt.ylabel("Call price")
    plt.legend(); plt.grid(alpha=0.3)
    plt.savefig(os.path.join(OUTDIR, "tree_convergence.png"), dpi=120, bbox_inches="tight")
    plt.close()

    for f in ["payoff_diagram.png", "greeks_vs_spot.png", "iv_smile.png",
              "tree_convergence.png"]:
        print(f"  Saved output/{f}")

    hr("DONE")
    print("  Excel + 4 charts written to output/.  All steps completed cleanly.")


if __name__ == "__main__":
    main()
