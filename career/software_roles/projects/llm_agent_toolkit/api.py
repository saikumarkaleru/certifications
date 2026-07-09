"""Optional FastAPI service exposing the agent over HTTP.

This file is import-guarded: FastAPI is NOT required for the core toolkit.
Install the extras first:

    pip install fastapi uvicorn

Then run:

    uvicorn api:app --reload

POST /run  { "task": "what is 12*(3+4)?", "provider": "mock" }
GET  /health
"""

from __future__ import annotations

try:
    from fastapi import FastAPI
    from pydantic import BaseModel
except ImportError as exc:  # pragma: no cover - optional dependency
    raise SystemExit(
        "FastAPI is not installed. Run: pip install fastapi uvicorn"
    ) from exc

from typing import Optional

from agent.agent import ReActAgent
from agent.llm import get_llm
from agent.tools import default_registry

app = FastAPI(title="llm_agent_toolkit", version="0.1.0")


class RunRequest(BaseModel):
    task: str
    provider: Optional[str] = None
    max_steps: int = 6


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/run")
def run(req: RunRequest) -> dict:
    llm = get_llm(req.provider)
    agent = ReActAgent(
        llm=llm, registry=default_registry(), max_steps=req.max_steps
    )
    result = agent.run(req.task)
    return {
        "provider": llm.name,
        "task": req.task,
        "answer": result.answer,
        "success": result.success,
        "iterations": result.iterations,
        "stop_reason": result.stop_reason,
        "trace": [
            {
                "thought": s.thought,
                "action": s.action.tool if s.action else None,
                "action_input": s.action.tool_input if s.action else None,
                "observation": s.observation.output if s.observation else None,
            }
            for s in result.steps
        ],
    }
