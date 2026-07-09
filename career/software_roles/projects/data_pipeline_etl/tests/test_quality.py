"""Unit tests for the data-quality stage (stdlib unittest, offline)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etl import quality  # noqa: E402


class TestChecks(unittest.TestCase):
    def test_not_null(self):
        rows = [{"a": 1}, {"a": None}]
        self.assertFalse(quality.check_not_null(rows, ["a"], "t").passed)
        self.assertTrue(quality.check_not_null([{"a": 1}], ["a"], "t").passed)

    def test_unique(self):
        self.assertTrue(quality.check_unique([{"k": 1}, {"k": 2}], "k", "t").passed)
        self.assertFalse(quality.check_unique([{"k": 1}, {"k": 1}], "k", "t").passed)

    def test_row_count(self):
        self.assertFalse(quality.check_row_count([], "t").passed)
        self.assertTrue(quality.check_row_count([{"x": 1}], "t").passed)

    def test_referential(self):
        facts = [{"fk": "A"}, {"fk": "Z"}]
        dims = [{"pk": "A"}]
        self.assertFalse(quality.check_referential(facts, dims, "fk", "pk", "d").passed)
        self.assertTrue(
            quality.check_referential([{"fk": "A"}], dims, "fk", "pk", "d").passed
        )

    def test_positive(self):
        self.assertFalse(quality.check_positive([{"q": 0}], "q", "t").passed)
        self.assertFalse(quality.check_positive([{"q": -1}], "q", "t").passed)
        self.assertTrue(quality.check_positive([{"q": 3}], "q", "t").passed)


class TestSuite(unittest.TestCase):
    def _clean_data(self):
        return {
            "dim_customer": [{"customer_id": "C1"}],
            "dim_product": [{"product_id": "P1", "unit_price": 10.0}],
            "fact_sales": [{
                "order_id": "O1", "customer_id": "C1", "product_id": "P1",
                "quantity": 2, "unit_price": 10.0, "revenue": 20.0,
                "order_date": "2023-09-01",
            }],
        }

    def test_clean_data_all_pass(self):
        results = quality.run_quality_checks(self._clean_data())
        self.assertTrue(quality.all_passed(results))

    def test_orphan_fact_fails_suite(self):
        data = self._clean_data()
        data["fact_sales"][0]["customer_id"] = "C_MISSING"
        results = quality.run_quality_checks(data)
        self.assertFalse(quality.all_passed(results))


if __name__ == "__main__":
    unittest.main(verbosity=2)
