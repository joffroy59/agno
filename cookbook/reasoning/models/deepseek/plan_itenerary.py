from agno.agent import Agent
from agno.models.deepseek import DeepSeek
from agno.models.ollama import Ollama

task = "Plan an itinerary from Los Angeles to Las Vegas"

reasoning_agent = Agent(
    model=Ollama(id="mistral:latest"),
    reasoning_model=DeepSeek(id="deepseek-reasoner"),
    markdown=True,
)
reasoning_agent.print_response(task, stream=True)
