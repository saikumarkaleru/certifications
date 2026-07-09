"""Net Asset Value computation and day-over-day NAV validation.

NAV waterfall
-------------
  Gross Asset Value (GAV) = market value of holdings + cash + accrued income
  Management fee accrued  = GAV * TER_annual * (accrual_days / 365)
  Total liabilities       = management fee accrued + other accrued expenses
  NAV                     = GAV - Total liabilities
  NAV per unit            = NAV / units outstanding

The management fee (a component of the Total Expense Ratio, TER) accrues daily
on the fund's assets, so it is modelled as a pro-rata slice of the annual rate.
A large day-over-day move in NAV per unit is flagged for a four-eyes check.
"""

from __future__ import annotations

from dataclasses import dataclass

LARGE_MOVE_THRESHOLD = 0.02  # 2% day-over-day move triggers a review flag


@dataclass
class NavResult:
    holdings_mv: float
    cash: float
    accrued_income: float
    gross_asset_value: float
    management_fee_accrued: float
    other_accrued_expenses: float
    total_liabilities: float
    nav: float
    units_outstanding: float
    nav_per_unit: float
    prior_nav_per_unit: float
    nav_move_pct: float
    move_flagged: bool

    def composition(self) -> dict:
        """Signed components that bridge from GAV to NAV (for the chart)."""
        return {
            "Holdings MV": self.holdings_mv,
            "Cash": self.cash,
            "Accrued Income": self.accrued_income,
            "Mgmt Fee (TER)": -self.management_fee_accrued,
            "Other Expenses": -self.other_accrued_expenses,
        }


def compute_nav(holdings_mv: float, fund: dict) -> NavResult:
    """Build the full NAV waterfall from priced holdings + fund static data."""
    cash = fund["cash_balance"]
    accrued_income = fund["accrued_income"]
    gav = holdings_mv + cash + accrued_income

    mgmt_fee = gav * fund["ter_annual"] * (fund["fee_accrual_days"] / 365.0)
    other_exp = fund["other_accrued_expenses"]
    liabilities = mgmt_fee + other_exp

    nav = gav - liabilities
    units = fund["units_outstanding"]
    nav_per_unit = nav / units if units else 0.0

    prior = fund["prior_nav_per_unit"]
    move = (nav_per_unit - prior) / prior if prior else 0.0

    return NavResult(
        holdings_mv=holdings_mv,
        cash=cash,
        accrued_income=accrued_income,
        gross_asset_value=gav,
        management_fee_accrued=mgmt_fee,
        other_accrued_expenses=other_exp,
        total_liabilities=liabilities,
        nav=nav,
        units_outstanding=units,
        nav_per_unit=nav_per_unit,
        prior_nav_per_unit=prior,
        nav_move_pct=move,
        move_flagged=abs(move) >= LARGE_MOVE_THRESHOLD,
    )
