import os
from dotenv import load_dotenv
load_dotenv()
# 加载文档
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader(
    web_paths=["https://zh.wikipedia.org/wiki/黑神话：悟空"]
)
docs = loader.load()
# 文档切割
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_spliter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
split_docs = text_spliter.split_documents(docs)
# 嵌入生成向量索引
from langchain_community.embeddings import DashScopeEmbeddings
embed_model = DashScopeEmbeddings()
from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embedding=embed_model)
vector_store.add_documents(split_docs)
# 定义状态
from typing_extensions import TypedDict
from typing import List
from langchain_core.documents import Document
class State(TypedDict):
    question: str
    docs: List[Document]
    answer: str
# 定义检索
def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(
        query=state["question"],
        k=3,
    )
    return {"docs": retrieved_docs}
# 定义生成
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
def generate(state: State):
    from langchain_deepseek.chat_models import ChatDeepSeek
    llm = ChatDeepSeek(
        model="deepseek-chat",
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )
    docs_content = "\n\n".join([doc.page_content for doc in state["docs"]])
    resp = llm.invoke(template.format(
        context=docs_content,
        question=state["question"]
    ))
    return {"answer": resp.content}
# 流程编排
from langgraph.graph import START, StateGraph
graph = (
    StateGraph(State)
    .add_sequence([retrieve, generate])
    .add_edge(START, "retrieve")
    .compile()
)
question = "《黑神话：悟空》有哪些游戏场景？"
response = graph.invoke({"question": question})
print(response["answer"])