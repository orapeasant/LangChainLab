from langchain_core.messages import SystemMessage,HumanMessage
# Message 直接拼接.
result=SystemMessage(content="你是我的私人助理") + HumanMessage(content="今天的天气不太好")
print (result)
print (type(result))
# 返回类型.
# ChatPromptTemplate(input_variables=[], messages=[SystemMessage(content='你是我的私人助理'), HumanMessage(content='今天的天气不太好')])
# 字符串拼接.
#SystemMessage(content="你是我的私人助理") + "今天是星期{day}"
# 返回类型.
# ChatPromptTemplate(input_variables=['day'], messages=[SystemMessage(content='你是我的私人助理'), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['day'], template='今天是星期{day}'))])