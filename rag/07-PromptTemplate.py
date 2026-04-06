# 导包
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

# 创建提示词模板对象
template = PromptTemplate.from_template("我的邻居姓{name}, 生了个{gender}，请你帮取个名字，输出保持精简，省略多余内容")

# 格式化提示词
prompt = template.format(name= "王", gender="女儿")

# 对话
model = ChatTongyi(model="qwen3-max")

res = model.invoke(input=prompt)

print(res.content)