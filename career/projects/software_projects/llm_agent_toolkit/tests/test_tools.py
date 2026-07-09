"""Tests for the individual tools."""

import unittest
from datetime import datetime

from agent.tools import (
    CalculatorTool,
    DateTimeTool,
    SearchDocsTool,
    ToolError,
    WordCountTool,
    default_registry,
    safe_eval,
)


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = CalculatorTool()

    def test_basic(self):
        self.assertEqual(self.calc.run({"expression": "12*(3+4)"}), "84")

    def test_precedence_and_power(self):
        self.assertEqual(self.calc.run({"expression": "2 + 3 * 4"}), "14")
        self.assertEqual(self.calc.run({"expression": "2 ** 10"}), "1024")

    def test_float_result(self):
        self.assertEqual(self.calc.run({"expression": "7 / 2"}), "3.5")

    def test_whole_float_becomes_int(self):
        self.assertEqual(self.calc.run({"expression": "10 / 2"}), "5")

    def test_rejects_names(self):
        with self.assertRaises(ToolError):
            safe_eval("__import__('os')")

    def test_rejects_calls(self):
        with self.assertRaises(ToolError):
            safe_eval("abs(-5)")

    def test_division_by_zero(self):
        with self.assertRaises(ToolError):
            safe_eval("1/0")

    def test_empty(self):
        with self.assertRaises(ToolError):
            safe_eval("")


class TestWordCount(unittest.TestCase):
    def test_counts(self):
        out = WordCountTool().run({"text": "hello world. bye!"})
        self.assertIn("words=3", out)
        self.assertIn("sentences=2", out)


class TestDateTime(unittest.TestCase):
    def test_injected_now(self):
        tool = DateTimeTool(now=datetime(2026, 7, 8, 10, 30, 0))
        self.assertEqual(tool.run({"format": "%Y-%m-%d"}), "2026-07-08")

    def test_iso_argument_overrides(self):
        tool = DateTimeTool(now=datetime(2000, 1, 1))
        self.assertEqual(
            tool.run({"iso": "2026-07-08T00:00:00", "format": "%Y"}), "2026"
        )

    def test_bad_iso(self):
        with self.assertRaises(ToolError):
            DateTimeTool().run({"iso": "not-a-date"})


class TestSearchDocs(unittest.TestCase):
    def test_in_memory_docs(self):
        tool = SearchDocsTool(
            docs={
                "a.txt": "ReAct interleaves reasoning and acting with tools.",
                "b.txt": "The calculator evaluates arithmetic safely.",
            }
        )
        out = tool.run({"query": "what is ReAct reasoning"})
        self.assertIn("a.txt", out)

    def test_empty_query(self):
        with self.assertRaises(ToolError):
            SearchDocsTool(docs={"a.txt": "x"}).run({"query": "   "})

    def test_loads_data_dir(self):
        # Uses the real data/ directory shipped with the project.
        tool = SearchDocsTool()
        self.assertTrue(tool.docs, "expected data/*.txt documents to load")
        out = tool.run({"query": "guardrails and evaluation"})
        self.assertTrue(out.startswith("["))


class TestRegistry(unittest.TestCase):
    def test_default_registry_has_tools(self):
        reg = default_registry()
        self.assertEqual(
            reg.names(),
            ["calculator", "datetime_tool", "search_docs", "word_count"],
        )
        self.assertIn("calculator", reg)
        self.assertIsNone(reg.get("nope"))


if __name__ == "__main__":
    unittest.main()
