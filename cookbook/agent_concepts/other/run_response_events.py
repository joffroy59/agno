from typing import Iterator, List

from agno.agent import (
    Agent,
    RunResponseContentEvent,
    RunResponseEvent,
    ToolCallCompletedEvent,
    ToolCallStartedEvent,
)
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Ollama(id="mistral:latest"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
run_response: Iterator[RunResponseEvent] = agent.run(
    "Whats happening in USA and Canada?", stream=True
)

response: List[str] = []
for chunk in run_response:
    if isinstance(chunk, RunResponseContentEvent):
        response.append(chunk.content)
    elif isinstance(chunk, ToolCallStartedEvent):
        response.append(
            f"Tool call started: {chunk.tool.tool_name} with args: {chunk.tool.tool_args}"
        )
    elif isinstance(chunk, ToolCallCompletedEvent):
        response.append(
            f"Tool call completed: {chunk.tool.tool_name} with result: {chunk.tool.result}"
        )

print("\n".join(response))
