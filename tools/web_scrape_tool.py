import requests
from langchain_core.tools import tool

@tool
def scrape_web_page(url: str) -> str:
    """Scrape the content of a web page."""
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        return f"Error scraping web page: {e}"
