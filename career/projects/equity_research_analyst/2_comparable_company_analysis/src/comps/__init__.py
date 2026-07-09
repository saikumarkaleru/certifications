"""
comps -- a small, interview-defensible comparable-company-analysis toolkit.

Modules
-------
data       : pull a target + peers from yfinance (caching + offline fallback).
multiples  : compute trading multiples (P/E, EV/EBITDA, EV/Revenue, P/B, PEG).
stats      : peer central tendency (median/mean/quartiles) + a cross-sectional
             z-score screen and an OLS regression to flag rich/cheap names.
valuation  : apply peer multiples to the target for an implied value range.
report     : write a formatted Excel workbook and the football-field chart.
"""

from . import data, multiples, stats, valuation, report  # noqa: F401

__all__ = ["data", "multiples", "stats", "valuation", "report"]
