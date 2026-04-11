# 导包
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

# 创建模板
template = PromptTemplate.from_template("隔壁好友姓:{name}，生了个{gender}，请你帮取个名字，省略多余的内容，直接输出结果")

# 创建模型
model = ChatTongyi(model="qwen3-max")

# 组成 chain
chain = template | model

# 触发
for chunk in chain.stream({"name": "张", "gender": "女儿"}):
    print(chunk.content, end="", flush=True)
