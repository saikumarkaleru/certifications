"""EXAMPLE Apache Airflow DAG for the e-commerce ETL pipeline.

*** This file is a documented CONCEPT reference — it is NOT executed by this
project and Airflow is NOT a dependency. *** It shows how the same E -> T -> Q
-> L stages you can run locally with `python etl/pipeline.py` would be
scheduled and orchestrated in production.

Why Airflow (or any orchestrator)?
  * Scheduling      : run daily at 02:00, backfill history, respect timezones.
  * Dependencies    : Load only runs if Quality passed; retries on transient
                      failures; alerting on hard failures.
  * Observability   : per-task logs, run history, SLA misses, lineage.
  * Idempotency     : each run keyed by logical date so re-runs are safe.

To actually run this you would:  pip install apache-airflow, drop this file in
your $AIRFLOW_HOME/dags/, and `airflow dags trigger ecommerce_etl`.
"""
from __future__ import annotations

from datetime import datetime, timedelta

# NOTE: these imports only resolve in an environment where Airflow is installed.
try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator

    from etl import extract, load, quality, transform

    default_args = {
        "owner": "data-engineering",
        "depends_on_past": False,
        "retries": 2,
        "retry_delay": timedelta(minutes=5),
        "email_on_failure": True,
    }

    # --- Task callables: thin wrappers around the reusable etl/ functions --- #
    def _extract(**ctx):
        sources = extract.extract_all()
        ctx["ti"].xcom_push(key="sources", value=sources)

    def _transform(**ctx):
        sources = ctx["ti"].xcom_pull(key="sources", task_ids="extract")
        transformed = transform.transform_all(sources)
        ctx["ti"].xcom_push(key="transformed", value=transformed)

    def _quality(**ctx):
        transformed = ctx["ti"].xcom_pull(key="transformed", task_ids="transform")
        results = quality.run_quality_checks(transformed)
        if not quality.all_passed(results):
            # Raising fails the task -> downstream Load is skipped, alert fires.
            raise ValueError("Data quality gate failed; aborting load.")

    def _load(**ctx):
        transformed = ctx["ti"].xcom_pull(key="transformed", task_ids="transform")
        load.load_warehouse(transformed)

    with DAG(
        dag_id="ecommerce_etl",
        description="Daily e-commerce sales ETL into the SQLite/warehouse.",
        default_args=default_args,
        schedule="0 2 * * *",          # every day at 02:00
        start_date=datetime(2023, 9, 1),
        catchup=False,
        tags=["etl", "ecommerce", "portfolio"],
    ) as dag:

        extract_task = PythonOperator(task_id="extract", python_callable=_extract)
        transform_task = PythonOperator(task_id="transform", python_callable=_transform)
        quality_task = PythonOperator(task_id="quality", python_callable=_quality)
        load_task = PythonOperator(task_id="load", python_callable=_load)

        # E -> T -> Q -> L  (Load gated behind Quality)
        extract_task >> transform_task >> quality_task >> load_task

except ImportError:
    # Airflow not installed — this module is illustrative only, so importing it
    # in a plain environment is a harmless no-op.
    DAG = None
    if __name__ == "__main__":
        print(
            "This is an EXAMPLE Airflow DAG (concept only). Install apache-airflow "
            "to use it. For a runnable pipeline use:  python etl/pipeline.py"
        )
