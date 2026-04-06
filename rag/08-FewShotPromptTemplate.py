# 导包
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

# 样例提示词
example_prompt = PromptTemplate.from_template("单词：{word}, 反义词：{antiword}")

# 样例数据
example_data = [
    {
        "word": "大",
        "antiword": "小"
    },
    {
        "word": "左",
        "antiword": "右"
    }
]

# 创建模板对象
template = FewShotPromptTemplate(
    example_prompt=example_prompt, # 样例提示词模板
    examples=example_data, # 样例数据
    prefix="帮我生成对应单词的反义词，参考样例如下:", # 前缀
    suffix="请告诉我{word}的反义词：", # 后缀
    input_variables=["word"] # 待注入的变量列表
)

# 创建提示词
prompt = template.invoke({"word": "美"}).to_string()
model = ChatTongyi(model="qwen3-max")

# 获取结果
print(model.invoke(input=prompt).content)

