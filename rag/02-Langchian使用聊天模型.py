# 导千问的包
from langchain_community.chat_models.tongyi import ChatTongyi

# 创建聊天模型对象
chat = ChatTongyi(model="qwen3-max")

# 阻塞式获取结果
res = chat.invoke(input="你是谁能做什么？")

# 打印结果
print(res.content)