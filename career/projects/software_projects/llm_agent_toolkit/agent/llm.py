"""LLM provider interface plus a deterministic MockLLM and optional real
providers (OpenAI, Anthropic).

The whole toolkit runs with **zero API keys** thanks to :class:`MockLLM`,
which parses the task and emits ReAct-formatted steps so the agent loop can
exercise real tool calls offline. Real providers are import-guarded: the
``openai`` / ``anthropic`` packages are only imported when actually used, so
the stdlib-only path never breaks.

Select a provider with the ``LLM_PROVIDER`` env var: ``mock`` (default),
``openai`` or ``anthropic``.
"""

from __future__ import annotations

import os
import re
from typing import List, Optional


class BaseLLM:
    """Minimal provider interface: one turn in, one completion out."""

    name = "base"

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        raise NotImplementedError


# --- Mock provider -------------------------------------------------------

# Matches a run of arithmetic characters that contains at least one operator,
# e.g. "12*(3+4)" inside "what is 12*(3+4)?".
_MATH_RE = re.compile(r"(\d[\d\s\.\+\-\*\/\%\(\)]*[\d\)]\s*)")
_HAS_OP_RE = re.compile(r"[\+\-\*\/\%]")
_STOPWORDS = {
    "what", "is", "the", "a", "an", "of", "to", "in", "how", "does",
    "do", "for", "and", "or", "please", "tell", "me", "about", "explain",
    "?", "count", "words",
}


class MockLLM(BaseLLM):
    """A deterministic, key-free stand-in for a real LLM.

    It reads the task and the running scratchpad from ``user_prompt`` and:

    * if a tool has already produced an ``Observation``, it emits a
      ``Final Answer`` built from that observation;
    * otherwise it picks a tool (calculator / word_count / datetime / search)
      by matching the task, and emits ``Thought`` + ``Action`` +
      ``Action Input`` in the exact ReAct text format the agent parses.

    This is intentionally simple and rule-based so tests are reproducible.
    """

    name = "mock"

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        task = self._extract_task(user_prompt)
        last_obs = self._last_observation(user_prompt)

        if last_obs is not None:
            return (
                "Thought: The tool returned a result; I can answer now.\n"
                f"Final Answer: {last_obs}"
            )
        return self._choose_action(task)

    # -- helpers --

    @staticmethod
    def _extract_task(prompt: str) -> str:
        m = re.search(r"Question:\s*(.+)", prompt)
        if m:
            # Take only up to the first newline of the Question line.
            return m.group(1).splitlines()[0].strip()
        return prompt.strip().splitlines()[0] if prompt.strip() else ""

    @staticmethod
    def _last_observation(prompt: str) -> Optional[str]:
        obs = re.findall(r"^\s*Observation.*?:\s*(.+)\s*$", prompt, re.MULTILINE)
        if obs:
            return obs[-1].strip()
        return None

    def _choose_action(self, task: str) -> str:
        low = task.lower()

        # 1) arithmetic
        math = self._find_math(task)
        if math:
            return self._action(
                f"This is an arithmetic question; use the calculator on {math!r}.",
                "calculator",
                f'{{"expression": "{math}"}}',
            )

        # 2) date / time
        if any(k in low for k in ("date", "time", "day", "today", "now")):
            fmt = "%Y-%m-%d"
            return self._action(
                "The question is about the date/time; use datetime_tool.",
                "datetime_tool",
                f'{{"format": "{fmt}"}}',
            )

        # 3) word / text statistics
        if any(k in low for k in ("word count", "how many words", "text stats",
                                  "count the words", "number of words")):
            quoted = self._quoted(task) or task
            safe = quoted.replace('"', "'")
            return self._action(
                "The question asks about word statistics; use word_count.",
                "word_count",
                f'{{"text": "{safe}"}}',
            )

        # 4) default: knowledge-base search
        query = self._keywords(task) or task
        safe = query.replace('"', "'")
        return self._action(
            "I should look this up in the local documents; use search_docs.",
            "search_docs",
            f'{{"query": "{safe}"}}',
        )

    @staticmethod
    def _action(thought: str, tool: str, json_input: str) -> str:
        return (
            f"Thought: {thought}\n"
            f"Action: {tool}\n"
            f"Action Input: {json_input}"
        )

    @staticmethod
    def _find_math(task: str) -> Optional[str]:
        for m in _MATH_RE.finditer(task):
            candidate = m.group(1).strip()
            if _HAS_OP_RE.search(candidate) and re.search(r"\d", candidate):
                return candidate
        return None

    @staticmethod
    def _quoted(task: str) -> Optional[str]:
        m = re.search(r'"([^"]+)"|\'([^\']+)\'', task)
        if m:
            return m.group(1) or m.group(2)
        return None

    @staticmethod
    def _keywords(task: str) -> str:
        tokens = re.findall(r"[a-zA-Z0-9]+", task.lower())
        kept = [t for t in tokens if t not in _STOPWORDS]
        return " ".join(kept)


# --- OpenAI provider (import-guarded) ------------------------------------

class OpenAIProvider(BaseLLM):
    """Calls the OpenAI Chat Completions API when ``OPENAI_API_KEY`` is set.

    Requires ``pip install openai``. The import happens inside ``__init__`` so
    that merely importing this module never needs the package.
    """

    name = "openai"

    def __init__(self, model: Optional[str] = None) -> None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")
        try:
            from openai import OpenAI  # type: ignore
        except ImportError as exc:  # pragma: no cover - needs pip
            raise RuntimeError(
                "openai package not installed; run `pip install openai`"
            ) from exc
        self._client = OpenAI(api_key=api_key)
        self._model = model or os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    def generate(self, system_prompt: str, user_prompt: str) -> str:  # pragma: no cover
        resp = self._client.chat.completions.create(
            model=self._model,
            temperature=0,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return resp.choices[0].message.content or ""


# --- Anthropic provider (import-guarded) ---------------------------------

class AnthropicProvider(BaseLLM):
    """Calls the Anthropic Messages API when ``ANTHROPIC_API_KEY`` is set.

    Requires ``pip install anthropic``. Import is deferred to ``__init__``.
    """

    name = "anthropic"

    def __init__(self, model: Optional[str] = None) -> None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set")
        try:
            import anthropic  # type: ignore
        except ImportError as exc:  # pragma: no cover - needs pip
            raise RuntimeError(
                "anthropic package not installed; run `pip install anthropic`"
            ) from exc
        self._client = anthropic.Anthropic(api_key=api_key)
        self._model = model or os.environ.get(
            "ANTHROPIC_MODEL", "claude-3-5-sonnet-latest"
        )

    def generate(self, system_prompt: str, user_prompt: str) -> str:  # pragma: no cover
        resp = self._client.messages.create(
            model=self._model,
            max_tokens=1024,
            temperature=0,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        parts: List[str] = []
        for block in resp.content:
            text = getattr(block, "text", None)
            if text:
                parts.append(text)
        return "".join(parts)


# --- factory -------------------------------------------------------------

def get_llm(provider: Optional[str] = None) -> BaseLLM:
    """Return an LLM provider chosen by ``provider`` or the ``LLM_PROVIDER``
    env var. Defaults to the offline :class:`MockLLM`."""

    provider = (provider or os.environ.get("LLM_PROVIDER") or "mock").lower()
    if provider in ("mock", "", "none"):
        return MockLLM()
    if provider == "openai":
        return OpenAIProvider()
    if provider == "anthropic":
        return AnthropicProvider()
    raise ValueError(f"unknown LLM_PROVIDER: {provider!r}")
