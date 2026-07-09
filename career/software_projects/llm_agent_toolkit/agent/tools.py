"""Tools the agent can call, plus a small registry.

Every tool exposes a stable ``name``, a human/LLM-readable ``description``
(used to build the system prompt), and a typed :meth:`run` that takes a dict
of arguments and returns a string observation. Tools never trust their input
blindly — the calculator uses an AST allow-list, not ``eval``.
"""

from __future__ import annotations

import ast
import operator
import os
import re
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional


class ToolError(Exception):
    """Raised for bad tool input; caught by the agent and turned into an
    Observation so the loop can recover instead of crashing."""


class Tool:
    """Base class. Subclasses set ``name``/``description`` and implement _run."""

    name: str = "tool"
    description: str = ""

    def run(self, args: Dict[str, Any]) -> str:
        if not isinstance(args, dict):
            raise ToolError("tool arguments must be a JSON object")
        return self._run(args)

    def _run(self, args: Dict[str, Any]) -> str:  # pragma: no cover - abstract
        raise NotImplementedError

    def spec(self) -> str:
        return f"- {self.name}: {self.description}"


# --- calculator ----------------------------------------------------------

_BIN_OPS: Dict[type, Callable[[Any, Any], Any]] = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_UNARY_OPS: Dict[type, Callable[[Any], Any]] = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def safe_eval(expression: str) -> float:
    """Evaluate a pure arithmetic expression safely via an AST allow-list.

    Supports + - * / // % ** and parentheses on numbers only. Any names,
    function calls, or attribute access raise :class:`ToolError`.
    """

    expression = expression.strip()
    if not expression:
        raise ToolError("empty expression")
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise ToolError(f"invalid expression: {expression!r}") from exc

    def _eval(node: ast.AST) -> Any:
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, bool) or not isinstance(
                node.value, (int, float)
            ):
                raise ToolError("only numeric constants are allowed")
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in _BIN_OPS:
            return _BIN_OPS[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPS:
            return _UNARY_OPS[type(node.op)](_eval(node.operand))
        raise ToolError(
            f"unsupported syntax in expression: {type(node).__name__}"
        )

    try:
        return _eval(tree)
    except ZeroDivisionError as exc:
        raise ToolError("division by zero") from exc


class CalculatorTool(Tool):
    name = "calculator"
    description = (
        'Evaluate an arithmetic expression. '
        'Input: {"expression": "12*(3+4)"}. Supports + - * / // % ** and parentheses.'
    )

    def _run(self, args: Dict[str, Any]) -> str:
        expr = args.get("expression") or args.get("input") or ""
        if not isinstance(expr, str):
            expr = str(expr)
        result = safe_eval(expr)
        # Present whole-number floats as ints for clean answers (84.0 -> 84).
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return str(result)


# --- text statistics -----------------------------------------------------

class WordCountTool(Tool):
    name = "word_count"
    description = (
        'Compute text statistics. Input: {"text": "..."}. '
        "Returns word, character, sentence and line counts."
    )

    def _run(self, args: Dict[str, Any]) -> str:
        text = args.get("text") or args.get("input") or ""
        if not isinstance(text, str):
            text = str(text)
        words = re.findall(r"\b\w+\b", text)
        sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
        lines = text.splitlines() or ([text] if text else [])
        return (
            f"words={len(words)} chars={len(text)} "
            f"sentences={len(sentences)} lines={len(lines)}"
        )


# --- datetime ------------------------------------------------------------

class DateTimeTool(Tool):
    """Report the date/time.

    The 'current' time is *injected* (constructor ``now`` or an ``iso``
    argument) so tests are deterministic and never depend on the wall clock.
    """

    name = "datetime_tool"
    description = (
        'Report or format a timestamp. Input: {"format": "%Y-%m-%d"} '
        'and optionally {"iso": "2026-07-08T00:00:00"} to supply the time.'
    )

    def __init__(self, now: Optional[datetime] = None) -> None:
        self._now = now

    def _resolve(self, args: Dict[str, Any]) -> datetime:
        iso = args.get("iso")
        if isinstance(iso, str) and iso.strip():
            try:
                return datetime.fromisoformat(iso.strip())
            except ValueError as exc:
                raise ToolError(f"invalid iso timestamp: {iso!r}") from exc
        if self._now is not None:
            return self._now
        return datetime.now(timezone.utc)

    def _run(self, args: Dict[str, Any]) -> str:
        moment = self._resolve(args)
        fmt = args.get("format") or "%Y-%m-%d %H:%M:%S"
        if not isinstance(fmt, str):
            fmt = str(fmt)
        try:
            return moment.strftime(fmt)
        except (ValueError, TypeError) as exc:
            raise ToolError(f"invalid format string: {fmt!r}") from exc


# --- document search -----------------------------------------------------

class SearchDocsTool(Tool):
    """Keyword search over a small local document set.

    Documents are loaded from a directory (``data/`` by default) or supplied
    directly for tests. Scoring is a simple bag-of-words term overlap — enough
    to demonstrate retrieval without any external dependency.
    """

    name = "search_docs"
    description = (
        'Search the local knowledge base. Input: {"query": "what is ReAct"}. '
        "Returns the best-matching passage."
    )

    def __init__(
        self,
        docs: Optional[Dict[str, str]] = None,
        data_dir: Optional[str] = None,
    ) -> None:
        if docs is not None:
            self.docs = dict(docs)
        else:
            self.docs = self._load_dir(data_dir)

    @staticmethod
    def _load_dir(data_dir: Optional[str]) -> Dict[str, str]:
        if data_dir is None:
            here = os.path.dirname(os.path.abspath(__file__))
            data_dir = os.path.join(os.path.dirname(here), "data")
        docs: Dict[str, str] = {}
        if not os.path.isdir(data_dir):
            return docs
        for fname in sorted(os.listdir(data_dir)):
            if fname.lower().endswith(".txt"):
                path = os.path.join(data_dir, fname)
                try:
                    with open(path, "r", encoding="utf-8") as fh:
                        docs[fname] = fh.read()
                except OSError:
                    continue
        return docs

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        return re.findall(r"[a-z0-9]+", text.lower())

    def _run(self, args: Dict[str, Any]) -> str:
        query = args.get("query") or args.get("input") or ""
        if not isinstance(query, str):
            query = str(query)
        terms = set(self._tokenize(query))
        if not terms:
            raise ToolError("empty search query")
        if not self.docs:
            return "No documents are indexed."

        best_name, best_score, best_snippet = None, 0, ""
        for name, content in self.docs.items():
            doc_tokens = self._tokenize(content)
            score = sum(1 for t in doc_tokens if t in terms)
            if score > best_score:
                best_score = score
                best_name = name
                best_snippet = self._best_line(content, terms)

        if best_name is None:
            return "No relevant document found."
        return f"[{best_name}] {best_snippet}"

    def _best_line(self, content: str, terms: set) -> str:
        best_line, best_hits = content.strip().split("\n")[0], -1
        for line in content.splitlines():
            hits = sum(1 for t in self._tokenize(line) if t in terms)
            if hits > best_hits and line.strip():
                best_hits = hits
                best_line = line.strip()
        return best_line[:300]


# --- registry ------------------------------------------------------------

class ToolRegistry:
    """A name -> Tool mapping used by the agent to dispatch actions."""

    def __init__(self) -> None:
        self._tools: Dict[str, Tool] = {}

    def register(self, tool: Tool) -> "ToolRegistry":
        self._tools[tool.name] = tool
        return self

    def get(self, name: str) -> Optional[Tool]:
        return self._tools.get(name)

    def names(self) -> List[str]:
        return sorted(self._tools)

    def __contains__(self, name: str) -> bool:
        return name in self._tools

    def __iter__(self):
        return iter(self._tools.values())

    def specs(self) -> str:
        return "\n".join(t.spec() for t in self._tools.values())


def default_registry(now: Optional[datetime] = None) -> ToolRegistry:
    """Build the standard toolset used by the CLI and tests."""
    reg = ToolRegistry()
    reg.register(CalculatorTool())
    reg.register(WordCountTool())
    reg.register(DateTimeTool(now=now))
    reg.register(SearchDocsTool())
    return reg
