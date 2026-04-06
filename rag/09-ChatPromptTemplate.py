# 导包
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

history_data = [
    ("human", "帮我写一首唐诗"),
    ("ai", "单车欲问边，属国过居延。征蓬出汉塞，归雁入胡天。大漠孤烟直，长河落日圆。萧关逢候骑，都护在燕然。")
]

# 创建提示词模板
template = ChatPromptTemplate.from_messages([
    ("system", "你是一个边塞诗人"),
    MessagesPlaceholder("history"),
    ("human", "帮我写一首唐诗")
])

prompt = template.invoke({"history": history_data}).to_string()

model = ChatTongyi(model="qwen3-max")

# 输出结果
print(prompt)
print(model.invoke(input=prompt).content)
