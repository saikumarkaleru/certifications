"""Central configuration for the e-commerce ETL pipeline.

All paths are resolved relative to the project root so the pipeline runs the
same way regardless of the current working directory. Standard library only.
"""
from __future__ import annotations

import os

# Project root = parent of this etl/ package directory.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
SQL_DIR = os.path.join(PROJECT_ROOT, "sql")
WAREHOUSE_DIR = os.path.join(PROJECT_ROOT, "warehouse")

# Raw source files (Extract).
CUSTOMERS_CSV = os.path.join(DATA_DIR, "customers.csv")
PRODUCTS_JSON = os.path.join(DATA_DIR, "products.json")
ORDERS_CSV = os.path.join(DATA_DIR, "orders_raw.csv")

# Target SQLite warehouse (Load).
WAREHOUSE_DB = os.path.join(WAREHOUSE_DIR, "ecommerce.db")

# Business rules used during Transform.
MIN_QUANTITY = 1          # quantity must be a positive integer
DATE_FORMAT = "%Y-%m-%d"  # expected order_date format

# Logging.
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s | %(levelname)-7s | %(name)-10s | %(message)s"
