"""Credit risk scoring package.

Modules
-------
data       : fetch/cache real company financials + market data (yfinance).
altman     : Altman Z-score (accounting model of bankruptcy risk).
merton     : Merton structural model (market-implied probability of default).
portfolio  : rank issuers and compute portfolio expected loss.
reporting  : Excel workbook + matplotlib charts.

The whole package is deliberately kept small and textbook-standard so every
line is defensible in an interview: two classic credit models (one accounting,
one structural) applied to a real large-cap universe.
"""

__all__ = ["data", "altman", "merton", "portfolio", "reporting"]
