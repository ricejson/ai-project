# 访问多个 MCP 服务器
from dotenv import load_dotenv
import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

os.environ.pop("http_proxy", None)
os.environ.pop("https_proxy", None)
os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)

load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "stdio",
                "command": "python",
                "args": ["07-mcp-server-math.py"]
            },
            "weather": {
                "transport": "streamable-http",
                "url": "http://localhost:8000/mcp",
                "headers": {
                    "accept": "application/json, text/event-stream"
                }
            }
        }
    )

    tools = await client.get_tools()

    llm = ChatOpenAI(
        model="qwen-plus",
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
    agent = create_agent(llm, tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    )
    print(math_response)
    print(weather_response)


if __name__ == "__main__":
    asyncio.run(main())