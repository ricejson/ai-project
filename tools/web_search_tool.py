import requests
import os
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()

SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")
url = "https://www.searchapi.io/api/v1/search"

@tool
def web_search(query: str) -> str:
    """Search information from Baidu search engine"""
    params = {
        "q": query,
        "engine": "baidu",
        "api_key": SEARCH_API_KEY,
    }
    try:
        resp = requests.get(url, params=params)
        return resp.text
    except Exception as e:
        return f"Error occurred: {e}"