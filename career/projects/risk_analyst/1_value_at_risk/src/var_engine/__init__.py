"""var_engine: a compact, interview-defensible Value-at-Risk toolkit.

Modules
-------
data        : download / cache / synthesize daily price data and returns.
var_methods : historical, parametric and Monte Carlo VaR, ES, component/marginal VaR.
backtest    : rolling VaR plus Kupiec POF and Christoffersen independence tests.
reporting   : Excel workbook and matplotlib charts.
"""

from . import data, var_methods, backtest, reporting  # noqa: F401

__all__ = ["data", "var_methods", "backtest", "reporting"]
