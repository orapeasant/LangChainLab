from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from transformers import AutoTokenizer
import time
import asyncio
llm = ChatOpenAI(
    model="qwen3",
    base_url='https://llm.adirontechs.com/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
 

messages2 = [
        HumanMessage(content="你好啊，你在干嘛")
] 

# 定义异步函数async_generate，该函数接收一个llm参数
async def async_generate(llm):
    # 调用OpenAI类的agenerate方法，传入字符串列表["Hello, how are you?"]并等待响应
    resp = await llm.agenerate([messages2])
    # 打印响应结果的生成文本
    print(resp.generations[0][0].text)


# 定义异步函数generate_concurrently
async def generate_concurrently():
    # 创建包含10个async_generate任务的列表
    tasks = [async_generate(llm) for _ in range(10)]
    # 并发执行任务
    await asyncio.gather(*tasks)
asyncio.run(generate_concurrently())