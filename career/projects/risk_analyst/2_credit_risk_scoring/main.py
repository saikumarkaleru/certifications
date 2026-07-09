# =============================================================================
# CREDIT RISK SCORING  -  ALTMAN Z-SCORE + MERTON STRUCTURAL MODEL
# =============================================================================
# GOAL: Score the default risk of ~10 real large-cap companies two independent,
# defensible ways, then roll them into a loan-book expected loss.
#
#   1. ALTMAN Z-SCORE  (accounting model): five balance-sheet ratios -> one
#      bankruptcy score -> Safe / Grey / Distress zone.
#   2. MERTON MODEL    (structural model): treat equity as a call option on the
#      firm's assets, back out asset value & volatility from the market, and read
#      off a distance-to-default and probability of default (PD).
#   3. PORTFOLIO EL    = sum of  PD * LGD * EAD  across issuers.
#
# Data is pulled LIVE from yfinance, cached to input/, and falls back to a
# realistic built-in dataset so the app ALWAYS runs offline.
#
# Run:  python main.py
# =============================================================================

import os
import sys

import pandas as pd

# Make the src/ package importable whether run from here or elsewhere.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, "src"))

from credit import data, altman, merton, portfolio, reporting  # noqa: E402

INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


def _fmt_money(x: float) -> str:
    return f"${x:,.0f}"


def main() -> None:
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # -- 1. DATA ----------------------------------------------------------
    inputs, source = data.load_credit_inputs(input_dir=INPUT_DIR, use_live=True)

    # -- 2. ALTMAN --------------------------------------------------------
    altman_tbl = altman.compute_altman(inputs)

    # -- 3. MERTON --------------------------------------------------------
    merton_tbl = merton.compute_merton(inputs, r=data.RISK_FREE_RATE, t=1.0)

    # -- 4. COMBINE + RANK ------------------------------------------------
    combined = portfolio.combine(altman_tbl, merton_tbl)

    # -- 5. PORTFOLIO EXPECTED LOSS --------------------------------------
    el_table = portfolio.expected_loss(merton_tbl)
    summary = portfolio.portfolio_summary(el_table)

    # -- 6. REPORT: EXCEL + CHARTS ---------------------------------------
    excel_path = os.path.join(OUTPUT_DIR, "credit_analysis.xlsx")
    reporting.write_excel(excel_path, inputs, altman_tbl, merton_tbl,
                          combined, el_table, summary)
    bar_path = reporting.chart_altman_bar(
        altman_tbl, os.path.join(OUTPUT_DIR, "altman_zscore_bar.png"))
    scatter_path = reporting.chart_pd_vs_z(
        altman_tbl, merton_tbl,
        os.path.join(OUTPUT_DIR, "pd_vs_zscore_scatter.png"))

    # -- 7. CONSOLE SUMMARY ----------------------------------------------
    line = "=" * 78
    print(line)
    print("CREDIT RISK SCORING  -  ALTMAN Z-SCORE + MERTON STRUCTURAL MODEL")
    print(line)
    print(f"Data source : {source}   (LIVE=yfinance, CACHED=input/, "
          f"FALLBACK=built-in)")
    print(f"Universe    : {len(inputs)} issuers  -> {', '.join(inputs.index)}")
    print(f"Assumptions : r={data.RISK_FREE_RATE:.0%}, T=1yr, "
          f"LGD={portfolio.LGD:.0%}, EAD={_fmt_money(portfolio.EAD_PER_ISSUER)}"
          f"/issuer")

    print("\n" + "-" * 78)
    print("ALTMAN Z-SCORE (accounting model)   Z>2.99 Safe | 1.81-2.99 Grey | "
          "<1.81 Distress")
    print("-" * 78)
    with pd.option_context("display.width", 120,
                           "display.float_format", "{:.3f}".format):
        print(altman_tbl.to_string())

    print("\n" + "-" * 78)
    print("MERTON STRUCTURAL MODEL (market-implied)   DD=distance-to-default, "
          "PD=prob. of default")
    print("-" * 78)
    show = merton_tbl.copy()
    show["default_point"] = show["default_point"].map(lambda v: f"{v/1e9:,.1f}B")
    show["asset_value"] = show["asset_value"].map(lambda v: f"{v/1e9:,.1f}B")
    show["asset_vol"] = show["asset_vol"].map(lambda v: f"{v:.1%}")
    show["DD"] = show["DD"].map(lambda v: f"{v:.2f}")
    show["PD"] = show["PD"].map(lambda v: f"{v:.3%}")
    print(show.to_string())

    print("\n" + "-" * 78)
    print("RANKED RISK TABLE (riskiest first by Merton PD)")
    print("-" * 78)
    for tk, row in combined.iterrows():
        flag = "" if row["converged"] else "  [!merton not converged]"
        agree = "agree" if row["agree"] else "DISAGREE"
        z_str = f"{row['Z']:6.2f}" if pd.notna(row["Z"]) else "   n/a"
        rz = int(row["rank_altman"]) if pd.notna(row["rank_altman"]) else 0
        rz_str = f"{rz:>2}" if rz else " -"
        print(f"  {tk:<5}  Z={z_str} ({row['Zone']:<8})  "
              f"PD={row['PD']:7.3%}  DD={row['DD']:5.2f}  "
              f"rankZ={rz_str} rankPD={int(row['rank_merton']):>2}"
              f"  [{agree}]{flag}")

    n_disagree = int((~combined["agree"]).sum())
    print(f"\n  Models agree on {len(combined) - n_disagree}/{len(combined)} "
          f"issuers; {n_disagree} disagreement(s).")

    print("\n" + "-" * 78)
    print("PORTFOLIO EXPECTED LOSS   EL = PD * LGD * EAD")
    print("-" * 78)
    for tk, row in el_table.iterrows():
        print(f"  {tk:<5}  PD={row['PD']:7.3%}  LGD={row['LGD']:.0%}  "
              f"EAD={_fmt_money(row['EAD'])}  ->  EL={_fmt_money(row['EL'])}")
    print("-" * 78)
    print(f"  Total exposure (EAD) : {_fmt_money(summary['total_ead'])}")
    print(f"  Portfolio expected loss: {_fmt_money(summary['total_el'])}  "
          f"({summary['el_pct']:.3%} of exposure)")

    print("\n" + "-" * 78)
    print("FILES WRITTEN")
    print("-" * 78)
    print(f"  Excel : {excel_path}")
    print(f"  Chart : {bar_path}")
    print(f"  Chart : {scatter_path}")
    print(f"  Cache : {os.path.join(INPUT_DIR, 'credit_inputs.csv')}")
    print(line)
    print("Done.")


if __name__ == "__main__":
    main()
