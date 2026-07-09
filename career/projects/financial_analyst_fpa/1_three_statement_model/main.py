"""
main.py — orchestrate the whole three-statement model, end to end.
============================================================================
Run this file:  `python main.py`   (works offline after the first data pull).

What it does, in order:
  1. LOAD real financials for a company (default MSFT) via yfinance, cache them
     to input/, and derive the model's drivers. Falls back to bundled numbers if
     there's no network and no cache, so it always runs.
  2. BUILD the linked 5-year three-statement model (with the debt cash sweep).
  3. Run BULL / BASE / BEAR scenarios and a 2-way DCF sensitivity table.
  4. VALUE the business with a DCF off the model's free cash flow.
  5. PRINT a console summary and WRITE the Excel workbook + PNG charts.

Read src/model/*.py for the heavy commenting on each step.
"""

from __future__ import annotations

import os
import sys

# make `import model...` work no matter where python is launched from
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from model import data, forecast, scenarios, valuation, reporting  # noqa: E402

TICKER = "MSFT"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def main(ticker: str = TICKER) -> None:
    # ---- 1) DATA -----------------------------------------------------------
    bundle = data.load(ticker)
    drivers, opening, meta, source = (
        bundle["drivers"], bundle["opening"], bundle["meta"], bundle["source"])

    src_label = {"live": "LIVE yfinance pull (cached to input/)",
                 "cache": "local cache in input/ (offline)",
                 "fallback": "bundled illustrative fallback (no network/cache)"}[source]

    print("=" * 68)
    print(f" THREE-STATEMENT MODEL + DCF  -  {bundle['ticker']}")
    print("=" * 68)
    print(f"Data source : {src_label}")
    print(f"Start revenue: ${drivers['start_revenue']:,.0f}m   "
          f"growth {drivers['revenue_growth']:.1%}   "
          f"gross margin {drivers['gross_margin']:.1%}   "
          f"tax {drivers['tax_rate']:.1%}")

    # ---- 2) BUILD THE MODEL ------------------------------------------------
    model = forecast.build_model(drivers, opening)

    print("\n--- INCOME STATEMENT ($m) ---")
    print(model["income"])
    print("\n--- BALANCE SHEET ($m) ---")
    print(model["balance"])
    print("\n--- CASH FLOW STATEMENT ($m) ---")
    print(model["cashflow"])
    print("\n--- DEBT SCHEDULE / CASH SWEEP ($m) ---")
    print(model["debt"])

    print(f"\nBalance sheet ties out every year "
          f"(max imbalance = {model['max_imbalance']:.6f})")

    # ---- 3) SCENARIOS + SENSITIVITY ---------------------------------------
    scen = scenarios.run_scenarios(drivers, opening, meta)
    sens = scenarios.sensitivity_table(drivers, opening, meta)
    print("\n--- SCENARIOS (Bull / Base / Bear) ---")
    print(scen)
    print("\n--- SENSITIVITY: DCF value/share, growth (rows) x gross margin (cols) ---")
    print(sens)

    # ---- 4) DCF VALUATION --------------------------------------------------
    dcf = valuation.run_dcf(model, drivers, opening, meta)
    print("\n--- DCF VALUATION ---")
    print(f"WACC             : {dcf['wacc']:.2%}  "
          f"(Ke {dcf['cost_of_equity']:.2%}, after-tax Kd "
          f"{dcf['cost_of_debt_after_tax']:.2%}, "
          f"We {dcf['weight_equity']:.0%}/Wd {dcf['weight_debt']:.0%})")
    print(f"Terminal growth  : {dcf['terminal_growth']:.2%}")
    print(f"Enterprise value : ${dcf['enterprise_value']:,.0f}m")
    print(f"  less net debt  : ${dcf['net_debt']:,.0f}m")
    print(f"Equity value     : ${dcf['equity_value']:,.0f}m")
    print(f"Value per share  : ${dcf['value_per_share']:,.2f}  "
          f"(market ${meta['price']:,.2f})")

    # ---- 5) WRITE OUTPUT ---------------------------------------------------
    xlsx = os.path.join(OUTPUT_DIR, "three_statement_model.xlsx")
    reporting.write_excel(xlsx, model, scen, sens, dcf, drivers, opening, meta,
                          src_label, bundle["ticker"])
    charts = reporting.write_charts(OUTPUT_DIR, model, scen, bundle["ticker"])

    print("\n--- OUTPUT FILES ---")
    print(f"[out] {xlsx}")
    for c in charts:
        print(f"[out] {c}")
    print("\nDone.")


if __name__ == "__main__":
    main()
