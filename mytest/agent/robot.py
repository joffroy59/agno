from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.ollama import Ollama
from agno.utils.pprint import pprint_run_response

agent = Agent(model=Ollama(id="mistral:latest"))

# Run agent and return the response as a variable
response: RunResponse = agent.run("Tell me a 5 second short story about a robot")

# Print the response in markdown format
pprint_run_response(response, markdown=True)