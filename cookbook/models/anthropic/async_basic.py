"""
Basic async example using Claude.
"""

import asyncio

from agno.agent import Agent
from agno.models.ollama import Ollama

agent = Agent(
    model=Ollama(id="mistral:latest"),
    markdown=True,
)

asyncio.run(agent.aprint_response("Share a 2 sentence horror story"))
