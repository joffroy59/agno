from agno.agent import Agent
from agno.models.ollama.chat import Ollama

agent = Agent(
    model=Ollama(id="deepseek-r1:14b"),
    reasoning_model=Ollama(id="deepseek-r1:14b"),
)
agent.print_response(
    "Solve the trolley problem. Evaluate multiple ethical frameworks. "
    "Include an ASCII diagram of your solution.",
    stream=True,
)
