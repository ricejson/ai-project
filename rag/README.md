
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

## langchain提供的三种提示词模板
目前 langchain 支持三种提示词模板：
1. PromptTemplate 通用提示词模板
2. FewShotPromptTemplate 少样本提示词模板
3. ChatPromptTemplate 聊天提示词模板

### 注意点：
* 三种对象都同时具有 invoke 方法（继承runnable接口）和 format 方法（继承BasePromptTemplate）
  1. invoke 方法返回PromptValue对象，format 方法返回字符串
  2. invoke 方法入参传递字典对象进行注入，format 方法则是通过=参数赋值
  3. invoke 方法不仅支持{}注入，还支持 MessagesPlaceHolder 注入用于ChatPromptTemplate

## langchain 提供的chain机制
chain 是 langchain 框架提供的把多个组件串联起来协同工作的方式，前一个组件的输出结果会作为下一个组件的输入
* 使用方式：通过 | 运算符
* 组成 chain 的各个组件必须实现 Runnable 接口
* chain 通过 Runnable 接口的 invoke or stream 方法进行触发