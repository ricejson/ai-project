# brew list poppler
from pdf2image import convert_from_path
import os
output_path = "temp_images"
if not os.path.exists(output_path):
    os.mkdir(output_path)
# 将 pdf 文件转换为图片
images = convert_from_path("../../data/黑神话悟空/黑神话悟空.pdf")
image_paths = []
for i, image in enumerate(images):
    image_path = os.path.join("temp_images", f"page{i+1}.jpg")
    image.save(image_path)
    image_paths.append(image_path)
print(f"成功转换{len(image_paths)}张图片")

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI(
    base_url="https://api.minimaxi.com/v1",
    api_key=os.getenv("MINIMAX_API_KEY"),
)

print("\n开始分析图片")
results = []
import base64
for image_path in image_paths:
    with open(image_path, "rb") as f:
        base64_image = base64.b64encode(f.read()).decode("utf-8")
        resp = client.chat.completions.create(
            model="MiniMax-M3",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "请详细描述这张图片的内容，包括标题，正文和图片内容"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        },
                    ]
                }
            ],
        )
        results.append(resp.choices[0].message.content)
# 转换为Document
from langchain_core.documents import Document
docs = [
    Document(
        page_content= res,
        metadata={"source": "../../data/黑神话悟空/黑神话悟空.pdf", "page_number": i+1}
    )
    for i, res in enumerate(results)
]
print("\n分析结果")
for doc in docs:
    print(f"内容: {doc.page_content}, 元数据: {doc.metadata}")