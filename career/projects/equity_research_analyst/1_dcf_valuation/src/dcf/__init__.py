"""
dcf -- a small, interview-defensible discounted-cash-flow toolkit.

Modules
-------
data    : pull a real company's financials from yfinance (with caching +
          an offline fallback so the model always runs).
fcff    : derive unlevered free cash flow (FCFF) from the statements.
wacc    : estimate the discount rate via CAPM (cost of equity) + cost of debt.
model   : project FCFF, build terminal values, discount to value/share, and
          run scenarios, a 2-way sensitivity grid and a reverse DCF.
report  : write a formatted Excel workbook and the charts.
"""

from . import data, fcff, wacc, model, report  # noqa: F401

__all__ = ["data", "fcff", "wacc", "model", "report"]
