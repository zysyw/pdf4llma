import pymupdf # imports the pymupdf library
doc = pymupdf.open("694.pdf") # open a document
for page_number, page in enumerate(doc, start=1):
  text = page.get_text()  # 提取页面中的纯文本
  print(f"--- Page {page_number} ---")  # 打印页码分隔符
  print(text)  # 输出页面内容