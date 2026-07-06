from langchain.agents import initialize_agent, AgentType, load_tools
from langchain_openai import ChatOpenAI
from langchain.agents import tool
from datetime import date

@tool
def time(text: str) -> str:
    """返回今天的日期。用于任何与获取今天日期相关的问题。
    该函数的输入应始终为空字符串，且它始终返回今天的日期。
    任何与日期相关的计算应在此函数之外完成。
    """
    return str(date.today())
 
llm = ChatOpenAI(
    model="qwen2.5-72b-instruct",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
# 加载常用工具，例如数学计算和维基百科
tools = load_tools(["llm-math"], llm=llm)

# 创建并初始化智能体Agent
agent = initialize_agent(
    tools=tools+[time],
    llm=llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True
)
response = agent.invoke("今天是星期几,20*3是多少")

print(response['output'])