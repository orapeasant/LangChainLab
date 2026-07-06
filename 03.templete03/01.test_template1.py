from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

llm=ChatOpenAI(
    model="llama3.1",
    base_url='https://llm.adirontechs.com/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)

prompt_template=PromptTemplate(
    input_variables=["day"],
    template="你好,今天是星期{day}，后天是星期几?"
)

print(prompt_template)
prompt_string=prompt_template.invoke({"day":"周五"})   
print(prompt_string)    
result= llm.invoke(prompt_string)
print(result)

print("\n")
prompt_template=ChatPromptTemplate(
    input_variables=[],
    messages=[SystemMessage(content="you are my private asisstant"),HumanMessage(content="who is donald trump")]
)
prompt_string=prompt_template.invoke({})  

result= llm.invoke(prompt_string)
print(result)
