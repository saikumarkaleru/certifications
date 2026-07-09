"""Tests for action-JSON parsing and structured types."""

import unittest

from agent.schema import parse_llm_output


class TestParseLLMOutput(unittest.TestCase):
    def test_action_with_json(self):
        text = (
            "Thought: need math\n"
            "Action: calculator\n"
            'Action Input: {"expression": "12*(3+4)"}'
        )
        out = parse_llm_output(text)
        self.assertFalse(out.is_final)
        self.assertTrue(out.has_action)
        self.assertEqual(out.action, "calculator")
        self.assertEqual(out.action_input, {"expression": "12*(3+4)"})
        self.assertEqual(out.thought, "need math")

    def test_final_answer(self):
        out = parse_llm_output("Thought: done\nFinal Answer: 84")
        self.assertTrue(out.is_final)
        self.assertEqual(out.final_answer, "84")

    def test_final_wins_over_action(self):
        text = "Action: calculator\nFinal Answer: 5"
        out = parse_llm_output(text)
        self.assertTrue(out.is_final)

    def test_code_fenced_json(self):
        text = 'Action: search_docs\nAction Input: ```json\n{"query": "react"}\n```'
        out = parse_llm_output(text)
        self.assertEqual(out.action_input, {"query": "react"})

    def test_malformed_json_falls_back(self):
        text = "Action: calculator\nAction Input: 12*(3+4)"
        out = parse_llm_output(text)
        # Non-JSON input is wrapped as {"input": ...} so a tool still gets a dict.
        self.assertEqual(out.action_input, {"input": "12*(3+4)"})

    def test_empty_text(self):
        out = parse_llm_output("")
        self.assertFalse(out.is_final)
        self.assertFalse(out.has_action)

    def test_case_insensitive(self):
        out = parse_llm_output("action: calculator\naction input: {}")
        self.assertEqual(out.action, "calculator")
        self.assertEqual(out.action_input, {})


if __name__ == "__main__":
    unittest.main()
