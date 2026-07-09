"""
credit_spread package
======================
A small, teaching-style corporate / NBFC credit-analysis toolkit. It takes a
few years of borrower financials and produces the same read a junior credit
analyst would hand to a committee: a standardised spread, the classic ratio
families, a cash-flow-based debt-serviceability view, a transparent internal
rating scorecard, and a stress-scenario table.

Modules (read them in this order):
  data.py           -> load + clean 3 years of financials, standardise a spread
  ratios.py         -> leverage, coverage, liquidity, profitability, WC cycle
  serviceability.py -> CFADS, DSCR, ICR vs a debt schedule, headroom class
  rating.py         -> weighted scorecard -> internal rating band + rationale
  scenario.py       -> stress EBITDA / rates / revenue, recompute rating
  reporting.py      -> write the Excel workbook and PNG charts

Everything here is plain arithmetic on accounting numbers. There is no exotic
math; if you can read a balance sheet you can defend every line.
"""

from . import data, ratios, serviceability, rating, scenario, reporting  # noqa: F401

__all__ = ["data", "ratios", "serviceability", "rating", "scenario", "reporting"]
