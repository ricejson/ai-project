# pip install beautifulsoup4
import bs4
from langchain_community.document_loaders import WebBaseLoader

page_url = "https://zh.wikipedia.org/wiki/黑神话：悟空"
docs = WebBaseLoader(
    web_paths=[page_url],
    bs_kwargs={
        "parse_only": bs4.SoupStrainer(id="bodyContent"), # 只提取id为bodyContent
    },
    bs_get_text_kwargs={
        "separator": "|", # 分隔符
        "strip": True, # 去除前后空串
    }
).load()

print(docs)