# 导包
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template("隔壁朋友姓:{lastname}，生了个{gender}，请你帮取个名字，不要输出多余内容")

model = ChatTongyi(model="qwen3-max")

parser = StrOutputParser()

chain = prompt | model | parser | model

res = chain.invoke({"lastname": "张", "gender": "女儿"}).content
print(res)