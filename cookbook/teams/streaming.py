from typing import Iterator  # noqa
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.team.team import Team
from agno.tools.yfinance import YFinanceTools


stock_searcher = Agent(
    name="Stock Searcher",
    model=Ollama(id="mistral:latest"),
    role="Searches the web for information on a stock.",
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
        )
    ],
)

company_info_agent = Agent(
    name="Company Info Searcher",
    model=Ollama(id="mistral:latest"),
    role="Searches the web for information on a stock.",
    tools=[
        YFinanceTools(
            stock_price=False,
            company_info=True,
            company_news=True,
        )
    ],
)


team = Team(
    name="Stock Research Team",
    mode="route",
    model=Ollama(id="mistral:latest"),
    members=[stock_searcher, company_info_agent],
    markdown=True,
    show_members_responses=True,
)

team.print_response("What is the current stock price of NVDA?", stream=True)
