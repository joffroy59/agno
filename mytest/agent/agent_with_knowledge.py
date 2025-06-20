import typer
from rich.prompt import Prompt
from typing import Optional

from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.chroma import ChromaDb
from agno.models.ollama import Ollama
from agno.embedder.ollama import OllamaEmbedder

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=ChromaDb(
            collection="recipes",
            embedder=OllamaEmbedder(id="llama3.2", dimensions=3072)),
)

def pdf_agent(user: str = "user"):
    run_id: Optional[str] = None

    agent = Agent(
        user_id=user,
        knowledge=knowledge_base,
        show_tool_calls=True,
        debug_mode=True,
        model=Ollama(id="llama3.1:8b"),
    )
    run_id = agent.run_id
    print(f"Started Run: {run_id}\n")

    while True:
        message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
        if message in ("exit", "bye"):
            break
        agent.print_response(message)

if __name__ == "__main__":
    # Comment out after first run
    knowledge_base.load(recreate=False)

    typer.run(pdf_agent)