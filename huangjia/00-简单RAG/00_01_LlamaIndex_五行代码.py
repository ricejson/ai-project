# 使用llama-index 初识 RAG，默认情况使用的是 OpenAI 的嵌入模型和生成模型
# 导入相关包
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
# 加载数据形成文档
documents = SimpleDirectoryReader(input_files=["../data/黑神话悟空/设定.txt"]).load_data()
# 基于文档构建索引
index = VectorStoreIndex.from_documents(documents)
# 基于索引创建问答引擎
query_engine = index.as_query_engine()
# 基于问答引擎开始问答
print(query_engine.query("《黑神话悟空》中一共有哪些战斗工具？"))