from langchain_core.messages import HumanMessage
from typing_extensions import Annotated
from langchain_core.tools import tool
from langchain_community.chat_models.tongyi import ChatTongyi

model = ChatTongyi(model="qwen3-max")

# 定义工具
@tool
def add(
    a: Annotated[int, ..., "第一个整数"],
    b: Annotated[int, ..., "第二个整数"]
) -> int:
    """两数相加"""
    return a + b

@tool
def multiply(
    a: Annotated[int, ..., "第一个整数"],
    b: Annotated[int, ..., "第二个整数"]
) -> int:
    """两数相乘"""
    return a * b

messages = [
    HumanMessage("1+3等于多少，2*3等于多少"),
]

# 绑定工具
model_with_tools = model.bind_tools(tools=[add, multiply])

# 调用工具
ai_msg = model_with_tools.invoke(input=messages)
messages.append(ai_msg)

for tool in ai_msg.tool_calls:
    tool_msg = {"add": add, "multiply": multiply}[tool["name"]].invoke(tool)
    messages.append(tool_msg)

print(model_with_tools.invoke(input=messages).content)
