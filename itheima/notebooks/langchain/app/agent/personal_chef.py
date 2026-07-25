# 导包
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, AIMessageChunk
from langchain_tavily import TavilySearch
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain.agents import create_agent
import sqlite3
import os
from common.logger import logger

# 读取环境变量
load_dotenv()
# 定义模型
base_url = os.getenv("DASHSCOPE_BASE_URL")
api_key = os.getenv("DASHSCOPE_API_KEY")
model = init_chat_model(
    model="qwen3.5-plus",
    model_provider="openai",
    base_url=base_url,
    api_key=api_key,
)
# 定义工具
search_tool = TavilySearch(
    max_results=5,
    topic="general"
)
# 定义记忆
connection = sqlite3.connect("./db/personal_chief.db", check_same_thread=False)
checkpointer = SqliteSaver(connection)
checkpointer.setup()
# 定义系统提示此
system_prompt = """
你是一名私人厨师。收到用户提供的食材照片或清单后，请按以下流程操作：
1.识别和评估食材：若用户提供照片，首先辨识所有可见食材。基于食材的外观状态，评估其新鲜度与可用量，整理出一份“当前可用食材清单”。
2.智能食谱检索：优先调用 web_search 工具，以“可用食材清单”为核心关键词，查找可行菜谱。
3.多维度评估与排序：从营养价值和制作难度两个维度对检索到的候选食谱进行量化打分，并根据得分排序，制作简单且营养丰富的排名靠前。
4.结构化方案输出：把排序后的食谱整理为一份结构清晰的建议报告，要包含食谱信息、得分、推荐理由、食谱的参考图片，帮助用户快速做出决策。

请严格按照流程，优先调用 web_search 工具搜索食谱，搜索不到的情况下才能自己发挥。
"""
# 定义agent
agent = create_agent(
    model=model,
    tools=[search_tool],
    checkpointer=checkpointer,
    system_prompt=system_prompt,
)

# 流式对话
async def search_recipes(prompt: str, image: str, thread_id: str):
    """调用agent搜索食谱"""
    logger.info(f"[用户]: {prompt}, image: {image}, thread_id: {thread_id}")
    try:
        if not image or image.strip() == "":
            message = HumanMessage(prompt)
        else:
            message = HumanMessage([
                {"type": "text", "text": prompt},
                {"type": "image", "url": image},
            ])
        # 调用agent
        for chunk, metadata in agent.stream(
            {"messages": [message]},
            {"configurable": {"thread_id": thread_id}},
            stream_mode="messages",
        ):
            if isinstance(chunk, AIMessageChunk) and chunk.content:
                yield chunk.content
    except Exception as e:
        logger.error(f"\n[错误]: {str(e)}")
        yield "信息检索失败，试试看手动输入食物列表？"

# 清空会话
def clear_messages(thread_id: str):
    """清空会话"""
    logger.info(f"清空历史消息，thread_id: {thread_id}")
    checkpointer.delete_thread(thread_id)

# 查询会话历史
def get_messages(thread_id: str) -> list[dict[str, str]]:
    """获取会话历史"""
    logger.info(f"获取历史消息，thread_id: {thread_id}")

    # 根据 thread_id 查询 cp
    cp = checkpointer.get({"configurable": {"thread_id": thread_id}})
    if not cp:
        return []

    # 安全获取 messages
    channel_values = cp.get("channel_values")
    if not channel_values:
        return []

    messages = channel_values.get("messages", [])
    if not messages:
        return []

    message_list = []
    for message in messages:
        if not message.content:
            continue
        if isinstance(message, HumanMessage):
            message_list.append({"role": "user", "content": message.content})
        elif isinstance(message, AIMessage):
            message_list.append({"role": "assistant", "content": message.content})

    return message_list