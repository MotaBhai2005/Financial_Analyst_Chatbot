from langchain.tools import tool
from duckduckgo_search import DDGS

from schema import NewsInput


@tool(args_schema=NewsInput)
def get_company_news(company: str) -> str:
    """
    Fetch the latest news articles for a given company using DuckDuckGo Search.
    """

    try:
        with DDGS() as ddgs:
            results = list(
                ddgs.text(
                    f"{company} latest stock news",
                    max_results=5
                )
            )

        if not results:
            return f"No recent news found for {company}."

        formatted_news = []

        for i, article in enumerate(results, start=1):

            title = article.get("title", "No Title")
            summary = article.get("body", "No Summary Available")
            link = article.get("href", "No Link")

            formatted_news.append(
                f"""
News {i}
Title   : {title}
Summary : {summary}
Link    : {link}
"""
            )

        return "\n".join(formatted_news)

    except Exception as e:
        return f"Error fetching news: {str(e)}"