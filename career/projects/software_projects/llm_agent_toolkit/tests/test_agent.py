"""End-to-end tests for the ReAct loop with the deterministic MockLLM."""

import unittest
from datetime import datetime

from agent.agent import ReActAgent
from agent.llm import BaseLLM, MockLLM
from agent.tools import ToolRegistry, CalculatorTool, default_registry


def make_agent(**kw):
    return ReActAgent(
        llm=MockLLM(),
        registry=default_registry(now=datetime(2026, 7, 8, 0, 0, 0)),
        **kw,
    )


class TestAgentCalculator(unittest.TestCase):
    def test_solves_arithmetic(self):
        result = make_agent().run("what is 12*(3+4)?")
        self.assertEqual(result.answer, "84")
        self.assertTrue(result.success)
        # Trace should contain a calculator action then a final step.
        actions = [s.action.tool for s in result.steps if s.action]
        self.assertIn("calculator", actions)

    def test_trace_has_observation(self):
        result = make_agent().run("compute 100 - 58")
        obs = [s.observation.output for s in result.steps if s.observation]
        self.assertIn("42", obs)


class TestAgentSearch(unittest.TestCase):
    def test_search_task(self):
        result = make_agent().run("Explain what ReAct reasoning is")
        self.assertTrue(result.success)
        self.assertIn("react.txt", result.answer.lower())


class TestAgentDateTime(unittest.TestCase):
    def test_datetime_task(self):
        result = make_agent().run("what is today's date?")
        self.assertEqual(result.answer, "2026-07-08")


class TestAgentGuardrails(unittest.TestCase):
    def test_unknown_tool_becomes_observation(self):
        class BadLLM(BaseLLM):
            name = "bad"

            def __init__(self):
                self.turn = 0

            def generate(self, system_prompt, user_prompt):
                self.turn += 1
                if self.turn == 1:
                    return (
                        "Thought: try\nAction: nonexistent\nAction Input: {}"
                    )
                return "Final Answer: recovered"

        agent = ReActAgent(llm=BadLLM(), registry=default_registry(), max_steps=4)
        result = agent.run("do something")
        obs = [s.observation for s in result.steps if s.observation]
        self.assertTrue(any(o.error == "unknown_tool" for o in obs))
        self.assertEqual(result.answer, "recovered")

    def test_bad_tool_input_becomes_error_observation(self):
        class BadInputLLM(BaseLLM):
            name = "badinput"

            def __init__(self):
                self.turn = 0

            def generate(self, system_prompt, user_prompt):
                self.turn += 1
                if self.turn == 1:
                    return (
                        "Action: calculator\n"
                        'Action Input: {"expression": "abs(-3)"}'
                    )
                return "Final Answer: handled"

        agent = ReActAgent(
            llm=BadInputLLM(), registry=default_registry(), max_steps=4
        )
        result = agent.run("x")
        obs = [s.observation for s in result.steps if s.observation]
        self.assertTrue(any(o.error is not None for o in obs))

    def test_max_steps_cap(self):
        class LoopLLM(BaseLLM):
            name = "loop"

            def generate(self, system_prompt, user_prompt):
                # Never emits a Final Answer.
                return "Action: calculator\nAction Input: {\"expression\": \"1+1\"}"

        agent = ReActAgent(llm=LoopLLM(), registry=default_registry(), max_steps=3)
        result = agent.run("loop forever")
        self.assertFalse(result.success)
        self.assertEqual(result.stop_reason, "max_steps")
        self.assertEqual(result.iterations, 3)


if __name__ == "__main__":
    unittest.main()
