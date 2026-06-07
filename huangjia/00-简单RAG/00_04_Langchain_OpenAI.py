# 加载文档
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader(
    web_paths="https://zh.wikipedia.org/wiki/黑神话：悟空",
)
docs = loader.load()
# 文本分块
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_spliter = RecursiveCharacterTextSplitter(
    chunk_size=1000, # 每个文本块的最大字符数
    chunk_overlap=200 # 相邻文本块的重复部分
)
all_splits = text_spliter.split_documents(docs)
# 设置嵌入模型
from langchain_openai import OpenAIEmbeddings
embed_model = OpenAIEmbeddings()
# 创建向量存储
from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embed_model)
vector_store.add_documents(all_splits)

# 构建用户查询
question = "《黑神话：悟空》有哪些游戏场景？"

# 在向量存储中搜索，并准备上下文内容
retrieved_docs = vector_store.similarity_search(
    question,
    k=3
)

docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

# 构建提示词模板
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template(
    """
    基于以下上下文，回答问题。如果上下文中没有相关信息，
    请说"我无法从提供的上下文中找到相关信息"。
    上下文: {context}
    问题: {question}
    回答:
    """
)
# 生成回答
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo")
answer = llm.invoke(prompt.format(question=question, context=docs_content))
print(answer.content)