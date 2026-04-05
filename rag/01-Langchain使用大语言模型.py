# 导入千问大模型包
from langchain_community.llms.tongyi import Tongyi

# 创建大模型对象
llm = Tongyi(model="qwen-max")

# 一次性阻塞获取模型返回内容
res = llm.invoke(input="你是谁能做什么？")

# 打印内容
print(res)