# 加载文档
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader(
    web_paths=["https://zh.wikipedia.org/wiki/黑神话：悟空"],
)
docs = loader.load()
# 文档分割
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
split_docs = text_splitter.split_documents(docs)
# 嵌入模型
from langchain_community.embeddings import DashScopeEmbeddings
embed_model = DashScopeEmbeddings()
# 向量存储嵌入索引
from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embedding=embed_model)
vector_store.add_documents(split_docs)
# 用户提问
question = "《黑神话：悟空》有哪些游戏场景？"
# 检索
retrieved_docs = vector_store.similarity_search(
    query=question,
    k = 3,
)
# 生成
from langchain_core.prompts import ChatPromptTemplate
template = ChatPromptTemplate.from_template(
    """
    基于以下上下文，回答问题。如果上下文中没有相关信息，
    请说"我无法从提供的上下文中找到相关信息"。
    上下文: {context}
    问题: {question}
    回答:
    """
)
prompt = template.format(
    question=question,
    context="\n\n".join([doc.page_content for doc in retrieved_docs]),
)
from langchain_deepseek.chat_models import ChatDeepSeek
from dotenv import load_dotenv
import os
load_dotenv()
chat = ChatDeepSeek(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)
print(chat.invoke(prompt).content)
