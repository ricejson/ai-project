# 导包
from langchain_community.chat_models.tongyi import ChatTongyi

# 创建聊天对象
chat = ChatTongyi(model="qwen3-max")

# 创建消息列表
messages = [
    ("system", "你是一个边塞诗人"),
    ("human", "帮我写一首唐诗"),
    ("ai", "单车欲问边，属国过居延。征蓬出汉塞，归雁入胡天。大漠孤烟直，长河落日圆。萧关逢候骑，都护在燕然。"),
    ("human", "请参考之前写的示例，再写一首唐诗")
]

# 打印结果
for chunk in chat.stream(input=messages):
    print(chunk.content, end="", flush=True)