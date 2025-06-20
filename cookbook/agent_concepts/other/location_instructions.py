from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Ollama(id="mistral:latest"),
    add_location_to_instructions=True,
    tools=[DuckDuckGoTools(cache_results=True)],
)
agent.print_response("What is current news about my city?")
