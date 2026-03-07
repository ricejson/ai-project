# 导入依赖
# pip install llama-index llama-index-embeddings-dashscope llama-index-llms-openai-like
import os
from pathlib import Path 
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.dashscope import DashScopeEmbedding, DashScopeTextEmbeddingModels
from llama_index.llms.openai_like import OpenAILike

load_dotenv()

# 解析当前脚本所在路径
script_path = Path(__file__).resolve()
# 获取父级目录
dir_path = script_path.parent
# 文档对应文件路径
doc_path = dir_path / "docs"

# 解析文件内容为文档
documents = SimpleDirectoryReader(str(doc_path)).load_data()
print("正在创建索引...")
# 加载文档为向量索引
index = VectorStoreIndex.from_documents(
    documents=documents,
    # 阿里云百炼嵌入模型
    embed_model=DashScopeEmbedding(
        model_name = DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V2
    )
)
print("正在创建提问引擎...")
query_engine = index.as_query_engine(
    # 流式输出
    streaming=True,
    llm=OpenAILike(
        model="qwen-plus",
        api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        is_chat_model=True
    )
)
print("正在生成回复...")
streaming_response = query_engine.query('我们公司项目管理应该用什么工具')
print("回答是：")
streaming_response.print_response_stream()