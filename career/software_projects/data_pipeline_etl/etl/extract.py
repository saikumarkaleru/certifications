"""Extract stage: read raw source files into plain Python structures.

The extract layer does NO cleaning. It only reads bytes off disk and returns
raw rows (as dicts). All values arrive as strings from CSV; JSON keeps native
types. Keeping extract "dumb" makes the pipeline easy to reason about and test.

Standard library only: csv, json.
"""
from __future__ import annotations

import csv
import json
import logging
from typing import Dict, List

from etl import config

logger = logging.getLogger("extract")


def extract_customers(path: str = config.CUSTOMERS_CSV) -> List[Dict[str, str]]:
    """Read the customers CSV into a list of raw dict rows."""
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    logger.info("Extracted %d customer rows from %s", len(rows), path)
    return rows


def extract_products(path: str = config.PRODUCTS_JSON) -> List[Dict]:
    """Read the products JSON into a list of raw dict rows."""
    with open(path, encoding="utf-8") as fh:
        rows = json.load(fh)
    logger.info("Extracted %d product rows from %s", len(rows), path)
    return rows


def extract_orders(path: str = config.ORDERS_CSV) -> List[Dict[str, str]]:
    """Read the raw (messy) orders CSV into a list of raw dict rows."""
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    logger.info("Extracted %d raw order rows from %s", len(rows), path)
    return rows


def extract_all() -> Dict[str, List[Dict]]:
    """Convenience: extract every source and return them keyed by name."""
    return {
        "customers": extract_customers(),
        "products": extract_products(),
        "orders": extract_orders(),
    }
