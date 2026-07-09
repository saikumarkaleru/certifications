# STUDY_GUIDE — llm_agent_toolkit

A defensible, line-by-line explainable GenAI project for a **GenAI / LLM
Application Engineer** resume. Read this before an interview.

## 30-second pitch

"I built a ReAct-style LLM agent framework from scratch in pure Python. The
agent runs a Thought → Action → Observation loop: the model reasons, picks a
tool, my runtime executes it and feeds the result back, and this repeats until
the model gives a Final Answer. It ships with four real tools — a safe
AST-based calculator, text stats, a datetime tool, and a keyword document
search — plus a tool registry and structured-output parsing. The whole core
runs on the standard library with a deterministic MockLLM, so it needs no API
key to run or test; OpenAI and Anthropic providers plug in behind one env var.
There are 30 unit tests covering tools, JSON parsing, and full agent runs
including error recovery."

## Architecture walkthrough

1. **`schema.py`** — stdlib dataclasses model the protocol: `ToolCall`
   (tool + JSON args), `Observation` (result or error), `Step` (one loop
   iteration), `AgentResult` (answer + trace). `parse_llm_output()` is the
   single trust-boundary parser: it extracts Thought / Action / Action Input /
   Final Answer with tolerant regexes and coerces the action JSON into a dict.
2. **`tools.py`** — `Tool` base class (name, description, typed `run`) and a
   `ToolRegistry`. `safe_eval` evaluates arithmetic by walking an AST with an
   operator allow-list (no `eval`). `SearchDocsTool` does bag-of-words term
   overlap over `data/*.txt`. `DateTimeTool` takes an injected clock for
   determinism.
3. **`llm.py`** — `BaseLLM.generate(system, user)` interface. `MockLLM` is a
   rule-based model that emits ReAct steps offline. `OpenAIProvider` /
   `AnthropicProvider` defer their imports to `__init__`, so importing the
   module never requires the SDK. `get_llm()` chooses via `LLM_PROVIDER`.
4. **`agent.py`** — `ReActAgent.run(task)` builds the system prompt from the
   registry, rebuilds the scratchpad each turn, calls the model, parses the
   output, dispatches the tool, records a `Step`, and loops until Final Answer
   or `max_steps`. `_dispatch` turns unknown tools / exceptions into error
   observations.
5. **`cli.py` / `api.py`** — a CLI that prints the trace, and an optional
   guarded FastAPI endpoint.

## Core concepts (be ready to explain these)

- **Agent** — an LLM in a loop that can take actions (call tools) toward a goal.
- **Tool / function calling** — exposing named functions with descriptions and
  argument schemas so the model can request structured actions instead of
  free-text. The model *proposes*; your code *executes* — that split is the
  security boundary.
- **ReAct** — interleaving Reasoning (Thought) and Acting (Action/Observation)
  in one prompt loop; reasoning plans the next tool, observations ground it.
- **Structured output** — forcing a parseable format (here a text protocol +
  JSON args; with real APIs, native tool-call/JSON-schema outputs).
- **Guardrails** — allow-list eval, bounded steps, error-as-observation,
  input validation.
- **Evaluation** — deterministic tests that assert correct final answers, tool
  selection, and recovery from bad input.

## Interview Q&A (18–20)

**1. What is an LLM agent?**
An LLM wrapped in a control loop that lets it take actions — call tools, read
results, and decide the next step — rather than emitting a single answer.

**2. What is the ReAct pattern and why use it?**
ReAct interleaves reasoning traces with actions and observations. The reasoning
helps the model choose the right tool and sequence steps; the observations feed
real data back so it hallucinates less. It's a simple, model-agnostic protocol.

**3. How does tool / function calling actually work here?**
The system prompt lists tools with descriptions. The model outputs `Action:
<name>` and `Action Input: <json>`. `parse_llm_output` validates that, the
registry looks up the tool, and the agent runs it and appends an `Observation`.
Production APIs do the same thing with native structured tool-call fields; I used
a text protocol so the mechanics are visible.

**4. Why can this run without an API key?**
`MockLLM` is a deterministic stand-in that parses the task and emits ReAct steps
using the same interface a real provider would. It drives the real loop and real
tools, so tests and demos are fully offline and reproducible.

