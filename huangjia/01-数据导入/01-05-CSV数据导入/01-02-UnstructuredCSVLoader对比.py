from langchain_community.document_loaders import UnstructuredCSVLoader

docs = UnstructuredCSVLoader(file_path="../../data/黑神话悟空/黑神话悟空.csv").load()

print(docs)