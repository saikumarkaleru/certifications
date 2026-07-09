"""Transform stage: clean, dedupe, type-cast, derive, and conform the raw data.

This is the heart of the pipeline. Every function here is pure (no I/O), which
makes the logic trivially unit-testable offline. The transform produces a
star-schema-shaped result:

    dim_customer  <- customers.csv
    dim_product   <- products.json
    fact_sales    <- orders_raw.csv (cleaned + enriched with product price)

Rows that cannot be salvaged (bad types, missing keys, orphan references) are
NOT silently dropped: they are collected in a `rejects` list with a reason so
the run is auditable.

Standard library only: datetime.
"""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from etl import config

logger = logging.getLogger("transform")


# --------------------------------------------------------------------------- #
# Small, individually testable helpers
# --------------------------------------------------------------------------- #
def clean_str(value: Optional[str]) -> Optional[str]:
    """Strip whitespace; convert empty / None to None."""
    if value is None:
        return None
    value = value.strip()
    return value or None


def parse_int(value: Optional[str]) -> Optional[int]:
    """Parse a positive-or-any integer from a possibly messy string.

    Returns None if the value is missing or not a clean integer (e.g. 'two',
    '3.5', ''). Sign is preserved so callers can enforce positivity.
    """
    value = clean_str(value)
    if value is None:
        return None
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def parse_float(value) -> Optional[float]:
    """Parse a float from a messy string/number; None if not parseable."""
    if isinstance(value, (int, float)):
        return float(value)
    value = clean_str(value)
    if value is None:
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def parse_date(value: Optional[str], fmt: str = config.DATE_FORMAT) -> Optional[str]:
    """Validate a date string against `fmt`; return ISO date or None."""
    value = clean_str(value)
    if value is None:
        return None
    try:
        return datetime.strptime(value, fmt).strftime(config.DATE_FORMAT)
    except (ValueError, TypeError):
        return None


# --------------------------------------------------------------------------- #
# Dimension transforms
# --------------------------------------------------------------------------- #
def transform_customers(raw: List[Dict]) -> List[Dict]:
    """Clean customer rows into dim_customer records (dedupe on customer_id)."""
    seen = set()
    out: List[Dict] = []
    for r in raw:
        cid = clean_str(r.get("customer_id"))
        if cid is None or cid in seen:
            continue
        seen.add(cid)
        out.append(
            {
                "customer_id": cid,
                "name": clean_str(r.get("name")),
                "city": clean_str(r.get("city")),
                "signup_date": parse_date(r.get("signup_date")),
            }
        )
    logger.info("Transformed %d -> %d customer dim rows", len(raw), len(out))
    return out


def transform_products(raw: List[Dict]) -> List[Dict]:
    """Clean product rows into dim_product records (dedupe on product_id)."""
    seen = set()
    out: List[Dict] = []
    for r in raw:
        pid = clean_str(r.get("product_id"))
        if pid is None or pid in seen:
            continue
        seen.add(pid)
        out.append(
            {
                "product_id": pid,
                "name": clean_str(r.get("name")),
                "category": clean_str(r.get("category")),
                "unit_price": parse_float(r.get("unit_price")),
            }
        )
    logger.info("Transformed %d -> %d product dim rows", len(raw), len(out))
    return out


# --------------------------------------------------------------------------- #
# Fact transform (the messy one)
# --------------------------------------------------------------------------- #
def transform_orders(
    raw: List[Dict],
    customers: List[Dict],
    products: List[Dict],
) -> Tuple[List[Dict], List[Dict]]:
    """Clean orders into fact_sales rows.

    Cleaning rules applied (in order):
      1. Dedupe on order_id (keep first occurrence).
      2. Reject rows with a missing customer_id or product_id.
      3. Reject rows whose quantity is not a positive integer.
      4. Reject rows with an invalid order_date.
      5. Backfill a missing unit_price from the product dimension.
      6. Reject rows whose keys do not exist in the dimensions (referential).
      7. Derive revenue = quantity * unit_price.

    Returns (fact_rows, reject_rows). Each reject carries a `reason`.
    """
    customer_ids = {c["customer_id"] for c in customers}
    price_by_product = {p["product_id"]: p["unit_price"] for p in products}

    facts: List[Dict] = []
    rejects: List[Dict] = []
    seen_orders = set()

    for r in raw:
        oid = clean_str(r.get("order_id"))
        row_ref = dict(r)

        if oid is None:
            rejects.append({**row_ref, "reason": "missing order_id"})
            continue
        if oid in seen_orders:
            rejects.append({**row_ref, "reason": "duplicate order_id"})
            continue
        seen_orders.add(oid)

        cid = clean_str(r.get("customer_id"))
        pid = clean_str(r.get("product_id"))
        if cid is None:
            rejects.append({**row_ref, "reason": "missing customer_id"})
            continue
        if pid is None:
            rejects.append({**row_ref, "reason": "missing product_id"})
            continue

        qty = parse_int(r.get("quantity"))
        if qty is None:
            rejects.append({**row_ref, "reason": "non-integer quantity"})
            continue
        if qty < config.MIN_QUANTITY:
            rejects.append({**row_ref, "reason": "quantity below minimum"})
            continue

        order_date = parse_date(r.get("order_date"))
        if order_date is None:
            rejects.append({**row_ref, "reason": "invalid order_date"})
            continue

        # Backfill price from the product dimension when missing/unparseable.
        unit_price = parse_float(r.get("unit_price"))
        if unit_price is None:
            unit_price = price_by_product.get(pid)

        # Referential integrity against the conformed dimensions.
        if cid not in customer_ids:
            rejects.append({**row_ref, "reason": "orphan customer_id"})
            continue
        if pid not in price_by_product:
            rejects.append({**row_ref, "reason": "orphan product_id"})
            continue
        if unit_price is None:
            rejects.append({**row_ref, "reason": "unresolved unit_price"})
            continue

        facts.append(
            {
                "order_id": oid,
                "customer_id": cid,
                "product_id": pid,
                "quantity": qty,
                "unit_price": round(float(unit_price), 2),
                "revenue": round(qty * float(unit_price), 2),
                "order_date": order_date,
            }
        )

    logger.info(
        "Transformed %d raw orders -> %d fact rows (%d rejected)",
        len(raw),
        len(facts),
        len(rejects),
    )
    return facts, rejects


def transform_all(sources: Dict[str, List[Dict]]) -> Dict[str, List[Dict]]:
    """Run every transform and return the star-schema-shaped result."""
    customers = transform_customers(sources["customers"])
    products = transform_products(sources["products"])
    facts, rejects = transform_orders(sources["orders"], customers, products)
    return {
        "dim_customer": customers,
        "dim_product": products,
        "fact_sales": facts,
        "rejects": rejects,
    }
