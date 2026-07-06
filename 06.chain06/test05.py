from langchain.schema.runnable import RunnableSequence
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 初始化大语言模型
from langchain_openai import ChatOpenAI 
llm = ChatOpenAI(
    model="qwen2.5-32b-instruct",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
# 1. 主题 → 标题生成链
title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="为以下主题创建一个吸引人的博客标题（不超过20字）：\n主题：{topic}\n标题："
)
title_chain = LLMChain(llm=llm, prompt=title_prompt, output_key="title")
#{"title":"人工智能发展史"}
# 2. 标题 → 大纲生成链
outline_prompt = PromptTemplate(
    input_variables=["title"],
    template="为以下标题创建一个结构化的博客大纲：\n标题：{title}\n大纲："
)
outline_chain = LLMChain(llm=llm, prompt=outline_prompt, output_key="outline")
#{"outline":"第一....第二..."}
# 3. 标题+大纲 → 内容生成链
content_prompt = PromptTemplate(
    input_variables=["title", "outline"],
    template="""根据标题和大纲撰写一篇详细的博客文章：
标题：{title}
大纲：{outline}

博客正文：""")
content_chain = LLMChain(llm=llm, prompt=content_prompt, output_key="content")
 
blog_chain ={"topic": lambda x: x["topic"]} | title_chain|{"title": lambda x: x["title"]} | outline_chain|{"title": lambda x: x["title"], "outline": lambda x: x["outline"]} | content_chain

# 执行链
result = blog_chain.invoke({"topic": "人工智能在医疗领域的应用"})

# 打印结果
print("标题:", result["title"])
print("\n大纲:", result["outline"])
print("\n内容:", result["content"])