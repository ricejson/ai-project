# 导包
from langchain_community.embeddings import DashScopeEmbeddings

# 创建嵌入模型对象（默认使用text-embedding-v1）
embeddings = DashScopeEmbeddings()

# 转化为向量
res = embeddings.embed_query("我喜欢你")
print(res)
batch_res = embeddings.embed_documents(["我稀饭你", "晚上吃什么"])
print(batch_res)