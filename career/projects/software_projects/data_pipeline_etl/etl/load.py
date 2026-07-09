"""Load stage: create the SQLite warehouse schema and load the star schema.

Design notes:
  * The load is IDEMPOTENT. Re-running the pipeline drops and recreates tables
    (a small-warehouse full-refresh pattern) so you always get the same result
    and never accumulate duplicates. For large tables you'd switch to an
    upsert/merge; the trade-off is discussed in STUDY_GUIDE.md.
  * Uses parameterized executemany() -- no string interpolation of data, so
    it is injection-safe and fast.

Standard library only: sqlite3, os.
"""
from __future__ import annotations

import logging
import os
import sqlite3
from typing import Dict, List

from etl import config

logger = logging.getLogger("load")


SCHEMA = """
DROP TABLE IF EXISTS fact_sales;
DROP TABLE IF EXISTS dim_customer;
DROP TABLE IF EXISTS dim_product;

CREATE TABLE dim_customer (
    customer_id  TEXT PRIMARY KEY,
    name         TEXT,
    city         TEXT,
    signup_date  TEXT
);

CREATE TABLE dim_product (
    product_id   TEXT PRIMARY KEY,
    name         TEXT,
    category     TEXT,
    unit_price   REAL
);

CREATE TABLE fact_sales (
    order_id     TEXT PRIMARY KEY,
    customer_id  TEXT NOT NULL,
    product_id   TEXT NOT NULL,
    quantity     INTEGER NOT NULL,
    unit_price   REAL NOT NULL,
    revenue      REAL NOT NULL,
    order_date   TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES dim_customer (customer_id),
    FOREIGN KEY (product_id)  REFERENCES dim_product (product_id)
);

CREATE INDEX idx_fact_customer ON fact_sales (customer_id);
CREATE INDEX idx_fact_product  ON fact_sales (product_id);
CREATE INDEX idx_fact_date     ON fact_sales (order_date);
"""


def get_connection(db_path: str = config.WAREHOUSE_DB) -> sqlite3.Connection:
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    conn.commit()
    logger.info("Warehouse schema (re)created")


def _insert(conn, table: str, columns: List[str], rows: List[Dict]) -> int:
    if not rows:
        return 0
    placeholders = ", ".join("?" for _ in columns)
    sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
    conn.executemany(sql, [tuple(r.get(c) for c in columns) for r in rows])
    return len(rows)


def load_warehouse(
    data: Dict[str, List[Dict]], db_path: str = config.WAREHOUSE_DB
) -> Dict[str, int]:
    """Create schema and load all tables. Returns rows loaded per table."""
    conn = get_connection(db_path)
    try:
        create_schema(conn)
        counts = {
            "dim_customer": _insert(
                conn,
                "dim_customer",
                ["customer_id", "name", "city", "signup_date"],
                data["dim_customer"],
            ),
            "dim_product": _insert(
                conn,
                "dim_product",
                ["product_id", "name", "category", "unit_price"],
                data["dim_product"],
            ),
            "fact_sales": _insert(
                conn,
                "fact_sales",
                [
                    "order_id",
                    "customer_id",
                    "product_id",
                    "quantity",
                    "unit_price",
                    "revenue",
                    "order_date",
                ],
                data["fact_sales"],
            ),
        }
        conn.commit()
        logger.info("Loaded warehouse: %s", counts)
        return counts
    finally:
        conn.close()
