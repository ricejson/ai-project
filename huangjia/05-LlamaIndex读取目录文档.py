import os

from llama_index.core import SimpleDirectoryReader

# 读取目录下所有文件
reader = SimpleDirectoryReader("./data/黑神话悟空")
docs = reader.load_data()
print(f"文档总数: {len(docs)}")
print(docs[0].text[:100])

# 读取目录下指定文件
reader = SimpleDirectoryReader(input_files=["./data/黑神话悟空/设定.txt"])
docs = reader.load_data()
print(f"文档总数: {len(docs)}")
print(docs[0].text[:100])

print(docs)
