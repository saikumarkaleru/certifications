"""Data-quality stage: assert the transformed data is trustworthy.

Runs a battery of checks against the in-memory star schema BEFORE it is loaded
into the warehouse (fail fast, never load bad data). Each check returns a
QualityResult with a pass/fail flag and a human-readable message.

Check families:
  * not-null      : required columns are never null
  * uniqueness    : primary keys are unique
  * row-count     : tables are non-empty (a silent 0-row load is a red flag)
  * referential   : every fact foreign key resolves to a dimension
  * value-range   : quantity/price/revenue are sane

Standard library only.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Dict, List

logger = logging.getLogger("quality")


@dataclass
class QualityResult:
    name: str
    passed: bool
    detail: str

    def __str__(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        return f"[{status}] {self.name}: {self.detail}"


# --------------------------------------------------------------------------- #
# Individual, reusable check primitives
# --------------------------------------------------------------------------- #
def check_not_null(rows: List[Dict], columns: List[str], table: str) -> QualityResult:
    bad = 0
    for r in rows:
        if any(r.get(c) is None for c in columns):
            bad += 1
    return QualityResult(
        name=f"not_null.{table}",
        passed=bad == 0,
        detail=f"{bad} row(s) with null in {columns}",
    )


def check_unique(rows: List[Dict], key: str, table: str) -> QualityResult:
    values = [r.get(key) for r in rows]
    dupes = len(values) - len(set(values))
    return QualityResult(
        name=f"unique.{table}.{key}",
        passed=dupes == 0,
        detail=f"{dupes} duplicate {key} value(s)",
    )


def check_row_count(rows: List[Dict], table: str, minimum: int = 1) -> QualityResult:
    n = len(rows)
    return QualityResult(
        name=f"row_count.{table}",
        passed=n >= minimum,
        detail=f"{n} row(s) (minimum {minimum})",
    )


def check_referential(
    facts: List[Dict], dim_rows: List[Dict], fk: str, pk: str, name: str
) -> QualityResult:
    valid_keys = {d.get(pk) for d in dim_rows}
    orphans = [f for f in facts if f.get(fk) not in valid_keys]
    return QualityResult(
        name=f"referential.{name}",
        passed=len(orphans) == 0,
        detail=f"{len(orphans)} fact row(s) with unresolved {fk}",
    )


def check_positive(rows: List[Dict], column: str, table: str) -> QualityResult:
    bad = [r for r in rows if r.get(column) is None or r.get(column) <= 0]
    return QualityResult(
        name=f"positive.{table}.{column}",
        passed=len(bad) == 0,
        detail=f"{len(bad)} row(s) with non-positive {column}",
    )


# --------------------------------------------------------------------------- #
# Orchestrated suite
# --------------------------------------------------------------------------- #
def run_quality_checks(data: Dict[str, List[Dict]]) -> List[QualityResult]:
    """Run the full suite against the transformed star schema."""
    customers = data["dim_customer"]
    products = data["dim_product"]
    facts = data["fact_sales"]

    results: List[QualityResult] = [
        # Dimensions: keys present + unique + non-empty.
        check_not_null(customers, ["customer_id"], "dim_customer"),
        check_unique(customers, "customer_id", "dim_customer"),
        check_row_count(customers, "dim_customer"),
        check_not_null(products, ["product_id", "unit_price"], "dim_product"),
        check_unique(products, "product_id", "dim_product"),
        check_row_count(products, "dim_product"),
        # Fact: keys, uniqueness, ranges, non-empty.
        check_not_null(
            facts,
            ["order_id", "customer_id", "product_id", "quantity", "order_date"],
            "fact_sales",
        ),
        check_unique(facts, "order_id", "fact_sales"),
        check_row_count(facts, "fact_sales"),
        check_positive(facts, "quantity", "fact_sales"),
        check_positive(facts, "revenue", "fact_sales"),
        # Referential integrity fact -> dimensions.
        check_referential(facts, customers, "customer_id", "customer_id", "customer"),
        check_referential(facts, products, "product_id", "product_id", "product"),
    ]

    for res in results:
        (logger.info if res.passed else logger.error)("%s", res)
    return results


def all_passed(results: List[QualityResult]) -> bool:
    return all(r.passed for r in results)
