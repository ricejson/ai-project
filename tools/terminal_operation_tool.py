import subprocess
from langchain_core.tools import tool

@tool
def execute_terminal_command(command: str) -> str:
    """Execute a command in the terminal."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        output = result.stdout
        if result.stderr:
            output += result.stderr
        if result.returncode != 0:
            output += f"\nCommand execution failed with exit code: {result.returncode}"
        return output
    except subprocess.TimeoutExpired:
        return "Error: Command timed out after 30 seconds"
    except Exception as e:
        return f"Error executing command: {e}"




