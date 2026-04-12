# 导包
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

first_prompt = PromptTemplate.from_template("隔壁朋友姓:{lastname}，生了个{gender}，请你帮取个名字，不要输出多余的内容")
second_prompt = PromptTemplate.from_template("请你解释一下名字为{name}的含义")

my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})

model = ChatTongyi(model="qwen3-max")

str_parser = StrOutputParser()

chain = first_prompt | model | my_func | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "张", "gender": "女儿"}):
    print(chunk, end="", flush=True)
