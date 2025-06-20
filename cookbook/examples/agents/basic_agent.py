from agno.agent import Agent
from agno.models.ollama import Ollama

agent = Agent(model=Ollama(id="mistral:latest"), markdown=True)
agent.print_response("What is the stock price of Apple?", stream=True)
