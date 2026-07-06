import io
from langchain_openai import ChatOpenAI
from langchain_core.messages import AnyMessage,HumanMessage
from pydantic import BaseModel, Field
import jieba
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableSequence
from typing import Optional    
from typing_extensions import TypedDict
from dashscope import Application
from langchain_core.tools import tool
 
 
#构建大模型
llm = ChatOpenAI(
    model="qwen2.5-72b-instruct",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
 
query = "有函数searhweather,它的作用根据时间和地点查询天气。根据现有函数，回答下面问题，请问北京今天天气"
 
output  = llm.invoke(query)
print (output)
 