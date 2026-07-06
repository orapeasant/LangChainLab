from langchain.text_splitter import RecursiveCharacterTextSplitter

# 示例文本
text = "这是一段较长的文本，我们将使用 LangChain 来对其进行分割。分割文本有助于处理大段内容，例如在进行文档分析、问答系统等场景中非常有用。"

# 初始化文本分割器
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=20,  # 每个文本块的最大字符数
    chunk_overlap=5,  # 相邻文本块之间的重叠字符数
    separators=["，","。"],
    keep_separator="end"
)

# 分割文本
texts = text_splitter.split_text(text)

# 打印分割后的文本块
for i, chunk in enumerate(texts):
    print(f"Chunk {i + 1}: {chunk}")
    