**5. How would you swap in a real model?**
Set `LLM_PROVIDER=openai` (or `anthropic`) and the key. `get_llm()` returns the
provider; it implements the same `generate(system, user)` method, so nothing in
the agent loop changes. Imports are guarded so the SDK is only needed when used.

**6. How do you keep the calculator safe?**
`safe_eval` parses the expression to an AST and evaluates only `BinOp`/`UnaryOp`
over numeric constants with an operator allow-list. Any `Name`, `Call`, or
attribute access raises `ToolError`. There is no `eval`/`exec`, so
`__import__('os')` or `abs(-5)` are rejected.

**7. What happens if the model asks for a tool that doesn't exist?**
`_dispatch` returns an `Observation` with `error="unknown_tool"` and the list of
valid tools, fed back to the model so it can correct itself — no crash.

**8. What if the tool input is malformed JSON?**
`parse_llm_output` tries strict JSON, then the first `{...}` block, then falls
back to `{"input": raw}` so a tool always receives a dict. If the tool still
can't use it, the exception becomes an error observation.

**9. How do you prevent infinite loops?**
A hard `max_steps` cap. If reached, the agent returns `success=False`,
`stop_reason="max_steps"`, and the last observation as a best-effort answer.

**10. How is the agent tested?**
30 `unittest` tests: each tool (e.g. calculator computes 84), the action-JSON
parser (including code-fenced and malformed input), and full agent runs —
arithmetic, search, datetime, unknown-tool recovery, bad-input recovery, and
the step cap. Injected clock + MockLLM make them deterministic.

**11. Why inject the clock into datetime_tool?**
So tests never depend on wall-clock time. The 'now' comes from the constructor
or an `iso` argument, making output reproducible.

**12. How does document search work? Is it RAG?**
It's the retrieval half: a keyword bag-of-words overlap score over local text
files, returning the best-matching passage. Real RAG would swap this scorer for
embeddings + a vector store; the tool interface would stay the same.

**13. What's the trust boundary in an agent?**
The model's output is untrusted text. It can *request* actions but never execute
anything directly — my code validates the request and decides what to run. That
separation is where you enforce allow-lists, auth, and rate limits.

**14. How would you add a new tool?**
Subclass `Tool`, set `name`/`description`, implement `_run(args) -> str`, and
`registry.register(...)`. The description auto-appears in the system prompt and
the agent can call it immediately.

**15. Structured output — how would you harden it for a real model?**
Use the provider's native tool-calling / JSON-schema mode so the model returns
validated arguments, add retries with a "your JSON was invalid" message, and
validate against a schema before dispatch. My tolerant parser is the fallback.

**16. How do you evaluate agent quality beyond unit tests?**
Task success rate on a labeled set, average steps to answer, correct-tool
selection rate, and recovery rate on adversarial/broken inputs — plus latency
and cost per task with real providers. An LLM-as-judge can grade open-ended
answers.

**17. What are the main failure modes of agents and your mitigations?**
Hallucinated tools/args (validation + error observations), infinite loops (step
cap), prompt injection via tool results (treat observations as untrusted, keep
tools least-privilege), and cost blowups (step/token budgets).

**18. Why build this instead of using LangChain?**
To understand and own every layer — the loop, parsing, and guardrails — which
makes it debuggable and explainable. The concepts map 1:1 onto any framework;
the abstractions here are deliberately thin.

**19. How would you add multi-tool / multi-step planning?**
The loop already supports N steps; MockLLM finalizes after one observation for
determinism, but a real model can chain: read one observation, then issue
another Action before the Final Answer. I'd also add scratchpad summarization to
control context length.

**20. What would you improve next?**
Native function-calling for real providers, embedding-based retrieval for
`search_docs`, per-tool timeouts and concurrency, token/cost tracking, and a
richer eval harness with a labeled task suite.

## Known scope / honest limits

- `MockLLM` is rule-based, not a learned model — it's for offline demos/tests.
- `search_docs` is keyword overlap, not embeddings (RAG-lite).
- Real-provider paths need `pip install` + a key; the FastAPI app needs
  `pip install fastapi uvicorn`. The core does not.
