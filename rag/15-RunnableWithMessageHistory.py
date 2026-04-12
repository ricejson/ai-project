# 导包
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

background_prompt = PromptTemplate.from_template("你需要根据历史会话回答问题，历史会话：{history}, 用户提问：{input}，请回答")
question_prompt = PromptTemplate.from_template("一共有多少只小动物？")

model = ChatTongyi(model="qwen3-max")

str_parser = StrOutputParser()

base_chain = background_prompt | model | str_parser

store = {}

def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


history_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="input",
    history_messages_key="history",
)

if __name__ == "__main__":
    session_config = {
        "configurable": {
            "session_id": "user_01"
        }
    }
    history_chain.invoke({"input": "小王有1只猫"}, session_config)
    history_chain.invoke({"input": "小李有2只狗"}, session_config)
    history_chain.invoke({"input": "小张有1只小仓鼠"}, session_config)
    for chunk in history_chain.invoke({"input": "一共出现了多少只动物？"}, session_config):
        print(chunk, end="", flush=True)

