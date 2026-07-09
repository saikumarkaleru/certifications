"""
=============================================================================
 DCF (DISCOUNTED CASH FLOW) VALUATION  --  live, real-company edition
=============================================================================
Pulls a REAL company's financials from yfinance, derives its unlevered free
cash flow (FCFF), estimates a WACC from CAPM + a live risk-free rate, projects
FCFF with fading growth, builds two terminal values, discounts to an intrinsic
value per share, and stress-tests it with scenarios, a 2-way sensitivity grid
and a reverse DCF -- then writes a formatted Excel workbook and two charts.

Run:   python main.py            (defaults to AAPL)
       python main.py MSFT       (any ticker)

Everything is fully explainable -- see STUDY_GUIDE.md.
=============================================================================
"""

import os
import sys

# Make the src/ package importable when run directly.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from dcf import data, fcff, wacc as wacc_mod, model, report  # noqa: E402

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

# ---------------------------------------------------------------------------
# Model assumptions (drivers). Each is defended in STUDY_GUIDE.md.
# ---------------------------------------------------------------------------
FORECAST_YEARS = 5
BASE_START_GROWTH = 0.08     # year-1 FCFF growth (fades to terminal)
TERMINAL_GROWTH = 0.025      # long-run growth ~ nominal GDP
EXIT_MULTIPLE = 14.0         # exit EV/EBITDA for the second terminal value


def fmt_b(x):
    """Format a big dollar number in $ billions."""
    return f"${x / 1e9:,.1f}B"


