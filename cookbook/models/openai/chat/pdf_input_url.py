from agno.agent import Agent
from agno.media import File
from agno.models.ollama import Ollama

agent = Agent(
    model=Ollama(id="mistral:latest"),
    markdown=True,
    add_history_to_messages=True,
)

agent.print_response(
    "Suggest me a recipe from the attached file.",
    files=[File(url="https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf")],
)
