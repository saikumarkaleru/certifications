"""The ReAct agent loop.

The agent alternates between asking the LLM for the next step and executing
the tool the LLM chose, feeding each ``Observation`` back into the prompt,
until the LLM emits a ``Final Answer`` or the step budget is exhausted.

Design notes / guardrails:
* the scratchpad is rebuilt each turn and passed back to the model (stateless
  provider interface — friendly to any HTTP LLM);
* unknown tools and bad tool input become Observations, not crashes, so the
  loop can self-correct;
* a hard ``max_steps`` cap prevents infinite loops.
"""

from __future__ import annotations

import json
from typing import List, Optional

from .llm import BaseLLM, get_llm
from .schema import (
    AgentResult,
    LLMOutput,
    Observation,
    Step,
    ToolCall,
    parse_llm_output,
)
from .tools import ToolRegistry, default_registry

SYSTEM_PROMPT = """You are a helpful assistant that solves tasks using tools.
Follow the ReAct format strictly. On each turn output EITHER:

Thought: <your reasoning>
Action: <one tool name>
Action Input: <a JSON object of arguments>

OR, when you have enough information:

Thought: <your reasoning>
Final Answer: <the answer>

Only use these tools:
{tools}

Use exactly one Action per turn and wait for the Observation.
"""


class ReActAgent:
    def __init__(
        self,
        llm: Optional[BaseLLM] = None,
        registry: Optional[ToolRegistry] = None,
        max_steps: int = 6,
    ) -> None:
        self.llm = llm or get_llm()
        self.registry = registry or default_registry()
        self.max_steps = max_steps

    # -- prompt construction --

    def _system_prompt(self) -> str:
        return SYSTEM_PROMPT.format(tools=self.registry.specs())

    def _scratchpad(self, steps: List[Step]) -> str:
        lines: List[str] = []
        for step in steps:
            if step.thought:
                lines.append(f"Thought: {step.thought}")
            if step.action is not None:
                lines.append(f"Action: {step.action.tool}")
                lines.append(
                    f"Action Input: {json.dumps(step.action.tool_input)}"
                )
            if step.observation is not None:
                lines.append(f"Observation: {step.observation.output}")
        return "\n".join(lines)

    def _user_prompt(self, task: str, steps: List[Step]) -> str:
        scratch = self._scratchpad(steps)
        prompt = f"Question: {task}\n"
        if scratch:
            prompt += scratch + "\n"
        return prompt

    # -- main loop --

    def run(self, task: str) -> AgentResult:
        steps: List[Step] = []

        for i in range(1, self.max_steps + 1):
            raw = self.llm.generate(
                self._system_prompt(), self._user_prompt(task, steps)
            )
            parsed: LLMOutput = parse_llm_output(raw)

            if parsed.is_final:
                steps.append(Step(thought=parsed.thought))
                return AgentResult(
                    answer=parsed.final_answer or "",
                    steps=steps,
                    success=True,
                    iterations=i,
                    stop_reason="final_answer",
                )

            if not parsed.has_action:
                # No action and no final answer: treat the raw text as the
                # answer rather than looping pointlessly.
                steps.append(Step(thought=parsed.thought))
                return AgentResult(
                    answer=(parsed.thought or raw).strip(),
                    steps=steps,
                    success=False,
                    iterations=i,
                    stop_reason="no_action",
                )

            call = ToolCall(
                tool=parsed.action or "",
                tool_input=parsed.action_input or {},
            )
            observation = self._dispatch(call)
            steps.append(
                Step(thought=parsed.thought, action=call, observation=observation)
            )

        # Step budget exhausted.
        last = steps[-1].observation.output if steps and steps[-1].observation else ""
        return AgentResult(
            answer=last or "No answer within step budget.",
            steps=steps,
            success=False,
            iterations=self.max_steps,
            stop_reason="max_steps",
        )

    def _dispatch(self, call: ToolCall) -> Observation:
        tool = self.registry.get(call.tool)
        if tool is None:
            return Observation(
                tool=call.tool,
                output=(
                    f"Unknown tool '{call.tool}'. "
                    f"Available: {', '.join(self.registry.names())}."
                ),
                error="unknown_tool",
            )
        try:
            result = tool.run(call.tool_input)
            return Observation(tool=call.tool, output=str(result))
        except Exception as exc:  # noqa: BLE001 - tools may raise anything
            return Observation(
                tool=call.tool,
                output=f"Error running {call.tool}: {exc}",
                error=str(exc),
            )
