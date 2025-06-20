from agno.agent import Agent
from agno.models.ollama import Ollama

task = "Plan an itinerary from Los Angeles to Las Vegas"

reasoning_agent = Agent(
    model=Ollama(id="mistral:latest"),
    reasoning=True,
    markdown=True,
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
