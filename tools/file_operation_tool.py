import os
from langchain_core.tools import tool

# root directory
BASE_DIR = "./files"

@tool
def read_file(file_name: str) -> str:
    """Read content from a file"""
    file_path = os.path.join(BASE_DIR, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

@tool
def write_file(file_name: str, content: str) -> str:
    """Write content to a file"""
    file_path = os.path.join(BASE_DIR, file_name)
    try:
        os.makedirs(BASE_DIR, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            return f"File written successfully to: {file_path}"
    except Exception as e:
        return f"Error writing to file: {e}"



