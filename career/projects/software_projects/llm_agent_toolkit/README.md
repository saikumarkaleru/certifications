# llm_agent_toolkit — a ReAct agent with tool calling (stdlib-only core)

A small, genuine **LLM agent framework**: a ReAct-style loop that reasons,
calls tools, reads observations, and returns a structured answer with a full
trace. The core agent loop, tools, CLI, and tests run on the **Python standard
library only — no pip installs and no API key required**. Real LLM providers
(OpenAI, Anthropic) are optional, import-guarded, and plug in via one env var.

```
python -m agent.cli "what is 12*(3+4)?"
# ... Thought / Action: calculator / Observation: 84 ...
# Answer: 84
```

## Why this exists

Modern "GenAI application" work is mostly **orchestration**: giving an LLM a set
of tools, letting it decide which to call, validating its output, and keeping it
safe. This project implements that orchestration from scratch so every moving
part is visible and explainable — the loop, the tool registry, the JSON parsing,
and the guardrails — instead of hiding it behind a framework.

## How it works

### Agents and tool calling
An **agent** is an LLM wrapped in a loop that can take actions in the world. A
**tool** (a.k.a. function call) is a named function with a description and a JSON
argument schema. The model emits a structured request naming a tool and its
arguments; the runtime executes it and feeds the result back. The model never
runs code itself — it only *asks* for a tool, and our code decides whether and
how to run it (the trust boundary).

### ReAct (Reasoning + Acting)
Each turn the model produces text in a strict protocol:

```
Thought: <reasoning about what to do next>
Action: <one tool name>
Action Input: <a JSON object of arguments>
```

The agent runs the tool and appends:

```
Observation: <tool result>
```

…then calls the model again with the growing scratchpad. When the model has
enough information it emits instead:

```
Thought: <reasoning>
Final Answer: <the answer>
```

Interleaving reasoning with observations lets the model plan tool use and stay
grounded in real results.

### The MockLLM (why it runs with no key)
`MockLLM` is a deterministic, rule-based stand-in for a real model. It reads the
task and the scratchpad and emits ReAct-formatted steps: it picks `calculator`
for arithmetic, `datetime_tool` for date questions, `word_count` for text-stats
questions, and `search_docs` otherwise — then, once an `Observation` exists, it
emits a `Final Answer`. This exercises the entire real agent loop and every tool
offline, which is exactly what the tests use.

## Project layout

```
agent/
  schema.py   dataclasses (ToolCall, Observation, Step, AgentResult) + robust
              parse_llm_output() that validates the model's action JSON
  tools.py    Tool base + registry; calculator (AST allow-list, no eval),
              word_count, datetime_tool (injected clock), search_docs
  llm.py      BaseLLM interface; MockLLM (default) + OpenAIProvider +
              AnthropicProvider (import-guarded); get_llm() factory
  agent.py    ReActAgent: the Thought->Action->Observation loop + guardrails
  cli.py      `python -m agent.cli "<task>"`
api.py        optional FastAPI /run endpoint (guarded import)
data/         small .txt knowledge base for search_docs
tests/        unittest suite (tools, parsing, full agent runs)
```

## Run it

Requires only Python 3.11+ (developed on 3.12 / 3.13).

```bash
# Demo tasks (offline MockLLM, no key):
python -m agent.cli "what is 12*(3+4)?"                 # -> 84
python -m agent.cli "Explain what ReAct reasoning is"    # -> search_docs hit
python -m agent.cli 'how many words in "the quick brown fox"?'
python -m agent.cli --now 2026-07-08T00:00:00 "what is today's date?"

# Full trace is printed by default; use --quiet for just the answer.
```

### Tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
# pytest also works if installed:  pytest -q
```

## Plugging in a real LLM

The core needs no dependencies. To use a hosted model:

```bash
pip install openai        # or: pip install anthropic
export LLM_PROVIDER=openai
export OPENAI_API_KEY=sk-...
python -m agent.cli "what is 12*(3+4)?"
```

Or `LLM_PROVIDER=anthropic` with `ANTHROPIC_API_KEY`. The provider classes send
the same system prompt + scratchpad and expect the same ReAct text back, so the
agent loop is unchanged. See `.env.example` for all variables.

## Optional HTTP API

```bash
pip install fastapi uvicorn
uvicorn api:app --reload
# POST /run  {"task": "what is 12*(3+4)?", "provider": "mock"}
```

## Docker

```bash
docker build -t llm-agent .      # runs the test suite during build
docker run --rm llm-agent "what is 2**10?"
```

## Design decisions & guardrails

- **No `eval`.** The calculator walks a Python AST with an operator allow-list;
  names, calls, and attribute access are rejected.
- **Fail into observations, not crashes.** Unknown tool names and bad tool
  input become error `Observation`s so the model can recover.
- **Tolerant parsing.** `parse_llm_output` handles casing, extra prose, and
  code-fenced JSON, and falls back to `{"input": raw}` so a tool always gets a
  dict.
- **Bounded loops.** A hard `max_steps` cap prevents runaway agents.
- **Deterministic time.** `datetime_tool` takes an injected clock so tests never
  depend on the wall clock.

See `STUDY_GUIDE.md` for a deeper walkthrough and interview Q&A.
