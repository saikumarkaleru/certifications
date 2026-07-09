"""Pipeline orchestrator: Extract -> Transform -> Quality -> Load.

Run it directly:

    python etl/pipeline.py

It wires the stages together, configures logging, gates the Load on the data
quality suite (bad data never reaches the warehouse), and prints a run summary
with row counts, rejects, and check results. Exit code is non-zero if quality
fails, so it is CI/orchestrator friendly.

Standard library only.
"""
from __future__ import annotations

import logging
import sys
import time
from typing import Dict

# Allow "python etl/pipeline.py" to work by ensuring the project root is on the
# path (so `import etl.*` resolves regardless of the invocation directory).
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etl import config, extract, load, quality, transform  # noqa: E402


def configure_logging() -> None:
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL, logging.INFO),
        format=config.LOG_FORMAT,
        datefmt="%H:%M:%S",
    )


def print_summary(
    started: float,
    sources: Dict,
    transformed: Dict,
    results,
    load_counts,
    quality_ok: bool,
) -> None:
    elapsed = time.time() - started
    line = "=" * 62
    print("\n" + line)
    print(" ETL RUN SUMMARY  (e-commerce sales warehouse)")
    print(line)
    print(" EXTRACT")
    print(f"   customers raw rows : {len(sources['customers'])}")
    print(f"   products  raw rows : {len(sources['products'])}")
    print(f"   orders    raw rows : {len(sources['orders'])}")
    print(" TRANSFORM")
    print(f"   dim_customer rows  : {len(transformed['dim_customer'])}")
    print(f"   dim_product  rows  : {len(transformed['dim_product'])}")
    print(f"   fact_sales   rows  : {len(transformed['fact_sales'])}")
    print(f"   rejected rows      : {len(transformed['rejects'])}")
    if transformed["rejects"]:
        from collections import Counter

        reasons = Counter(r["reason"] for r in transformed["rejects"])
        for reason, n in sorted(reasons.items()):
            print(f"       - {reason:24s}: {n}")
    passed = sum(1 for r in results if r.passed)
    print(" QUALITY")
    print(f"   checks passed      : {passed}/{len(results)}")
    for r in results:
        if not r.passed:
            print(f"       FAILED -> {r}")
    print(" LOAD")
    if load_counts is None:
        print("   SKIPPED (quality gate failed) -- warehouse not modified")
    else:
        for table, n in load_counts.items():
            print(f"   {table:18s} : {n} rows")
        print(f"   warehouse db       : {config.WAREHOUSE_DB}")
    print(line)
    print(f" STATUS: {'SUCCESS' if quality_ok else 'FAILED (quality gate)'}"
          f"   |   elapsed {elapsed:.3f}s")
    print(line + "\n")


def run() -> int:
    configure_logging()
    log = logging.getLogger("pipeline")
    started = time.time()

    log.info("=== ETL pipeline starting ===")

    # E — Extract
    sources = extract.extract_all()

    # T — Transform
    transformed = transform.transform_all(sources)

    # Q — Quality (gate before load)
    results = quality.run_quality_checks(transformed)
    quality_ok = quality.all_passed(results)

    # L — Load (only if quality passed)
    load_counts = None
    if quality_ok:
        load_counts = load.load_warehouse(transformed)
        log.info("=== ETL pipeline finished OK ===")
    else:
        log.error("=== Quality gate FAILED — load skipped ===")

    print_summary(started, sources, transformed, results, load_counts, quality_ok)
    return 0 if quality_ok else 1


if __name__ == "__main__":
    sys.exit(run())
