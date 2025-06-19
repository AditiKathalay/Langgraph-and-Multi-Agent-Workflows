from langchain_core.tools import tool

@tool
def web_search(query: str) -> str:
    """Search the web using DuckDuckGo."""
    search = DuckDuckGoSearchRun()
    return search.run(query)