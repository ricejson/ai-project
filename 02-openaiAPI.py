import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("V3_API_KEY")

print(f"api_key: {api_key}")

client = OpenAI(
    base_url="https://api.vveai.com/v1",
    api_key=api_key,
)

# 输出结果
response = client.chat.completions.create(
    model="o3-mini",
    messages=[
        {"role": "user", "content": "你好"}
    ]
)

print(response.choices[0].message.content)

