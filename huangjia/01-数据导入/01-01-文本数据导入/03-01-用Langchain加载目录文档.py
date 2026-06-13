# pip install unstructured
# pip install "unstructured[md]"
# pip install "unstructured[image]"
# brew install tesseract tesseract-lang
# pip install pytesseract
import os
from langchain_community.document_loaders import DirectoryLoader

script_dir = os.path.dirname(__file__)
data_dir = os.path.join(script_dir, "../../data/黑神话悟空")

docs = DirectoryLoader(data_dir).load()

print(f"文档总数: {len(docs)}")
print(f"第一个文档内容:{docs[0]}")