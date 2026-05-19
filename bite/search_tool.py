from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

# 使用 langchain-tavily 接入搜索工具
model = ChatTongyi(model="qwen3-max")

# 创建搜索工具
search_tool = TavilySearch(max_results=2, tavily_api_key = "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")

# 绑定工具
model_with_tools = model.bind_tools(tools=[search_tool])

messages = [
    HumanMessage("今天北京新澄海大厦天气怎么样？")
]

# 调用工具
ai_msg = model_with_tools.invoke(input=messages)
messages.append(ai_msg)
tool_msg = search_tool.invoke(ai_msg.tool_calls[0])
messages.append(tool_msg)

print(model_with_tools.invoke(input=messages).content)
