from dotenv import load_dotenv
from openai import OpenAI
import os

# 加载 .env 文件
load_dotenv()

with open("test.md", "r", encoding="utf-8") as file:
    markdown_content = file.read()

# 构造 GPT 提示
prompt = f"""
以下是从 PDF 转换而来的 Markdown 文本，其中每行可能存在换行符并被错误分割。
请你根据上下文和语言逻辑，智能地将段落合并，保留章节标题和格式，输出整理后的 Markdown 内容。

原始内容：
{markdown_content}

请合并以上内容，逐段翻译为中文，并保留原文格式。要求输出为对照 Markdown 文本：
- 每段原文后插入对应的中文翻译。
- 原文和译文分开显示，译文用空行分隔。
"""

# 获取 API 密钥
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": prompt},
    ],
    stream=False
)

# 提取模型返回结果
merged_markdown = response.choices[0].message.content

# 将合并后的内容写入输出文件
with open("test_output.md", "w", encoding="utf-8") as file:
    file.write(merged_markdown)

print(f"Markdown 文件已成功合并并保存到：{"test_output.md"}")

# print(response.choices[0].message.content)