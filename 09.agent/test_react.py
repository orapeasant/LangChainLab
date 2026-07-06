import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    model="qwen2.5-32b-instruct",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
# 加载工具
 
os.environ["serpapi_api_key"] = "VyrRp96CkMsLTWirT1Bpfu3S"
 

# 定义 tools
from langchain.agents import load_tools
tools = load_tools(["serpapi"])

from langchain.agents import initialize_agent
from langchain.agents import AgentType
# 工具加载后都需要初始化，verbose 参数为 True，会打印全部的执行详情
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
# 运行 agent
agent.run("今天的日期是什么? 历史上的今天发生了什么大事?用中文回答")
 