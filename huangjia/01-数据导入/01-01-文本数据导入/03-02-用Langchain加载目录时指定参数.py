# pip install tqdm（show_progress使用）
import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader

script_dir = os.path.dirname(__file__)
data_dir = os.path.join(script_dir, "../../data/黑神话悟空")

loader = DirectoryLoader(
    data_dir,
    # glob="**/*.md", # 匹配指定文件
    show_progress=True, # 展示进度条
    use_multithreading=True, # 多线程
    loader_cls=TextLoader, # 指定文本读取器
    silent_errors=True  # 静默处理错误（例如文本读取器无法解析）
)

docs = loader.load()

print(f"文档数：{len(docs)}")  # 输出文档总数
print(docs[0])  # 输出第一个文档