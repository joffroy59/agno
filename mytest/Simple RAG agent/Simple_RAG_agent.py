from agno.embedder.ollama import OllamaEmbedder
from agno.models.ollama import Ollama
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.agent import Agent
from agno.knowledge.website import WebsiteKnowledgeBase
from agno.vectordb.pgvector import PgVector
from agno.vectordb.qdrant import Qdrant

COLLECTION_NAME = "website-content"

vector_db = Qdrant(collection=COLLECTION_NAME, url="http://localhost:6333")



embedder=OllamaEmbedder(id="nomic-embed-text:latest", dimensions=768)
vector_db = LanceDb(
    table_name="gloomhaven",
    uri="tmp/lancedb",
    search_type=SearchType.hybrid,
    embedder=embedder
)
pdf_url_kb = PDFUrlKnowledgeBase(
    # urls=["https://cdn.1j1ju.com/medias/8d/c5/21-gloomhaven-rulebook.pdf"],
    urls=["http://bytrophy.free.fr/files/Reglement-2025.pdf", "http://bytrophy.free.fr/files/Classement-apres-tour-1.pdf"],
    vector_db=vector_db
)

website_kb = WebsiteKnowledgeBase(
    urls=["http://bytrophy.free.fr/"],
    # Number of links to follow from the seed URLs
    max_links=5,
    # Table name: ai.website_documents
    vector_db=vector_db,
)

# Combine knowledge bases
knowledge_base = CombinedKnowledgeBase(
    sources=[
        pdf_url_kb,
        website_kb,
    ],
    vector_db=PgVector(
        table_name="combined_documents",
        db_url=db_url,
    ),
)

agent = Agent(
    model=Ollama(id="mistral", options={"num_ctx": 16192}),
    # Enable RAG
    knowledge=knowledge_base,
    add_context=True,
    # Add references to the original documents
    add_references=True,
    description="You are an expert of the Golf competition By Trophy.",
    instructions=[
        "Use additional data provided for the corresponding infomration on By Trophy.",
        "Cite the reference used at the end of the answer to a question"
    ],
    search_knowledge=False,
    add_history_to_messages=True,
    num_history_responses=10,
    markdown=True,
    # debug_mode=True,
)

prompt = "How many rules"
response = agent.run(prompt)
agent.print_response(response.content)