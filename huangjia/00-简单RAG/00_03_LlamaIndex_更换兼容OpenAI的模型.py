# 更换嵌入模型和生成模型 pip install llama-index-llms-deepseek
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.deepseek import DeepSeek
from dotenv import load_dotenv
import os

# 创建嵌入模型
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-zh",
)

documents = SimpleDirectoryReader(input_files=["../data/黑神话悟空/设定.txt"]).load_data()

index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

load_dotenv()

# 创建 llm
llm = DeepSeek(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 构建查询引擎
query_engine = index.as_query_engine(llm=llm)

# 查询
print(query_engine.query("黑神话悟空中有哪些战斗工具?"))
