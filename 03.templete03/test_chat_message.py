from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate([
    ("system", "你是我的私人助理"),
    ("user", "今天是星期{day}")
])
print (prompt_template)
print ("-"*20)
result=prompt_template.invoke({"day":"三"})
print (result)