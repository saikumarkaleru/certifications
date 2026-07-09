"""LLM provider interface with three implementations.

- ``MockLLM`` (DEFAULT): deterministic, no API key. Produces an extractive
  answer by stitching together the most relevant sentences from the retrieved
  context. This lets the demo and the test-suite run fully offline.
- ``OpenAIProvider``: calls the OpenAI Chat Completions API when
  ``OPENAI_API_KEY`` is set. Import guarded.
- ``AnthropicProvider``: calls the Anthropic Messages API when
  ``ANTHROPIC_API_KEY`` is set. Import guarded.

Selection is driven by the ``LLM_PROVIDER`` env var (``mock`` | ``openai`` |
``anthropic``); ``mock`` is the default.
"""
from __future__ import annotations

import os
import re
from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """Common interface: turn a grounded prompt into an answer string."""

    name: str = "base"

    @abstractmethod
    def generate(self, prompt: str, question: str, context: str) -> str:
        """Return an answer. ``prompt`` is the fully-built grounded prompt.

        ``question`` and ``context`` are passed separately so lightweight
        providers (like the mock) can work directly with them instead of
        re-parsing the prompt string.
        """
        ...


def _split_sentences(text: str) -> list[str]:
    """Naive sentence splitter — good enough for extractive stitching."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


class MockLLM(LLMProvider):
    """Deterministic extractive 'LLM' — no network, no key.

    It scores each sentence in the retrieved context by word overlap with the
    question and returns the best few sentences. Deterministic output makes it
    perfect for tests and for a zero-setup demo.
    """

    name = "mock"

    def __init__(self, max_sentences: int = 3) -> None:
        self.max_sentences = max_sentences

    def generate(self, prompt: str, question: str, context: str) -> str:
        q_words = {w for w in re.findall(r"[a-z0-9]+", question.lower()) if len(w) > 2}
        # Drop the verbose "(source: path)" annotation but keep the [n] markers
        # so the extractive answer still reads as a cited response.
        context = re.sub(r"\(source:[^)]*\)\s*", "", context)
        sentences = _split_sentences(context)
        if not sentences:
            return "I could not find relevant information in the provided documents."

        scored: list[tuple[int, int, str]] = []
        for i, sent in enumerate(sentences):
            s_words = set(re.findall(r"[a-z0-9]+", sent.lower()))
            overlap = len(q_words & s_words)
            scored.append((overlap, i, sent))

        # Keep sentences with any overlap; fall back to the first sentence.
        relevant = [s for s in scored if s[0] > 0]
        relevant.sort(key=lambda t: (-t[0], t[1]))  # best overlap, then order
        picked = relevant[: self.max_sentences]
        if not picked:
            picked = [scored[0]]

        # Restore original document order for a readable answer.
        picked.sort(key=lambda t: t[1])
        answer = " ".join(s[2] for s in picked)
        return answer


class OpenAIProvider(LLMProvider):
    """Real OpenAI provider. Requires OPENAI_API_KEY and `pip install openai`."""

    name = "openai"

    def __init__(self, model: str = "gpt-4o-mini") -> None:
        self.model = os.environ.get("OPENAI_MODEL", model)
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")
        try:
            from openai import OpenAI  # type: ignore
        except ImportError as exc:  # pragma: no cover - optional path
            raise ImportError(
                "OpenAIProvider requires the openai package. "
                "Install with: pip install openai"
            ) from exc
        self._client = OpenAI(api_key=api_key)

    def generate(self, prompt: str, question: str, context: str) -> str:  # pragma: no cover
        resp = self._client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant. Answer ONLY using the "
                        "provided context. If the answer is not in the context, "
                        "say you don't know. Cite sources by their [n] markers."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        return resp.choices[0].message.content or ""


class AnthropicProvider(LLMProvider):
    """Real Anthropic provider. Requires ANTHROPIC_API_KEY and `pip install anthropic`."""

    name = "anthropic"

    def __init__(self, model: str = "claude-sonnet-4-5") -> None:
        self.model = os.environ.get("ANTHROPIC_MODEL", model)
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set")
        try:
            import anthropic  # type: ignore
        except ImportError as exc:  # pragma: no cover - optional path
            raise ImportError(
                "AnthropicProvider requires the anthropic package. "
                "Install with: pip install anthropic"
            ) from exc
        self._client = anthropic.Anthropic(api_key=api_key)

    def generate(self, prompt: str, question: str, context: str) -> str:  # pragma: no cover
        msg = self._client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=(
                "You are a helpful assistant. Answer ONLY using the provided "
                "context. If the answer is not in the context, say you don't "
                "know. Cite sources by their [n] markers."
            ),
            messages=[{"role": "user", "content": prompt}],
        )
        # Concatenate text blocks from the response.
        return "".join(
            block.text for block in msg.content if getattr(block, "type", "") == "text"
        )


def get_provider(name: str | None = None) -> LLMProvider:
    """Return a provider by name, defaulting to the ``LLM_PROVIDER`` env var.

    Falls back to ``MockLLM`` so the system always works with no configuration.
    """
    name = (name or os.environ.get("LLM_PROVIDER") or "mock").lower()
    if name == "mock":
        return MockLLM()
    if name == "openai":
        return OpenAIProvider()
    if name == "anthropic":
        return AnthropicProvider()
    raise ValueError(f"unknown LLM_PROVIDER: {name!r} (use mock|openai|anthropic)")
