import os
import requests
from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
PEXELS_URL = "https://api.pexels.com/v1/search"
PEXELS_PER_PAGE = 5

mcp = FastMCP("search image")

@mcp.tool()
def search_image(query: str) -> str:
    """Search image from web"""
    if not PEXELS_API_KEY:
        return ""

    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": query, "per_page": PEXELS_PER_PAGE}

    images_urls = request_pexels(PEXELS_URL, headers, params)
    if images_urls:
        return ",".join(images_urls)
    else:
        return ""


def request_pexels(url: str, headers: dict, params: dict) -> list[str]:
    """Request image from pexels"""
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if data.get("photos"):
            return [photo["src"]["original"] for photo in data["photos"]]
        else:
            return []
    except requests.exceptions.RequestException as e:
        return []


if __name__ == "__main__":
    mcp.run(transport = "stdio")