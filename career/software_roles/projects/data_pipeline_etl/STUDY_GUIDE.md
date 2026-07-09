# Data Engineering Study Guide — ETL Concepts & Interview Q&A

A companion to this project. It explains the concepts the pipeline demonstrates
and gives 20 interview-style Q&A a fresher Data Engineer should be able to
answer. Each answer references how *this* project implements the idea.

---

## Core concepts

### ETL vs ELT
- **ETL (Extract → Transform → Load)**: transform data *before* loading it into
  the warehouse. Good when the target is a structured relational warehouse and
  you want only clean, conformed data landing in it. **This project is ETL** —
  cleaning happens in `transform.py` before `load.py` writes SQLite.
- **ELT (Extract → Load → Transform)**: load raw data first (into a lake or a
  columnar warehouse like BigQuery/Snowflake), then transform *in-warehouse*
  with SQL (often via dbt). Wins when storage is cheap and compute is elastic;
  keeps raw data for replay.

### Idempotency
Running the pipeline twice produces the same warehouse state — no duplicates, no
drift. This project uses an **idempotent full refresh**: `load.py` drops and
recreates tables each run. For large tables you'd instead **upsert/merge** keyed
on the primary key, or partition by date and overwrite only the affected
partition. Idempotency is what makes retries and backfills safe.

### Data quality
Bad data is worse than no data. `quality.py` runs **not-null, uniqueness,
row-count, referential-integrity, and value-range** checks and returns pass/fail.
`pipeline.py` **gates the load**: if any check fails, nothing is loaded and the
process exits non-zero (so an orchestrator/CI marks the run failed and alerts).

### Star schema (dimensional modeling)
A central **fact** table (measurable events — here `fact_sales`, grain = one
order line) surrounded by **dimension** tables (descriptive context —
`dim_customer`, `dim_product`). Facts hold foreign keys + numeric measures
(`quantity`, `revenue`); dimensions hold attributes you filter/group by
(city, category). Denormalized for fast, simple analytical joins.

### Orchestration
Local run = `python etl/pipeline.py`. In production an orchestrator (Airflow,
Dagster, Prefect) handles **scheduling, retries, dependencies, alerting, and
observability**. `airflow_dag_example.py` shows the same E→T→Q→L wired as tasks
with the load gated behind the quality task.

### Grain
The level of detail of one fact row. Defining the grain first ("one row per
order") prevents double-counting and drives every other modeling decision.

### Slowly Changing Dimensions (SCD)
How dimension changes are handled over time. **Type 1** overwrites (no history);
**Type 2** adds a new row with validity dates (keeps history). This project uses
Type-1-style dimension refreshes.

---

## Interview Q&A (20)

**1. What is ETL and what are the stages?**
Extract (pull from sources), Transform (clean/standardize/aggregate), Load
(write to the target warehouse). Here: `extract.py` → `transform.py` → `load.py`,
with a quality gate in between.

**2. ETL vs ELT — when would you pick each?**
ETL when the target needs only clean structured data and transforms are cheaper
outside the warehouse. ELT when using a scalable cloud warehouse/lake, want to
keep raw data, and transform with in-warehouse SQL (e.g., dbt).

**3. What is idempotency and why does it matter in pipelines?**
Re-running yields the same result with no side effects. It makes retries and
backfills safe. Implemented here via full drop-and-reload; alternatives are
upserts or partition overwrites.

**4. How do you prevent duplicate data on re-runs?**
Idempotent load: primary keys + `INSERT OR REPLACE`/upsert, or truncate-and-load,
or partition overwrite. This project dedupes on `order_id` in transform and
recreates tables in load.

**5. What data-quality checks do you run?**
Not-null on required columns, uniqueness of keys, row-count/volume checks,
referential integrity (FK resolves to a dimension), and value ranges (e.g.,
quantity > 0). See `quality.py`.

**6. What is referential integrity and how do you enforce it?**
Every foreign key must reference an existing dimension row. Enforced in transform
(orphan rows rejected) and asserted again in the quality suite; the schema also
declares `FOREIGN KEY` constraints.

**7. Explain the star schema and why it's used for analytics.**
Central fact + surrounding dimensions. Denormalized for simple joins and fast
aggregations, and intuitive for BI tools. Contrast with the more normalized
snowflake schema.

**8. Fact vs dimension table?**
Facts store measurable events with numeric measures and FKs (`fact_sales`).
Dimensions store descriptive attributes used to slice/filter (`dim_product`).

**9. What is "grain"?**
The meaning of one fact row. Here the grain is one order. Defining it first
avoids double counting.

**10. What are Slowly Changing Dimensions?**
Strategies for evolving dimension attributes: Type 1 (overwrite), Type 2 (new
versioned row with effective dates), Type 3 (previous-value column).

**11. Batch vs streaming ETL?**
Batch processes bounded chunks on a schedule (this project). Streaming processes
unbounded events in near-real-time (Kafka, Spark Structured Streaming, Flink).

**12. How do you handle a pipeline failure mid-run?**
Make stages idempotent and retryable, use transactions, checkpoint/watermark,
alert on failure, and design so a rerun is safe. The load runs in a transaction
and only commits after all inserts.

**13. Why gate the load on data quality?**
To keep bad data out of the warehouse ("fail fast"). Downstream dashboards and
models trust the warehouse, so a bad load has wide blast radius. `pipeline.py`
skips the load and exits non-zero if any check fails.

**14. What is a data warehouse vs a data lake?**
Warehouse: structured, schema-on-write, optimized for SQL analytics (SQLite here
stands in for BigQuery/Snowflake/Redshift). Lake: raw/semi-structured files,
schema-on-read (S3/HDFS), cheaper and more flexible.

**15. What does an orchestrator like Airflow give you?**
Scheduling, dependency management (DAGs), retries with backoff, alerting, logging
/observability, backfills, and SLAs. See `airflow_dag_example.py`.

**16. How do you make transforms testable?**
Keep them as **pure functions** (no I/O) so they can be unit-tested offline —
that's why `transform.py`/`quality.py` take and return plain data. See `tests/`.

**17. How do you deal with schema changes at the source?**
Validate/contract-check on extract, version schemas, use nullable defaults,
alert on unexpected columns, and evolve the target schema deliberately (migrations).

**18. What is a surrogate key vs a natural key?**
Natural key comes from the business data (`order_id`). Surrogate key is a
pipeline-generated ID (e.g., autoincrement) that is stable even if natural keys
change; common for SCD Type 2.

**19. How would you scale this beyond SQLite?**
Swap the load target for a columnar/cloud warehouse, process with Spark/DuckDB
for large volumes, partition by date, orchestrate with Airflow, and add
incremental/CDC loads instead of full refresh.

**20. What is CDC (Change Data Capture)?**
Capturing only inserts/updates/deletes from a source (via logs or timestamps) so
you load *deltas* instead of full snapshots — efficient incremental ETL.

---

## What this project demonstrates on a resume
- End-to-end ETL with a **quality gate** and **run summary/observability**.
- **Dimensional modeling** (star schema) into a SQL warehouse.
- **Idempotent** design and **auditable rejects**.
- **Testable, pure-function** transforms with an offline unit-test suite.
- Awareness of **orchestration** (Airflow) and an **optional pandas** path.
