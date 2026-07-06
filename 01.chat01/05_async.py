from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from transformers import AutoTokenizer

import time
import asyncio

llm=ChatOpenAI(
    model="llama3.1",
    base_url="https://llm.adirontechs.com/v1",
    api_key="asf"
)

messages=[
    HumanMessage(content="Hi, what are you doing?")
]
async def async_generate(llm):
    resp = await llm.agenerate([messages])  
    print(resp.generations[0][0].text)  
    
async def generate_concurrently():
    tasks=[async_generate(llm) for _ in range(10)]
    await asyncio.gather(*tasks)
asyncio.run(generate_concurrently())    