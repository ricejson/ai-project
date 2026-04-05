
## 环境准备
* conda 创建新环境：itheima_rag
* 安装 langchain 开发环境：pip install langchain langchain_community langchain_ollama dashscope chromadb

## langchain-models
目前 langchain 支持三种模型：
1. LLMs（大语言模型）生成文本模型
2. Chat-Model（聊天模型），大语言模型中专门用于对话聊天场景
3. Embedding（嵌入模型）：将文本中的语义特征转化为向量表达

### 注意点：
* langchain中有两种获取结果的方式：1、invoke阻塞式调用，2、stream 流式输出返回
* langchain中有两种定义消息的方式：
  1. 使用对应类：AIMessage、HumanMessage、SystemMessage，
  2. 用元组()，动态运行时会替换为方式一，但是能够进行模版提示词替换
* langchain提供了两种嵌入模型API：1、embed_query 单次转换，2、embed_documents 批量转换
