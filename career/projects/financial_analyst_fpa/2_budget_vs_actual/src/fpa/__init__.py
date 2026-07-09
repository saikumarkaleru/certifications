"""
fpa - a small FP&A (Financial Planning & Analysis) package.

This package builds a driver-based annual budget, simulates actual results,
computes variances (with favorable/unfavorable flags), decomposes the revenue
variance into Price / Volume / Mix, builds a flex (flexible) budget, produces a
rolling reforecast, writes plain-English commentary, and reports to Excel + PNG.

Company modelled: "Meridian Instruments Co." - a made-up industrial-hardware
firm selling four product lines through four cost centres. All numbers are
synthetic and generated with a fixed random seed so every run is identical.

Modules
-------
budget      : driver-based annual budget build (volume x price, unit-cost COGS,
              cost-centre opex with seasonality).
actuals     : seeded simulation of actual results (with drift vs budget) plus
              CSV caching so runs are reproducible offline.
variance    : variances, favorable/unfavorable flags, Price/Volume/Mix
              decomposition, and flex-budget (activity vs rate) splits.
reforecast  : rolling reforecast of the remaining months from YTD actual trends.
commentary  : auto-generated English commentary and the CFO KPI summary.
reporting   : Excel workbook + matplotlib charts (waterfall, bars, trend).
"""

from . import budget, actuals, variance, reforecast, commentary, reporting

__all__ = [
    "budget",
    "actuals",
    "variance",
    "reforecast",
    "commentary",
    "reporting",
]
