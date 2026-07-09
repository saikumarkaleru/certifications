"""Position pricing with an explicit stale / missing price policy.

Fund accountants cannot strike a NAV on a price they do not trust, so every
position must resolve to a price *and* carry the provenance of that price.

Price-source policy (documented and testable)
---------------------------------------------
1. GOOD    : a price dated on the valuation date is used as-is.
2. STALE   : the latest available price is older than ``STALE_PRICE_DAYS``.
             It is still used (last-known-good) but flagged for review, because
             a stale mark can distort the NAV.
3. FALLBACK: no price at all in today's file -> fall back to the prior-day
             price file (a common "carry forward last close" rule) and flag it.
4. MISSING : not present anywhere -> value at 0 and raise a hard flag. A real
             desk would suspend the NAV; here we surface it as an exception.
"""

from __future__ import annotations

import pandas as pd

from .data import STALE_PRICE_DAYS


def _resolve_price(sec_id, price_map, price_date_map, prior_map, valuation_date):
    """Return (price, source, price_date, age_days) for one security."""
    if sec_id in price_map:
        price = price_map[sec_id]
        pdate = price_date_map[sec_id]
        age = (valuation_date - pdate).days
        source = "STALE" if age > STALE_PRICE_DAYS else "GOOD"
        return price, source, pdate, age
    if sec_id in prior_map:
        # No price today -> carry forward the prior-day close.
        return prior_map[sec_id], "FALLBACK_PRIOR", None, None
    return 0.0, "MISSING", None, None


def price_positions(positions, prices, prior_prices, valuation_date) -> pd.DataFrame:
    """Value every holding, returning a per-position valuation table.

    Columns: security_id, ticker, asset_class, quantity, price, price_source,
             price_date, price_age_days, market_value, price_flag.
    """
    price_map = dict(zip(prices["security_id"], prices["price"]))
    price_date_map = dict(zip(prices["security_id"], prices["price_date"]))
    prior_map = dict(zip(prior_prices["security_id"], prior_prices["price"]))

    rows = []
    for _, pos in positions.iterrows():
        sec = pos["security_id"]
        price, source, pdate, age = _resolve_price(
            sec, price_map, price_date_map, prior_map, valuation_date
        )
        mv = pos["quantity"] * price
        rows.append(
            {
                "security_id": sec,
                "ticker": pos["ticker"],
                "asset_class": pos["asset_class"],
                "quantity": pos["quantity"],
                "price": price,
                "price_source": source,
                "price_date": pdate,
                "price_age_days": age,
                "market_value": mv,
                "price_flag": source not in ("GOOD",),
            }
        )
    return pd.DataFrame(rows)


def pricing_exceptions(valuation: pd.DataFrame) -> pd.DataFrame:
    """Rows that needed policy intervention (stale / fallback / missing)."""
    return valuation[valuation["price_flag"]].copy()


def total_market_value(valuation: pd.DataFrame) -> float:
    return float(valuation["market_value"].sum())
