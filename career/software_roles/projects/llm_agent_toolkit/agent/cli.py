"""Command-line entry point.

Usage:
    python -m agent.cli "what is 12*(3+4)?"
    python -m agent.cli --provider mock --max-steps 6 "search: what is ReAct?"

Runs the ReAct agent and prints the full reasoning trace followed by the
final answer. Defaults to the offline MockLLM (no API key required).
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone

from .agent import ReActAgent
from .llm import get_llm
from .tools import default_registry


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="agent.cli",
        description="Run a ReAct tool-calling agent on a task.",
    )
    p.add_argument("task", nargs="+", help="the task/question for the agent")
    p.add_argument(
        "--provider",
        default=None,
        help="LLM provider: mock (default), openai, anthropic. "
        "Overrides the LLM_PROVIDER env var.",
    )
    p.add_argument(
        "--max-steps", type=int, default=6, help="max ReAct iterations (default 6)"
    )
    p.add_argument(
        "--now",
        default=None,
        help="ISO timestamp to inject into datetime_tool (deterministic).",
    )
    p.add_argument(
        "--quiet", action="store_true", help="print only the final answer"
    )
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    task = " ".join(args.task)

    now = None
    if args.now:
        try:
            now = datetime.fromisoformat(args.now)
        except ValueError:
            print(f"warning: bad --now value {args.now!r}; ignoring", file=sys.stderr)
    if now is None:
        now = datetime.now(timezone.utc)

    llm = get_llm(args.provider)
    registry = default_registry(now=now)
    agent = ReActAgent(llm=llm, registry=registry, max_steps=args.max_steps)

    result = agent.run(task)

    if not args.quiet:
        print(f"Provider: {llm.name}")
        print(f"Task: {task}\n")
        print(result.format_trace())
        print()
        print(f"(stopped: {result.stop_reason}, iterations: {result.iterations})")
        print("=" * 40)
    print(f"Answer: {result.answer}")
    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
