from langchain_community.document_loaders import UnstructuredMarkdownLoader

markdown_path = "../../data/黑神话悟空/黑悟空版本介绍.md"
loader = UnstructuredMarkdownLoader(
    file_path=markdown_path,
    mode="elements" # 拆分每个元素作为一个单独文档
)

docs = loader.load()
print(docs)