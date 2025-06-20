import asyncio
from typing import Iterator  # noqa

from agno.agent import Agent, RunResponseEvent  # noqa
from agno.models.ollama import Ollama

agent = Agent(model=Ollama(id="mistral:latest"), markdown=True)

# Get the response in a variable
run_response: Iterator[RunResponseEvent] = agent.run(
    "Share a 2 sentence horror story", stream=True
)
for chunk in run_response:
    print(chunk.content, end="")

# # Print the response in the terminal
# asyncio.run(agent.aprint_response("Share a 2 sentence horror story", stream=True))
