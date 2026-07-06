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

#网络服务接口，对langchain是透明的
#对于真正的网络接口，MCP就这里起到作用了，标准化
@tool
def add(a: int, b: int) -> str:
    """Add two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return "{}+{}的结果是{}".format(a,b,a + b)

@tool
def multiply(a: int, b: int) -> str:
    """Multiply two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return "{}*{}的结果是{}".format(a,b,a*b)



available_tools = {"multiply": multiply,"add":add }
#构建大模型
llm = ChatOpenAI(
    model="qwen2.5-72b-instruct",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
llm_with_tools = llm.bind_tools([add, multiply])
query = "(6+3)*(2+5)是多少"
messages=[HumanMessage(query)]
i=1
while True:
    print ("第{}次".format(i))
    output  = llm_with_tools.invoke(messages)
    print("大模型输出",output)
    messages.append(output)
    if len(output.tool_calls)==0:
        break
    print (output.tool_calls)
    print ("---"*20)
    for tool_call in output.tool_calls:
        selected_tool = available_tools[tool_call["name"].lower()]
        tool_msg = selected_tool.invoke(tool_call)
        print ("工具的输出",tool_msg)
        messages.append(tool_msg)
    i+=1
    print ("---"*20)
    print ("第{}轮的输入".format(i),messages)
 
print (messages[-1].content)

 
 