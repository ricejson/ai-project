import os
import requests
from langchain_core.tools import tool

BASE_DIR = "./downloads/"

@tool
def download_resource(url: str, file_name: str) -> str:
    """Download a resource from a given URL."""
    file_path = os.path.join(BASE_DIR, file_name)
    try:
        os.makedirs(BASE_DIR, exist_ok=True)
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return f"Resource downloaded successfully to: {file_path}"
    except Exception as e:
        return f"Error downloading resource: {e}"


