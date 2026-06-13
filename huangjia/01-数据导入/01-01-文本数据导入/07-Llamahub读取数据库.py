# pip install llama-index-readers-database
# pip install pymysql
# pip install mysqlclient
# brew install libmysqlclient-dev
# brew install python3-dev
from llama_index.readers.database import DatabaseReader

reader = DatabaseReader(
    scheme="mysql+pymysql",
    host="localhost",
    port="13316",
    user="root",
    password="root",
    dbname="exampledb"
)

query = "SELECT * FROM game_scenes"
docs = reader.load_data(query)
print(f"从数据库加载的文档数目: {len(docs)}")
print(docs)
