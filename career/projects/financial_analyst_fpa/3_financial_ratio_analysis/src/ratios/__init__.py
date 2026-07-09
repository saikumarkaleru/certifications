"""
ratios package
==============
A small, teaching-style toolkit for classic financial-statement analysis.

Modules (read them in this order):
  data.py       -> pull statements from yfinance, cache to input/, offline fallback
  ratios.py     -> compute the four ratio families over several years
  dupont.py     -> break ROE into its 3-step and 5-step drivers
  benchmark.py  -> percentile-rank the target company against its peers
  quality.py    -> trend flags + a simple earnings-quality red-flag panel
  reporting.py  -> write the Excel workbook and PNG charts

Everything here is plain division of accounting numbers. There is no exotic
math; if you can read an income statement you can defend every line.
"""

from . import data, ratios, dupont, benchmark, quality, reporting  # noqa: F401

__all__ = ["data", "ratios", "dupont", "benchmark", "quality", "reporting"]
