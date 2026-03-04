import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
import datetime

load_dotenv()
api_key = os.getenv("V3_API_KEY")

# ===== 1. 初始化 LLM （大语言模型）=====
# langchain 特点：整合多种大模型，提供统一的接口
llm = ChatOpenAI(
    base_url="https://api.vveai.com/v1",
    api_key=api_key,
    model="gpt-4o",
    temperature=0.7
)

# ===== 2. LLMChain Prompt -> LLM -> 输出链 =====
def demo_llm_chain():
    print("=" * 50)
    print("🔗 LLMChain 演示：Prompt → LLM → 输出链")
    print("=" * 50)
    # 创建提示词模板
    prompt_template = PromptTemplate(
        input_variables=["style", "topic"],
        template="""
        请以{style}的风格，写一段关于{topic}的介绍。
        要求：简洁明了，不超过100字。
        """
    )
    chain = prompt_template | llm
    # 执行链
    result = chain.invoke({"style": "科普", "topic": "人工智能"})
    print(f"📝 LLMChain 输出：\n{result.content}\n")
    return result.content


# ===== 3. tools 工具系统 =====

def get_current_time(query: str) -> str:
    """获取当前时间的工具函数"""
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"当前时间是：{now}"

def calculate_simple(expression: str) -> str:
    """简单计算器工具"""
    try:
        allowed_chars = set[str]('0123456789+-*/.() ')
        if all(c in allowed_chars for c in expression):
            result = eval(expression)
            return f"计算结果：{expression} = {result}"
        else:
            return "错误：包含不允许的字符"
    except Exception as e:
        return f"计算错误：{str(e)}"


# langchain 特点：统一的工具接口定义
tools = [
    Tool(
        name="get_time",
        description="获取当前的日期和时间信息",
        func=get_current_time
    ),
    Tool(
        name="calculator",
        description="执行简单的数学计算，如加减乘除运算",
        func=calculate_simple
    )
]

def demo_tools():
    """演示 tools 工具系统"""
    print("=" * 50)
    print("🔧 Tools 演示：工具系统")
    print("=" * 50)
    for tool in tools:
        print(f"🔧 工具名称：{tool.name}")
        print(f"📖 工具描述：{tool.description}")
        # 测试工具
        if tool.name == "get_time":
            result = tool.run("现在几点了？")
        elif tool.name == "calculator":
            result = tool.run("10 + 5 * 2")
        print(f"🔍 工具测试结果：{result}\n")

# ===== 4. 简化版 Agents =====
def demo_simple_agents():
    """
    演示简化版 Agents：手动工具选择和执行
    LangChain 特点：工具集成和智能选择（这里用简化版演示概念）
    """
    print("=" * 50)
    print("🤖 简化版 Agents 演示：工具选择与执行")
    print("=" * 50)
    # 创建工具选择提示词
    tool_selection_prompt = ChatPromptTemplate.from_messages([
        ("system", """你是一个智能助手，可以使用以下工具
        1. get_time - 获取当前时间
        2. calculate - 执行数学计算
        请分析用户问题，选择合适的工具并说明原因。
        只回答工具名称和原因，格式：工具名称｜原因"""),
        ("human", "{question}")
    ])
    tool_chain = tool_selection_prompt | llm

    test_questions = [
        "现在几点了？",
        "帮我计算 15 * 8 + 20",
        "今天是什么日期？"
    ]

    for question in test_questions:
        print(f"👤 用户问题：{question}")
        # 1. 工具选择
        selection_result = tool_chain.invoke({"question": question})
        print(f"🧠 工具选择：{selection_result.content}")
        # 2. 执行工具（简化版手动执行）
        if "get_time" in selection_result.content.lower():
            result = get_current_time(question)
        elif "calculate" in selection_result.content.lower():
            # 提取数学表达式（简化处理）
            if "15 * 8 + 20" in question:
                result = calculate_simple("15 * 8 + 20")
            else:
                result = "需要具体的数学表达式"
        else:
            result = "未找到合适的工具"
        print(f"🔍 工具执行结果：{result}\n")

# ===== 5. Memory 记忆系统 =====
def demo_memeory():
    """
    演示 Memory：对话记忆管理
    LangChain 特点：自动管理对话历史
    """
    print("=" * 50)
    print("🧠 Memory 演示：记忆系统")
    print("=" * 50)
    # 简化版记忆管理方式
    conversation_history = []
    # 带有记忆的提示词模板
    memory_prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个友好的助手，能够记住之前的对话内容，以下是对话历史:{history}"),
        ("human", "{input}")]
    )

    memory_chain = memory_prompt | llm

    # 模拟多轮对话
    conversations = [
        "我叫张三，今年25岁",
        "我喜欢编程和阅读",
        "你还记得我的名字吗？",
        "我的爱好是什么？"
    ]

    for i, user_prompt in enumerate[str](conversations, 1):
        print(f"👤 第{i}轮对话：{user_prompt}")

        # 拼接对话历史
        history_str = "\n".join([f"用户: {h['user']}\n助手: {h['assistant']}" for h in conversation_history])
        
        # 获取回复
        response = memory_chain.invoke({
            "history": history_str,
            "input": user_prompt
        })
        
        # 助手回复
        print(f"🤖 助手回复：{response.content}\n")
        
        # 更新对话历史
        conversation_history.append({
            "user": user_prompt,
            "assistant": response.content
        })
        
        # 显示当前记忆内容
        print(f"💭 当前记忆：{len(conversation_history)} 轮对话")
        print("-" * 30)

# ===== 6. LCEL LangChain Expression Language =====
def demo_lcel():
    """
    演示LECE: LangChain 0.3 新特性，链式组合语法
    """
    print("=" * 50)
    print("🔗 LCEL 演示：LangChain Expression Language")
    print("=" * 50)
    # LCEL 语法：使用 | 管道符组合组件
    prompt = PromptTemplate.from_template("请用{language}语言解释什么是{concept}")
    # 创建链
    chain = prompt | llm
    # 调用链
    result = chain.invoke({
        "language": "简单易懂的中文",
        "concept": "区块链"
    })
    print(f"📝 LCEL 链式调用结果：\n{result.content}\n")
    # 演示更复杂的链结构
    from langchain_core.output_parsers import StrOutputParser
    # 创建输出解析器
    output_parser = StrOutputParser()
    # 更复杂的链
    complex_chain = prompt | llm | output_parser
    result2 = complex_chain.invoke({
        "language": "技术术语",
        "concept": "机器学习"
    })
    print(f"📝 复杂 LCEL 链结果：\n{result2}\n")

def main():
    """主函数：依次演示各个核心组件"""
    print("🚀 LangChain 0.3 核心组件实战演示")
    print("基于 OpenAI API 的完整示例（兼容版本）\n")
    try:
        demo_llm_chain()
        demo_tools()
        demo_simple_agents()
        demo_memeory()
        demo_lcel()
    except Exception as e:
        print(f"❌ 演示过程中出现错误：{str(e)}")
        print("请检查 API 密钥和网络连接")

if __name__ == "__main__":
    main()