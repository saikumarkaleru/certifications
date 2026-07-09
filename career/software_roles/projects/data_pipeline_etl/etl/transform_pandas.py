"""OPTIONAL pandas showcase path (never required by the core pipeline).

The default runnable pipeline is 100% standard library. This module demonstrates
the same fact-table cleaning expressed with pandas, guarded so that importing it
without pandas installed degrades gracefully instead of crashing.

Usage:
    from etl.transform_pandas import PANDAS_AVAILABLE, transform_orders_pandas
    if PANDAS_AVAILABLE:
        df = transform_orders_pandas(raw_orders, customers, products)
"""
from __future__ import annotations

from typing import Dict, List

try:
    import pandas as pd  # type: ignore

    PANDAS_AVAILABLE = True
except ImportError:  # pandas is an optional extra
    pd = None
    PANDAS_AVAILABLE = False


def transform_orders_pandas(
    raw_orders: List[Dict], customers: List[Dict], products: List[Dict]
):
    """Vectorized version of transform.transform_orders using pandas.

    Returns a cleaned pandas DataFrame of fact rows. Raises RuntimeError if
    pandas is not installed (call PANDAS_AVAILABLE first).
    """
    if not PANDAS_AVAILABLE:
        raise RuntimeError("pandas is not installed; use etl.transform instead.")

    df = pd.DataFrame(raw_orders)
    prices = {p["product_id"]: p["unit_price"] for p in products}
    customer_ids = {c["customer_id"] for c in customers}

    # Normalize / type-cast.
    for col in ("order_id", "customer_id", "product_id"):
        df[col] = df[col].astype(str).str.strip().replace({"": None})
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["order_date"] = pd.to_datetime(
        df["order_date"], format="%Y-%m-%d", errors="coerce"
    )
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["unit_price"] = df["unit_price"].fillna(df["product_id"].map(prices))

    # Dedupe + filter.
    df = df.drop_duplicates(subset=["order_id"], keep="first")
    df = df.dropna(subset=["order_id", "customer_id", "product_id",
                           "quantity", "order_date", "unit_price"])
    df = df[df["quantity"] >= 1]
    df = df[df["customer_id"].isin(customer_ids)]
    df = df[df["product_id"].isin(prices.keys())]

    # Derive.
    df["quantity"] = df["quantity"].astype(int)
    df["revenue"] = (df["quantity"] * df["unit_price"]).round(2)
    df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")
    return df.reset_index(drop=True)
