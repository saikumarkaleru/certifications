"""llm_agent_toolkit — a stdlib-only ReAct agent with tool calling.

Public surface:
    ReActAgent, default_registry, get_llm, MockLLM, AgentResult
"""

from .agent import ReActAgent
from .llm import AnthropicProvider, MockLLM, OpenAIProvider, get_llm
from .schema import AgentResult, Observation, Step, ToolCall, parse_llm_output
from .tools import default_registry

__all__ = [
    "ReActAgent",
    "default_registry",
    "get_llm",
    "MockLLM",
    "OpenAIProvider",
    "AnthropicProvider",
    "AgentResult",
    "Observation",
    "Step",
    "ToolCall",
    "parse_llm_output",
]

__version__ = "0.1.0"
