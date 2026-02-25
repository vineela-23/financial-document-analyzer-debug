from crewai import Agent
from langchain_openai import ChatOpenAI
from tools import read_financial_document


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)


financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide accurate financial analysis based strictly on the provided document and user query: {query}",
    backstory=(
        "You are a certified financial analyst with 15 years of experience in "
        "financial statement analysis and equity research. "
        "You provide factual, evidence-based insights. "
        "You never fabricate data."
    ),
    tools=[],
    llm=llm,
    verbose=True,
    allow_delegation=False
)