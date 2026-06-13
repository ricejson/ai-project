# pip install jq
from langchain_community.document_loaders import JSONLoader
# 提取并打印主角信息
print("1. 主角信息")
main_loader = JSONLoader(
    file_path="../../data/黑神话悟空/人物角色.json",
    jq_schema='.mainCharacter | "姓名: " + .name + "，背景: " + .backstory',
    text_content=True
)
main_char = main_loader.load()
print(main_char)
# 提取并打印支持角色信息
support_loader = JSONLoader(
    file_path="../../data/黑神话悟空/人物角色.json",
    jq_schema='.supportCharacters[] | "姓名: " + .name + "，背景: " + .background',
    text_content=True
)

support_char = support_loader.load()
print(support_char)
