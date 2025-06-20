from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Ollama(id="mistral:latest"),
    tools=[YFinanceTools(stock_price=True)],
    instructions=[
        "Use tables to display data.",
        "Only include the table in your response. No other text.",
    ],
    markdown=True,
)
agent.print_response("What is the stock price of Apple?", stream=True)
