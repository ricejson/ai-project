# 导包
from langchain_community.chat_models.tongyi import ChatTongyi

# 创建聊天模型对象
chat = ChatTongyi(model="qwen3-max")

# 获取流式结果
res = chat.stream(input="你是谁能做什么？")

# 迭代器打印
for chunk in res:
    print(chunk.content, end="", flush=True)