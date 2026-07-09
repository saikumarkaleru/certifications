"""fund_ops: a compact, interview-defensible investment-operations toolkit.

Modules
-------
data           : load the synthetic sample CSVs from input/ (fully offline).
pricing        : value holdings with a stale / missing price policy.
nav            : NAV waterfall (GAV, TER accrual, NAV per unit) + move validation.
reconciliation : generic book-vs-custodian break engine for trades and cash.
kyc            : customer risk scoring (CDD/EDD) + AML transaction monitoring.
reporting      : formatted Excel workbook and matplotlib charts.
"""

from . import data, pricing, nav, reconciliation, kyc, reporting  # noqa: F401

__all__ = ["data", "pricing", "nav", "reconciliation", "kyc", "reporting"]
