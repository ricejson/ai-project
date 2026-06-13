from unstructured.partition.pptx import partition_pptx

ppt_elements = partition_pptx(filename="../../data/黑神话悟空/黑神话悟空.pptx")

# 构建 Langchain 中的文档
from langchain_core.documents import Document
docs = [
    Document(
        page_content=element.text,
        metadataa={"source": "../../data/黑神话悟空/黑神话悟空.pptx"}
    )
    for element in ppt_elements
]
print(docs)