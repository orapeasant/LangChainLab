from langchain_core.messages import SystemMessage, HumanMessage

result = SystemMessage(content="you are my assistant")+HumanMessage(content="the weather is not good today")
print(result)
print(type(result))