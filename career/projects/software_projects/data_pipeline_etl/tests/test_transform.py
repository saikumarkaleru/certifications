"""Unit tests for the transform stage (stdlib unittest, runs fully offline)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etl import transform  # noqa: E402


class TestHelpers(unittest.TestCase):
    def test_clean_str_strips_and_nulls(self):
        self.assertEqual(transform.clean_str("  hi  "), "hi")
        self.assertIsNone(transform.clean_str("   "))
        self.assertIsNone(transform.clean_str(""))
        self.assertIsNone(transform.clean_str(None))

    def test_parse_int(self):
        self.assertEqual(transform.parse_int(" 2 "), 2)
        self.assertEqual(transform.parse_int("-3"), -3)
        self.assertIsNone(transform.parse_int("two"))
        self.assertIsNone(transform.parse_int("3.5"))
        self.assertIsNone(transform.parse_int(""))

    def test_parse_float(self):
        self.assertEqual(transform.parse_float("799.00"), 799.0)
        self.assertEqual(transform.parse_float(1999), 1999.0)
        self.assertIsNone(transform.parse_float("abc"))
        self.assertIsNone(transform.parse_float(""))

    def test_parse_date(self):
        self.assertEqual(transform.parse_date("2023-09-01"), "2023-09-01")
        self.assertIsNone(transform.parse_date("not_a_date"))
        self.assertIsNone(transform.parse_date(""))


class TestDimensions(unittest.TestCase):
    def test_customers_dedupe_and_clean(self):
        raw = [
            {"customer_id": "C1", "name": " A ", "city": "X", "signup_date": "2023-01-01"},
            {"customer_id": "C1", "name": "A", "city": "X", "signup_date": "2023-01-01"},
            {"customer_id": "", "name": "B", "city": "Y", "signup_date": "2023-01-02"},
        ]
        out = transform.transform_customers(raw)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]["name"], "A")

    def test_products_typecast(self):
        raw = [{"product_id": "P1", "name": "M", "category": "E", "unit_price": "10.5"}]
        out = transform.transform_products(raw)
        self.assertEqual(out[0]["unit_price"], 10.5)


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.customers = [{"customer_id": "C1"}, {"customer_id": "C2"}]
        self.products = [
            {"product_id": "P1", "unit_price": 100.0},
            {"product_id": "P2", "unit_price": 50.0},
        ]

    def _run(self, raw):
        return transform.transform_orders(raw, self.customers, self.products)

    def test_happy_path_and_revenue(self):
        raw = [{"order_id": "O1", "customer_id": "C1", "product_id": "P1",
                "quantity": "2", "order_date": "2023-09-01", "unit_price": "100.0"}]
        facts, rejects = self._run(raw)
        self.assertEqual(len(facts), 1)
        self.assertEqual(rejects, [])
        self.assertEqual(facts[0]["revenue"], 200.0)

    def test_dedupe_orders(self):
        raw = [
            {"order_id": "O1", "customer_id": "C1", "product_id": "P1",
             "quantity": "1", "order_date": "2023-09-01", "unit_price": "100"},
            {"order_id": "O1", "customer_id": "C1", "product_id": "P1",
             "quantity": "1", "order_date": "2023-09-01", "unit_price": "100"},
        ]
        facts, rejects = self._run(raw)
        self.assertEqual(len(facts), 1)
        self.assertTrue(any(r["reason"] == "duplicate order_id" for r in rejects))

    def test_rejects_bad_quantity(self):
        raw = [{"order_id": "O1", "customer_id": "C1", "product_id": "P1",
                "quantity": "two", "order_date": "2023-09-01", "unit_price": "100"}]
        facts, rejects = self._run(raw)
        self.assertEqual(facts, [])
        self.assertEqual(rejects[0]["reason"], "non-integer quantity")

    def test_rejects_nonpositive_quantity(self):
        raw = [{"order_id": "O1", "customer_id": "C1", "product_id": "P1",
                "quantity": "0", "order_date": "2023-09-01", "unit_price": "100"}]
        facts, rejects = self._run(raw)
        self.assertEqual(facts, [])
        self.assertEqual(rejects[0]["reason"], "quantity below minimum")

    def test_rejects_bad_date(self):
        raw = [{"order_id": "O1", "customer_id": "C1", "product_id": "P1",
                "quantity": "1", "order_date": "bad", "unit_price": "100"}]
        facts, rejects = self._run(raw)
        self.assertEqual(rejects[0]["reason"], "invalid order_date")

    def test_rejects_orphans(self):
        raw = [
            {"order_id": "O1", "customer_id": "C9", "product_id": "P1",
             "quantity": "1", "order_date": "2023-09-01", "unit_price": "100"},
            {"order_id": "O2", "customer_id": "C1", "product_id": "P9",
             "quantity": "1", "order_date": "2023-09-01", "unit_price": "100"},
        ]
        facts, rejects = self._run(raw)
        self.assertEqual(facts, [])
        reasons = {r["reason"] for r in rejects}
        self.assertIn("orphan customer_id", reasons)
        self.assertIn("orphan product_id", reasons)

    def test_backfills_missing_price_from_product(self):
        raw = [{"order_id": "O1", "customer_id": "C1", "product_id": "P2",
                "quantity": "3", "order_date": "2023-09-01", "unit_price": ""}]
        facts, rejects = self._run(raw)
        self.assertEqual(len(facts), 1)
        self.assertEqual(facts[0]["unit_price"], 50.0)
        self.assertEqual(facts[0]["revenue"], 150.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
