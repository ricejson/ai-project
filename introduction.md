# AI Project 项目介绍

## 项目概述

这是一个 AI 开发学习项目，主要涵盖了 OpenAI API、LangChain、LlamaIndex 和 MCP（Model Context Protocol）等主流 AI 开发框架的实践示例。

## 项目结构

```
ai-project/
├── 02-openaiAPI.py              # OpenAI API 基础调用示例
├── 05-langchain.py              # LangChain 核心组件演示
├── 06-llamaindex.py             # LlamaIndex RAG 检索增强生成示例
├── 07-mcp-client.py             # MCP 客户端：多服务器连接示例
├── 07-mcp-server-math.py        # MCP 数学计算服务器
├── 07-mcp-server-weather.py    # MCP 天气查询服务器
├── test.py                      # 测试文件
├── requirements.txt             # 项目依赖
├── .env                         # 环境变量配置（API Keys）
├── README.md                    # 项目说明文档
├── docs/                        # 文档目录
│   └── 项目管理工具介绍.txt
├── tools/                       # 自定义工具集
│   ├── web_search_tool.py       # 网络搜索工具（百度搜索）
│   ├── web_scrape_tool.py       # 网页爬取工具
│   ├── file_operation_tool.py   # 文件操作工具
│   ├── download_resource_tool.py # 资源下载工具
│   ├── terminal_operation_tool.py # 终端操作工具
│   └── generate_pdf_tool.py     # PDF 生成工具
└── mcp-image-search/            # MCP 图片搜索项目
    ├── mcp-server/              # MCP 服务端
    │   └── search-image.py      # 图片搜索服务（Pexels API）
    └── mcp-client/              # MCP 客户端
        └── search-image.py      # 图片搜索客户端
```

## 核心模块说明

### 1. OpenAI API 基础（02-openaiAPI.py）
- 演示如何使用 OpenAI SDK 进行基础的 API 调用
- 配置自定义 API 端点（base_url）
- 简单的对话生成示例

### 2. LangChain 框架（05-langchain.py）
完整演示 LangChain 0.3 的核心组件：

- **LLMChain**：提示词模板 → LLM → 输出链
- **Tools 工具系统**：
  - 时间查询工具
  - 简单计算器工具
- **Agents 代理**：智能工具选择与执行
- **Memory 记忆系统**：对话历史管理
- **LCEL 语法**：LangChain Expression Language 链式组合

### 3. LlamaIndex RAG（06-llamaindex.py）
- 文档加载与向量化索引
- 使用阿里云百炼嵌入模型（DashScope Embedding）
- 流式查询引擎
- 基于文档的问答系统

### 4. MCP 协议实现

#### MCP 服务器
- **math 服务器**：数学计算服务
- **weather 服务器**：天气查询服务
- **image-search 服务器**：图片搜索服务（Pexels API）

#### MCP 客户端（07-mcp-client.py）
- 多服务器连接管理
- 支持 stdio 和 HTTP 两种传输协议
- 与 LangChain Agent 集成

### 5. 自定义工具集（tools/）
提供了一系列实用工具：

- **web_search_tool.py**：百度搜索 API 集成
- **web_scrape_tool.py**：网页内容抓取
- **file_operation_tool.py**：文件读写操作
- **download_resource_tool.py**：网络资源下载
- **terminal_operation_tool.py**：终端命令执行
- **generate_pdf_tool.py**：PDF 文档生成

## 技术栈

### 核心依赖
- **openai** (1.98.0)：OpenAI API SDK
- **langchain** (0.3.27)：LangChain 核心框架
- **langchain-community** (0.3.27)：社区扩展
- **langchain-core** (0.3.72)：核心组件
- **langchain-openai** (0.3.28)：OpenAI 集成
- **llama-index**：RAG 检索增强生成框架
- **fastmcp**：MCP 服务器快速开发框架
- **python-dotenv** (1.1.1)：环境变量管理

### 外部 API
- OpenAI Compatible API（vveai.com）
- 阿里云百炼 DashScope API
- Pexels 图片搜索 API
- SearchAPI 百度搜索 API

## 环境配置

需要在 `.env` 文件中配置以下 API Keys：

```env
V3_API_KEY=your_openai_api_key
DASHSCOPE_API_KEY=your_dashscope_api_key
PEXELS_API_KEY=your_pexels_api_key
SEARCH_API_KEY=your_search_api_key
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 主要特性

1. **多框架集成**：OpenAI、LangChain、LlamaIndex 三大框架实战
2. **MCP 协议**：实现了完整的 MCP 服务器和客户端
3. **工具生态**：丰富的自定义工具集
4. **RAG 应用**：基于文档的检索增强生成
5. **Agent 系统**：智能工具选择与执行
6. **流式输出**：支持流式响应

## 学习路径

1. 从 `02-openaiAPI.py` 开始了解基础 API 调用
2. 学习 `05-langchain.py` 掌握 LangChain 核心概念
3. 通过 `06-llamaindex.py` 理解 RAG 应用
4. 探索 MCP 协议的服务器和客户端实现
5. 研究 tools 目录下的自定义工具开发

## 注意事项

- 确保所有 API Keys 已正确配置
- MCP 服务器需要单独启动
- 部分功能需要网络连接
- 建议使用 Python 3.9+ 版本
