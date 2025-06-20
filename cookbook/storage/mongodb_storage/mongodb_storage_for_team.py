"""
1. Run: `pip install openai duckduckgo-search newspaper4k lxml_html_clean agno` to install the dependencies
2. Run: `python cookbook/storage/mongodb_storage/mongodb_storage_for_team.py` to run the agent
"""

from typing import List

from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.storage.mongodb import MongoDbStorage
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from pydantic import BaseModel

# MongoDB connection settings
db_url = "mongodb://localhost:27017"


class Article(BaseModel):
    title: str
    summary: str
    reference_links: List[str]


hn_researcher = Agent(
    name="HackerNews Researcher",
    model=Ollama(id="mistral:latest"),
    role="Gets top stories from hackernews.",
    tools=[HackerNewsTools()],
)

web_searcher = Agent(
    name="Web Searcher",
    model=Ollama(id="mistral:latest"),
    role="Searches the web for information on a topic",
    tools=[DuckDuckGoTools()],
    add_datetime_to_instructions=True,
)


hn_team = Team(
    name="HackerNews Team",
    mode="coordinate",
    model=Ollama(id="mistral:latest"),
    members=[hn_researcher, web_searcher],
    storage=MongoDbStorage(
        collection_name="team_sessions", db_url=db_url, db_name="agno"
    ),
    instructions=[
        "First, search hackernews for what the user is asking about.",
        "Then, ask the web searcher to search for each story to get more information.",
        "Finally, provide a thoughtful and engaging summary.",
    ],
    response_model=Article,
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
    show_members_responses=True,
    add_member_tools_to_system_message=False,
)

hn_team.print_response("Write an article about the top 2 stories on hackernews")
