# 通过 HuggingFace 导入其他开源嵌入模型 pip install llama-index-embeddings-huggingface
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
# 加载文档
documents = SimpleDirectoryReader(input_files=["../data/黑神话悟空/设定.txt"]).load_data()
# 加载本地嵌入模型
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-zh"
)
# 构建索引时指定嵌入模型
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
# 创建问答引擎
query_engine = index.as_query_engine()
# 获取问答结果
print(query_engine.query("黑神话悟空中有哪些战斗工具?"))

