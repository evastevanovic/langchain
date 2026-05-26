
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient

# can also do from langchain_tavily import TavilySearch
# tools = [TavilySearch]

load_dotenv()


tavily = TavilyClient()

@tool
def search_query(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)


llm = ChatOllama(temperature = 0, model = "llama3.2:3b")

tools = [search_query]


agent = create_agent(llm, tools = tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()
