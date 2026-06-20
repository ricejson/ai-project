from langchain_community.document_loaders import CSVLoader
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../data/黑神话悟空/黑神话悟空.csv")

loader = CSVLoader(
    file_path=file_path,
    csv_args={
        "delimiter": ",",
        "quotechar": "|",
        "fieldnames": ["种类", "名称", "说明", "等级"], # 替换 field
    },
    source_column="Name" # 替换 metadata 中的 source 为实际列值
)

docs = loader.load()

print(docs)