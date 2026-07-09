"""
model — a small, readable three-statement modelling package.

Modules (read them in this order):
  data.py       -> pull real financials (yfinance), cache them, derive drivers.
  forecast.py   -> the linked 3-statement engine + debt/revolver cash sweep.
  scenarios.py  -> bull/base/bear cases + a 2-way DCF sensitivity table.
  valuation.py  -> discounted-cash-flow (DCF) valuation off the model's FCFF.
  reporting.py  -> write the Excel workbook and the PNG charts.

Everything is deliberately plain-English so it can be defended line by line.
"""

from . import data, forecast, scenarios, valuation, reporting  # noqa: F401

__all__ = ["data", "forecast", "scenarios", "valuation", "reporting"]
