import asyncio
import os
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

load_dotenv()

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")

async def main():

    llm = ChatOpenAI(
        api_key=DASHSCOPE_API_KEY,
        model="qwen-plus",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )

    client = MultiServerMCPClient(
        {
            "image-search": {
                "transport": "stdio",
                "command": "python",
                "args": ["../mcp-server/search-image.py"]
            }
        }
    )

    tools = await client.get_tools()

    agent = create_agent(llm, tools)

    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "please help me search some images about a cute dog"}]}
    )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())

