# pip install unstructured
import os
from langchain_community.document_loaders import DirectoryLoader

script_dir = os.path.dirname(__file__)
data_dir = os.path.join(script_dir, "./data/黑神话悟空")

loader = DirectoryLoader(
    data_dir,
    glob="**/*.txt",
    use_multithreading=True,
    show_progress=True,
)

docs = loader.load()

print(f"文档数：{len(docs)}")  # 输出文档总数
print(docs[0])  # 输出第一个文档