def main(ticker="AAPL"):
    print("=" * 72)
    print(f"  DCF VALUATION  --  fetching {ticker} ...")
    print("=" * 72)

    # 1) DATA -------------------------------------------------------------
    company = data.load_company(ticker)
    print(f"  Company ... {company['name']} ({company['ticker']})")
    print(f"  Source .... {company['source']}  ({company.get('as_of')})")
    print(f"  Price ..... ${company['price']:,.2f}   "
          f"Shares: {company['shares'] / 1e9:,.2f}B   "
          f"Net debt: {fmt_b(company.get('net_debt') or 0)}")

    # 2) FCFF -------------------------------------------------------------
    # Use the multi-year AVERAGE as the base to normalise one-off working-capital
    # swings (e.g. a single year with a large receivables build).
    base_fcff_val, fcff_rows = fcff.base_fcff(company, method="average")
    base_ebitda = fcff.latest_ebitda(company)
    print("\nFREE CASH FLOW TO THE FIRM (derived from statements)")
    print(f"  {'Year':<6}{'EBIT':>14}{'NOPAT':>14}{'D&A':>12}"
          f"{'Capex':>14}{'ChgWC':>14}{'FCFF':>14}")
    for r in fcff_rows:
        print(f"  {str(r['year']):<6}{fmt_b(r['ebit']):>14}"
              f"{fmt_b(r['nopat']):>14}{fmt_b(r['dep_amort']):>12}"
              f"{fmt_b(r['capex']):>14}{fmt_b(r['change_in_wc']):>14}"
              f"{fmt_b(r['fcff']):>14}")
    if fcff_rows[0]["fcff_check"] is not None:
        print(f"  (cross-check FCFF from CFO method: "
              f"{fmt_b(fcff_rows[0]['fcff_check'])})")
    print(f"  Base FCFF used ....... {fmt_b(base_fcff_val)}")

    # 3) WACC -------------------------------------------------------------
    w = wacc_mod.estimate_wacc(company)
    print("\nWACC (discount rate) via CAPM")
    print(f"  Risk-free (10Y) ...... {w['risk_free_rate']:.2%}")
    print(f"  Beta ................. {w['beta']:.2f}")
    print(f"  Equity risk premium .. {w['erp']:.2%}")
    print(f"  Cost of equity (CAPM)  {w['cost_of_equity']:.2%}")
    print(f"  Cost of debt (a.t.) .. {w['cost_of_debt_after_tax']:.2%}   "
          f"(pre-tax {w['cost_of_debt_pre_tax']:.2%})")
    print(f"  Weights E/D .......... {w['weight_equity']:.1%} / {w['weight_debt']:.1%}")
    print(f"  WACC ................. {w['wacc']:.2%}")

    net_debt = company.get("net_debt") or 0.0
    shares = company["shares"]

    # 4) BASE-CASE DCF ----------------------------------------------------
    base_res = model.run_dcf(base_fcff_val, BASE_START_GROWTH, TERMINAL_GROWTH,
                             w["wacc"], net_debt, shares, FORECAST_YEARS,
                             base_ebitda, EXIT_MULTIPLE)
    upside = base_res["value_per_share"] / company["price"] - 1
    verdict = "UNDERVALUED" if upside > 0 else "OVERVALUED"

    print("\nBASE-CASE VALUATION BRIDGE")
    print(f"  PV of explicit FCFF .. {fmt_b(base_res['pv_explicit'])}")
    print(f"  Terminal (Gordon) .... {fmt_b(base_res['tv_gordon'])}")
    if base_res["tv_exit"]:
        print(f"  Terminal (exit mult.)  {fmt_b(base_res['tv_exit'])}")
    print(f"  PV of terminal value . {fmt_b(base_res['pv_terminal'])}  "
          f"({base_res['terminal_pct_of_ev']:.0%} of EV)")
    print(f"  ENTERPRISE VALUE ..... {fmt_b(base_res['enterprise_value'])}")
    print(f"  Less: net debt ....... {fmt_b(net_debt)}")
    print(f"  EQUITY VALUE ......... {fmt_b(base_res['equity_value'])}")
    print(f"  INTRINSIC VALUE/SHARE  ${base_res['value_per_share']:,.2f}")
    print(f"  Current price ........ ${company['price']:,.2f}")
    print(f"  Upside/(downside) .... {upside:+.1%}   -> {verdict}")

    # 5) SCENARIOS --------------------------------------------------------
    scen = model.run_scenarios(base_fcff_val, w["wacc"], net_debt, shares,
                               FORECAST_YEARS, base_ebitda, EXIT_MULTIPLE,
                               BASE_START_GROWTH, TERMINAL_GROWTH)
    print("\nSCENARIOS (value / share)")
    for name in ["Bear", "Base", "Bull"]:
        s = scen[name]
        print(f"  {name:<5} growth {s['start_growth']:+.0%}  WACC {s['wacc']:.1%}"
              f"  ->  ${s['value_per_share']:,.2f}")

    # 6) SENSITIVITY ------------------------------------------------------
    sens = model.sensitivity_grid(base_fcff_val, BASE_START_GROWTH, net_debt,
                                  shares, FORECAST_YEARS, base_ebitda,
                                  EXIT_MULTIPLE, w["wacc"], TERMINAL_GROWTH)
    wacc_vals, term_vals, matrix = sens
    print("\nSENSITIVITY: value/share  (rows=WACC, cols=terminal g)")
    header = "        " + "".join(f"{g:>9.1%}" for g in term_vals)
    print(header)
    for i, wv in enumerate(wacc_vals):
        cells = "".join(
            (f"{matrix[i][j]:>9.0f}" if not (matrix[i][j] != matrix[i][j])
             else f"{'-':>9}")
            for j in range(len(term_vals)))
        print(f"  {wv:>5.1%} {cells}")

    # 7) REVERSE DCF ------------------------------------------------------
    rev = model.reverse_dcf(company["price"], base_fcff_val, TERMINAL_GROWTH,
                            w["wacc"], net_debt, shares, FORECAST_YEARS,
                            base_ebitda, EXIT_MULTIPLE)
    print("\nREVERSE DCF")
    if rev["implied_growth"] is not None:
        print(f"  Market price implies a year-1 FCFF growth of "
              f"{rev['implied_growth']:.1%}")
        print(f"  (our base case assumes {BASE_START_GROWTH:.1%})")
    else:
        print(f"  {rev['note']}")

    # 8) OUTPUT: Excel + charts ------------------------------------------
    model_assumptions = {
        "base_fcff": base_fcff_val,
        "start_growth": BASE_START_GROWTH,
        "terminal_growth": TERMINAL_GROWTH,
        "exit_multiple": EXIT_MULTIPLE,
        "years": FORECAST_YEARS,
    }
    xlsx = os.path.join(OUT_DIR, "dcf_valuation.xlsx")
    report.write_workbook(xlsx, company, w, fcff_rows,
                          {"result": base_res}, scen, sens, rev,
                          model_assumptions)
    bridge_png = report.chart_fcf_bridge(
        os.path.join(OUT_DIR, "fcf_bridge.png"), {"result": base_res}, company)
    ff_png = report.chart_football_field(
        os.path.join(OUT_DIR, "football_field.png"), scen, rev, company,
        BASE_START_GROWTH)

    print("\nFILES WRITTEN")
    for p in (xlsx, bridge_png, ff_png):
        print(f"  {p}")
    print("Done.")


if __name__ == "__main__":
    tk = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    main(tk)
