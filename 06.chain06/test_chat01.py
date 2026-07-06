import io

from langchain_core.messages import AnyMessage
from pydantic import BaseModel, Field
import jieba
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableSequence

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个知识渊博的助手，能准确回答各种问题。"),
    ("human", "{question}")
])
from langchain_openai import ChatOpenAI 
llm = ChatOpenAI(
    model="qwen2.5-32b-instruct",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
#输入的构建
query=prompt.invoke("你好，你是谁")
#大模型的调用
response=llm.invoke(query)
#结果的解析
result=response.content
print  (result)