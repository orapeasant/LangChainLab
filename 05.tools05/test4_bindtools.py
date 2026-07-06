import io
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field
 
from dashscope import Application
from langchain_core.tools import tool
#做了互联网搜索，获得天气
@tool
def search_weather(query):
    """
    根据时间和地点查询天气
    """
    response = Application.call(api_key="sk-6790bcf8821e466bb015d5d297c413d4",app_id='2670dff3ae114560a1cda9b81c652981',prompt=query )
    content=response.output.text
    return content
available_tools = {"search_weather": search_weather }
#构建大模型
llm = ChatOpenAI(
    model="qwen2.5-72b-instruct",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
#提供一组非常好的提示词，用来描述工具
#并且会对输出进行解析，让工具的调用结构化。
llm_with_tools = llm.bind_tools([search_weather])
query = "北京今天的天气怎么样？"
messages=[HumanMessage(query)]

#把绑定上工具的内容作为提示词传给大模型
#函数本身的实现过程，不进入大模型
output  = llm_with_tools.invoke(messages)
 
messages.append(output)
#写成循环的原因，是有可能调用几个工具
for tool_call in output.tool_calls:
    selected_tool = available_tools[tool_call["name"].lower()]
    #真实的进入函数内部进行调用
    tool_msg = selected_tool.invoke(tool_call)
    messages.append(tool_msg)
new_output = llm_with_tools.invoke(messages)
print(new_output.content)
 