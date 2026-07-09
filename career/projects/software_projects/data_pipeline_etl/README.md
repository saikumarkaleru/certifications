# E-Commerce Sales ETL Pipeline

A small, **fully runnable** batch ETL pipeline that ingests messy raw e-commerce
data (CSV + JSON), cleans and conforms it into a **star schema**, gates it behind
a **data-quality suite**, and loads it into a **SQLite data warehouse** ready for
analytics SQL.

> **Zero dependencies to run.** The default path uses the Python **standard
> library only** (`sqlite3`, `csv`, `json`, `datetime`, `logging`, `unittest`).
> No `pip install` needed. An optional pandas path is included as a showcase.

---

## Architecture (Extract -> Transform -> Quality -> Load)

```
  data/                         etl/                         warehouse/
  ┌──────────────┐   Extract    ┌───────────┐
  │ customers.csv│ ───────────► │extract.py │
  │ products.json│              └─────┬─────┘
  │orders_raw.csv│  (messy)           │ raw dict rows
  └──────────────┘                    ▼
                                ┌───────────┐   Transform: clean, dedupe,
                                │transform  │   type-cast, backfill price,
                                │  .py      │   derive revenue, conform dims
                                └─────┬─────┘
                                      │ star schema (dim_customer,
                                      │             dim_product, fact_sales)
                                      ▼
                                ┌───────────┐   Quality gate: null / unique /
                                │quality.py │   row-count / referential / range
                                └─────┬─────┘   → PASS/FAIL (blocks bad loads)
                                      │ (only if all checks pass)
                                      ▼
                                ┌───────────┐   Load: (re)create schema +      ┌────────────┐
                                │ load.py   │ ──────────────────────────────►  │ecommerce.db│
                                └───────────┘   idempotent full refresh        └────────────┘
        pipeline.py orchestrates all four stages with logging + a run summary.
```

- **`etl/extract.py`** — reads raw sources into plain dicts (no cleaning).
- **`etl/transform.py`** — pure functions: clean, dedupe on key, type-cast,
  validate dates, backfill missing price from the product dimension, enforce
  referential integrity, derive `revenue = quantity * unit_price`. Rejected rows
  are collected with a reason (auditable, not silently dropped).
- **`etl/quality.py`** — not-null, uniqueness, row-count, referential, and
  value-range checks; each returns pass/fail.
- **`etl/load.py`** — creates the schema and loads the warehouse. **Idempotent**
  full-refresh (drop + recreate) so re-runs never duplicate data.
- **`etl/pipeline.py`** — orchestrates E → T → Q → L, logs each stage, **gates
  the load on the quality suite**, prints a run summary, exits non-zero on
  quality failure (CI-friendly).
- **`etl/config.py`** — paths and business rules in one place.

---

## How to run

```bash
# 1. Run the whole pipeline (populates warehouse/ecommerce.db)
python etl/pipeline.py

# 2. Run the offline test suite
python -m unittest discover -s tests -v

# 3. Query the warehouse with analytics SQL
sqlite3 -header -column warehouse/ecommerce.db < sql/analytics_queries.sql
```

No environment setup required (Python 3.9+). `requirements.txt` lists only
**optional** extras (pandas, Airflow).

---

## Warehouse schema / data dictionary

**`dim_customer`** (one row per customer)

| column       | type | notes                     |
|--------------|------|---------------------------|
| customer_id  | TEXT | primary key               |
| name         | TEXT | customer full name        |
| city         | TEXT | city                      |
| signup_date  | TEXT | ISO `YYYY-MM-DD`          |

**`dim_product`** (one row per product)

| column      | type | notes                      |
|-------------|------|----------------------------|
| product_id  | TEXT | primary key                |
| name        | TEXT | product name               |
| category    | TEXT | product category           |
| unit_price  | REAL | list price                 |

**`fact_sales`** (one row per cleaned order — the grain)

| column      | type    | notes                                   |
|-------------|---------|-----------------------------------------|
| order_id    | TEXT    | primary key                             |
| customer_id | TEXT    | FK → dim_customer                       |
| product_id  | TEXT    | FK → dim_product                        |
| quantity    | INTEGER | positive integer                        |
| unit_price  | REAL    | price at order time (backfilled if null)|
| revenue     | REAL    | derived: `quantity * unit_price`        |
| order_date  | TEXT    | ISO `YYYY-MM-DD`                        |

Indexes on `customer_id`, `product_id`, `order_date` for analytics.

---

## Deliberately messy raw data (what the pipeline cleans)

`data/orders_raw.csv` contains realistic dirt so the transform is meaningful:

- **duplicate order rows** (deduped on `order_id`)
- **null `customer_id` / `product_id`** (rejected — missing key)
- **bad quantity types** (`"two"`, empty) and **non-positive** (`0`, `-3`)
- **invalid date** (`not_a_date`)
- **missing `unit_price`** (backfilled from the product dimension)
- **orphan foreign keys** (`C011`, `P999` not in dimensions → rejected)

Latest run: **32 raw orders → 21 clean fact rows, 11 rejected**, 13/13 quality
checks passed.

---

## Optional extras

- **pandas path** — `etl/transform_pandas.py` mirrors the fact cleaning with a
  vectorized DataFrame implementation, guarded by `try/except` so it is a no-op
  when pandas is not installed.
- **Airflow** — `airflow_dag_example.py` is a documented example DAG showing how
  the same stages would be scheduled/retried/gated in production (concept only,
  not executed here).

---

## Project layout

```
data_pipeline_etl/
├── data/                    # raw sources (CSV + JSON, intentionally messy)
├── etl/                     # extract, transform, quality, load, pipeline, config
├── sql/                     # analytics queries
├── tests/                   # stdlib unittest suite (transform + quality)
├── warehouse/               # SQLite warehouse output (ecommerce.db)
├── airflow_dag_example.py   # example orchestration DAG (concept only)
├── requirements.txt         # OPTIONAL extras only
├── README.md
└── STUDY_GUIDE.md           # ETL concepts + interview Q&A
```
