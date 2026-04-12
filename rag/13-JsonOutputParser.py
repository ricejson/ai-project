# 导包
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

first_prompt = PromptTemplate.from_template("隔壁朋友姓:{lastname}，生了个{gender}，请你帮取个名字，输出格式为JSON字符串，其中key为name，value为名字")

second_prompt = PromptTemplate.from_template("请你解释一下姓名为：{name}的含义")

model = ChatTongyi(model="qwen3-max")

json_parser = JsonOutputParser()
str_parser = StrOutputParser()

chain = first_prompt | model | json_parser| second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "张", "gender": "女儿"}):
    print(chunk, end="", flush=True)