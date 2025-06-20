from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.thinking import ThinkingTools
from agno.tools.yfinance import YFinanceTools

reasoning_agent = Agent(
    model=Ollama(id="mistral:latest"),
    tools=[
        ThinkingTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions="Use tables where possible",
    markdown=True,
)

if __name__ == "__main__":
    reasoning_agent.print_response(
        "Write a report on NVDA. Only the report, no other text.",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
