from typing import Iterator
from agno.agent import Agent, RunResponseEvent
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response
from agno.models.ollama import Ollama

agent = Agent(model=Ollama(id="mistral:latest"))

# Run agent and return the response as a stream
response_stream: Iterator[RunResponseEvent] = agent.run(
    "Tell me a 5 second short story about a lion",
    stream=True
)

# Print the response stream in markdown format
pprint_run_response(response_stream, markdown=True)
