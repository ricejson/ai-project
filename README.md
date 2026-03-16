
## conda 常见命令

### conda 相关
* conda env list：查看所有环境
* conda create -n myenv python=3.10：创建虚拟环境
* conda activate myenv：激活虚拟环境

### pip 相关
* pip install -r requirements.txt：安装依赖

## LangChain

### LangChain 核心概念
* PromptTemplate：提示词模板
* LLM：大语言模型
* Chain：链，可以将多个组件串联
* Memory：存储
* VectorStore：向量数据库存储
* DocumentLoader：文档加载，切块
* Agent：封装的代理实现，例如 Tool

### LangChain 核心组件
* IO输入输出组件：包含Input（prompt）、Output（parser）、LLM
* RAG：Retrieval-Augmented Generation，检索增强生成
* Tool：工具组件
* Memory：存储组件
* Callback：回调组件
* LCEL：LangChain Expression Language，| 链式语法

### LangChain MCP
1. 安装依赖：pip install langchain-mcp-adapters

