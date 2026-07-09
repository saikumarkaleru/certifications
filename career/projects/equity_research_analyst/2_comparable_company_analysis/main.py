"""
=============================================================================
 COMPARABLE COMPANY ANALYSIS ("COMPS")  --  live, real-company edition
=============================================================================
Pulls a REAL target + ~6 real peers from yfinance, computes trading multiples
(P/E, EV/EBITDA, EV/Revenue, P/B, PEG), summarises the peer set (median / mean /
quartiles), derives an implied valuation per multiple and a blended football-
field range vs the current price, and runs a rich/cheap screen (z-scores + an
OLS regression of EV/EBITDA on growth & margin) -- then writes a formatted Excel
workbook and a football-field chart.

Run:   python main.py             (target AAPL, mega-cap tech peers)
       python main.py MSFT        (any target from the peer set)

Everything is fully explainable -- see STUDY_GUIDE.md.
=============================================================================
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

import pandas as pd  # noqa: E402
from comps import data, multiples, stats, valuation, report  # noqa: E402

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def main(target="AAPL"):
    print("=" * 74)
    print(f"  COMPARABLE COMPANY ANALYSIS  --  target: {target}")
    print("=" * 74)

    # 1) DATA -------------------------------------------------------------
    universe = data.load_universe(target=target)
    target = universe["target"]
    print(f"  Source ... {universe['source']}  ({universe.get('as_of')})")
    print(f"  Universe . {', '.join(universe['companies'].keys())}")

    # 2) MULTIPLES --------------------------------------------------------
    mult_df = multiples.build_multiples_table(universe)
    pd.set_option("display.width", 130)
    pd.set_option("display.max_columns", 20)
    show = mult_df[["name", "P/E", "EV/EBITDA", "EV/Revenue", "P/B", "PEG"]].round(2)
    print("\nTRADING MULTIPLES (by company)")
    print(show.to_string())

    # 3) PEER SUMMARY (peers only; target excluded) -----------------------
    summary = stats.peer_summary(mult_df, target)
    print("\nPEER SUMMARY (median / mean / quartiles -- peers only)")
    print(summary.round(2).to_string())

    peer_stats = {"Median": summary["Median"], "Mean": summary["Mean"]}

    # 4) IMPLIED VALUATION + FOOTBALL FIELD -------------------------------
    implied_df, football = valuation.implied_valuation(universe, peer_stats)
    print(f"\nIMPLIED VALUATION of {target} "
          f"(peer median multiple applied to target metrics)")
    print(implied_df.round(2).to_string(index=False))
    print("\nFOOTBALL FIELD (implied price/share)")
    print(f"  Low ............. ${football['low']:,.2f}")
    print(f"  Median .......... ${football['median']:,.2f}")
    print(f"  High ............ ${football['high']:,.2f}")
    print(f"  Current price ... ${football['current_price']:,.2f}")
    print(f"  Upside to median  {football['upside_to_median']:+.1%}")
    print(f"  VERDICT ......... {football['verdict']}")

    # 5) RICH/CHEAP SCREEN ------------------------------------------------
    zscreen = stats.zscore_screen(mult_df)
    print("\nSCREEN (a): z-scores of raw multiples (positive = richer)")
    print(zscreen.round(2).to_string())

    reg_df, reg_coef, reg_r2 = stats.regression_screen(mult_df)
    print("\nSCREEN (b): OLS  EV/EBITDA ~ revenue growth + EBITDA margin")
    if not reg_df.empty:
        print(f"  fair EV/EBITDA = {reg_coef['intercept']:.1f} "
              f"+ {reg_coef['rev_growth']:.1f}*growth "
              f"+ {reg_coef['ebitda_margin']:.1f}*margin   (R^2={reg_r2:.2f})")
        print(reg_df[["actual_EV/EBITDA", "predicted_EV/EBITDA",
                      "residual", "flag"]].round(2).to_string())
    else:
        print("  (not enough complete observations to fit the regression)")

    # 6) OUTPUT: Excel + chart -------------------------------------------
    xlsx = os.path.join(OUT_DIR, "comparable_company_analysis.xlsx")
    report.write_workbook(xlsx, universe, mult_df, summary, implied_df,
                          football, zscreen, reg_df, reg_coef, reg_r2)
    png = report.chart_football_field(
        os.path.join(OUT_DIR, "football_field.png"), implied_df, football,
        universe)

    print("\nFILES WRITTEN")
    for p in (xlsx, png):
        print(f"  {p}")
    print("Done.")


if __name__ == "__main__":
    tk = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    main(tk)
