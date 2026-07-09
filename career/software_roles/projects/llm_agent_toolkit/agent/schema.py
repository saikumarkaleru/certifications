"""Structured types for the agent, using stdlib dataclasses (no pydantic).

These types model the ReAct protocol:

    Thought  -> the model's reasoning
    Action   -> a tool name + JSON input  (a ``ToolCall``)
    Observation -> the tool's result       (an ``Observation``)
    ...repeat...
    Final Answer -> the structured result   (an ``AgentResult``)

The :func:`parse_llm_output` helper turns raw LLM text into a validated
:class:`LLMOutput`, which is the single place where we tolerate messy model
output and fail safely.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ToolCall:
    """A request from the model to run a tool with a JSON argument object."""

    tool: str
    tool_input: Dict[str, Any] = field(default_factory=dict)
    raw_input: str = ""


@dataclass
class Observation:
    """The result of running a tool (or an error message)."""

    tool: str
    output: str
    error: Optional[str] = None

    @property
    def ok(self) -> bool:
        return self.error is None


@dataclass
class Step:
    """One iteration of the ReAct loop, captured for the trace."""

    thought: str = ""
    action: Optional[ToolCall] = None
    observation: Optional[Observation] = None


@dataclass
class LLMOutput:
    """Parsed view of a single LLM completion in the ReAct format."""

    thought: str = ""
    action: Optional[str] = None
    action_input: Optional[Dict[str, Any]] = None
    final_answer: Optional[str] = None
    raw: str = ""

    @property
    def is_final(self) -> bool:
        return self.final_answer is not None

    @property
    def has_action(self) -> bool:
        return bool(self.action)


@dataclass
class AgentResult:
    """The end product of an agent run: an answer plus the full trace."""

    answer: str
    steps: List[Step] = field(default_factory=list)
    success: bool = True
    iterations: int = 0
    stop_reason: str = "final_answer"

    def format_trace(self) -> str:
        """Human-readable reasoning trace for the CLI."""
        lines: List[str] = []
        for i, step in enumerate(self.steps, start=1):
            lines.append(f"--- Step {i} ---")
            if step.thought:
                lines.append(f"Thought: {step.thought}")
            if step.action is not None:
                lines.append(f"Action: {step.action.tool}")
                lines.append(
                    f"Action Input: {json.dumps(step.action.tool_input)}"
                )
            if step.observation is not None:
                tag = "Observation" if step.observation.ok else "Observation (error)"
                lines.append(f"{tag}: {step.observation.output}")
        return "\n".join(lines)


# --- Parsing -------------------------------------------------------------

_ACTION_RE = re.compile(r"^\s*Action\s*:\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
# Capture everything after "Action Input:" to the end so multi-line / code-fenced
# JSON is preserved (Action Input is the last field of a ReAct turn).
_INPUT_RE = re.compile(
    r"Action\s*Input\s*:\s*(.+)\Z", re.IGNORECASE | re.DOTALL
)
_THOUGHT_RE = re.compile(r"^\s*Thought\s*:\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
_FINAL_RE = re.compile(
    r"^\s*Final\s*Answer\s*:\s*(.+)\s*$", re.IGNORECASE | re.MULTILINE | re.DOTALL
)


def _coerce_input(raw: str) -> Dict[str, Any]:
    """Turn an ``Action Input`` string into a dict, tolerantly.

    Accepts strict JSON objects; if that fails, tries to locate the first
    ``{...}`` block; finally falls back to wrapping the raw string as
    ``{"input": raw}`` so a tool always receives a dict.
    """

    raw = raw.strip()
    if not raw:
        return {}
    # Strip code fences if a model wrapped the JSON.
    if raw.startswith("```"):
        raw = raw.strip("`")
        raw = re.sub(r"^json", "", raw, flags=re.IGNORECASE).strip()
    try:
        parsed = json.loads(raw)
        if isinstance(parsed, dict):
            return parsed
        return {"input": parsed}
    except (ValueError, TypeError):
        pass
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if match:
        try:
            parsed = json.loads(match.group(0))
            if isinstance(parsed, dict):
                return parsed
        except ValueError:
            pass
    return {"input": raw}


def parse_llm_output(text: str) -> LLMOutput:
    """Parse a raw LLM completion into a validated :class:`LLMOutput`.

    Robust to extra prose, casing, and code fences. A ``Final Answer`` takes
    precedence over an ``Action`` if both somehow appear.
    """

    out = LLMOutput(raw=text or "")
    if not text:
        return out

    thought_m = _THOUGHT_RE.search(text)
    if thought_m:
        out.thought = thought_m.group(1).strip()

    final_m = _FINAL_RE.search(text)
    if final_m:
        out.final_answer = final_m.group(1).strip()
        return out

    action_m = _ACTION_RE.search(text)
    if action_m:
        out.action = action_m.group(1).strip()
        input_m = _INPUT_RE.search(text)
        raw_input = input_m.group(1).strip() if input_m else ""
        out.action_input = _coerce_input(raw_input)
    return out
