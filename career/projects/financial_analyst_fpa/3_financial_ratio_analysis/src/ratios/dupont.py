"""
dupont.py -- why is ROE what it is?
===================================

Return on Equity (Net Income / Equity) is the single number shareholders care
about most, but on its own it hides WHAT is driving it. The DuPont method
factorises ROE into a product of drivers, each of which is a lever management
can pull. Two standard versions:

  3-STEP:  ROE = Net Margin x Asset Turnover x Equity Multiplier
                 (profit per $ sales) (sales per $ assets) (assets per $ equity)
           i.e.  is the ROE coming from being PROFITABLE, EFFICIENT, or LEVERED?

  5-STEP:  ROE = Tax Burden x Interest Burden x Operating Margin
                       x Asset Turnover x Equity Multiplier
           This splits "Net Margin" further into how much profit taxes and
           interest eat, versus the pure OPERATING margin -- so you can tell a
           genuinely profitable firm from one that just has a low tax bill.

The algebra is deliberately a telescoping product: every intermediate term
cancels, leaving exactly Net Income / Equity. That is the whole point, and it
is what our unit tests check -- the product of the drivers MUST equal the ROE
computed directly, to within rounding.

To make that identity hold EXACTLY, this module uses year-end balances
consistently for every term (no average-balance mixing). ratios.py may report a
slightly different ROE because it uses average equity -- that is fine; they are
answering slightly different questions. DuPont's job is the clean decomposition.
"""

from __future__ import annotations

import pandas as pd


def _v(facts, field, year):
    return facts.at[field, year] if field in facts.index else float("nan")


def dupont_3step(facts, year):
    """Return a dict of the 3-step drivers plus the reconciliation.

    Keys: net_margin, asset_turnover, equity_multiplier,
          roe_product (their product), roe_direct (Net Income / Equity),
          diff (product - direct; should be ~0).
    """
    ni = _v(facts, "Net Income", year)
    rev = _v(facts, "Revenue", year)
    assets = _v(facts, "Total Assets", year)
    equity = _v(facts, "Equity", year)

    net_margin = ni / rev                 # profit squeezed from each sales $
    asset_turnover = rev / assets         # sales generated per $ of assets
    equity_multiplier = assets / equity   # leverage: $ assets per $ equity

    product = net_margin * asset_turnover * equity_multiplier
    direct = ni / equity
    return {
        "Net Margin": net_margin,
        "Asset Turnover": asset_turnover,
        "Equity Multiplier": equity_multiplier,
        "ROE (product)": product,
        "ROE (direct)": direct,
        "Reconciliation diff": product - direct,
    }


def dupont_5step(facts, year):
    """Return a dict of the 5-step drivers plus the reconciliation.

    Tax Burden      = Net Income / Pretax Income   (fraction kept after tax)
    Interest Burden = Pretax Income / EBIT         (fraction kept after interest)
    Operating Margin= EBIT / Revenue               (pure operating profitability)
    Asset Turnover  = Revenue / Assets
    Equity Multiplier = Assets / Equity
    """
    ni = _v(facts, "Net Income", year)
    pretax = _v(facts, "Pretax Income", year)
    ebit = _v(facts, "EBIT", year)
    rev = _v(facts, "Revenue", year)
    assets = _v(facts, "Total Assets", year)
    equity = _v(facts, "Equity", year)

    tax_burden = ni / pretax
    interest_burden = pretax / ebit
    operating_margin = ebit / rev
    asset_turnover = rev / assets
    equity_multiplier = assets / equity

    product = (tax_burden * interest_burden * operating_margin
               * asset_turnover * equity_multiplier)
    direct = ni / equity
    return {
        "Tax Burden": tax_burden,
        "Interest Burden": interest_burden,
        "Operating Margin": operating_margin,
        "Asset Turnover": asset_turnover,
        "Equity Multiplier": equity_multiplier,
        "ROE (product)": product,
        "ROE (direct)": direct,
        "Reconciliation diff": product - direct,
    }


def dupont_table(facts, year):
    """Tidy both decompositions into one DataFrame for the Excel/console report.

    Rows are the drivers; a 'Method' column tags each as 3-step or 5-step.
    """
    three = dupont_3step(facts, year)
    five = dupont_5step(facts, year)
    rows = []
    for k, val in three.items():
        rows.append({"Method": "3-step", "Component": k, "Value": val})
    for k, val in five.items():
        rows.append({"Method": "5-step", "Component": k, "Value": val})
    return pd.DataFrame(rows).round(4)
